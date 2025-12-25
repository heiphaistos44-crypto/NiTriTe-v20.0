#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Thèmes Personnalisables - NiTriTe V17
Permet une personnalisation complète de l'apparence de l'application
"""

import json
import os
from pathlib import Path
from typing import Dict, Any


class ThemeManager:
    """Gestionnaire centralisé des thèmes personnalisables"""

    # Thèmes par défaut
    DEFAULT_THEMES = {
        "dark_professional": {
            "name": "Professionnel Sombre",
            "colors": {
                "primary": "#2563eb",
                "secondary": "#7c3aed",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444",
                "bg_primary": "#0f172a",
                "bg_secondary": "#1e293b",
                "bg_elevated": "#334155",
                "text_primary": "#f1f5f9",
                "text_secondary": "#cbd5e1",
                "border": "#475569",
                "accent": "#3b82f6"
            },
            "fonts": {
                "family": "Segoe UI",
                "size_xs": 10,
                "size_sm": 12,
                "size_md": 14,
                "size_lg": 16,
                "size_xl": 20,
                "size_xxl": 24
            },
            "spacing": {
                "xs": 4,
                "sm": 8,
                "md": 12,
                "lg": 16,
                "xl": 24,
                "xxl": 32
            },
            "border_radius": {
                "sm": 4,
                "md": 8,
                "lg": 12,
                "xl": 16
            },
            "scrollbar": {
                "width": 12,
                "bg_color": "#1e293b",
                "thumb_color": "#475569",
                "thumb_hover_color": "#64748b"
            }
        },
        "light_modern": {
            "name": "Moderne Clair",
            "colors": {
                "primary": "#2563eb",
                "secondary": "#7c3aed",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444",
                "bg_primary": "#ffffff",
                "bg_secondary": "#f8fafc",
                "bg_elevated": "#f1f5f9",
                "text_primary": "#0f172a",
                "text_secondary": "#475569",
                "border": "#cbd5e1",
                "accent": "#3b82f6"
            },
            "fonts": {
                "family": "Segoe UI",
                "size_xs": 10,
                "size_sm": 12,
                "size_md": 14,
                "size_lg": 16,
                "size_xl": 20,
                "size_xxl": 24
            },
            "spacing": {
                "xs": 4,
                "sm": 8,
                "md": 12,
                "lg": 16,
                "xl": 24,
                "xxl": 32
            },
            "border_radius": {
                "sm": 4,
                "md": 8,
                "lg": 12,
                "xl": 16
            },
            "scrollbar": {
                "width": 12,
                "bg_color": "#f1f5f9",
                "thumb_color": "#cbd5e1",
                "thumb_hover_color": "#94a3b8"
            }
        },
        "cyberpunk": {
            "name": "Cyberpunk",
            "colors": {
                "primary": "#00ffff",
                "secondary": "#ff00ff",
                "success": "#00ff00",
                "warning": "#ffff00",
                "error": "#ff0066",
                "bg_primary": "#0a0e27",
                "bg_secondary": "#1a1f3a",
                "bg_elevated": "#2a2f4a",
                "text_primary": "#00ffff",
                "text_secondary": "#00cccc",
                "border": "#00ffff",
                "accent": "#ff00ff"
            },
            "fonts": {
                "family": "Consolas",
                "size_xs": 10,
                "size_sm": 12,
                "size_md": 14,
                "size_lg": 16,
                "size_xl": 20,
                "size_xxl": 24
            },
            "spacing": {
                "xs": 6,
                "sm": 10,
                "md": 14,
                "lg": 18,
                "xl": 26,
                "xxl": 34
            },
            "border_radius": {
                "sm": 2,
                "md": 4,
                "lg": 6,
                "xl": 8
            },
            "scrollbar": {
                "width": 14,
                "bg_color": "#1a1f3a",
                "thumb_color": "#00ffff",
                "thumb_hover_color": "#ff00ff"
            }
        },
        "nature": {
            "name": "Nature",
            "colors": {
                "primary": "#059669",
                "secondary": "#0891b2",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#dc2626",
                "bg_primary": "#f0fdf4",
                "bg_secondary": "#ecfdf5",
                "bg_elevated": "#d1fae5",
                "text_primary": "#064e3b",
                "text_secondary": "#047857",
                "border": "#86efac",
                "accent": "#059669"
            },
            "fonts": {
                "family": "Segoe UI",
                "size_xs": 10,
                "size_sm": 12,
                "size_md": 14,
                "size_lg": 16,
                "size_xl": 20,
                "size_xxl": 24
            },
            "spacing": {
                "xs": 4,
                "sm": 8,
                "md": 12,
                "lg": 16,
                "xl": 24,
                "xxl": 32
            },
            "border_radius": {
                "sm": 6,
                "md": 10,
                "lg": 14,
                "xl": 18
            },
            "scrollbar": {
                "width": 12,
                "bg_color": "#ecfdf5",
                "thumb_color": "#86efac",
                "thumb_hover_color": "#34d399"
            }
        }
    }

    def __init__(self):
        self.config_path = os.path.join(os.path.expanduser("~"), ".nitrite_theme.json")
        self.current_theme = self._load_theme()

    def _load_theme(self) -> Dict[str, Any]:
        """Charger le thème depuis le fichier de configuration"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    saved_theme = json.load(f)
                    # Valider et compléter avec les valeurs par défaut si nécessaire
                    return self._merge_with_defaults(saved_theme)
            else:
                # Retourner le thème par défaut
                return self.DEFAULT_THEMES["dark_professional"].copy()
        except Exception as e:
            print(f"Erreur chargement thème: {e}")
            return self.DEFAULT_THEMES["dark_professional"].copy()

    def _merge_with_defaults(self, theme: Dict) -> Dict:
        """Fusionner un thème personnalisé avec les valeurs par défaut"""
        default = self.DEFAULT_THEMES["dark_professional"].copy()

        # Fusionner récursivement
        for key, value in theme.items():
            if key in default and isinstance(value, dict) and isinstance(default[key], dict):
                default[key].update(value)
            else:
                default[key] = value

        return default

    def save_theme(self, theme: Dict[str, Any]) -> bool:
        """Sauvegarder un thème personnalisé"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(theme, f, indent=2, ensure_ascii=False)
            self.current_theme = theme
            return True
        except Exception as e:
            print(f"Erreur sauvegarde thème: {e}")
            return False

    def get_theme(self, theme_name: str = None) -> Dict[str, Any]:
        """Obtenir un thème (prédéfini ou personnalisé)"""
        if theme_name and theme_name in self.DEFAULT_THEMES:
            return self.DEFAULT_THEMES[theme_name].copy()
        return self.current_theme.copy()

    def get_available_themes(self) -> Dict[str, str]:
        """Obtenir la liste des thèmes disponibles"""
        return {key: value["name"] for key, value in self.DEFAULT_THEMES.items()}

    def apply_theme(self, theme_name: str = None, custom_theme: Dict = None):
        """Appliquer un thème"""
        if custom_theme:
            self.current_theme = self._merge_with_defaults(custom_theme)
        elif theme_name and theme_name in self.DEFAULT_THEMES:
            self.current_theme = self.DEFAULT_THEMES[theme_name].copy()

        self.save_theme(self.current_theme)

    def get_color(self, color_key: str, default: str = "#000000") -> str:
        """Obtenir une couleur du thème actuel"""
        return self.current_theme.get("colors", {}).get(color_key, default)

    def get_font_size(self, size_key: str, default: int = 14) -> int:
        """Obtenir une taille de police du thème actuel"""
        return self.current_theme.get("fonts", {}).get(size_key, default)

    def get_spacing(self, spacing_key: str, default: int = 12) -> int:
        """Obtenir un espacement du thème actuel"""
        return self.current_theme.get("spacing", {}).get(spacing_key, default)

    def get_border_radius(self, radius_key: str, default: int = 8) -> int:
        """Obtenir un rayon de bordure du thème actuel"""
        return self.current_theme.get("border_radius", {}).get(radius_key, default)

    def get_scrollbar_config(self) -> Dict[str, Any]:
        """Obtenir la configuration de la scrollbar"""
        return self.current_theme.get("scrollbar", {
            "width": 12,
            "bg_color": "#1e293b",
            "thumb_color": "#475569",
            "thumb_hover_color": "#64748b"
        })

    def export_theme(self, filepath: str) -> bool:
        """Exporter le thème actuel vers un fichier"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.current_theme, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erreur export thème: {e}")
            return False

    def import_theme(self, filepath: str) -> bool:
        """Importer un thème depuis un fichier"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                imported_theme = json.load(f)
            self.apply_theme(custom_theme=imported_theme)
            return True
        except Exception as e:
            print(f"Erreur import thème: {e}")
            return False


# Instance globale du gestionnaire de thèmes
_theme_manager = None

def get_theme_manager() -> ThemeManager:
    """Obtenir l'instance globale du gestionnaire de thèmes"""
    global _theme_manager
    if _theme_manager is None:
        _theme_manager = ThemeManager()
    return _theme_manager
