#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icônes et emojis pour les catégories d'applications
Module centralisé pour éviter la duplication
"""

CATEGORY_EMOJIS = {
    "Antivirus": "🛡️",
    "Bureautique": "📝",
    "Communication": "💬",
    "Compression": "📦",
    "Désinstallateurs Antivirus": "🗑️",
    "Développement": "💻",
    "IA & Assistants": "🤖",
    "Imprimantes & Scan": "🖨️",
    "Internet": "🌍",
    "Jeux": "🎮",
    "Multimédia": "🎵",
    "Navigateurs": "🌐",
    "Outils OrdiPlus": "🏢",
    "PDF et Documents": "📄",
    "Pack Office": "📊",
    "Productivité": "⚡",
    "Réseaux Sociaux": "👥",
    "Services Apple": "🍎",
    "Stockage Cloud": "☁️",
    "Streaming Audio": "🎧",
    "Streaming Vidéo": "🎬",
    "Suites Professionnelles": "💼",
    "Sécurité": "🔐",
    "Utilitaires": "🔨",
    "Utilitaires Système": "⚙️"
}


def get_category_emoji(category_name: str) -> str:
    """
    Retourne l'emoji pour une catégorie donnée

    Args:
        category_name: Nom de la catégorie

    Returns:
        Emoji correspondant ou 📁 par défaut
    """
    return CATEGORY_EMOJIS.get(category_name, "📁")


def get_category_display_name(category_name: str) -> str:
    """
    Retourne le nom de catégorie avec son emoji

    Args:
        category_name: Nom de la catégorie

    Returns:
        Nom formaté avec emoji (ex: "🛡️ Antivirus")
    """
    emoji = get_category_emoji(category_name)
    return f"{emoji} {category_name}"
