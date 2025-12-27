#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Composants Modernes - NiTriTe V17 MVP
Composants réutilisables avec design moderne
"""

import customtkinter as ctk
import tkinter as tk
from typing import Callable, Optional
from v14_mvp.design_system import DesignTokens, ModernColors

# Import du système d'icônes colorées
try:
    from v14_mvp.icons_system import ColoredIconsManager
    COLORED_ICONS_AVAILABLE = True
except ImportError:
    COLORED_ICONS_AVAILABLE = False


class ModernButton(ctk.CTkButton):
    """Bouton moderne avec 3 variantes et support icônes colorées"""

    def __init__(self, parent, emoji=None, variant="filled", size="md", **kwargs):
        # Styles selon variante
        if variant == "filled":
            fg_color = DesignTokens.ACCENT_PRIMARY
            hover_color = DesignTokens.ACCENT_HOVER
            text_color = DesignTokens.TEXT_PRIMARY
            border_width = 0
        elif variant == "outlined":
            fg_color = "transparent"
            hover_color = DesignTokens.BG_HOVER
            text_color = DesignTokens.ACCENT_PRIMARY
            border_width = 2
            kwargs['border_color'] = DesignTokens.ACCENT_PRIMARY
        else:  # text
            fg_color = "transparent"
            hover_color = DesignTokens.BG_HOVER
            text_color = DesignTokens.TEXT_PRIMARY
            border_width = 0

        # Tailles
        sizes = {
            'sm': (100, 32, DesignTokens.FONT_SIZE_SM, 18),
            'md': (140, 40, DesignTokens.FONT_SIZE_MD, 20),
            'lg': (180, 48, DesignTokens.FONT_SIZE_LG, 22)
        }
        width, height, font_size, icon_size = sizes.get(size, sizes['md'])

        # Si un emoji est fourni ET que les icônes colorées sont disponibles
        if emoji and COLORED_ICONS_AVAILABLE:
            try:
                icon_image = ColoredIconsManager.create_colored_icon(emoji, size=icon_size)
                kwargs['image'] = icon_image
                kwargs['compound'] = "left"
                # Enlever l'emoji du texte s'il y est
                if 'text' in kwargs:
                    text = kwargs['text']
                    # Enlever l'emoji du début du texte
                    if text.startswith(emoji):
                        kwargs['text'] = text[len(emoji):].strip()
            except Exception as e:
                print(f"Erreur création icône colorée pour {emoji}: {e}")

        super().__init__(
            parent,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            border_width=border_width,
            corner_radius=DesignTokens.RADIUS_MD,
            width=width,
            height=height,
            font=(DesignTokens.FONT_FAMILY, font_size, "bold"),
            cursor="hand2",
            **kwargs
        )


class ModernCard(ctk.CTkFrame):
    """Carte moderne avec coins très arrondis"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_LG,
            **kwargs
        )


class ModernSearchBar(ctk.CTkFrame):
    """Barre de recherche moderne"""
    
    def __init__(self, parent, placeholder="Rechercher...", on_search=None, **kwargs):
        super().__init__(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_LG,
            **kwargs
        )
        
        self.on_search = on_search
        
        # Container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill=tk.BOTH, expand=True, padx=DesignTokens.SPACING_SM, pady=DesignTokens.SPACING_SM)
        
        # Icône
        icon = ctk.CTkLabel(
            container,
            text="",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_LG),
            text_color=DesignTokens.ACCENT_PRIMARY
        )
        icon.pack(side=tk.LEFT, padx=DesignTokens.SPACING_SM)
        
        # Entry
        self.entry = ctk.CTkEntry(
            container,
            placeholder_text=placeholder,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            fg_color="transparent",
            border_width=0
        )
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.entry.bind('<KeyRelease>', self._on_key_release)
        
        # Bouton clear
        self.clear_btn = ctk.CTkLabel(
            container,
            text="",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_TERTIARY,
            cursor="hand2"
        )
        self.clear_btn.pack(side=tk.RIGHT, padx=DesignTokens.SPACING_SM)
        self.clear_btn.bind('<Button-1>', self._clear)
    
    def _on_key_release(self, event):
        if self.on_search:
            self.on_search(self.entry.get())
    
    def _clear(self, event):
        self.entry.delete(0, tk.END)
        if self.on_search:
            self.on_search("")


