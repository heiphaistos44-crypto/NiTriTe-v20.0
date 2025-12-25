#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pages Complètes CORRIGÉES - NiTriTe V17
Updates, Backup, Diagnostic, Optimizations avec vraies commandes
"""

import customtkinter as ctk
import tkinter as tk
import subprocess
import platform
import os
import sys
import json
import shutil
import threading
import ctypes
from datetime import datetime
from pathlib import Path
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, ModernStatsCard

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
    print("⚠️ psutil non disponible - installation: pip install psutil")


def get_local_software_folder():
    """Obtenir le dossier 'logiciel' à côté de l'exécutable ou à la racine du projet"""
    if getattr(sys, 'frozen', False):
        # Version compilée (PyInstaller) - chercher à côté de l'exe
        base_dir = os.path.dirname(sys.executable)
    else:
        # Mode développement - chercher depuis le script actuel
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. D'abord, chercher à côté de l'exécutable (pour version portable distribuée)
    logiciel_dir = os.path.join(base_dir, "logiciel")
    if os.path.exists(logiciel_dir):
        return logiciel_dir

    # 2. Si pas trouvé, chercher en remontant dans l'arborescence (pour développement)
    current_dir = base_dir
    for _ in range(3):  # Remonter jusqu'à 3 niveaux maximum
        logiciel_dir = os.path.join(current_dir, "logiciel")
        if os.path.exists(logiciel_dir):
            return logiciel_dir
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Racine atteinte
            break
        current_dir = parent_dir

    # 3. Si toujours pas trouvé, chercher la racine du projet (présence de src/)
    project_root = base_dir
    while True:
        parent = os.path.dirname(project_root)
        if parent == project_root:  # Racine du système atteinte
            break
        # Vérifier si on est à la racine du projet (présence de src/)
        if os.path.exists(os.path.join(project_root, "src")):
            logiciel_dir = os.path.join(project_root, "logiciel")
            if os.path.exists(logiciel_dir):
                return logiciel_dir
            break
        project_root = parent

    # 4. Fallback: créer à côté de l'exécutable
    logiciel_dir = os.path.join(base_dir, "logiciel")
    os.makedirs(logiciel_dir, exist_ok=True)
    return logiciel_dir


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


