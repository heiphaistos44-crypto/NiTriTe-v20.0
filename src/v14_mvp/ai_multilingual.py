#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multilingual Support System - Phase 8
Détection automatique de langue et réponses multilingues
Support: Français, Anglais, Espagnol, Allemand, Italien
"""

from typing import Dict, Optional, Tuple
import re

class MultilingualSystem:
    """
    Système de support multilingue
    - Détection automatique de la langue
    - Traductions des réponses systèmes
    - Adaptation du ton selon la langue/culture
    """

    def __init__(self):
        self.supported_languages = {
            "fr": "Français",
            "en": "English",
            "es": "Español",
            "de": "Deutsch",
            "it": "Italiano"
        }

        # Mots-clés pour détection de langue
        self.language_keywords = {
            "fr": [
                "bonjour", "merci", "salut", "comment", "pourquoi", "quand",
                "aide", "problème", "ordinateur", "souris", "clavier",
                "écran", "processeur", "mémoire", "disque"
            ],
            "en": [
                "hello", "thanks", "help", "problem", "computer", "mouse",
                "keyboard", "screen", "processor", "memory", "disk",
                "how", "why", "when", "what"
            ],
            "es": [
                "hola", "gracias", "ayuda", "problema", "computadora",
                "ratón", "teclado", "pantalla", "procesador", "memoria",
                "cómo", "por qué", "cuándo"
            ],
            "de": [
                "hallo", "danke", "hilfe", "problem", "computer", "maus",
                "tastatur", "bildschirm", "prozessor", "speicher",
                "wie", "warum", "wann"
            ],
            "it": [
                "ciao", "grazie", "aiuto", "problema", "computer", "mouse",
                "tastiera", "schermo", "processore", "memoria",
                "come", "perché", "quando"
            ]
        }

        # Messages système traduits
        self.system_messages = {
            "welcome": {
                "fr": "👋 Bonjour! Je suis votre assistant IA spécialisé en maintenance informatique. Comment puis-je vous aider aujourd'hui?",
                "en": "👋 Hello! I'm your AI assistant specialized in computer maintenance. How can I help you today?",
                "es": "👋 ¡Hola! Soy tu asistente de IA especializado en mantenimiento informático. ¿Cómo puedo ayudarte hoy?",
                "de": "👋 Hallo! Ich bin Ihr KI-Assistent für Computerwartung. Wie kann ich Ihnen heute helfen?",
                "it": "👋 Ciao! Sono il tuo assistente IA specializzato in manutenzione informatica. Come posso aiutarti oggi?"
            },
            "thinking": {
                "fr": "🤔 Réflexion en cours...",
                "en": "🤔 Thinking...",
                "es": "🤔 Pensando...",
                "de": "🤔 Nachdenken...",
                "it": "🤔 Sto pensando..."
            },
            "error": {
                "fr": "❌ Une erreur s'est produite. Veuillez réessayer.",
                "en": "❌ An error occurred. Please try again.",
                "es": "❌ Ocurrió un error. Por favor, intenta de nuevo.",
                "de": "❌ Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut.",
                "it": "❌ Si è verificato un errore. Riprova."
            },
            "command_confirmation": {
                "fr": "⚠️ Voulez-vous exécuter cette commande?",
                "en": "⚠️ Do you want to execute this command?",
                "es": "⚠️ ¿Quieres ejecutar este comando?",
                "de": "⚠️ Möchten Sie diesen Befehl ausführen?",
                "it": "⚠️ Vuoi eseguire questo comando?"
            },
            "feedback_positive": {
                "fr": "✅ Merci pour votre retour positif!",
                "en": "✅ Thank you for your positive feedback!",
                "es": "✅ ¡Gracias por tu comentario positivo!",
                "de": "✅ Vielen Dank für Ihr positives Feedback!",
                "it": "✅ Grazie per il tuo feedback positivo!"
            },
            "feedback_negative": {
                "fr": "⚠️ Désolé que la réponse ne soit pas satisfaisante. Pouvez-vous préciser ce qui manque?",
                "en": "⚠️ Sorry the response wasn't satisfactory. Can you specify what's missing?",
                "es": "⚠️ Lamento que la respuesta no sea satisfactoria. ¿Puedes especificar qué falta?",
                "de": "⚠️ Es tut mir leid, dass die Antwort nicht zufriedenstellend war. Können Sie angeben, was fehlt?",
                "it": "⚠️ Mi dispiace che la risposta non sia soddisfacente. Puoi specificare cosa manca?"
            }
        }

        # Instructions système par langue pour l'API
        self.system_instructions = {
            "fr": """Tu réponds en FRANÇAIS. Utilise un ton professionnel mais accessible.
Structure tes réponses avec des emojis, du markdown, et des explications détaillées.""",

            "en": """You respond in ENGLISH. Use a professional but accessible tone.
Structure your responses with emojis, markdown, and detailed explanations.""",

            "es": """Respondes en ESPAÑOL. Usa un tono profesional pero accesible.
Estructura tus respuestas con emojis, markdown y explicaciones detalladas.""",

            "de": """Du antwortest auf DEUTSCH. Verwende einen professionellen aber zugänglichen Ton.
Strukturiere deine Antworten mit Emojis, Markdown und detaillierten Erklärungen.""",

            "it": """Rispondi in ITALIANO. Usa un tono professionale ma accessibile.
