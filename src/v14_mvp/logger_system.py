#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système de Logs Centralisé - NiTriTe V18
Log toutes les erreurs et événements de l'application
"""

import os
import sys
import json
import datetime
import threading
from pathlib import Path
from typing import Literal, Optional, Dict, Any

# Import du système de chemins portables
sys.path.insert(0, str(Path(__file__).parent.parent))
from portable_paths import get_portable_logs_dir

LogLevel = Literal["DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]


class CentralizedLogger:
    """Système de logs centralisé pour toute l'application"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            # Utiliser le dossier logs portable (à côté de l'exe)
            self.log_dir = get_portable_logs_dir()
            if self.log_dir is None:
                # Fallback si création impossible
                self.log_dir = Path("data/logs")
                self.log_dir.mkdir(parents=True, exist_ok=True)

            self.session_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.log_file = self.log_dir / f"nitrite_v18_{self.session_id}.log"
            self.error_file = self.log_dir / "errors.log"
            self.diagnostic_file = self.log_dir / "diagnostic.log"

            # Créer fichiers si n'existent pas
            for file in [self.log_file, self.error_file, self.diagnostic_file]:
                if not file.exists():
                    file.write_text("", encoding="utf-8")

            self.callbacks = []  # Callbacks pour UI
            self.initialized = True

            self.log("INFO", "System", "=== NiTriTe V18 - Nouvelle session démarrée ===")

    def log(
        self,
        level: LogLevel,
        category: str,
        message: str,
        details: Optional[Dict[str, Any]] = None
    ):
        """
        Log un événement

        Args:
            level: Niveau de log
            category: Catégorie (Installation, Network, UI, System, etc.)
            message: Message principal
            details: Détails additionnels (dict)
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format du log
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "category": category,
            "message": message,
            "details": details or {}
        }

        # Format texte
        log_line = f"[{timestamp}] [{level:8}] [{category:15}] {message}"
        if details:
            log_line += f" | {json.dumps(details, ensure_ascii=False)}"

        # Écriture dans fichier principal
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_line + "\n")
        except Exception as e:
            print(f"ERREUR LOGS: {e}")

        # Si erreur, log aussi dans fichier erreurs
        if level in ["ERROR", "CRITICAL"]:
            try:
                with open(self.error_file, "a", encoding="utf-8") as f:
                    f.write(log_line + "\n")
            except:
                pass

        # Notifier callbacks UI
        for callback in self.callbacks:
            try:
                callback(log_entry)
            except:
                pass

        # Print console
        print(log_line)

    def debug(self, category: str, message: str, **kwargs):
        """Log DEBUG"""
        self.log("DEBUG", category, message, kwargs if kwargs else None)

    def info(self, category: str, message: str, **kwargs):
        """Log INFO"""
        self.log("INFO", category, message, kwargs if kwargs else None)

    def success(self, category: str, message: str, **kwargs):
        """Log SUCCESS"""
        self.log("SUCCESS", category, message, kwargs if kwargs else None)

    def warning(self, category: str, message: str, **kwargs):
        """Log WARNING"""
        self.log("WARNING", category, message, kwargs if kwargs else None)

    def error(self, category: str, message: str, **kwargs):
        """Log ERROR"""
        self.log("ERROR", category, message, kwargs if kwargs else None)

    def critical(self, category: str, message: str, **kwargs):
        """Log CRITICAL"""
        self.log("CRITICAL", category, message, kwargs if kwargs else None)

    def log_exception(self, category: str, exception: Exception, context: str = ""):
        """Log une exception avec stack trace"""
        import traceback

        details = {
            "exception_type": type(exception).__name__,
            "exception_message": str(exception),
            "context": context,
            "traceback": traceback.format_exc()
        }

        self.error(category, f"Exception: {type(exception).__name__}: {str(exception)}", **details)

    def add_ui_callback(self, callback):
        """Ajoute un callback pour notifications UI"""
        self.callbacks.append(callback)

    def remove_ui_callback(self, callback):
        """Retire un callback"""
        if callback in self.callbacks:
            self.callbacks.remove(callback)

    def get_recent_logs(self, count: int = 100, level: Optional[LogLevel] = None) -> list:
        """
        Récupère les logs récents

        Args:
            count: Nombre de logs à récupérer
            level: Filtrer par niveau (None = tous)

        Returns:
            Liste des logs récents
        """
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if level:
                lines = [l for l in lines if f"[{level:8}]" in l]

            return lines[-count:]
        except:
            return []

    def get_error_count(self) -> Dict[str, int]:
        """Retourne le nombre d'erreurs par catégorie"""
        errors = {"ERROR": 0, "CRITICAL": 0, "WARNING": 0}

        try:
            with open(self.error_file, "r", encoding="utf-8") as f:
                for line in f:
                    if "[ERROR" in line:
                        errors["ERROR"] += 1
                    elif "[CRITICAL" in line:
                        errors["CRITICAL"] += 1
                    elif "[WARNING" in line:
                        errors["WARNING"] += 1
        except:
            pass

        return errors

    def save_diagnostic_snapshot(self, diagnostic_data: Dict[str, Any]):
        """Sauvegarde un snapshot de diagnostic PC"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        snapshot = {
            "timestamp": timestamp,
            "session_id": self.session_id,
            "data": diagnostic_data
        }

        try:
            # Charger diagnostics existants
            if self.diagnostic_file.exists():
                with open(self.diagnostic_file, "r", encoding="utf-8") as f:
                    diagnostics = json.load(f)
            else:
                diagnostics = []

            # Ajouter nouveau
            diagnostics.append(snapshot)

            # Garder seulement 50 derniers
            diagnostics = diagnostics[-50:]

            # Sauvegarder
            with open(self.diagnostic_file, "w", encoding="utf-8") as f:
                json.dump(diagnostics, f, indent=2, ensure_ascii=False)

            self.success("Diagnostic", "Snapshot sauvegardé", snapshot=timestamp)

        except Exception as e:
            self.error("Diagnostic", f"Erreur sauvegarde snapshot: {e}")

    def export_logs_zip(self, output_path: str) -> bool:
        """
        Exporte tous les logs dans un fichier ZIP

        Args:
            output_path: Chemin du fichier ZIP de sortie

        Returns:
            True si succès
        """
        import zipfile

        try:
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Ajouter tous les fichiers logs
                for log_file in self.log_dir.glob("*.log"):
                    zipf.write(log_file, log_file.name)

                # Ajouter fichier de diagnostic
                if self.diagnostic_file.exists():
                    zipf.write(self.diagnostic_file, self.diagnostic_file.name)

            self.success("Export", f"Logs exportés vers {output_path}")
            return True

        except Exception as e:
            self.error("Export", f"Erreur export logs: {e}")
            return False


# Instance globale
logger = CentralizedLogger()


# Fonction helper pour compatibility
def log_event(level: LogLevel, category: str, message: str, **kwargs):
    """Helper function pour logs"""
    logger.log(level, category, message, kwargs if kwargs else None)
