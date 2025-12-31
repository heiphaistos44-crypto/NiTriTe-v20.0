#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Applications Portables - NiTriTe V14
Téléchargement et gestion d'applications portables
"""

import customtkinter as ctk
import tkinter as tk
import requests
import zipfile
import shutil
import json
import time
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, ModernSearchBar, ModernStatsCard
from v14_mvp.logger_system import logger
from v14_mvp.category_icons import get_category_emoji


class PortableAppsPage(ctk.CTkFrame):
    """Page Applications Portables avec téléchargement 1-clic"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Dossier pour stocker apps portables (dans downloads/ portable)
        try:
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from portable_paths import get_portable_downloads_dir
            downloads_dir = get_portable_downloads_dir()
            self.portable_dir = downloads_dir / "PortableApps"
        except:
            # Fallback
            import sys
            if getattr(sys, 'frozen', False):
                app_dir = Path(sys.executable).parent
            else:
                app_dir = Path(__file__).parent.parent.parent
            self.portable_dir = app_dir / 'downloads' / 'PortableApps'

        self.portable_dir.mkdir(parents=True, exist_ok=True)
        
        # Base de données des applications portables
        self.portable_apps = self._get_portable_apps_database()
        
        self.filtered_apps = self.portable_apps.copy()
        self.downloading = set()  # Apps en cours de téléchargement
        
        self._create_header()
        self._create_stats()
        self._create_search()
        self._create_content()
    
    def _get_portable_apps_database(self):
        """Base de données des applications portables avec URLs de téléchargement"""
        # Charger depuis le fichier JSON
        json_path = Path(__file__).parent.parent.parent / "data" / "portable_apps.json"

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # Transformer la structure JSON en format attendu par le code
            portable_apps = {}

            for category_name, apps_dict in json_data.items():
                # Stocker le nom original de la catégorie et l'emoji séparément
                # On n'ajoute PAS l'emoji au nom, il sera géré par l'icône colorée

                # Créer la liste d'applications pour cette catégorie
                apps_list = []
                for app_name, app_info in apps_dict.items():
                    apps_list.append({
                        "name": app_name,
                        "description": app_info.get("description", ""),
                        "url": app_info.get("url", ""),
                        "size": app_info.get("size", ""),
                        "installed": False
                    })

                # Utiliser le nom SANS emoji comme clé
                portable_apps[category_name] = apps_list

            return portable_apps

        except Exception as e:
            print(f" Erreur chargement portable_apps.json: {e}")
            # Fallback: retourner une base minimale
            return {
                " Outils Système": [
                    {
                        "name": "7-Zip Portable",
                        "description": "Archiveur puissant - Format 7z, ZIP, RAR",
                        "url": "https://www.7-zip.org/a/7z2301-x64.exe",
                        "size": "1.5 MB",
                        "installed": False
                    }
                ]
            }
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        left_side = ctk.CTkFrame(container, fg_color="transparent")
        left_side.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        title = ctk.CTkLabel(
            left_side,
            text="💾 Applications Portables",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            left_side,
            text="Téléchargement et gestion en 1 clic",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)
        
        # Bouton ouvrir dossier
        ModernButton(
            container,
            text=" Ouvrir Dossier",
            variant="outlined",
            command=self._open_portable_folder
        ).pack(side=tk.RIGHT)
    
    def _create_stats(self):
        """Stats"""
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Compter total apps
        total = sum(len(apps) for apps in self.portable_apps.values())

        self.stats_total = ModernStatsCard(
            stats_frame,
            "📦 Disponibles",
            total,
            "",
            DesignTokens.INFO
        )
        self.stats_total.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.stats_installed = ModernStatsCard(
            stats_frame,
            "✅ Installées",
            0,
            "",
            DesignTokens.SUCCESS
        )
        self.stats_installed.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.stats_downloading = ModernStatsCard(
            stats_frame,
            "Téléchargements",
            0,
            "",
            DesignTokens.WARNING
        )
        self.stats_downloading.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    def _create_search(self):
        """Barre de recherche"""
        total = sum(len(apps) for apps in self.portable_apps.values())
        search = ModernSearchBar(
            self,
            placeholder=f"Rechercher dans {total} apps portables • {len(self.portable_apps)} catégories",
            on_search=self._on_search
        )
        search.pack(fill=tk.X, padx=20, pady=10)
    
    def _create_content(self):
        """Contenu avec catégories"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.content_container = scroll
        self._update_display()
    
    def _update_display(self):
        """Mettre à jour l'affichage"""
        # Clear
        for widget in self.content_container.winfo_children():
            widget.destroy()
        
        # Afficher chaque catégorie
        for category_name in sorted(self.filtered_apps.keys()):
            apps = self.filtered_apps[category_name]
            
            if not apps:
                continue
            
            self._create_category_section(category_name, apps)
    
    def _create_category_section(self, category_name, apps):
        """Créer section de catégorie repliable avec icône colorée"""
        card = ModernCard(self.content_container)
        card.pack(fill=tk.X, pady=5)

        # Container pour apps (caché par défaut)
        apps_container = ctk.CTkFrame(card, fg_color="transparent")
        apps_container.pack_forget()

        # État
        category_state = {
            'container': apps_container,
            'visible': False,
            'apps': apps
        }

        # Header cliquable avec icône colorée
        emoji = get_category_emoji(category_name)

        # Frame cliquable pour le header
        header_frame = ctk.CTkFrame(
            card,
            fg_color="transparent",
            corner_radius=0,
            height=50
        )
        header_frame.pack(fill=tk.X, padx=10, pady=5)

        # Rendre le frame cliquable
        header_frame.bind("<Button-1>", lambda e: self._toggle_category(card, category_state, category_name))

        # Container horizontal pour icône + texte
        content_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        content_frame.bind("<Button-1>", lambda e: self._toggle_category(card, category_state, category_name))

        # Icône colorée
        try:
            from v14_mvp.icons_system import ColoredIconsManager
            icon_image = ColoredIconsManager.create_colored_icon(emoji, size=24)
            icon_label = ctk.CTkLabel(
                content_frame,
                image=icon_image,
                text=""
            )
            icon_label.image = icon_image
            icon_label.pack(side=tk.LEFT, padx=(0, 10))
            icon_label.bind("<Button-1>", lambda e: self._toggle_category(card, category_state, category_name))
        except Exception as e:
            print(f"ERREUR icone coloree pour {category_name}: {e}")
            import traceback
            traceback.print_exc()

        # Texte du header (sans emoji car déjà dans l'icône colorée)
        header_text = ctk.CTkLabel(
            content_frame,
            text=f"{category_name} ({len(apps)} applications) ▶",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY,
            anchor="w"
        )
        header_text.pack(side=tk.LEFT, fill=tk.X, expand=True)
        header_text.bind("<Button-1>", lambda e: self._toggle_category(card, category_state, category_name))

        # Stocker pour mise à jour
        category_state['header_frame'] = header_frame
        category_state['header_text'] = header_text
        category_state['emoji'] = emoji
    
    def _toggle_category(self, card, category_state, category_name):
        """Basculer affichage catégorie"""
        if category_state['visible']:
            # Cacher
            category_state['container'].pack_forget()
            category_state['visible'] = False
            category_state['header_text'].configure(text=f"{category_name} ({len(category_state['apps'])} applications) ▶")
        else:
            # Afficher
            # Clear
            for widget in category_state['container'].winfo_children():
                widget.destroy()

            # Créer grille
            for app in category_state['apps']:
                self._create_app_card(category_state['container'], app)

            category_state['container'].pack(fill=tk.X, padx=10, pady=(0, 10))
            category_state['visible'] = True
            category_state['header_text'].configure(text=f"{category_name} ({len(category_state['apps'])} applications) ▼")
    
    def _create_app_card(self, parent, app):
        """Créer carte d'application"""
        frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        frame.pack(fill=tk.X, pady=5)
        
        container = ctk.CTkFrame(frame, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=12)
        
        # Info gauche
        left = ctk.CTkFrame(container, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        name_label = ctk.CTkLabel(
            left,
            text=app['name'],
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        desc_label = ctk.CTkLabel(
            left,
            text=app['description'],
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc_label.pack(anchor="w", pady=(2, 0))
        
        size_label = ctk.CTkLabel(
            left,
            text=f" {app['size']}",
            font=(DesignTokens.FONT_FAMILY, 10),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        size_label.pack(anchor="w", pady=(2, 0))
        
        # Boutons à droite
        buttons = ctk.CTkFrame(container, fg_color="transparent")
        buttons.pack(side=tk.RIGHT)
        
        # Vérifier si installée
        app_folder = self.portable_dir / app['name'].replace(" ", "_")
        is_installed = app_folder.exists()
        
        if is_installed:
            # Bouton lancer
            ModernButton(
                buttons,
                text=" Lancer",
                variant="filled",
                size="sm",
                command=lambda: self._launch_app(app)
            ).pack(side=tk.LEFT, padx=3)
            
            # Bouton désinstaller
            ModernButton(
                buttons,
                text="",
                variant="text",
                size="sm",
                command=lambda: self._uninstall_app(app, frame)
            ).pack(side=tk.LEFT, padx=3)
        else:
            # Bouton télécharger
            ModernButton(
                buttons,
                text=" Télécharger",
                variant="filled",
                size="sm",
                command=lambda: self._download_app(app, frame)
            ).pack(side=tk.LEFT, padx=3)
    
    def _download_app(self, app, frame):
        """Télécharger et installer une application portable"""
        print(f" Téléchargement de {app['name']}...")
        print(f"   URL: {app['url']}")
        print(f"   Destination: {self.portable_dir}")

        # Si c'est un redirect, ouvrir dans le navigateur
        if app.get('type') == 'redirect':
            import webbrowser
            print(f" Ouverture du lien de téléchargement dans le navigateur...")
            webbrowser.open(app['url'])
            from tkinter import messagebox
            messagebox.showinfo(
                "Téléchargement manuel",
                f"{app['name']}\n\nLe lien de téléchargement s'ouvre dans votre navigateur.\n\nAprès téléchargement, copiez le fichier dans:\n{self.portable_dir / app['name'].replace(' ', '_')}"
            )
            return

        # Marquer comme en cours de téléchargement
        self.downloading.add(app['name'])
        self.stats_downloading.update_value(len(self.downloading))
        
        # Créer fenêtre de progression
        download_window = ctk.CTkToplevel(self)
        download_window.title(f"Téléchargement - {app['name']}")
        download_window.geometry("500x200")
        download_window.resizable(False, False)
        
        # Centrer
        download_window.update_idletasks()
        x = (download_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (download_window.winfo_screenheight() // 2) - (200 // 2)
        download_window.geometry(f"500x200+{x}+{y}")
        
        # Contenu
        content = ctk.CTkFrame(download_window, fg_color="transparent")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title = ctk.CTkLabel(
            content,
            text=f" Téléchargement de {app['name']}",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=10)
        
        status_label = ctk.CTkLabel(
            content,
            text="Préparation...",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        status_label.pack(pady=10)
        
        progress = ctk.CTkProgressBar(
            content,
            width=400,
            height=20,
            corner_radius=10
        )
        progress.pack(pady=10)
        progress.set(0)
        
        # Téléchargement réel de l'application
        def install_app():
            try:
                # Créer dossier
                app_folder = self.portable_dir / app['name'].replace(" ", "_")
                app_folder.mkdir(parents=True, exist_ok=True)

                status_label.configure(text="Téléchargement...")
                progress.set(0.1)
                download_window.update()

                logger.info("PortableApps", f"Début téléchargement: {app['name']}", url=app['url'])

                # Télécharger le fichier avec headers pour éviter les blocages
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                response = requests.get(app['url'], stream=True, timeout=60, headers=headers, allow_redirects=True)
                response.raise_for_status()

                # Déterminer le nom du fichier depuis l'URL ou l'en-tête Content-Disposition
                file_extension = app.get('type', 'exe')

                # Essayer de détecter l'extension depuis l'URL finale après redirections
                final_url = response.url
                if final_url.endswith('.zip'):
                    file_extension = 'zip'
                elif final_url.endswith('.exe'):
                    file_extension = 'exe'
                elif final_url.endswith('.7z'):
                    file_extension = '7z'

                temp_file = app_folder / f"download.{file_extension}"

                print(f" URL finale: {final_url}")
                print(f" Type de fichier: {file_extension}")

                # Télécharger avec barre de progression
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0

                with open(temp_file, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                percent = (downloaded / total_size) * 0.7  # 70% pour le téléchargement
                                progress.set(0.1 + percent)
                                status_label.configure(text=f"Téléchargement... {int((downloaded/total_size)*100)}%")
                                download_window.update()

                progress.set(0.8)
                status_label.configure(text="Extraction...")
                download_window.update()

                # Extraction selon le type
                if file_extension == 'zip':
                    import zipfile
                    try:
                        with zipfile.ZipFile(temp_file, 'r') as zip_ref:
                            zip_ref.extractall(app_folder)
                        temp_file.unlink()  # Supprimer le zip
                        print(f" Archive ZIP extraite avec succès")
                    except zipfile.BadZipFile:
                        print(f" Erreur: Le fichier n'est pas un ZIP valide")
                        status_label.configure(text=" Erreur: Fichier ZIP invalide")
                        progress.set(0)
                        return
                elif file_extension == '7z':
                    # Pour les fichiers .7z, on garde le fichier tel quel
                    # L'utilisateur devra l'extraire manuellement avec 7-Zip
                    print(f" Fichier .7z détecté - extraction manuelle requise")
                    final_7z = app_folder / f"{app['name'].replace(' ', '_')}.7z"
                    if temp_file != final_7z:
                        temp_file.rename(final_7z)
                elif file_extension == 'exe':
                    # Renommer l'exe
                    final_exe = app_folder / f"{app['name'].replace(' ', '_')}.exe"
                    if temp_file != final_exe:
                        temp_file.rename(final_exe)
                    print(f" Exécutable sauvegardé: {final_exe.name}")

                progress.set(0.9)
                status_label.configure(text="Création du lanceur...")
                download_window.update()

                # Créer README
                readme = app_folder / "README.txt"
                readme.write_text(
                    f"{app['name']}\n{'='*50}\n\n"
                    f"Description: {app['description']}\n"
                    f"Taille: {app['size']}\n"
                    f"Installé le: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
                    f"Source: {app['url']}\n\n"
                    f"Dossier: {app_folder}",
                    encoding='utf-8'
                )

                progress.set(1.0)
                status_label.configure(text=" Terminé!")
                logger.success("PortableApps", f"{app['name']} installé avec succès")

            except requests.exceptions.RequestException as e:
                error_msg = str(e)
                if "ConnectionError" in error_msg or "timeout" in error_msg.lower():
                    error_msg = "Impossible de se connecter au serveur"
                elif "404" in error_msg:
                    error_msg = "Fichier non trouvé (404)"
                elif "403" in error_msg:
                    error_msg = "Accès refusé (403)"

                logger.error("PortableApps", f"Erreur téléchargement {app['name']}: {error_msg}", url=app['url'])

                def show_error():
                    status_label.configure(text=f" Erreur: {error_msg[:50]}")
                    progress.set(0)

                    # Afficher un message d'aide
                    help_label = ctk.CTkLabel(
                        content,
                        text="Vérifiez votre connexion Internet ou essayez plus tard.",
                        font=(DesignTokens.FONT_FAMILY, 10),
                        text_color=DesignTokens.TEXT_SECONDARY
                    )
                    help_label.pack(pady=5)

                download_window.after(0, show_error)
                return
            except Exception as e:
                logger.log_exception("PortableApps", e, f"Installation de {app['name']}")

                def show_error():
                    status_label.configure(text=f" Erreur: {str(e)[:50]}")
                    progress.set(0)

                download_window.after(0, show_error)
                return
            
            # Update stats
            self.downloading.discard(app['name'])
            self.stats_downloading.update_value(len(self.downloading))
            
            installed_count = sum(
                1 for category in self.portable_apps.values()
                for a in category
                if (self.portable_dir / a['name'].replace(" ", "_")).exists()
            )
            self.stats_installed.update_value(installed_count)
            
            # Fermer fenêtre
            download_window.after(1000, download_window.destroy)
            
            # Recréer la carte
            for widget in frame.winfo_children():
                widget.destroy()
            
            self._create_app_card(frame.master, app)
            frame.destroy()
            
            print(f" {app['name']} installé: {app_folder}")
        
        # Lancer installation
        download_window.after(100, install_app)
    
    def _launch_app(self, app):
        """Lancer une application portable"""
        app_folder = self.portable_dir / app['name'].replace(" ", "_")
        
        print(f" Lancement de {app['name']}")
        print(f" Dossier: {app_folder}")
        
        import subprocess
        
        # Vérifier si le dossier existe et contient des fichiers
        if not app_folder.exists():
            print(f" Dossier n'existe pas: {app_folder}")
            return
        
        # Lister le contenu du dossier
        files = list(app_folder.iterdir())
        print(f" Fichiers trouvés: {len(files)}")
        for f in files:
            print(f"   • {f.name}")
        
        # Chercher un exécutable (récursif pour chercher dans les sous-dossiers)
        exe_files = list(app_folder.glob("*.exe"))

        # Si pas trouvé, chercher récursivement
        if not exe_files:
            exe_files = list(app_folder.glob("**/*.exe"))
            # Exclure les uninstaller
            exe_files = [f for f in exe_files if "unins" not in f.name.lower() and "uninst" not in f.name.lower()]

        if exe_files:
            # Prioriser les .exe portables (paf.exe, portable.exe, etc.)
            portable_exe = [f for f in exe_files if "portable" in f.name.lower() or "paf" in f.name.lower()]
            main_exe = portable_exe[0] if portable_exe else exe_files[0]

            print(f" Lancement de: {main_exe.name}")
            try:
                subprocess.Popen([str(main_exe)], cwd=str(main_exe.parent))
            except Exception as e:
                print(f" Erreur lancement: {e}")
                from tkinter import messagebox
                messagebox.showerror("Erreur", f"Impossible de lancer {app['name']}:\n{str(e)}")
        else:
            # Si pas d'exe, chercher LANCER.bat
            launcher = app_folder / "LANCER.bat"
            if launcher.exists():
                print(f" Lancement du script: LANCER.bat")
                try:
                    subprocess.Popen(['cmd.exe', '/c', str(launcher)], cwd=str(app_folder), shell=False)
                except Exception as e:
                    print(f" Erreur script: {e}")
            else:
                # Ouvrir le dossier
                print(f" Ouverture du dossier")
                try:
                    subprocess.Popen(['explorer', str(app_folder)])
                except Exception as e:
                    print(f" Erreur ouverture: {e}")
    
    def _uninstall_app(self, app, frame):
        """Désinstaller une application portable"""
        app_folder = self.portable_dir / app['name'].replace(" ", "_")
        
        try:
            if app_folder.exists():
                shutil.rmtree(app_folder)
                print(f" {app['name']} désinstallé")
                
                # Update stats
                installed_count = sum(
                    1 for category in self.portable_apps.values()
                    for app in category
                    if (self.portable_dir / app['name'].replace(" ", "_")).exists()
                )
                self.stats_installed.update_value(installed_count)
                
                # Recréer la carte
                for widget in frame.winfo_children():
                    widget.destroy()
                
                self._create_app_card(frame.master, app)
                frame.destroy()
        except Exception as e:
            print(f" Erreur désinstallation: {e}")
    
    def _open_portable_folder(self):
        """Ouvrir dossier des portables"""
        import subprocess
        try:
            subprocess.Popen(f'explorer "{self.portable_dir}"')
            print(f" Ouverture de {self.portable_dir}")
        except Exception as e:
            print(f" Erreur: {e}")
    
    def _on_search(self, query):
        """Recherche dans les apps portables"""
        query = query.lower().strip()
        
        if not query:
            self.filtered_apps = self.portable_apps.copy()
        else:
            self.filtered_apps = {}
            for category, apps in self.portable_apps.items():
                filtered = [
                    app for app in apps
                    if query in app['name'].lower() or query in app['description'].lower()
                ]
                if filtered:
                    self.filtered_apps[category] = filtered
        
        self._update_display()