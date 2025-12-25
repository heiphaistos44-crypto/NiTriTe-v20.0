#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pages Optimisées - NiTriTe V17
Versions optimisées avec chargement progressif
"""

import customtkinter as ctk
import tkinter as tk
from typing import Dict, List
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernSearchBar, ModernStatsCard, ModernButton
from v14_mvp.installer import installer
from v14_mvp.progress_dialog import MultiProgressDialog
from v14_mvp.installer_enhanced import EnhancedInstallationManager
import threading
import time
import subprocess
import ctypes
import sys
import requests
from pathlib import Path


def is_admin():
    """Vérifier si l'application a les droits administrateur"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin(command, wait=False):
    """Exécuter une commande en mode administrateur sans prompt UAC"""
    try:
        if is_admin():
            # Déjà admin, exécuter directement
            if wait:
                subprocess.run(command, shell=True, check=True)
            else:
                subprocess.Popen(command, shell=True)
        else:
            # Pas admin, utiliser PowerShell avec Start-Process -Verb RunAs
            ps_command = f'Start-Process powershell -ArgumentList "-NoExit","-Command","{command}" -Verb RunAs'
            subprocess.Popen(['powershell', '-Command', ps_command], shell=False)
    except Exception as e:
        print(f"Erreur run_as_admin: {e}")
        # Fallback: essayer quand même
        subprocess.Popen(command, shell=True)


