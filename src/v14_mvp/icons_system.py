#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système d'Icônes Colorées - NiTriTe V20.0
Génère des icônes colorées à partir d'emojis Unicode
"""

import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont
import io
from pathlib import Path
import sys

class ColoredIconsManager:
    """Gestionnaire d'icônes colorées pour remplacer les emojis monochromes"""

    # Cache des icônes générées
    _icon_cache = {}

    # Mapping emoji -> couleur de fond
    ICON_COLORS = {
        # Navigation
        "💻": "#4A90E2",  # Applications - Bleu
        "🛠️": "#F5A623",  # Outils - Orange
        "🎯": "#E74C3C",  # Master Install - Rouge
        "📦": "#9B59B6",  # Packages - Violet
        "🔌": "#3498DB",  # USB - Bleu clair
        "⚡": "#F39C12",  # Terminal/Performance - Jaune/Orange
        "⬆️": "#27AE60",  # Mises à jour - Vert
        "💼": "#34495E",  # Sauvegarde - Gris foncé
        "🚀": "#E67E22",  # Optimisations - Orange vif
        "🔬": "#1ABC9C",  # Diagnostic - Turquoise
        "📝": "#95A5A6",  # Logs - Gris
        "🪟": "#00A4EF",  # Windows - Bleu Windows
        "🧠": "#8E44AD",  # IA - Violet foncé
        "⚙️": "#7F8C8D",  # Paramètres - Gris

        # Mises à jour
        "🔎": "#3498DB",  # Rechercher - Bleu
        "🔍": "#3498DB",  # Rechercher alt - Bleu
        "🔄": "#2ECC71",  # WinGet - Vert
        "🍫": "#8B4513",  # Chocolatey - Marron
        "🪣": "#E74C3C",  # Scoop - Rouge
        "🐍": "#3776AB",  # Python - Bleu Python
        "🌐": "#4A90E2",  # Réseau - Bleu
        "🌍": "#4A90E2",  # Terre - Bleu
        "🌎": "#4A90E2",  # Terre alt - Bleu
        "🌏": "#4A90E2",  # Terre alt 2 - Bleu
        "🔊": "#E67E22",  # Audio - Orange
        "🎮": "#9B59B6",  # Vidéo/Gaming - Violet
        "🖨️": "#34495E",  # Imprimante - Gris
        "⬇️": "#27AE60",  # Télécharger - Vert
        "📡": "#3498DB",  # Bluetooth - Bleu
        "🏭": "#7F8C8D",  # Usine/Constructeurs - Gris

        # Diagnostic
        "💾": "#3498DB",  # Sauvegarder/Exporter - Bleu
        "♻️": "#27AE60",  # Restaurer - Vert
        "📂": "#F39C12",  # Dossier - Jaune
        "🔋": "#2ECC71",  # Batterie - Vert
        "🌡️": "#E67E22",  # Température - Orange
        "🛡️": "#3498DB",  # Sécurité/Protection - Bleu
        "📥": "#27AE60",  # Télécharger/Mettre à jour - Vert
        "👤": "#95A5A6",  # Utilisateur - Gris

        # Optimisations
        "🧹": "#E67E22",  # Nettoyage - Orange
        "▶️": "#27AE60",  # Exécuter - Vert
        "✅": "#27AE60",  # Validé/Sélection - Vert
        "👁️": "#3498DB",  # Voir/Affichage - Bleu

        # Dialogues
        "➕": "#27AE60",  # Ajouter - Vert
        "📁": "#F39C12",  # Parcourir - Jaune
        "❌": "#E74C3C",  # Annuler - Rouge
        "✖️": "#E74C3C",  # Fermer - Rouge

        # Autres
        "📋": "#95A5A6",  # Liste - Gris
        "ℹ️": "#3498DB",  # Info - Bleu
        "💡": "#F39C12",  # Recommandations - Jaune
        "📊": "#9B59B6",  # Graphiques - Violet
        "📈": "#27AE60",  # Graphique montant - Vert
        "📉": "#E74C3C",  # Graphique descendant - Rouge
        "📄": "#ECF0F1",  # Document - Blanc cassé
        "⚠️": "#F39C12",  # Avertissement - Orange
        "🔴": "#E74C3C",  # AMD Rouge
        "🐉": "#E74C3C",  # MSI Dragon - Rouge
        "🌟": "#F39C12",  # Acer Étoile - Jaune
        "📱": "#4A90E2",  # Mobile - Bleu
        "⌨️": "#34495E",  # Clavier - Gris
        "🖥️": "#4A90E2",  # Ordinateur - Bleu
        "📀": "#95A5A6",  # CD - Gris
        "💿": "#9B59B6",  # DVD/Disque - Violet
        "🗂️": "#F39C12",  # Classeur - Jaune
        "🗄️": "#7F8C8D",  # Armoire - Gris
        "📇": "#95A5A6",  # Cartes - Gris
        "🗃️": "#F39C12",  # Boîte classement - Jaune
        "🔒": "#E74C3C",  # Verrouillé - Rouge
        "🔓": "#27AE60",  # Déverrouillé - Vert
        "🔑": "#F39C12",  # Clé - Jaune
        "🔧": "#F5A623",  # Clé à molette - Orange
        "🔨": "#E67E22",  # Marteau - Orange

        # Catégories Applications
        "💬": "#3498DB",  # Communication - Bleu
        "🗑️": "#E74C3C",  # Corbeille - Rouge
        "🤖": "#9B59B6",  # Robot/IA - Violet
        "🎵": "#E91E63",  # Musique - Rose
        "🏢": "#34495E",  # Bureau/Entreprise - Gris foncé
        "👥": "#3498DB",  # Personnes/Réseaux sociaux - Bleu
        "🍎": "#95A5A6",  # Apple - Gris
        "☁️": "#5DADE2",  # Cloud - Bleu ciel
        "🎧": "#E91E63",  # Casque audio - Rose
        "🎬": "#8E44AD",  # Cinéma - Violet foncé
        "🔐": "#E74C3C",  # Cadenas - Rouge
    }

    @staticmethod
    def create_colored_icon(emoji: str, size: int = 24) -> ctk.CTkImage:
        """
        Créer une icône colorée à partir d'un emoji

        Args:
            emoji: L'emoji à convertir
            size: Taille de l'icône en pixels

        Returns:
            CTkImage: Image CustomTkinter colorée
        """
        # Vérifier le cache
        cache_key = f"{emoji}_{size}"
        if cache_key in ColoredIconsManager._icon_cache:
            return ColoredIconsManager._icon_cache[cache_key]

        # Obtenir la couleur de fond
        bg_color = ColoredIconsManager.ICON_COLORS.get(emoji, "#95A5A6")

        try:
            # Créer une image avec fond coloré
            img_size = size * 2  # Haute résolution pour meilleure qualité
            image = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)

            # Dessiner un cercle coloré de fond
            padding = img_size // 8
            draw.ellipse(
                [padding, padding, img_size - padding, img_size - padding],
                fill=bg_color,
                outline=None
            )

            # Essayer de charger une police qui supporte les emojis
            try:
                # Windows 10/11 font qui supporte les emojis
                font_size = int(img_size * 0.5)

                # Essayer plusieurs polices
                font_paths = [
                    "C:/Windows/Fonts/seguiemj.ttf",  # Segoe UI Emoji
                    "C:/Windows/Fonts/seguisym.ttf",  # Segoe UI Symbol
                ]

                font = None
                for font_path in font_paths:
                    try:
                        font = ImageFont.truetype(font_path, font_size)
                        break
                    except:
                        continue

                if font is None:
                    # Fallback à la police par défaut
                    font = ImageFont.load_default()

                # Dessiner l'emoji au centre
                # Calculer la position pour centrer le texte
                bbox = draw.textbbox((0, 0), emoji, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]

                x = (img_size - text_width) // 2
                y = (img_size - text_height) // 2 - bbox[1]

                # Dessiner l'emoji en blanc pour contraste
                draw.text((x, y), emoji, font=font, fill='white')

            except Exception as e:
                # Si échec, dessiner juste un point blanc au centre
                center = img_size // 2
                radius = img_size // 4
                draw.ellipse(
                    [center - radius, center - radius, center + radius, center + radius],
                    fill='white'
                )

            # Créer CTkImage
            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(size, size)
            )

            # Mettre en cache
            ColoredIconsManager._icon_cache[cache_key] = ctk_image

            return ctk_image

        except Exception as e:
            print(f"Erreur création icône pour {emoji}: {e}")
            # Retourner une image vide en cas d'erreur
            empty_img = Image.new('RGBA', (size, size), (150, 150, 150, 255))
            return ctk.CTkImage(light_image=empty_img, dark_image=empty_img, size=(size, size))

    @staticmethod
    def get_icon_label(parent, emoji: str, size: int = 24, **kwargs):
        """
        Créer un label avec icône colorée

        Args:
            parent: Widget parent
            emoji: Emoji à afficher
            size: Taille de l'icône
            **kwargs: Arguments supplémentaires pour CTkLabel

        Returns:
            CTkLabel: Label avec l'icône colorée
        """
        icon = ColoredIconsManager.create_colored_icon(emoji, size)

        label = ctk.CTkLabel(
            parent,
            image=icon,
            text="",
            **kwargs
        )
        label.image = icon  # Garder référence

        return label

    @staticmethod
    def create_icon_text_label(parent, emoji: str, text: str, icon_size: int = 20, **kwargs):
        """
        Créer un label avec icône colorée + texte

        Args:
            parent: Widget parent
            emoji: Emoji à afficher
            text: Texte à afficher
            icon_size: Taille de l'icône
            **kwargs: Arguments pour le frame conteneur

        Returns:
            CTkFrame: Frame contenant l'icône et le texte
        """
        from v14_mvp.design_system import DesignTokens

        frame = ctk.CTkFrame(parent, fg_color="transparent", **kwargs)

        # Icône
        icon_label = ColoredIconsManager.get_icon_label(frame, emoji, icon_size)
        icon_label.pack(side="left", padx=(0, 8))

        # Texte
        text_label = ctk.CTkLabel(
            frame,
            text=text,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        text_label.pack(side="left", fill="x", expand=True)

        return frame

    @staticmethod
    def clear_cache():
        """Vider le cache des icônes"""
        ColoredIconsManager._icon_cache.clear()


# Fonction helper pour faciliter l'utilisation
def create_icon(emoji: str, size: int = 24) -> ctk.CTkImage:
    """Créer une icône colorée (alias)"""
    return ColoredIconsManager.create_colored_icon(emoji, size)


def icon_label(parent, emoji: str, size: int = 24, **kwargs):
    """Créer un label avec icône colorée (alias)"""
    return ColoredIconsManager.get_icon_label(parent, emoji, size, **kwargs)