Struttura le tue risposte con emoji, markdown e spiegazioni dettagliate."""
        }

    def detect_language(self, text: str) -> str:
        """
        Détecter automatiquement la langue d'un texte

        Args:
            text: Texte à analyser

        Returns:
            Code langue détecté (fr, en, es, de, it)
        """
        text_lower = text.lower()

        # Compter les mots-clés par langue
        scores = {lang: 0 for lang in self.supported_languages.keys()}

        for lang, keywords in self.language_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    scores[lang] += 1

        # Retourner langue avec le meilleur score
        if max(scores.values()) == 0:
            return "fr"  # Défaut français si aucune détection

        detected = max(scores, key=scores.get)
        return detected

    def get_system_message(self, message_key: str, language: str = "fr") -> str:
        """
        Obtenir un message système traduit

        Args:
            message_key: Clé du message (welcome, thinking, error, etc.)
            language: Code langue

        Returns:
            Message traduit
        """
        if message_key in self.system_messages:
            return self.system_messages[message_key].get(language, self.system_messages[message_key]["fr"])

        return ""

    def get_system_instruction(self, language: str = "fr") -> str:
        """
        Obtenir l'instruction système pour l'API dans la langue appropriée

        Args:
            language: Code langue

        Returns:
            Instruction système traduite
        """
        return self.system_instructions.get(language, self.system_instructions["fr"])

    def adapt_response_tone(self, response: str, language: str) -> str:
        """
        Adapter le ton de la réponse selon la langue/culture

        Args:
            response: Réponse brute
            language: Code langue

        Returns:
            Réponse adaptée culturellement
        """
        # Pour l'instant: simple vérification
        # Dans une vraie implémentation: utiliser l'API pour reformuler

        # Adaptations culturelles légères
        if language == "de":
            # Allemand: plus formel, vouvoiement
            response = response.replace("tu ", "vous ")
            response = response.replace("ton ", "votre ")

        elif language == "en":
            # Anglais: plus direct, moins d'emojis
            # (Déjà géré par l'API si instruction correcte)
            pass

        elif language == "es":
            # Espagnol: chaleureux, exclamatifs
            pass

        return response

    def translate_technical_term(self, term: str, source_lang: str, target_lang: str) -> str:
        """
        Traduire un terme technique

        Args:
            term: Terme à traduire
            source_lang: Langue source
            target_lang: Langue cible

        Returns:
            Terme traduit
        """
        # Dictionnaire de termes techniques communs
        tech_terms = {
            "cpu": {"fr": "processeur", "en": "CPU", "es": "procesador", "de": "Prozessor", "it": "processore"},
            "gpu": {"fr": "carte graphique", "en": "graphics card", "es": "tarjeta gráfica", "de": "Grafikkarte", "it": "scheda grafica"},
            "ram": {"fr": "mémoire vive", "en": "RAM", "es": "memoria RAM", "de": "Arbeitsspeicher", "it": "memoria RAM"},
            "ssd": {"fr": "disque SSD", "en": "SSD", "es": "disco SSD", "de": "SSD-Laufwerk", "it": "disco SSD"},
            "driver": {"fr": "pilote", "en": "driver", "es": "controlador", "de": "Treiber", "it": "driver"},
            "bsod": {"fr": "écran bleu", "en": "blue screen", "es": "pantalla azul", "de": "Bluescreen", "it": "schermo blu"},
        }

        term_lower = term.lower()
        if term_lower in tech_terms:
            return tech_terms[term_lower].get(target_lang, term)

        return term  # Pas de traduction trouvée

    def format_command_output(self, command: str, output: str, language: str) -> str:
        """
        Formater la sortie d'une commande selon la langue

        Args:
            command: Commande exécutée
            output: Sortie brute
            language: Langue cible

        Returns:
            Sortie formatée et traduite
        """
        headers = {
            "command": {
                "fr": "Commande",
                "en": "Command",
                "es": "Comando",
                "de": "Befehl",
                "it": "Comando"
            },
            "output": {
                "fr": "Résultat",
                "en": "Output",
                "es": "Resultado",
                "de": "Ausgabe",
                "it": "Risultato"
            }
        }

        formatted = f"**{headers['command'][language]}**: `{command}`\n\n"
        formatted += f"**{headers['output'][language]}**:\n```\n{output}\n```"

        return formatted

    def get_language_stats(self) -> Dict:
        """Statistiques du système multilingue"""
        return {
            "supported_languages": len(self.supported_languages),
            "languages": list(self.supported_languages.values()),
            "system_messages": len(self.system_messages)
        }


# Test
if __name__ == "__main__":
    ml = MultilingualSystem()

    # Test détection
    test_texts = [
        "Bonjour, comment optimiser mon ordinateur?",
        "Hello, how to optimize my computer?",
        "Hola, ¿cómo optimizar mi computadora?",
        "Hallo, wie optimiere ich meinen Computer?",
        "Ciao, come ottimizzare il mio computer?"
    ]

    for text in test_texts:
        detected = ml.detect_language(text)
        welcome = ml.get_system_message("welcome", detected)
        print(f"Text: {text[:30]}...")
        print(f"Detected: {ml.supported_languages[detected]}")
        print(f"Welcome: {welcome}\n")