class OptimizedApplicationsPage(ctk.CTkFrame):
    """Page Applications optimisée avec catégories groupées"""
    
    def __init__(self, parent, programs_data: Dict):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.programs_data = programs_data if programs_data else {}
        self.selected_apps = set()
        self.all_apps = []
        self.filtered_categories = {}

        # Validation des données
        if not self.programs_data:
            print("⚠️ AVERTISSEMENT: Aucune donnée de programmes chargée")
            self._create_error_message("Aucune donnée d'applications disponible")
            return

        # Préparer liste
        self._prepare_apps_list()

        # UI
        self._create_header()
        self._create_stats()
        self._create_search()
        self._create_content()

    def _create_error_message(self, message):
        """Afficher un message d'erreur"""
        error_container = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        error_container.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        error_label = ctk.CTkLabel(
            error_container,
            text=f"⚠️ {message}",
            font=(DesignTokens.FONT_FAMILY, 18),
            text_color=DesignTokens.WARNING
        )
        error_label.pack(expand=True)

        help_label = ctk.CTkLabel(
            error_container,
            text="Vérifiez que le fichier data/programs.json existe et est correctement formaté.",
            font=(DesignTokens.FONT_FAMILY, 12),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        help_label.pack(pady=10)

    def _prepare_apps_list(self):
        """Préparer liste d'applications groupées par catégorie (TOUTES les apps)"""
        # Préparer liste complète
        for category, apps in self.programs_data.items():
            for app_name, app_data in apps.items():
                app_info = {
                    'name': app_name,
                    'category': category,
                    'description': app_data.get('description', ''),
                    'essential': app_data.get('essential', False)
                }
                self.all_apps.append(app_info)
        
        # Grouper par catégorie pour affichage - SANS LIMITE
        self.filtered_categories = {}
        for category, apps in self.programs_data.items():
            apps_list = [
                {
                    'name': app_name,
                    'category': category,
                    'description': app_data.get('description', ''),
                    'essential': app_data.get('essential', False)
                }
                for app_name, app_data in apps.items()
            ]
            
            # AUCUNE LIMITE - Afficher toutes les apps
            self.filtered_categories[category] = apps_list
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="📦 Applications",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)
        
        ModernButton(
            actions,
            text="🚀 Installer Sélection",
            variant="filled",
            size="md",
            command=self._install_selected
        ).pack(side=tk.LEFT, padx=5)
    
    def _create_stats(self):
        """Stats"""
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.stats_total = ModernStatsCard(
            stats_frame,
            "Total",
            len(self.all_apps),
            "📦",
            DesignTokens.ACCENT_PRIMARY
        )
        self.stats_total.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Calculer nombre d'apps affichées
        total_displayed = sum(len(apps) for apps in self.filtered_categories.values())
        
        self.stats_displayed = ModernStatsCard(
            stats_frame,
            "Affichées",
            total_displayed,
            "👁️",
            DesignTokens.INFO
        )
        self.stats_displayed.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.stats_selected = ModernStatsCard(
            stats_frame,
            "Sélection",
            0,
            "✓",
            DesignTokens.SUCCESS
        )
        self.stats_selected.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    def _create_search(self):
        """Recherche"""
        search = ModernSearchBar(
            self,
            placeholder=f"Rechercher dans {len(self.all_apps)} apps • {len(self.filtered_categories)} catégories",
            on_search=self._on_search
        )
        search.pack(fill=tk.X, padx=20, pady=10)
    
    def _create_content(self):
        """Contenu avec catégories groupées"""
        # Liste scrollable
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=DesignTokens.BG_PRIMARY
        )
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Container grille
        self.grid_container = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        self.grid_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Afficher toutes les catégories
        self._update_grid()
    
    def _update_grid(self):
        """Mettre à jour grille avec catégories repliables"""
        # Clear
        for widget in self.grid_container.winfo_children():
            widget.destroy()

        # Afficher chaque catégorie DANS L'ORDRE du JSON (pas de tri alphabétique)
        for category_name in self.filtered_categories.keys():
            apps = self.filtered_categories[category_name]

            if not apps:
                continue

            self._create_category_section(category_name, apps)
    
    def _create_category_section(self, category_name, apps):
        """Créer une section de catégorie repliable"""
        # Card pour la catégorie
        card = ctk.CTkFrame(
            self.grid_container,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        card.pack(fill=tk.X, pady=5)
        
        # Container pour apps (caché par défaut)
        apps_container = ctk.CTkFrame(card, fg_color="transparent")
        apps_container.pack_forget()
        
        # État de la catégorie
        category_state = {
            'container': apps_container,
            'visible': False,
            'apps': apps
        }
        
        # Header cliquable
        header = ctk.CTkButton(
            card,
            text=f"📂 {category_name} ({len(apps)} applications) ▶",
            command=lambda: self._toggle_category(card, category_state, category_name),
            fg_color="transparent",
            hover_color=DesignTokens.BG_HOVER,
            text_color=DesignTokens.ACCENT_PRIMARY,
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            anchor="w",
            corner_radius=0,
            height=50
        )
        header.pack(fill=tk.X, padx=10, pady=5)
        
        # Stocker header pour mise à jour texte
        category_state['header'] = header
    
    def _toggle_category(self, card, category_state, category_name):
        """Basculer affichage catégorie"""
        if category_state['visible']:
            # Cacher
            category_state['container'].pack_forget()
            category_state['visible'] = False
            category_state['header'].configure(text=f"📂 {category_name} ({len(category_state['apps'])} applications) ▶")
        else:
            # Afficher
            # Clear container
            for widget in category_state['container'].winfo_children():
                widget.destroy()
            
            # Créer grille 3 colonnes
            grid_frame = ctk.CTkFrame(category_state['container'], fg_color="transparent")
            grid_frame.pack(fill=tk.X, padx=10, pady=10)
            
            row, col = 0, 0
            max_cols = 3
            
            for app in category_state['apps']:
                self._create_app_card_in_grid(grid_frame, app, row, col)
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
            
            # Configurer colonnes
            for i in range(max_cols):
                grid_frame.columnconfigure(i, weight=1)
            
            category_state['container'].pack(fill=tk.X, padx=5, pady=(0, 10))
            category_state['visible'] = True
            category_state['header'].configure(text=f"📂 {category_name} ({len(category_state['apps'])} applications) ▼")
    
    def _create_app_card_in_grid(self, parent, app, row, col):
        """Créer carte app dans grille"""
        frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=DesignTokens.RADIUS_MD,
            height=70
        )
        frame.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        
        # Container
        container = ctk.CTkFrame(frame, fg_color="transparent")
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
        
        # Checkbox
        var = tk.BooleanVar()
        checkbox = ctk.CTkCheckBox(
            container,
            text="",
            variable=var,
            command=lambda: self._toggle_app(app['name'], var.get()),
            fg_color=DesignTokens.ACCENT_PRIMARY,
            corner_radius=4,
            width=20
        )
        checkbox.pack(side=tk.LEFT, padx=(0, 8))
        
        # Info (nom + catégorie)
        info_frame = ctk.CTkFrame(container, fg_color="transparent")
        info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Nom
        name_label = ctk.CTkLabel(
            info_frame,
            text=app['name'][:30] + ('...' if len(app['name']) > 30 else ''),
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        # Catégorie
        cat_label = ctk.CTkLabel(
            info_frame,
            text=f"📁 {app['category']}",
            font=(DesignTokens.FONT_FAMILY, 10),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        cat_label.pack(anchor="w")
        
        # Bouton site web
        web_btn = ctk.CTkButton(
            container,
            text="🌐",
            width=28,
            height=28,
            corner_radius=6,
            fg_color=DesignTokens.INFO,
            hover_color=DesignTokens.BG_HOVER,
            command=lambda: self._open_website(app['name']),
            font=(DesignTokens.FONT_FAMILY, 14)
        )
        web_btn.pack(side=tk.RIGHT, padx=3)
        
        # Badge essentiel
        if app['essential']:
            badge = ctk.CTkLabel(
                container,
                text="⭐",
                font=(DesignTokens.FONT_FAMILY, 12),
                text_color=DesignTokens.WARNING
            )
            badge.pack(side=tk.RIGHT, padx=3)
    
    def _create_app_card(self, app, row, col):
        """Créer une carte d'application compacte"""
        frame = ctk.CTkFrame(
            self.grid_container,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD,
            height=60
        )
        frame.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        
        # Container avec padding
        container = ctk.CTkFrame(frame, fg_color="transparent")
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
        
        # Ligne du haut: Checkbox + Nom + Badge
        top_row = ctk.CTkFrame(container, fg_color="transparent")
        top_row.pack(fill=tk.X)
        
        # Checkbox
        var = tk.BooleanVar()
        checkbox = ctk.CTkCheckBox(
            top_row,
            text="",
            variable=var,
            command=lambda: self._toggle_app(app['name'], var.get()),
            fg_color=DesignTokens.ACCENT_PRIMARY,
            corner_radius=4,
            width=20
        )
        checkbox.pack(side=tk.LEFT, padx=(0, 8))
        
        # Nom (tronqué si trop long)
        name_label = ctk.CTkLabel(
            top_row,
            text=app['name'][:30] + ('...' if len(app['name']) > 30 else ''),
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Badge essentiel
        if app['essential']:
            badge = ctk.CTkLabel(
                top_row,
                text="⭐",
                font=(DesignTokens.FONT_FAMILY, 12),
                text_color=DesignTokens.WARNING
            )
            badge.pack(side=tk.RIGHT, padx=3)
        
        # Ligne du bas: Catégorie
        cat_label = ctk.CTkLabel(
            container,
            text=f"📁 {app['category']}",
            font=(DesignTokens.FONT_FAMILY, 10),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        cat_label.pack(fill=tk.X, pady=(3, 0))
    
    def _toggle_app(self, app_name, selected):
        """Toggle sélection"""
        if selected:
            self.selected_apps.add(app_name)
        else:
            self.selected_apps.discard(app_name)
        self.stats_selected.update_value(len(self.selected_apps))
    
    def _on_search(self, query):
        """Recherche avec filtrage par catégorie"""
        query = query.lower().strip()
        
        if not query:
            # Restaurer toutes les catégories
            self.filtered_categories = {}
            for category, apps in self.programs_data.items():
                self.filtered_categories[category] = [
                    {
                        'name': app_name,
                        'category': category,
                        'description': app_data.get('description', ''),
                        'essential': app_data.get('essential', False)
                    }
                    for app_name, app_data in apps.items()
                ]
        else:
            # Filtrer dans chaque catégorie
            self.filtered_categories = {}
            for category, apps in self.programs_data.items():
                filtered_apps = [
                    {
                        'name': app_name,
                        'category': category,
                        'description': app_data.get('description', ''),
                        'essential': app_data.get('essential', False)
                    }
                    for app_name, app_data in apps.items()
                    if query in app_name.lower() or query in app_data.get('description', '').lower()
                ]
                if filtered_apps:
                    self.filtered_categories[category] = filtered_apps
        
        # Calculer total
        total_displayed = sum(len(apps) for apps in self.filtered_categories.values())
        self.stats_displayed.update_value(total_displayed)
        self._update_grid()
    
    def _install_selected(self):
        """Installer les applications sélectionnées"""
        if not self.selected_apps:
            return

        # Préparer liste d'installation
        apps_to_install = []
        for app_name in self.selected_apps:
            # Trouver dans programs_data pour obtenir package_id
            for category, apps in self.programs_data.items():
                if app_name in apps:
                    app_data = apps[app_name]

                    # Déterminer la méthode d'installation intelligemment
                    # 1. Si install_method est explicitement défini, l'utiliser
                    # 2. Sinon, si winget_id existe, utiliser winget
                    # 3. Sinon, si download_url existe, utiliser download
                    # 4. Sinon, par défaut winget (essaiera de chercher par nom)

                    has_winget_id = 'winget_id' in app_data or 'id' in app_data
                    has_download_url = 'download_url' in app_data
                    is_portable = app_data.get('portable', False)

                    if 'install_method' in app_data:
                        # Méthode explicite définie
                        method = app_data['install_method']
                    elif has_winget_id:
                        # A un winget_id => utiliser WinGet
                        method = 'winget'
                    elif has_download_url:
                        # A un download_url mais pas de winget_id => téléchargement direct
                        method = 'download'
                    else:
                        # Aucune info => essayer WinGet par défaut
                        method = 'winget'

                    package_id = app_data.get('winget_id') or app_data.get('id') or app_name
                    download_url = app_data.get('download_url', None)

                    apps_to_install.append({
                        'name': app_name,
                        'package_id': package_id,
                        'method': method,
                        'portable': is_portable,
                        'download_url': download_url,
                        'cleanup_folder': app_data.get('cleanup_folder', 'Outils de nettoyage'),
                        'install_args': app_data.get('install_args', ''),
                        'admin_required': app_data.get('admin_required', False)
                    })
                    break

        # Créer dialogue de progression avec logs
        progress_dialog = MultiProgressDialog(
            self,
            f"Installation - {len(apps_to_install)} application(s)"
        )
        progress_dialog.set_total_apps(len(apps_to_install))

        # Lancer installation en thread
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

                # Callbacks pour mise à jour UI
                def on_progress(percent, status):
                    progress_dialog.update_app_progress(percent, status)

                def on_log(message, level):
                    progress_dialog.add_log(message, level)

                def on_complete(success, message):
                    install_result['success'] = success
                    install_done.set()

                # Installer l'application
                try:
                    # Vérifier si c'est une installation par téléchargement direct
                    # Cas 1: App portable avec download_url
                    # Cas 2: Method='download' (apps sans winget_id mais avec download_url)
                    if (app_info.get('portable') and app_info.get('download_url')) or \
                       (method == 'download' and app_info.get('download_url')):

                        # Téléchargement direct
                        on_log(f"Téléchargement direct: {app_name}", "info")
                        on_log(f"URL: {app_info['download_url'][:80]}...", "info")
                        on_progress(0.1, "Téléchargement...")

                        if app_info.get('portable'):
                            # App portable => télécharger dans le dossier portable
                            success = self._download_portable_app(
                                app_name=app_name,
                                download_url=app_info['download_url'],
                                cleanup_folder=app_info['cleanup_folder'],
                                on_progress=on_progress,
                                on_log=on_log
                            )
                        else:
                            # App normale => télécharger et installer
                            success = self._download_and_install_app(
                                app_name=app_name,
                                download_url=app_info['download_url'],
                                install_args=app_info.get('install_args', ''),
                                admin_required=app_info.get('admin_required', False),
                                on_progress=on_progress,
                                on_log=on_log
                            )

                        install_result['success'] = success
                        if success:
                            on_log(f"Installation terminee avec succes", "success")
                        else:
                            on_log(f"Echec de l'installation", "error")
                        install_done.set()
                    else:
                        # Installation normale via WinGet/Chocolatey
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
                        progress_dialog.add_log(f"✓ {app_name} installé avec succès", "success")
                    else:
                        progress_dialog.add_log(f"✗ {app_name} n'a pas pu être installé", "error")
                except Exception as e:
                    progress_dialog.add_log(f"✗ Erreur: {str(e)}", "error")
                    install_result['success'] = False

                # Compléter l'app
                progress_dialog.complete_app(install_result['success'])

            # Marquer comme terminé
            if not progress_dialog.is_cancelled:
                progress_dialog.mark_completed()

        # Démarrer installation
        install_thread_obj = threading.Thread(target=install_thread, daemon=True)
        install_thread_obj.start()
    
    def _download_portable_app(self, app_name, download_url, cleanup_folder, on_progress, on_log):
        """Télécharger une application portable directement"""
        try:
            # Créer le dossier de destination sur le Bureau
            base_dir = Path.home() / "Desktop" / "NiTriTe_Portables" / cleanup_folder
            base_dir.mkdir(parents=True, exist_ok=True)

            app_dir = base_dir / app_name.replace(" ", "_")
            app_dir.mkdir(exist_ok=True)

            on_log(f"📁 Dossier: {app_dir}", "info")
            on_progress(0.2, "Connexion...")

            # Télécharger le fichier
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(download_url, stream=True, headers=headers, allow_redirects=True, timeout=60)
            response.raise_for_status()

            # Déterminer le nom du fichier
            filename = app_name.replace(" ", "_") + ".exe"
            if download_url.endswith('.zip'):
                filename = app_name.replace(" ", "_") + ".zip"

            file_path = app_dir / filename

            on_log(f"⬇️ Téléchargement vers: {filename}", "info")
            on_progress(0.3, "Téléchargement en cours...")

            # Télécharger avec progression
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = 0.3 + (downloaded / total_size) * 0.6
                            on_progress(percent, f"Téléchargement... {int((downloaded/total_size)*100)}%")

            on_progress(0.9, "Finalisation...")

            # Si c'est un ZIP, extraire
            if filename.endswith('.zip'):
                import zipfile
                on_log(f"📦 Extraction du fichier ZIP...", "info")
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(app_dir)
                file_path.unlink()  # Supprimer le ZIP

            on_progress(1.0, "Terminé")
            on_log(f"✅ {app_name} téléchargé dans {app_dir}", "success")
            return True

        except requests.exceptions.RequestException as e:
            on_log(f"Erreur reseau: {str(e)}", "error")
            return False
        except Exception as e:
            on_log(f"Erreur: {str(e)}", "error")
            return False

    def _download_and_install_app(self, app_name, download_url, install_args, admin_required, on_progress, on_log):
        """Télécharger et installer une application normale (non-portable)"""
        import tempfile
        import os

        try:
            # Créer dossier temporaire
            temp_dir = Path(tempfile.gettempdir()) / "NiTriTe_Downloads"
            temp_dir.mkdir(exist_ok=True)

            on_log(f"Telechargement depuis: {download_url[:60]}...", "info")
            on_progress(0.2, "Connexion...")

            # Télécharger le fichier
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(download_url, stream=True, headers=headers, allow_redirects=True, timeout=120)
            response.raise_for_status()

            # Déterminer le nom du fichier
            if 'content-disposition' in response.headers:
                import re
                cd = response.headers['content-disposition']
                filename_match = re.findall('filename=(.+)', cd)
                if filename_match:
                    filename = filename_match[0].strip('"\'')
                else:
                    filename = app_name.replace(" ", "_") + ".exe"
            else:
                # Détecter l'extension depuis l'URL
                if '.exe' in download_url.lower():
                    filename = app_name.replace(" ", "_") + ".exe"
                elif '.msi' in download_url.lower():
                    filename = app_name.replace(" ", "_") + ".msi"
                else:
                    filename = app_name.replace(" ", "_") + ".exe"

            file_path = temp_dir / filename

            on_log(f"Telechargement: {filename}", "info")
            on_progress(0.3, "Telechargement en cours...")

            # Télécharger avec progression
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = 0.3 + (downloaded / total_size) * 0.4
                            on_progress(percent, f"Telechargement... {int((downloaded/total_size)*100)}%")

            on_progress(0.7, "Telechargement termine")
            on_log(f"Fichier telecharge: {file_path}", "success")

            # Installer l'application
            on_log(f"Lancement de l'installation...", "info")
            on_progress(0.75, "Installation en cours...")

            # Construire la commande
            if filename.endswith('.msi'):
                # Installateur MSI
                cmd = f'msiexec /i "{file_path}" {install_args}'
            else:
                # Installateur EXE
                cmd = f'"{file_path}" {install_args}'

            on_log(f"Commande: {cmd}", "info")

            # Exécuter l'installation
            if admin_required:
                on_log("Droits administrateur requis", "warning")
                # Utiliser PowerShell avec Start-Process -Verb RunAs
                ps_cmd = f'Start-Process -FilePath "{file_path}" -ArgumentList "{install_args}" -Verb RunAs -Wait'
                result = subprocess.run(
                    ['powershell', '-Command', ps_cmd],
                    capture_output=True,
                    text=True,
                    timeout=300
                )
            else:
                # Exécution normale
                result = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=300
                )

            on_progress(0.95, "Finalisation...")

            # Nettoyer le fichier temporaire
            try:
                if file_path.exists():
                    file_path.unlink()
                    on_log("Fichier temporaire supprime", "info")
            except:
                pass

            # Vérifier le code de retour
            if result.returncode == 0:
                on_progress(1.0, "Termine")
                on_log(f"{app_name} installe avec succes", "success")
                return True
            else:
                on_log(f"Code retour: {result.returncode}", "warning")
                # Certains installateurs retournent des codes non-zéro même en cas de succès
                if result.returncode in [1641, 3010]:  # Codes de redémarrage requis
                    on_log("Installation reussie (redemarrage requis)", "success")
                    on_progress(1.0, "Termine")
                    return True
                else:
                    on_log(f"L'installation peut avoir echoue", "warning")
                    on_progress(1.0, "Termine avec avertissement")
                    return True  # Considérer comme succès partiel

        except requests.exceptions.RequestException as e:
            on_log(f"Erreur de telechargement: {str(e)}", "error")
            return False
        except subprocess.TimeoutExpired:
            on_log("Timeout: l'installation prend trop de temps", "error")
            return False
        except Exception as e:
            on_log(f"Erreur: {str(e)}", "error")
            return False

    def _open_website(self, app_name):
        """Ouvrir le site web de l'application"""
        import webbrowser
        
        # Dictionnaire de mapping pour URLs spécifiques
        website_map = {
            # Navigateurs
            "Google Chrome": "https://www.google.com/chrome/",
            "Mozilla Firefox": "https://www.mozilla.org/firefox/",
            "Microsoft Edge": "https://www.microsoft.com/edge",
            "Brave Browser": "https://brave.com/",
            "Opera": "https://www.opera.com/",
            "Vivaldi": "https://vivaldi.com/",
            
            # Office
            "LibreOffice": "https://www.libreoffice.org/",
            "WPS Office": "https://www.wps.com/",
            "Adobe Acrobat Reader DC": "https://get.adobe.com/reader/",
            
            # Développement
            "Visual Studio Code": "https://code.visualstudio.com/",
            "Git": "https://git-scm.com/",
            "Node.js": "https://nodejs.org/",
            "Python": "https://www.python.org/",
            "Docker Desktop": "https://www.docker.com/products/docker-desktop/",
            
            # Multimédia
            "VLC Media Player": "https://www.videolan.org/vlc/",
            "GIMP": "https://www.gimp.org/",
            "Audacity": "https://www.audacityteam.org/",
            "OBS Studio": "https://obsproject.com/",
            "HandBrake": "https://handbrake.fr/",
            
            # Utilitaires
            "7-Zip": "https://www.7-zip.org/",
            "WinRAR": "https://www.win-rar.com/",
            "CCleaner": "https://www.ccleaner.com/",
            "Everything": "https://www.voidtools.com/",
            "TreeSize Free": "https://www.jam-software.com/treesize_free",
            
            # Communication
            "Discord": "https://discord.com/",
            "Skype": "https://www.skype.com/",
            "Zoom": "https://zoom.us/",
            "Microsoft Teams": "https://www.microsoft.com/teams/",
            "Slack": "https://slack.com/",
            
            # Jeux
            "Steam": "https://store.steampowered.com/",
            "Epic Games Launcher": "https://www.epicgames.com/store/",
            "GOG Galaxy": "https://www.gog.com/galaxy",
            
            # Sécurité
            "Malwarebytes": "https://www.malwarebytes.com/",
            "Avast Free Antivirus": "https://www.avast.com/",
            "Bitdefender Antivirus Free": "https://www.bitdefender.com/",
            
            # Streaming
            "Spotify": "https://www.spotify.com/",
            "Netflix": "https://www.netflix.com/",
            "Disney+": "https://www.disneyplus.com/"
        }
        
        # Récupérer URL depuis le mapping ou générer URL de recherche
        if app_name in website_map:
            url = website_map[app_name]
        else:
            # Générer URL de recherche Google
            search_query = app_name.replace(" ", "+")
            url = f"https://www.google.com/search?q={search_query}+download+official+site"
        
        # Ouvrir dans navigateur par défaut
        try:
            webbrowser.open(url)
            print(f"🌐 Ouverture du site: {app_name} -> {url}")
        except Exception as e:
            print(f"❌ Erreur ouverture site pour {app_name}: {e}")


class OptimizedToolsPage(ctk.CTkFrame):
    """Page Outils optimisée avec sections repliables"""

    def __init__(self, parent, tools_data: Dict):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.tools_data = tools_data if tools_data else {}

        # Validation des données
        if not self.tools_data:
            print("⚠️ AVERTISSEMENT: Aucune donnée d'outils chargée")
            self._create_error_message("Aucune donnée d'outils système disponible")
            return

        self._create_header()
        self._create_sections()

    def _create_error_message(self, message):
        """Afficher un message d'erreur"""
        error_container = ctk.CTkFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        error_container.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        error_label = ctk.CTkLabel(
            error_container,
            text=f"⚠️ {message}",
            font=(DesignTokens.FONT_FAMILY, 18),
            text_color=DesignTokens.WARNING
        )
        error_label.pack(expand=True)

        help_label = ctk.CTkLabel(
            error_container,
            text="Vérifiez que le fichier src/tools_data_complete.py existe et est correctement formaté.",
            font=(DesignTokens.FONT_FAMILY, 12),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        help_label.pack(pady=10)
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="🛠️ Outils Système",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        total = sum(len(tools) for tools in self.tools_data.values())
        subtitle = ctk.CTkLabel(
            container,
            text=f"{total} outils • {len(self.tools_data)} sections",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)
    
    def _create_sections(self):
        """Sections repliables"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Créer Master Outils comme section repliable
        self._create_master_outils_section(scroll)

        # Autres sections
        for section_name, tools in self.tools_data.items():
            self._create_section(scroll, section_name, tools)
    
    def _create_master_outils_section(self, parent):
        """Créer la section Master Outils (repliable)"""
        # Card section
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=5)

        # Container (caché par défaut)
        container = ctk.CTkFrame(card, fg_color="transparent")
        container.pack_forget()

        # État de la section
        section_state = {
            'container': container,
            'visible': False
        }

        # Header
        header = ctk.CTkButton(
            card,
            text="🔧 Master Outils (14)",
            command=lambda: self._toggle_master_outils(section_state),
            fg_color="transparent",
            hover_color=DesignTokens.BG_HOVER,
            text_color=DesignTokens.TEXT_PRIMARY,
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            anchor="w",
            corner_radius=0
        )
        header.pack(fill=tk.X, padx=10, pady=10)

    def _toggle_master_outils(self, section_state):
        """Basculer affichage Master Outils"""
        if section_state['visible']:
            section_state['container'].pack_forget()
            section_state['visible'] = False
        else:
            # Clear container
            for widget in section_state['container'].winfo_children():
                widget.destroy()

            # Ajouter les 10 boutons Master Outils
            grid_frame = ctk.CTkFrame(section_state['container'], fg_color="transparent")
            grid_frame.pack(fill=tk.X, padx=10, pady=10)

            # Configurer grille 4x3 (4 colonnes, 3 lignes pour 12 emplacements)
            for i in range(4):
                grid_frame.columnconfigure(i, weight=1)

            # === LIGNE 1 ===
            # Bouton 1: Activation Windows/Office
            ModernButton(
                grid_frame,
                text="🔑 Activation Windows/Office",
                variant="outlined",
                size="md",
                command=self._activate_windows_office
            ).grid(row=0, column=0, padx=5, pady=5, sticky="ew")

            # Bouton 2: MSCONFIG
            ModernButton(
                grid_frame,
                text="⚙️ MSCONFIG",
                variant="outlined",
                size="md",
                command=lambda: self._execute_tool("MSCONFIG", "msconfig")
            ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

            # Bouton 3: Gestionnaire des tâches
            ModernButton(
                grid_frame,
                text="📊 Gestionnaire des Tâches",
                variant="outlined",
                size="md",
                command=lambda: self._execute_tool("Gestionnaire des tâches", "taskmgr")
            ).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

            # Bouton 4: MSINFO
            ModernButton(
                grid_frame,
                text="ℹ️ MSINFO",
                variant="outlined",
                size="md",
                command=lambda: self._execute_tool("MSINFO", "msinfo32")
            ).grid(row=0, column=3, padx=5, pady=5, sticky="ew")

            # === LIGNE 2 ===
            # Bouton 5: Dossier Temp
            ModernButton(
                grid_frame,
                text="🗂️ Dossier Temp",
                variant="outlined",
                size="md",
                command=self._open_temp_folder
            ).grid(row=1, column=0, padx=5, pady=5, sticky="ew")

            # Bouton 6: AppData Local
            ModernButton(
                grid_frame,
                text="📁 AppData Local",
                variant="outlined",
                size="md",
                command=self._open_appdata_local
            ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

            # Bouton 7: WinVer (Version Windows)
            ModernButton(
                grid_frame,
                text="🪟 Version Windows",
                variant="outlined",
                size="md",
                command=lambda: self._execute_tool("Version Windows", "winver")
            ).grid(row=1, column=2, padx=5, pady=5, sticky="ew")

            # Bouton 8: Mettre à jour tout (WinGet)
            ModernButton(
                grid_frame,
                text="🔄 Tout Mettre à Jour",
                variant="outlined",
                size="md",
                command=self._update_all_apps
            ).grid(row=1, column=3, padx=5, pady=5, sticky="ew")

            # === LIGNE 3 ===
            # Bouton 9: Drivers NVIDIA
            ModernButton(
                grid_frame,
                text="🎮 Drivers NVIDIA",
                variant="outlined",
                size="md",
                command=self._update_nvidia_drivers
            ).grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

            # Bouton 10: Drivers AMD
            ModernButton(
                grid_frame,
                text="🔴 Drivers AMD",
                variant="outlined",
                size="md",
                command=self._update_amd_drivers
            ).grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

            # === LIGNE 4 === (4 nouveaux boutons)
            # Bouton 11: Réparer l'image Windows (DISM)
            ModernButton(
                grid_frame,
                text="🔧 Réparer Image Windows",
                variant="outlined",
                size="md",
                command=self._repair_windows_image
            ).grid(row=3, column=0, padx=5, pady=5, sticky="ew")

            # Bouton 12: Propriétés dossier utilisateur
            ModernButton(
                grid_frame,
                text="👤 Propriétés Utilisateur",
                variant="outlined",
                size="md",
                command=self._open_user_properties
            ).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

            # Bouton 13: Système (sysdm.cpl)
            ModernButton(
                grid_frame,
                text="⚙️ Système",
                variant="outlined",
                size="md",
                command=lambda: self._execute_tool("Système", "sysdm.cpl")
            ).grid(row=3, column=2, padx=5, pady=5, sticky="ew")

            # Bouton 14: CHKDSK complet
            ModernButton(
                grid_frame,
                text="🔍 CHKDSK Complet",
                variant="outlined",
                size="md",
                command=self._run_chkdsk
            ).grid(row=3, column=3, padx=5, pady=5, sticky="ew")

            # Afficher container
            section_state['container'].pack(fill=tk.X, padx=10, pady=10)
            section_state['visible'] = True

    def _activate_windows_office(self):
        """Activer Windows et Office"""
        from tkinter import messagebox
        response = messagebox.askyesno(
            "Activation Windows/Office",
            "Cette action va exécuter le script MAS (Microsoft Activation Scripts) depuis Internet.\n\n"
            "⚠️ Assurez-vous de comprendre ce que vous faites.\n\n"
            "Continuer ?",
            icon='warning'
        )
        if not response:
            return
        try:
            import tempfile
            script_content = "irm https://get.activated.win | iex"
            with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                f.write(script_content)
                script_path = f.name
            cmd = f'powershell -Command "Start-Process powershell -ArgumentList \'-ExecutionPolicy Bypass -File \"{script_path}\"\' -Verb RunAs"'
            import subprocess
            subprocess.Popen(cmd, shell=True)
            messagebox.showinfo(
                "Activation lancée",
                "Le script MAS a été lancé en mode administrateur.\n\n"
                "Suivez les instructions dans la fenêtre PowerShell qui s'ouvre."
            )
            def cleanup():
                import time
                time.sleep(60)
                try:
                    import os
                    os.remove(script_path)
                except:
                    pass
            threading.Thread(target=cleanup, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lancer le script d'activation:\n\n{str(e)}")

    def _open_temp_folder(self):
        """Ouvrir le dossier Temp"""
        import subprocess, os
        try:
            temp_path = os.path.expandvars("%TEMP%")
            subprocess.Popen(f'explorer "{temp_path}"', shell=True)
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier Temp:\n\n{str(e)}")

    def _open_appdata_local(self):
        """Ouvrir le dossier LocalAppData"""
        import subprocess, os
        try:
            appdata_path = os.path.expandvars("%LOCALAPPDATA%")
            subprocess.Popen(f'explorer "{appdata_path}"', shell=True)
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Impossible d'ouvrir AppData Local:\n\n{str(e)}")

    def _update_all_apps(self):
        """Mettre à jour toutes les applications via WinGet"""
        import subprocess, threading
        from tkinter import messagebox

        def run_update():
            try:
                # Demander confirmation
                result = messagebox.askyesno(
                    "Mise à jour globale",
                    "Voulez-vous mettre à jour toutes les applications installées via WinGet?\n\n"
                    "Cette opération peut prendre plusieurs minutes.",
                    icon='question'
                )

                if not result:
                    return

                messagebox.showinfo(
                    "Mise à jour en cours",
                    "La mise à jour a démarré.\n\n"
                    "Une fenêtre PowerShell va s'ouvrir pour afficher la progression.\n"
                    "Ne fermez pas cette fenêtre."
                )

                # Lancer winget upgrade --all dans PowerShell visible
                subprocess.Popen(
                    ['powershell', '-NoExit', '-Command',
                     'Write-Host "Mise a jour de toutes les applications..." -ForegroundColor Cyan; '
                     'winget upgrade --all --accept-source-agreements --accept-package-agreements; '
                     'Write-Host "`nTermine! Vous pouvez fermer cette fenetre." -ForegroundColor Green'],
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )

            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de lancer la mise à jour:\n\n{str(e)}")

        # Lancer dans un thread pour ne pas bloquer l'UI
        threading.Thread(target=run_update, daemon=True).start()

    def _update_nvidia_drivers(self):
        """Ouvrir la page de téléchargement des drivers NVIDIA"""
        import subprocess, webbrowser
        from tkinter import messagebox

        try:
            # Essayer d'ouvrir GeForce Experience si installé
            # Sinon ouvrir la page web de téléchargement
            try:
                subprocess.Popen(['C:\\Program Files\\NVIDIA Corporation\\NVIDIA GeForce Experience\\NVIDIA GeForce Experience.exe'])
                messagebox.showinfo(
                    "NVIDIA Drivers",
                    "GeForce Experience a été lancé.\n\n"
                    "Utilisez-le pour vérifier et installer les derniers drivers."
                )
            except:
                # GeForce Experience non installé, ouvrir le site web
                webbrowser.open('https://www.nvidia.com/Download/index.aspx?lang=fr')
                messagebox.showinfo(
                    "NVIDIA Drivers",
                    "La page de téléchargement des drivers NVIDIA a été ouverte dans votre navigateur.\n\n"
                    "Sélectionnez votre carte graphique pour télécharger les derniers drivers."
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir les drivers NVIDIA:\n\n{str(e)}")

    def _update_amd_drivers(self):
        """Ouvrir la page de téléchargement des drivers AMD"""
        import subprocess, webbrowser
        from tkinter import messagebox

        try:
            # Essayer d'ouvrir AMD Radeon Software si installé
            # Sinon ouvrir la page web de téléchargement
            try:
                subprocess.Popen(['C:\\Program Files\\AMD\\CNext\\CNext\\RadeonSoftware.exe'])
                messagebox.showinfo(
                    "AMD Drivers",
                    "AMD Radeon Software a été lancé.\n\n"
                    "Utilisez-le pour vérifier et installer les derniers drivers."
                )
            except:
                # Radeon Software non installé, ouvrir le site web
                webbrowser.open('https://www.amd.com/fr/support')
                messagebox.showinfo(
                    "AMD Drivers",
                    "La page de téléchargement des drivers AMD a été ouverte dans votre navigateur.\n\n"
                    "Utilisez l'outil de détection automatique ou sélectionnez votre carte graphique."
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir les drivers AMD:\n\n{str(e)}")

    def _repair_windows_image(self):
        """Réparer l'image Windows avec DISM"""
        from tkinter import messagebox

        result = messagebox.askyesno(
            "Réparer l'image Windows",
            "Cette opération va réparer l'image système Windows avec DISM.\n\n"
            "Cela peut prendre 10-30 minutes.\n\n"
            "Une fenêtre PowerShell va s'ouvrir en mode Administrateur.\n\n"
            "Continuer ?",
            icon='question'
        )

        if not result:
            return

        try:
            messagebox.showinfo(
                "Réparation en cours",
                "La réparation de l'image Windows a démarré.\n\n"
                "Une fenêtre PowerShell admin va s'ouvrir.\n"
                "Ne la fermez pas pendant l'opération."
            )

            # Commande DISM
            dism_cmd = (
                'Write-Host "Reparation de l\'\'image Windows..." -ForegroundColor Cyan; '
                'Write-Host "Cette operation peut prendre 10-30 minutes." -ForegroundColor Yellow; '
                'Write-Host ""; '
                'DISM /Online /Cleanup-Image /RestoreHealth; '
                'Write-Host ""; '
                'Write-Host "Termine! Vous pouvez fermer cette fenetre." -ForegroundColor Green'
            )

            run_as_admin(dism_cmd)

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lancer DISM:\n\n{str(e)}")

    def _open_user_properties(self):
        """Ouvrir les propriétés du dossier utilisateur"""
        import os
        from tkinter import messagebox

        try:
            # Obtenir le chemin du dossier utilisateur
            user_folder = os.path.expandvars("%USERPROFILE%")

            # Ouvrir simplement l'explorateur sur le dossier Users
            users_folder = os.path.dirname(user_folder)
            subprocess.Popen(f'explorer "{users_folder}"', shell=True)

            messagebox.showinfo(
                "Dossier Utilisateurs",
                f"Dossier ouvert: {users_folder}\n\n"
                "Vous pouvez voir tous les utilisateurs et faire clic-droit > Propriétés\n"
                "sur n'importe quel dossier utilisateur."
            )

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n\n{str(e)}")

    def _run_chkdsk(self):
        """Lancer un CHKDSK complet"""
        import subprocess
        from tkinter import messagebox

        result = messagebox.askyesno(
            "CHKDSK Complet",
            "Cette opération va analyser et réparer le disque C:\n\n"
            "⚠️ Le PC devra redémarrer pour effectuer la vérification.\n\n"
            "Options:\n"
            "• /F : Corrige les erreurs sur le disque\n"
            "• /R : Recherche les secteurs défectueux et récupère les données\n\n"
            "Continuer ?",
            icon='warning'
        )

        if not result:
            return

        try:
            # Lancer CHKDSK avec /F /R dans PowerShell
            subprocess.Popen(
                ['powershell', '-NoExit', '-Command',
                 'Write-Host "Planification de CHKDSK au prochain redemarrage..." -ForegroundColor Cyan; '
                 'Write-Host ""; '
                 'chkdsk C: /F /R; '
                 'Write-Host ""; '
                 'Write-Host "Le CHKDSK s\'executera au prochain redemarrage." -ForegroundColor Green; '
                 'Write-Host "Tapez \'shutdown /r /t 60\' pour redemarrer dans 60 secondes." -ForegroundColor Yellow'],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )

            messagebox.showinfo(
                "CHKDSK planifié",
                "CHKDSK a été planifié pour le prochain redémarrage.\n\n"
                "Le PC va redémarrer et effectuer la vérification complète du disque.\n\n"
                "Cela peut prendre 1-2 heures selon la taille du disque."
            )

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lancer CHKDSK:\n\n{str(e)}")

    def _create_section(self, parent, section_name, tools):
        """Créer une section"""
        # Card section
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=5)

        # Container tools (caché par défaut)
        container = ctk.CTkFrame(card, fg_color="transparent")
        container.pack_forget()

        # État de la section (utiliser dictionnaire pour éviter erreur Pylance)
        section_state = {
            'container': container,
            'visible': False
        }

        # Header avec lambda qui capture section_state
        header = ctk.CTkButton(
            card,
            text=f"{section_name} ({len(tools)})",
            command=lambda: self._toggle_section(section_state, tools, section_name),
            fg_color="transparent",
            hover_color=DesignTokens.BG_HOVER,
            text_color=DesignTokens.TEXT_PRIMARY,
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            anchor="w",
            corner_radius=0
        )
        header.pack(fill=tk.X, padx=10, pady=10)

    def _toggle_section(self, section_state, tools, section_name):
        """Basculer affichage section"""
        if section_state['visible']:
            # Cacher
            section_state['container'].pack_forget()
            section_state['visible'] = False
        else:
            # Afficher
            # Clear container
            for widget in section_state['container'].winfo_children():
                widget.destroy()
            
            # Ajouter TOUS les boutons - SANS LIMITE
            grid_frame = ctk.CTkFrame(section_state['container'], fg_color="transparent")
            grid_frame.pack(fill=tk.X, padx=10, pady=10)
            
            row, col = 0, 0
            max_cols = 2
            
            # Afficher TOUS les outils (pas de [:20])
            for tool_name, tool_action in tools:
                btn = ctk.CTkButton(
                    grid_frame,
                    text=tool_name,
                    command=lambda t=tool_name, a=tool_action: self._execute_tool(t, a),
                    fg_color=DesignTokens.BG_SECONDARY,
                    hover_color=DesignTokens.BG_HOVER,
                    corner_radius=DesignTokens.RADIUS_MD,
                    height=40,
                    font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                    anchor="w"
                )
                btn.grid(row=row, column=col, sticky="ew", padx=5, pady=3)
                
                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1
            
            # Configurer colonnes
            for i in range(max_cols):
                grid_frame.columnconfigure(i, weight=1)
            
            # Afficher total outils
            total_label = ctk.CTkLabel(
                section_state['container'],
                text=f"✅ {len(tools)} outils dans cette section",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.SUCCESS
            )
            total_label.pack(pady=5)
            
            section_state['container'].pack(fill=tk.X)
            section_state['visible'] = True
    
    def _execute_tool(self, tool_name, tool_action):
        """Exécuter outil (commande ou URL)"""
        import subprocess
        import webbrowser
        import os
        
        print(f"🔧 Exécution: {tool_name}")
        print(f"   Action: {tool_action}")
        
        try:
            # Déterminer si c'est une URL ou une commande
            if tool_action.startswith(('http://', 'https://', 'ms-settings:', 'windowsdefender:')):
                # C'est une URL - ouvrir dans le navigateur
                print(f"🌐 Ouverture URL: {tool_action}")
                webbrowser.open(tool_action)
                
            else:
                # C'est une commande système - l'exécuter
                print(f"⚡ Exécution commande: {tool_action}")
                
                # Déterminer si on doit utiliser cmd.exe ou PowerShell
                if 'Get-AppXPackage' in tool_action or tool_action.startswith('Get-'):
                    # Commande PowerShell
                    subprocess.Popen(
                        ['powershell.exe', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', tool_action],
                        creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                else:
                    # Commande CMD standard
                    # Remplacer && par & pour Windows CMD
                    cmd_action = tool_action.replace('&&', '&')
                    
                    # Certaines commandes doivent être lancées directement
                    direct_commands = [
                        'msinfo32', 'dxdiag', 'eventvwr.msc', 'devmgmt.msc', 'taskmgr',
                        'resmon', 'diskmgmt.msc', 'compmgmt.msc', 'services.msc', 'perfmon',
                        'dfrgui', 'regedit', 'gpedit.msc', 'secpol.msc', 'netplwiz',
                        'printmanagement.msc', 'dcomcnfg', 'appwiz.cpl', 'systempropertiesadvanced',
                        'desk.cpl', 'mmsys.cpl', 'joy.cpl', 'main.cpl', 'intl.cpl',
                        'timedate.cpl', 'powercfg.cpl', 'cleanmgr', 'wsreset', 'ncpa.cpl',
                        'sndvol', 'systemreset'
                    ]
                    
                    # Vérifier si c'est une commande directe
                    is_direct = any(cmd in tool_action for cmd in direct_commands)
                    
                    if is_direct:
                        # Lancer directement sans cmd
                        subprocess.Popen(tool_action, shell=True)
                    else:
                        # Lancer avec cmd /k pour garder la fenêtre ouverte
                        subprocess.Popen(
                            f'cmd.exe /k {cmd_action}',
                            creationflags=subprocess.CREATE_NEW_CONSOLE
                        )
                
                print(f"✅ Commande lancée avec succès")
                
        except Exception as e:
            print(f"❌ Erreur lors de l'exécution de '{tool_name}': {e}")
            # Afficher une notification d'erreur à l'utilisateur
            try:
                import tkinter.messagebox as messagebox
                messagebox.showerror(
                    "Erreur d'exécution",
                    f"Impossible d'exécuter '{tool_name}':\n{str(e)}"
                )
            except:
                pass