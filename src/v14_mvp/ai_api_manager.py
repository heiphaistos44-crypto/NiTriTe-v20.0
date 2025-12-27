#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire d'APIs IA - Multi-API avec fallback automatique
Support: DeepSeek, Groq, HuggingFace, OpenRouter, Gemini
Toutes les APIs sont gratuites ou ont un tier gratuit généreux
"""

import requests
import json
from typing import Optional, Dict, List, Tuple, Generator

# Import logger avec fallback (compatibilité multi-contexte)
try:
    from v14_mvp.logger_system import logger
except ImportError:
    try:
        from logger_system import logger
    except ImportError:
        from .logger_system import logger

# Essayer d'importer google-generativeai
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

# Import Ollama Manager
try:
    try:
        from v14_mvp.ai_ollama_manager import get_ollama_manager
    except ImportError:
        try:
            from ai_ollama_manager import get_ollama_manager
        except ImportError:
            from .ai_ollama_manager import get_ollama_manager
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    logger.warning("API_Manager", "ai_ollama_manager non disponible")

# Import Smart Cache
try:
    try:
        from v14_mvp.ai_cache_manager import get_cache_manager
    except ImportError:
        try:
            from ai_cache_manager import get_cache_manager
        except ImportError:
            from .ai_cache_manager import get_cache_manager
    CACHE_AVAILABLE = True
except ImportError:
    CACHE_AVAILABLE = False
    logger.warning("API_Manager", "ai_cache_manager non disponible")


class APIManager:
    """Gestionnaire multi-API avec fallback automatique + Ollama local"""

    def __init__(self):
        # Ollama Manager (priorité absolue si disponible)
        self.ollama_manager = None
        if OLLAMA_AVAILABLE:
            self.ollama_manager = get_ollama_manager()

        # Smart Cache Manager
        self.cache_manager = None
        if CACHE_AVAILABLE:
            self.cache_manager = get_cache_manager()

        # Configuration des APIs par priorité
        # Priority 0 = Ollama (local, gratuit, privé)
        # Priority 1-13 = APIs cloud
        self.api_configs = {
            "ollama": {
                "name": "Ollama (Local)",
                "models": [],  # Rempli dynamiquement
                "free": True,
                "performance": "★★★★★ (Gratuit, Privé, Offline)",
                "priority": 0,  # PRIORITÉ LA PLUS ÉLEVÉE
                "enabled": False,  # Activé si Ollama détecté
                "api_key": "local"  # Pas besoin de clé
            },
            "deepseek": {
                "name": "DeepSeek",
                "endpoint": "https://api.deepseek.com/v1/chat/completions",
                "model": "deepseek-chat",
                "free": True,
                "performance": "GPT-4 level",
                "priority": 1,
                "enabled": False,
                "api_key": ""
            },
            "groq": {
                "name": "Groq",
                "endpoint": "https://api.groq.com/openai/v1/chat/completions",
                "models": [
                    "llama-3.3-70b-versatile",  # Le plus puissant
                    "mixtral-8x7b-32768",
                    "llama-3.1-70b-versatile"
                ],
                "free": True,
                "performance": "Excellent + Ultra-rapide",
                "priority": 2,
                "enabled": False,
                "api_key": ""
            },
            "huggingface": {
                "name": "HuggingFace Inference",
                "endpoint": "https://api-inference.huggingface.co/models",
                "models": [
                    "Qwen/Qwen2.5-72B-Instruct",
                    "meta-llama/Llama-3.1-70B-Instruct",
                    "mistralai/Mixtral-8x7B-Instruct-v0.1"
                ],
                "free": True,
                "performance": "Très bon",
                "priority": 3,
                "enabled": False,
                "api_key": ""
            },
            "openrouter": {
                "name": "OpenRouter",
                "endpoint": "https://openrouter.ai/api/v1/chat/completions",
                "models_free": [
                    "google/gemma-2-9b-it:free",
                    "meta-llama/llama-3.1-8b-instruct:free",
                    "microsoft/phi-3-medium-128k-instruct:free"
                ],
                "free": True,
                "performance": "Bon (fallback)",
                "priority": 4,
                "enabled": False,
                "api_key": ""
            },
            "gemini": {
                "name": "Gemini",
                "models": [
                    "gemini-1.5-pro",     # Plus puissant (gratuit 50 req/jour)
                    "gemini-1.5-flash",   # Plus rapide
                    "gemini-2.0-flash-exp"  # Experimental (très rapide)
                ],
                "free": True,
                "performance": "Excellent",
                "priority": 5,
                "enabled": False,
                "api_key": ""
            },
            "openai": {
                "name": "OpenAI (GPT-3.5/4)",
                "endpoint": "https://api.openai.com/v1/chat/completions",
                "models": [
                    "gpt-3.5-turbo",      # Gratuit avec crédits ($5 initial)
                    "gpt-4o-mini",        # GPT-4 optimisé, moins cher
                    "gpt-4-turbo"         # Le plus puissant
                ],
                "free": "5$ crédits gratuits",
                "performance": "Top tier (GPT-4 level)",
                "priority": 6,
                "enabled": False,
                "api_key": ""
            },
            "mistral": {
                "name": "Mistral AI",
                "endpoint": "https://api.mistral.ai/v1/chat/completions",
                "models": [
                    "mistral-small-latest",   # Gratuit tier
                    "mistral-medium-latest",
                    "mistral-large-latest"
                ],
                "free": True,
                "performance": "Très bon (style Copilot)",
                "priority": 7,
                "enabled": False,
                "api_key": ""
            },
            "together": {
                "name": "Together AI",
                "endpoint": "https://api.together.xyz/v1/chat/completions",
                "models": [
                    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
                    "mistralai/Mixtral-8x7B-Instruct-v0.1",
                    "Qwen/Qwen2.5-72B-Instruct-Turbo"
                ],
                "free": True,
                "performance": "Excellent (5$ crédits gratuits)",
                "priority": 8,
                "enabled": False,
                "api_key": ""
            },
            "cohere": {
                "name": "Cohere",
                "endpoint": "https://api.cohere.ai/v1/chat",
                "models": [
                    "command-r-plus",
                    "command-r",
                    "command-light"
                ],
                "free": True,
                "performance": "Très bon (1000 req/mois gratuit)",
                "priority": 9,
                "enabled": False,
                "api_key": ""
            },
            "ai21": {
                "name": "AI21 Labs",
                "endpoint": "https://api.ai21.com/studio/v1/chat/completions",
                "models": [
                    "jamba-1.5-mini",
                    "jamba-1.5-large"
                ],
                "free": True,
                "performance": "Bon (10K crédits gratuits)",
                "priority": 10,
                "enabled": False,
                "api_key": ""
            },
            "replicate": {
                "name": "Replicate",
                "endpoint": "https://api.replicate.com/v1/predictions",
                "models": [
                    "meta/llama-2-70b-chat",
                    "meta/llama-3-70b-instruct",
                    "mistralai/mixtral-8x7b-instruct-v0.1"
                ],
                "free": True,
                "performance": "Bon (crédits gratuits mensuels)",
                "priority": 11,
                "enabled": False,
                "api_key": ""
            },
            "perplexity": {
                "name": "Perplexity AI",
                "endpoint": "https://api.perplexity.ai/chat/completions",
                "models": [
                    "llama-3.1-sonar-small-128k-online",
                    "llama-3.1-sonar-large-128k-online"
                ],
                "free": True,
                "performance": "Excellent (5$ crédits gratuits)",
                "priority": 12,
                "enabled": False,
                "api_key": ""
            },
            "anthropic": {
                "name": "Anthropic Claude",
                "endpoint": "https://api.anthropic.com/v1/messages",
                "models": [
                    "claude-3-5-sonnet-20241022",
                    "claude-3-5-haiku-20241022",
                    "claude-3-opus-20240229"
                ],
                "free": "5$ crédits gratuits",
                "performance": "Top tier (meilleur raisonnement)",
                "priority": 13,
                "enabled": False,
                "api_key": ""
            },
            "fireworks": {
                "name": "Fireworks AI",
                "endpoint": "https://api.fireworks.ai/inference/v1/chat/completions",
                "models": [
                    "accounts/fireworks/models/llama-v3p1-70b-instruct",
                    "accounts/fireworks/models/mixtral-8x7b-instruct",
                    "accounts/fireworks/models/qwen2p5-72b-instruct"
                ],
                "free": True,
                "performance": "Très bon (1$ crédits gratuits)",
                "priority": 14,
                "enabled": False,
                "api_key": ""
            },
            "novita": {
                "name": "Novita AI",
                "endpoint": "https://api.novita.ai/v3/openai/chat/completions",
                "models": [
                    "meta-llama/llama-3.1-70b-instruct",
                    "mistralai/mixtral-8x7b-instruct-v0.1"
                ],
                "free": True,
                "performance": "Bon (0.5$ crédits gratuits)",
                "priority": 15,
                "enabled": False,
                "api_key": ""
            },
            "deepinfra": {
                "name": "DeepInfra",
                "endpoint": "https://api.deepinfra.com/v1/openai/chat/completions",
                "models": [
                    "meta-llama/Meta-Llama-3.1-70B-Instruct",
                    "mistralai/Mixtral-8x7B-Instruct-v0.1",
                    "Qwen/Qwen2.5-72B-Instruct"
                ],
                "free": True,
                "performance": "Excellent (crédits gratuits généreux)",
                "priority": 16,
                "enabled": False,
                "api_key": ""
            },
            "lepton": {
                "name": "Lepton AI",
                "endpoint": "https://llama3-1-70b.lepton.run/api/v1/chat/completions",
                "models": [
                    "llama3-1-70b",
                    "mixtral-8x7b"
                ],
                "free": True,
                "performance": "Bon (10$ crédits gratuits)",
                "priority": 17,
                "enabled": False,
                "api_key": ""
            },
            "anyscale": {
                "name": "Anyscale",
                "endpoint": "https://api.endpoints.anyscale.com/v1/chat/completions",
                "models": [
                    "meta-llama/Meta-Llama-3.1-70B-Instruct",
                    "mistralai/Mixtral-8x7B-Instruct-v0.1"
                ],
                "free": True,
                "performance": "Très bon (10$ crédits gratuits)",
                "priority": 18,
                "enabled": False,
                "api_key": ""
            },
            "voyage": {
                "name": "Voyage AI",
                "endpoint": "https://api.voyageai.com/v1/chat/completions",
                "models": [
                    "llama-3-70b-chat",
                    "mixtral-8x7b-instruct"
                ],
                "free": True,
                "performance": "Bon (crédits gratuits initiaux)",
                "priority": 19,
                "enabled": False,
                "api_key": ""
            },
            "nebius": {
                "name": "Nebius AI Studio",
                "endpoint": "https://api.studio.nebius.ai/v1/chat/completions",
                "models": [
                    "meta-llama/Meta-Llama-3.1-70B-Instruct",
                    "Qwen/Qwen2.5-72B-Instruct"
                ],
                "free": True,
                "performance": "Excellent (15$ crédits gratuits)",
                "priority": 20,
                "enabled": False,
                "api_key": ""
            }
        }

        self.last_successful_api = None
        self.request_timeout = 30  # 30 secondes max par requête

        # 🔑 AUTO-CHARGEMENT des clés depuis config/api_keys.json
        self._load_api_keys_from_file()

        # 🚀 AUTO-ACTIVATION d'Ollama si disponible
        if self.ollama_manager and self.ollama_manager.ollama_installed:
            self.api_configs["ollama"]["enabled"] = True
            self.api_configs["ollama"]["models"] = self.ollama_manager.available_models
            logger.info("API_Manager", f"✓ Ollama activé avec {len(self.ollama_manager.available_models)} modèles")
        else:
            logger.info("API_Manager", "Ollama non disponible - Utilisez les APIs cloud ou installez Ollama")

    def _load_api_keys_from_file(self):
        """Charge automatiquement les clés API depuis config/api_keys.json"""
        import os

        # Chercher le fichier de config
        possible_paths = [
            "config/api_keys.json",
            "../config/api_keys.json",
            "../../config/api_keys.json",
            os.path.join(os.path.dirname(__file__), "..", "..", "config", "api_keys.json")
        ]

        config_file = None
        for path in possible_paths:
            if os.path.exists(path):
                config_file = path
                break

        if not config_file:
            logger.info("APIManager", "Aucun fichier api_keys.json trouvé - utilise le script OBTENIR_CLES_2MIN.bat")
            return

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                keys_config = json.load(f)

            # Charger chaque clé
            loaded_count = 0
            for api_name, config in keys_config.items():
                if api_name.startswith("_"):  # Skip instructions
                    continue

                if isinstance(config, dict) and "api_key" in config:
                    api_key = config["api_key"]
                    if api_key and api_key != "VIDE" and not api_key.startswith("XXX"):
                        self.set_api_key(api_name, api_key)
                        loaded_count += 1

            if loaded_count > 0:
                logger.info("APIManager", f"✅ {loaded_count} clés API chargées automatiquement!")
            else:
                logger.info("APIManager", "⚠️ Fichier api_keys.json vide - utilise OBTENIR_CLES_2MIN.bat")

        except Exception as e:
            logger.error("APIManager", f"Erreur chargement clés: {e}")

    def set_api_key(self, api_name: str, api_key: str):
        """Définir la clé API pour un service"""
        if api_name in self.api_configs:
            self.api_configs[api_name]["api_key"] = api_key
            self.api_configs[api_name]["enabled"] = bool(api_key)
            logger.info("APIManager", f"Clé API configurée pour {api_name}")
        else:
            logger.warning("APIManager", f"API inconnue: {api_name}")

    def get_enabled_apis(self) -> List[str]:
        """Retourne la liste des APIs activées, triées par priorité"""
        enabled = [
            (name, config["priority"])
            for name, config in self.api_configs.items()
            if config["enabled"] and config["api_key"]
        ]
        # Trier par priorité (1 = plus haute)
        enabled.sort(key=lambda x: x[1])
        return [name for name, _ in enabled]

    def query(self, user_message: str, system_prompt: str = "", temperature: float = 0.9, max_tokens: int = 8000, use_cache: bool = True) -> Tuple[Optional[str], Optional[str]]:
        """
        Interroge les APIs dans l'ordre de priorité avec fallback automatique
        Vérifie d'abord le cache, puis Ollama local, puis APIs cloud

        Returns:
            (response_text, api_used) ou (None, None) si échec total
        """
        # === ÉTAPE 1: VÉRIFIER LE CACHE ===
        if use_cache and self.cache_manager:
            cached_response = self.cache_manager.get(user_message)
            if cached_response:
                logger.info("APIManager", "✓ Réponse trouvée dans le cache")
                return (cached_response, "cache")

        # === ÉTAPE 2: ESSAYER OLLAMA (LOCAL) ===
        if self.ollama_manager and self.ollama_manager.ollama_installed:
            if self.ollama_manager.available_models:
                try:
                    logger.info("APIManager", "Tentative avec Ollama (local)...")
                    model = self.ollama_manager.auto_select_model("technical")

                    # Construire le prompt complet
                    full_prompt = f"{system_prompt}\n\n{user_message}" if system_prompt else user_message

                    # Query Ollama (non-streaming pour compatibilité)
                    result = self.ollama_manager.query_local(
                        full_prompt,
                        model=model,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=False
                    )

                    if result:
                        logger.info("APIManager", f"✓ Succès avec Ollama ({model})")

                        # Mettre en cache
                        if use_cache and self.cache_manager:
                            self.cache_manager.put(user_message, result, model="ollama:" + model)

                        self.last_successful_api = "ollama"
                        return (result, "ollama")

                except Exception as e:
                    logger.error("APIManager", f"Erreur Ollama: {e}")
                    # Continuer avec APIs cloud

        # === ÉTAPE 3: ESSAYER APIS CLOUD ===
        enabled_apis = self.get_enabled_apis()

        if not enabled_apis and not (self.ollama_manager and self.ollama_manager.ollama_installed):
            return ("Aucune API configurée et Ollama non disponible. Veuillez configurer au moins une API ou installer Ollama.", None)

        # Essayer chaque API dans l'ordre de priorité
        for api_name in enabled_apis:
            # Skip Ollama car déjà essayé
            if api_name == "ollama":
                continue

            try:
                logger.info("APIManager", f"Tentative avec {api_name}...")

                if api_name == "deepseek":
                    result = self._query_deepseek(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "groq":
                    result = self._query_groq(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "huggingface":
                    result = self._query_huggingface(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "openrouter":
                    result = self._query_openrouter(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "gemini":
                    result = self._query_gemini(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "openai":
                    result = self._query_openai(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "mistral":
                    result = self._query_mistral(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "together":
                    result = self._query_together(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "cohere":
                    result = self._query_cohere(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "ai21":
                    result = self._query_ai21(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "replicate":
                    result = self._query_replicate(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "perplexity":
                    result = self._query_perplexity(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "anthropic":
                    result = self._query_anthropic(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "fireworks":
                    result = self._query_fireworks(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "novita":
                    result = self._query_novita(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "deepinfra":
                    result = self._query_deepinfra(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "lepton":
                    result = self._query_lepton(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "anyscale":
                    result = self._query_anyscale(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "voyage":
                    result = self._query_voyage(user_message, system_prompt, temperature, max_tokens)
                elif api_name == "nebius":
                    result = self._query_nebius(user_message, system_prompt, temperature, max_tokens)
                else:
                    continue

                if result:
                    self.last_successful_api = api_name
                    logger.info("APIManager", f"Succès avec {api_name}")

                    # Mettre en cache la réponse cloud
                    if use_cache and self.cache_manager:
                        self.cache_manager.put(user_message, result, model=api_name)

                    return (result, api_name)

            except Exception as e:
                logger.error("APIManager", f"Erreur avec {api_name}: {str(e)}")
                continue

        # Toutes les APIs ont échoué
        return (f"Toutes les APIs ont échoué. APIs testées: {', '.join(enabled_apis)}", None)

    def _query_deepseek(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger DeepSeek API (compatible OpenAI)"""
        config = self.api_configs["deepseek"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        payload = {
            "model": config["model"],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }

        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]

        return None

    def _query_groq(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Groq API (ultra-rapide)"""
        config = self.api_configs["groq"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        # Utiliser le modèle le plus puissant
        model = config["models"][0]  # llama-3.3-70b-versatile

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }

        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]

        return None

    def _query_huggingface(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger HuggingFace Inference API"""
        config = self.api_configs["huggingface"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        # Construire le prompt complet
        full_prompt = ""
        if system_prompt:
            full_prompt = f"<|system|>\n{system_prompt}\n<|user|>\n{user_message}\n<|assistant|>"
        else:
            full_prompt = f"<|user|>\n{user_message}\n<|assistant|>"

        # Utiliser le modèle le plus puissant
        model = config["models"][0]  # Qwen/Qwen2.5-72B-Instruct
        endpoint = f"{config['endpoint']}/{model}"

        payload = {
            "inputs": full_prompt,
            "parameters": {
                "temperature": temperature,
                "max_new_tokens": max_tokens,
                "return_full_text": False
            }
        }

        response = requests.post(
            endpoint,
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0].get("generated_text", "")
            elif isinstance(data, dict):
                return data.get("generated_text", "")

        return None

    def _query_openrouter(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger OpenRouter API (fallback avec modèles gratuits)"""
        config = self.api_configs["openrouter"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://nitrite.app",  # Requis par OpenRouter
            "X-Title": "NiTriTe AI Agent"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        # Utiliser le premier modèle gratuit
        model = config["models_free"][0]  # google/gemma-2-9b-it:free

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]

        return None

    def _query_gemini(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Gemini API (Google)"""
        if not GENAI_AVAILABLE:
            return None

        config = self.api_configs["gemini"]

        try:
            genai.configure(api_key=config['api_key'])

            # Utiliser le premier modèle (gemini-1.5-pro)
            model_name = config["models"][0]

            model = genai.GenerativeModel(
                model_name,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    top_p=0.95,
                    top_k=40,
                )
            )

            # Construire le prompt complet
            full_prompt = ""
            if system_prompt:
                full_prompt = f"{system_prompt}\n\n**QUESTION:** {user_message}\n\n**RÉPONSE:**"
            else:
                full_prompt = user_message

            response = model.generate_content(full_prompt)

            if response and response.text:
                return response.text

        except Exception as e:
            logger.error("APIManager", f"Erreur Gemini: {str(e)}")

        return None

    def _query_openai(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger OpenAI API (GPT-3.5/GPT-4)"""
        config = self.api_configs["openai"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        # Utiliser GPT-3.5-turbo par défaut (gratuit avec crédits)
        model = config["models"][0]  # gpt-3.5-turbo

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]

        return None

    def _query_mistral(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Mistral AI API"""
        config = self.api_configs["mistral"]

        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        # Utiliser mistral-small par défaut (gratuit)
        model = config["models"][0]  # mistral-small-latest

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        response = requests.post(
            config["endpoint"],
            headers=headers,
            json=payload,
            timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]

        return None

    def get_api_status(self) -> Dict[str, dict]:
        """Retourne le statut de toutes les APIs"""
        status = {}
        for name, config in self.api_configs.items():
            status[name] = {
                "name": config["name"],
                "enabled": config["enabled"],
                "has_key": bool(config["api_key"]),
                "performance": config["performance"],
                "priority": config["priority"],
                "free": config.get("free", True)
            }
        return status

    def test_api(self, api_name: str) -> Tuple[bool, str]:
        """Tester une API spécifique"""
        if api_name not in self.api_configs:
            return (False, f"API inconnue: {api_name}")

        if not self.api_configs[api_name]["enabled"]:
            return (False, f"{api_name} n'est pas activée (clé API manquante)")

        try:
            test_message = "Réponds simplement 'OK' si tu me reçois."
            result, _ = self.query(test_message, "")

            if result and "OK" in result.upper():
                return (True, f"{api_name} fonctionne correctement!")
            else:
                return (False, f"{api_name} a répondu mais pas comme attendu")

        except Exception as e:
            return (False, f"Erreur de test {api_name}: {str(e)}")

    def _query_together(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Together AI API"""
        config = self.api_configs["together"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_cohere(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Cohere API"""
        config = self.api_configs["cohere"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": config["models"][0],
            "message": user_message,
            "preamble": system_prompt if system_prompt else None,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "text" in data:
                return data["text"]
        return None

    def _query_ai21(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger AI21 Labs API"""
        config = self.api_configs["ai21"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_replicate(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Replicate API"""
        config = self.api_configs["replicate"]
        headers = {
            "Authorization": f"Token {config['api_key']}",
            "Content-Type": "application/json"
        }
        prompt = f"{system_prompt}\n\n{user_message}" if system_prompt else user_message
        payload = {
            "version": config["models"][0],
            "input": {
                "prompt": prompt,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 201:
            data = response.json()
            if "output" in data:
                return "".join(data["output"]) if isinstance(data["output"], list) else data["output"]
        return None

    def _query_perplexity(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Perplexity AI API"""
        config = self.api_configs["perplexity"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_anthropic(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Anthropic Claude API"""
        config = self.api_configs["anthropic"]
        headers = {
            "x-api-key": config['api_key'],
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        payload = {
            "model": config["models"][0],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [{"role": "user", "content": user_message}]
        }
        if system_prompt:
            payload["system"] = system_prompt
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "content" in data and len(data["content"]) > 0:
                return data["content"][0]["text"]
        return None

    def _query_fireworks(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Fireworks AI API"""
        config = self.api_configs["fireworks"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_novita(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Novita AI API"""
        config = self.api_configs["novita"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_deepinfra(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger DeepInfra API"""
        config = self.api_configs["deepinfra"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_lepton(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Lepton AI API"""
        config = self.api_configs["lepton"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_anyscale(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Anyscale API"""
        config = self.api_configs["anyscale"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_voyage(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Voyage AI API"""
        config = self.api_configs["voyage"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None

    def _query_nebius(self, user_message: str, system_prompt: str, temperature: float, max_tokens: int) -> Optional[str]:
        """Interroger Nebius AI Studio API"""
        config = self.api_configs["nebius"]
        headers = {
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})
        payload = {
            "model": config["models"][0],
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        response = requests.post(config["endpoint"], headers=headers, json=payload, timeout=self.request_timeout)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
        return None
