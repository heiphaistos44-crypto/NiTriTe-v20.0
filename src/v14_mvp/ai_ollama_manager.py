#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ollama Manager - Gestionnaire LLM Local pour NiTriTe V20.0
Support modèles: llama3, mistral, deepseek-r1, phi3, qwen2.5
Offline-first, gratuit, privacy-focused
"""

import subprocess
import json
import requests
import time
from typing import Optional, List, Dict, Generator
from pathlib import Path
from v14_mvp.logger_system import logger


class OllamaManager:
    """Gestionnaire Ollama pour inférence LLM locale"""

    def __init__(self):
        self.base_url = "http://localhost:11434"
        self.available_models = []
        self.recommended_models = {
            "llama3:8b": {
                "name": "Llama 3 8B",
                "size": "4.7 GB",
                "vram": "4 GB",
                "use_case": "Général, rapide",
                "speed": "★★★★★",
                "quality": "★★★★☆"
            },
            "mistral:7b": {
                "name": "Mistral 7B",
                "size": "4.1 GB",
                "vram": "4 GB",
                "use_case": "Technique, précis",
                "speed": "★★★★★",
                "quality": "★★★★★"
            },
            "deepseek-r1:8b": {
                "name": "DeepSeek R1 8B",
                "size": "5.2 GB",
                "vram": "5 GB",
                "use_case": "Raisonnement avancé",
                "speed": "★★★★☆",
                "quality": "★★★★★"
            },
            "phi3:mini": {
                "name": "Phi-3 Mini",
                "size": "2.3 GB",
                "vram": "2 GB",
                "use_case": "Ultra-rapide, CPU-friendly",
                "speed": "★★★★★",
                "quality": "★★★☆☆"
            },
            "qwen2.5:14b": {
                "name": "Qwen 2.5 14B",
                "size": "9.0 GB",
                "vram": "8 GB",
                "use_case": "Meilleur qualité/vitesse",
                "speed": "★★★★☆",
                "quality": "★★★★★"
            }
        }

        self.ollama_installed = self.detect_ollama_installation()
        if self.ollama_installed:
            self.available_models = self.list_available_models()
            logger.info("Ollama", f"Détecté - {len(self.available_models)} modèles locaux disponibles")
        else:
            logger.warning("Ollama", "Non détecté - Support LLM local désactivé")

    def detect_ollama_installation(self) -> bool:
        """Vérifie si Ollama est installé et en cours d'exécution"""
        try:
            # Méthode 1: Tester l'API
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            if response.status_code == 200:
                logger.info("Ollama", "API détectée et fonctionnelle")
                return True
        except requests.exceptions.RequestException:
            pass

        try:
            # Méthode 2: Tester via commande CLI
            result = subprocess.run(
                ["ollama", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                logger.info("Ollama", f"CLI détecté: {version}")

                # Démarrer le service si pas actif
                self.ensure_ollama_running()
                return True
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        logger.warning("Ollama", "Non installé. Téléchargement: https://ollama.ai/download")
        return False

    def ensure_ollama_running(self):
        """S'assure que le service Ollama est actif"""
        try:
            # Tenter de démarrer le service
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
            )
            time.sleep(2)  # Attendre démarrage
            logger.info("Ollama", "Service démarré")
        except Exception as e:
            logger.error("Ollama", f"Erreur démarrage service: {e}")

    def list_available_models(self) -> List[str]:
        """Liste les modèles Ollama installés localement"""
        if not self.ollama_installed:
            return []

        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                models = [model['name'] for model in data.get('models', [])]
                logger.info("Ollama", f"Modèles installés: {', '.join(models) if models else 'Aucun'}")
                return models
        except Exception as e:
            logger.error("Ollama", f"Erreur liste modèles: {e}")

        return []

    def pull_model(self, model_name: str, progress_callback=None) -> bool:
        """
        Télécharge un modèle Ollama

        Args:
            model_name: Nom du modèle (ex: "llama3:8b")
            progress_callback: Fonction callback(status, progress) pour UI

        Returns:
            bool: True si succès
        """
        try:
            logger.info("Ollama", f"Téléchargement {model_name}...")

            # Utiliser l'API streaming pour suivre la progression
            response = requests.post(
                f"{self.base_url}/api/pull",
                json={"name": model_name},
                stream=True,
                timeout=600  # 10 minutes timeout
            )

            total_size = 0
            downloaded = 0

            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    status = data.get('status', '')

                    # Extraire progression
                    if 'total' in data and 'completed' in data:
                        total_size = data['total']
                        downloaded = data['completed']
                        progress_pct = (downloaded / total_size * 100) if total_size > 0 else 0

                        if progress_callback:
                            progress_callback(status, progress_pct)

                        logger.debug("Ollama", f"{status}: {progress_pct:.1f}%")

                    # Vérifier si terminé
                    if status == "success":
                        logger.info("Ollama", f"✓ Modèle {model_name} téléchargé avec succès")
                        self.available_models = self.list_available_models()
                        return True

            return False

        except Exception as e:
            logger.error("Ollama", f"Erreur téléchargement {model_name}: {e}")
            return False

    def delete_model(self, model_name: str) -> bool:
        """Supprime un modèle local pour libérer de l'espace"""
        try:
            response = requests.delete(
                f"{self.base_url}/api/delete",
                json={"name": model_name},
                timeout=10
            )

            if response.status_code == 200:
                logger.info("Ollama", f"Modèle {model_name} supprimé")
                self.available_models = self.list_available_models()
                return True

            return False

        except Exception as e:
            logger.error("Ollama", f"Erreur suppression {model_name}: {e}")
            return False

    def query_local(
        self,
        prompt: str,
        model: str = "llama3:8b",
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        stream: bool = True
    ) -> Generator[str, None, None] | str:
        """
        Interroge un modèle Ollama local

        Args:
            prompt: Question utilisateur
            model: Modèle à utiliser
            system_prompt: Instructions système (optionnel)
            temperature: Créativité (0=déterministe, 1=créatif)
            max_tokens: Nombre max tokens réponse
            stream: Si True, retourne generator pour streaming

        Returns:
            Generator[str] si stream=True, str si stream=False
        """
        if not self.ollama_installed:
            raise RuntimeError("Ollama n'est pas installé")

        if model not in self.available_models:
            raise ValueError(f"Modèle {model} non installé. Modèles disponibles: {self.available_models}")

        # Construire le payload
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }

        if system_prompt:
            payload["system"] = system_prompt

        try:
            start_time = time.time()
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                stream=stream,
                timeout=120
            )

            if stream:
                # Mode streaming - yield chaque token
                def stream_generator():
                    full_response = ""
                    for line in response.iter_lines():
                        if line:
                            data = json.loads(line)
                            chunk = data.get('response', '')
                            full_response += chunk
                            yield chunk

                            if data.get('done', False):
                                elapsed = time.time() - start_time
                                tokens = len(full_response.split())
                                tps = tokens / elapsed if elapsed > 0 else 0
                                logger.info("Ollama", f"Réponse générée en {elapsed:.1f}s ({tps:.1f} tok/s)")
                                break

                return stream_generator()

            else:
                # Mode non-streaming - retourner réponse complète
                data = response.json()
                full_response = data.get('response', '')

                elapsed = time.time() - start_time
                tokens = len(full_response.split())
                tps = tokens / elapsed if elapsed > 0 else 0
                logger.info("Ollama", f"Réponse générée en {elapsed:.1f}s ({tps:.1f} tok/s)")

                return full_response

        except Exception as e:
            logger.error("Ollama", f"Erreur query {model}: {e}")
            raise

    def benchmark_models(self, test_prompt: str = "Explique comment optimiser Windows pour le gaming en 3 étapes.") -> Dict[str, Dict]:
        """
        Benchmark tous les modèles installés

        Returns:
            Dict: {model_name: {latency, tokens_per_sec, quality_score}}
        """
        results = {}

        for model in self.available_models:
            try:
                logger.info("Ollama", f"Benchmark {model}...")

                start_time = time.time()
                response = self.query_local(test_prompt, model=model, stream=False)
                elapsed = time.time() - start_time

                tokens = len(response.split())
                tps = tokens / elapsed if elapsed > 0 else 0

                results[model] = {
                    "latency": round(elapsed, 2),
                    "tokens_per_sec": round(tps, 1),
                    "response_length": tokens,
                    "quality_score": self._estimate_quality(response)
                }

                logger.info("Ollama", f"{model}: {elapsed:.1f}s, {tps:.1f} tok/s")

            except Exception as e:
                logger.error("Ollama", f"Erreur benchmark {model}: {e}")
                results[model] = {"error": str(e)}

        return results

    def _estimate_quality(self, response: str) -> float:
        """
        Estime la qualité d'une réponse (heuristique simple)

        Returns:
            float: Score 0-10
        """
        score = 5.0  # Base

        # Longueur raisonnable
        words = len(response.split())
        if 50 <= words <= 300:
            score += 1.0

        # Structure (paragraphes)
        paragraphs = response.count('\n\n')
        if paragraphs >= 2:
            score += 1.0

        # Listes/énumérations
        if any(marker in response for marker in ['1.', '2.', '3.', '-', '*']):
            score += 1.0

        # Vocabulaire technique pertinent
        tech_keywords = ['optimiser', 'performance', 'configur', 'paramètre', 'système']
        if sum(1 for kw in tech_keywords if kw in response.lower()) >= 2:
            score += 1.5

        # Pas d'erreurs évidentes
        if not any(err in response.lower() for err in ['erreur', 'désolé', "je ne peux pas", "je ne sais pas"]):
            score += 0.5

        return min(score, 10.0)

    def auto_select_model(self, task_type: str = "general") -> str:
        """
        Sélectionne automatiquement le meilleur modèle selon la tâche

        Args:
            task_type: Type de tâche ("general", "technical", "reasoning", "fast")

        Returns:
            str: Nom du modèle recommandé
        """
        if not self.available_models:
            raise RuntimeError("Aucun modèle Ollama installé")

        # Mapping tâche → modèle prioritaire
        task_preferences = {
            "general": ["llama3:8b", "mistral:7b", "qwen2.5:14b"],
            "technical": ["mistral:7b", "qwen2.5:14b", "deepseek-r1:8b"],
            "reasoning": ["deepseek-r1:8b", "qwen2.5:14b", "llama3:8b"],
            "fast": ["phi3:mini", "llama3:8b", "mistral:7b"]
        }

        preferences = task_preferences.get(task_type, task_preferences["general"])

        # Retourner le premier modèle disponible dans les préférences
        for model in preferences:
            if model in self.available_models:
                logger.info("Ollama", f"Modèle sélectionné pour '{task_type}': {model}")
                return model

        # Fallback: premier modèle disponible
        fallback = self.available_models[0]
        logger.warning("Ollama", f"Aucun modèle préféré disponible, fallback: {fallback}")
        return fallback

    def get_model_info(self, model_name: str) -> Optional[Dict]:
        """Récupère les informations détaillées d'un modèle"""
        try:
            response = requests.post(
                f"{self.base_url}/api/show",
                json={"name": model_name},
                timeout=5
            )

            if response.status_code == 200:
                return response.json()

            return None

        except Exception as e:
            logger.error("Ollama", f"Erreur info modèle {model_name}: {e}")
            return None

    def get_installation_guide(self) -> str:
        """Retourne le guide d'installation Ollama"""
        return """
╔══════════════════════════════════════════════════════════════╗
║              INSTALLATION OLLAMA - GUIDE RAPIDE              ║
╚══════════════════════════════════════════════════════════════╝

📥 TÉLÉCHARGEMENT
   Windows: https://ollama.ai/download
   Taille: ~500 MB

⚙️ INSTALLATION
   1. Lancer l'installateur (.exe)
   2. Suivre l'assistant (installation automatique)
   3. Ollama démarre automatiquement en arrière-plan

✅ VÉRIFICATION
   Ouvrir un terminal et taper: ollama --version
   Si affiche la version → Installation réussie!

🚀 PREMIER MODÈLE (Recommandé: llama3:8b)
   Dans terminal: ollama pull llama3:8b
   Taille: ~4.7 GB
   Temps: ~10-15 minutes (selon connexion)

🎯 UTILISATION DANS NITRITE
   Une fois installé, redémarrer NiTriTe
   L'agent IA détectera automatiquement Ollama
   Mode local = GRATUIT + RAPIDE + PRIVÉ!

💡 MODÈLES RECOMMANDÉS
   - llama3:8b (Général) - 4.7 GB
   - mistral:7b (Technique) - 4.1 GB
   - phi3:mini (Ultra-rapide) - 2.3 GB

📚 DOCUMENTATION: https://github.com/ollama/ollama
"""


# Singleton pour accès global
_ollama_manager_instance = None

def get_ollama_manager() -> OllamaManager:
    """Retourne l'instance singleton du OllamaManager"""
    global _ollama_manager_instance
    if _ollama_manager_instance is None:
        _ollama_manager_instance = OllamaManager()
    return _ollama_manager_instance


if __name__ == "__main__":
    # Tests
    print("=== Ollama Manager - Tests ===\n")

    manager = get_ollama_manager()

    if manager.ollama_installed:
        print(f"✓ Ollama installé")
        print(f"✓ Modèles disponibles: {manager.available_models}\n")

        if manager.available_models:
            # Test query
            model = manager.available_models[0]
            print(f"Test query avec {model}...\n")

            try:
                # Test streaming
                print("Réponse (streaming):")
                for chunk in manager.query_local("Dis bonjour en 1 phrase courte", model=model):
                    print(chunk, end='', flush=True)
                print("\n")

            except Exception as e:
                print(f"Erreur: {e}")
        else:
            print("Aucun modèle installé. Installer avec:")
            print("  ollama pull llama3:8b")

    else:
        print("✗ Ollama non installé\n")
        print(manager.get_installation_guide())
