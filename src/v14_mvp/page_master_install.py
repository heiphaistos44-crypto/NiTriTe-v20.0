#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Master Install - NiTriTe V17
Pack OrdiPlus personnalisable
"""

import customtkinter as ctk
import tkinter as tk
from typing import Dict, List
import json
import os
import sys
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton
from v14_mvp.progress_dialog import MultiProgressDialog
from v14_mvp.installer_enhanced import EnhancedInstallationManager
from v14_mvp.category_icons import get_category_emoji
import threading


def resource_path(relative_path):
    """Obtenir le chemin absolu d'une ressource (compatible PyInstaller)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    return os.path.abspath(os.path.join(base_path, relative_path))


class OrdiPlusManagerDialog(ctk.CTkToplevel):
    """Dialogue de gestion des applications OrdiPlus"""

    def __init__(self, parent, current_apps: List[str], all_programs: Dict):
        super().__init__(parent)

        self.title("Gérer OrdiPlus")
        self.geometry("700x600")
        self.transient(parent)
        self.grab_set()

        self.current_apps = list(current_apps)
        self.all_programs = all_programs
        self.result = None

        self._create_ui()

        # Centrer
        self.update()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - (self.winfo_width() // 2)
        y = parent.winfo_y() + (parent.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

    def _create_ui(self):
        """Créer l'interface"""
        main = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titre
        title = ctk.CTkLabel(
            main,
            text=f"{get_category_emoji('Outils OrdiPlus')} Gérer la catégorie OrdiPlus",
            font=(DesignTokens.FONT_FAMILY, 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(0, 20))

        # Liste des apps actuelles
        self.apps_count_label = ctk.CTkLabel(
            main,
            text=f"Applications dans OrdiPlus ({len(self.current_apps)})",
            font=(DesignTokens.FONT_FAMILY, 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        self.apps_count_label.pack(anchor="w", pady=(0, 10))

        # Scrollable frame pour les apps
        self.apps_scroll = ctk.CTkScrollableFrame(
            main,
            fg_color=DesignTokens.BG_SECONDARY,
            height=300
        )
        self.apps_scroll.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Afficher les apps actuelles
        self._refresh_apps_display()

        # Bouton ajouter
        add_frame = ctk.CTkFrame(main, fg_color="transparent")
        add_frame.pack(fill=tk.X, pady=(0, 15))

        ModernButton(
            add_frame,
            text=" Ajouter une application",
            variant="outlined",
            size="md",
            command=self._show_add_dialog
        ).pack()

        # Boutons actions
        actions = ctk.CTkFrame(main, fg_color="transparent")
        actions.pack(fill=tk.X)

        ModernButton(
            actions,
            text="Annuler",
            variant="outlined",
            size="md",
            command=self._cancel
        ).pack(side=tk.LEFT)

        ModernButton(
            actions,
            text=" Sauvegarder",
            variant="filled",
            size="md",
            command=self._save
        ).pack(side=tk.RIGHT)

    def _refresh_apps_display(self):
        """Rafraîchir l'affichage de la liste d'apps"""
        # Clear
        for widget in self.apps_scroll.winfo_children():
            widget.destroy()

        # Mettre à jour le compteur
        self.apps_count_label.configure(text=f"Applications dans OrdiPlus ({len(self.current_apps)})")

        # Réafficher toutes les apps
        for app in self.current_apps:
            app_frame = ctk.CTkFrame(self.apps_scroll, fg_color=DesignTokens.BG_ELEVATED)
            app_frame.pack(fill=tk.X, pady=3, padx=5)

            app_label = ctk.CTkLabel(
                app_frame,
                text=f"   {app}",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_PRIMARY,
                anchor="w"
            )
            app_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=15, pady=10)

            ModernButton(
                app_frame,
                text="Retirer",
                variant="outlined",
                size="sm",
                command=lambda a=app: self._remove_app(a)
            ).pack(side=tk.RIGHT, padx=10, pady=5)

    def _remove_app(self, app_name: str):
        """Retirer une application"""
        if app_name in self.current_apps:
            self.current_apps.remove(app_name)
            self._refresh_apps_display()

    def _show_add_dialog(self):
        """Afficher dialogue d'ajout"""
        # Créer liste de toutes les apps disponibles
        all_apps = []
        for category, apps in self.all_programs.items():
            for app_name in apps.keys():
                if app_name not in self.current_apps and app_name not in all_apps:
                    all_apps.append(app_name)

        all_apps.sort()

        # Créer dialogue de sélection
        dialog = ctk.CTkToplevel(self)
        dialog.title("Ajouter une application")
        dialog.geometry("500x600")
        dialog.transient(self)
        dialog.grab_set()

        main = ctk.CTkFrame(dialog, fg_color=DesignTokens.BG_PRIMARY)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(
            main,
            text="Sélectionner une application",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(0, 15))

        # Barre de recherche
        search_var = tk.StringVar()
        search_entry = ctk.CTkEntry(
            main,
            placeholder_text=" Rechercher...",
            textvariable=search_var,
            height=40,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD)
        )
        search_entry.pack(fill=tk.X, pady=(0, 10))

        # Liste scrollable
        scroll = ctk.CTkScrollableFrame(main, fg_color=DesignTokens.BG_SECONDARY)
        scroll.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        def filter_apps():
            search_text = search_var.get().lower()
            for widget in scroll.winfo_children():
                widget.destroy()

            for app in all_apps:
                if search_text in app.lower():
                    ModernButton(
                        scroll,
                        text=f" {app}",
                        variant="outlined",
                        size="md",
                        command=lambda a=app: self._add_app(a, dialog)
                    ).pack(fill=tk.X, pady=3)

        search_var.trace("w", lambda *args: filter_apps())
        filter_apps()

        ModernButton(
            main,
            text="Fermer",
            variant="outlined",
            size="md",
            command=dialog.destroy
        ).pack()

    def _add_app(self, app_name: str, dialog):
        """Ajouter une application"""
        if app_name not in self.current_apps:
            self.current_apps.append(app_name)
            dialog.destroy()
            # Rafraîchir l'affichage
            self._refresh_apps_display()
            from tkinter import messagebox
            messagebox.showinfo(
                "Application ajoutée",
                f" {app_name} a été ajouté à OrdiPlus.\n\nN'oubliez pas de cliquer sur 'Sauvegarder' pour conserver vos modifications !"
            )

    def _save(self):
        """Sauvegarder et fermer"""
        self.result = self.current_apps
        self.grab_release()
        self.destroy()

    def _cancel(self):
        """Annuler"""
        self.result = None
        self.grab_release()
        self.destroy()


class MasterInstallPage(ctk.CTkFrame):
    """Page Master Install - OrdiPlus et packs personnalisés"""

    def __init__(self, parent, programs_data: Dict):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        try:
            self.programs_data = programs_data
            self.ordiplus_apps = []
            self.cleaning_tools = []
            self.custom_packs = {}  # Nouveau: dictionnaire de packs personnalisés
            self.config_path = resource_path(os.path.join("data", "ordiplus_config.json"))
            self.custom_packs_path = resource_path(os.path.join("data", "custom_packs.json"))

            self._load_ordiplus_config()
            self._load_custom_packs()
            self._create_header()
            self._create_content()
        except Exception as e:
            # Afficher l'erreur si quelque chose ne fonctionne pas
            error_frame = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
            error_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            ctk.CTkLabel(
                error_frame,
                text=" Erreur de chargement",
                font=(DesignTokens.FONT_FAMILY, 24, "bold"),
                text_color="#F44336"
            ).pack(pady=20)

            ctk.CTkLabel(
                error_frame,
                text=f"Erreur: {str(e)}",
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color=DesignTokens.TEXT_PRIMARY,
                wraplength=600
            ).pack(pady=10)

    def _load_ordiplus_config(self):
        """Charger la configuration OrdiPlus"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.ordiplus_apps = config.get('ordiplus_apps', [])
                    self.cleaning_tools = config.get('cleaning_tools', [])
            else:
                # Config par défaut
                self.ordiplus_apps = [
                    "Microsoft Office",
                    "Adobe Acrobat Reader DC",
                    "Mozilla Firefox",
                    "VLC Media Player",
                    "Malwarebytes",
                    "Spybot Search and Destroy",
                    "Wise Disk Cleaner"
                ]
                self.cleaning_tools = [
                    "Malwarebytes",
                    "Spybot Search and Destroy",
                    "Wise Disk Cleaner",
                    "RustDesk Portable"
                ]
                self._save_ordiplus_config()
        except Exception as e:
            print(f"Erreur chargement config OrdiPlus: {e}")
            self.ordiplus_apps = []
            self.cleaning_tools = []

    def _save_ordiplus_config(self):
        """Sauvegarder la configuration OrdiPlus"""
        try:
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
            config = {
                "ordiplus_apps": self.ordiplus_apps,
                "cleaning_tools": self.cleaning_tools,
                "last_modified": "2025-12-07",
                "version": "1.1"
            }
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde config OrdiPlus: {e}")

    def _load_custom_packs(self):
        """Charger les packs personnalisés"""
        try:
            if os.path.exists(self.custom_packs_path):
                with open(self.custom_packs_path, 'r', encoding='utf-8') as f:
                    self.custom_packs = json.load(f)
            else:
                self.custom_packs = {}
        except Exception as e:
            print(f"Erreur chargement packs personnalisés: {e}")
            self.custom_packs = {}

    def _save_custom_packs(self):
        """Sauvegarder les packs personnalisés"""
        try:
            os.makedirs(os.path.dirname(self.custom_packs_path), exist_ok=True)
            with open(self.custom_packs_path, 'w', encoding='utf-8') as f:
                json.dump(self.custom_packs, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur sauvegarde packs personnalisés: {e}")

    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Gauche
        left_frame = ctk.CTkFrame(container, fg_color="transparent")
        left_frame.pack(side=tk.LEFT)

        title = ctk.CTkLabel(
            left_frame,
            text=" Master Install - OrdiPlus",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            left_frame,
            text=f"Pack professionnel • {len(self.ordiplus_apps)} applications",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)

        # Droite
        right_frame = ctk.CTkFrame(container, fg_color="transparent")
        right_frame.pack(side=tk.RIGHT)

        ModernButton(
            right_frame,
            text=" Créer Pack",
            variant="outlined",
            size="md",
            command=self._create_custom_pack
        ).pack()

    def _create_content(self):
        """Contenu"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Card OrdiPlus
        card = ModernCard(scroll)
        card.pack(fill=tk.BOTH, expand=True)

        # Header coloré
        header = ctk.CTkFrame(
            card,
            fg_color="#1E88E5",
            corner_radius=DesignTokens.RADIUS_MD
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(fill=tk.X, padx=15, pady=12)

        # Gauche - Titre et description
        left_header = ctk.CTkFrame(header_content, fg_color="transparent")
        left_header.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Frame pour icône + titre
        title_frame = ctk.CTkFrame(left_header, fg_color="transparent")
        title_frame.pack(anchor="w")

        # Icône colorée
        try:
            from v14_mvp.icons_system import ColoredIconsManager
            icon_img = ColoredIconsManager.create_colored_icon("🔧", size=20)
            icon_lbl = ctk.CTkLabel(title_frame, image=icon_img, text="")
            icon_lbl.image = icon_img
            icon_lbl.pack(side=tk.LEFT, padx=(0, 10))
        except Exception as e:
            print(f"ERREUR icone coloree OrdiPlus: {e}")
            import traceback
            traceback.print_exc()

        title = ctk.CTkLabel(
            title_frame,
            text="OrdiPlus - Pack Professionnel",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        desc = ctk.CTkLabel(
            left_header,
            text="Pack complet pour maintenance professionnelle",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color="#FFFFFF"
        )
        desc.pack(anchor="w", pady=(5, 0))

        # Droite - Boutons Gérer et Installer
        btn_frame = ctk.CTkFrame(header_content, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text=f"{get_category_emoji('Outils OrdiPlus')} Gérer",
            variant="outlined",
            size="md",
            command=self._manage_ordiplus
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Installer",
            variant="filled",
            size="md",
            command=self._install_all
        ).pack(side=tk.LEFT)

        # Liste apps
        apps_frame = ctk.CTkFrame(
            card,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=8
        )
        apps_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        count_label = ctk.CTkLabel(
            apps_frame,
            text=f" {len(self.ordiplus_apps)} applications",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        count_label.pack(anchor="w", padx=15, pady=10)

        # Grille d'applications (2 colonnes)
        grid_frame = ctk.CTkFrame(apps_frame, fg_color="transparent")
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)

        for idx, app in enumerate(self.ordiplus_apps):
            row = idx // 2
            col = idx % 2

            app_label = ctk.CTkLabel(
                grid_frame,
                text=f"  • {app}",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            )
            app_label.grid(row=row, column=col, sticky="w", padx=5, pady=2)

        # Afficher les packs personnalisés
        try:
            if self.custom_packs:
                # Séparateur
                ctk.CTkLabel(
                    scroll,
                    text="",
                    height=20
                ).pack()

                # Frame pour icône + titre
                packs_title_frame = ctk.CTkFrame(scroll, fg_color="transparent")
                packs_title_frame.pack(anchor="w", pady=(10, 15))

                # Icône colorée
                try:
                    from v14_mvp.icons_system import ColoredIconsManager
                    icon_img = ColoredIconsManager.create_colored_icon("📦", size=20)
                    icon_lbl = ctk.CTkLabel(packs_title_frame, image=icon_img, text="")
                    icon_lbl.image = icon_img
                    icon_lbl.pack(side=tk.LEFT, padx=(0, 10))
                except Exception as e:
                    print(f"ERREUR icone coloree Packs Personnalisés: {e}")
                    import traceback
                    traceback.print_exc()

                ctk.CTkLabel(
                    packs_title_frame,
                    text="Packs Personnalisés",
                    font=(DesignTokens.FONT_FAMILY, 20, "bold"),
                    text_color=DesignTokens.TEXT_PRIMARY
                ).pack(side=tk.LEFT)

                # Créer une carte pour chaque pack personnalisé
                for pack_name, pack_data in self.custom_packs.items():
                    self._create_custom_pack_card(scroll, pack_name, pack_data)
        except Exception as e:
            error_label = ctk.CTkLabel(
                scroll,
                text=f"Erreur affichage packs: {str(e)}",
                font=(DesignTokens.FONT_FAMILY, 12),
                text_color="#F44336"
            )
            error_label.pack(pady=10)

    def _create_custom_pack_card(self, parent, pack_name: str, pack_data: dict):
        """Créer une carte pour un pack personnalisé"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header avec couleur personnalisée
        header = ctk.CTkFrame(
            card,
            fg_color="#7B1FA2",
            corner_radius=DesignTokens.RADIUS_MD
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(fill=tk.X, padx=15, pady=12)

        # Gauche - Titre et description
        left_header = ctk.CTkFrame(header_content, fg_color="transparent")
        left_header.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Frame pour icône + titre
        pack_title_frame = ctk.CTkFrame(left_header, fg_color="transparent")
        pack_title_frame.pack(anchor="w")

        # Icône colorée
        try:
            from v14_mvp.icons_system import ColoredIconsManager
            icon_img = ColoredIconsManager.create_colored_icon("📋", size=20)
            icon_lbl = ctk.CTkLabel(pack_title_frame, image=icon_img, text="")
            icon_lbl.image = icon_img
            icon_lbl.pack(side=tk.LEFT, padx=(0, 10))
        except Exception as e:
            print(f"ERREUR icone coloree pack {pack_name}: {e}")
            import traceback
            traceback.print_exc()

        title = ctk.CTkLabel(
            pack_title_frame,
            text=pack_name,
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        desc = ctk.CTkLabel(
            left_header,
            text=pack_data.get("description", "Pack personnalisé"),
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color="#FFFFFF"
        )
        desc.pack(anchor="w", pady=(5, 0))

        # Droite - Boutons d'action
        btn_frame = ctk.CTkFrame(header_content, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text=" Gérer",
            variant="outlined",
            size="sm",
            command=lambda: self._manage_custom_pack(pack_name)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame,
            text=" Installer",
            variant="filled",
            size="sm",
            command=lambda: self._install_custom_pack(pack_name)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame,
            text="",
            variant="text",
            size="sm",
            command=lambda: self._delete_custom_pack(pack_name)
        ).pack(side=tk.LEFT, padx=3)

        # Liste des apps
        apps_frame = ctk.CTkFrame(
            card,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=8
        )
        apps_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        apps_list = pack_data.get("apps", [])
        count_label = ctk.CTkLabel(
            apps_frame,
            text=f" {len(apps_list)} applications",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        count_label.pack(anchor="w", padx=15, pady=10)

        # Grille d'applications (2 colonnes)
        if apps_list:
            grid_frame = ctk.CTkFrame(apps_frame, fg_color="transparent")
            grid_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

            grid_frame.columnconfigure(0, weight=1)
            grid_frame.columnconfigure(1, weight=1)

            for idx, app in enumerate(apps_list):
                row = idx // 2
                col = idx % 2

                app_label = ctk.CTkLabel(
                    grid_frame,
                    text=f"  • {app}",
                    font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                    text_color=DesignTokens.TEXT_SECONDARY,
                    anchor="w"
                )
                app_label.grid(row=row, column=col, sticky="w", padx=5, pady=2)
        else:
            # Message si aucune app
            empty_label = ctk.CTkLabel(
                apps_frame,
                text=" Aucune application dans ce pack",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.WARNING
            )
            empty_label.pack(padx=15, pady=15)

    def _manage_ordiplus(self):
        """Ouvrir le dialogue de gestion OrdiPlus"""
        dialog = OrdiPlusManagerDialog(self, self.ordiplus_apps, self.programs_data)
        self.wait_window(dialog)

        if dialog.result is not None:
            self.ordiplus_apps = dialog.result
            self._save_ordiplus_config()
            # Rafraîchir l'affichage
            for widget in self.winfo_children():
                widget.destroy()
            self._create_header()
            self._create_content()

            from tkinter import messagebox
            messagebox.showinfo(
                "Configuration sauvegardée",
                f"La configuration OrdiPlus a été mise à jour.\n\n{len(self.ordiplus_apps)} applications configurées."
            )

    def _install_all(self):
        """Installer toutes les applications OrdiPlus"""
        if not self.ordiplus_apps:
            from tkinter import messagebox
            messagebox.showwarning(
                "Aucune application",
                "Le pack OrdiPlus est vide.\n\nUtilisez 'Gérer OrdiPlus' pour ajouter des applications."
            )
            return

        # Préparer liste d'installation
        apps_to_install = []
        for app_name in self.ordiplus_apps:
            # Trouver package_id dans programs_data
            package_id = app_name
            for category, apps in self.programs_data.items():
                if app_name in apps:
                    app_data = apps[app_name]
                    package_id = app_data.get('winget_id') or app_data.get('id') or app_name
                    break

            apps_to_install.append({
                'name': app_name,
                'package_id': package_id,
                'method': 'winget'
            })

        # Créer dialogue de progression
        progress_dialog = MultiProgressDialog(
            self,
            f"Installation OrdiPlus - {len(apps_to_install)} applications"
        )
        progress_dialog.set_total_apps(len(apps_to_install))

        # Installation en thread
        def install_thread():
            enhanced_installer = EnhancedInstallationManager()

            for i, app_info in enumerate(apps_to_install):
                if progress_dialog.is_cancelled:
                    break

                app_name = app_info['name']
                package_id = app_info['package_id']
                method = app_info['method']

                # Démarrer l'app dans le dialogue
                progress_dialog.start_app(app_name)

                # Event pour synchroniser
                install_done = threading.Event()
                install_result = {'success': False}

                # Callbacks
                def on_progress(percent, status):
                    progress_dialog.update_app_progress(percent, status)

                def on_log(message, level):
                    progress_dialog.add_log(message, level)

                def on_complete(success, message):
                    install_result['success'] = success
                    install_done.set()

                # Installation
                try:
                    enhanced_installer.install_app(
                        app_name=app_name,
                        package_id=package_id,
                        method=method,
                        on_progress=on_progress,
                        on_log=on_log,
                        on_complete=on_complete
                    )
                    # Attendre que l'installation se termine (max 5 minutes)
                    install_done.wait(timeout=300)

                    if install_result['success']:
                        progress_dialog.add_log(f" {app_name} installé avec succès", "success")
                    else:
                        progress_dialog.add_log(f" {app_name} n'a pas pu être installé", "error")
                except Exception as e:
                    progress_dialog.add_log(f" Erreur: {str(e)}", "error")
                    install_result['success'] = False

                # Compléter l'app
                progress_dialog.complete_app(install_result['success'])

            # Marquer comme terminé
            if not progress_dialog.is_cancelled:
                progress_dialog.mark_completed()

                # Créer dossier "Outils de Nettoyage" sur le bureau
                if self.cleaning_tools:
                    self._create_cleaning_tools_folder(progress_dialog)

        # Démarrer installation
        install_thread_obj = threading.Thread(target=install_thread, daemon=True)
        install_thread_obj.start()

    def _create_cleaning_tools_folder(self, progress_dialog):
        """Créer le dossier Outils de Nettoyage sur le bureau avec raccourcis"""
        import os
        import winshell
        from win32com.client import Dispatch

        try:
            # Chemin du dossier sur le bureau
            desktop = winshell.desktop()
            tools_folder = os.path.join(desktop, "Outils de Nettoyage")

            # Créer le dossier
            os.makedirs(tools_folder, exist_ok=True)
            progress_dialog.add_log(f" Dossier créé: {tools_folder}", "info")

            # Créer raccourcis pour chaque outil de nettoyage
            shell = Dispatch('WScript.Shell')

            # Mapping des applications vers leurs emplacements communs
            app_paths = {
                "Malwarebytes": [
                    r"C:\Program Files\Malwarebytes\Anti-Malware\mbam.exe",
                    r"C:\Program Files (x86)\Malwarebytes\Anti-Malware\mbam.exe"
                ],
                "Spybot Search and Destroy": [
                    r"C:\Program Files\Spybot - Search & Destroy 2\SDWelcome.exe",
                    r"C:\Program Files (x86)\Spybot - Search & Destroy 2\SDWelcome.exe"
                ],
                "Wise Disk Cleaner": [
                    r"C:\Program Files\Wise\Wise Disk Cleaner\WiseDiskCleaner.exe",
                    r"C:\Program Files (x86)\Wise\Wise Disk Cleaner\WiseDiskCleaner.exe"
                ]
            }

            for tool_name in self.cleaning_tools:
                # RustDesk Portable - télécharger le .exe directement
                if "RustDesk" in tool_name:
                    progress_dialog.add_log(f" Téléchargement de {tool_name}...", "info")
                    # TODO: Implémenter téléchargement RustDesk portable
                    readme_path = os.path.join(tools_folder, "RustDesk_README.txt")
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.write(
                            "RustDesk Portable\n"
                            "=================\n\n"
                            "Téléchargez RustDesk portable depuis:\n"
                            "https://github.com/rustdesk/rustdesk/releases\n\n"
                            "Placez le fichier rustdesk.exe dans ce dossier."
                        )
                    progress_dialog.add_log(f" README créé pour {tool_name}", "info")
                    continue

                # Autres outils - créer raccourci
                if tool_name in app_paths:
                    # Chercher l'exe
                    exe_path = None
                    for path in app_paths[tool_name]:
                        if os.path.exists(path):
                            exe_path = path
                            break

                    if exe_path:
                        # Créer raccourci
                        shortcut_path = os.path.join(tools_folder, f"{tool_name}.lnk")
                        shortcut = shell.CreateShortCut(shortcut_path)
                        shortcut.Targetpath = exe_path
                        shortcut.WorkingDirectory = os.path.dirname(exe_path)
                        shortcut.save()
                        progress_dialog.add_log(f" Raccourci créé: {tool_name}", "success")
                    else:
                        progress_dialog.add_log(f" {tool_name} non trouvé (installez-le d'abord)", "warning")

            progress_dialog.add_log(f" Dossier 'Outils de Nettoyage' créé sur le bureau", "success")

        except Exception as e:
            progress_dialog.add_log(f" Erreur création dossier outils: {str(e)}", "warning")

    def _manage_custom_pack(self, pack_name: str):
        """Gérer un pack personnalisé (ajouter/retirer des apps)"""
        pack_data = self.custom_packs.get(pack_name)
        if not pack_data:
            return

        dialog = OrdiPlusManagerDialog(self, pack_data.get("apps", []), self.programs_data)
        self.wait_window(dialog)

        if dialog.result is not None:
            self.custom_packs[pack_name]["apps"] = dialog.result
            self._save_custom_packs()

            # Rafraîchir l'affichage
            for widget in self.winfo_children():
                widget.destroy()
            self._create_header()
            self._create_content()

            from tkinter import messagebox
            messagebox.showinfo(
                "Pack mis à jour",
                f"Le pack '{pack_name}' a été mis à jour.\n\n{len(dialog.result)} applications configurées."
            )

    def _install_custom_pack(self, pack_name: str):
        """Installer un pack personnalisé"""
        from tkinter import messagebox

        pack_data = self.custom_packs.get(pack_name)
        if not pack_data:
            return

        apps_list = pack_data.get("apps", [])
        if not apps_list:
            messagebox.showwarning(
                "Pack vide",
                f"Le pack '{pack_name}' est vide.\n\nUtilisez 'Gérer' pour ajouter des applications."
            )
            return

        # Préparer liste d'installation
        apps_to_install = []
        for app_name in apps_list:
            # Trouver package_id dans programs_data
            package_id = app_name
            for category, apps in self.programs_data.items():
                if app_name in apps:
                    app_data = apps[app_name]
                    package_id = app_data.get('winget_id') or app_data.get('id') or app_name
                    break

            apps_to_install.append({
                'name': app_name,
                'package_id': package_id,
                'method': 'winget'
            })

        # Créer dialogue de progression
        progress_dialog = MultiProgressDialog(
            self,
            f"Installation {pack_name} - {len(apps_to_install)} applications"
        )
        progress_dialog.set_total_apps(len(apps_to_install))

        # Installation en thread
        def install_thread():
            enhanced_installer = EnhancedInstallationManager()

            for i, app_info in enumerate(apps_to_install):
                if progress_dialog.is_cancelled:
                    break

                app_name = app_info['name']
                package_id = app_info['package_id']
                method = app_info['method']

                # Démarrer l'app dans le dialogue
                progress_dialog.start_app(app_name)

                # Event pour synchroniser
                install_done = threading.Event()
                install_result = {'success': False}

                # Callbacks
                def on_progress(percent, status):
                    progress_dialog.update_app_progress(percent, status)

                def on_log(message, level):
                    progress_dialog.add_log(message, level)

                def on_complete(success, message):
                    install_result['success'] = success
                    install_done.set()

                # Installation
                try:
                    enhanced_installer.install_app(
                        app_name=app_name,
                        package_id=package_id,
                        method=method,
                        on_progress=on_progress,
                        on_log=on_log,
                        on_complete=on_complete
                    )
                    install_done.wait(timeout=300)

                    if install_result['success']:
                        progress_dialog.add_log(f" {app_name} installé avec succès", "success")
                    else:
                        progress_dialog.add_log(f" {app_name} n'a pas pu être installé", "error")
                except Exception as e:
                    progress_dialog.add_log(f" Erreur: {str(e)}", "error")
                    install_result['success'] = False

                # Compléter l'app
                progress_dialog.complete_app(install_result['success'])

            # Marquer comme terminé
            if not progress_dialog.is_cancelled:
                progress_dialog.mark_completed()

        # Démarrer installation
        install_thread_obj = threading.Thread(target=install_thread, daemon=True)
        install_thread_obj.start()

    def _delete_custom_pack(self, pack_name: str):
        """Supprimer un pack personnalisé"""
        from tkinter import messagebox

        response = messagebox.askyesno(
            "Supprimer le pack",
            f"Êtes-vous sûr de vouloir supprimer le pack '{pack_name}' ?\n\nCette action est irréversible.",
            icon='warning'
        )

        if response:
            if pack_name in self.custom_packs:
                del self.custom_packs[pack_name]
                self._save_custom_packs()

                # Rafraîchir l'affichage
                for widget in self.winfo_children():
                    widget.destroy()
                self._create_header()
                self._create_content()

                messagebox.showinfo(
                    "Pack supprimé",
                    f"Le pack '{pack_name}' a été supprimé avec succès."
                )

    def _create_custom_pack(self):
        """Créer un nouveau pack personnalisé"""
        from tkinter import messagebox

        # Dialogue de création
        create_dialog = ctk.CTkToplevel(self)
        create_dialog.title("Créer un Pack Personnalisé")
        create_dialog.geometry("600x700")
        create_dialog.transient(self)
        create_dialog.grab_set()

        # Centrer
        create_dialog.update_idletasks()
        x = (create_dialog.winfo_screenwidth() // 2) - (600 // 2)
        y = (create_dialog.winfo_screenheight() // 2) - (700 // 2)
        create_dialog.geometry(f"600x700+{x}+{y}")

        main = ctk.CTkFrame(create_dialog, fg_color=DesignTokens.BG_PRIMARY)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titre
        title = ctk.CTkLabel(
            main,
            text=" Créer un Pack Personnalisé",
            font=(DesignTokens.FONT_FAMILY, 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(0, 20))

        # Nom du pack
        ctk.CTkLabel(
            main,
            text="Nom du pack:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        pack_name_entry = ctk.CTkEntry(
            main,
            placeholder_text="Ex: Pack Gaming, Pack Bureautique...",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            fg_color=DesignTokens.BG_ELEVATED,
            height=40
        )
        pack_name_entry.pack(fill=tk.X, pady=(0, 10))

        # Description
        ctk.CTkLabel(
            main,
            text="Description (optionnel):",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        pack_desc_entry = ctk.CTkEntry(
            main,
            placeholder_text="Description courte du pack...",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            fg_color=DesignTokens.BG_ELEVATED,
            height=40
        )
        pack_desc_entry.pack(fill=tk.X, pady=(0, 15))

        # Applications sélectionnées
        selected_apps = []

        ctk.CTkLabel(
            main,
            text="Applications sélectionnées:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(10, 5))

        selected_frame = ctk.CTkScrollableFrame(
            main,
            fg_color=DesignTokens.BG_ELEVATED,
            height=150
        )
        selected_frame.pack(fill=tk.X, pady=(0, 15))

        selected_label = ctk.CTkLabel(
            selected_frame,
            text="Aucune application sélectionnée",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY
        )
        selected_label.pack(pady=20)

        def update_selected_display():
            for widget in selected_frame.winfo_children():
                widget.destroy()

            if selected_apps:
                for app in selected_apps:
                    app_frame = ctk.CTkFrame(selected_frame, fg_color=DesignTokens.BG_SECONDARY)
                    app_frame.pack(fill=tk.X, pady=2, padx=5)

                    ctk.CTkLabel(
                        app_frame,
                        text=f"   {app}",
                        font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                        text_color=DesignTokens.TEXT_PRIMARY,
                        anchor="w"
                    ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5)

                    ModernButton(
                        app_frame,
                        text="",
                        variant="text",
                        size="sm",
                        command=lambda a=app: remove_app(a)
                    ).pack(side=tk.RIGHT, padx=5)
            else:
                ctk.CTkLabel(
                    selected_frame,
                    text="Aucune application sélectionnée",
                    font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                    text_color=DesignTokens.TEXT_TERTIARY
                ).pack(pady=20)

        def remove_app(app_name):
            if app_name in selected_apps:
                selected_apps.remove(app_name)
                update_selected_display()

        # Bouton pour ajouter des apps
        ModernButton(
            main,
            text=" Ajouter des applications",
            variant="outlined",
            size="md",
            command=lambda: show_app_selector()
        ).pack(pady=(0, 15))

        def show_app_selector():
            # Créer liste de toutes les apps disponibles
            all_apps = []
            for category, apps in self.programs_data.items():
                for app_name in apps.keys():
                    if app_name not in selected_apps and app_name not in all_apps:
                        all_apps.append(app_name)
            all_apps.sort()

            # Dialogue de sélection
            selector = ctk.CTkToplevel(create_dialog)
            selector.title("Sélectionner des applications")
            selector.geometry("500x600")
            selector.transient(create_dialog)
            selector.grab_set()

            selector_main = ctk.CTkFrame(selector, fg_color=DesignTokens.BG_PRIMARY)
            selector_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            ctk.CTkLabel(
                selector_main,
                text="Sélectionner une application",
                font=(DesignTokens.FONT_FAMILY, 16, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY
            ).pack(pady=(0, 15))

            # Barre de recherche
            search_var = tk.StringVar()
            search_entry = ctk.CTkEntry(
                selector_main,
                placeholder_text=" Rechercher...",
                textvariable=search_var,
                height=40,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD)
            )
            search_entry.pack(fill=tk.X, pady=(0, 10))

            # Liste scrollable
            scroll = ctk.CTkScrollableFrame(selector_main, fg_color=DesignTokens.BG_SECONDARY)
            scroll.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

            def filter_apps_selector():
                search_text = search_var.get().lower()
                for widget in scroll.winfo_children():
                    widget.destroy()

                for app in all_apps:
                    if search_text in app.lower():
                        ModernButton(
                            scroll,
                            text=f" {app}",
                            variant="outlined",
                            size="md",
                            command=lambda a=app: add_app_to_pack(a, selector)
                        ).pack(fill=tk.X, pady=3)

            def add_app_to_pack(app_name, dialog):
                if app_name not in selected_apps:
                    selected_apps.append(app_name)
                    update_selected_display()
                dialog.destroy()

            search_var.trace("w", lambda *args: filter_apps_selector())
            filter_apps_selector()

            ModernButton(
                selector_main,
                text="Fermer",
                variant="outlined",
                size="md",
                command=selector.destroy
            ).pack()

        # Boutons de validation
        btn_frame = ctk.CTkFrame(main, fg_color="transparent")
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        def save_pack():
            pack_name = pack_name_entry.get().strip()
            pack_desc = pack_desc_entry.get().strip()

            if not pack_name:
                messagebox.showerror("Erreur", "Veuillez entrer un nom pour le pack.")
                return

            if not selected_apps:
                messagebox.showerror("Erreur", "Veuillez sélectionner au moins une application.")
                return

            if pack_name in self.custom_packs:
                response = messagebox.askyesno(
                    "Pack existant",
                    f"Un pack nommé '{pack_name}' existe déjà.\n\nVoulez-vous le remplacer ?"
                )
                if not response:
                    return

            # Sauvegarder le pack
            self.custom_packs[pack_name] = {
                "apps": selected_apps.copy(),  # Copier la liste pour éviter les références
                "description": pack_desc or f"Pack personnalisé avec {len(selected_apps)} applications"
            }
            self._save_custom_packs()

            messagebox.showinfo(
                "Pack créé",
                f" Le pack '{pack_name}' a été créé avec succès!\n\n{len(selected_apps)} applications configurées."
            )

            create_dialog.destroy()

            # Rafraîchir l'affichage
            print("[DEBUG] Refreshing display...")
            for widget in self.winfo_children():
                widget.destroy()
            self._create_header()
            self._create_content()
            print("[DEBUG] Display refreshed.")

        ModernButton(
            btn_frame,
            text=" Créer le Pack",
            variant="filled",
            size="md",
            command=save_pack
        ).pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text="Annuler",
            variant="outlined",
            size="md",
            command=create_dialog.destroy
        ).pack(side=tk.RIGHT, padx=(0, 10))
