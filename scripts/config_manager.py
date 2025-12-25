"""Gestionnaire de configuration pour les outils de diagnostic"""


import json
import os


class DiagnosticConfigManager:
    """Gère la configuration des outils de diagnostic"""
    
    def __init__(self, config_file="diag_config.json"):
        """Initialise le gestionaire de configuration"""
        self.config_file = config_file
        self.config = self._load_configuration()
    
    def _load_configuration(self):
        """Charge la configuration depuis le fichier"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        
        # Configuration par défaut
        return {
            "last_used_directory": ".",
            "auto_launch_tools": False,
            "update_check_interval": 24,  # Heures
            "language": "fr-FR",
            "tool_preferences": {}
        }
    
    def _save_configuration(self):
        """Enregistre la configuration dans le fichier"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def set_last_used_directory(self, directory):
        """Définit le dernier répertoire utilisé"""
        self.config['last_used_directory'] = directory
        self._save_configuration()
    
    def get_last_used_directory(self):
        """Récupère le dernier répertoire utilisé"""
        return self.config.get('last_used_directory', ".")
    
    def toggle_auto_launch(self):
        """Basculle l'autolancement des outils"""
        self.config['auto_launch_tools'] = not self.config.get('auto_launch_tools', False)
        self._save_configuration()
    
    def get_auto_launch_status(self):
        """Récupère le statut d'autolancement"""
        return self.config.get('auto_launch_tools', False)


# File: ui_components.py