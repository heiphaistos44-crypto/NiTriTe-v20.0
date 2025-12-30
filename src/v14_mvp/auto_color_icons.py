#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module d'extraction automatique d'emojis pour icônes colorées
Extrait les emojis des labels pour créer des icônes colorées
"""

import re

def extract_emoji(text):
    """
    Extrait le premier emoji d'un texte

    Args:
        text (str): Texte contenant potentiellement un emoji

    Returns:
        tuple: (emoji, texte_nettoyé) ou ("", texte_original) si pas d'emoji

    Examples:
        >>> extract_emoji("🔧 Processeur")
        ("🔧", "Processeur")

        >>> extract_emoji("💾 RAM Totale")
        ("💾", "RAM Totale")

        >>> extract_emoji("Processeur")
        ("", "Processeur")
    """
    if not text or not isinstance(text, str):
        return "", text or ""

    # Pattern pour détecter les emojis
    # Couvre la plupart des emojis Unicode courants
    emoji_pattern = re.compile(
        "["
        "\U0001F1E0-\U0001F1FF"  # drapeaux (iOS)
        "\U0001F300-\U0001F5FF"  # symboles & pictogrammes
        "\U0001F600-\U0001F64F"  # émoticônes
        "\U0001F680-\U0001F6FF"  # transport & symboles de carte
        "\U0001F700-\U0001F77F"  # symboles alchimiques
        "\U0001F780-\U0001F7FF"  # formes géométriques étendues
        "\U0001F800-\U0001F8FF"  # flèches supplémentaires C
        "\U0001F900-\U0001F9FF"  # symboles & pictogrammes supplémentaires
        "\U0001FA00-\U0001FA6F"  # symboles d'échecs
        "\U0001FA70-\U0001FAFF"  # symboles & pictogrammes étendus A
        "\U00002702-\U000027B0"  # symboles Dingbats
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )

    # Chercher emoji au début du texte
    match = emoji_pattern.match(text.strip())

    if match:
        emoji = match.group()
        # Retirer l'emoji et les espaces
        clean_text = text[match.end():].strip()
        return emoji, clean_text

    return "", text


def has_emoji(text):
    """
    Vérifie si un texte contient un emoji

    Args:
        text (str): Texte à vérifier

    Returns:
        bool: True si contient un emoji, False sinon
    """
    emoji, _ = extract_emoji(text)
    return bool(emoji)


def replace_emoji_with_colored_icon(text, icon_manager):
    """
    Remplace l'emoji d'un texte par une icône colorée

    Args:
        text (str): Texte contenant un emoji
        icon_manager: Instance de ColoredIconsManager

    Returns:
        tuple: (icon_image, clean_text) ou (None, text) si pas d'emoji
    """
    emoji, clean_text = extract_emoji(text)

    if emoji:
        try:
            icon_image = icon_manager.create_colored_icon(emoji, size=20)
            return icon_image, clean_text
        except Exception:
            return None, text

    return None, text