class ModernStatsCard(ctk.CTkFrame):
    """Carte statistique moderne avec support icônes colorées"""

    def __init__(self, parent, title, value, icon, color, **kwargs):
        super().__init__(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_LG,
            **kwargs
        )

        # Extraire l'emoji du titre si présent
        emoji = None
        clean_title = title
        # Note: auto_color_icons.extract_emoji désactivé (module n'existe plus)
        # if title and COLORED_ICONS_AVAILABLE:
        #     try:
        #         from v14_mvp.auto_color_icons import extract_emoji
        #         emoji, clean_title = extract_emoji(title)
        #     except:
        #         pass

        # Container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill=tk.BOTH, expand=True, padx=DesignTokens.SPACING_MD, pady=DesignTokens.SPACING_MD)

        # Icône - utiliser icône colorée si emoji détecté
        if emoji and COLORED_ICONS_AVAILABLE:
            try:
                icon_image = ColoredIconsManager.create_colored_icon(emoji, size=28)
                icon_label = ctk.CTkLabel(
                    container,
                    image=icon_image,
                    text=""
                )
                icon_label.image = icon_image  # Garder référence
                icon_label.pack(side=tk.LEFT, padx=(0, DesignTokens.SPACING_MD))
            except Exception as e:
                print(f"Erreur creation icone coloree pour ModernStatsCard: {e}")
                # Fallback à l'icône texte
                icon_label = ctk.CTkLabel(
                    container,
                    text=icon if icon else emoji,
                    font=(DesignTokens.FONT_FAMILY, 24),
                    text_color=color
                )
                icon_label.pack(side=tk.LEFT, padx=(0, DesignTokens.SPACING_MD))
        else:
            # Icône texte classique
            icon_label = ctk.CTkLabel(
                container,
                text=icon,
                font=(DesignTokens.FONT_FAMILY, 24),
                text_color=color
            )
            icon_label.pack(side=tk.LEFT, padx=(0, DesignTokens.SPACING_MD))

        # Texte
        text_frame = ctk.CTkFrame(container, fg_color="transparent")
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        title_label = ctk.CTkLabel(
            text_frame,
            text=clean_title,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor='w'
        )
        title_label.pack(fill=tk.X)

        self.value_label = ctk.CTkLabel(
            text_frame,
            text=str(value),
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_2XL, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor='w'
        )
        self.value_label.pack(fill=tk.X)
    
    def update_value(self, new_value):
        """Mettre à jour la valeur"""
        self.value_label.configure(text=str(new_value))


class SectionHeader(ctk.CTkFrame):
    """En-tête de section avec icône colorée"""

    def __init__(self, parent, text, emoji=None, **kwargs):
        super().__init__(
            parent,
            fg_color="transparent",
            **kwargs
        )

        # Container horizontal
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Extraire emoji du texte si présent
        # Note: auto_color_icons.extract_emoji désactivé (module n'existe plus)
        # if not emoji and text:
        #     from v14_mvp.auto_color_icons import extract_emoji
        #     emoji, text = extract_emoji(text)

        # Icône colorée si emoji fourni
        if emoji and COLORED_ICONS_AVAILABLE:
            try:
                icon_image = ColoredIconsManager.create_colored_icon(emoji, size=24)
                icon_label = ctk.CTkLabel(
                    container,
                    image=icon_image,
                    text=""
                )
                icon_label.image = icon_image
                icon_label.pack(side=tk.LEFT, padx=(0, 12))
            except Exception as e:
                print(f"Erreur création icône section header: {e}")

        # Titre
        title_label = ctk.CTkLabel(
            container,
            text=text,
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title_label.pack(side=tk.LEFT, fill=tk.X, expand=True)