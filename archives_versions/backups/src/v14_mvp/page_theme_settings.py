#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page de Personnalisation des Thèmes - NiTriTe V17
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import colorchooser, messagebox, filedialog
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton
from v14_mvp.theme_manager import get_theme_manager


class ThemeSettingsPage(ctk.CTkFrame):
    """Page de configuration des thèmes personnalisables"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Gestion d'erreur pour éviter l'écran noir
        try:
            self.theme_manager = get_theme_manager()
            self._create_ui()
        except Exception as e:
            # Afficher l'erreur au lieu d'un écran noir
            import traceback
            error_frame = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
            error_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            ctk.CTkLabel(
                error_frame,
                text="❌ Erreur de chargement de la page Thèmes",
                font=(DesignTokens.FONT_FAMILY, 24, "bold"),
                text_color=DesignTokens.COLOR_ERROR
            ).pack(pady=20)

            error_text = f"Type: {type(e).__name__}\nMessage: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"

            error_display = ctk.CTkTextbox(
                error_frame,
                font=(DesignTokens.FONT_FAMILY, 12),
                fg_color=DesignTokens.BG_ELEVATED,
                wrap="word"
            )
            error_display.pack(fill=tk.BOTH, expand=True, pady=10)
            error_display.insert("1.0", error_text)
            error_display.configure(state="disabled")

    def _create_ui(self):
        """Créer l'interface"""
        # Titre
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill=tk.X, padx=20, pady=20)

        ctk.CTkLabel(
            title_frame,
            text="🎨 Personnalisation des Thèmes",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_frame,
            text="Personnalisez complètement l'apparence de l'application",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(anchor="w", pady=(5, 0))

        # Scrollable frame pour le contenu
        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Section: Thèmes prédéfinis
        self._create_preset_themes_section(scroll)

        # Section: Couleurs personnalisées
        self._create_colors_section(scroll)

        # Section: Polices
        self._create_fonts_section(scroll)

        # Section: Import/Export
        self._create_import_export_section(scroll)

    def _create_preset_themes_section(self, parent):
        """Section des thèmes prédéfinis"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="📚 Thèmes Prédéfinis",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", padx=15, pady=10)

        # Grille de thèmes
        themes_frame = ctk.CTkFrame(card, fg_color="transparent")
        themes_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        available_themes = self.theme_manager.get_available_themes()

        for idx, (theme_id, theme_name) in enumerate(available_themes.items()):
            row = idx // 2
            col = idx % 2

            theme_btn = ctk.CTkButton(
                themes_frame,
                text=theme_name,
                command=lambda tid=theme_id: self._apply_preset_theme(tid),
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                fg_color=DesignTokens.COLOR_PRIMARY,
                hover_color=DesignTokens.COLOR_PRIMARY_HOVER,
                corner_radius=8,
                height=40
            )
            theme_btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

        themes_frame.grid_columnconfigure(0, weight=1)
        themes_frame.grid_columnconfigure(1, weight=1)

    def _create_colors_section(self, parent):
        """Section de personnalisation des couleurs"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="🎨 Couleurs Personnalisées",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", padx=15, pady=10)

        colors_grid = ctk.CTkFrame(card, fg_color="transparent")
        colors_grid.pack(fill=tk.X, padx=15, pady=(0, 15))

        color_keys = [
            ("primary", "Couleur Primaire"),
            ("secondary", "Couleur Secondaire"),
            ("bg_primary", "Fond Principal"),
            ("bg_secondary", "Fond Secondaire"),
            ("text_primary", "Texte Principal"),
            ("text_secondary", "Texte Secondaire")
        ]

        for idx, (key, label) in enumerate(color_keys):
            row = idx // 2
            col = idx % 2

            color_frame = ctk.CTkFrame(colors_grid, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
            color_frame.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

            ctk.CTkLabel(
                color_frame,
                text=label,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM)
            ).pack(side=tk.LEFT, padx=10, pady=10)

            current_color = self.theme_manager.get_color(key)
            color_preview = ctk.CTkFrame(
                color_frame,
                fg_color=current_color,
                width=40,
                height=30,
                corner_radius=4
            )
            color_preview.pack(side=tk.LEFT, padx=5)

            ctk.CTkButton(
                color_frame,
                text="Changer",
                command=lambda k=key: self._change_color(k),
                width=80,
                height=30
            ).pack(side=tk.LEFT, padx=10, pady=5)

        colors_grid.grid_columnconfigure(0, weight=1)
        colors_grid.grid_columnconfigure(1, weight=1)

    def _create_fonts_section(self, parent):
        """Section de personnalisation des polices"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="🔤 Tailles de Police",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", padx=15, pady=10)

        fonts_frame = ctk.CTkFrame(card, fg_color="transparent")
        fonts_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        font_sizes = [
            ("size_xs", "Très Petit", 8, 14),
            ("size_sm", "Petit", 10, 16),
            ("size_md", "Moyen", 12, 18),
            ("size_lg", "Grand", 14, 22),
            ("size_xl", "Très Grand", 16, 28),
            ("size_xxl", "Extra Grand", 18, 32)
        ]

        for key, label, min_val, max_val in font_sizes:
            size_frame = ctk.CTkFrame(fonts_frame, fg_color="transparent")
            size_frame.pack(fill=tk.X, pady=5)

            ctk.CTkLabel(
                size_frame,
                text=label,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                width=120,
                anchor="w"
            ).pack(side=tk.LEFT, padx=5)

            current_size = self.theme_manager.get_font_size(key)
            slider = ctk.CTkSlider(
                size_frame,
                from_=min_val,
                to=max_val,
                number_of_steps=max_val - min_val,
                command=lambda v, k=key: self._update_font_size(k, int(v))
            )
            slider.set(current_size)
            slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

            size_label = ctk.CTkLabel(
                size_frame,
                text=f"{current_size}px",
                width=50
            )
            size_label.pack(side=tk.LEFT, padx=5)

    def _create_import_export_section(self, parent):
        """Section Import/Export"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="💾 Import/Export",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", padx=15, pady=10)

        buttons_frame = ctk.CTkFrame(card, fg_color="transparent")
        buttons_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        ModernButton(
            buttons_frame,
            text="📤 Exporter le thème",
            variant="outlined",
            command=self._export_theme
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            buttons_frame,
            text="📥 Importer un thème",
            variant="outlined",
            command=self._import_theme
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            buttons_frame,
            text="🔄 Réinitialiser",
            variant="outlined",
            command=self._reset_theme
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _apply_preset_theme(self, theme_id):
        """Appliquer un thème prédéfini"""
        self.theme_manager.apply_theme(theme_name=theme_id)
        messagebox.showinfo(
            "Thème appliqué",
            "Le thème a été appliqué avec succès!\n\n"
            "Redémarrez l'application pour voir tous les changements."
        )

    def _change_color(self, color_key):
        """Changer une couleur"""
        current_color = self.theme_manager.get_color(color_key)
        color = colorchooser.askcolor(
            color=current_color,
            title=f"Choisir la couleur - {color_key}"
        )

        if color[1]:  # color[1] est le code hex
            theme = self.theme_manager.current_theme
            theme["colors"][color_key] = color[1]
            self.theme_manager.save_theme(theme)
            self._refresh_ui()

    def _update_font_size(self, size_key, value):
        """Mettre à jour une taille de police"""
        theme = self.theme_manager.current_theme
        theme["fonts"][size_key] = value
        self.theme_manager.save_theme(theme)

    def _export_theme(self):
        """Exporter le thème actuel"""
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Fichier JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Exporter le thème"
        )

        if filepath:
            if self.theme_manager.export_theme(filepath):
                messagebox.showinfo("Succès", "Thème exporté avec succès!")
            else:
                messagebox.showerror("Erreur", "Impossible d'exporter le thème")

    def _import_theme(self):
        """Importer un thème"""
        filepath = filedialog.askopenfilename(
            filetypes=[("Fichier JSON", "*.json"), ("Tous les fichiers", "*.*")],
            title="Importer un thème"
        )

        if filepath:
            if self.theme_manager.import_theme(filepath):
                messagebox.showinfo(
                    "Succès",
                    "Thème importé avec succès!\n\n"
                    "Redémarrez l'application pour voir tous les changements."
                )
                self._refresh_ui()
            else:
                messagebox.showerror("Erreur", "Impossible d'importer le thème")

    def _reset_theme(self):
        """Réinitialiser au thème par défaut"""
        response = messagebox.askyesno(
            "Confirmation",
            "Voulez-vous vraiment réinitialiser le thème?"
        )

        if response:
            self.theme_manager.apply_theme(theme_name="dark_professional")
            messagebox.showinfo(
                "Réinitialisation",
                "Thème réinitialisé!\n\nRedémarrez l'application pour voir les changements."
            )
            self._refresh_ui()

    def _refresh_ui(self):
        """Rafraîchir l'interface"""
        # Détruire et recréer l'UI
        for widget in self.winfo_children():
            widget.destroy()
        self._create_ui()
