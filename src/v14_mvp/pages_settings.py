#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Paramètres Complète - NiTriTe V14
10 sections de configuration
"""

import customtkinter as ctk
import tkinter as tk
from typing import Callable
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton


class SettingsPage(ctk.CTkFrame):
    """Page Paramètres complète avec 10 sections"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        try:
            self._create_header()
            self._create_settings()
        except Exception as e:
            import traceback
            error_frame = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
            error_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            ctk.CTkLabel(
                error_frame,
                text=" Erreur de chargement de la page Paramètres",
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
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text=" Paramètres",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        subtitle = ctk.CTkLabel(
            container,
            text="Configuration complète de l'application",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)
    
    def _create_settings(self):
        """Créer sections de paramètres"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # 1. Apparence
        self._create_appearance_section(scroll)
        
        # 2. Langue
        self._create_language_section(scroll)
        
        # 3. Mises à jour
        self._create_updates_section(scroll)
        
        # 4. Performances
        self._create_performance_section(scroll)
        
        # 5. Installation
        self._create_installation_section(scroll)
        
        # 6. Sauvegarde
        self._create_backup_section(scroll)
        
        # 7. Notifications
        self._create_notifications_section(scroll)
        
        # 8. Avancé
        self._create_advanced_section(scroll)
        
        # 9. À propos
        self._create_about_section(scroll)
        
        # 10. Actions
        self._create_actions_section(scroll)
    
    def _create_appearance_section(self, parent):
        """Section Apparence"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        # Titre
        self._create_section_title(card, " Apparence", "Personnalisation de l'interface")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        # Thème
        self._create_option(
            content,
            "Thème",
            "Sélectionner le jeu de couleurs",
            self._create_theme_selector
        )
        
        # Mode
        self._create_option(
            content,
            "Mode d'affichage",
            "Clair ou sombre",
            self._create_mode_selector
        )
        
        # Taille police
        self._create_option(
            content,
            "Taille de police",
            "Ajuster la lisibilité",
            self._create_font_slider
        )

        # Éditeur de thème
        self._create_option(
            content,
            "Éditeur de Thème",
            "Personnaliser l'apparence en temps réel",
            self._create_theme_editor_button
        )

    def _create_language_section(self, parent):
        """Section Langue"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Langue", "Sélection de la langue")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Langue de l'interface",
            "Français ou Anglais",
            self._create_language_selector
        )
    
    def _create_updates_section(self, parent):
        """Section Mises à jour"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Mises à jour", "Gestion des mises à jour")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Vérification automatique",
            "Chercher les mises à jour au démarrage",
            self._create_auto_update_toggle
        )
        
        self._create_option(
            content,
            "Canal de mise à jour",
            "Stable ou Beta",
            self._create_update_channel_selector
        )
    
    def _create_performance_section(self, parent):
        """Section Performances"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Performances", "Optimisation de l'application")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Limite d'apps par catégorie",
            "Nombre maximum d'applications affichées",
            self._create_app_limit_slider
        )
        
        self._create_option(
            content,
            "Animation",
            "Activer les animations d'interface",
            self._create_animation_toggle
        )
    
    def _create_installation_section(self, parent):
        """Section Installation"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Installation", "Options d'installation")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Gestionnaire par défaut",
            "WinGet, Chocolatey ou Téléchargement",
            self._create_package_manager_selector
        )
        
        self._create_option(
            content,
            "Dossier de téléchargement",
            "Emplacement des fichiers téléchargés",
            self._create_download_folder_selector
        )
    
    def _create_backup_section(self, parent):
        """Section Sauvegarde"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Sauvegarde", "Sauvegarde automatique")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Sauvegarde automatique",
            "Sauvegarder la configuration régulièrement",
            self._create_auto_backup_toggle
        )
    
    def _create_notifications_section(self, parent):
        """Section Notifications"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Notifications", "Alertes et notifications")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Notifications système",
            "Afficher les notifications Windows",
            self._create_notifications_toggle
        )
        
        self._create_option(
            content,
            "Sons",
            "Activer les sons de notification",
            self._create_sounds_toggle
        )
    
    def _create_advanced_section(self, parent):
        """Section Avancé"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Avancé", "Options avancées")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._create_option(
            content,
            "Mode Debug",
            "Activer les logs détaillés",
            self._create_debug_toggle
        )
        
        self._create_option(
            content,
            "Portable",
            "Mode portable (données dans le dossier app)",
            self._create_portable_toggle
        )
    
    def _create_about_section(self, parent):
        """Section À propos"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, "ℹ À propos", "Informations sur l'application")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        info_text = """
        NiTriTe V20.0
        Maintenance Informatique Professionnelle

        ✨ 200+ applications disponibles via WinGet
        🔧 25+ outils diagnostiques portables
        🤖 500+ scénarios IA de maintenance
        🎨 Système de thèmes personnalisables
        💾 Mode 100% portable (aucune trace système)
        ⌨️ 6 terminaux intégrés (CMD, PowerShell, Git Bash, WSL, Azure)

        🌐 Site Web: https://heiphaistos44-crypto.github.io/Site-Web-NiTriTe/

        © 2024 OrdiPlus - Tous droits réservés
        """
        
        info = ctk.CTkLabel(
            content,
            text=info_text,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            justify="left"
        )
        info.pack(pady=10)

        # Bouton Site Web
        website_btn = ModernButton(
            content,
            text="🌐 Visiter le Site Web NiTriTe",
            variant="filled",
            command=self._open_website
        )
        website_btn.pack(pady=10)
    
    def _create_actions_section(self, parent):
        """Section Actions"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        self._create_section_title(card, " Actions", "Actions rapides")
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        actions_frame = ctk.CTkFrame(content, fg_color="transparent")
        actions_frame.pack(fill=tk.X, pady=10)
        
        ModernButton(
            actions_frame,
            text=" Sauvegarder Configuration",
            variant="filled",
            command=self._save_config
        ).pack(side=tk.LEFT, padx=5)
        
        ModernButton(
            actions_frame,
            text=" Réinitialiser",
            variant="outlined",
            command=self._reset_config
        ).pack(side=tk.LEFT, padx=5)
        
        ModernButton(
            actions_frame,
            text=" Ouvrir Dossier Config",
            variant="text",
            command=self._open_config_folder
        ).pack(side=tk.LEFT, padx=5)
    
    # Helpers
    def _create_section_title(self, parent, title, subtitle):
        """Créer titre de section"""
        header = ctk.CTkFrame(parent, fg_color="transparent")
        header.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        title_label = ctk.CTkLabel(
            header,
            text=title,
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title_label.pack(anchor="w")
        
        subtitle_label = ctk.CTkLabel(
            header,
            text=subtitle,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        subtitle_label.pack(anchor="w")
    
    def _create_option(self, parent, label, description, widget_creator):
        """Créer une option de paramètre"""
        frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=DesignTokens.RADIUS_MD
        )
        frame.pack(fill=tk.X, pady=5)
        
        content = ctk.CTkFrame(frame, fg_color="transparent")
        content.pack(fill=tk.X, padx=15, pady=12)
        
        # Label et description à gauche
        left = ctk.CTkFrame(content, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        label_widget = ctk.CTkLabel(
            left,
            text=label,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        label_widget.pack(anchor="w")
        
        desc_widget = ctk.CTkLabel(
            left,
            text=description,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        desc_widget.pack(anchor="w")
        
        # Widget de contrôle à droite
        right = ctk.CTkFrame(content, fg_color="transparent")
        right.pack(side=tk.RIGHT)
        
        widget_creator(right)
    
    # Widget creators
    def _create_theme_selector(self, parent):
        from .design_system import ThemePalettes

        themes = ["Orange NiTriTe", "Bleu Pro", "Vert Tech", "Violet Creative", "Rouge Energy"]
        selector = ctk.CTkOptionMenu(
            parent,
            values=themes,
            command=self._on_theme_change,
            fg_color=DesignTokens.ACCENT_PRIMARY,
            button_color=DesignTokens.ACCENT_PRIMARY,
            button_hover_color=DesignTokens.BG_HOVER
        )
        # Charger le thème actuel depuis la config
        current_theme = ThemePalettes.get_current_theme()
        selector.set(current_theme)
        selector.pack()
    
    def _create_mode_selector(self, parent):
        modes = ["Sombre", "Clair", "Auto"]
        selector = ctk.CTkOptionMenu(
            parent,
            values=modes,
            command=self._on_mode_change,
            fg_color=DesignTokens.ACCENT_PRIMARY
        )
        selector.set("Sombre")
        selector.pack()
    
    def _create_font_slider(self, parent):
        slider = ctk.CTkSlider(
            parent,
            from_=12,
            to=20,
            number_of_steps=8,
            command=self._on_font_size_change,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.ACCENT_PRIMARY,
            button_color=DesignTokens.ACCENT_PRIMARY,
            button_hover_color=DesignTokens.BG_HOVER
        )
        slider.set(14)
        slider.pack()

    def _create_theme_editor_button(self, parent):
        """Bouton pour ouvrir l'éditeur de thème"""
        btn = ctk.CTkButton(
            parent,
            text="Ouvrir l'Éditeur",
            command=self._open_theme_editor,
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER,
            width=150,
            height=32
        )
        btn.pack()

    def _create_language_selector(self, parent):
        languages = [" Français", " English"]
        selector = ctk.CTkOptionMenu(
            parent,
            values=languages,
            command=self._on_language_change,
            fg_color=DesignTokens.ACCENT_PRIMARY
        )
        selector.set(" Français")
        selector.pack()
    
    def _create_auto_update_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_auto_update_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.SUCCESS,
            button_color=DesignTokens.TEXT_PRIMARY,
            button_hover_color=DesignTokens.TEXT_SECONDARY
        )
        switch.select()
        switch.pack()
    
    def _create_update_channel_selector(self, parent):
        channels = ["Stable", "Beta"]
        selector = ctk.CTkOptionMenu(
            parent,
            values=channels,
            command=self._on_channel_change,
            fg_color=DesignTokens.ACCENT_PRIMARY
        )
        selector.set("Stable")
        selector.pack()
    
    def _create_app_limit_slider(self, parent):
        slider = ctk.CTkSlider(
            parent,
            from_=10,
            to=50,
            number_of_steps=8,
            command=self._on_app_limit_change,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.ACCENT_PRIMARY
        )
        slider.set(20)
        slider.pack()
    
    def _create_animation_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_animation_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.SUCCESS
        )
        switch.select()
        switch.pack()
    
    def _create_package_manager_selector(self, parent):
        managers = ["WinGet", "Chocolatey", "Téléchargement Direct"]
        selector = ctk.CTkOptionMenu(
            parent,
            values=managers,
            command=self._on_package_manager_change,
            fg_color=DesignTokens.ACCENT_PRIMARY
        )
        selector.set("WinGet")
        selector.pack()
    
    def _create_download_folder_selector(self, parent):
        btn = ModernButton(
            parent,
            text=" Parcourir...",
            variant="outlined",
            size="sm",
            command=self._browse_download_folder
        )
        btn.pack()
    
    def _create_auto_backup_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_auto_backup_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.SUCCESS
        )
        switch.select()
        switch.pack()
    
    def _create_notifications_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_notifications_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.SUCCESS
        )
        switch.select()
        switch.pack()
    
    def _create_sounds_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_sounds_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.SUCCESS
        )
        switch.pack()
    
    def _create_debug_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_debug_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.WARNING
        )
        switch.pack()
    
    def _create_portable_toggle(self, parent):
        switch = ctk.CTkSwitch(
            parent,
            text="",
            command=self._on_portable_toggle,
            fg_color=DesignTokens.BG_HOVER,
            progress_color=DesignTokens.INFO
        )
        switch.pack()
    
    # Callbacks
    def _on_theme_change(self, value):
        """Changer le thème de couleur de l'application"""
        from tkinter import messagebox
        from .design_system import ThemePalettes

        print(f" Thème changé: {value}")

        # Sauvegarder le thème
        if ThemePalettes.save_theme(value):
            # Informer l'utilisateur
            messagebox.showinfo(
                "Thème changé",
                f" Thème '{value}' sauvegardé!\n\n"
                f" Veuillez redémarrer l'application pour appliquer le nouveau thème.\n\n"
                f"Le thème sera appliqué au prochain lancement."
            )
        else:
            messagebox.showerror(
                "Erreur",
                "Impossible de sauvegarder le thème.\n\n"
                "Vérifiez les permissions d'écriture."
            )
    
    def _on_mode_change(self, value):
        """Changer le mode d'affichage (clair/sombre)"""
        from tkinter import messagebox
        import os
        import json

        print(f" Mode changé: {value}")

        # Mapper les valeurs
        mode_map = {
            "Sombre": "dark",
            "Clair": "light",
            "Auto": "system"
        }

        if value in mode_map:
            ctk_mode = mode_map[value]
            try:
                # Sauvegarder la préférence
                config_path = os.path.join(os.path.expanduser("~"), ".nitrite_config.json")
                config = {}
                if os.path.exists(config_path):
                    with open(config_path, 'r', encoding='utf-8') as f:
                        config = json.load(f)

                config["appearance_mode"] = ctk_mode

                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=2)

                # Essayer de changer immédiatement (peut ne pas tout mettre à jour)
                ctk.set_appearance_mode(ctk_mode)
                print(f" Mode sauvegardé et appliqué: {ctk_mode}")

                # Informer l'utilisateur
                messagebox.showinfo(
                    "Mode d'affichage",
                    f" Mode '{value}' sauvegardé!\n\n"
                    f" Veuillez redémarrer l'application pour que\n"
                    f"le changement soit complètement appliqué.\n\n"
                    f"Le mode sera chargé automatiquement au prochain lancement."
                )
            except Exception as e:
                print(f" Erreur changement mode: {e}")
                messagebox.showerror(
                    "Erreur",
                    f"Impossible de sauvegarder le mode:\n\n{str(e)}"
                )
    
    def _on_font_size_change(self, value):
        """Changer la taille de la police"""
        from tkinter import messagebox
        print(f" Taille police: {int(value)}px")
        messagebox.showinfo(
            "Taille de police",
            f"Taille sélectionnée: {int(value)}px\n\n"
            f" Cette fonctionnalité sera disponible dans une prochaine version.\n"
            f"Elle nécessite une refonte de l'interface pour s'adapter dynamiquement."
        )

    def _open_theme_editor(self):
        """Ouvrir l'éditeur de thème dynamique"""
        try:
            from v14_mvp.theme_editor_dynamic import open_theme_editor
            print(" Ouverture de l'éditeur de thème...")
            open_theme_editor(self.winfo_toplevel(), app_instance=None)
        except Exception as e:
            from tkinter import messagebox
            import traceback
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir l'éditeur de thème:\n\n{str(e)}\n\n{traceback.format_exc()}"
            )
            print(f" Erreur ouverture éditeur: {e}")

    def _on_language_change(self, value):
        """Changer la langue de l'interface"""
        from tkinter import messagebox
        print(f" Langue: {value}")
        messagebox.showinfo(
            "Changement de langue",
            f"Langue sélectionnée: {value}\n\n"
            f" Cette fonctionnalité sera disponible dans une prochaine version.\n"
            f"L'internationalisation nécessite la traduction de tous les textes."
        )
    
    def _on_auto_update_toggle(self):
        print(" Auto-update toggled")
    
    def _on_channel_change(self, value):
        print(f" Canal: {value}")
    
    def _on_app_limit_change(self, value):
        print(f" Limite apps: {int(value)}")
    
    def _on_animation_toggle(self):
        print(" Animations toggled")
    
    def _on_package_manager_change(self, value):
        print(f" Gestionnaire: {value}")
    
    def _browse_download_folder(self):
        print(" Parcourir dossier téléchargement")
    
    def _on_auto_backup_toggle(self):
        print(" Auto-backup toggled")
    
    def _on_notifications_toggle(self):
        print(" Notifications toggled")
    
    def _on_sounds_toggle(self):
        print(" Sons toggled")
    
    def _on_debug_toggle(self):
        print(" Debug mode toggled")
    
    def _on_portable_toggle(self):
        print(" Mode portable toggled")
    
    def _save_config(self):
        """Sauvegarder la configuration"""
        from tkinter import messagebox
        print(" Sauvegarde configuration...")
        messagebox.showinfo(
            "Sauvegarder Configuration",
            " Configuration sauvegardée!\n\n"
            "Les paramètres modifiés (thème, mode) sont\n"
            "automatiquement sauvegardés lors du changement.\n\n"
            " Fichier: ~/.nitrite_config.json"
        )

    def _reset_config(self):
        """Réinitialiser la configuration"""
        from tkinter import messagebox
        import os
        import json

        print(" Réinitialisation configuration...")

        response = messagebox.askyesno(
            "Réinitialiser Configuration",
            " Êtes-vous sûr de vouloir réinitialiser la configuration?\n\n"
            "Cela supprimera tous vos paramètres personnalisés\n"
            "(thème, mode d'apparence, etc.)\n\n"
            "L'application devra être redémarrée."
        )

        if response:
            try:
                config_path = os.path.join(os.path.expanduser("~"), ".nitrite_config.json")
                if os.path.exists(config_path):
                    os.remove(config_path)
                    messagebox.showinfo(
                        "Configuration réinitialisée",
                        " Configuration réinitialisée avec succès!\n\n"
                        "Veuillez redémarrer l'application pour\n"
                        "appliquer les paramètres par défaut."
                    )
                else:
                    messagebox.showinfo(
                        "Aucune configuration",
                        "Aucun fichier de configuration à réinitialiser.\n"
                        "Vous utilisez déjà les paramètres par défaut."
                    )
            except Exception as e:
                messagebox.showerror(
                    "Erreur",
                    f"Impossible de réinitialiser la configuration:\n\n{str(e)}"
                )

    def _open_config_folder(self):
        """Ouvrir le dossier de configuration"""
        import os
        import subprocess
        from tkinter import messagebox

        print(" Ouverture dossier config...")

        try:
            home_dir = os.path.expanduser("~")
            # Ouvrir l'explorateur dans le dossier home où se trouve .nitrite_config.json
            subprocess.Popen(f'explorer "{home_dir}"')
            messagebox.showinfo(
                "Dossier de configuration",
                f" Emplacement:\n{home_dir}\n\n"
                f"Recherchez le fichier:\n.nitrite_config.json"
            )
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir le dossier:\n\n{str(e)}"
            )

    def _open_website(self):
        """Ouvrir le site web NiTriTe"""
        import webbrowser
        print(" Ouverture du site web NiTriTe...")
        webbrowser.open("https://heiphaistos44-crypto.github.io/Site-Web-NiTriTe/")