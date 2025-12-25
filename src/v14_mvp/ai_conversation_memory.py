#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversation Memory System - Phase 6
Système de mémoire conversationnelle avancé pour l'agent IA
Conserve le contexte, les préférences utilisateur, et l'historique
"""

import json
import os
from typing import List, Dict, Optional
from datetime import datetime
import hashlib

class ConversationMemory:
    """
    Système de mémoire conversationnelle intelligent
    - Historique multi-sessions
    - Détection automatique des préférences utilisateur
    - Résumés automatiques de conversations longues
    - Rappel contextuel
    """

    def __init__(self, memory_dir: str = "data/memory"):
        self.memory_dir = memory_dir
        self.session_file = os.path.join(memory_dir, "current_session.json")
        self.history_file = os.path.join(memory_dir, "conversation_history.json")
        self.preferences_file = os.path.join(memory_dir, "user_preferences.json")

        # Créer dossier si nécessaire
        os.makedirs(memory_dir, exist_ok=True)

        # Charger données
        self.current_session = self._load_current_session()
        self.user_preferences = self._load_preferences()
        self.conversation_history = []

        # Limites
        self.max_session_messages = 50  # Résumé auto après 50 messages
        self.max_context_tokens = 4000  # Contexte max à envoyer à l'API

    def _load_current_session(self) -> Dict:
        """Charger la session courante"""
        if os.path.exists(self.session_file):
            try:
                with open(self.session_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass

        return {
            "session_id": self._generate_session_id(),
            "started_at": datetime.now().isoformat(),
            "messages": [],
            "topics": [],
            "user_info": {}
        }

    def _load_preferences(self) -> Dict:
        """Charger les préférences utilisateur"""
        if os.path.exists(self.preferences_file):
            try:
                with open(self.preferences_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass

        return {
            "hardware": {},  # CPU, GPU, RAM détectés
            "common_issues": [],  # Problèmes fréquents
            "preferred_solutions": {},  # Solutions préférées
            "technical_level": "intermediate",  # beginner, intermediate, expert
            "language": "fr",  # Langue préférée
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

    def _generate_session_id(self) -> str:
        """Générer un ID unique pour la session"""
        timestamp = datetime.now().isoformat()
        return hashlib.md5(timestamp.encode()).hexdigest()[:12]

    def add_message(self, role: str, content: str, metadata: Optional[Dict] = None):
        """
        Ajouter un message à la mémoire

        Args:
            role: "user" ou "assistant"
            content: Contenu du message
            metadata: Métadonnées additionnelles (API utilisée, temps réponse, etc.)
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }

        self.current_session["messages"].append(message)
        self.conversation_history.append(message)

        # Détecter topics/sujets automatiquement
        if role == "user":
            self._extract_topics(content)

        # Détecter préférences
        self._update_preferences(message)

        # Vérifier si résumé nécessaire
        if len(self.current_session["messages"]) >= self.max_session_messages:
            self._summarize_and_archive()

        # Sauvegarder
        self._save_current_session()

    def _extract_topics(self, content: str):
        """Extraire les sujets/topics de la conversation"""
        content_lower = content.lower()

        # Topics hardware
        hardware_keywords = {
            "cpu": ["cpu", "processeur", "ryzen", "intel", "core"],
            "gpu": ["gpu", "carte graphique", "nvidia", "amd", "rtx", "radeon"],
            "ram": ["ram", "mémoire", "ddr4", "ddr5"],
            "storage": ["ssd", "nvme", "disque", "stockage"],
            "monitor": ["moniteur", "écran", "144hz", "refresh"]
        }

        # Topics software
        software_keywords = {
            "bsod": ["bsod", "écran bleu", "blue screen"],
            "driver": ["driver", "pilote"],
            "optimization": ["optimisation", "optimiser", "performance"],
            "gaming": ["gaming", "jeu", "fps", "valorant", "cs2"],
            "network": ["réseau", "wifi", "ethernet", "connexion"]
        }

        detected_topics = []

        for topic, keywords in {**hardware_keywords, **software_keywords}.items():
            if any(kw in content_lower for kw in keywords):
                if topic not in detected_topics:
                    detected_topics.append(topic)

        # Ajouter topics à la session si nouveaux
        for topic in detected_topics:
            if topic not in self.current_session["topics"]:
                self.current_session["topics"].append(topic)

    def _update_preferences(self, message: Dict):
        """Mettre à jour les préférences utilisateur basées sur la conversation"""
        if message["role"] != "user":
            return

        content_lower = message["content"].lower()

        # Détecter hardware mentionné
        hardware_patterns = {
            "cpu": r"(ryzen \d+ \d+x3d|core i\d+-\d+k|ryzen \d \d+x)",
            "gpu": r"(rtx \d+|rx \d+|radeon)",
            "ram": r"(ddr\d+[-\s]\d+|gb ram|\d+gb)"
        }

        import re
        for hw_type, pattern in hardware_patterns.items():
            match = re.search(pattern, content_lower)
            if match:
                self.user_preferences["hardware"][hw_type] = match.group(0)

        # Détecter niveau technique
        expert_keywords = ["overclock", "registry", "bios", "undervolt", "timings"]
        beginner_keywords = ["comment", "c'est quoi", "aide", "je ne sais pas"]

        if any(kw in content_lower for kw in expert_keywords):
            self.user_preferences["technical_level"] = "expert"
        elif any(kw in content_lower for kw in beginner_keywords):
            if self.user_preferences["technical_level"] != "expert":
                self.user_preferences["technical_level"] = "beginner"

        self.user_preferences["updated_at"] = datetime.now().isoformat()
        self._save_preferences()

    def get_context_for_api(self, max_messages: int = 10) -> List[Dict]:
        """
        Obtenir le contexte conversationnel à envoyer à l'API

        Args:
            max_messages: Nombre maximum de messages récents à inclure

        Returns:
            Liste de messages formatés pour l'API
        """
        # Prendre les N derniers messages
        recent_messages = self.conversation_history[-max_messages:]

        # Formater pour API (role + content uniquement)
        formatted = []
        for msg in recent_messages:
            formatted.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        return formatted

    def get_user_context_summary(self) -> str:
        """
        Générer un résumé du contexte utilisateur pour enrichir les prompts

        Returns:
            String de contexte à ajouter au system prompt
        """
        summary_parts = []

        # Hardware détecté
        if self.user_preferences.get("hardware"):
            hw_list = ", ".join([f"{k}: {v}" for k, v in self.user_preferences["hardware"].items()])
            summary_parts.append(f"🖥️ **Hardware utilisateur**: {hw_list}")

        # Topics de session
        if self.current_session.get("topics"):
            topics_str = ", ".join(self.current_session["topics"])
            summary_parts.append(f"📋 **Sujets abordés cette session**: {topics_str}")

        # Niveau technique
        level = self.user_preferences.get("technical_level", "intermediate")
        level_desc = {
            "beginner": "débutant (expliquer simplement, éviter jargon)",
            "intermediate": "intermédiaire (équilibre technique/accessible)",
            "expert": "expert (termes techniques OK, détails avancés)"
        }
        summary_parts.append(f"👤 **Niveau technique**: {level_desc.get(level, level)}")

        # Problèmes récurrents
        common_issues = self.user_preferences.get("common_issues", [])
        if common_issues:
            issues_str = ", ".join(common_issues[-3:])  # 3 derniers
            summary_parts.append(f"⚠️ **Problèmes fréquents**: {issues_str}")

        return "\n".join(summary_parts) if summary_parts else ""

    def _summarize_and_archive(self):
        """Créer un résumé de la session et archiver"""
        # TODO: Utiliser API pour générer résumé intelligent
        # Pour l'instant: simple archivage

        archive_entry = {
            "session_id": self.current_session["session_id"],
            "started_at": self.current_session["started_at"],
            "ended_at": datetime.now().isoformat(),
            "message_count": len(self.current_session["messages"]),
            "topics": self.current_session["topics"],
            "summary": f"Session avec {len(self.current_session['messages'])} messages sur {', '.join(self.current_session['topics']) if self.current_session['topics'] else 'divers sujets'}"
        }

        # Sauvegarder archive
        archive_file = os.path.join(self.memory_dir, "sessions_archive.json")
        archive = []
        if os.path.exists(archive_file):
            try:
                with open(archive_file, 'r', encoding='utf-8') as f:
                    archive = json.load(f)
            except:
                pass

        archive.append(archive_entry)

        with open(archive_file, 'w', encoding='utf-8') as f:
            json.dump(archive, f, indent=2, ensure_ascii=False)

        # Réinitialiser session courante
        self.current_session = {
            "session_id": self._generate_session_id(),
            "started_at": datetime.now().isoformat(),
            "messages": [],
            "topics": [],
            "user_info": {}
        }

        # Garder seulement les 20 derniers messages en mémoire
        self.conversation_history = self.conversation_history[-20:]

    def _save_current_session(self):
        """Sauvegarder la session courante"""
        try:
            with open(self.session_file, 'w', encoding='utf-8') as f:
                json.dump(self.current_session, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde session: {e}")

    def _save_preferences(self):
        """Sauvegarder les préférences utilisateur"""
        try:
            with open(self.preferences_file, 'w', encoding='utf-8') as f:
                json.dump(self.user_preferences, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde préférences: {e}")

    def clear_session(self):
        """Effacer la session courante"""
        self.current_session = {
            "session_id": self._generate_session_id(),
            "started_at": datetime.now().isoformat(),
            "messages": [],
            "topics": [],
            "user_info": {}
        }
        self.conversation_history = []
        self._save_current_session()

    def get_stats(self) -> Dict:
        """Statistiques de la mémoire"""
        return {
            "current_session_messages": len(self.current_session["messages"]),
            "topics_discussed": len(self.current_session["topics"]),
            "user_hardware_detected": len(self.user_preferences.get("hardware", {})),
            "technical_level": self.user_preferences.get("technical_level"),
            "session_id": self.current_session["session_id"]
        }


# Test
if __name__ == "__main__":
    memory = ConversationMemory()

    # Simuler conversation
    memory.add_message("user", "J'ai un Ryzen 7 7800X3D et une RTX 4080, comment optimiser pour Valorant?")
    memory.add_message("assistant", "Voici comment optimiser...")
    memory.add_message("user", "Merci! Et pour les timings RAM DDR5-6000?")

    print(json.dumps(memory.get_stats(), indent=2))
    print("\nContexte utilisateur:")
    print(memory.get_user_context_summary())
