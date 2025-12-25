#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Voice Interface System - Phase 9
Interface vocale: Speech-to-Text et Text-to-Speech
Permet interaction mains-libres avec l'agent IA
"""

import os
from typing import Optional, Callable
import threading

class VoiceInterface:
    """
    Interface vocale pour l'agent IA
    - Speech-to-Text: Convertir parole → texte
    - Text-to-Speech: Convertir texte → parole
    - Support multilingue
    - Commandes vocales (activer, désactiver, effacer, etc.)
    """

    def __init__(self):
        self.is_listening = False
        self.tts_enabled = True
        self.language = "fr-FR"  # Langue par défaut

        # Modules voice (importations lazy pour éviter dépendances lourdes)
        self.speech_recognition = None
        self.tts_engine = None

        # Callbacks
        self.on_speech_detected = None  # Callback(text)
        self.on_error = None  # Callback(error)

        # Commandes vocales spéciales
        self.voice_commands = {
            "fr-FR": {
                "arrête": "stop_listening",
                "efface": "clear_chat",
                "répète": "repeat_last",
                "aide": "help",
                "silence": "mute_tts"
            },
            "en-US": {
                "stop": "stop_listening",
                "clear": "clear_chat",
                "repeat": "repeat_last",
                "help": "help",
                "mute": "mute_tts"
            }
        }

    def initialize_speech_recognition(self) -> bool:
        """
        Initialiser le module de reconnaissance vocale
        Utilise speech_recognition (Google Speech API gratuite)

        Returns:
            True si succès, False si échec
        """
        try:
            import speech_recognition as sr
            self.speech_recognition = sr
            return True
        except ImportError:
            print("❌ speech_recognition non installé: pip install SpeechRecognition pyaudio")
            return False

    def initialize_tts(self) -> bool:
        """
        Initialiser le module Text-to-Speech
        Utilise pyttsx3 (TTS offline multi-plateforme)

        Returns:
            True si succès, False si échec
        """
        try:
            import pyttsx3
            self.tts_engine = pyttsx3.init()

            # Configuration
            self.tts_engine.setProperty('rate', 150)  # Vitesse modérée
            self.tts_engine.setProperty('volume', 0.9)  # Volume 90%

            # Sélectionner voix française si disponible
            voices = self.tts_engine.getProperty('voices')
            for voice in voices:
                if 'french' in voice.name.lower() or 'fr' in voice.id.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break

            return True
        except ImportError:
            print("❌ pyttsx3 non installé: pip install pyttsx3")
            return False
        except Exception as e:
            print(f"❌ Erreur initialisation TTS: {e}")
            return False

    def start_listening(self, callback: Optional[Callable[[str], None]] = None):
        """
        Démarrer l'écoute continue (asynchrone)

        Args:
            callback: Fonction appelée quand texte détecté
        """
        if not self.speech_recognition:
            if not self.initialize_speech_recognition():
                return

        self.is_listening = True
        self.on_speech_detected = callback

        # Lancer dans un thread séparé
        listen_thread = threading.Thread(target=self._listen_loop, daemon=True)
        listen_thread.start()

    def stop_listening(self):
        """Arrêter l'écoute"""
        self.is_listening = False

    def _listen_loop(self):
        """
        Boucle d'écoute (thread séparé)
        """
        recognizer = self.speech_recognition.Recognizer()
        microphone = self.speech_recognition.Microphone()

        print("🎤 Écoute activée...")

        with microphone as source:
            # Ajuster pour le bruit ambiant
            recognizer.adjust_for_ambient_noise(source, duration=1)

        while self.is_listening:
            try:
                with microphone as source:
                    print("🎤 En attente de parole...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

                # Reconnaissance vocale
                try:
                    # Utiliser Google Speech API (gratuit, limite 50 req/jour)
                    text = recognizer.recognize_google(audio, language=self.language)
                    print(f"🎤 Détecté: {text}")

                    # Vérifier commandes vocales spéciales
                    command = self._check_voice_command(text)
                    if command:
                        self._execute_voice_command(command)
                    elif self.on_speech_detected:
                        self.on_speech_detected(text)

                except self.speech_recognition.UnknownValueError:
                    print("🎤 Parole non comprise")
                except self.speech_recognition.RequestError as e:
                    print(f"❌ Erreur API Google Speech: {e}")
                    if self.on_error:
                        self.on_error(str(e))

            except Exception as e:
                print(f"❌ Erreur écoute: {e}")
                if self.on_error:
                    self.on_error(str(e))

        print("🎤 Écoute arrêtée")

    def _check_voice_command(self, text: str) -> Optional[str]:
        """Vérifier si le texte contient une commande vocale"""
        text_lower = text.lower().strip()

        # Chercher commandes de la langue actuelle
        lang_commands = self.voice_commands.get(self.language, {})

        for trigger, command in lang_commands.items():
            if trigger in text_lower:
                return command

        return None

    def _execute_voice_command(self, command: str):
        """Exécuter une commande vocale spéciale"""
        print(f"🎤 Commande vocale: {command}")

        if command == "stop_listening":
            self.stop_listening()
            self.speak("Écoute arrêtée" if self.language == "fr-FR" else "Listening stopped")

        elif command == "mute_tts":
            self.tts_enabled = not self.tts_enabled
            status = "désactivée" if not self.tts_enabled else "activée"
            self.speak(f"Voix {status}")

    def speak(self, text: str, interrupt: bool = False):
        """
        Prononcer un texte (Text-to-Speech)

        Args:
            text: Texte à prononcer
            interrupt: Si True, interrompre parole en cours
        """
        if not self.tts_enabled:
            return

        if not self.tts_engine:
            if not self.initialize_tts():
                return

        try:
            if interrupt:
                self.tts_engine.stop()

            # Nettoyer le texte (enlever markdown, emojis pour meilleure prononciation)
            clean_text = self._clean_text_for_speech(text)

            # Prononcer dans un thread pour ne pas bloquer
            speak_thread = threading.Thread(
                target=lambda: self.tts_engine.say(clean_text) or self.tts_engine.runAndWait(),
                daemon=True
            )
            speak_thread.start()

        except Exception as e:
            print(f"❌ Erreur TTS: {e}")
            if self.on_error:
                self.on_error(str(e))

    def _clean_text_for_speech(self, text: str) -> str:
        """
        Nettoyer le texte pour améliorer la prononciation

        Args:
            text: Texte brut avec markdown/emojis

        Returns:
            Texte nettoyé
        """
        import re

        # Supprimer emojis (regex Unicode)
        text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
        text = re.sub(r'[\u2600-\u26FF\u2700-\u27BF]', '', text)

        # Supprimer markdown
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # **gras**
        text = re.sub(r'\*([^*]+)\*', r'\1', text)  # *italique*
        text = re.sub(r'`([^`]+)`', r'\1', text)  # `code`
        text = re.sub(r'#{1,6}\s+', '', text)  # # titres

        # Supprimer URLs
        text = re.sub(r'http[s]?://\S+', '', text)

        # Remplacer abréviations techniques pour meilleure prononciation
        replacements = {
            "CPU": "processeur",
            "GPU": "carte graphique",
            "RAM": "mémoire vive",
            "SSD": "disque SSD",
            "HDD": "disque dur",
            "BSOD": "écran bleu",
            "FPS": "images par seconde",
            "GHz": "gigahertz",
            "MHz": "mégahertz",
            "GB": "gigaoctets",
            "MB": "mégaoctets",
            "TB": "téraoctets"
        }

        for abbr, full in replacements.items():
            text = re.sub(r'\b' + abbr + r'\b', full, text, flags=re.IGNORECASE)

        # Nettoyer espaces multiples
        text = ' '.join(text.split())

        return text

    def set_language(self, language_code: str):
        """
        Changer la langue de l'interface vocale

        Args:
            language_code: Code langue (fr-FR, en-US, es-ES, etc.)
        """
        self.language = language_code

        # Mettre à jour voix TTS si possible
        if self.tts_engine:
            voices = self.tts_engine.getProperty('voices')
            lang_short = language_code.split('-')[0]  # fr, en, es, etc.

            for voice in voices:
                if lang_short in voice.id.lower() or lang_short in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break

    def get_available_voices(self) -> list:
        """Obtenir la liste des voix TTS disponibles"""
        if not self.tts_engine:
            if not self.initialize_tts():
                return []

        voices = self.tts_engine.getProperty('voices')
        return [{"id": v.id, "name": v.name, "languages": v.languages} for v in voices]

    def test_microphone(self) -> bool:
        """
        Tester le microphone

        Returns:
            True si microphone fonctionne, False sinon
        """
        if not self.speech_recognition:
            if not self.initialize_speech_recognition():
                return False

        try:
            recognizer = self.speech_recognition.Recognizer()
            microphone = self.speech_recognition.Microphone()

            with microphone as source:
                print("🎤 Test microphone - parlez maintenant...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

            # Essayer de reconnaître
            text = recognizer.recognize_google(audio, language=self.language)
            print(f"✅ Microphone OK! Détecté: {text}")
            return True

        except Exception as e:
            print(f"❌ Problème microphone: {e}")
            return False

    def get_stats(self) -> dict:
        """Statistiques de l'interface vocale"""
        return {
            "is_listening": self.is_listening,
            "tts_enabled": self.tts_enabled,
            "language": self.language,
            "speech_recognition_available": self.speech_recognition is not None,
            "tts_available": self.tts_engine is not None
        }


# Test
if __name__ == "__main__":
    voice = VoiceInterface()

    # Test TTS
    if voice.initialize_tts():
        print("✅ TTS initialisé")
        voice.speak("Bonjour, je suis votre assistant IA vocal. Comment puis-je vous aider?")
    else:
        print("❌ TTS non disponible")

    # Test microphone
    if voice.initialize_speech_recognition():
        print("✅ Speech Recognition initialisé")
        if voice.test_microphone():
            print("✅ Microphone fonctionne")
    else:
        print("❌ Speech Recognition non disponible")

    print("\nVoix TTS disponibles:")
    for v in voice.get_available_voices():
        print(f"  - {v['name']}")
