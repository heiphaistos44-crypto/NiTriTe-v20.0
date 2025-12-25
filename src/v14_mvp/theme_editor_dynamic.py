#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Éditeur de Thème Dynamique - NiTriTe V18.5
Éditeur complet avec prévisualisation temps réel
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
import json
import os
from datetime import datetime
from typing import Callable, Dict, Any, Optional
from v14_mvp.design_system import DesignTokens


class ColorPicker(ctk.CTkFrame):
    """Widget de sélection de couleur avec aperçu"""

    def __init__(self, master, label: str, initial_color: str, on_change: Callable[[str], None]):
        super().__init__(master, fg_color="transparent")

        self.current_color = initial_color
        self.on_change = on_change

        # Label
        label_widget = ctk.CTkLabel(
            self,
            text=label,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        label_widget.pack(side=tk.LEFT, padx=(0, 10))

        # Aperçu couleur (bouton cliquable)
        self.preview_btn = ctk.CTkButton(
            self,
            text="",
            width=40,
            height=30,
            fg_color=self.current_color,
            hover_color=self.current_color,
            command=self.pick_color
        )
        self.preview_btn.pack(side=tk.LEFT, padx=5)

        # Code hex
        self.hex_label = ctk.CTkLabel(
            self,
            text=self.current_color,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            width=80
        )
        self.hex_label.pack(side=tk.LEFT, padx=5)

        # Bouton choisir
        choose_btn = ctk.CTkButton(
            self,
            text="Choisir",
            width=80,
            height=30,
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER,
            command=self.pick_color
        )
        choose_btn.pack(side=tk.LEFT, padx=5)

    def pick_color(self):
        """Ouvrir le sélecteur de couleur"""
        color = colorchooser.askcolor(
            color=self.current_color,
            title=f"Choisir une couleur"
        )
        if color[1]:
            self.set_color(color[1])

    def set_color(self, color: str):
        """Définir la couleur"""
        self.current_color = color
        self.preview_btn.configure(fg_color=color, hover_color=color)
        self.hex_label.configure(text=color)
        if self.on_change:
            self.on_change(color)

    def get_color(self) -> str:
        """Obtenir la couleur actuelle"""
        return self.current_color


class NumericSlider(ctk.CTkFrame):
    """Widget slider avec valeur numérique"""

    def __init__(self, master, label: str, min_val: int, max_val: int,
                 initial_val: int, on_change: Callable[[int], None]):
        super().__init__(master, fg_color="transparent")

        self.on_change = on_change

        # Container pour label et valeur
        top_container = ctk.CTkFrame(self, fg_color="transparent")
        top_container.pack(fill=tk.X, pady=(0, 5))

        # Label
        label_widget = ctk.CTkLabel(
            top_container,
            text=label,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        label_widget.pack(side=tk.LEFT)

        # Valeur
        self.value_label = ctk.CTkLabel(
            top_container,
            text=str(initial_val),
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY,
            width=50
        )
        self.value_label.pack(side=tk.RIGHT)

        # Slider
        self.slider = ctk.CTkSlider(
            self,
            from_=min_val,
            to=max_val,
            number_of_steps=max_val - min_val,
            command=self._on_slider_change,
            fg_color=DesignTokens.BG_ELEVATED,
            progress_color=DesignTokens.ACCENT_PRIMARY,
            button_color=DesignTokens.ACCENT_PRIMARY,
            button_hover_color=DesignTokens.ACCENT_HOVER
        )
        self.slider.set(initial_val)
        self.slider.pack(fill=tk.X)

    def _on_slider_change(self, value):
        """Callback changement slider"""
        int_value = int(value)
        self.value_label.configure(text=str(int_value))
        if self.on_change:
            self.on_change(int_value)

    def get_value(self) -> int:
        """Obtenir la valeur actuelle"""
        return int(self.slider.get())

    def set_value(self, value: int):
        """Définir la valeur"""
        self.slider.set(value)
        self.value_label.configure(text=str(value))


class ThemeEditorDynamic(ctk.CTkToplevel):
    """Éditeur de thème dynamique avec prévisualisation temps réel"""

    def __init__(self, parent, app_instance=None):
        super().__init__(parent)

        self.app_instance = app_instance

        # Configuration fenêtre
        self.title("Éditeur de Thème Dynamique - NiTriTe V18.5")
        self.geometry("1200x800")

        # Position centrée
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

        # Stockage du thème en cours d'édition
        self.current_theme = self.load_current_theme()

        # Widgets de contrôle (pour mise à jour)
        self.color_pickers = {}
        self.numeric_sliders = {}

        # Créer l'interface
        self._create_header()
        self._create_main_content()

        # Première mise à jour de la prévisualisation
        self.after(100, self.update_preview)

    def load_current_theme(self) -> Dict[str, Any]:
        """Charger le thème actuel depuis DesignTokens"""
        return {
            "name": "Thème Personnalisé",
            "created_at": datetime.now().isoformat(),
            "colors": {
                "bg_primary": DesignTokens.BG_PRIMARY,
                "bg_secondary": DesignTokens.BG_SECONDARY,
                "bg_tertiary": DesignTokens.BG_TERTIARY,
                "bg_elevated": DesignTokens.BG_ELEVATED,
                "bg_hover": DesignTokens.BG_HOVER,
                "accent_primary": DesignTokens.ACCENT_PRIMARY,
                "accent_hover": DesignTokens.ACCENT_HOVER,
                "accent_pressed": DesignTokens.ACCENT_PRESSED,
                "text_primary": DesignTokens.TEXT_PRIMARY,
                "text_secondary": DesignTokens.TEXT_SECONDARY,
                "text_tertiary": DesignTokens.TEXT_TERTIARY,
                "success": DesignTokens.SUCCESS,
                "warning": DesignTokens.WARNING,
                "error": DesignTokens.ERROR,
                "info": DesignTokens.INFO,
                "border_default": DesignTokens.BORDER_DEFAULT,
                "border_focus": DesignTokens.BORDER_FOCUS
            },
            "spacing": {
                "xs": DesignTokens.SPACING_XS,
                "sm": DesignTokens.SPACING_SM,
                "md": DesignTokens.SPACING_MD,
                "lg": DesignTokens.SPACING_LG,
                "xl": DesignTokens.SPACING_XL
            },
            "radius": {
                "sm": DesignTokens.RADIUS_SM,
                "md": DesignTokens.RADIUS_MD,
                "lg": DesignTokens.RADIUS_LG
            },
            "fonts": {
                "family": DesignTokens.FONT_FAMILY,
                "size_xs": DesignTokens.FONT_SIZE_XS,
                "size_sm": DesignTokens.FONT_SIZE_SM,
                "size_md": DesignTokens.FONT_SIZE_MD,
                "size_lg": DesignTokens.FONT_SIZE_LG,
                "size_xl": DesignTokens.FONT_SIZE_XL,
                "size_2xl": DesignTokens.FONT_SIZE_2XL
            }
        }

    def _create_header(self):
        """Créer l'en-tête avec titre et boutons d'action"""
        header = ctk.CTkFrame(self, fg_color=DesignTokens.BG_ELEVATED, height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)

        # Container principal
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Titre
        title_frame = ctk.CTkFrame(container, fg_color="transparent")
        title_frame.pack(side=tk.LEFT, fill=tk.Y)

        title = ctk.CTkLabel(
            title_frame,
            text="Éditeur de Thème",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            title_frame,
            text="Personnalisez l'apparence en temps réel",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(anchor="w")

        # Boutons d'action
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Ligne 1
        btn_row1 = ctk.CTkFrame(btn_frame, fg_color="transparent")
        btn_row1.pack(fill=tk.X, pady=(0, 5))

        ctk.CTkButton(
            btn_row1,
            text="Nouveau",
            width=100,
            command=self.new_theme,
            fg_color=DesignTokens.BG_SECONDARY,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            btn_row1,
            text="Charger",
            width=100,
            command=self.load_theme,
            fg_color=DesignTokens.INFO,
            hover_color="#1976d2"
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            btn_row1,
            text="Sauvegarder",
            width=100,
            command=self.save_theme,
            fg_color=DesignTokens.SUCCESS,
            hover_color="#388e3c"
        ).pack(side=tk.LEFT, padx=2)

        # Ligne 2
        btn_row2 = ctk.CTkFrame(btn_frame, fg_color="transparent")
        btn_row2.pack(fill=tk.X)

        ctk.CTkButton(
            btn_row2,
            text="Exporter",
            width=100,
            command=self.export_theme,
            fg_color=DesignTokens.WARNING,
            hover_color="#f57c00"
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            btn_row2,
            text="Appliquer",
            width=202,
            command=self.apply_theme,
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER
        ).pack(side=tk.LEFT, padx=2)

    def _create_main_content(self):
        """Créer le contenu principal (tabs + prévisualisation)"""
        main_container = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        main_container.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        # Panel gauche: Tabs d'édition
        left_panel = ctk.CTkFrame(main_container, fg_color=DesignTokens.BG_SECONDARY, width=600)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # TabView
        self.tabview = ctk.CTkTabview(
            left_panel,
            fg_color=DesignTokens.BG_SECONDARY,
            segmented_button_fg_color=DesignTokens.BG_ELEVATED,
            segmented_button_selected_color=DesignTokens.ACCENT_PRIMARY,
            segmented_button_selected_hover_color=DesignTokens.ACCENT_HOVER
        )
        self.tabview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Créer les onglets
        self.tabview.add("Couleurs")
        self.tabview.add("Espacements")
        self.tabview.add("Bordures")
        self.tabview.add("Polices")
        self.tabview.add("Presets")

        # Remplir les onglets
        self._create_colors_tab(self.tabview.tab("Couleurs"))
        self._create_spacing_tab(self.tabview.tab("Espacements"))
        self._create_borders_tab(self.tabview.tab("Bordures"))
        self._create_fonts_tab(self.tabview.tab("Polices"))
        self._create_presets_tab(self.tabview.tab("Presets"))

        # Panel droit: Prévisualisation
        right_panel = ctk.CTkFrame(
            main_container,
            fg_color=DesignTokens.BG_ELEVATED,
            width=500,
            corner_radius=DesignTokens.RADIUS_LG
        )
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(0, 10), pady=10)
        right_panel.pack_propagate(False)

        # Titre prévisualisation
        preview_title = ctk.CTkLabel(
            right_panel,
            text="Prévisualisation",
            font=(DesignTokens.FONT_FAMILY, 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        preview_title.pack(pady=(15, 10))

        # Container scroll pour la prévisualisation
        self.preview_scroll = ctk.CTkScrollableFrame(
            right_panel,
            fg_color=DesignTokens.BG_PRIMARY
        )
        self.preview_scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        # Créer les widgets de prévisualisation
        self._create_preview_widgets()

    def _create_colors_tab(self, parent):
        """Onglet Couleurs (16 paramètres)"""
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Titre section
        ctk.CTkLabel(
            scroll,
            text="Couleurs de Fond",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        # Fonds
        self.color_pickers["bg_primary"] = ColorPicker(
            scroll, "Fond Principal", self.current_theme["colors"]["bg_primary"],
            lambda c: self.on_color_change("bg_primary", c)
        )
        self.color_pickers["bg_primary"].pack(fill=tk.X, pady=5)

        self.color_pickers["bg_secondary"] = ColorPicker(
            scroll, "Fond Secondaire", self.current_theme["colors"]["bg_secondary"],
            lambda c: self.on_color_change("bg_secondary", c)
        )
        self.color_pickers["bg_secondary"].pack(fill=tk.X, pady=5)

        self.color_pickers["bg_tertiary"] = ColorPicker(
            scroll, "Fond Tertiaire", self.current_theme["colors"]["bg_tertiary"],
            lambda c: self.on_color_change("bg_tertiary", c)
        )
        self.color_pickers["bg_tertiary"].pack(fill=tk.X, pady=5)

        self.color_pickers["bg_elevated"] = ColorPicker(
            scroll, "Fond Élevé", self.current_theme["colors"]["bg_elevated"],
            lambda c: self.on_color_change("bg_elevated", c)
        )
        self.color_pickers["bg_elevated"].pack(fill=tk.X, pady=5)

        self.color_pickers["bg_hover"] = ColorPicker(
            scroll, "Fond Survol", self.current_theme["colors"]["bg_hover"],
            lambda c: self.on_color_change("bg_hover", c)
        )
        self.color_pickers["bg_hover"].pack(fill=tk.X, pady=5)

        # Séparateur
        ctk.CTkFrame(scroll, height=2, fg_color=DesignTokens.BORDER_DEFAULT).pack(fill=tk.X, pady=15)

        # Titre section
        ctk.CTkLabel(
            scroll,
            text="Couleurs d'Accent",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        # Accents
        self.color_pickers["accent_primary"] = ColorPicker(
            scroll, "Accent Principal", self.current_theme["colors"]["accent_primary"],
            lambda c: self.on_color_change("accent_primary", c)
        )
        self.color_pickers["accent_primary"].pack(fill=tk.X, pady=5)

        self.color_pickers["accent_hover"] = ColorPicker(
            scroll, "Accent Survol", self.current_theme["colors"]["accent_hover"],
            lambda c: self.on_color_change("accent_hover", c)
        )
        self.color_pickers["accent_hover"].pack(fill=tk.X, pady=5)

        self.color_pickers["accent_pressed"] = ColorPicker(
            scroll, "Accent Pressé", self.current_theme["colors"]["accent_pressed"],
            lambda c: self.on_color_change("accent_pressed", c)
        )
        self.color_pickers["accent_pressed"].pack(fill=tk.X, pady=5)

        # Séparateur
        ctk.CTkFrame(scroll, height=2, fg_color=DesignTokens.BORDER_DEFAULT).pack(fill=tk.X, pady=15)

        # Titre section
        ctk.CTkLabel(
            scroll,
            text="Couleurs de Texte",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        # Textes
        self.color_pickers["text_primary"] = ColorPicker(
            scroll, "Texte Principal", self.current_theme["colors"]["text_primary"],
            lambda c: self.on_color_change("text_primary", c)
        )
        self.color_pickers["text_primary"].pack(fill=tk.X, pady=5)

        self.color_pickers["text_secondary"] = ColorPicker(
            scroll, "Texte Secondaire", self.current_theme["colors"]["text_secondary"],
            lambda c: self.on_color_change("text_secondary", c)
        )
        self.color_pickers["text_secondary"].pack(fill=tk.X, pady=5)

        self.color_pickers["text_tertiary"] = ColorPicker(
            scroll, "Texte Tertiaire", self.current_theme["colors"]["text_tertiary"],
            lambda c: self.on_color_change("text_tertiary", c)
        )
        self.color_pickers["text_tertiary"].pack(fill=tk.X, pady=5)

        # Séparateur
        ctk.CTkFrame(scroll, height=2, fg_color=DesignTokens.BORDER_DEFAULT).pack(fill=tk.X, pady=15)

        # Titre section
        ctk.CTkLabel(
            scroll,
            text="Couleurs Sémantiques",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        # Sémantiques
        self.color_pickers["success"] = ColorPicker(
            scroll, "Succès", self.current_theme["colors"]["success"],
            lambda c: self.on_color_change("success", c)
        )
        self.color_pickers["success"].pack(fill=tk.X, pady=5)

        self.color_pickers["warning"] = ColorPicker(
            scroll, "Avertissement", self.current_theme["colors"]["warning"],
            lambda c: self.on_color_change("warning", c)
        )
        self.color_pickers["warning"].pack(fill=tk.X, pady=5)

        self.color_pickers["error"] = ColorPicker(
            scroll, "Erreur", self.current_theme["colors"]["error"],
            lambda c: self.on_color_change("error", c)
        )
        self.color_pickers["error"].pack(fill=tk.X, pady=5)

        self.color_pickers["info"] = ColorPicker(
            scroll, "Information", self.current_theme["colors"]["info"],
            lambda c: self.on_color_change("info", c)
        )
        self.color_pickers["info"].pack(fill=tk.X, pady=5)

        # Séparateur
        ctk.CTkFrame(scroll, height=2, fg_color=DesignTokens.BORDER_DEFAULT).pack(fill=tk.X, pady=15)

        # Titre section
        ctk.CTkLabel(
            scroll,
            text="Couleurs de Bordure",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        # Bordures
        self.color_pickers["border_default"] = ColorPicker(
            scroll, "Bordure Par Défaut", self.current_theme["colors"]["border_default"],
            lambda c: self.on_color_change("border_default", c)
        )
        self.color_pickers["border_default"].pack(fill=tk.X, pady=5)

        self.color_pickers["border_focus"] = ColorPicker(
            scroll, "Bordure Focus", self.current_theme["colors"]["border_focus"],
            lambda c: self.on_color_change("border_focus", c)
        )
        self.color_pickers["border_focus"].pack(fill=tk.X, pady=5)

    def _create_spacing_tab(self, parent):
        """Onglet Espacements (5 paramètres)"""
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll,
            text="Espacements (Pixels)",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 20))

        self.numeric_sliders["spacing_xs"] = NumericSlider(
            scroll, "Extra Small (XS)", 2, 8,
            self.current_theme["spacing"]["xs"],
            lambda v: self.on_spacing_change("xs", v)
        )
        self.numeric_sliders["spacing_xs"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["spacing_sm"] = NumericSlider(
            scroll, "Small (SM)", 4, 16,
            self.current_theme["spacing"]["sm"],
            lambda v: self.on_spacing_change("sm", v)
        )
        self.numeric_sliders["spacing_sm"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["spacing_md"] = NumericSlider(
            scroll, "Medium (MD)", 8, 32,
            self.current_theme["spacing"]["md"],
            lambda v: self.on_spacing_change("md", v)
        )
        self.numeric_sliders["spacing_md"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["spacing_lg"] = NumericSlider(
            scroll, "Large (LG)", 16, 48,
            self.current_theme["spacing"]["lg"],
            lambda v: self.on_spacing_change("lg", v)
        )
        self.numeric_sliders["spacing_lg"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["spacing_xl"] = NumericSlider(
            scroll, "Extra Large (XL)", 24, 64,
            self.current_theme["spacing"]["xl"],
            lambda v: self.on_spacing_change("xl", v)
        )
        self.numeric_sliders["spacing_xl"].pack(fill=tk.X, pady=10)

    def _create_borders_tab(self, parent):
        """Onglet Bordures (3 rayons)"""
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll,
            text="Rayons de Bordure (Pixels)",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 20))

        self.numeric_sliders["radius_sm"] = NumericSlider(
            scroll, "Small (SM)", 0, 16,
            self.current_theme["radius"]["sm"],
            lambda v: self.on_radius_change("sm", v)
        )
        self.numeric_sliders["radius_sm"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["radius_md"] = NumericSlider(
            scroll, "Medium (MD)", 4, 32,
            self.current_theme["radius"]["md"],
            lambda v: self.on_radius_change("md", v)
        )
        self.numeric_sliders["radius_md"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["radius_lg"] = NumericSlider(
            scroll, "Large (LG)", 8, 48,
            self.current_theme["radius"]["lg"],
            lambda v: self.on_radius_change("lg", v)
        )
        self.numeric_sliders["radius_lg"].pack(fill=tk.X, pady=10)

    def _create_fonts_tab(self, parent):
        """Onglet Polices (1 famille + 6 tailles)"""
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Famille de police
        ctk.CTkLabel(
            scroll,
            text="Famille de Police",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 10))

        self.font_family_var = tk.StringVar(value=self.current_theme["fonts"]["family"])

        font_selector = ctk.CTkOptionMenu(
            scroll,
            values=["Segoe UI", "Arial", "Helvetica", "Calibri", "Consolas", "Courier New"],
            variable=self.font_family_var,
            command=self.on_font_family_change,
            fg_color=DesignTokens.BG_ELEVATED,
            button_color=DesignTokens.ACCENT_PRIMARY,
            button_hover_color=DesignTokens.ACCENT_HOVER
        )
        font_selector.pack(fill=tk.X, pady=(0, 20))

        # Séparateur
        ctk.CTkFrame(scroll, height=2, fg_color=DesignTokens.BORDER_DEFAULT).pack(fill=tk.X, pady=15)

        # Tailles de police
        ctk.CTkLabel(
            scroll,
            text="Tailles de Police (Pixels)",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 20))

        self.numeric_sliders["font_xs"] = NumericSlider(
            scroll, "Extra Small (XS)", 8, 14,
            self.current_theme["fonts"]["size_xs"],
            lambda v: self.on_font_size_change("size_xs", v)
        )
        self.numeric_sliders["font_xs"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["font_sm"] = NumericSlider(
            scroll, "Small (SM)", 9, 16,
            self.current_theme["fonts"]["size_sm"],
            lambda v: self.on_font_size_change("size_sm", v)
        )
        self.numeric_sliders["font_sm"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["font_md"] = NumericSlider(
            scroll, "Medium (MD)", 11, 18,
            self.current_theme["fonts"]["size_md"],
            lambda v: self.on_font_size_change("size_md", v)
        )
        self.numeric_sliders["font_md"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["font_lg"] = NumericSlider(
            scroll, "Large (LG)", 14, 22,
            self.current_theme["fonts"]["size_lg"],
            lambda v: self.on_font_size_change("size_lg", v)
        )
        self.numeric_sliders["font_lg"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["font_xl"] = NumericSlider(
            scroll, "Extra Large (XL)", 18, 28,
            self.current_theme["fonts"]["size_xl"],
            lambda v: self.on_font_size_change("size_xl", v)
        )
        self.numeric_sliders["font_xl"].pack(fill=tk.X, pady=10)

        self.numeric_sliders["font_2xl"] = NumericSlider(
            scroll, "2X Large (2XL)", 20, 36,
            self.current_theme["fonts"]["size_2xl"],
            lambda v: self.on_font_size_change("size_2xl", v)
        )
        self.numeric_sliders["font_2xl"].pack(fill=tk.X, pady=10)

    def _create_presets_tab(self, parent):
        """Onglet Presets (6 thèmes pré-configurés)"""
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            scroll,
            text="Thèmes Pré-configurés",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(0, 20))

        presets = [
            ("Orange NiTriTe", "#ff6b35", "#ff8555", "#ff5020"),
            ("Bleu Pro", "#2196f3", "#42a5f5", "#1976d2"),
            ("Vert Tech", "#4caf50", "#66bb6a", "#388e3c"),
            ("Violet Creative", "#9c27b0", "#ab47bc", "#7b1fa2"),
            ("Rouge Energy", "#f44336", "#e57373", "#d32f2f"),
            ("Cyan Fresh", "#00bcd4", "#26c6da", "#0097a7")
        ]

        for name, primary, hover, pressed in presets:
            self._create_preset_button(scroll, name, primary, hover, pressed)

    def _create_preset_button(self, parent, name: str, primary: str, hover: str, pressed: str):
        """Créer un bouton de preset"""
        frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
        frame.pack(fill=tk.X, pady=5)

        # Container
        container = ctk.CTkFrame(frame, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=10)

        # Nom
        ctk.CTkLabel(
            container,
            text=name,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(side=tk.LEFT)

        # Aperçu couleurs
        preview_frame = ctk.CTkFrame(container, fg_color="transparent")
        preview_frame.pack(side=tk.LEFT, padx=20)

        for color in [primary, hover, pressed]:
            color_box = ctk.CTkFrame(preview_frame, fg_color=color, width=30, height=30, corner_radius=5)
            color_box.pack(side=tk.LEFT, padx=2)

        # Bouton appliquer
        ctk.CTkButton(
            container,
            text="Appliquer",
            width=100,
            command=lambda: self.apply_preset(name, primary, hover, pressed),
            fg_color=primary,
            hover_color=hover
        ).pack(side=tk.RIGHT)

    def _create_preview_widgets(self):
        """Créer les widgets de prévisualisation"""
        # Titre
        self.preview_title = ctk.CTkLabel(
            self.preview_scroll,
            text="Exemple de Titre",
            font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_2xl"], "bold"),
            text_color=self.current_theme["colors"]["text_primary"]
        )
        self.preview_title.pack(pady=15)

        # Carte exemple
        self.preview_card = ctk.CTkFrame(
            self.preview_scroll,
            fg_color=self.current_theme["colors"]["bg_elevated"],
            corner_radius=self.current_theme["radius"]["md"]
        )
        self.preview_card.pack(fill=tk.X, padx=20, pady=10)

        card_content = ctk.CTkFrame(self.preview_card, fg_color="transparent")
        card_content.pack(fill=tk.X, padx=20, pady=15)

        self.preview_card_title = ctk.CTkLabel(
            card_content,
            text="Carte Exemple",
            font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_lg"], "bold"),
            text_color=self.current_theme["colors"]["text_primary"],
            anchor="w"
        )
        self.preview_card_title.pack(fill=tk.X, pady=(0, 5))

        self.preview_card_subtitle = ctk.CTkLabel(
            card_content,
            text="Ceci est un exemple de carte avec du texte secondaire",
            font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_md"]),
            text_color=self.current_theme["colors"]["text_secondary"],
            anchor="w"
        )
        self.preview_card_subtitle.pack(fill=tk.X)

        # Boutons
        btn_frame = ctk.CTkFrame(self.preview_scroll, fg_color="transparent")
        btn_frame.pack(fill=tk.X, padx=20, pady=10)

        self.preview_btn_primary = ctk.CTkButton(
            btn_frame,
            text="Bouton Principal",
            fg_color=self.current_theme["colors"]["accent_primary"],
            hover_color=self.current_theme["colors"]["accent_hover"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_primary.pack(side=tk.LEFT, padx=5)

        self.preview_btn_secondary = ctk.CTkButton(
            btn_frame,
            text="Bouton Secondaire",
            fg_color=self.current_theme["colors"]["bg_elevated"],
            hover_color=self.current_theme["colors"]["bg_hover"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_secondary.pack(side=tk.LEFT, padx=5)

        # Boutons sémantiques
        semantic_frame = ctk.CTkFrame(self.preview_scroll, fg_color="transparent")
        semantic_frame.pack(fill=tk.X, padx=20, pady=10)

        self.preview_btn_success = ctk.CTkButton(
            semantic_frame,
            text="Succès",
            width=100,
            fg_color=self.current_theme["colors"]["success"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_success.pack(side=tk.LEFT, padx=5)

        self.preview_btn_warning = ctk.CTkButton(
            semantic_frame,
            text="Attention",
            width=100,
            fg_color=self.current_theme["colors"]["warning"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_warning.pack(side=tk.LEFT, padx=5)

        self.preview_btn_error = ctk.CTkButton(
            semantic_frame,
            text="Erreur",
            width=100,
            fg_color=self.current_theme["colors"]["error"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_error.pack(side=tk.LEFT, padx=5)

        self.preview_btn_info = ctk.CTkButton(
            semantic_frame,
            text="Info",
            width=100,
            fg_color=self.current_theme["colors"]["info"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_btn_info.pack(side=tk.LEFT, padx=5)

        # Champ de saisie
        self.preview_entry = ctk.CTkEntry(
            self.preview_scroll,
            placeholder_text="Champ de saisie",
            fg_color=self.current_theme["colors"]["bg_secondary"],
            border_color=self.current_theme["colors"]["border_default"],
            corner_radius=self.current_theme["radius"]["sm"]
        )
        self.preview_entry.pack(fill=tk.X, padx=20, pady=10)

        # Switch
        self.preview_switch = ctk.CTkSwitch(
            self.preview_scroll,
            text="Interrupteur",
            fg_color=self.current_theme["colors"]["bg_elevated"],
            progress_color=self.current_theme["colors"]["accent_primary"]
        )
        self.preview_switch.pack(anchor="w", padx=20, pady=5)

        # Slider
        self.preview_slider = ctk.CTkSlider(
            self.preview_scroll,
            from_=0,
            to=100,
            fg_color=self.current_theme["colors"]["bg_elevated"],
            progress_color=self.current_theme["colors"]["accent_primary"],
            button_color=self.current_theme["colors"]["accent_primary"],
            button_hover_color=self.current_theme["colors"]["accent_hover"]
        )
        self.preview_slider.pack(fill=tk.X, padx=20, pady=10)

        # Progress bar
        self.preview_progress = ctk.CTkProgressBar(
            self.preview_scroll,
            fg_color=self.current_theme["colors"]["bg_elevated"],
            progress_color=self.current_theme["colors"]["accent_primary"]
        )
        self.preview_progress.set(0.6)
        self.preview_progress.pack(fill=tk.X, padx=20, pady=10)

    def update_preview(self):
        """Mettre à jour la prévisualisation en temps réel"""
        try:
            # Titre
            self.preview_title.configure(
                font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_2xl"], "bold"),
                text_color=self.current_theme["colors"]["text_primary"]
            )

            # Carte
            self.preview_card.configure(
                fg_color=self.current_theme["colors"]["bg_elevated"],
                corner_radius=self.current_theme["radius"]["md"]
            )

            self.preview_card_title.configure(
                font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_lg"], "bold"),
                text_color=self.current_theme["colors"]["text_primary"]
            )

            self.preview_card_subtitle.configure(
                font=(self.current_theme["fonts"]["family"], self.current_theme["fonts"]["size_md"]),
                text_color=self.current_theme["colors"]["text_secondary"]
            )

            # Boutons
            self.preview_btn_primary.configure(
                fg_color=self.current_theme["colors"]["accent_primary"],
                hover_color=self.current_theme["colors"]["accent_hover"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            self.preview_btn_secondary.configure(
                fg_color=self.current_theme["colors"]["bg_elevated"],
                hover_color=self.current_theme["colors"]["bg_hover"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            # Boutons sémantiques
            self.preview_btn_success.configure(
                fg_color=self.current_theme["colors"]["success"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            self.preview_btn_warning.configure(
                fg_color=self.current_theme["colors"]["warning"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            self.preview_btn_error.configure(
                fg_color=self.current_theme["colors"]["error"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            self.preview_btn_info.configure(
                fg_color=self.current_theme["colors"]["info"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            # Champ de saisie
            self.preview_entry.configure(
                fg_color=self.current_theme["colors"]["bg_secondary"],
                border_color=self.current_theme["colors"]["border_default"],
                corner_radius=self.current_theme["radius"]["sm"]
            )

            # Switch
            self.preview_switch.configure(
                fg_color=self.current_theme["colors"]["bg_elevated"],
                progress_color=self.current_theme["colors"]["accent_primary"]
            )

            # Slider
            self.preview_slider.configure(
                fg_color=self.current_theme["colors"]["bg_elevated"],
                progress_color=self.current_theme["colors"]["accent_primary"],
                button_color=self.current_theme["colors"]["accent_primary"],
                button_hover_color=self.current_theme["colors"]["accent_hover"]
            )

            # Progress bar
            self.preview_progress.configure(
                fg_color=self.current_theme["colors"]["bg_elevated"],
                progress_color=self.current_theme["colors"]["accent_primary"]
            )

        except Exception as e:
            print(f"Erreur mise à jour preview: {e}")

    # === CALLBACKS ===

    def on_color_change(self, color_key: str, color_value: str):
        """Callback changement de couleur"""
        self.current_theme["colors"][color_key] = color_value
        self.update_preview()

    def on_spacing_change(self, spacing_key: str, spacing_value: int):
        """Callback changement d'espacement"""
        self.current_theme["spacing"][spacing_key] = spacing_value
        self.update_preview()

    def on_radius_change(self, radius_key: str, radius_value: int):
        """Callback changement de rayon"""
        self.current_theme["radius"][radius_key] = radius_value
        self.update_preview()

    def on_font_family_change(self, family: str):
        """Callback changement de famille de police"""
        self.current_theme["fonts"]["family"] = family
        self.update_preview()

    def on_font_size_change(self, size_key: str, size_value: int):
        """Callback changement de taille de police"""
        self.current_theme["fonts"][size_key] = size_value
        self.update_preview()

    def apply_preset(self, name: str, primary: str, hover: str, pressed: str):
        """Appliquer un preset de thème"""
        self.current_theme["colors"]["accent_primary"] = primary
        self.current_theme["colors"]["accent_hover"] = hover
        self.current_theme["colors"]["accent_pressed"] = pressed
        self.current_theme["colors"]["border_focus"] = primary

        # Mettre à jour les color pickers
        self.color_pickers["accent_primary"].set_color(primary)
        self.color_pickers["accent_hover"].set_color(hover)
        self.color_pickers["accent_pressed"].set_color(pressed)
        self.color_pickers["border_focus"].set_color(primary)

        self.update_preview()

        messagebox.showinfo(
            "Preset Appliqué",
            f"Le preset '{name}' a été appliqué aux couleurs d'accent."
        )

    # === ACTIONS ===

    def new_theme(self):
        """Créer un nouveau thème (reset)"""
        if messagebox.askyesno(
            "Nouveau Thème",
            "Voulez-vous réinitialiser le thème aux valeurs par défaut?"
        ):
            self.current_theme = self.load_current_theme()

            # Réinitialiser tous les widgets
            for key, picker in self.color_pickers.items():
                picker.set_color(self.current_theme["colors"][key])

            for key, slider in self.numeric_sliders.items():
                if "spacing_" in key:
                    slider.set_value(self.current_theme["spacing"][key.replace("spacing_", "")])
                elif "radius_" in key:
                    slider.set_value(self.current_theme["radius"][key.replace("radius_", "")])
                elif "font_" in key:
                    font_key = key.replace("font_", "size_")
                    slider.set_value(self.current_theme["fonts"][font_key])

            self.font_family_var.set(self.current_theme["fonts"]["family"])

            self.update_preview()

            messagebox.showinfo("Nouveau Thème", "Le thème a été réinitialisé.")

    def load_theme(self):
        """Charger un thème depuis un fichier"""
        themes_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "themes")

        if not os.path.exists(themes_dir):
            messagebox.showwarning(
                "Aucun Thème",
                "Le dossier de thèmes n'existe pas encore. Sauvegardez d'abord un thème."
            )
            return

        filepath = filedialog.askopenfilename(
            title="Charger un thème",
            initialdir=themes_dir,
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )

        if not filepath:
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                loaded_theme = json.load(f)

            self.current_theme = loaded_theme

            # Mettre à jour tous les widgets
            for key, picker in self.color_pickers.items():
                if key in self.current_theme["colors"]:
                    picker.set_color(self.current_theme["colors"][key])

            for key, slider in self.numeric_sliders.items():
                if "spacing_" in key:
                    spacing_key = key.replace("spacing_", "")
                    if spacing_key in self.current_theme["spacing"]:
                        slider.set_value(self.current_theme["spacing"][spacing_key])
                elif "radius_" in key:
                    radius_key = key.replace("radius_", "")
                    if radius_key in self.current_theme["radius"]:
                        slider.set_value(self.current_theme["radius"][radius_key])
                elif "font_" in key:
                    font_key = key.replace("font_", "size_")
                    if font_key in self.current_theme["fonts"]:
                        slider.set_value(self.current_theme["fonts"][font_key])

            if "family" in self.current_theme["fonts"]:
                self.font_family_var.set(self.current_theme["fonts"]["family"])

            self.update_preview()

            messagebox.showinfo(
                "Thème Chargé",
                f"Le thème '{loaded_theme.get('name', 'Sans nom')}' a été chargé."
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de charger le thème:\n{str(e)}"
            )

    def save_theme(self):
        """Sauvegarder le thème actuel"""
        themes_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "themes")

        # Créer le dossier si nécessaire
        os.makedirs(themes_dir, exist_ok=True)

        # Demander le nom du thème
        dialog = ctk.CTkInputDialog(
            text="Nom du thème:",
            title="Sauvegarder le thème"
        )
        theme_name = dialog.get_input()

        if not theme_name:
            return

        self.current_theme["name"] = theme_name
        self.current_theme["created_at"] = datetime.now().isoformat()

        # Créer le nom de fichier
        filename = theme_name.lower().replace(" ", "_") + ".json"
        filepath = os.path.join(themes_dir, filename)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.current_theme, f, indent=2, ensure_ascii=False)

            messagebox.showinfo(
                "Thème Sauvegardé",
                f"Le thème '{theme_name}' a été sauvegardé dans:\n{filepath}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de sauvegarder le thème:\n{str(e)}"
            )

    def export_theme(self):
        """Exporter le thème vers un fichier"""
        filepath = filedialog.asksaveasfilename(
            title="Exporter le thème",
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )

        if not filepath:
            return

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.current_theme, f, indent=2, ensure_ascii=False)

            messagebox.showinfo(
                "Thème Exporté",
                f"Le thème a été exporté vers:\n{filepath}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'exporter le thème:\n{str(e)}"
            )

    def apply_theme(self):
        """Appliquer le thème à l'application"""
        result = messagebox.askyesno(
            "Appliquer le Thème",
            "Voulez-vous appliquer ce thème à l'application?\n\n"
            "Note: L'application devra être redémarrée pour que tous les changements prennent effet."
        )

        if not result:
            return

        # Sauvegarder dans la config utilisateur
        try:
            config_path = os.path.join(os.path.expanduser("~"), ".nitrite_config.json")
            config = {}

            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)

            config["custom_theme"] = self.current_theme

            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)

            messagebox.showinfo(
                "Thème Appliqué",
                "Le thème a été appliqué.\n\n"
                "Veuillez redémarrer l'application pour voir tous les changements."
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'appliquer le thème:\n{str(e)}"
            )


def open_theme_editor(parent, app_instance=None):
    """Fonction utilitaire pour ouvrir l'éditeur de thème"""
    editor = ThemeEditorDynamic(parent, app_instance)
    editor.focus()
    return editor


if __name__ == "__main__":
    # Test standalone
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.withdraw()
    editor = ThemeEditorDynamic(root)
    root.mainloop()
