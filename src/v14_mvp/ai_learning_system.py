#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Learning System - Phase 7
Système d'apprentissage continu avec feedback utilisateur
L'agent s'améliore au fil des interactions
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime
import hashlib

class LearningSystem:
    """
    Système d'apprentissage et de feedback
    - Collecte feedback utilisateur (👍/👎)
    - Identifie réponses à améliorer
    - Suggestions d'ajouts à la knowledge base
    - Tracking qualité des réponses
    """

    def __init__(self, data_dir: str = "data/learning"):
        self.data_dir = data_dir
        self.feedback_file = os.path.join(data_dir, "feedback.json")
        self.learned_patterns_file = os.path.join(data_dir, "learned_patterns.json")
        self.suggestions_file = os.path.join(data_dir, "kb_suggestions.json")

        os.makedirs(data_dir, exist_ok=True)

        # Charger données
        self.feedbacks = self._load_feedbacks()
        self.learned_patterns = self._load_learned_patterns()
        self.kb_suggestions = self._load_kb_suggestions()

    def _load_feedbacks(self) -> List[Dict]:
        """Charger l'historique des feedbacks"""
        if os.path.exists(self.feedback_file):
            try:
                with open(self.feedback_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return []

    def _load_learned_patterns(self) -> Dict:
        """Charger les patterns appris"""
        if os.path.exists(self.learned_patterns_file):
            try:
                with open(self.learned_patterns_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass

        return {
            "successful_responses": {},  # Question → Réponse qui a bien fonctionné
            "failed_responses": {},  # Question → Réponses à éviter
            "user_corrections": [],  # Corrections apportées par l'utilisateur
            "effective_commands": {},  # Commandes qui ont résolu des problèmes
        }

    def _load_kb_suggestions(self) -> List[Dict]:
        """Charger les suggestions d'ajouts à la KB"""
        if os.path.exists(self.suggestions_file):
            try:
                with open(self.suggestions_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return []

    def record_feedback(
        self,
        question: str,
        response: str,
        rating: str,  # "positive", "negative", "neutral"
        comment: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> str:
        """
        Enregistrer un feedback utilisateur

        Args:
            question: Question posée
            response: Réponse fournie
            rating: Évaluation (positive/negative/neutral)
            comment: Commentaire optionnel de l'utilisateur
            metadata: Métadonnées (API utilisée, temps, etc.)

        Returns:
            feedback_id
        """
        feedback_id = self._generate_feedback_id(question, response)

        feedback_entry = {
            "feedback_id": feedback_id,
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "response": response[:500],  # Limiter taille
            "rating": rating,
            "comment": comment,
            "metadata": metadata or {},
            "processed": False
        }

        self.feedbacks.append(feedback_entry)

        # Sauvegarder
        self._save_feedbacks()

        # Traiter immédiatement
        self._process_feedback(feedback_entry)

        return feedback_id

    def _generate_feedback_id(self, question: str, response: str) -> str:
        """Générer un ID unique pour le feedback"""
        combined = f"{question}{response}{datetime.now().isoformat()}"
        return hashlib.md5(combined.encode()).hexdigest()[:12]

    def _process_feedback(self, feedback: Dict):
        """
        Traiter un feedback et mettre à jour les patterns appris

        Args:
            feedback: Entry de feedback à traiter
        """
        question = feedback["question"]
        response = feedback["response"]
        rating = feedback["rating"]

        # Créer une clé de question normalisée (lowercase, sans ponctuation)
        question_key = self._normalize_question(question)

        if rating == "positive":
            # Réponse a bien fonctionné → apprendre
            if question_key not in self.learned_patterns["successful_responses"]:
                self.learned_patterns["successful_responses"][question_key] = []

            self.learned_patterns["successful_responses"][question_key].append({
                "response_snippet": response[:200],
                "full_question": question,
                "count": 1,
                "last_seen": datetime.now().isoformat()
            })

        elif rating == "negative":
            # Réponse mauvaise → éviter ce pattern
            if question_key not in self.learned_patterns["failed_responses"]:
                self.learned_patterns["failed_responses"][question_key] = []

            self.learned_patterns["failed_responses"][question_key].append({
                "response_snippet": response[:200],
                "full_question": question,
                "issue": feedback.get("comment", "Non spécifié"),
                "count": 1,
                "last_seen": datetime.now().isoformat()
            })

            # Créer suggestion pour améliorer KB
            self._create_kb_suggestion(question, feedback.get("comment"))

        # Sauvegarder patterns
        self._save_learned_patterns()

        # Marquer comme traité
        feedback["processed"] = True

    def _normalize_question(self, question: str) -> str:
        """Normaliser une question pour matching"""
        import re
        normalized = question.lower()
        normalized = re.sub(r'[^\w\s]', '', normalized)  # Supprimer ponctuation
        normalized = ' '.join(normalized.split())  # Normaliser espaces
        return normalized

    def _create_kb_suggestion(self, question: str, issue: Optional[str]):
        """Créer une suggestion d'ajout à la knowledge base"""
        suggestion = {
            "timestamp": datetime.now().isoformat(),
            "question": question,
            "issue": issue or "Réponse inadéquate ou incomplète",
            "status": "pending",  # pending, approved, rejected
            "suggested_content": None
        }

        self.kb_suggestions.append(suggestion)
        self._save_kb_suggestions()

    def get_similar_successful_responses(self, question: str, limit: int = 3) -> List[Dict]:
        """
        Trouver des réponses similaires qui ont bien fonctionné dans le passé

        Args:
            question: Question actuelle
            limit: Nombre max de suggestions

        Returns:
            Liste de réponses réussies similaires
        """
        question_key = self._normalize_question(question)

        # Exact match
        if question_key in self.learned_patterns["successful_responses"]:
            return self.learned_patterns["successful_responses"][question_key][:limit]

        # Fuzzy matching (mots-clés communs)
        question_words = set(question_key.split())
        similar = []

        for stored_key, responses in self.learned_patterns["successful_responses"].items():
            stored_words = set(stored_key.split())
            # Calculer similarité (Jaccard)
            intersection = len(question_words & stored_words)
            union = len(question_words | stored_words)
            similarity = intersection / union if union > 0 else 0

            if similarity > 0.3:  # Seuil 30% similarité
                for resp in responses:
                    similar.append({
                        **resp,
                        "similarity": similarity
                    })

        # Trier par similarité décroissante
        similar.sort(key=lambda x: x["similarity"], reverse=True)
        return similar[:limit]

    def should_avoid_response_pattern(self, question: str, response_snippet: str) -> bool:
        """
        Vérifier si un pattern de réponse doit être évité

        Args:
            question: Question posée
            response_snippet: Début de la réponse à vérifier

        Returns:
            True si ce pattern a reçu des feedbacks négatifs
        """
        question_key = self._normalize_question(question)

        if question_key in self.learned_patterns["failed_responses"]:
            failed = self.learned_patterns["failed_responses"][question_key]
            for fail_entry in failed:
                # Check si snippet similaire
                if response_snippet[:100].lower() in fail_entry["response_snippet"].lower():
                    return True

        return False

    def record_effective_command(self, problem: str, command: str, success: bool):
        """
        Enregistrer une commande qui a été efficace (ou non) pour résoudre un problème

        Args:
            problem: Description du problème
            command: Commande exécutée
            success: Si la commande a résolu le problème
        """
        problem_key = self._normalize_question(problem)

        if problem_key not in self.learned_patterns["effective_commands"]:
            self.learned_patterns["effective_commands"][problem_key] = []

        self.learned_patterns["effective_commands"][problem_key].append({
            "command": command,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })

        self._save_learned_patterns()

    def get_stats(self) -> Dict:
        """Statistiques du système d'apprentissage"""
        total_feedbacks = len(self.feedbacks)
        positive = sum(1 for f in self.feedbacks if f["rating"] == "positive")
        negative = sum(1 for f in self.feedbacks if f["rating"] == "negative")

        return {
            "total_feedbacks": total_feedbacks,
            "positive_feedbacks": positive,
            "negative_feedbacks": negative,
            "satisfaction_rate": (positive / total_feedbacks * 100) if total_feedbacks > 0 else 0,
            "learned_patterns": len(self.learned_patterns["successful_responses"]),
            "kb_suggestions_pending": sum(1 for s in self.kb_suggestions if s["status"] == "pending"),
            "effective_commands": sum(len(cmds) for cmds in self.learned_patterns["effective_commands"].values())
        }

    def get_improvement_suggestions(self) -> List[str]:
        """Obtenir des suggestions d'amélioration basées sur les feedbacks négatifs"""
        suggestions = []

        # Analyser feedbacks négatifs récents
        recent_negative = [f for f in self.feedbacks[-50:] if f["rating"] == "negative"]

        if len(recent_negative) > 5:
            suggestions.append(f"⚠️ {len(recent_negative)} feedbacks négatifs récents - revoir qualité réponses")

        # KB suggestions en attente
        pending_suggestions = [s for s in self.kb_suggestions if s["status"] == "pending"]
        if len(pending_suggestions) > 10:
            suggestions.append(f"📚 {len(pending_suggestions)} suggestions KB en attente - enrichir la base")

        # Patterns échoués fréquents
        for question_key, fails in self.learned_patterns["failed_responses"].items():
            if len(fails) >= 3:
                suggestions.append(f"❌ Question récurrente mal répondue: '{fails[0]['full_question'][:50]}...'")

        return suggestions[:5]  # Top 5

    def _save_feedbacks(self):
        """Sauvegarder feedbacks"""
        try:
            with open(self.feedback_file, 'w', encoding='utf-8') as f:
                json.dump(self.feedbacks, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde feedbacks: {e}")

    def _save_learned_patterns(self):
        """Sauvegarder patterns appris"""
        try:
            with open(self.learned_patterns_file, 'w', encoding='utf-8') as f:
                json.dump(self.learned_patterns, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde patterns: {e}")

    def _save_kb_suggestions(self):
        """Sauvegarder suggestions KB"""
        try:
            with open(self.suggestions_file, 'w', encoding='utf-8') as f:
                json.dump(self.kb_suggestions, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde suggestions: {e}")


# Test
if __name__ == "__main__":
    learning = LearningSystem()

    # Simuler feedback
    learning.record_feedback(
        question="Comment overclocker mon Ryzen 7 7800X3D?",
        response="Le 7800X3D ne doit PAS être overclocké car...",
        rating="positive",
        comment="Très claire, merci!"
    )

    learning.record_feedback(
        question="Mon PC est lent",
        response="Redémarrez votre PC",
        rating="negative",
        comment="Trop basique, pas utile"
    )

    print(json.dumps(learning.get_stats(), indent=2))
    print("\nSuggestions d'amélioration:")
    for sugg in learning.get_improvement_suggestions():
        print(f"  {sugg}")