class UpdatesPage(ctk.CTkFrame):
    """Page Mises à jour avec vraies commandes WinGet"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)
        
        self._create_header()
        self._create_terminal()
        self._create_content()
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="🔄 Mises à Jour",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        # Actions
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)
        
        ModernButton(
            actions,
            text="🔍 Rechercher",
            variant="filled",
            command=self._check_updates
        ).pack(side=tk.LEFT, padx=5)
        
        ModernButton(
            actions,
            text="⬇️ Tout Mettre à Jour",
            variant="outlined",
            command=self._update_all
        ).pack(side=tk.LEFT, padx=5)
    
    def _create_terminal(self):
        """Terminal intégré"""
        terminal_card = ModernCard(self)
        terminal_card.pack(fill=tk.X, padx=20, pady=10)
        
        term_title = ctk.CTkLabel(
            terminal_card,
            text="💻 Terminal",
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        term_title.pack(fill=tk.X, padx=20, pady=(15, 5))
        
        # Zone de sortie
        self.terminal_output = ctk.CTkTextbox(
            terminal_card,
            height=150,
            font=("Consolas", 10),
            fg_color="#1E1E1E",
            text_color="#D4D4D4",
            wrap="word"
        )
        self.terminal_output.pack(fill=tk.X, padx=20, pady=(0, 15))
        self.terminal_output.insert("1.0", "🔄 Terminal prêt. Cliquez sur un bouton pour exécuter une commande.\n")
        self.terminal_output.configure(state="disabled")
    
    def _log_to_terminal(self, message):
        """Ajouter message au terminal"""
        self.terminal_output.configure(state="normal")
        self.terminal_output.insert("end", f"{message}\n")
        self.terminal_output.see("end")
        self.terminal_output.configure(state="disabled")
    
    def _create_content(self):
        """Contenu"""
        # Créer un frame scrollable principal pour tout le contenu
        self.main_scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        self.main_scroll.pack(fill=tk.BOTH, expand=True)

        # Stats
        stats_frame = ctk.CTkFrame(self.main_scroll, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.stats_installed = ModernStatsCard(
            stats_frame,
            "Installées",
            "...",
            "📦",
            DesignTokens.INFO
        )
        self.stats_installed.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.stats_uptodate = ModernStatsCard(
            stats_frame,
            "À jour",
            "...",
            "✅",
            DesignTokens.SUCCESS
        )
        self.stats_uptodate.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.stats_updates = ModernStatsCard(
            stats_frame,
            "Mises à jour",
            "...",
            "🔄",
            DesignTokens.WARNING
        )
        self.stats_updates.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Liste mises à jour
        card = ModernCard(self.main_scroll)
        card.pack(fill=tk.X, padx=20, pady=10)
        
        header = ctk.CTkLabel(
            card,
            text="📋 Mises à jour disponibles",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        header.pack(fill=tk.X, padx=20, pady=15)
        
        self.updates_scroll = ctk.CTkScrollableFrame(card, fg_color="transparent")
        self.updates_scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        # Message initial
        initial_msg = ctk.CTkLabel(
            self.updates_scroll,
            text="Cliquez sur '🔍 Rechercher' pour scanner les mises à jour disponibles",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        initial_msg.pack(pady=20)

        # Section Gestionnaires de paquets
        self._create_package_managers_section()

        # Section Outils constructeurs
        self._create_manufacturer_tools_section()

        # Section Snappy Driver Installer
        self._create_snappy_section()

    def _create_package_managers_section(self):
        """Section gestionnaires de paquets"""
        card = ModernCard(self.main_scroll)
        card.pack(fill=tk.X, padx=20, pady=10)

        title = ctk.CTkLabel(
            card,
            text="📦 Gestionnaires de Paquets",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Grid layout pour les gestionnaires de paquets
        pm_grid = ctk.CTkFrame(content, fg_color="transparent")
        pm_grid.pack(fill=tk.X)

        # Row 1: WinGet et Chocolatey
        row1 = ctk.CTkFrame(pm_grid, fg_color="transparent")
        row1.pack(fill=tk.X, pady=5)

        ModernButton(
            row1,
            text="📦 WinGet (Scan + Update)",
            variant="outlined",
            command=self._update_winget
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row1,
            text="🍫 Chocolatey (Auto-install + Update)",
            variant="outlined",
            command=self._update_chocolatey
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Row 2: Scoop et pip
        row2 = ctk.CTkFrame(pm_grid, fg_color="transparent")
        row2.pack(fill=tk.X, pady=5)

        ModernButton(
            row2,
            text="🪣 Scoop (Auto-install + Update)",
            variant="outlined",
            command=self._update_scoop
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row2,
            text="🐍 pip (Python packages)",
            variant="outlined",
            command=self._update_pip
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Row 3: npm
        row3 = ctk.CTkFrame(pm_grid, fg_color="transparent")
        row3.pack(fill=tk.X, pady=5)

        ModernButton(
            row3,
            text="📦 npm (Node.js packages)",
            variant="outlined",
            command=self._update_npm
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _create_manufacturer_tools_section(self):
        """Section outils constructeurs"""
        card = ModernCard(self.main_scroll)
        card.pack(fill=tk.X, padx=20, pady=10)

        title = ctk.CTkLabel(
            card,
            text="🏭 Outils de Mise à Jour Constructeurs",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Grille de boutons
        button_grid = ctk.CTkFrame(content, fg_color="transparent")
        button_grid.pack(fill=tk.X)

        manufacturers = [
            ("💻 Dell SupportAssist", "https://www.dell.com/support/home/"),
            ("🖥️ HP Support Assistant", "https://support.hp.com/drivers"),
            ("🔧 Lenovo Vantage", "https://support.lenovo.com/solutions/ht505081"),
            ("⚡ Intel Driver Assistant", "https://www.intel.com/content/www/us/en/support/detect.html"),
            ("🎮 NVIDIA GeForce Experience", "https://www.nvidia.com/geforce/geforce-experience/"),
            ("🔴 AMD Software Adrenalin", "https://www.amd.com/support"),
            ("🏆 ASUS MyASUS", "https://www.asus.com/support/download-center/"),
            ("🐉 MSI Center", "https://www.msi.com/Landing/msi-center"),
            ("🌟 Acer Care Center", "https://www.acer.com/ac/en/US/content/software-download"),
        ]

        row = 0
        col = 0
        for text, url in manufacturers:
            btn = ModernButton(
                button_grid,
                text=text,
                variant="outlined",
                command=lambda u=url: self._open_url(u)
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col > 2:  # 3 colonnes
                col = 0
                row += 1

        # Configure colonnes pour expansion égale
        for i in range(3):
            button_grid.grid_columnconfigure(i, weight=1, uniform="manufacturer")

    def _create_snappy_section(self):
        """Section Snappy Driver Installer"""
        card = ModernCard(self.main_scroll)
        card.pack(fill=tk.X, padx=20, pady=10)

        title = ctk.CTkLabel(
            card,
            text="🚗 Snappy Driver Installer",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Téléchargez Snappy Driver Installer pour mettre à jour automatiquement tous vos drivers.\n"
                 "Version Full (~40 GB) : Tous les drivers | Version Lite (~2 GB) : Télécharge à la demande",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w",
            wraplength=800,
            justify="left"
        )
        desc.pack(fill=tk.X, pady=(0, 10))

        # Boutons
        btn_frame = ctk.CTkFrame(content, fg_color="transparent")
        btn_frame.pack(fill=tk.X)

        ModernButton(
            btn_frame,
            text="💾 Télécharger Snappy Full (~40 GB)",
            variant="filled",
            command=self._download_snappy_full
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            btn_frame,
            text="📦 Télécharger Snappy Lite (~2 GB)",
            variant="outlined",
            command=self._download_snappy_lite
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _update_chocolatey(self):
        """Mettre à jour via Chocolatey (auto-install si nécessaire)"""
        self._log_to_terminal("🍫 Vérification de Chocolatey...")

        def run_choco_update():
            try:
                # Vérifier si Chocolatey est installé
                check_result = subprocess.run(
                    ["choco", "--version"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    shell=True
                )

                if check_result.returncode != 0:
                    # Chocolatey n'est pas installé, l'installer
                    self._log_to_terminal("❌ Chocolatey n'est pas installé")
                    self._log_to_terminal("📥 Installation automatique de Chocolatey...")

                    from tkinter import messagebox
                    response = messagebox.askyesno(
                        "Installer Chocolatey?",
                        "Chocolatey n'est pas installé.\n\n"
                        "Voulez-vous l'installer automatiquement?\n"
                        "(Une fenêtre PowerShell admin va s'ouvrir)"
                    )

                    if not response:
                        self._log_to_terminal("❌ Installation annulée par l'utilisateur")
                        return

                    # Script d'installation Chocolatey
                    install_cmd = (
                        'Set-ExecutionPolicy Bypass -Scope Process -Force; '
                        '[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; '
                        'iex ((New-Object System.Net.WebClient).DownloadString(\'https://community.chocolatey.org/install.ps1\')); '
                        'Write-Host ""; '
                        'Write-Host "Installation terminee! Appuyez sur Entree pour fermer..." -ForegroundColor Green; '
                        'Read-Host'
                    )

                    subprocess.Popen(
                        f'powershell -NoExit -Command "Start-Process powershell -Verb RunAs -ArgumentList \'-NoExit\',\'-Command\',\'{install_cmd}\'"',
                        shell=True
                    )

                    self._log_to_terminal("✅ Installation lancée! Patientez...")
                    self._log_to_terminal("💡 Après installation, re-cliquez sur le bouton pour mettre à jour")
                    return

                self._log_to_terminal("✅ Chocolatey détecté")
                self._log_to_terminal("🔄 Mise à jour de tous les packages...")

                # Lancer mise à jour dans PowerShell visible
                subprocess.Popen(
                    'powershell -NoExit -Command "Write-Host \'Mise a jour via Chocolatey...\' -ForegroundColor Cyan; '
                    'choco upgrade all -y; '
                    'Write-Host \'\'; '
                    'Write-Host \'Termine! Appuyez sur Entree pour fermer...\' -ForegroundColor Green; '
                    'Read-Host"',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    shell=True
                )

                self._log_to_terminal("✅ Mise à jour Chocolatey lancée dans PowerShell")

            except FileNotFoundError as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")
            except Exception as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_choco_update, daemon=True).start()

    def _open_url(self, url):
        """Ouvrir une URL dans le navigateur"""
        import webbrowser
        try:
            webbrowser.open(url)
            self._log_to_terminal(f"✅ Ouverture de {url}")
        except Exception as e:
            self._log_to_terminal(f"❌ Erreur: {e}")

    def _update_winget(self):
        """Scanner et mettre à jour via WinGet dans PowerShell visible"""
        self._log_to_terminal("📦 Scan des mises à jour WinGet...")

        def run_winget_update():
            try:
                # Lancer dans PowerShell visible pour voir toutes les mises à jour
                subprocess.Popen(
                    'powershell -NoExit -Command "Write-Host \'Scan des mises a jour disponibles...\' -ForegroundColor Cyan; '
                    'Write-Host \'\'; '
                    'winget upgrade; '
                    'Write-Host \'\'; '
                    'Write-Host \'Voulez-vous tout mettre a jour? (y/n)\' -ForegroundColor Yellow; '
                    '$response = Read-Host; '
                    'if ($response -eq \'y\' -or $response -eq \'Y\') { '
                    '    Write-Host \'Mise a jour en cours...\' -ForegroundColor Cyan; '
                    '    winget upgrade --all --accept-source-agreements --accept-package-agreements; '
                    '    Write-Host \'\'; '
                    '    Write-Host \'Termine!\' -ForegroundColor Green '
                    '} else { '
                    '    Write-Host \'Annule.\' -ForegroundColor Yellow '
                    '}; '
                    'Write-Host \'\'; '
                    'Write-Host \'Appuyez sur Entree pour fermer...\' -ForegroundColor Gray; '
                    'Read-Host"',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    shell=True
                )
                self._log_to_terminal("✅ Scan WinGet lancé dans PowerShell")
                self._log_to_terminal("💡 Vous pouvez voir toutes les mises à jour dans la fenêtre PowerShell")
            except Exception as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_winget_update, daemon=True).start()

    def _update_scoop(self):
        """Mettre à jour via Scoop (auto-install si nécessaire)"""
        self._log_to_terminal("🪣 Vérification de Scoop...")

        def run_scoop_update():
            try:
                # Vérifier si Scoop est installé
                check_result = subprocess.run(
                    "scoop --version",
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW,
                    shell=True
                )

                if check_result.returncode != 0:
                    # Scoop n'est pas installé
                    self._log_to_terminal("❌ Scoop n'est pas installé")
                    self._log_to_terminal("📥 Installation automatique de Scoop...")

                    from tkinter import messagebox
                    response = messagebox.askyesno(
                        "Installer Scoop?",
                        "Scoop n'est pas installé.\n\n"
                        "Voulez-vous l'installer automatiquement?\n"
                        "(Une fenêtre PowerShell va s'ouvrir)"
                    )

                    if not response:
                        self._log_to_terminal("❌ Installation annulée")
                        return

                    # Installation Scoop
                    subprocess.Popen(
                        'powershell -NoExit -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force; '
                        'irm get.scoop.sh | iex; '
                        'Write-Host \'\'; '
                        'Write-Host \'Installation terminee!\' -ForegroundColor Green; '
                        'Write-Host \'Appuyez sur Entree pour fermer...\' -ForegroundColor Gray; '
                        'Read-Host"',
                        creationflags=subprocess.CREATE_NEW_CONSOLE,
                        shell=True
                    )

                    self._log_to_terminal("✅ Installation Scoop lancée")
                    self._log_to_terminal("💡 Après installation, re-cliquez pour mettre à jour")
                    return

                self._log_to_terminal("✅ Scoop détecté")
                self._log_to_terminal("🔄 Mise à jour Scoop + packages...")

                # Mise à jour Scoop et packages
                subprocess.Popen(
                    'powershell -NoExit -Command "Write-Host \'Mise a jour Scoop...\' -ForegroundColor Cyan; '
                    'scoop update; '
                    'Write-Host \'\'; '
                    'Write-Host \'Mise a jour des packages...\' -ForegroundColor Cyan; '
                    'scoop update *; '
                    'Write-Host \'\'; '
                    'Write-Host \'Termine!\' -ForegroundColor Green; '
                    'Write-Host \'Appuyez sur Entree pour fermer...\' -ForegroundColor Gray; '
                    'Read-Host"',
                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                    shell=True
                )

                self._log_to_terminal("✅ Mise à jour Scoop lancée")

            except FileNotFoundError as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")
            except Exception as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_scoop_update, daemon=True).start()

    def _update_pip(self):
        """Mettre à jour les packages Python via pip"""
        self._log_to_terminal("🐍 Vérification de pip...")

        def run_pip_update():
            try:
                # Vérifier si Python/pip est installé
                check_result = subprocess.run(
                    ["python", "-m", "pip", "--version"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )

                if check_result.returncode != 0:
                    self._log_to_terminal("❌ Python/pip n'est pas installé")
                    self._log_to_terminal("💡 Installez Python depuis https://www.python.org/")
                    return

                self._log_to_terminal("✅ pip détecté")
                self._log_to_terminal("🔄 Mise à jour des packages Python...")

                # Liste packages obsolètes et mise à jour
                subprocess.Popen(
                    ['powershell', '-NoExit', '-Command',
                     'Write-Host "Packages Python obsoletes..." -ForegroundColor Cyan; '
                     'python -m pip list --outdated; '
                     'Write-Host ""; '
                     'Write-Host "Mise a jour de pip..." -ForegroundColor Cyan; '
                     'python -m pip install --upgrade pip; '
                     'Write-Host ""; '
                     'Write-Host "Termine!" -ForegroundColor Green; '
                     'Write-Host "Pour mettre a jour un package: pip install --upgrade <package>" -ForegroundColor Yellow; '
                     'Write-Host "Appuyez sur Entree pour fermer..." -ForegroundColor Gray; '
                     'Read-Host'],
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )

                self._log_to_terminal("✅ Scan pip lancé")

            except FileNotFoundError:
                self._log_to_terminal("❌ Python n'est pas installé ou pas dans PATH")
            except Exception as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_pip_update, daemon=True).start()

    def _update_npm(self):
        """Mettre à jour les packages Node.js via npm"""
        self._log_to_terminal("📦 Vérification de npm...")

        def run_npm_update():
            try:
                # Vérifier si Node.js/npm est installé
                check_result = subprocess.run(
                    ["npm", "--version"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )

                if check_result.returncode != 0:
                    self._log_to_terminal("❌ Node.js/npm n'est pas installé")
                    self._log_to_terminal("💡 Installez Node.js depuis https://nodejs.org/")
                    return

                self._log_to_terminal("✅ npm détecté")
                self._log_to_terminal("🔄 Mise à jour packages Node.js...")

                # Liste et mise à jour packages globaux
                subprocess.Popen(
                    ['powershell', '-NoExit', '-Command',
                     'Write-Host "Packages npm globaux obsoletes..." -ForegroundColor Cyan; '
                     'npm outdated -g; '
                     'Write-Host ""; '
                     'Write-Host "Mise a jour de npm..." -ForegroundColor Cyan; '
                     'npm install -g npm; '
                     'Write-Host ""; '
                     'Write-Host "Mise a jour des packages globaux..." -ForegroundColor Cyan; '
                     'npm update -g; '
                     'Write-Host ""; '
                     'Write-Host "Termine!" -ForegroundColor Green; '
                     'Write-Host "Appuyez sur Entree pour fermer..." -ForegroundColor Gray; '
                     'Read-Host'],
                    creationflags=subprocess.CREATE_NEW_CONSOLE
                )

                self._log_to_terminal("✅ Mise à jour npm lancée")

            except FileNotFoundError:
                self._log_to_terminal("❌ Node.js/npm n'est pas installé ou pas dans PATH")
            except Exception as e:
                self._log_to_terminal(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_npm_update, daemon=True).start()

    def _download_snappy_full(self):
        """Télécharger Snappy Driver Installer Full"""
        import webbrowser
        from tkinter import messagebox

        self._log_to_terminal("💾 Ouverture page Snappy Full (~40 GB)...")

        response = messagebox.askyesno(
            "Snappy Driver Installer Full",
            "Vous allez télécharger Snappy Driver Installer Full (~40 GB).\n\n"
            "Cette version contient TOUS les drivers et ne nécessite pas de connexion Internet.\n\n"
            "⚠️ Le téléchargement est très volumineux!\n\n"
            "Continuer?"
        )

        if response:
            webbrowser.open("https://sdi-tool.org/download/")
            self._log_to_terminal("✅ Page de téléchargement Snappy Full ouverte")
            messagebox.showinfo(
                "Instructions",
                "Sur la page web:\n\n"
                "1. Cherchez 'Snappy Driver Installer Full'\n"
                "2. Téléchargez le fichier (~40 GB)\n"
                "3. Extrayez et lancez SDI.exe"
            )
        else:
            self._log_to_terminal("❌ Téléchargement annulé")

    def _download_snappy_lite(self):
        """Télécharger Snappy Driver Installer Lite"""
        import webbrowser
        from tkinter import messagebox

        self._log_to_terminal("📦 Ouverture page Snappy Lite (~2 GB)...")

        response = messagebox.askyesno(
            "Snappy Driver Installer Lite",
            "Vous allez télécharger Snappy Driver Installer Lite (~2 GB).\n\n"
            "Cette version télécharge les drivers à la demande (nécessite Internet).\n\n"
            "Continuer?"
        )

        if response:
            webbrowser.open("https://sdi-tool.org/download/")
            self._log_to_terminal("✅ Page de téléchargement Snappy Lite ouverte")
            messagebox.showinfo(
                "Instructions",
                "Sur la page web:\n\n"
                "1. Cherchez 'Snappy Driver Installer Lite'\n"
                "2. Téléchargez le fichier (~2 GB)\n"
                "3. Extrayez et lancez SDI.exe"
            )
        else:
            self._log_to_terminal("❌ Téléchargement annulé")

    def _check_updates(self):
        """Rechercher mises à jour avec WinGet ET Windows Update"""
        self._log_to_terminal("🔍 Recherche des mises à jour...")

        # Clear liste
        for widget in self.updates_scroll.winfo_children():
            widget.destroy()

        # Message de chargement
        loading_msg = ctk.CTkLabel(
            self.updates_scroll,
            text="⏳ Recherche en cours...\n\nVérification WinGet + Windows Update",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        loading_msg.pack(pady=20)

        # Lancer la recherche en arrière-plan pour éviter le freeze
        def search_updates():
            winget_count = 0
            windows_updates_count = 0

            # 1. Recherche WinGet
            winget_updates = []
            try:
                self._log_to_terminal("📦 Recherche mises à jour WinGet...")
                result = subprocess.run(
                    "winget upgrade",
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    timeout=30,
                    shell=True
                )

                if result.returncode == 0 or result.returncode == -1978335189:
                    output = result.stdout
                    lines = output.split('\n')
                    # Parser les vraies lignes de mises à jour (pas les headers)
                    in_table = False
                    for line in lines:
                        # Détecter le début du tableau de mises à jour
                        if 'Name' in line and 'Id' in line and 'Version' in line:
                            in_table = True
                            continue
                        # Détecter la ligne de séparation (-----)
                        if in_table and line.strip().startswith('---'):
                            continue
                        # Détecter la fin du tableau
                        if in_table and (line.strip() == '' or 'upgrades available' in line.lower()):
                            in_table = False
                            continue
                        # Parser les lignes de mises à jour
                        if in_table and line.strip() and not line.startswith('-'):
                            # Extraire les informations de la ligne
                            # Format typique: Nom    ID    Version    Disponible    Source
                            parts = line.split()
                            if len(parts) >= 4:
                                # Essayer d'extraire le nom, l'ID, la version actuelle et la version disponible
                                # La structure varie, mais généralement on a: Name, Id, Current, Available
                                winget_updates.append({
                                    'raw_line': line.strip(),
                                    'parts': parts
                                })
                                winget_count += 1

                    self._log_to_terminal(f"✅ WinGet: {winget_count} mises à jour trouvées")
                else:
                    self._log_to_terminal(f"⚠️ WinGet returncode: {result.returncode}")
                    if result.stderr:
                        self._log_to_terminal(f"⚠️ {result.stderr[:200]}")

            except FileNotFoundError:
                self._log_to_terminal("⚠️ WinGet non trouvé")
            except Exception as e:
                self._log_to_terminal(f"⚠️ Erreur WinGet: {str(e)[:100]}")

            # 2. Recherche Windows Update
            try:
                self._log_to_terminal("🪟 Recherche Windows Update...")
                # Utiliser COM pour accéder à Windows Update
                import win32com.client

                update_session = win32com.client.Dispatch("Microsoft.Update.Session")
                update_searcher = update_session.CreateUpdateSearcher()

                # Rechercher les mises à jour non installées
                search_result = update_searcher.Search("IsInstalled=0 and Type='Software'")

                windows_updates_count = search_result.Updates.Count
                self._log_to_terminal(f"✅ Windows Update: {windows_updates_count} mises à jour trouvées")

                # Afficher quelques détails
                if windows_updates_count > 0:
                    for i in range(min(3, windows_updates_count)):
                        update = search_result.Updates.Item(i)
                        self._log_to_terminal(f"   • {update.Title[:60]}")
                    if windows_updates_count > 3:
                        self._log_to_terminal(f"   ... et {windows_updates_count - 3} autres")

            except ImportError:
                self._log_to_terminal("⚠️ pywin32 non disponible (pip install pywin32)")
                windows_updates_count = -1
            except Exception as e:
                self._log_to_terminal(f"⚠️ Erreur Windows Update: {str(e)[:100]}")
                windows_updates_count = -1

            # Mettre à jour l'UI dans le thread principal
            def update_ui():
                # Clear
                for widget in self.updates_scroll.winfo_children():
                    widget.destroy()

                total_updates = winget_count
                if windows_updates_count >= 0:
                    total_updates += windows_updates_count

                # Update stats
                self.stats_updates.update_value(str(total_updates))

                # Afficher résumé
                if winget_count > 0 or windows_updates_count > 0:
                    # Section WinGet
                    if winget_count > 0:
                        winget_header_frame = ctk.CTkFrame(
                            self.updates_scroll,
                            fg_color=DesignTokens.BG_ELEVATED,
                            corner_radius=DesignTokens.RADIUS_MD
                        )
                        winget_header_frame.pack(fill=tk.X, pady=5, padx=10)

                        ctk.CTkLabel(
                            winget_header_frame,
                            text=f"📦 WinGet: {winget_count} mises à jour d'applications",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
                            text_color=DesignTokens.TEXT_PRIMARY,
                            anchor="w"
                        ).pack(padx=15, pady=10, anchor="w")

                        # Afficher les détails de chaque mise à jour
                        for update_info in winget_updates:
                            update_frame = ctk.CTkFrame(
                                self.updates_scroll,
                                fg_color=DesignTokens.BG_SECONDARY,
                                corner_radius=DesignTokens.RADIUS_SM
                            )
                            update_frame.pack(fill=tk.X, pady=2, padx=20)

                            # Afficher la ligne complète de winget
                            update_text = update_info['raw_line']
                            ctk.CTkLabel(
                                update_frame,
                                text=f"  {update_text}",
                                font=("Consolas", 10),
                                text_color=DesignTokens.TEXT_PRIMARY,
                                anchor="w"
                            ).pack(padx=10, pady=5, anchor="w")

                        # Bouton pour tout mettre à jour
                        action_frame = ctk.CTkFrame(
                            self.updates_scroll,
                            fg_color="transparent"
                        )
                        action_frame.pack(fill=tk.X, pady=5, padx=20)

                        ctk.CTkLabel(
                            action_frame,
                            text="Utilisez 'Tout Mettre à Jour' ou le bouton '📦 WinGet (Scan + Update)' pour installer",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                            text_color=DesignTokens.TEXT_SECONDARY,
                            anchor="w"
                        ).pack(padx=0, pady=5, anchor="w")

                    # Section Windows Update
                    if windows_updates_count > 0:
                        wu_frame = ctk.CTkFrame(
                            self.updates_scroll,
                            fg_color=DesignTokens.BG_ELEVATED,
                            corner_radius=DesignTokens.RADIUS_MD
                        )
                        wu_frame.pack(fill=tk.X, pady=5, padx=10)

                        ctk.CTkLabel(
                            wu_frame,
                            text=f"🪟 Windows Update: {windows_updates_count} mises à jour système",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
                            text_color=DesignTokens.TEXT_PRIMARY,
                            anchor="w"
                        ).pack(padx=15, pady=10, anchor="w")

                        ctk.CTkLabel(
                            wu_frame,
                            text="Ouvrez Windows Update dans les Paramètres pour installer",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                            text_color=DesignTokens.TEXT_SECONDARY,
                            anchor="w"
                        ).pack(padx=15, pady=(0, 5), anchor="w")

                        # Bouton pour ouvrir Windows Update
                        ModernButton(
                            wu_frame,
                            text="⚙️ Ouvrir Windows Update",
                            variant="outlined",
                            size="sm",
                            command=self._open_windows_update
                        ).pack(padx=15, pady=(0, 10), anchor="w")

                    elif windows_updates_count == -1:
                        # Erreur Windows Update
                        wu_frame = ctk.CTkFrame(
                            self.updates_scroll,
                            fg_color=DesignTokens.BG_ELEVATED,
                            corner_radius=DesignTokens.RADIUS_MD
                        )
                        wu_frame.pack(fill=tk.X, pady=5, padx=10)

                        ctk.CTkLabel(
                            wu_frame,
                            text="⚠️ Windows Update non disponible",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
                            text_color=DesignTokens.WARNING,
                            anchor="w"
                        ).pack(padx=15, pady=10, anchor="w")

                        ctk.CTkLabel(
                            wu_frame,
                            text="Installez pywin32: pip install pywin32",
                            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                            text_color=DesignTokens.TEXT_SECONDARY,
                            anchor="w"
                        ).pack(padx=15, pady=(0, 10), anchor="w")
                else:
                    # Aucune mise à jour
                    msg = ctk.CTkLabel(
                        self.updates_scroll,
                        text="✅ Aucune mise à jour disponible\n\nVotre système est à jour !",
                        font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                        text_color=DesignTokens.SUCCESS
                    )
                    msg.pack(pady=20)

                self._log_to_terminal(f"✅ Scan terminé: {total_updates} mises à jour au total")

            # Scheduler l'update UI dans le thread principal
            self.after(0, update_ui)

        # Lancer la recherche dans un thread
        threading.Thread(target=search_updates, daemon=True).start()

    def _open_windows_update(self):
        """Ouvrir Windows Update dans les Paramètres"""
        try:
            subprocess.Popen('start ms-settings:windowsupdate', shell=True)
            self._log_to_terminal("✅ Windows Update ouvert")
        except Exception as e:
            self._log_to_terminal(f"❌ Erreur: {e}")
    
    def _update_all(self):
        """Mettre à jour toutes les apps"""
        self._log_to_terminal("⬇️ Lancement mise à jour globale...")
        
        try:
            # Ouvrir PowerShell avec commande winget
            subprocess.Popen(
                'start powershell -Command "winget upgrade --all"',
                shell=True
            )
            self._log_to_terminal("✅ PowerShell lancé avec winget upgrade --all")
        except Exception as e:
            self._log_to_terminal(f"❌ Erreur: {e}")


class BackupPage(ctk.CTkFrame):
    """Page Sauvegarde avec vraies fonctions"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)
        
        self.backup_dir = Path.home() / "Documents" / "NiTriTe_Backups"
        self.backup_dir.mkdir(exist_ok=True)
        
        self._create_header()
        self._create_content()
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="💾 Sauvegarde",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        location = ctk.CTkLabel(
            container,
            text=f"📁 {self.backup_dir}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        location.pack(side=tk.RIGHT)
    
    def _create_content(self):
        """Contenu"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self._create_backup_section(scroll)
        self._create_restore_section(scroll)
        self._create_backups_list_section(scroll)
    
    def _create_backup_section(self, parent):
        """Section création sauvegarde"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="📦 Créer une Sauvegarde",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        # Options
        self.backup_options = {}
        options = [
            ("apps", "💾 Liste des applications installées", True),
            ("drivers", "🔧 Liste des drivers système", True),
            ("settings", "⚙️ Paramètres NiTriTe", True),
            ("diagnostic_logs", "📊 Logs de diagnostic PC", True),
        ]
        
        for key, text, default in options:
            var = tk.BooleanVar(value=default)
            self.backup_options[key] = var
            check = ctk.CTkCheckBox(
                content,
                text=text,
                variable=var,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                fg_color=DesignTokens.ACCENT_PRIMARY
            )
            check.pack(anchor="w", pady=5)
        
        # Bouton
        ModernButton(
            content,
            text="💾 Créer Sauvegarde",
            variant="filled",
            command=self._create_backup
        ).pack(pady=15)
    
    def _create_restore_section(self, parent):
        """Section restauration"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="♻️ Restaurer une Sauvegarde",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        desc = ctk.CTkLabel(
            content,
            text="Sélectionnez une sauvegarde ci-dessous pour la restaurer",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=10)
    
    def _create_backups_list_section(self, parent):
        """Liste des sauvegardes"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="📋 Sauvegardes Disponibles",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        self.backups_container = ctk.CTkFrame(card, fg_color="transparent")
        self.backups_container.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self._refresh_backups_list()
    
    def _refresh_backups_list(self):
        """Rafraîchir liste des sauvegardes"""
        # Clear
        for widget in self.backups_container.winfo_children():
            widget.destroy()
        
        # Lister fichiers backup
        backups = sorted(self.backup_dir.glob("backup_*.json"), reverse=True)
        
        if not backups:
            msg = ctk.CTkLabel(
                self.backups_container,
                text="Aucune sauvegarde disponible",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_SECONDARY
            )
            msg.pack(pady=10)
            return
        
        for backup_file in backups[:10]:  # Max 10
            try:
                with open(backup_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                name = backup_file.stem
                info = f"{data.get('apps_count', 0)} apps"
                size = f"{backup_file.stat().st_size / 1024:.1f} KB"
                
                self._create_backup_row(self.backups_container, name, info, size, backup_file)
            except:
                continue
    
    def _create_backup_row(self, parent, name, info, size, filepath):
        """Ligne de sauvegarde"""
        row = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        row.pack(fill=tk.X, pady=5)
        
        container = ctk.CTkFrame(row, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=12)
        
        left = ctk.CTkFrame(container, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        name_label = ctk.CTkLabel(
            left,
            text=name,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        info_label = ctk.CTkLabel(
            left,
            text=f"{info} • {size}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        info_label.pack(anchor="w")
        
        buttons = ctk.CTkFrame(container, fg_color="transparent")
        buttons.pack(side=tk.RIGHT)
        
        ModernButton(
            buttons,
            text="♻️ Restaurer",
            variant="filled",
            size="sm",
            command=lambda: self._restore_backup(filepath)
        ).pack(side=tk.LEFT, padx=3)
        
        ModernButton(
            buttons,
            text="🗑️",
            variant="text",
            size="sm",
            command=lambda: self._delete_backup(filepath)
        ).pack(side=tk.LEFT, padx=3)
    
    def _create_backup(self):
        """Créer sauvegarde"""
        print("💾 Création de la sauvegarde...")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.backup_dir / f"backup_{timestamp}.json"
        
        backup_data = {
            "timestamp": timestamp,
            "date": datetime.now().isoformat(),
            "apps_count": 0,
            "apps": []
        }
        
        # Sauvegarder liste apps installées si demandé
        if self.backup_options["apps"].get():
            try:
                result = subprocess.run(
                    ["winget", "list"],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore'
                )
                if result.returncode == 0:
                    lines = result.stdout.split('\n')
                    backup_data["apps"] = [line.strip() for line in lines if line.strip()]
                    backup_data["apps_count"] = len(backup_data["apps"])
            except:
                pass

        # Sauvegarder logs de diagnostic si demandé
        if self.backup_options["diagnostic_logs"].get():
            try:
                logs_dir = Path("data/logs")
                if logs_dir.exists():
                    backup_data["diagnostic_logs"] = {
                        "included": True,
                        "log_files": []
                    }

                    # Copier tous les fichiers logs dans le backup
                    logs_backup_dir = self.backup_dir / f"logs_{timestamp}"
                    logs_backup_dir.mkdir(exist_ok=True)

                    import shutil
                    for log_file in logs_dir.glob("*.log"):
                        try:
                            dest_file = logs_backup_dir / log_file.name
                            shutil.copy2(log_file, dest_file)
                            backup_data["diagnostic_logs"]["log_files"].append(log_file.name)
                        except Exception as e:
                            print(f"⚠️ Erreur copie {log_file.name}: {e}")

                    backup_data["diagnostic_logs"]["count"] = len(backup_data["diagnostic_logs"]["log_files"])
                    backup_data["diagnostic_logs"]["path"] = str(logs_backup_dir)
                    print(f"✅ {backup_data['diagnostic_logs']['count']} fichiers logs sauvegardés")
                else:
                    backup_data["diagnostic_logs"] = {"included": False, "reason": "Aucun log trouvé"}
            except Exception as e:
                backup_data["diagnostic_logs"] = {"included": False, "error": str(e)}
                print(f"⚠️ Erreur sauvegarde logs: {e}")

        # Sauvegarder
        try:
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Sauvegarde créée: {backup_file}")
            self._refresh_backups_list()
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _restore_backup(self, filepath):
        """Restaurer sauvegarde"""
        print(f"♻️ Restauration de {filepath.name}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"✅ Backup chargé: {data.get('apps_count', 0)} apps")
            # TODO: Implémenter restauration réelle
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _delete_backup(self, filepath):
        """Supprimer sauvegarde"""
        try:
            filepath.unlink()
            print(f"🗑️ Suppression de {filepath.name}")
            self._refresh_backups_list()
        except Exception as e:
            print(f"❌ Erreur: {e}")


class DiagnosticPage(ctk.CTkFrame):
    """Page Diagnostic avec vraie détection psutil"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.system_info = self._get_system_info()

        # Variables pour mise à jour en temps réel
        self.cpu_card = None
        self.ram_card = None
        self.update_timer = None

        self._create_header()
        self._create_content()

        # Démarrer la mise à jour en temps réel
        if PSUTIL_AVAILABLE:
            self._start_realtime_updates()
    
    def _get_ram_type_name(self, memory_type_code):
        """Convertir le code WMI MemoryType en nom lisible (DDR3, DDR4, DDR5)"""
        memory_types = {
            0: "Unknown",
            1: "Other",
            2: "DRAM",
            3: "Synchronous DRAM",
            4: "Cache DRAM",
            5: "EDO",
            6: "EDRAM",
            7: "VRAM",
            8: "SRAM",
            9: "RAM",
            10: "ROM",
            11: "Flash",
            12: "EEPROM",
            13: "FEPROM",
            14: "EPROM",
            15: "CDRAM",
            16: "3DRAM",
            17: "SDRAM",
            18: "SGRAM",
            19: "RDRAM",
            20: "DDR",
            21: "DDR2",
            22: "DDR2 FB-DIMM",
            24: "DDR3",
            25: "FBD2",
            26: "DDR4",
            27: "LPDDR",
            28: "LPDDR2",
            29: "LPDDR3",
            30: "LPDDR4",
            34: "DDR5",
            35: "LPDDR5"
        }
        return memory_types.get(memory_type_code, f"Unknown ({memory_type_code})")

    def _get_system_info(self):
        """Obtenir vraies informations système avec détails matériels"""
        info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "os_release": platform.release(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "hostname": platform.node(),
        }

        # Obtenir noms exacts des composants via WMI (Windows uniquement)
        try:
            import wmi
            w = wmi.WMI()

            # CPU - Nom exact
            for cpu in w.Win32_Processor():
                info["cpu_name"] = cpu.Name.strip()
                info["cpu_manufacturer"] = cpu.Manufacturer
                info["cpu_cores"] = cpu.NumberOfCores
                info["cpu_threads"] = cpu.NumberOfLogicalProcessors
                info["cpu_max_speed"] = cpu.MaxClockSpeed  # MHz
                break

            # RAM - Modules détaillés avec génération DDR (utilise SMBIOSMemoryType pour meilleure détection)
            info["ram_modules"] = []
            total_ram_gb = 0
            for mem in w.Win32_PhysicalMemory():
                capacity_gb = int(mem.Capacity) / (1024**3)
                total_ram_gb += capacity_gb

                # Essayer d'abord SMBIOSMemoryType (plus fiable), puis MemoryType en fallback
                memory_type_code = 0
                if hasattr(mem, 'SMBIOSMemoryType') and mem.SMBIOSMemoryType:
                    memory_type_code = mem.SMBIOSMemoryType
                elif mem.MemoryType:
                    memory_type_code = mem.MemoryType

                # Si toujours 0, essayer de deviner selon la vitesse
                if memory_type_code == 0 or memory_type_code == 2:  # Unknown ou DRAM générique
                    speed = mem.Speed if mem.Speed else 0
                    if speed >= 4800:
                        memory_type_code = 34  # DDR5
                    elif speed >= 2133:
                        memory_type_code = 26  # DDR4
                    elif speed >= 800:
                        memory_type_code = 24  # DDR3
                    elif speed > 0:
                        memory_type_code = 21  # DDR2

                memory_type_name = self._get_ram_type_name(memory_type_code)

                info["ram_modules"].append({
                    "manufacturer": mem.Manufacturer.strip() if mem.Manufacturer else "Unknown",
                    "capacity_gb": capacity_gb,
                    "speed_mhz": mem.Speed if mem.Speed else 0,
                    "type_code": memory_type_code,
                    "type_name": memory_type_name,
                    "form_factor": mem.FormFactor if mem.FormFactor else 0,
                    "device_locator": mem.DeviceLocator if mem.DeviceLocator else "Unknown"
                })
            info["ram_total_gb"] = total_ram_gb

            # Déterminer type RAM dominant (le plus courant)
            if info["ram_modules"]:
                from collections import Counter
                type_counts = Counter(m["type_name"] for m in info["ram_modules"])
                info["ram_type_dominant"] = type_counts.most_common(1)[0][0]
                speed_values = [m["speed_mhz"] for m in info["ram_modules"] if m["speed_mhz"] > 0]
                info["ram_speed_avg"] = sum(speed_values) / len(speed_values) if speed_values else 0
            
            # Carte mère
            for board in w.Win32_BaseBoard():
                info["motherboard_manufacturer"] = board.Manufacturer
                info["motherboard_product"] = board.Product
                break
            
            # GPU - Cartes graphiques
            info["gpus"] = []
            for gpu in w.Win32_VideoController():
                info["gpus"].append({
                    "name": gpu.Name,
                    "ram_bytes": gpu.AdapterRAM if gpu.AdapterRAM else 0,
                    "driver_version": gpu.DriverVersion if gpu.DriverVersion else "N/A"
                })
            
            # Disques - Modèles exacts
            info["storage_devices"] = []
            for disk in w.Win32_DiskDrive():
                size_gb = int(disk.Size) / (1024**3) if disk.Size else 0
                info["storage_devices"].append({
                    "model": disk.Model if disk.Model else "Unknown",
                    "size_gb": size_gb,
                    "interface": disk.InterfaceType if disk.InterfaceType else "Unknown"
                })
            
        except ImportError:
            print("⚠️ Module wmi non disponible - installation: pip install wmi")
            # Fallback sans WMI
            info["cpu_name"] = platform.processor()
        except Exception as e:
            print(f"⚠️ Erreur WMI: {e}")
        
        # Données psutil (usage actuel)
        if PSUTIL_AVAILABLE:
            # CPU usage
            info["cpu_count"] = psutil.cpu_count(logical=False)
            info["cpu_threads"] = psutil.cpu_count(logical=True)
            info["cpu_percent"] = psutil.cpu_percent(interval=1)
            info["cpu_freq"] = psutil.cpu_freq()
            
            # RAM usage
            mem = psutil.virtual_memory()
            info["ram_total"] = mem.total / (1024**3)  # GB
            info["ram_used"] = mem.used / (1024**3)
            info["ram_percent"] = mem.percent
            
            # Partitions disques
            info["disks"] = []
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    info["disks"].append({
                        "mount": partition.mountpoint,
                        "fstype": partition.fstype,
                        "total": usage.total / (1024**3),
                        "used": usage.used / (1024**3),
                        "percent": usage.percent
                    })
                except:
                    continue
            
            # Réseau
            net = psutil.net_io_counters()
            info["net_sent"] = net.bytes_sent / (1024**2)  # MB
            info["net_recv"] = net.bytes_recv / (1024**2)
        
        return info
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="🔍 Diagnostic",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        # Boutons d'action
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text="💾 Exporter",
            variant="outlined",
            command=self._export_pc_info
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text="🔄 Analyser",
            variant="filled",
            command=self._run_diagnostic
        ).pack(side=tk.LEFT)
    
    def _create_content(self):
        """Contenu"""
        # Stats système (avec mise à jour temps réel)
        stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)

        cpu_val = f"{self.system_info.get('cpu_percent', 0):.1f}%" if PSUTIL_AVAILABLE else "N/A"
        self.cpu_card = ModernStatsCard(
            stats_frame,
            "CPU",
            cpu_val,
            "💻",
            DesignTokens.INFO
        )
        self.cpu_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        if PSUTIL_AVAILABLE:
            ram_val = f"{self.system_info['ram_used']:.1f}/{self.system_info['ram_total']:.1f} GB"
        else:
            ram_val = "N/A"
        self.ram_card = ModernStatsCard(
            stats_frame,
            "RAM",
            ram_val,
            "🧠",
            DesignTokens.SUCCESS
        )
        self.ram_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        if PSUTIL_AVAILABLE and self.system_info.get('disks'):
            disk = self.system_info['disks'][0]
            disk_val = f"{disk['used']:.0f}/{disk['total']:.0f} GB"
        else:
            disk_val = "N/A"
        ModernStatsCard(
            stats_frame,
            "Disque",
            disk_val,
            "💾",
            DesignTokens.WARNING
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        net_val = "OK" if PSUTIL_AVAILABLE else "N/A"
        ModernStatsCard(
            stats_frame,
            "Réseau",
            net_val,
            "🌐",
            DesignTokens.SUCCESS
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Résultats diagnostic
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Sections avec vraies données
        self._create_system_section(scroll)
        self._create_hardware_section(scroll)
        self._create_storage_section(scroll)
        self._create_network_section(scroll)
        self._create_tools_section(scroll)
    
    def _create_system_section(self, parent):
        """Section système"""
        items = [
            ("OS", f"{self.system_info['os']} {self.system_info['os_release']}", "✅"),
            ("Version", self.system_info['os_version'][:50], "✅"),
            ("Architecture", self.system_info['architecture'], "✅"),
            ("Hostname", self.system_info['hostname'], "✅"),
        ]
        
        # Carte mère si disponible
        if 'motherboard_product' in self.system_info:
            mb_info = f"{self.system_info.get('motherboard_manufacturer', 'N/A')} {self.system_info.get('motherboard_product', 'N/A')}"
            items.append(("Carte mère", mb_info, "✅"))
        
        self._create_diagnostic_section(parent, "💻 Système", items)
    
    def _create_hardware_section(self, parent):
        """Section matériel avec noms exacts"""
        items = []
        
        # CPU - Nom exact si disponible via WMI
        if 'cpu_name' in self.system_info:
            cpu_name = self.system_info['cpu_name']
            cpu_details = f"{self.system_info.get('cpu_cores', '?')} cores / {self.system_info.get('cpu_threads', '?')} threads"
            if 'cpu_max_speed' in self.system_info:
                cpu_details += f" @ {self.system_info['cpu_max_speed']} MHz"
            items.append(("Processeur", cpu_name, "✅"))
            items.append(("Configuration CPU", cpu_details, "✅"))
            
            if PSUTIL_AVAILABLE:
                items.append(("Utilisation CPU", f"{self.system_info.get('cpu_percent', 0):.1f}%", "✅"))
        else:
            # Fallback
            if PSUTIL_AVAILABLE:
                cpu_count = self.system_info.get('cpu_count', '?')
                cpu_threads = self.system_info.get('cpu_threads', '?')
                cpu_info = f"{cpu_count} cores / {cpu_threads} threads"
                items.append(("Processeur", self.system_info.get('processor', 'N/A'), "✅"))
                items.append(("Configuration", cpu_info, "✅"))
            else:
                items.append(("Processeur", self.system_info.get('processor', 'N/A'), "⚠️"))
        
        # RAM - Modules détaillés si disponibles
        if 'ram_modules' in self.system_info and self.system_info['ram_modules']:
            total_ram = self.system_info.get('ram_total_gb', 0)
            ram_type = self.system_info.get('ram_type_dominant', 'Unknown')
            ram_speed = self.system_info.get('ram_speed_avg', 0)

            # Ligne 1: Total RAM avec type et fréquence (génération bien visible)
            if ram_speed > 0:
                ram_summary = f"{total_ram:.1f} GB de RAM {ram_type} @ {ram_speed:.0f} MHz"
            else:
                ram_summary = f"{total_ram:.1f} GB de RAM {ram_type}"
            items.append(("RAM Totale", ram_summary, "✅"))

            # Ligne supplémentaire pour type/génération de RAM (plus visible)
            items.append(("Génération RAM", f"{ram_type}", "✅"))

            # Afficher chaque module avec détails complets
            for i, module in enumerate(self.system_info['ram_modules'][:4], 1):  # Max 4 modules
                module_info = f"{module['manufacturer']} {module['capacity_gb']:.0f}GB {module['type_name']}"
                if module['speed_mhz'] > 0:
                    module_info += f" @ {module['speed_mhz']}MHz"
                if module['device_locator'] != "Unknown":
                    module_info += f" ({module['device_locator']})"
                items.append((f"  Module {i}", module_info, "✅"))

            if PSUTIL_AVAILABLE:
                ram_used = self.system_info.get('ram_used', 0)
                ram_percent = self.system_info.get('ram_percent', 0)
                ram_usage = f"{ram_used:.1f} GB utilisés ({ram_percent:.1f}%)"
                items.append(("Utilisation RAM", ram_usage, "✅"))
        else:
            # Fallback
            if PSUTIL_AVAILABLE:
                ram_total = self.system_info.get('ram_total', 0)
                ram_percent = self.system_info.get('ram_percent', 0)
                ram_info = f"{ram_total:.1f} GB ({ram_percent:.1f}% utilisés)"
                items.append(("RAM", ram_info, "✅"))
            else:
                items.append(("RAM", "psutil requis", "⚠️"))
        
        # GPU - Cartes graphiques
        if 'gpus' in self.system_info and self.system_info['gpus']:
            for i, gpu in enumerate(self.system_info['gpus'][:3], 1):  # Max 3 GPUs
                gpu_name = gpu['name']
                gpu_ram = gpu['ram_bytes'] / (1024**3) if gpu['ram_bytes'] > 0 else 0
                if gpu_ram > 0:
                    gpu_info = f"{gpu_name} ({gpu_ram:.0f} GB VRAM)"
                else:
                    gpu_info = gpu_name
                items.append((f"GPU {i}" if len(self.system_info['gpus']) > 1 else "GPU", gpu_info, "✅"))
        
        self._create_diagnostic_section(parent, "🧠 Matériel", items)
    
    def _create_storage_section(self, parent):
        """Section stockage avec modèles de disques"""
        items = []
        
        # Disques physiques avec modèles
        if 'storage_devices' in self.system_info and self.system_info['storage_devices']:
            for i, device in enumerate(self.system_info['storage_devices'], 1):
                device_info = f"{device['model']} - {device['size_gb']:.0f} GB ({device['interface']})"
                items.append((f"Disque {i}", device_info, "✅"))
        
        # Partitions avec usage
        if PSUTIL_AVAILABLE and self.system_info.get('disks'):
            if items:  # Si on a déjà des disques physiques
                items.append(("", "--- Partitions ---", ""))  # Séparateur
            for disk in self.system_info['disks']:
                try:
                    percent = float(disk.get('percent', 0))
                    status = "✅" if percent < 80 else "⚠️"
                    used = float(disk.get('used', 0))
                    total = float(disk.get('total', 0))
                    items.append((
                        f"Partition {disk['mount']}",
                        f"{used:.1f} / {total:.1f} GB ({percent:.1f}%) - {disk.get('fstype', 'N/A')}",
                        status
                    ))
                except (TypeError, ValueError, KeyError):
                    continue
        elif not items:
            items = [("Disques", "Informations non disponibles", "⚠️")]
        
        self._create_diagnostic_section(parent, "💾 Stockage", items)
    
    def _create_network_section(self, parent):
        """Section réseau avec détails complets (portable - sans netifaces)"""
        items = []

        if PSUTIL_AVAILABLE:
            # Données envoyées/reçues
            items.append(("Données envoyées", f"{self.system_info['net_sent']:.1f} MB", "✅"))
            items.append(("Données reçues", f"{self.system_info['net_recv']:.1f} MB", "✅"))

            # Informations réseau détaillées via psutil (portable)
            try:
                import socket

                # Nom d'hôte
                hostname = socket.gethostname()
                items.append(("Nom d'hôte", hostname, "✅"))

                # Utiliser psutil.net_if_addrs() au lieu de netifaces (portable)
                net_if_addrs = psutil.net_if_addrs()

                for iface_name, addrs in net_if_addrs.items():
                    for addr in addrs:
                        # IPv4
                        if addr.family == socket.AF_INET:
                            if not addr.address.startswith('127.'):
                                netmask = addr.netmask if addr.netmask else 'N/A'
                                items.append((f"IPv4 ({iface_name})", f"{addr.address} / {netmask}", "✅"))

                        # IPv6
                        elif addr.family == socket.AF_INET6:
                            if not addr.address.startswith('::1') and not addr.address.startswith('fe80'):
                                items.append((f"IPv6 ({iface_name})", addr.address.split('%')[0], "✅"))

                # Obtenir la passerelle via ipconfig (Windows uniquement - portable)
                if platform.system() == "Windows":
                    try:
                        import subprocess
                        result = subprocess.run(['ipconfig'], capture_output=True, text=True, timeout=5)
                        output = result.stdout

                        # Parser la sortie pour trouver la passerelle par défaut
                        for line in output.split('\n'):
                            if 'Passerelle par défaut' in line or 'Default Gateway' in line:
                                gateway = line.split(':')[-1].strip()
                                if gateway and gateway != '' and not gateway.startswith('fe80'):
                                    items.append(("Passerelle par défaut", gateway, "✅"))
                                    break
                    except Exception as e:
                        pass  # Ignorer les erreurs de parsing

            except Exception as e:
                items.append(("Erreur réseau", str(e)[:50], "⚠️"))
        else:
            items = [("Réseau", "psutil requis", "⚠️")]

        # Créer la section
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill=tk.X, padx=20, pady=15)

        header_label = ctk.CTkLabel(
            header_frame,
            text="🌐 Réseau",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        header_label.pack(side=tk.LEFT)

        # Bouton Speed Test
        ModernButton(
            header_frame,
            text="🚀 Speed Test",
            variant="filled",
            size="sm",
            command=self._run_speed_test
        ).pack(side=tk.RIGHT)

        # Items
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 20))

        for label, value, status in items:
            row = ctk.CTkFrame(content, fg_color="transparent")
            row.pack(fill=tk.X, pady=2)

            status_label = ctk.CTkLabel(
                row,
                text=status,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                width=30
            )
            status_label.pack(side=tk.LEFT)

            label_widget = ctk.CTkLabel(
                row,
                text=label,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY,
                anchor="w",
                width=200
            )
            label_widget.pack(side=tk.LEFT, padx=10)

            value_widget = ctk.CTkLabel(
                row,
                text=str(value),
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            )
            value_widget.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def _create_tools_section(self, parent):
        """Section outils de diagnostic avancés"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        header = ctk.CTkLabel(
            card,
            text="🛠️ Outils de Diagnostic",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        header.pack(fill=tk.X, padx=20, pady=15)

        # Boutons d'outils
        tools_frame = ctk.CTkFrame(card, fg_color="transparent")
        tools_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        # Ligne 1: CrystalDiskInfo, OCCT et Test Batterie OrdiPlus
        row1 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row1.pack(fill=tk.X, pady=5)

        ModernButton(
            row1,
            text="💾 CrystalDiskInfo",
            variant="outlined",
            size="md",
            command=self._launch_crystaldiskinfo
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row1,
            text="🌡️ OCCT (Temp & Stress)",
            variant="outlined",
            size="md",
            command=self._launch_occt
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row1,
            text="🔋 Test Batterie OrdiPlus",
            variant="outlined",
            size="md",
            command=self._test_battery
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 2: Test Batterie NiTrite, Autoruns et Malwarebytes
        row2 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row2.pack(fill=tk.X, pady=5)

        ModernButton(
            row2,
            text="🔋 Test Batterie NiTrite",
            variant="outlined",
            size="md",
            command=self._test_battery_nitrite
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row2,
            text="🚀 Autoruns",
            variant="outlined",
            size="md",
            command=self._launch_autoruns
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row2,
            text="🛡️ Malwarebytes Portable",
            variant="outlined",
            size="md",
            command=self._launch_malwarebytes
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 3: Spybot, AdwCleaner et Wise Disk Cleaner
        row3 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row3.pack(fill=tk.X, pady=5)

        ModernButton(
            row3,
            text="🕵️ Spybot Search & Destroy",
            variant="outlined",
            size="md",
            command=self._launch_spybot
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row3,
            text="🧹 AdwCleaner Portable",
            variant="outlined",
            size="md",
            command=self._launch_adwcleaner
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row3,
            text="💿 Wise Disk Cleaner",
            variant="outlined",
            size="md",
            command=self._launch_wisediskcleaner
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 4: HWMonitor, HWinfo et CrystalDiskMark
        row4 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row4.pack(fill=tk.X, pady=5)

        ModernButton(
            row4,
            text="🌡️ HWMonitor",
            variant="outlined",
            size="md",
            command=self._launch_hwmonitor
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row4,
            text="📊 HWinfo",
            variant="outlined",
            size="md",
            command=self._launch_hwinfo
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row4,
            text="💾 CrystalDiskMark",
            variant="outlined",
            size="md",
            command=self._launch_crystaldiskmark
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 5: CPU-Z, GPU-Z et Wise Care 365
        row5 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row5.pack(fill=tk.X, pady=5)

        ModernButton(
            row5,
            text="🔬 CPU-Z",
            variant="outlined",
            size="md",
            command=self._launch_cpuz
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row5,
            text="🎮 GPU-Z",
            variant="outlined",
            size="md",
            command=self._launch_gpuz
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row5,
            text="🛠️ Wise Care 365",
            variant="outlined",
            size="md",
            command=self._launch_wisecare365
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 6: Activation Windows/Office, MSCONFIG et Gestionnaire des Tâches
        row6 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row6.pack(fill=tk.X, pady=5)

        ModernButton(
            row6,
            text="🔑 Activation Windows/Office",
            variant="outlined",
            size="md",
            command=self._activate_windows_office
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row6,
            text="⚙️ MSCONFIG",
            variant="outlined",
            size="md",
            command=lambda: self._execute_tool("MSCONFIG", "msconfig")
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row6,
            text="📊 Gestionnaire des Tâches",
            variant="outlined",
            size="md",
            command=lambda: self._execute_tool("Gestionnaire des tâches", "taskmgr")
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 7: MSINFO, Dossier Temp et AppData Local
        row7 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row7.pack(fill=tk.X, pady=5)

        ModernButton(
            row7,
            text="ℹ️ MSINFO",
            variant="outlined",
            size="md",
            command=lambda: self._execute_tool("MSINFO", "msinfo32")
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row7,
            text="🗂️ Dossier Temp",
            variant="outlined",
            size="md",
            command=self._open_temp_folder
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row7,
            text="📁 AppData Local",
            variant="outlined",
            size="md",
            command=self._open_appdata_local
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 8: Version Windows, Tout Mettre à Jour et Drivers NVIDIA
        row8 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row8.pack(fill=tk.X, pady=5)

        ModernButton(
            row8,
            text="🪟 Version Windows",
            variant="outlined",
            size="md",
            command=lambda: self._execute_tool("Version Windows", "winver")
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row8,
            text="🔄 Tout Mettre à Jour",
            variant="outlined",
            size="md",
            command=self._update_all_apps
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row8,
            text="🎮 Drivers NVIDIA",
            variant="outlined",
            size="md",
            command=self._update_nvidia_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 9: Drivers AMD, Réparer Image Windows et Propriétés Utilisateur
        row9 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row9.pack(fill=tk.X, pady=5)

        ModernButton(
            row9,
            text="🔴 Drivers AMD",
            variant="outlined",
            size="md",
            command=self._update_amd_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row9,
            text="🔧 Réparer Image Windows",
            variant="outlined",
            size="md",
            command=self._repair_windows_image
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row9,
            text="👤 Propriétés Utilisateur",
            variant="outlined",
            size="md",
            command=self._open_user_properties
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 10: Système et CHKDSK Complet
        row10 = ctk.CTkFrame(tools_frame, fg_color="transparent")
        row10.pack(fill=tk.X, pady=5)

        ModernButton(
            row10,
            text="⚙️ Système",
            variant="outlined",
            size="md",
            command=lambda: self._execute_tool("Système", "sysdm.cpl")
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row10,
            text="🔍 CHKDSK Complet",
            variant="outlined",
            size="md",
            command=self._run_chkdsk
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _start_realtime_updates(self):
        """Démarrer les mises à jour en temps réel des statistiques"""
        self._update_stats()

    def _update_stats(self):
        """Mettre à jour les statistiques CPU et RAM en temps réel"""
        try:
            if PSUTIL_AVAILABLE and self.cpu_card and self.ram_card:
                # Mise à jour CPU
                cpu_percent = psutil.cpu_percent(interval=0.1)
                self.cpu_card.update_value(f"{cpu_percent:.1f}%")

                # Mise à jour RAM
                ram = psutil.virtual_memory()
                ram_used = ram.used / (1024**3)
                ram_total = ram.total / (1024**3)
                self.ram_card.update_value(f"{ram_used:.1f}/{ram_total:.1f} GB")

                # Planifier la prochaine mise à jour dans 2 secondes
                self.update_timer = self.after(2000, self._update_stats)
        except Exception as e:
            print(f"Erreur mise à jour stats: {e}")

    def destroy(self):
        """Nettoyer les timers quand la page est détruite"""
        if self.update_timer:
            self.after_cancel(self.update_timer)
        super().destroy()

    def _run_speed_test(self):
        """Exécuter un test de vitesse intégré"""
        from tkinter import messagebox
        import threading

        # Créer fenêtre de test
        test_window = ctk.CTkToplevel(self)
        test_window.title("🚀 Speed Test - Test de connexion")
        test_window.geometry("600x500")
        test_window.resizable(False, False)

        # Centrer
        test_window.update_idletasks()
        x = (test_window.winfo_screenwidth() // 2) - (300)
        y = (test_window.winfo_screenheight() // 2) - (250)
        test_window.geometry(f"600x500+{x}+{y}")

        # Contenu
        content = ctk.CTkFrame(test_window, fg_color=DesignTokens.BG_PRIMARY)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Header
        header = ctk.CTkLabel(
            content,
            text="🚀 Test de Vitesse de Connexion",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        header.pack(pady=(0, 20))

        # Status
        status_label = ctk.CTkLabel(
            content,
            text="Initialisation...",
            font=(DesignTokens.FONT_FAMILY, 16),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        status_label.pack(pady=10)

        # Progress
        progress = ctk.CTkProgressBar(
            content,
            width=500,
            height=25,
            corner_radius=12
        )
        progress.pack(pady=20)
        progress.set(0)

        # Résultats
        results_frame = ctk.CTkFrame(content, fg_color=DesignTokens.BG_ELEVATED, corner_radius=DesignTokens.RADIUS_LG)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        def run_test():
            try:
                status_label.configure(text="Vérification du module speedtest...")
                progress.set(0.1)
                test_window.update()

                try:
                    import speedtest
                except ImportError:
                    status_label.configure(text="❌ Module speedtest-cli manquant")
                    messagebox.showwarning(
                        "Module manquant",
                        "Le module speedtest-cli n'est pas installé.\n\n"
                        "Installation requise:\n"
                        "pip install speedtest-cli"
                    )
                    return

                status_label.configure(text="🔍 Recherche du meilleur serveur...")
                progress.set(0.2)
                test_window.update()

                st = speedtest.Speedtest()
                st.get_best_server()

                status_label.configure(text="⬇️ Test de téléchargement...")
                progress.set(0.4)
                test_window.update()

                download_speed = st.download() / 1_000_000  # Convertir en Mbps

                status_label.configure(text="⬆️ Test d'envoi...")
                progress.set(0.7)
                test_window.update()

                upload_speed = st.upload() / 1_000_000  # Convertir en Mbps

                status_label.configure(text="🏓 Test de ping...")
                progress.set(0.9)
                test_window.update()

                results = st.results.dict()
                ping = results['ping']
                server = results['server']

                progress.set(1.0)
                status_label.configure(text="✅ Test terminé!")

                # Afficher les résultats
                results_text = f"""
📊 RÉSULTATS DU TEST DE VITESSE

⬇️ Téléchargement: {download_speed:.2f} Mbps
⬆️ Envoi: {upload_speed:.2f} Mbps
🏓 Ping: {ping:.0f} ms

🌐 Serveur: {server['sponsor']}
📍 Localisation: {server['name']}, {server['country']}
🔗 Hébergeur: {server['host']}

💡 Évaluation:
"""
                if download_speed > 100:
                    results_text += "🟢 Excellente connexion !"
                elif download_speed > 50:
                    results_text += "🟡 Bonne connexion"
                elif download_speed > 10:
                    results_text += "🟠 Connexion correcte"
                else:
                    results_text += "🔴 Connexion lente"

                result_label = ctk.CTkLabel(
                    results_frame,
                    text=results_text,
                    font=(DesignTokens.FONT_FAMILY, 14),
                    text_color=DesignTokens.TEXT_PRIMARY,
                    justify="left"
                )
                result_label.pack(padx=20, pady=20)

            except Exception as e:
                status_label.configure(text=f"❌ Erreur: {str(e)[:50]}")
                messagebox.showerror(
                    "Erreur Speed Test",
                    f"Impossible d'exécuter le test de vitesse:\n\n{str(e)}"
                )

        # Bouton fermer
        close_btn = ModernButton(
            content,
            text="Fermer",
            variant="outlined",
            command=test_window.destroy
        )
        close_btn.pack(pady=10)

        # Lancer le test dans un thread
        thread = threading.Thread(target=run_test, daemon=True)
        thread.start()

    def _launch_crystaldiskinfo(self):
        """Lancer CrystalDiskInfo portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()
            cdi_dir = os.path.join(tools_dir, "CrystalDiskInfo")
            os.makedirs(cdi_dir, exist_ok=True)

            # Chercher l'exécutable (nom peut varier)
            cdi_exe = None
            if os.path.exists(cdi_dir):
                for file in os.listdir(cdi_dir):
                    if file.endswith('.exe') and 'DiskInfo' in file and '64' in file:
                        cdi_exe = os.path.join(cdi_dir, file)
                        break

            # Vérifier si déjà téléchargé
            if not cdi_exe or not os.path.exists(cdi_exe):
                response = messagebox.askyesno(
                    "Télécharger CrystalDiskInfo",
                    "CrystalDiskInfo n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~6 MB, version portable, téléchargement unique)",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL CrystalDiskInfo Portable (lien direct depuis le site officiel)
                # Version portable Shizuku Edition (plus jolie interface)
                url = "https://sourceforge.net/projects/crystaldiskinfo/files/latest/download"
                zip_path = os.path.join(tools_dir, "cdi.zip")

                # Télécharger
                print(f"📥 Téléchargement de CrystalDiskInfo...")
                try:
                    urllib.request.urlretrieve(url, zip_path)

                    # Extraire
                    print(f"📦 Extraction...")
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(cdi_dir)

                    # Nettoyer
                    os.remove(zip_path)
                    print(f"✅ CrystalDiskInfo installé dans: {cdi_dir}")

                    # Rechercher l'exécutable après extraction
                    cdi_exe = None
                    for file in os.listdir(cdi_dir):
                        if file.endswith('.exe') and 'DiskInfo' in file and '64' in file:
                            cdi_exe = os.path.join(cdi_dir, file)
                            break

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger CrystalDiskInfo:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://crystalmark.info/en/software/crystaldiskinfo/\n\n"
                        f"Et placez les fichiers dans:\n{cdi_dir}"
                    )
                    return

            # Lancer
            if cdi_exe and os.path.exists(cdi_exe):
                subprocess.Popen([cdi_exe], shell=True)
                messagebox.showinfo(
                    "CrystalDiskInfo",
                    f"CrystalDiskInfo lancé!\n\n"
                    f"Emplacement: {cdi_exe}"
                )
            else:
                raise FileNotFoundError("Exécutable CrystalDiskInfo introuvable après extraction")

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer CrystalDiskInfo:\n\n{str(e)}\n\n"
                f"Vous pouvez le télécharger manuellement depuis:\n"
                f"https://crystalmark.info/en/software/crystaldiskinfo/\n\n"
                f"Et placer les fichiers dans:\n{os.path.join(get_local_software_folder(), 'CrystalDiskInfo')}"
            )

    def _launch_occt(self):
        """Lancer OCCT portable (Monitoring température + Stress test)"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Créer dossier portable_tools s'il n'existe pas
            tools_dir = os.path.join(os.path.expanduser("~"), "Desktop", "NiTriTe_Tools")
            os.makedirs(tools_dir, exist_ok=True)

            occt_dir = os.path.join(tools_dir, "OCCT")

            # Chercher l'exécutable (nom peut varier)
            occt_exe = None
            if os.path.exists(occt_dir):
                for file in os.listdir(occt_dir):
                    if file.endswith('.exe') and 'OCCT' in file:
                        occt_exe = os.path.join(occt_dir, file)
                        break

            # Vérifier si déjà téléchargé
            if not occt_exe or not os.path.exists(occt_exe):
                response = messagebox.askyesno(
                    "Télécharger OCCT",
                    "OCCT n'est pas encore téléchargé.\n\n"
                    "OCCT est un outil professionnel pour:\n"
                    "• Surveiller les températures CPU/GPU\n"
                    "• Tester la stabilité du système\n"
                    "• Détecter les problèmes de surchauffe\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~25 MB, téléchargement unique)",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants...\n"
                    "OCCT est un outil gratuit pour usage personnel."
                )

                # URL OCCT portable (version gratuite)
                # Note: OCCT peut être un .exe portable ou un .zip
                url = "https://www.ocbase.com/download/occt"
                download_path = os.path.join(tools_dir, "occt_download")

                try:
                    # Télécharger
                    print(f"📥 Téléchargement d'OCCT...")
                    urllib.request.urlretrieve(url, download_path)

                    os.makedirs(occt_dir, exist_ok=True)

                    # Vérifier le type de fichier téléchargé
                    # Lire les premiers bytes pour détecter le format
                    with open(download_path, 'rb') as f:
                        header = f.read(4)

                    # Vérifier si c'est un ZIP (commence par PK)
                    if header[:2] == b'PK':
                        # C'est un fichier ZIP - extraire
                        print(f"📦 Extraction du ZIP...")
                        with zipfile.ZipFile(download_path, 'r') as zip_ref:
                            zip_ref.extractall(occt_dir)

                        # Rechercher l'exécutable après extraction
                        occt_exe = None
                        for file in os.listdir(occt_dir):
                            if file.endswith('.exe') and 'OCCT' in file:
                                occt_exe = os.path.join(occt_dir, file)
                                break

                    # Vérifier si c'est un EXE (commence par MZ)
                    elif header[:2] == b'MZ':
                        # C'est un exécutable portable - sauvegarder directement
                        print(f"💾 Installation de l'exécutable portable...")
                        occt_exe = os.path.join(occt_dir, "OCCT.exe")

                        # Copier le fichier téléchargé vers le dossier OCCT
                        import shutil
                        shutil.move(download_path, occt_exe)
                        print(f"✅ OCCT installé: {occt_exe}")

                    else:
                        raise ValueError("Format de fichier non reconnu (ni ZIP ni EXE)")

                    # Nettoyer le fichier temporaire s'il existe encore
                    if os.path.exists(download_path):
                        os.remove(download_path)

                    print(f"✅ OCCT installé dans: {occt_dir}")

                except Exception as download_error:
                    # Nettoyer en cas d'erreur
                    if os.path.exists(download_path):
                        try:
                            os.remove(download_path)
                        except:
                            pass

                    # Si le téléchargement échoue, proposer le téléchargement manuel
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger OCCT automatiquement:\n\n{str(download_error)}\n\n"
                        f"Veuillez télécharger OCCT manuellement:\n"
                        f"1. Visitez: https://www.ocbase.com\n"
                        f"2. Téléchargez la version portable\n"
                        f"3. Extrayez dans: {occt_dir}"
                    )
                    return

            # Lancer
            if occt_exe and os.path.exists(occt_exe):
                # Lancer sans UAC en utilisant os.startfile (comme double-clic)
                # Cela évite l'erreur 740 (elevation required)
                try:
                    os.startfile(occt_exe)
                    messagebox.showinfo(
                        "OCCT",
                        f"OCCT lancé!\n\n"
                        f"Fonctionnalités:\n"
                        f"• Monitoring en temps réel des températures\n"
                        f"• Test de stabilité CPU/GPU/RAM\n"
                        f"• Détection de surchauffe\n"
                        f"• Graphiques de performance\n\n"
                        f"⚠️ Attention: Les tests de stress chauffent le PC!\n"
                        f"Surveillez les températures pendant les tests.\n\n"
                        f"Emplacement: {occt_dir}"
                    )
                except OSError as e:
                    # Si os.startfile échoue, essayer avec subprocess et shell=True
                    subprocess.Popen(f'start "" "{occt_exe}"', shell=True)
                    messagebox.showinfo("OCCT", "OCCT lancé!")
            else:
                raise FileNotFoundError("Exécutable OCCT introuvable après extraction")

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer OCCT:\n\n{str(e)}\n\n"
                f"Vous pouvez le télécharger manuellement depuis:\n"
                f"https://www.ocbase.com"
            )

    def _test_battery(self):
        """Tester la batterie (pour portables) avec détails avancés"""
        from tkinter import messagebox
        import subprocess
        import os

        # Essayer de lancer l'outil externe Battery Tester s'il existe
        try:
            tools_dir = get_local_software_folder()
            battery_tester_path = os.path.join(tools_dir, "Ordi Plus - Battery Tester.exe")

            if os.path.exists(battery_tester_path):
                subprocess.Popen([battery_tester_path], shell=True)
                messagebox.showinfo(
                    "Test Batterie",
                    "✅ Outil Battery Tester lancé!\n\n"
                    f"Emplacement: {battery_tester_path}"
                )
                return
        except Exception as e:
            print(f"Erreur lancement Battery Tester: {e}")
            # Continuer avec la méthode interne

        # Méthode interne (fallback)
        try:
            if PSUTIL_AVAILABLE:
                battery = psutil.sensors_battery()

                if battery is None:
                    messagebox.showinfo(
                        "Batterie",
                        "❌ Aucune batterie détectée.\n\n"
                        "Ce PC est probablement un ordinateur de bureau."
                    )
                    return

                percent = battery.percent
                plugged = battery.power_plugged
                time_left = battery.secsleft

                # Calculer le temps restant
                if time_left == psutil.POWER_TIME_UNLIMITED:
                    time_str = "Illimité (branché)"
                elif time_left == psutil.POWER_TIME_UNKNOWN:
                    time_str = "Inconnu"
                else:
                    hours = time_left // 3600
                    minutes = (time_left % 3600) // 60
                    time_str = f"{hours}h {minutes}min"

                # Obtenir détails avancés via WMI
                battery_info = ""
                try:
                    import wmi
                    w = wmi.WMI()

                    for bat in w.Win32_Battery():
                        design_capacity = getattr(bat, 'DesignCapacity', None)
                        full_charge_capacity = getattr(bat, 'FullChargeCapacity', None)
                        design_voltage = getattr(bat, 'DesignVoltage', None)
                        battery_status = getattr(bat, 'BatteryStatus', None)
                        chemistry = getattr(bat, 'Chemistry', None)
                        device_id = getattr(bat, 'DeviceID', 'N/A')

                        # Calculer santé de la batterie
                        if design_capacity and full_charge_capacity:
                            health_percent = (full_charge_capacity / design_capacity) * 100

                            # Calculer capacité en mAh
                            design_mah = None
                            current_mah = None

                            # Essayer de récupérer le voltage (plusieurs méthodes)
                            voltage_v = None
                            if design_voltage and design_voltage > 0:
                                # Voltage en mV, convertir en V
                                voltage_v = design_voltage / 1000.0

                            # Si pas de voltage, estimer selon le type de batterie
                            # Laptops modernes utilisent généralement 11.1V (3 cellules) ou 14.8V (4 cellules)
                            if not voltage_v or voltage_v == 0:
                                # Estimer selon la capacité (heuristique)
                                if design_capacity < 35000:
                                    voltage_v = 11.1  # Batterie 3 cellules
                                elif design_capacity < 50000:
                                    voltage_v = 14.4  # Batterie 4 cellules
                                else:
                                    voltage_v = 14.8  # Batterie haute capacité

                            if voltage_v and voltage_v > 0:
                                # Convertir mWh en mAh: mAh = mWh / V
                                design_mah = design_capacity / voltage_v
                                current_mah = full_charge_capacity / voltage_v

                            battery_info += f"\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                            battery_info += f"\n📊 SANTÉ BATTERIE: {health_percent:.1f}%"
                            battery_info += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

                            # Toujours afficher en mAh (estimé si voltage inconnu)
                            if design_mah and current_mah:
                                battery_info += f"\n⚡ Capacité ORIGINALE: {design_mah:.0f} mAh ({design_capacity} mWh)"
                                battery_info += f"\n🔋 Capacité ACTUELLE: {current_mah:.0f} mAh ({full_charge_capacity} mWh)"
                                battery_info += f"\n📉 Usure: {design_mah - current_mah:.0f} mAh ({100 - health_percent:.1f}%)"
                                if not design_voltage or design_voltage == 0:
                                    battery_info += f"\n⚠️ Voltage estimé: {voltage_v:.1f}V (capacités mAh approximatives)"
                                else:
                                    battery_info += f"\n⚡ Voltage: {voltage_v:.1f}V"
                            else:
                                battery_info += f"\n⚡ Capacité ORIGINALE: {design_capacity} mWh"
                                battery_info += f"\n🔋 Capacité ACTUELLE: {full_charge_capacity} mWh"
                                battery_info += f"\n📉 Usure: {design_capacity - full_charge_capacity} mWh ({100 - health_percent:.1f}%)"

                        if device_id:
                            battery_info += f"\n🔖 Référence: {device_id}"

                        # Type de chimie
                        chemistry_types = {
                            1: "Autre", 2: "Inconnu", 3: "Lead Acid",
                            4: "Nickel Cadmium", 5: "Nickel Metal Hydride",
                            6: "Lithium-ion", 7: "Zinc air", 8: "Lithium Polymer"
                        }
                        if chemistry in chemistry_types:
                            battery_info += f"\n⚡ Type: {chemistry_types[chemistry]}"

                        break  # Une seule batterie normalement
                except:
                    pass  # Si WMI échoue, continuer sans détails avancés

                # Déterminer le statut
                if percent > 80:
                    status_emoji = "🟢"
                    health = "Excellente"
                elif percent > 50:
                    status_emoji = "🟡"
                    health = "Bonne"
                elif percent > 20:
                    status_emoji = "🟠"
                    health = "Faible"
                else:
                    status_emoji = "🔴"
                    health = "Critique"

                plugged_str = "✅ Branché" if plugged else "🔋 Sur batterie"

                messagebox.showinfo(
                    "État de la Batterie",
                    f"{status_emoji} Niveau actuel: {percent}%\n"
                    f"État de charge: {health}\n"
                    f"Alimentation: {plugged_str}\n"
                    f"Autonomie restante: {time_str}"
                    f"{battery_info}\n\n"
                    f"💡 Recommandation:\n"
                    f"{'✓ Niveau optimal' if percent > 50 else '⚠️ Pensez à recharger'}"
                )
            else:
                messagebox.showwarning(
                    "Test Batterie",
                    "Le module psutil est requis pour tester la batterie.\n\n"
                    "Installation: pip install psutil"
                )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Erreur lors du test de batterie:\n\n{str(e)}"
            )

    def _test_battery_nitrite(self):
        """Test batterie NiTrite avec fenêtre dédiée et informations complètes"""
        from tkinter import messagebox

        try:
            if not PSUTIL_AVAILABLE:
                messagebox.showwarning(
                    "Test Batterie NiTrite",
                    "Le module psutil est requis pour tester la batterie.\n\n"
                    "Installation: pip install psutil"
                )
                return

            battery = psutil.sensors_battery()

            if battery is None:
                messagebox.showinfo(
                    "Test Batterie NiTrite",
                    "❌ Aucune batterie détectée.\n\n"
                    "Ce PC est probablement un ordinateur de bureau."
                )
                return

            # Créer fenêtre dédiée
            battery_window = ctk.CTkToplevel(self)
            battery_window.title("🔋 Test Batterie NiTrite - Diagnostic Complet")
            battery_window.geometry("700x600")
            battery_window.resizable(False, False)

            # Centrer la fenêtre
            battery_window.update_idletasks()
            x = (battery_window.winfo_screenwidth() // 2) - (350)
            y = (battery_window.winfo_screenheight() // 2) - (300)
            battery_window.geometry(f"700x600+{x}+{y}")

            # Contenu scrollable
            scroll_frame = ctk.CTkScrollableFrame(
                battery_window,
                fg_color=DesignTokens.BG_PRIMARY
            )
            scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            # Header
            header = ctk.CTkLabel(
                scroll_frame,
                text="🔋 Diagnostic Complet de la Batterie",
                font=(DesignTokens.FONT_FAMILY, 24, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY
            )
            header.pack(pady=(0, 20))

            # Informations de base via psutil
            percent = battery.percent
            plugged = battery.power_plugged
            time_left = battery.secsleft

            # Statut de charge
            if percent > 80:
                status_emoji = "🟢"
                health_status = "Excellente"
                status_color = "#4CAF50"
            elif percent > 50:
                status_emoji = "🟡"
                health_status = "Bonne"
                status_color = "#FFA500"
            elif percent > 20:
                status_emoji = "🟠"
                health_status = "Faible"
                status_color = "#FF6B35"
            else:
                status_emoji = "🔴"
                health_status = "Critique"
                status_color = "#F44336"

            # Carte statut actuel
            status_card = ModernCard(scroll_frame)
            status_card.pack(fill=tk.X, pady=10)

            status_title = ctk.CTkLabel(
                status_card,
                text=f"{status_emoji} STATUT ACTUEL",
                font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                text_color=status_color
            )
            status_title.pack(pady=10)

            # Niveau de charge
            charge_label = ctk.CTkLabel(
                status_card,
                text=f"Niveau de charge: {percent}%",
                font=(DesignTokens.FONT_FAMILY, 16),
                text_color=DesignTokens.TEXT_PRIMARY
            )
            charge_label.pack(pady=5)

            # Barre de progression
            progress = ctk.CTkProgressBar(
                status_card,
                width=600,
                height=25,
                corner_radius=12,
                progress_color=status_color
            )
            progress.pack(pady=10)
            progress.set(percent / 100)

            # État d'alimentation
            plugged_text = "✅ Branché - En charge" if plugged else "🔋 Sur batterie"
            plugged_label = ctk.CTkLabel(
                status_card,
                text=plugged_text,
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color=DesignTokens.TEXT_SECONDARY
            )
            plugged_label.pack(pady=5)

            # Autonomie restante
            if time_left == psutil.POWER_TIME_UNLIMITED:
                time_str = "Illimité (branché)"
            elif time_left == psutil.POWER_TIME_UNKNOWN:
                time_str = "Inconnu"
            else:
                hours = time_left // 3600
                minutes = (time_left % 3600) // 60
                time_str = f"{hours}h {minutes}min"

            time_label = ctk.CTkLabel(
                status_card,
                text=f"Autonomie restante: {time_str}",
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color=DesignTokens.TEXT_SECONDARY
            )
            time_label.pack(pady=5)

            # Informations avancées via WMI
            try:
                import wmi
                w = wmi.WMI()

                for bat in w.Win32_Battery():
                    # Carte détails techniques
                    details_card = ModernCard(scroll_frame)
                    details_card.pack(fill=tk.X, pady=10)

                    details_title = ctk.CTkLabel(
                        details_card,
                        text="⚡ DÉTAILS TECHNIQUES",
                        font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                        text_color=DesignTokens.TEXT_PRIMARY
                    )
                    details_title.pack(pady=10)

                    # Récupérer les informations
                    design_capacity = getattr(bat, 'DesignCapacity', None)
                    full_charge_capacity = getattr(bat, 'FullChargeCapacity', None)
                    design_voltage = getattr(bat, 'DesignVoltage', None)
                    device_id = getattr(bat, 'DeviceID', 'N/A')
                    chemistry = getattr(bat, 'Chemistry', None)

                    # Calcul de la santé
                    if design_capacity and full_charge_capacity:
                        health_percent = (full_charge_capacity / design_capacity) * 100

                        # Déterminer voltage
                        voltage_v = None
                        if design_voltage and design_voltage > 0:
                            voltage_v = design_voltage / 1000.0
                        else:
                            # Estimation selon capacité
                            if design_capacity < 35000:
                                voltage_v = 11.1
                            elif design_capacity < 50000:
                                voltage_v = 14.4
                            else:
                                voltage_v = 14.8

                        # Convertir en mAh
                        design_mah = design_capacity / voltage_v if voltage_v else 0
                        current_mah = full_charge_capacity / voltage_v if voltage_v else 0

                        # Santé de la batterie
                        health_frame = ctk.CTkFrame(details_card, fg_color="transparent")
                        health_frame.pack(fill=tk.X, padx=20, pady=10)

                        health_label = ctk.CTkLabel(
                            health_frame,
                            text=f"État de santé: {health_percent:.1f}%",
                            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
                            text_color="#4CAF50" if health_percent > 80 else "#FFA500" if health_percent > 60 else "#F44336"
                        )
                        health_label.pack(anchor="w")

                        # Capacité originale
                        design_cap_label = ctk.CTkLabel(
                            health_frame,
                            text=f"⚡ Capacité ORIGINALE: {design_capacity} mWh ({design_mah:.0f} mAh)",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        design_cap_label.pack(anchor="w", pady=2)

                        # Capacité actuelle
                        current_cap_label = ctk.CTkLabel(
                            health_frame,
                            text=f"🔋 Capacité ACTUELLE: {full_charge_capacity} mWh ({current_mah:.0f} mAh)",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        current_cap_label.pack(anchor="w", pady=2)

                        # Usure
                        wear_mah = design_mah - current_mah
                        wear_mwh = design_capacity - full_charge_capacity
                        wear_percent = 100 - health_percent
                        wear_label = ctk.CTkLabel(
                            health_frame,
                            text=f"📉 Usure: {wear_mwh} mWh ({wear_mah:.0f} mAh) - {wear_percent:.1f}%",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.WARNING if wear_percent > 20 else DesignTokens.TEXT_SECONDARY
                        )
                        wear_label.pack(anchor="w", pady=2)

                        # Voltage
                        voltage_label = ctk.CTkLabel(
                            health_frame,
                            text=f"⚡ Voltage: {voltage_v:.2f}V" + (" (estimé)" if not design_voltage or design_voltage == 0 else ""),
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        voltage_label.pack(anchor="w", pady=2)

                        # Ampérage (calculé)
                        if voltage_v and current_mah:
                            amperage_a = current_mah / 1000
                            amperage_label = ctk.CTkLabel(
                                health_frame,
                                text=f"🔌 Ampérage: {amperage_a:.2f}Ah",
                                font=(DesignTokens.FONT_FAMILY, 14),
                                text_color=DesignTokens.TEXT_SECONDARY
                            )
                            amperage_label.pack(anchor="w", pady=2)

                    # Numéro de série / Device ID
                    if device_id:
                        serial_label = ctk.CTkLabel(
                            details_card,
                            text=f"🔖 Numéro de série: {device_id}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        serial_label.pack(anchor="w", padx=20, pady=2)

                    # Type de chimie
                    chemistry_types = {
                        1: "Autre", 2: "Inconnu", 3: "Lead Acid",
                        4: "Nickel Cadmium", 5: "Nickel Metal Hydride",
                        6: "Lithium-ion", 7: "Zinc air", 8: "Lithium Polymer"
                    }
                    if chemistry in chemistry_types:
                        chemistry_label = ctk.CTkLabel(
                            details_card,
                            text=f"⚗️ Type de batterie: {chemistry_types[chemistry]}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        chemistry_label.pack(anchor="w", padx=20, pady=2)

                    # Carte informations supplémentaires
                    extra_card = ModernCard(scroll_frame)
                    extra_card.pack(fill=tk.X, pady=10)

                    extra_title = ctk.CTkLabel(
                        extra_card,
                        text="📊 INFORMATIONS SUPPLÉMENTAIRES",
                        font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                        text_color=DesignTokens.TEXT_PRIMARY
                    )
                    extra_title.pack(pady=10)

                    extra_frame = ctk.CTkFrame(extra_card, fg_color="transparent")
                    extra_frame.pack(fill=tk.X, padx=20, pady=10)

                    # Nom et fabricant
                    bat_name = getattr(bat, 'Name', None)
                    bat_manufacturer = getattr(bat, 'Manufacturer', None)

                    if bat_name:
                        name_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"🏷️ Nom: {bat_name}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        name_label.pack(anchor="w", pady=2)

                    if bat_manufacturer:
                        manu_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"🏭 Fabricant: {bat_manufacturer}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        manu_label.pack(anchor="w", pady=2)

                    # Statut de la batterie
                    battery_status = getattr(bat, 'BatteryStatus', None)
                    status_map = {
                        1: "🔋 Autre",
                        2: "❓ Inconnu",
                        3: "✅ Complètement chargée",
                        4: "⚡ Charge normale",
                        5: "⚡ Charge rapide",
                        6: "⚡ Charge d'entretien",
                        7: "🔴 Critique - Charge faible",
                        8: "⚠️ En charge et critique",
                        9: "⚠️ En charge et faible",
                        10: "⚠️ En charge et élevée",
                        11: "⬇️ Décharge",
                        12: "❌ Batterie indisponible"
                    }
                    if battery_status in status_map:
                        status_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"Statut: {status_map[battery_status]}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        status_label.pack(anchor="w", pady=2)

                    # État du système
                    status_info = getattr(bat, 'Status', None)
                    if status_info:
                        sys_status_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"État système: {status_info}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        sys_status_label.pack(anchor="w", pady=2)

                    # Temps de charge restant
                    time_to_full = getattr(bat, 'TimeToFullCharge', None)
                    if time_to_full and time_to_full != 71582788:  # Valeur spéciale = non applicable
                        hours_to_full = time_to_full // 60
                        mins_to_full = time_to_full % 60
                        charge_time_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"⏱️ Temps jusqu'à charge complète: {hours_to_full}h {mins_to_full}min",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        charge_time_label.pack(anchor="w", pady=2)

                    # Durée de vie estimée
                    estimated_runtime = getattr(bat, 'EstimatedRunTime', None)
                    if estimated_runtime and estimated_runtime != 71582788:  # Valeur spéciale = non applicable
                        est_hours = estimated_runtime // 60
                        est_mins = estimated_runtime % 60
                        runtime_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"⏰ Autonomie estimée: {est_hours}h {est_mins}min",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        runtime_label.pack(anchor="w", pady=2)

                    # Nombre de cycles (si disponible)
                    cycle_count = getattr(bat, 'CycleCount', None)
                    if cycle_count:
                        cycle_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"🔄 Cycles de charge: {cycle_count}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        cycle_label.pack(anchor="w", pady=2)

                    # Tension actuelle
                    current_voltage = getattr(bat, 'Voltage', None)
                    if current_voltage:
                        voltage_current_v = current_voltage / 1000.0
                        voltage_current_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"⚡ Tension actuelle: {voltage_current_v:.2f}V",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        voltage_current_label.pack(anchor="w", pady=2)

                    # Taux de décharge
                    discharge_rate = getattr(bat, 'EstimatedChargeRemaining', None)
                    if discharge_rate is not None:
                        discharge_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"📉 Charge restante estimée: {discharge_rate}%",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        discharge_label.pack(anchor="w", pady=2)

                    # Description
                    description = getattr(bat, 'Description', None)
                    if description and description != bat_name:
                        desc_label = ctk.CTkLabel(
                            extra_frame,
                            text=f"📝 Description: {description}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        desc_label.pack(anchor="w", pady=2)

                    # Carte informations avancées supplémentaires
                    advanced_card = ModernCard(scroll_frame)
                    advanced_card.pack(fill=tk.X, pady=10)

                    advanced_title = ctk.CTkLabel(
                        advanced_card,
                        text="⚡ INFORMATIONS AVANCÉES",
                        font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                        text_color=DesignTokens.TEXT_PRIMARY
                    )
                    advanced_title.pack(pady=10)

                    advanced_frame = ctk.CTkFrame(advanced_card, fg_color="transparent")
                    advanced_frame.pack(fill=tk.X, padx=20, pady=10)

                    # Taux de charge/décharge (si disponible)
                    charge_rate = getattr(bat, 'ChargeRate', None)
                    discharge_rate = getattr(bat, 'DischargeRate', None)

                    if charge_rate and charge_rate != 0:
                        rate_w = charge_rate / 1000.0  # Convertir en watts
                        rate_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"⚡ Taux de charge: {rate_w:.2f}W",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        rate_label.pack(anchor="w", pady=2)

                    if discharge_rate and discharge_rate != 0:
                        drate_w = discharge_rate / 1000.0  # Convertir en watts
                        drate_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"📉 Taux de décharge: {drate_w:.2f}W",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        drate_label.pack(anchor="w", pady=2)

                    # Expected Life
                    expected_life = getattr(bat, 'ExpectedLife', None)
                    if expected_life:
                        life_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"⏳ Durée de vie estimée: {expected_life} minutes",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        life_label.pack(anchor="w", pady=2)

                    # Max Recharge Time
                    max_recharge = getattr(bat, 'MaxRechargeTime', None)
                    if max_recharge and max_recharge != 71582788:
                        hours_max = max_recharge // 60
                        mins_max = max_recharge % 60
                        recharge_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"⏱️ Temps de recharge max: {hours_max}h {mins_max}min",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        recharge_label.pack(anchor="w", pady=2)

                    # Time on Battery
                    time_on_battery = getattr(bat, 'TimeOnBattery', None)
                    if time_on_battery and time_on_battery != 71582788:
                        hours_on = time_on_battery // 60
                        mins_on = time_on_battery % 60
                        time_on_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"🔋 Temps sur batterie: {hours_on}h {mins_on}min",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_PRIMARY
                        )
                        time_on_label.pack(anchor="w", pady=2)

                    # Smart Battery Version
                    smart_battery_ver = getattr(bat, 'SmartBatteryVersion', None)
                    if smart_battery_ver:
                        smart_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"🧠 Smart Battery Version: {smart_battery_ver}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        smart_label.pack(anchor="w", pady=2)

                    # Availability
                    availability = getattr(bat, 'Availability', None)
                    availability_map = {
                        1: "Autre", 2: "Inconnue", 3: "En cours d'exécution/Pleine puissance",
                        4: "Avertissement", 5: "En test", 6: "Non applicable",
                        7: "Hors tension", 8: "Hors ligne", 9: "Hors service",
                        10: "Dégradé", 11: "Non installé", 12: "Erreur d'installation",
                        13: "Économie d'énergie - Inconnue", 14: "Économie d'énergie - Mode faible consommation",
                        15: "Économie d'énergie - Veille", 16: "Cycle d'alimentation",
                        17: "Économie d'énergie - Avertissement"
                    }
                    if availability and availability in availability_map:
                        avail_label = ctk.CTkLabel(
                            advanced_frame,
                            text=f"📡 Disponibilité: {availability_map[availability]}",
                            font=(DesignTokens.FONT_FAMILY, 14),
                            text_color=DesignTokens.TEXT_SECONDARY
                        )
                        avail_label.pack(anchor="w", pady=2)

                    break  # Une seule batterie normalement

                # Ajouter rapport PowerCfg
                try:
                    import subprocess
                    import tempfile
                    import os

                    powercfg_card = ModernCard(scroll_frame)
                    powercfg_card.pack(fill=tk.X, pady=10)

                    powercfg_title = ctk.CTkLabel(
                        powercfg_card,
                        text="📋 RAPPORT POWERCFG (Windows)",
                        font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                        text_color=DesignTokens.TEXT_PRIMARY
                    )
                    powercfg_title.pack(pady=10)

                    powercfg_frame = ctk.CTkFrame(powercfg_card, fg_color="transparent")
                    powercfg_frame.pack(fill=tk.X, padx=20, pady=10)

                    # Générer rapport batterie avec PowerCfg
                    temp_report = os.path.join(tempfile.gettempdir(), "battery-report.xml")

                    # Exécuter powercfg /batteryreport
                    result = subprocess.run(
                        ['powercfg', '/batteryreport', '/output', temp_report, '/xml'],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )

                    if result.returncode == 0 and os.path.exists(temp_report):
                        # Lire le rapport XML
                        import xml.etree.ElementTree as ET
                        tree = ET.parse(temp_report)
                        root = tree.getroot()

                        # Extraire informations du rapport
                        design_capacity_elem = root.find('.//DesignCapacity')
                        full_capacity_elem = root.find('.//FullChargeCapacity')
                        cycle_count_elem = root.find('.//CycleCount')

                        if design_capacity_elem is not None:
                            design_mwh = int(design_capacity_elem.text)
                            design_label = ctk.CTkLabel(
                                powercfg_frame,
                                text=f"⚙️ Capacité design (PowerCfg): {design_mwh} mWh",
                                font=(DesignTokens.FONT_FAMILY, 14),
                                text_color=DesignTokens.TEXT_PRIMARY
                            )
                            design_label.pack(anchor="w", pady=2)

                        if full_capacity_elem is not None:
                            full_mwh = int(full_capacity_elem.text)
                            full_label = ctk.CTkLabel(
                                powercfg_frame,
                                text=f"🔋 Capacité complète (PowerCfg): {full_mwh} mWh",
                                font=(DesignTokens.FONT_FAMILY, 14),
                                text_color=DesignTokens.TEXT_PRIMARY
                            )
                            full_label.pack(anchor="w", pady=2)

                        if cycle_count_elem is not None:
                            cycles = int(cycle_count_elem.text)
                            cycle_label = ctk.CTkLabel(
                                powercfg_frame,
                                text=f"🔄 Cycles (PowerCfg): {cycles}",
                                font=(DesignTokens.FONT_FAMILY, 14),
                                text_color=DesignTokens.TEXT_PRIMARY
                            )
                            cycle_label.pack(anchor="w", pady=2)

                        # Bouton pour ouvrir le rapport HTML complet
                        def open_full_report():
                            html_report = os.path.join(tempfile.gettempdir(), "battery-report.html")
                            subprocess.run(['powercfg', '/batteryreport', '/output', html_report],
                                         capture_output=True)
                            if os.path.exists(html_report):
                                os.startfile(html_report)

                        ModernButton(
                            powercfg_card,
                            text="📄 Ouvrir Rapport Complet",
                            variant="outlined",
                            size="sm",
                            command=open_full_report
                        ).pack(pady=10)

                        # Nettoyer
                        try:
                            os.remove(temp_report)
                        except:
                            pass
                    else:
                        error_label = ctk.CTkLabel(
                            powercfg_frame,
                            text="⚠️ Impossible de générer le rapport PowerCfg",
                            font=(DesignTokens.FONT_FAMILY, 12),
                            text_color=DesignTokens.WARNING
                        )
                        error_label.pack(pady=10)

                except Exception as e:
                    error_label = ctk.CTkLabel(
                        scroll_frame,
                        text=f"⚠️ Erreur PowerCfg: {str(e)[:60]}",
                        font=(DesignTokens.FONT_FAMILY, 12),
                        text_color=DesignTokens.WARNING
                    )
                    error_label.pack(pady=5)

            except ImportError:
                info_label = ctk.CTkLabel(
                    scroll_frame,
                    text="⚠️ Module WMI non disponible - Informations avancées limitées",
                    font=(DesignTokens.FONT_FAMILY, 12),
                    text_color=DesignTokens.WARNING
                )
                info_label.pack(pady=10)
            except Exception as e:
                error_label = ctk.CTkLabel(
                    scroll_frame,
                    text=f"⚠️ Impossible de récupérer les détails avancés: {str(e)[:50]}",
                    font=(DesignTokens.FONT_FAMILY, 12),
                    text_color=DesignTokens.WARNING
                )
                error_label.pack(pady=10)

            # Recommandations
            recommendations_card = ModernCard(scroll_frame)
            recommendations_card.pack(fill=tk.X, pady=10)

            recommendations_title = ctk.CTkLabel(
                recommendations_card,
                text="💡 RECOMMANDATIONS",
                font=(DesignTokens.FONT_FAMILY, 18, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY
            )
            recommendations_title.pack(pady=10)

            if percent < 20:
                rec_text = "⚠️ Niveau critique - Branchez immédiatement votre ordinateur"
            elif percent < 50:
                rec_text = "🔌 Niveau faible - Pensez à recharger prochainement"
            else:
                rec_text = "✅ Niveau optimal - Batterie en bon état"

            rec_label = ctk.CTkLabel(
                recommendations_card,
                text=rec_text,
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color=DesignTokens.TEXT_SECONDARY
            )
            rec_label.pack(padx=20, pady=5)

            # Bouton fermer
            close_btn = ModernButton(
                battery_window,
                text="Fermer",
                variant="filled",
                command=battery_window.destroy
            )
            close_btn.pack(pady=10)

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Erreur lors du test de batterie NiTrite:\n\n{str(e)}"
            )

    def _launch_autoruns(self):
        """Lancer Autoruns (Sysinternals)"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Créer dossier portable_tools s'il n'existe pas
            tools_dir = os.path.join(os.path.expanduser("~"), "Desktop", "NiTriTe_Tools")
            os.makedirs(tools_dir, exist_ok=True)

            autoruns_dir = os.path.join(tools_dir, "Autoruns")
            autoruns_exe = os.path.join(autoruns_dir, "Autoruns64.exe")

            # Vérifier si déjà téléchargé
            if not os.path.exists(autoruns_exe):
                response = messagebox.askyesno(
                    "Télécharger Autoruns",
                    "Autoruns n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~2 MB, téléchargement unique)\n\n"
                    "Autoruns est un outil Microsoft Sysinternals\n"
                    "pour gérer les programmes au démarrage.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL Autoruns (Microsoft Sysinternals)
                url = "https://download.sysinternals.com/files/Autoruns.zip"
                zip_path = os.path.join(tools_dir, "autoruns.zip")

                # Télécharger
                print(f"📥 Téléchargement d'Autoruns...")
                urllib.request.urlretrieve(url, zip_path)

                # Extraire
                print(f"📦 Extraction...")
                os.makedirs(autoruns_dir, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(autoruns_dir)

                # Nettoyer
                os.remove(zip_path)
                print(f"✅ Autoruns installé dans: {autoruns_dir}")

            # Lancer
            if os.path.exists(autoruns_exe):
                subprocess.Popen([autoruns_exe], shell=True)
                messagebox.showinfo(
                    "Autoruns",
                    f"Autoruns lancé!\n\n"
                    f"Cet outil vous permet de:\n"
                    f"• Voir tous les programmes au démarrage\n"
                    f"• Désactiver les logiciels indésirables\n"
                    f"• Améliorer les performances de démarrage\n\n"
                    f"Emplacement: {autoruns_dir}"
                )
            else:
                raise FileNotFoundError("Autoruns64.exe introuvable après extraction")

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer Autoruns:\n\n{str(e)}\n\n"
                f"Vous pouvez le télécharger manuellement depuis:\n"
                f"https://docs.microsoft.com/sysinternals/downloads/autoruns"
            )

    def _launch_malwarebytes(self):
        """Ouvrir la page de téléchargement Malwarebytes"""
        import webbrowser
        from tkinter import messagebox

        try:
            response = messagebox.askyesno(
                "Télécharger Malwarebytes",
                "Malwarebytes est un outil anti-malware professionnel.\n\n"
                "Cette action va ouvrir la page de téléchargement officielle\n"
                "de Malwarebytes dans votre navigateur.\n\n"
                "Voulez-vous continuer?",
                icon='question'
            )

            if not response:
                return

            # Ouvrir la page de téléchargement dans le navigateur
            webbrowser.open("https://www.malwarebytes.com/fr/mwb-download")

            messagebox.showinfo(
                "Page ouverte",
                "La page de téléchargement Malwarebytes a été ouverte\n"
                "dans votre navigateur.\n\n"
                "Téléchargez et installez Malwarebytes depuis cette page."
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir la page de téléchargement:\n\n{str(e)}\n\n"
                f"Visitez manuellement:\n"
                f"https://www.malwarebytes.com/fr/mwb-download"
            )

    def _launch_spybot(self):
        """Lancer Spybot Search & Destroy Portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()

            # Chercher d'abord dans SpybotPortable (PortableApps)
            spybot_portable_dir = os.path.join(tools_dir, "SpybotPortable")
            spybot_portable_exe = os.path.join(spybot_portable_dir, "SpybotPortable.exe")

            if os.path.exists(spybot_portable_exe):
                os.startfile(spybot_portable_exe)
                messagebox.showinfo(
                    "Spybot",
                    f"Spybot Search & Destroy lancé!\n\nEmplacement: {spybot_portable_exe}"
                )
                return

            # Sinon, chercher dans dossier classique Spybot
            spybot_dir = os.path.join(tools_dir, "Spybot")
            os.makedirs(spybot_dir, exist_ok=True)

            # Chercher l'exécutable Spybot
            spybot_exe = None
            if os.path.exists(spybot_dir):
                for file in os.listdir(spybot_dir):
                    if file.lower().endswith('.exe') and 'spybot' in file.lower():
                        spybot_exe = os.path.join(spybot_dir, file)
                        break

            # Si pas trouvé, télécharger
            if not spybot_exe or not os.path.exists(spybot_exe):
                response = messagebox.askyesno(
                    "Télécharger Spybot",
                    "Spybot Search & Destroy n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~50 MB, téléchargement unique)\n\n"
                    "Spybot détecte et élimine les malwares.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques minutes..."
                )

                # URL Spybot (version portable depuis PortableApps)
                url = "https://portableapps.com/redirect/?a=SpybotSD&s=s&d=pa&f=SpybotSDPortable_2.9.82.0.paf.exe"
                spybot_installer = os.path.join(tools_dir, "SpybotPortable.exe")

                # Télécharger
                print(f"📥 Téléchargement de Spybot...")
                try:
                    urllib.request.urlretrieve(url, spybot_installer)
                    print(f"✅ Spybot téléchargé dans: {tools_dir}")

                    # L'installer portable s'auto-extrait
                    messagebox.showinfo(
                        "Installation",
                        "Spybot va s'installer.\n\n"
                        "Choisissez comme destination:\n"
                        f"{spybot_dir}\n\n"
                        "Puis cliquez à nouveau sur le bouton Spybot."
                    )
                    os.startfile(spybot_installer)
                    return

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger Spybot:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://www.safer-networking.org/download/"
                    )
                    return

            # Lancer
            os.startfile(spybot_exe)
            messagebox.showinfo(
                "Spybot",
                f"Spybot Search & Destroy lancé!\n\n"
                f"Emplacement: {spybot_exe}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer Spybot:\n\n{str(e)}\n\n"
                f"Téléchargez-le depuis:\n"
                f"https://www.safer-networking.org"
            )

    def _launch_adwcleaner(self):
        """Lancer AdwCleaner Portable"""
        import subprocess
        import os
        import urllib.request
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()
            adw_dir = os.path.join(tools_dir, "AdwCleaner")
            os.makedirs(adw_dir, exist_ok=True)
            adw_exe = os.path.join(adw_dir, "adwcleaner.exe")

            # Vérifier si déjà téléchargé
            if not os.path.exists(adw_exe):
                response = messagebox.askyesno(
                    "Télécharger AdwCleaner",
                    "AdwCleaner n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~8 MB, téléchargement unique)\n\n"
                    "AdwCleaner supprime les adwares et PUPs.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL AdwCleaner (Malwarebytes)
                url = "https://adwcleaner.malwarebytes.com/adwcleaner?channel=release"
                os.makedirs(adw_dir, exist_ok=True)

                # Télécharger
                print(f"📥 Téléchargement d'AdwCleaner...")
                urllib.request.urlretrieve(url, adw_exe)
                print(f"✅ AdwCleaner installé dans: {adw_dir}")

            # Lancer
            if os.path.exists(adw_exe):
                os.startfile(adw_exe)
                messagebox.showinfo(
                    "AdwCleaner",
                    f"AdwCleaner lancé!\n\n"
                    f"Emplacement: {adw_dir}"
                )
            else:
                raise FileNotFoundError("AdwCleaner introuvable")

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer AdwCleaner:\n\n{str(e)}\n\n"
                f"Vous pouvez le télécharger manuellement depuis:\n"
                f"https://www.malwarebytes.com/adwcleaner"
            )

    def _launch_wisediskcleaner(self):
        """Lancer Wise Disk Cleaner Portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()

            # Chercher d'abord dans WiseDiskCleanerPortable (PortableApps)
            wise_portable_dir = os.path.join(tools_dir, "WiseDiskCleanerPortable")
            wise_portable_exe = os.path.join(wise_portable_dir, "WiseDiskCleanerPortable.exe")

            if os.path.exists(wise_portable_exe):
                os.startfile(wise_portable_exe)
                messagebox.showinfo(
                    "Wise Disk Cleaner",
                    f"Wise Disk Cleaner lancé!\n\nEmplacement: {wise_portable_exe}"
                )
                return

            # Sinon, chercher dans dossier classique WiseDiskCleaner
            wise_dir = os.path.join(tools_dir, "WiseDiskCleaner")
            os.makedirs(wise_dir, exist_ok=True)

            # Chercher l'exécutable Wise Disk Cleaner
            wise_exe = None
            if os.path.exists(wise_dir):
                for file in os.listdir(wise_dir):
                    if file.lower().endswith('.exe') and 'wise' in file.lower():
                        wise_exe = os.path.join(wise_dir, file)
                        break

            # Si pas trouvé, télécharger
            if not wise_exe or not os.path.exists(wise_exe):
                response = messagebox.askyesno(
                    "Télécharger Wise Disk Cleaner",
                    "Wise Disk Cleaner n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~5 MB, téléchargement unique)\n\n"
                    "Wise Disk Cleaner nettoie les fichiers inutiles.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL Wise Disk Cleaner Portable (depuis PortableApps)
                url = "https://portableapps.com/redirect/?a=WiseDiskCleanerPortable&s=s&d=pa&f=WiseDiskCleanerPortable_11.1.5.655.paf.exe"
                wise_installer = os.path.join(tools_dir, "WiseDiskCleanerPortable.exe")

                # Télécharger
                print(f"📥 Téléchargement de Wise Disk Cleaner...")
                try:
                    urllib.request.urlretrieve(url, wise_installer)
                    print(f"✅ Wise Disk Cleaner téléchargé dans: {tools_dir}")

                    # L'installer portable s'auto-extrait
                    messagebox.showinfo(
                        "Installation",
                        "Wise Disk Cleaner va s'installer.\n\n"
                        "Choisissez comme destination:\n"
                        f"{wise_dir}\n\n"
                        "Puis cliquez à nouveau sur le bouton Wise Disk Cleaner."
                    )
                    os.startfile(wise_installer)
                    return

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger Wise Disk Cleaner:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://www.wisecleaner.com/wise-disk-cleaner.html"
                    )
                    return

            # Lancer
            os.startfile(wise_exe)
            messagebox.showinfo(
                "Wise Disk Cleaner",
                f"Wise Disk Cleaner lancé!\n\n"
                f"Emplacement: {wise_exe}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer Wise Disk Cleaner:\n\n{str(e)}\n\n"
                f"Téléchargez-le depuis:\n"
                f"https://www.wisecleaner.com"
            )

    def _launch_portable_tool(self, tool_name, folder_name, file_pattern, description, download_url=None):
        """Template générique pour lancer un outil portable depuis le dossier logiciel"""
        import os
        from tkinter import messagebox

        try:
            tools_dir = get_local_software_folder()
            tool_dir = os.path.join(tools_dir, folder_name)
            os.makedirs(tool_dir, exist_ok=True)

            # Chercher l'exécutable
            tool_exe = None
            if os.path.exists(tool_dir):
                for file in os.listdir(tool_dir):
                    if file.lower().endswith('.exe') and file_pattern.lower() in file.lower():
                        tool_exe = os.path.join(tool_dir, file)
                        break

            if tool_exe and os.path.exists(tool_exe):
                # Lancer l'outil
                os.startfile(tool_exe)
                messagebox.showinfo(
                    tool_name,
                    f"{tool_name} lancé!\n\nEmplacement: {tool_exe}"
                )
            else:
                # Outil non trouvé
                messagebox.showwarning(
                    f"{tool_name} non trouvé",
                    f"{tool_name} n'est pas installé dans le dossier logiciel.\n\n"
                    f"Veuillez placer {tool_name} dans:\n{tool_dir}\n\n"
                    f"{description}"
                )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer {tool_name}:\n\n{str(e)}"
            )

    def _launch_hwmonitor(self):
        """Lancer HWMonitor portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()
            hwm_dir = os.path.join(tools_dir, "HWMonitor")
            os.makedirs(hwm_dir, exist_ok=True)

            # Chercher l'exécutable
            hwm_exe = None
            if os.path.exists(hwm_dir):
                for file in os.listdir(hwm_dir):
                    if file.lower().endswith('.exe') and 'hwmonitor' in file.lower():
                        hwm_exe = os.path.join(hwm_dir, file)
                        break

            # Vérifier si déjà téléchargé
            if not hwm_exe or not os.path.exists(hwm_exe):
                response = messagebox.askyesno(
                    "Télécharger HWMonitor",
                    "HWMonitor n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~2 MB, version portable, téléchargement unique)\n\n"
                    "HWMonitor surveille températures, tensions et vitesses des ventilateurs.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL HWMonitor Portable (lien direct depuis CPUID)
                url = "https://download.cpuid.com/hwmonitor/hwmonitor_1.53.zip"
                zip_path = os.path.join(tools_dir, "hwmonitor.zip")

                # Télécharger
                print(f"📥 Téléchargement de HWMonitor...")
                try:
                    urllib.request.urlretrieve(url, zip_path)

                    # Extraire
                    print(f"📦 Extraction...")
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(hwm_dir)

                    # Nettoyer
                    os.remove(zip_path)
                    print(f"✅ HWMonitor installé dans: {hwm_dir}")

                    # Rechercher l'exécutable après extraction
                    hwm_exe = None
                    for file in os.listdir(hwm_dir):
                        if file.lower().endswith('.exe') and 'hwmonitor' in file.lower():
                            hwm_exe = os.path.join(hwm_dir, file)
                            break

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger HWMonitor:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://www.cpuid.com/softwares/hwmonitor.html\n\n"
                        f"Et placez les fichiers dans:\n{hwm_dir}"
                    )
                    return

            # Lancer
            if hwm_exe and os.path.exists(hwm_exe):
                os.startfile(hwm_exe)
                messagebox.showinfo(
                    "HWMonitor",
                    f"HWMonitor lancé!\n\nEmplacement: {hwm_exe}"
                )
            else:
                messagebox.showwarning(
                    "HWMonitor non trouvé",
                    f"HWMonitor n'est pas installé dans le dossier logiciel.\n\n"
                    f"Veuillez placer HWMonitor portable dans:\n{hwm_dir}\n\n"
                    f"Téléchargeable depuis: https://www.cpuid.com/softwares/hwmonitor.html"
                )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer HWMonitor:\n\n{str(e)}"
            )

    def _launch_hwinfo(self):
        """Lancer HWinfo portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()

            # Chercher d'abord dans HWiNFOPortable (PortableApps)
            hwi_portable_dir = os.path.join(tools_dir, "HWiNFOPortable")
            hwi_portable_exe = os.path.join(hwi_portable_dir, "HWiNFOPortable.exe")

            if os.path.exists(hwi_portable_exe):
                # Lancer la version PortableApps
                os.startfile(hwi_portable_exe)
                messagebox.showinfo(
                    "HWinfo",
                    f"HWinfo lancé!\n\nEmplacement: {hwi_portable_exe}"
                )
                return

            # Sinon, chercher dans HWinfo (dossier classique)
            hwi_dir = os.path.join(tools_dir, "HWinfo")
            os.makedirs(hwi_dir, exist_ok=True)

            # Chercher l'exécutable
            hwi_exe = None
            if os.path.exists(hwi_dir):
                for file in os.listdir(hwi_dir):
                    if file.lower().endswith('.exe') and 'hwinfo' in file.lower() and '64' in file.lower():
                        hwi_exe = os.path.join(hwi_dir, file)
                        break

            # Vérifier si déjà téléchargé
            if not hwi_exe or not os.path.exists(hwi_exe):
                response = messagebox.askyesno(
                    "Télécharger HWinfo",
                    "HWinfo n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~5 MB, version portable, téléchargement unique)\n\n"
                    "HWinfo fournit des informations détaillées sur le matériel système.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL HWinfo Portable (lien direct depuis le site officiel)
                url = "https://www.fosshub.com/HWiNFO.html?dwl=hwi_800.zip"
                zip_path = os.path.join(tools_dir, "hwinfo.zip")

                # Télécharger
                print(f"📥 Téléchargement de HWinfo...")
                try:
                    urllib.request.urlretrieve(url, zip_path)

                    # Extraire
                    print(f"📦 Extraction...")
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(hwi_dir)

                    # Nettoyer
                    os.remove(zip_path)
                    print(f"✅ HWinfo installé dans: {hwi_dir}")

                    # Rechercher l'exécutable après extraction
                    hwi_exe = None
                    for file in os.listdir(hwi_dir):
                        if file.lower().endswith('.exe') and 'hwinfo' in file.lower() and '64' in file.lower():
                            hwi_exe = os.path.join(hwi_dir, file)
                            break

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger HWinfo:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://www.hwinfo.com/download/\n\n"
                        f"Et placez les fichiers dans:\n{hwi_dir}"
                    )
                    return

            # Lancer
            if hwi_exe and os.path.exists(hwi_exe):
                os.startfile(hwi_exe)
                messagebox.showinfo(
                    "HWinfo",
                    f"HWinfo lancé!\n\nEmplacement: {hwi_exe}"
                )
            else:
                messagebox.showwarning(
                    "HWinfo non trouvé",
                    f"HWinfo n'est pas installé dans le dossier logiciel.\n\n"
                    f"Veuillez placer HWinfo portable dans:\n{hwi_dir}\n\n"
                    f"Téléchargeable depuis: https://www.hwinfo.com/download/"
                )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer HWinfo:\n\n{str(e)}"
            )

    def _launch_crystaldiskmark(self):
        """Lancer CrystalDiskMark portable"""
        import subprocess
        import os
        import urllib.request
        import zipfile
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()
            cdm_dir = os.path.join(tools_dir, "CrystalDiskMark")
            os.makedirs(cdm_dir, exist_ok=True)

            # Chercher l'exécutable (nom peut varier)
            cdm_exe = None
            if os.path.exists(cdm_dir):
                for file in os.listdir(cdm_dir):
                    if file.endswith('.exe') and 'DiskMark' in file and '64' in file:
                        cdm_exe = os.path.join(cdm_dir, file)
                        break

            # Vérifier si déjà téléchargé
            if not cdm_exe or not os.path.exists(cdm_exe):
                response = messagebox.askyesno(
                    "Télécharger CrystalDiskMark",
                    "CrystalDiskMark n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~4 MB, version portable, téléchargement unique)\n\n"
                    "CrystalDiskMark teste les performances de lecture/écriture des disques.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL CrystalDiskMark Portable (lien direct depuis le site officiel)
                url = "https://sourceforge.net/projects/crystaldiskmark/files/latest/download"
                zip_path = os.path.join(tools_dir, "cdm.zip")

                # Télécharger
                print(f"📥 Téléchargement de CrystalDiskMark...")
                try:
                    urllib.request.urlretrieve(url, zip_path)

                    # Extraire
                    print(f"📦 Extraction...")
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(cdm_dir)

                    # Nettoyer
                    os.remove(zip_path)
                    print(f"✅ CrystalDiskMark installé dans: {cdm_dir}")

                    # Rechercher l'exécutable après extraction
                    cdm_exe = None
                    for file in os.listdir(cdm_dir):
                        if file.endswith('.exe') and 'DiskMark' in file and '64' in file:
                            cdm_exe = os.path.join(cdm_dir, file)
                            break

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger CrystalDiskMark:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://crystalmark.info/en/software/crystaldiskmark/\n\n"
                        f"Et placez les fichiers dans:\n{cdm_dir}"
                    )
                    return

            # Lancer
            if cdm_exe and os.path.exists(cdm_exe):
                subprocess.Popen([cdm_exe], shell=True)
                messagebox.showinfo(
                    "CrystalDiskMark",
                    f"CrystalDiskMark lancé!\n\n"
                    f"Emplacement: {cdm_exe}"
                )
            else:
                raise FileNotFoundError("Exécutable CrystalDiskMark introuvable après extraction")

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer CrystalDiskMark:\n\n{str(e)}\n\n"
                f"Vous pouvez le télécharger manuellement depuis:\n"
                f"https://crystalmark.info/en/software/crystaldiskmark/\n\n"
                f"Et placer les fichiers dans:\n{os.path.join(get_local_software_folder(), 'CrystalDiskMark')}"
            )

    def _launch_cpuz(self):
        """Lancer CPU-Z portable"""
        import os
        from tkinter import messagebox

        try:
            tools_dir = get_local_software_folder()

            # Chercher d'abord dans CPU-ZPortable (PortableApps)
            cpuz_portable_dir = os.path.join(tools_dir, "CPU-ZPortable")
            cpuz_portable_exe = os.path.join(cpuz_portable_dir, "CPU-ZPortable.exe")

            if os.path.exists(cpuz_portable_exe):
                os.startfile(cpuz_portable_exe)
                messagebox.showinfo(
                    "CPU-Z",
                    f"CPU-Z lancé!\n\nEmplacement: {cpuz_portable_exe}"
                )
                return

            # Sinon, chercher dans dossier classique CPU-Z
            self._launch_portable_tool(
                tool_name="CPU-Z",
                folder_name="CPU-Z",
                file_pattern="cpuz",
                description="CPU-Z affiche les informations détaillées du processeur."
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer CPU-Z:\n\n{str(e)}"
            )

    def _launch_gpuz(self):
        """Lancer GPU-Z portable"""
        import os
        from tkinter import messagebox

        try:
            tools_dir = get_local_software_folder()

            # Chercher GPU-Z dans le dossier logiciel
            gpuz_exe = os.path.join(tools_dir, "GPU-Z.0.7.0.exe")

            if os.path.exists(gpuz_exe):
                os.startfile(gpuz_exe)
                messagebox.showinfo(
                    "GPU-Z",
                    "✅ GPU-Z lancé!\n\n"
                    f"Emplacement: {gpuz_exe}\n\n"
                    "GPU-Z affiche les informations détaillées de votre carte graphique."
                )
                return

            # Chercher dans un sous-dossier GPU-Z
            gpuz_dir = os.path.join(tools_dir, "GPU-Z")
            if os.path.exists(gpuz_dir):
                for file in os.listdir(gpuz_dir):
                    if file.lower().endswith('.exe') and 'gpu-z' in file.lower():
                        gpuz_path = os.path.join(gpuz_dir, file)
                        os.startfile(gpuz_path)
                        messagebox.showinfo(
                            "GPU-Z",
                            f"✅ GPU-Z lancé!\n\nEmplacement: {gpuz_path}"
                        )
                        return

            # Pas trouvé
            messagebox.showwarning(
                "GPU-Z non trouvé",
                "GPU-Z n'est pas encore installé.\n\n"
                f"Emplacement attendu:\n{gpuz_exe}\n\n"
                "Vous pouvez le télécharger depuis:\n"
                "https://www.techpowerup.com/gpuz/"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer GPU-Z:\n\n{str(e)}"
            )

    def _launch_wisecare365(self):
        """Lancer Wise Care 365 Portable"""
        import subprocess
        import os
        import urllib.request
        from tkinter import messagebox

        try:
            # Utiliser dossier 'logiciel' local à côté de l'exécutable
            tools_dir = get_local_software_folder()
            wc365_dir = os.path.join(tools_dir, "WiseCare365")
            os.makedirs(wc365_dir, exist_ok=True)

            # Chercher l'exécutable Wise Care 365
            wc365_exe = None
            if os.path.exists(wc365_dir):
                for file in os.listdir(wc365_dir):
                    if file.lower().endswith('.exe') and 'wisecare' in file.lower():
                        wc365_exe = os.path.join(wc365_dir, file)
                        break

            # Si pas trouvé, télécharger
            if not wc365_exe or not os.path.exists(wc365_exe):
                response = messagebox.askyesno(
                    "Télécharger Wise Care 365",
                    "Wise Care 365 n'est pas encore téléchargé.\n\n"
                    "Voulez-vous le télécharger maintenant?\n"
                    "(~15 MB, version portable, téléchargement unique)\n\n"
                    "Wise Care 365 optimise et nettoie le système Windows.",
                    icon='question'
                )

                if not response:
                    return

                messagebox.showinfo(
                    "Téléchargement",
                    "Le téléchargement va démarrer.\n\n"
                    "Cela peut prendre quelques instants..."
                )

                # URL Wise Care 365 Portable (depuis PortableApps)
                url = "https://portableapps.com/redirect/?a=WiseCare365Portable&s=s&d=pa&f=WiseCare365Portable_6.7.4.paf.exe"
                wc365_installer = os.path.join(tools_dir, "WiseCare365Portable.exe")

                # Télécharger
                print(f"📥 Téléchargement de Wise Care 365...")
                try:
                    urllib.request.urlretrieve(url, wc365_installer)
                    print(f"✅ Wise Care 365 téléchargé dans: {tools_dir}")

                    # L'installer portable s'auto-extrait
                    messagebox.showinfo(
                        "Installation",
                        "Wise Care 365 va s'installer.\n\n"
                        "Choisissez comme destination:\n"
                        f"{wc365_dir}\n\n"
                        "Puis cliquez à nouveau sur le bouton Wise Care 365."
                    )
                    os.startfile(wc365_installer)
                    return

                except Exception as download_error:
                    messagebox.showerror(
                        "Erreur de téléchargement",
                        f"Impossible de télécharger Wise Care 365:\n\n{str(download_error)}\n\n"
                        f"Téléchargez-le manuellement depuis:\n"
                        f"https://www.wisecleaner.com/wise-care-365.html\n"
                        f"ou depuis PortableApps.com"
                    )
                    return

            # Lancer
            os.startfile(wc365_exe)
            messagebox.showinfo(
                "Wise Care 365",
                f"Wise Care 365 lancé!\n\n"
                f"Emplacement: {wc365_exe}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer Wise Care 365:\n\n{str(e)}\n\n"
                f"Téléchargez-le depuis:\n"
                f"https://www.wisecleaner.com"
            )

    def _create_diagnostic_section(self, parent, title, items):
        """Section de diagnostic"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        header = ctk.CTkLabel(
            card,
            text=title,
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        header.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        for label, value, status in items:
            row = ctk.CTkFrame(
                content,
                fg_color=DesignTokens.BG_ELEVATED,
                corner_radius=DesignTokens.RADIUS_SM
            )
            row.pack(fill=tk.X, pady=3)
            
            row_content = ctk.CTkFrame(row, fg_color="transparent")
            row_content.pack(fill=tk.X, padx=12, pady=8)
            
            label_widget = ctk.CTkLabel(
                row_content,
                text=label,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY,
                anchor="w",
                width=150
            )
            label_widget.pack(side=tk.LEFT)
            
            value_widget = ctk.CTkLabel(
                row_content,
                text=value,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            )
            value_widget.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
            
            status_widget = ctk.CTkLabel(
                row_content,
                text=status,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.SUCCESS if status == "✅" else DesignTokens.WARNING
            )
            status_widget.pack(side=tk.RIGHT)
    
    def _run_diagnostic(self):
        """Lancer diagnostic"""
        print("🔍 Lancement du diagnostic complet...")
        # Rafraîchir infos
        self.system_info = self._get_system_info()
        # Recréer contenu
        for widget in self.winfo_children():
            widget.destroy()
        self._create_header()
        self._create_content()
        print("✅ Diagnostic terminé")

    def _export_pc_info(self):
        """Exporter les informations PC vers un fichier texte"""
        from tkinter import filedialog, messagebox
        from datetime import datetime

        try:
            # Demander l'emplacement du fichier
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
                initialfile=f"info_pc_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )

            if not filename:
                return

            # Rafraîchir les infos avant export
            self.system_info = self._get_system_info()

            # Créer le contenu du fichier
            content = []
            content.append("=" * 80)
            content.append(" INFORMATIONS SYSTÈME - NITRITE V17")
            content.append("=" * 80)
            content.append(f"\nDate de génération: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

            # Système
            content.append("\n" + "=" * 80)
            content.append("SYSTÈME D'EXPLOITATION")
            content.append("=" * 80)
            content.append(f"OS: {self.system_info.get('os', 'N/A')}")
            content.append(f"Version: {self.system_info.get('os_version', 'N/A')}")
            content.append(f"Release: {self.system_info.get('os_release', 'N/A')}")
            content.append(f"Architecture: {self.system_info.get('architecture', 'N/A')}")
            content.append(f"Hostname: {self.system_info.get('hostname', 'N/A')}")

            # Carte mère
            if 'motherboard_product' in self.system_info:
                content.append(f"\nCarte mère: {self.system_info.get('motherboard_manufacturer', 'N/A')} {self.system_info.get('motherboard_product', 'N/A')}")

            # Processeur
            content.append("\n" + "=" * 80)
            content.append("PROCESSEUR")
            content.append("=" * 80)
            if 'cpu_name' in self.system_info:
                content.append(f"Modèle: {self.system_info.get('cpu_name', 'N/A')}")
                content.append(f"Fabricant: {self.system_info.get('cpu_manufacturer', 'N/A')}")
                content.append(f"Cores: {self.system_info.get('cpu_cores', 'N/A')}")
                content.append(f"Threads: {self.system_info.get('cpu_threads', 'N/A')}")
                content.append(f"Fréquence max: {self.system_info.get('cpu_max_speed', 'N/A')} MHz")
            else:
                content.append(f"Processeur: {self.system_info.get('processor', 'N/A')}")

            if PSUTIL_AVAILABLE:
                content.append(f"Utilisation actuelle: {self.system_info.get('cpu_percent', 0):.1f}%")

            # Mémoire RAM
            content.append("\n" + "=" * 80)
            content.append("MÉMOIRE RAM")
            content.append("=" * 80)
            if 'ram_modules' in self.system_info and self.system_info['ram_modules']:
                content.append(f"Total: {self.system_info.get('ram_total_gb', 0):.2f} GB")
                content.append(f"\nModules installés:")
                for i, module in enumerate(self.system_info['ram_modules'], 1):
                    content.append(f"  Module {i}:")
                    content.append(f"    - Fabricant: {module.get('manufacturer', 'Unknown')}")
                    content.append(f"    - Capacité: {module.get('capacity_gb', 0):.2f} GB")
                    content.append(f"    - Vitesse: {module.get('speed_mhz', 0)} MHz")
            if PSUTIL_AVAILABLE:
                content.append(f"\nUtilisation: {self.system_info.get('ram_used', 0):.2f} / {self.system_info.get('ram_total', 0):.2f} GB")
                content.append(f"Pourcentage: {self.system_info.get('ram_percent', 0):.1f}%")

            # Cartes graphiques
            if 'gpus' in self.system_info and self.system_info['gpus']:
                content.append("\n" + "=" * 80)
                content.append("CARTES GRAPHIQUES")
                content.append("=" * 80)
                for i, gpu in enumerate(self.system_info['gpus'], 1):
                    content.append(f"\nGPU {i}:")
                    content.append(f"  Nom: {gpu.get('name', 'N/A')}")
                    vram_gb = gpu.get('ram_bytes', 0) / (1024**3)
                    if vram_gb > 0:
                        content.append(f"  VRAM: {vram_gb:.2f} GB")
                    content.append(f"  Driver: {gpu.get('driver_version', 'N/A')}")

            # Stockage
            if 'storage_devices' in self.system_info and self.system_info['storage_devices']:
                content.append("\n" + "=" * 80)
                content.append("DISQUES DE STOCKAGE")
                content.append("=" * 80)
                for i, disk in enumerate(self.system_info['storage_devices'], 1):
                    content.append(f"\nDisque {i}:")
                    content.append(f"  Modèle: {disk.get('model', 'N/A')}")
                    content.append(f"  Capacité: {disk.get('size_gb', 0):.2f} GB")
                    content.append(f"  Interface: {disk.get('interface', 'N/A')}")

            # Partitions
            if PSUTIL_AVAILABLE and 'disks' in self.system_info:
                content.append("\n" + "=" * 80)
                content.append("PARTITIONS")
                content.append("=" * 80)
                for disk in self.system_info['disks']:
                    content.append(f"\n{disk.get('device', 'N/A')} ({disk.get('fstype', 'N/A')})")
                    content.append(f"  Mountpoint: {disk.get('mountpoint', 'N/A')}")
                    content.append(f"  Total: {disk.get('total', 0):.2f} GB")
                    content.append(f"  Utilisé: {disk.get('used', 0):.2f} GB ({disk.get('percent', 0):.1f}%)")
                    content.append(f"  Libre: {disk.get('free', 0):.2f} GB")

            # Réseau
            if PSUTIL_AVAILABLE:
                content.append("\n" + "=" * 80)
                content.append("RÉSEAU")
                content.append("=" * 80)
                content.append(f"Données envoyées: {self.system_info.get('net_sent', 0):.2f} MB")
                content.append(f"Données reçues: {self.system_info.get('net_recv', 0):.2f} MB")

            content.append("\n" + "=" * 80)
            content.append("FIN DU RAPPORT")
            content.append("=" * 80)

            # Écrire dans le fichier
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(content))

            messagebox.showinfo(
                "Export réussi",
                f"Les informations PC ont été exportées vers:\n\n{filename}\n\n"
                f"Vous pouvez maintenant partager ce fichier pour obtenir de l'aide."
            )

            # Ouvrir le fichier
            import subprocess
            subprocess.Popen(['notepad.exe', filename])

        except Exception as e:
            messagebox.showerror(
                "Erreur d'export",
                f"Impossible d'exporter les informations:\n\n{str(e)}"
            )

    # === MÉTHODES MASTER OUTILS ===

    def _execute_tool(self, tool_name, tool_action):
        """Exécuter outil (commande ou URL)"""
        import subprocess
        import webbrowser

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

                # Certaines commandes doivent être lancées directement
                direct_commands = [
                    'msinfo32', 'dxdiag', 'taskmgr', 'msconfig',
                    'resmon', 'diskmgmt.msc', 'compmgmt.msc', 'services.msc',
                    'dfrgui', 'regedit', 'winver', 'sysdm.cpl'
                ]

                # Vérifier si c'est une commande directe
                is_direct = any(cmd in tool_action for cmd in direct_commands)

                if is_direct:
                    # Lancer directement sans cmd
                    subprocess.Popen(tool_action, shell=True)
                else:
                    # Utiliser cmd.exe pour autres commandes
                    subprocess.Popen(
                        ['cmd.exe', '/c', 'start', tool_action],
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )

        except Exception as e:
            print(f"❌ Erreur exécution {tool_name}: {e}")
            from tkinter import messagebox
            messagebox.showerror(
                "Erreur d'exécution",
                f"Impossible d'exécuter {tool_name}:\n\n{str(e)}"
            )

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
                    os.remove(script_path)
                except:
                    pass
            threading.Thread(target=cleanup, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lancer le script d'activation:\n\n{str(e)}")

    def _open_temp_folder(self):
        """Ouvrir le dossier Temp"""
        try:
            temp_path = os.path.expandvars("%TEMP%")
            subprocess.Popen(f'explorer "{temp_path}"', shell=True)
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier Temp:\n\n{str(e)}")

    def _open_appdata_local(self):
        """Ouvrir le dossier LocalAppData"""
        try:
            appdata_path = os.path.expandvars("%LOCALAPPDATA%")
            subprocess.Popen(f'explorer "{appdata_path}"', shell=True)
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erreur", f"Impossible d'ouvrir AppData Local:\n\n{str(e)}")

    def _update_all_apps(self):
        """Mettre à jour toutes les applications via WinGet"""
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
        import webbrowser
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
        import webbrowser
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


class OptimizationsPage(ctk.CTkFrame):
    """Page Optimisations avec vraies commandes"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)
        
        self._create_header()
        self._create_content()
    
    def _create_header(self):
        """Header"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)
        
        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)
        
        title = ctk.CTkLabel(
            container,
            text="⚡ Optimisations",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        ModernButton(
            container,
            text="🚀 Optimiser Tout",
            variant="filled",
            command=self._optimize_all
        ).pack(side=tk.RIGHT)
    
    def _create_content(self):
        """Contenu"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self._create_cleanup_section(scroll)
        self._create_performance_section(scroll)
        self._create_services_section(scroll)
        self._create_startup_section(scroll)
    
    def _create_cleanup_section(self, parent):
        """Section nettoyage"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="🧹 Nettoyage",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        actions = [
            ("🗑️ Vider la corbeille", "Libérer de l'espace", self._empty_recycle_bin),
            ("🧹 Fichiers temporaires", "Supprimer fichiers temp", self._clean_temp_files),
            ("📁 Cache navigateurs", "Nettoyer cache", self._clean_browser_cache),
            ("💾 Nettoyage disque Windows", "Outil système", self._clean_system_files),
        ]
        
        for text, desc, command in actions:
            self._create_action_row(content, text, desc, command)
    
    def _create_performance_section(self, parent):
        """Section performance"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="⚡ Performance",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        actions = [
            ("🔧 Optimiser disques", "Défragmentation/TRIM", self._defragment),
            ("🎯 Gestionnaire des tâches", "Ouvrir Task Manager", self._optimize_boot),
            ("💻 Nettoyeur de disque", "Outil Windows", self._clean_registry),
            ("⚙️ Options performances", "Ajuster effets visuels", self._adjust_visual_effects),
            ("🚀 AtlasOS", "OS optimisé performance gaming", lambda: self._open_url("https://atlasos.net")),
            ("🔥 ReviOS", "Windows debloaté optimisé", lambda: self._open_url("https://www.revi.cc/")),
        ]

        for text, desc, command in actions:
            self._create_action_row(content, text, desc, command)
    
    def _create_services_section(self, parent):
        """Section services"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="🔧 Services",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        desc = ctk.CTkLabel(
            content,
            text="Gérer les services Windows",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=10)
        
        ModernButton(
            content,
            text="🔧 Ouvrir Services",
            variant="outlined",
            command=self._manage_services
        ).pack(anchor="w")
    
    def _create_startup_section(self, parent):
        """Section démarrage"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)
        
        title = ctk.CTkLabel(
            card,
            text="🚀 Démarrage",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=15)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        desc = ctk.CTkLabel(
            content,
            text="Gérer les programmes au démarrage",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=10)
        
        ModernButton(
            content,
            text="🚀 Gestionnaire Démarrage",
            variant="outlined",
            command=self._manage_startup
        ).pack(anchor="w")
    
    def _create_action_row(self, parent, text, description, command):
        """Ligne d'action"""
        row = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        row.pack(fill=tk.X, pady=5)
        
        container = ctk.CTkFrame(row, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=12)
        
        left = ctk.CTkFrame(container, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        text_label = ctk.CTkLabel(
            left,
            text=text,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        text_label.pack(anchor="w")
        
        desc_label = ctk.CTkLabel(
            left,
            text=description,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        desc_label.pack(anchor="w")
        
        ModernButton(
            container,
            text="▶️ Exécuter",
            variant="filled",
            size="sm",
            command=command
        ).pack(side=tk.RIGHT)
    
    # Callbacks avec vraies commandes
    def _optimize_all(self):
        """Optimisation complète"""
        print("🚀 Optimisation complète...")
        self._empty_recycle_bin()
        self._clean_temp_files()
        print("✅ Optimisation terminée")
    
    def _empty_recycle_bin(self):
        """Vider corbeille"""
        try:
            subprocess.run('powershell -Command "Clear-RecycleBin -Force"', shell=True, check=True)
            print("✅ Corbeille vidée")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _clean_temp_files(self):
        """Nettoyer fichiers temporaires"""
        try:
            temp_dirs = [
                os.environ.get('TEMP'),
                os.environ.get('TMP'),
                os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Temp')
            ]
            
            for temp_dir in temp_dirs:
                if temp_dir and os.path.exists(temp_dir):
                    try:
                        for item in os.listdir(temp_dir):
                            item_path = os.path.join(temp_dir, item)
                            try:
                                if os.path.isfile(item_path):
                                    os.unlink(item_path)
                                elif os.path.isdir(item_path):
                                    shutil.rmtree(item_path)
                            except:
                                continue
                    except:
                        continue
            
            print("✅ Fichiers temporaires nettoyés")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _clean_browser_cache(self):
        """Nettoyer cache navigateurs"""
        print("📁 Ouverture gestionnaire stockage...")
        try:
            subprocess.Popen('ms-settings:storagesense', shell=True)
        except:
            print("❌ Impossible d'ouvrir les paramètres")
    
    def _clean_system_files(self):
        """Nettoyage disque Windows"""
        try:
            subprocess.Popen('cleanmgr', shell=True)
            print("✅ Nettoyage disque lancé")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _defragment(self):
        """Défragmentation"""
        try:
            subprocess.Popen('dfrgui', shell=True)
            print("✅ Défragmenteur lancé")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _optimize_boot(self):
        """Gestionnaire des tâches"""
        try:
            subprocess.Popen('taskmgr', shell=True)
            print("✅ Gestionnaire des tâches lancé")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _clean_registry(self):
        """Nettoyage disque"""
        try:
            subprocess.Popen('cleanmgr /sageset:1', shell=True)
            print("✅ Nettoyage disque configuré")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _adjust_visual_effects(self):
        """Ajuster effets visuels"""
        try:
            subprocess.Popen('SystemPropertiesPerformance.exe', shell=True)
            print("✅ Options de performances ouvertes")
        except Exception as e:
            print(f"❌ Erreur: {e}")

    def _open_url(self, url):
        """Ouvrir une URL dans le navigateur"""
        import webbrowser
        try:
            webbrowser.open(url)
            print(f"✅ Ouverture de {url}")
        except Exception as e:
            print(f"❌ Erreur lors de l'ouverture de l'URL: {e}")

    def _manage_services(self):
        """Gérer services"""
        try:
            subprocess.Popen('services.msc', shell=True)
            print("✅ Gestionnaire de services ouvert")
        except Exception as e:
            print(f"❌ Erreur: {e}")
    
    def _manage_startup(self):
        """Gérer démarrage"""
        try:
            subprocess.Popen('taskmgr /0 /startup', shell=True)
            print("✅ Gestionnaire de démarrage ouvert")
        except Exception as e:
            print(f"❌ Erreur: {e}")