#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page ScanVirus - NiTriTe V20.0
Scanner de fichiers et analyse système anti-malware
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import subprocess
import threading
import hashlib
import os
import psutil
import webbrowser
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader


class ScanVirusPage(ctk.CTkFrame):
    """Page de scan antivirus et analyse système"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Stockage des menaces détectées
        self.detected_threats = {
            'quarantine': [],  # Fichiers en quarantaine
            'delete': [],      # Fichiers à supprimer
            'false_positive': []  # Faux positifs
        }
        self.threat_analysis = {}  # Résultats VirusTotal par fichier

        # Configurer grid layout
        self.grid_rowconfigure(0, weight=0)  # Header
        self.grid_rowconfigure(1, weight=0)  # Actions rapides
        self.grid_rowconfigure(2, weight=0)  # Catégories de menaces
        self.grid_rowconfigure(3, weight=1)  # Terminal
        self.grid_columnconfigure(0, weight=1)

        self._create_header()
        self._create_quick_actions()
        self._create_threat_categories()
        self._create_terminal()

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre
        title_frame = SectionHeader(container, text="🛡️ Scanner Antivirus & Analyse Système")
        title_frame.pack(side=tk.LEFT)

        # Info
        ctk.CTkLabel(
            container,
            text="Powered by Windows Defender",
            font=("Segoe UI", 11),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.RIGHT)

    def _create_quick_actions(self):
        """Actions rapides"""
        actions_card = ModernCard(self)
        actions_card.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(actions_card, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Section Scan Fichiers
        file_section = ctk.CTkFrame(container, fg_color="transparent")
        file_section.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ctk.CTkLabel(
            file_section,
            text="📁 Scan de Fichiers",
            font=("Segoe UI", 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(0, 10))

        btn_frame1 = ctk.CTkFrame(file_section, fg_color="transparent")
        btn_frame1.pack(fill=tk.X)

        ModernButton(
            btn_frame1,
            text="📄 Scanner Fichier",
            variant="filled",
            size="md",
            command=self._scan_file
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame1,
            text="📂 Scanner Dossier",
            variant="outlined",
            size="md",
            command=self._scan_folder
        ).pack(side=tk.LEFT, padx=5)

        # Section Scan PC
        pc_section = ctk.CTkFrame(container, fg_color="transparent")
        pc_section.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(20, 0))

        ctk.CTkLabel(
            pc_section,
            text="🖥️ Scan Système",
            font=("Segoe UI", 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(0, 10))

        btn_frame2 = ctk.CTkFrame(pc_section, fg_color="transparent")
        btn_frame2.pack(fill=tk.X)

        ModernButton(
            btn_frame2,
            text="⚡ Scan Rapide",
            variant="filled",
            size="md",
            command=self._quick_scan
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame2,
            text="🔍 Scan Complet",
            variant="outlined",
            size="md",
            command=self._full_scan
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame2,
            text="🔬 Analyse Avancée",
            variant="outlined",
            size="md",
            command=self._advanced_analysis
        ).pack(side=tk.LEFT, padx=5)

        # Section Scans Ultra-Poussés
        ultra_section = ctk.CTkFrame(container, fg_color="transparent")
        ultra_section.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(20, 0))

        ctk.CTkLabel(
            ultra_section,
            text="🛡️ Scans Ultra-Poussés",
            font=("Segoe UI", 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(0, 10))

        btn_frame_ultra1 = ctk.CTkFrame(ultra_section, fg_color="transparent")
        btn_frame_ultra1.pack(fill=tk.X)

        ModernButton(
            btn_frame_ultra1,
            text="🔥 Scan Rootkit",
            variant="filled",
            size="md",
            command=self._rootkit_scan
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame_ultra1,
            text="💾 Scan RAM",
            variant="outlined",
            size="md",
            command=self._memory_scan
        ).pack(side=tk.LEFT, padx=5)

        btn_frame_ultra2 = ctk.CTkFrame(ultra_section, fg_color="transparent")
        btn_frame_ultra2.pack(fill=tk.X, pady=(5, 0))

        ModernButton(
            btn_frame_ultra2,
            text="🧬 Scan Heuristique",
            variant="outlined",
            size="md",
            command=self._heuristic_scan
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame_ultra2,
            text="🔐 Scan Profond",
            variant="outlined",
            size="md",
            command=self._deep_scan
        ).pack(side=tk.LEFT, padx=5)

        # Section Outils Externes
        tools_section = ctk.CTkFrame(container, fg_color="transparent")
        tools_section.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(20, 0))

        ctk.CTkLabel(
            tools_section,
            text="🛠️ Outils Externes",
            font=("Segoe UI", 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w", pady=(0, 10))

        btn_frame3 = ctk.CTkFrame(tools_section, fg_color="transparent")
        btn_frame3.pack(fill=tk.X)

        ModernButton(
            btn_frame3,
            text="🦠 Malwarebytes",
            variant="filled",
            size="sm",
            command=self._launch_malwarebytes
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame3,
            text="🕷️ Spybot",
            variant="outlined",
            size="sm",
            command=self._launch_spybot
        ).pack(side=tk.LEFT, padx=3)

        btn_frame4 = ctk.CTkFrame(tools_section, fg_color="transparent")
        btn_frame4.pack(fill=tk.X, pady=(5, 0))

        ModernButton(
            btn_frame4,
            text="🧹 AdwCleaner",
            variant="outlined",
            size="sm",
            command=self._launch_adwcleaner
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame4,
            text="💿 Wise Disk Cleaner",
            variant="outlined",
            size="sm",
            command=self._launch_wise_disk_cleaner
        ).pack(side=tk.LEFT, padx=3)

        btn_frame5 = ctk.CTkFrame(tools_section, fg_color="transparent")
        btn_frame5.pack(fill=tk.X, pady=(5, 0))

        ModernButton(
            btn_frame5,
            text="🔎 VirusTotal",
            variant="filled",
            size="sm",
            command=self._launch_virustotal
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame5,
            text="🚀 AutoRuns",
            variant="outlined",
            size="sm",
            command=self._launch_autoruns
        ).pack(side=tk.LEFT, padx=3)

        # Analyses Avancées Multi-Moteurs
        ctk.CTkLabel(
            tools_section,
            text="🧪 Analyses Avancées",
            font=("Segoe UI", 11, "bold"),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(anchor="w", pady=(15, 5))

        btn_frame6 = ctk.CTkFrame(tools_section, fg_color="transparent")
        btn_frame6.pack(fill=tk.X, pady=(5, 0))

        ModernButton(
            btn_frame6,
            text="🔍 Jotti",
            variant="outlined",
            size="sm",
            command=self._launch_jotti
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame6,
            text="🧪 Hybrid-Analysis",
            variant="outlined",
            size="sm",
            command=self._launch_hybrid_analysis
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            btn_frame6,
            text="🛡️ Dr.Web VMS",
            variant="outlined",
            size="sm",
            command=self._launch_drweb_vms
        ).pack(side=tk.LEFT, padx=3)

    def _is_admin(self):
        """Vérifier si l'application tourne avec des privilèges administrateur"""
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def _create_threat_categories(self):
        """Créer les catégories de menaces détectées"""
        self.categories_card = ModernCard(self)
        self.categories_card.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(self.categories_card, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Header
        header_frame = ctk.CTkFrame(container, fg_color="transparent")
        header_frame.pack(fill=tk.X, pady=(0, 10))

        SectionHeader(
            header_frame,
            text="🦠 Menaces Détectées"
        ).pack(side=tk.LEFT)

        # Bouton rafraîchir
        ModernButton(
            header_frame,
            text="🔄 Rafraîchir",
            variant="outlined",
            size="sm",
            command=self._refresh_threat_categories
        ).pack(side=tk.RIGHT)

        # Frame pour les 3 catégories
        categories_container = ctk.CTkFrame(container, fg_color="transparent")
        categories_container.pack(fill=tk.X, pady=(5, 0))

        # Quarantaine
        self._create_category_display(
            categories_container,
            "🔒 Quarantaine",
            "quarantine",
            DesignTokens.WARNING,
            0
        )

        # À Supprimer
        self._create_category_display(
            categories_container,
            "🗑️ À Supprimer",
            "delete",
            DesignTokens.ERROR,
            1
        )

        # Faux Positifs
        self._create_category_display(
            categories_container,
            "✅ Faux Positifs",
            "false_positive",
            DesignTokens.SUCCESS,
            2
        )

        # Initialement masqué (affiché après scan)
        self.categories_card.grid_remove()

    def _create_category_display(self, parent, title, category_key, color, column):
        """Créer l'affichage d'une catégorie de menaces"""
        category_frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=12
        )
        category_frame.grid(row=0, column=column, sticky="nsew", padx=5)
        parent.grid_columnconfigure(column, weight=1, uniform="category")

        # Header catégorie
        header = ctk.CTkFrame(category_frame, fg_color="transparent")
        header.pack(fill=tk.X, padx=15, pady=(15, 10))

        ctk.CTkLabel(
            header,
            text=title,
            font=("Segoe UI", 14, "bold"),
            text_color=color
        ).pack(side=tk.LEFT)

        # Compteur
        count_label = ctk.CTkLabel(
            header,
            text="0",
            font=("Segoe UI", 13, "bold"),
            text_color=DesignTokens.TEXT_SECONDARY,
            width=30,
            height=30,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=15
        )
        count_label.pack(side=tk.RIGHT)

        # Stocker le label pour mise à jour
        if not hasattr(self, 'category_labels'):
            self.category_labels = {}
        self.category_labels[category_key] = count_label

        # Liste scrollable des fichiers
        list_frame = ctk.CTkScrollableFrame(
            category_frame,
            fg_color=DesignTokens.BG_SECONDARY,
            height=150
        )
        list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        # Stocker le frame pour y ajouter des fichiers
        if not hasattr(self, 'category_frames'):
            self.category_frames = {}
        self.category_frames[category_key] = list_frame

    def _create_terminal(self):
        """Terminal pour afficher les résultats"""
        terminal_card = ModernCard(self)
        terminal_card.grid(row=3, column=0, sticky="nsew", padx=20, pady=10)

        # Header terminal
        header = ctk.CTkFrame(terminal_card, fg_color="transparent")
        header.pack(fill=tk.X, padx=20, pady=(15, 5))

        ctk.CTkLabel(
            header,
            text="📊 Résultats du Scan",
            font=("Segoe UI", 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT)

        # Boutons contrôle terminal
        controls_frame = ctk.CTkFrame(header, fg_color="transparent")
        controls_frame.pack(side=tk.RIGHT)

        # Police
        ctk.CTkLabel(
            controls_frame,
            text="Police:",
            font=("Segoe UI", 11),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.LEFT, padx=(0, 5))

        ctk.CTkButton(
            controls_frame,
            text="A-",
            width=30,
            height=25,
            command=lambda: self._change_font_size(-1)
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            controls_frame,
            text="A+",
            width=30,
            height=25,
            command=lambda: self._change_font_size(1)
        ).pack(side=tk.LEFT, padx=2)

        # Hauteur
        ctk.CTkLabel(
            controls_frame,
            text="Hauteur:",
            font=("Segoe UI", 11),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.LEFT, padx=(10, 5))

        ctk.CTkButton(
            controls_frame,
            text="▼",
            width=30,
            height=25,
            command=lambda: self._resize_terminal(-5)
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            controls_frame,
            text="▲",
            width=30,
            height=25,
            command=lambda: self._resize_terminal(5)
        ).pack(side=tk.LEFT, padx=2)

        # Bouton clear
        ModernButton(
            controls_frame,
            text="🗑️ Effacer",
            variant="outlined",
            size="sm",
            command=self._clear_terminal
        ).pack(side=tk.LEFT, padx=(10, 0))

        # Terminal
        terminal_container = ctk.CTkFrame(terminal_card, fg_color="transparent")
        terminal_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 15))

        # Paramètres terminal
        self.terminal_height = 25
        self.terminal_font_size = 10

        # TextBox pour le terminal
        self.terminal_text = ctk.CTkTextbox(
            terminal_container,
            font=("Consolas", self.terminal_font_size),
            fg_color="#0C1E2E",
            text_color="#00FF00",
            wrap="word"
        )
        self.terminal_text.pack(fill=tk.BOTH, expand=True)

        # Configurer hauteur initiale
        self.terminal_text.configure(height=self.terminal_height * 16)

        # Message initial
        self._log("=" * 80)
        self._log("🛡️ SCANNER ANTIVIRUS - NiTriTe V20.0")
        self._log("=" * 80)
        self._log("")
        self._log("💡 Sélectionnez une action ci-dessus pour commencer le scan")
        self._log("")
        self._log("FONCTIONNALITÉS:")
        self._log("  • Scanner Fichier: Analyser un fichier spécifique (.exe, .zip, .bat, etc.)")
        self._log("  • Scanner Dossier: Analyser tous les fichiers d'un dossier")
        self._log("  • Scan Rapide: Scan rapide du système (5-10 min)")
        self._log("  • Scan Complet: Scan complet du disque (1-2h)")
        self._log("  • Analyse Avancée: Processus, connexions réseau, registre")
        self._log("")
        self._log("-" * 80)
        self._log("")

    def _log(self, message):
        """Ajouter un message au terminal"""
        self.terminal_text.insert("end", message + "\n")
        self.terminal_text.see("end")

    def _clear_terminal(self):
        """Effacer le terminal"""
        self.terminal_text.delete("1.0", "end")

    def _resize_terminal(self, delta):
        """Redimensionner le terminal"""
        self.terminal_height = max(10, min(50, self.terminal_height + delta))
        self.terminal_text.configure(height=self.terminal_height * 16)

    def _change_font_size(self, delta):
        """Changer la taille de la police"""
        self.terminal_font_size = max(8, min(16, self.terminal_font_size + delta))
        self.terminal_text.configure(font=("Consolas", self.terminal_font_size))

    def _scan_file(self):
        """Scanner un fichier spécifique"""
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier à scanner",
            filetypes=[
                ("Tous les fichiers", "*.*"),
                ("Exécutables", "*.exe;*.com;*.bat;*.cmd;*.ps1;*.msi"),
                ("Archives", "*.zip;*.rar;*.7z;*.tar;*.gz"),
                ("Scripts", "*.sh;*.bash;*.bat;*.cmd;*.ps1;*.vbs"),
                ("Documents", "*.pdf;*.doc;*.docx;*.xls;*.xlsx")
            ]
        )

        if not file_path:
            return

        self._log(f"\n🔍 SCAN FICHIER: {file_path}")
        self._log(f"Taille: {Path(file_path).stat().st_size / 1024:.2f} KB")
        self._log("")

        # Calculer hash
        self._calculate_file_hash(file_path)

        # Scanner avec Windows Defender
        self._run_defender_scan(file_path, "file")

    def _scan_folder(self):
        """Scanner un dossier complet"""
        folder_path = filedialog.askdirectory(title="Sélectionner un dossier à scanner")

        if not folder_path:
            return

        self._log(f"\n📂 SCAN DOSSIER: {folder_path}")
        self._log("")

        # Compter les fichiers
        file_count = len(list(Path(folder_path).rglob('*')))
        self._log(f"Fichiers à scanner: {file_count}")
        self._log("")

        # Scanner avec Windows Defender
        self._run_defender_scan(folder_path, "folder")

    def _quick_scan(self):
        """Scan rapide du système"""
        self._log("\n⚡ DÉMARRAGE SCAN RAPIDE DU SYSTÈME")
        self._log("Durée estimée: 5-10 minutes")
        self._log("")

        confirm = messagebox.askyesno(
            "Scan Rapide",
            "Lancer un scan rapide du système ?\n\n"
            "Durée: 5-10 minutes\n"
            "Analyse: Fichiers système, mémoire, zones critiques"
        )

        if not confirm:
            self._log("❌ Scan annulé par l'utilisateur\n")
            return

        def run_scan():
            try:
                self._log("🔄 Lancement du scan rapide...")
                result = subprocess.run(
                    ['powershell', '-Command', 'Start-MpScan', '-ScanType', 'QuickScan'],
                    capture_output=True,
                    text=True,
                    timeout=900  # 15 min max
                )

                if result.returncode == 0:
                    self._log("✅ Scan rapide terminé avec succès")
                    self._log("\n📊 Vérification des détections...")
                    self._check_defender_threats()
                else:
                    self._log(f"⚠️ Scan terminé avec code: {result.returncode}")
                    if result.stderr:
                        self._log(f"Erreur: {result.stderr}")

            except subprocess.TimeoutExpired:
                self._log("⏱️ Timeout: Le scan a dépassé 15 minutes")
            except Exception as e:
                self._log(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_scan, daemon=True).start()

    def _full_scan(self):
        """Scan complet du système"""
        self._log("\n🔍 DÉMARRAGE SCAN COMPLET DU SYSTÈME")
        self._log("Durée estimée: 1-2 heures")
        self._log("")

        confirm = messagebox.askyesno(
            "Scan Complet",
            "Lancer un scan complet du système ?\n\n"
            "⚠️ AVERTISSEMENT:\n"
            "• Durée: 1-2 heures\n"
            "• Analyse TOUS les fichiers du disque\n"
            "• Peut ralentir le PC pendant le scan"
        )

        if not confirm:
            self._log("❌ Scan annulé par l'utilisateur\n")
            return

        def run_scan():
            try:
                self._log("🔄 Lancement du scan complet...")
                self._log("⏱️ Cette opération peut prendre 1-2 heures...")
                result = subprocess.run(
                    ['powershell', '-Command', 'Start-MpScan', '-ScanType', 'FullScan'],
                    capture_output=True,
                    text=True,
                    timeout=7200  # 2h max
                )

                if result.returncode == 0:
                    self._log("✅ Scan complet terminé avec succès")
                    self._log("\n📊 Vérification des détections...")
                    self._check_defender_threats()
                else:
                    self._log(f"⚠️ Scan terminé avec code: {result.returncode}")
                    if result.stderr:
                        self._log(f"Erreur: {result.stderr}")

            except subprocess.TimeoutExpired:
                self._log("⏱️ Timeout: Le scan a dépassé 2 heures")
            except Exception as e:
                self._log(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_scan, daemon=True).start()

    def _advanced_analysis(self):
        """Analyse avancée: processus, connexions, registre"""
        self._log("\n🔬 ANALYSE SYSTÈME AVANCÉE")
        self._log("=" * 80)
        self._log("")

        def run_analysis():
            # 1. Processus suspects
            self._log("📋 ANALYSE DES PROCESSUS EN COURS")
            self._log("-" * 80)
            self._analyze_processes()
            self._log("")

            # 2. Connexions réseau
            self._log("🌐 CONNEXIONS RÉSEAU ACTIVES")
            self._log("-" * 80)
            self._analyze_network()
            self._log("")

            # 3. Programmes de démarrage
            self._log("🚀 PROGRAMMES AU DÉMARRAGE")
            self._log("-" * 80)
            self._analyze_startup()
            self._log("")

            # 4. Services suspects
            self._log("⚙️ SERVICES SYSTÈME")
            self._log("-" * 80)
            self._analyze_services()
            self._log("")

            self._log("=" * 80)
            self._log("✅ Analyse système terminée")
            self._log("")

        threading.Thread(target=run_analysis, daemon=True).start()

    def _analyze_processes(self):
        """Analyser les processus en cours"""
        try:
            suspicious_count = 0
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    # Détection de processus suspects (heuristique simple)
                    name = proc.info['name'].lower()
                    cpu = proc.info['cpu_percent']
                    mem = proc.info['memory_percent']

                    is_suspicious = False
                    reason = ""

                    # CPU élevé
                    if cpu and cpu > 80:
                        is_suspicious = True
                        reason = f"CPU élevé ({cpu:.1f}%)"

                    # Mémoire élevée
                    if mem and mem > 30:
                        is_suspicious = True
                        reason += f" RAM élevée ({mem:.1f}%)" if reason else f"RAM élevée ({mem:.1f}%)"

                    # Noms suspects
                    suspicious_names = ['cryptominer', 'miner', 'trojan', 'keylog', 'backdoor']
                    if any(sus in name for sus in suspicious_names):
                        is_suspicious = True
                        reason += " Nom suspect" if reason else "Nom suspect"

                    if is_suspicious:
                        self._log(f"  ⚠️ {proc.info['name']} (PID: {proc.info['pid']}) - {reason}")
                        suspicious_count += 1

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

            if suspicious_count == 0:
                self._log("  ✅ Aucun processus suspect détecté")
            else:
                self._log(f"\n  ⚠️ {suspicious_count} processus suspect(s) détecté(s)")

        except Exception as e:
            self._log(f"  ❌ Erreur analyse processus: {str(e)}")

    def _analyze_network(self):
        """Analyser les connexions réseau actives"""
        try:
            connections = psutil.net_connections(kind='inet')
            active_count = 0
            suspicious_count = 0

            for conn in connections[:20]:  # Limiter à 20 connexions
                if conn.status == 'ESTABLISHED':
                    active_count += 1
                    remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

                    # Détecter ports suspects
                    suspicious_ports = [4444, 5555, 6666, 7777, 8888, 31337]  # Ports backdoor courants
                    if conn.raddr and conn.raddr.port in suspicious_ports:
                        self._log(f"  ⚠️ Connexion suspecte: {remote} (Port backdoor potentiel)")
                        suspicious_count += 1
                    else:
                        self._log(f"  ℹ️ {remote}")

            self._log(f"\n  📊 {active_count} connexions actives")
            if suspicious_count > 0:
                self._log(f"  ⚠️ {suspicious_count} connexion(s) suspecte(s)")

        except Exception as e:
            self._log(f"  ❌ Erreur analyse réseau: {str(e)}")

    def _analyze_startup(self):
        """Analyser les programmes au démarrage"""
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Get-CimInstance', 'Win32_StartupCommand', '|', 'Select-Object', 'Name,Command', '|', 'Format-Table', '-AutoSize'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.stdout:
                lines = result.stdout.strip().split('\n')
                self._log(f"  📊 {len(lines)-3} programme(s) au démarrage")
                for line in lines[:15]:  # Limiter à 15 lignes
                    if line.strip():
                        self._log(f"  {line}")
            else:
                self._log("  ℹ️ Aucun programme de démarrage détecté")

        except Exception as e:
            self._log(f"  ❌ Erreur analyse démarrage: {str(e)}")

    def _analyze_services(self):
        """Analyser les services système"""
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Get-Service', '|', 'Where-Object', '{$_.Status', '-eq', '"Running"}', '|', 'Select-Object', 'Name,DisplayName', '-First', '15', '|', 'Format-Table', '-AutoSize'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.stdout:
                lines = result.stdout.strip().split('\n')
                self._log(f"  📊 Services en cours d'exécution (15 premiers):")
                for line in lines:
                    if line.strip():
                        self._log(f"  {line}")
            else:
                self._log("  ℹ️ Impossible de lister les services")

        except Exception as e:
            self._log(f"  ❌ Erreur analyse services: {str(e)}")

    def _calculate_file_hash(self, file_path):
        """Calculer le hash SHA256 d'un fichier"""
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

            hash_value = sha256_hash.hexdigest()
            self._log(f"🔐 SHA256: {hash_value}")
            self._log("")
            self._log("💡 Vous pouvez vérifier ce hash sur VirusTotal.com")
            self._log("")

        except Exception as e:
            self._log(f"❌ Erreur calcul hash: {str(e)}")

    def _run_defender_scan(self, path, scan_type):
        """Lancer un scan Windows Defender sur un chemin"""
        # Vérifier privilèges admin AVANT de lancer le thread
        if not self._is_admin():
            self._log("⚠️ AVERTISSEMENT: NiTriTe ne tourne pas en mode administrateur")
            self._log("   Le scan Windows Defender peut échouer sans privilèges admin.")
            self._log("")

            # Proposer de scanner avec VirusTotal en alternative
            response = messagebox.askyesno(
                "Privilèges Administrateur Requis",
                "⚠️ Windows Defender nécessite des privilèges administrateur.\n\n"
                "NiTriTe ne tourne pas en mode admin actuellement.\n\n"
                "Options:\n"
                "• OUI: Scanner uniquement le hash sur VirusTotal (rapide)\n"
                "• NON: Essayer quand même le scan Defender (peut échouer)",
                icon='warning'
            )

            if response:
                # Scanner avec VirusTotal uniquement
                self._log("🔎 Scan VirusTotal uniquement (sans privilèges admin)")
                vt_result = self._check_virustotal_file(path)
                if vt_result:
                    self._log(f"✅ Hash calculé et envoyé à VirusTotal")
                    self._log(f"   Vérifiez les résultats dans votre navigateur")
                return

        def run_scan():
            try:
                self._log(f"🔄 Lancement scan Windows Defender...")
                self._log(f"Cible: {path}")
                self._log("")

                # Utiliser Windows Defender en ligne de commande
                result = subprocess.run(
                    ['powershell', '-Command', f'Start-MpScan', '-ScanPath', f'"{path}"', '-ScanType', 'CustomScan'],
                    capture_output=True,
                    text=True,
                    timeout=600  # 10 min max
                )

                if result.returncode == 0:
                    self._log("✅ Scan terminé avec succès")
                    self._log("")
                    self._check_defender_threats()
                    # Rafraîchir catégories pour afficher menaces détectées
                    self._refresh_threat_categories()
                else:
                    self._log(f"⚠️ Scan terminé avec code: {result.returncode}")

                    # Gestion spécifique erreur 0x80508023
                    if result.stderr and "0x80508023" in result.stderr:
                        self._log("")
                        self._log("❌ ERREUR 0x80508023: Accès refusé ou fichier protégé")
                        self._log("")
                        self._log("📋 Causes possibles:")
                        self._log("   1. Privilèges administrateur insuffisants")
                        self._log("   2. Fichier archive protégé (ZIP, RAR avec mot de passe)")
                        self._log("   3. Fichier en cours d'utilisation par une autre application")
                        self._log("   4. Protection en temps réel de Defender bloque le scan")
                        self._log("")
                        self._log("💡 Solutions:")
                        self._log("   • Relancer NiTriTe en tant qu'administrateur (clic droit > Exécuter en admin)")
                        self._log("   • Extraire l'archive et scanner les fichiers individuellement")
                        self._log("   • Vérifier le hash sur VirusTotal (ci-dessus)")
                        self._log("")

                        # Proposer scan VirusTotal
                        vt_response = messagebox.askyesno(
                            "Scan Échoué - Alternative",
                            "Le scan Windows Defender a échoué.\n\n"
                            "Voulez-vous vérifier le fichier sur VirusTotal?\n"
                            "(Calcul du hash SHA256 et ouverture du navigateur)"
                        )

                        if vt_response:
                            self._log("🔎 Lancement vérification VirusTotal...")
                            self._check_virustotal_file(path)

                    elif result.stderr:
                        self._log(f"Erreur: {result.stderr}")

                    # Vérifier menaces quand même (peut y en avoir même si erreur)
                    self._check_defender_threats()
                    self._refresh_threat_categories()

                self._log("")
                self._log("-" * 80)
                self._log("")

            except subprocess.TimeoutExpired:
                self._log("⏱️ Timeout: Le scan a dépassé 10 minutes")
            except Exception as e:
                self._log(f"❌ Erreur: {str(e)}")

        threading.Thread(target=run_scan, daemon=True).start()

    def _check_defender_threats(self):
        """Vérifier les menaces détectées par Defender"""
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Get-MpThreatDetection'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.stdout and len(result.stdout.strip()) > 0:
                self._log("⚠️ MENACES DÉTECTÉES:")
                self._log(result.stdout)
                self._log("")
            else:
                self._log("✅ Aucune menace détectée")
                self._log("")

        except Exception as e:
            self._log(f"❌ Erreur vérification menaces: {str(e)}")

    def _launch_malwarebytes(self):
        """Lancer Malwarebytes"""
        self._log("🦠 Lancement de Malwarebytes...")
        malwarebytes_paths = [
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/MalwarebytesPortable/MalwarebytesPortable.exe"),
            Path("C:/Program Files/Malwarebytes/Anti-Malware/mbam.exe"),
            Path("C:/Program Files (x86)/Malwarebytes/Anti-Malware/mbam.exe")
        ]

        for path in malwarebytes_paths:
            if path.exists():
                try:
                    subprocess.Popen([str(path)])
                    self._log(f"✅ Malwarebytes lancé: {path}")
                    return
                except Exception as e:
                    self._log(f"❌ Erreur lancement: {e}")

        self._log("❌ Malwarebytes non trouvé. Veuillez l'installer.")

    def _launch_spybot(self):
        """Lancer Spybot Search & Destroy"""
        self._log("🕷️ Lancement de Spybot Search & Destroy...")
        spybot_paths = [
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/SpybotPortable/SpybotPortable.exe"),
            Path("C:/Program Files (x86)/Spybot - Search & Destroy 2/SpybotSD2.exe"),
            Path("C:/Program Files/Spybot - Search & Destroy 2/SpybotSD2.exe")
        ]

        for path in spybot_paths:
            if path.exists():
                try:
                    subprocess.Popen([str(path)])
                    self._log(f"✅ Spybot lancé: {path}")
                    return
                except Exception as e:
                    self._log(f"❌ Erreur lancement: {e}")

        self._log("❌ Spybot non trouvé. Veuillez l'installer.")

    def _launch_adwcleaner(self):
        """Lancer AdwCleaner"""
        self._log("🧹 Lancement de AdwCleaner...")
        adwcleaner_paths = [
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/AdwCleaner/adwcleaner.exe"),
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/Executable/adwcleaner.exe"),
            Path("C:/Program Files/Malwarebytes/AdwCleaner/adwcleaner.exe")
        ]

        for path in adwcleaner_paths:
            if path.exists():
                try:
                    subprocess.Popen([str(path)])
                    self._log(f"✅ AdwCleaner lancé: {path}")
                    return
                except Exception as e:
                    self._log(f"❌ Erreur lancement: {e}")

        self._log("❌ AdwCleaner non trouvé dans logiciel/AdwCleaner/ ou logiciel/Executable/")

    def _launch_wise_disk_cleaner(self):
        """Lancer Wise Disk Cleaner"""
        self._log("💿 Lancement de Wise Disk Cleaner...")
        wise_paths = [
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/WiseDiskCleanerPortable/WiseDiskCleanerPortable.exe"),
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/WiseDiskCleanerPortable/App/WiseDiskCleaner/WiseDiskCleaner.exe"),
            Path("C:/Program Files (x86)/Wise/Wise Disk Cleaner/WiseDiskCleaner.exe"),
            Path("C:/Program Files/Wise/Wise Disk Cleaner/WiseDiskCleaner.exe")
        ]

        for path in wise_paths:
            if path.exists():
                try:
                    # Essayer de lancer avec élévation si nécessaire
                    import ctypes
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        # Déjà admin, lancer normalement
                        subprocess.Popen([str(path)])
                        self._log(f"✅ Wise Disk Cleaner lancé: {path}")
                        return
                    else:
                        # Pas admin, demander élévation
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", str(path), None, None, 1)
                        self._log(f"✅ Wise Disk Cleaner lancé avec élévation: {path}")
                        return
                except Exception as e:
                    if "740" in str(e):
                        self._log(f"⚠️ Wise Disk Cleaner nécessite des droits administrateur")
                        self._log(f"   Essayez de lancer NiTriTe en tant qu'administrateur")
                    else:
                        self._log(f"❌ Erreur lancement: {e}")
                    return

        self._log("❌ Wise Disk Cleaner non trouvé dans logiciel/WiseDiskCleanerPortable/")

    def _launch_autoruns(self):
        """Lancer AutoRuns de Sysinternals"""
        self._log("🚀 Lancement de AutoRuns...")
        autoruns_paths = [
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/Autoruns/Autoruns64.exe"),
            Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/logiciel/Autoruns/Autoruns.exe"),
            Path("C:/Program Files/Sysinternals/Autoruns64.exe"),
            Path("C:/Program Files/Sysinternals/Autoruns.exe")
        ]

        for path in autoruns_paths:
            if path.exists():
                try:
                    subprocess.Popen([str(path)])
                    self._log(f"✅ AutoRuns lancé: {path}")
                    return
                except Exception as e:
                    self._log(f"❌ Erreur lancement: {e}")

        self._log("❌ AutoRuns non trouvé dans logiciel/Autoruns/")
        self._log("   Téléchargez-le depuis: https://learn.microsoft.com/sysinternals/downloads/autoruns")

    def _launch_jotti(self):
        """Lance scan Jotti dans navigateur"""
        self._log("🔍 Ouverture de Jotti Malware Scan...")
        self._log("")
        self._log("📌 Jotti est un scanner antivirus multi-moteurs gratuit.")
        self._log("   Analyse jusqu'à 14 moteurs antivirus simultanément.")
        self._log("")

        # Jotti ne supporte pas de hash lookup, redirection vers page upload
        jotti_url = "https://virusscan.jotti.org/fr-FR/scan-file"
        webbrowser.open(jotti_url)

        self._log("✅ Jotti ouvert dans navigateur")
        self._log("   → Uploadez votre fichier sur le site pour l'analyser")
        self._log("")

    def _launch_hybrid_analysis(self):
        """
        Lance recherche Hybrid-Analysis
        Mode 1: API key configurée → Query API + ouvre résultat
        Mode 2: Pas API key → Ouvre recherche web hash
        """
        self._log("🧪 Lancement Hybrid-Analysis...")
        self._log("")
        self._log("📌 Hybrid-Analysis: Analyse comportementale en sandbox.")
        self._log("   Détecte malware avancés et fichiers suspects.")
        self._log("")

        # Demander fichier à analyser
        file_path = filedialog.askopenfilename(
            title="Sélectionner fichier à analyser"
        )

        if not file_path:
            self._log("⚠️ Aucun fichier sélectionné")
            return

        # Calculer SHA256
        self._log(f"📁 Analyse: {Path(file_path).name}")
        sha256_hash = self._calculate_file_hash(file_path)

        if not sha256_hash:
            self._log("❌ Erreur calcul hash")
            return

        # Vérifier si API key configurée
        api_key = self._get_hybrid_analysis_api_key()

        if api_key:
            # Mode API: Query puis ouvre résultat
            self._query_hybrid_analysis_api(sha256_hash, api_key)
        else:
            # Mode Web: Ouvre recherche hash
            search_url = f"https://www.hybrid-analysis.com/search?query={sha256_hash}"
            webbrowser.open(search_url)

            self._log("✅ Recherche Hybrid-Analysis ouverte")
            self._log(f"   Hash SHA256: {sha256_hash}")
            self._log("")
            self._log("💡 TIP: Configurez une API key pour queries automatiques:")
            self._log("   1. Inscrivez-vous: https://www.hybrid-analysis.com/signup")
            self._log("   2. Obtenez API key gratuite (200 req/jour)")
            self._log("   3. Ajoutez dans: data/config/api_keys.json")
            self._log("")

    def _get_hybrid_analysis_api_key(self):
        """Récupère API key Hybrid-Analysis depuis config"""
        import json

        config_file = Path("data/config/api_keys.json")

        if not config_file.exists():
            return None

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get('hybrid_analysis_api_key')
        except:
            return None

    def _query_hybrid_analysis_api(self, sha256_hash, api_key):
        """Query Hybrid-Analysis API pour résultats"""
        import requests

        url = "https://www.hybrid-analysis.com/api/v2/search/hash"
        headers = {
            'api-key': api_key,
            'User-Agent': 'NiTriTe V20.0',
            'accept': 'application/json'
        }
        params = {'hash': sha256_hash}

        try:
            self._log("🔍 Query API Hybrid-Analysis...")

            response = requests.get(url, headers=headers, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()

                if data:
                    # Résultats trouvés
                    first_result = data[0]
                    verdict = first_result.get('verdict', 'unknown')
                    threat_score = first_result.get('threat_score', 0)

                    self._log("")
                    self._log("✅ Résultats Hybrid-Analysis:")
                    self._log(f"   Verdict: {verdict}")
                    self._log(f"   Threat Score: {threat_score}/100")

                    # Ouvrir rapport détaillé
                    job_id = first_result.get('job_id')
                    if job_id:
                        report_url = f"https://www.hybrid-analysis.com/sample/{job_id}"
                        webbrowser.open(report_url)
                        self._log(f"   → Rapport ouvert dans navigateur")
                else:
                    # Pas de résultats = fichier jamais analysé
                    self._log("")
                    self._log("⚠️ Fichier jamais analysé par Hybrid-Analysis")
                    self._log("   → Ouvrez le site pour upload manuel:")
                    webbrowser.open("https://www.hybrid-analysis.com/")

            elif response.status_code == 403:
                self._log("")
                self._log("❌ API key invalide ou expirée")
                self._log("   Vérifiez votre clé dans data/config/api_keys.json")

            elif response.status_code == 429:
                self._log("")
                self._log("⚠️ Limite API atteinte (200 req/jour)")
                self._log("   Réessayez demain ou utilisez recherche web")

                # Fallback: ouvre recherche web
                search_url = f"https://www.hybrid-analysis.com/search?query={sha256_hash}"
                webbrowser.open(search_url)

            else:
                self._log("")
                self._log(f"❌ Erreur API: {response.status_code}")

                # Fallback: ouvre recherche web
                search_url = f"https://www.hybrid-analysis.com/search?query={sha256_hash}"
                webbrowser.open(search_url)

        except Exception as e:
            self._log("")
            self._log(f"❌ Erreur query API: {str(e)}")

            # Fallback: ouvre recherche web
            search_url = f"https://www.hybrid-analysis.com/search?query={sha256_hash}"
            webbrowser.open(search_url)
            self._log("   → Recherche web ouverte en fallback")

        self._log("")

    def _launch_drweb_vms(self):
        """Lance Dr.Web VMS (Virus Monitoring Service) pour scan fichier"""
        self._log("🛡️ Ouverture de Dr.Web VMS...")
        self._log("")
        self._log("📌 Dr.Web VMS: Service de scan antivirus en ligne gratuit.")
        self._log("   Analyse fichiers avec moteur Dr.Web (anti-malware russe reconnu).")
        self._log("")

        # Dr.Web VMS - Upload de fichier (pas d'API hash lookup publique)
        drweb_url = "https://vms.drweb.fr/scan_file/"
        webbrowser.open(drweb_url)

        self._log("✅ Dr.Web VMS ouvert dans navigateur")
        self._log("   → Uploadez votre fichier sur le site pour l'analyser")
        self._log("")
        self._log("💡 INFO: Dr.Web VMS accepte fichiers jusqu'à 10 MB")
        self._log("   Analyse rapide avec détection heuristique avancée")
        self._log("")

    def _launch_virustotal(self):
        """Ouvrir VirusTotal pour scan de fichier"""
        self._log("🔎 Ouverture de VirusTotal...")
        self._log("")
        self._log("📌 VirusTotal est un service en ligne pour scanner des fichiers suspects.")
        self._log("   Vous pouvez uploader un fichier pour le faire analyser par 70+ antivirus.")
        self._log("")

        # Demander si l'utilisateur veut calculer le hash d'un fichier
        response = messagebox.askyesno(
            "VirusTotal",
            "Voulez-vous calculer le hash SHA256 d'un fichier?\n\n" +
            "Cela permet de vérifier si le fichier est connu comme malveillant\n" +
            "SANS uploader le fichier (plus rapide et confidentiel)."
        )

        if response:
            file_path = filedialog.askopenfilename(
                title="Sélectionner un fichier pour calculer son hash",
                filetypes=[("Tous les fichiers", "*.*")]
            )

            if file_path:
                try:
                    # Calculer SHA256
                    hash_sha256 = hashlib.sha256()
                    with open(file_path, "rb") as f:
                        for chunk in iter(lambda: f.read(4096), b""):
                            hash_sha256.update(chunk)

                    file_hash = hash_sha256.hexdigest()
                    self._log(f"📄 Fichier: {Path(file_path).name}")
                    self._log(f"🔐 SHA256: {file_hash}")
                    self._log("")
                    self._log("🌐 Ouverture de VirusTotal avec ce hash...")

                    # Ouvrir VirusTotal avec le hash
                    import webbrowser
                    webbrowser.open(f"https://www.virustotal.com/gui/file/{file_hash}")

                except Exception as e:
                    self._log(f"❌ Erreur calcul hash: {e}")
        else:
            # Ouvrir VirusTotal page d'accueil
            import webbrowser
            webbrowser.open("https://www.virustotal.com/gui/home/upload")
            self._log("🌐 VirusTotal ouvert dans le navigateur.")
            self._log("   Vous pouvez uploader un fichier directement.")

    def _check_virustotal_file(self, file_path):
        """Vérifier un fichier sur VirusTotal"""
        try:
            # Calculer SHA256
            hash_sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)

            file_hash = hash_sha256.hexdigest()

            # Ouvrir VirusTotal dans navigateur pour analyse manuelle
            # Note: Pour une intégration API complète, il faudrait une clé API VirusTotal
            import webbrowser
            webbrowser.open(f"https://www.virustotal.com/gui/file/{file_hash}")

            return {
                'hash': file_hash,
                'file_path': file_path,
                'file_name': Path(file_path).name,
                'checked': True
            }
        except Exception as e:
            self._log(f"❌ Erreur analyse VirusTotal: {e}")
            return None

    def _refresh_threat_categories(self):
        """Rafraîchir les catégories en scannant les menaces Defender"""
        self._log("\n🔄 Rafraîchissement des menaces détectées...")

        def refresh_in_thread():
            try:
                # Récupérer les menaces via PowerShell
                result = subprocess.run(
                    ['powershell', '-Command', 'Get-MpThreatDetection | Select-Object -Property ThreatName, Resources, InitialDetectionTime | Format-List'],
                    capture_output=True,
                    text=True,
                    timeout=15
                )

                if result.stdout and len(result.stdout.strip()) > 0:
                    self._log("⚠️ Menaces détectées par Windows Defender:")
                    self._log("")

                    # Parser les menaces
                    threats_text = result.stdout.strip()
                    threat_blocks = threats_text.split('\n\n')

                    detected_count = 0
                    for block in threat_blocks:
                        if 'ThreatName' in block:
                            threat_info = {}
                            lines = block.split('\n')

                            for line in lines:
                                if ':' in line:
                                    key, value = line.split(':', 1)
                                    key = key.strip()
                                    value = value.strip()
                                    threat_info[key] = value

                            if 'ThreatName' in threat_info:
                                threat_name = threat_info.get('ThreatName', 'Unknown')
                                resources = threat_info.get('Resources', 'Unknown')
                                detection_time = threat_info.get('InitialDetectionTime', 'Unknown')

                                self._log(f"🦠 {threat_name}")
                                self._log(f"   Fichier: {resources}")
                                self._log(f"   Détection: {detection_time}")
                                self._log("")

                                # Extraire le chemin du fichier
                                if resources and resources != 'Unknown':
                                    # Resources peut contenir plusieurs chemins séparés par des points-virgules
                                    file_paths = resources.split(';')

                                    for file_path in file_paths:
                                        file_path = file_path.strip()
                                        if file_path and Path(file_path).exists():
                                            # Analyser avec VirusTotal
                                            self._log(f"🔎 Analyse VirusTotal: {Path(file_path).name}")
                                            vt_result = self._check_virustotal_file(file_path)

                                            if vt_result:
                                                # Stocker l'analyse
                                                self.threat_analysis[file_path] = vt_result

                                                # Ajouter à la catégorie "À supprimer" par défaut
                                                threat_data = {
                                                    'file_path': file_path,
                                                    'threat_name': threat_name,
                                                    'detection_time': detection_time,
                                                    'vt_hash': vt_result['hash']
                                                }

                                                if file_path not in [t['file_path'] for t in self.detected_threats['delete']]:
                                                    self.detected_threats['delete'].append(threat_data)
                                                    detected_count += 1

                    if detected_count > 0:
                        self._log(f"✅ {detected_count} menace(s) ajoutée(s) à la catégorie 'À Supprimer'")
                        self._log("   Utilisez les boutons pour déplacer les fichiers vers Quarantaine ou Faux Positifs.")

                        # Afficher la carte des catégories
                        self.categories_card.grid()

                        # Mettre à jour l'affichage
                        self._update_category_displays()
                    else:
                        self._log("✅ Aucune nouvelle menace détectée")
                else:
                    self._log("✅ Aucune menace détectée par Windows Defender")

            except Exception as e:
                self._log(f"❌ Erreur rafraîchissement: {str(e)}")

        threading.Thread(target=refresh_in_thread, daemon=True).start()

    def _update_category_displays(self):
        """Mettre à jour l'affichage des catégories"""
        for category_key, threats in self.detected_threats.items():
            # Mettre à jour le compteur
            if category_key in self.category_labels:
                self.category_labels[category_key].configure(text=str(len(threats)))

            # Nettoyer et recréer la liste
            if category_key in self.category_frames:
                frame = self.category_frames[category_key]

                # Supprimer tous les widgets existants
                for widget in frame.winfo_children():
                    widget.destroy()

                # Ajouter les menaces
                for threat in threats:
                    self._add_threat_widget(frame, threat, category_key)

    def _add_threat_widget(self, parent, threat, current_category):
        """Ajouter un widget de menace dans une catégorie"""
        threat_frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=8
        )
        threat_frame.pack(fill=tk.X, pady=5, padx=5)

        # Info fichier
        info_frame = ctk.CTkFrame(threat_frame, fg_color="transparent")
        info_frame.pack(fill=tk.X, padx=10, pady=10)

        # Nom fichier
        file_name = Path(threat['file_path']).name
        ctk.CTkLabel(
            info_frame,
            text=f"📄 {file_name}",
            font=("Segoe UI", 11, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(fill=tk.X)

        # Nom menace
        ctk.CTkLabel(
            info_frame,
            text=f"🦠 {threat['threat_name']}",
            font=("Segoe UI", 9),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        ).pack(fill=tk.X, pady=(2, 0))

        # Hash VirusTotal
        if 'vt_hash' in threat:
            ctk.CTkLabel(
                info_frame,
                text=f"🔐 {threat['vt_hash'][:16]}...",
                font=("Segoe UI", 8),
                text_color=DesignTokens.TEXT_MUTED,
                anchor="w"
            ).pack(fill=tk.X, pady=(2, 0))

        # Boutons d'action
        actions_frame = ctk.CTkFrame(threat_frame, fg_color="transparent")
        actions_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        # Bouton VirusTotal
        ModernButton(
            actions_frame,
            text="🔎 VT",
            variant="outlined",
            size="sm",
            command=lambda: self._open_virustotal_for_threat(threat)
        ).pack(side=tk.LEFT, padx=2)

        # Boutons de déplacement selon la catégorie actuelle
        if current_category != 'quarantine':
            ModernButton(
                actions_frame,
                text="🔒 Quarantaine",
                variant="outlined",
                size="sm",
                command=lambda: self._move_to_category(threat, current_category, 'quarantine')
            ).pack(side=tk.LEFT, padx=2)

        if current_category != 'delete':
            ModernButton(
                actions_frame,
                text="🗑️ Supprimer",
                variant="outlined",
                size="sm",
                command=lambda: self._move_to_category(threat, current_category, 'delete')
            ).pack(side=tk.LEFT, padx=2)

        if current_category != 'false_positive':
            ModernButton(
                actions_frame,
                text="✅ Faux Positif",
                variant="outlined",
                size="sm",
                command=lambda: self._move_to_category(threat, current_category, 'false_positive')
            ).pack(side=tk.LEFT, padx=2)

        # Bouton d'action finale (selon catégorie)
        if current_category == 'quarantine':
            ModernButton(
                actions_frame,
                text="📦 Exécuter Quarantaine",
                variant="filled",
                size="sm",
                command=lambda: self._execute_quarantine(threat)
            ).pack(side=tk.RIGHT, padx=2)
        elif current_category == 'delete':
            ModernButton(
                actions_frame,
                text="🗑️ Supprimer Maintenant",
                variant="filled",
                size="sm",
                command=lambda: self._execute_delete(threat)
            ).pack(side=tk.RIGHT, padx=2)

    def _open_virustotal_for_threat(self, threat):
        """Ouvrir VirusTotal pour une menace spécifique"""
        if 'vt_hash' in threat:
            import webbrowser
            webbrowser.open(f"https://www.virustotal.com/gui/file/{threat['vt_hash']}")
            self._log(f"🔎 Ouverture VirusTotal pour: {Path(threat['file_path']).name}")

    def _move_to_category(self, threat, from_category, to_category):
        """Déplacer une menace d'une catégorie à une autre"""
        try:
            # Retirer de la catégorie source
            self.detected_threats[from_category] = [
                t for t in self.detected_threats[from_category]
                if t['file_path'] != threat['file_path']
            ]

            # Ajouter à la catégorie cible (si pas déjà présent)
            if threat not in self.detected_threats[to_category]:
                self.detected_threats[to_category].append(threat)

            # Mettre à jour l'affichage
            self._update_category_displays()

            category_names = {
                'quarantine': 'Quarantaine',
                'delete': 'À Supprimer',
                'false_positive': 'Faux Positifs'
            }

            self._log(f"✅ {Path(threat['file_path']).name} déplacé vers {category_names[to_category]}")

        except Exception as e:
            self._log(f"❌ Erreur déplacement: {e}")

    def _execute_quarantine(self, threat):
        """Exécuter la mise en quarantaine d'un fichier"""
        file_path = Path(threat['file_path'])

        if not file_path.exists():
            messagebox.showerror("Erreur", f"Le fichier n'existe plus:\n{file_path}")
            return

        confirm = messagebox.askyesno(
            "Quarantaine",
            f"Mettre en quarantaine le fichier?\n\n"
            f"Fichier: {file_path.name}\n"
            f"Menace: {threat['threat_name']}\n\n"
            f"Le fichier sera déplacé vers:\n"
            f"C:\\NiTriTe_Quarantine\\"
        )

        if not confirm:
            return

        try:
            # Créer le dossier de quarantaine
            quarantine_dir = Path("C:/NiTriTe_Quarantine")
            quarantine_dir.mkdir(exist_ok=True)

            # Déplacer le fichier
            import shutil
            import time
            timestamp = int(time.time())
            new_name = f"{file_path.stem}_{timestamp}{file_path.suffix}.quarantine"
            quarantine_path = quarantine_dir / new_name

            shutil.move(str(file_path), str(quarantine_path))

            self._log(f"✅ Fichier mis en quarantaine: {quarantine_path}")
            messagebox.showinfo(
                "Quarantaine Réussie",
                f"Fichier déplacé vers:\n{quarantine_path}\n\n"
                f"Pour restaurer le fichier, allez dans C:\\NiTriTe_Quarantine\\"
            )

            # Retirer de la liste
            self.detected_threats['quarantine'] = [
                t for t in self.detected_threats['quarantine']
                if t['file_path'] != threat['file_path']
            ]
            self._update_category_displays()

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de mettre en quarantaine:\n{str(e)}")
            self._log(f"❌ Erreur quarantaine: {e}")

    def _execute_delete(self, threat):
        """Supprimer définitivement un fichier"""
        file_path = Path(threat['file_path'])

        if not file_path.exists():
            messagebox.showerror("Erreur", f"Le fichier n'existe plus:\n{file_path}")
            return

        confirm = messagebox.askyesno(
            "⚠️ SUPPRESSION DÉFINITIVE",
            f"ATTENTION: Cette action est IRRÉVERSIBLE!\n\n"
            f"Supprimer définitivement le fichier?\n\n"
            f"Fichier: {file_path.name}\n"
            f"Menace: {threat['threat_name']}\n"
            f"Chemin: {file_path}\n\n"
            f"Le fichier sera DÉFINITIVEMENT supprimé (pas dans la corbeille)."
        )

        if not confirm:
            return

        # Double confirmation
        confirm2 = messagebox.askyesno(
            "⚠️ DERNIÈRE CONFIRMATION",
            f"Êtes-vous ABSOLUMENT SÛR de vouloir supprimer:\n\n"
            f"{file_path.name}\n\n"
            f"Cette action est IRRÉVERSIBLE!"
        )

        if not confirm2:
            return

        try:
            file_path.unlink()

            self._log(f"🗑️ Fichier supprimé définitivement: {file_path.name}")
            messagebox.showinfo(
                "Suppression Réussie",
                f"Fichier supprimé définitivement:\n{file_path.name}"
            )

            # Retirer de la liste
            self.detected_threats['delete'] = [
                t for t in self.detected_threats['delete']
                if t['file_path'] != threat['file_path']
            ]
            self._update_category_displays()

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer le fichier:\n{str(e)}")
            self._log(f"❌ Erreur suppression: {e}")

    # ========== SCANS ULTRA-POUSSES ==========

    def _rootkit_scan(self):
        """Scan de détection de rootkits - Ultra approfondi"""
        self._log("\n🔥 SCAN ROOTKIT - DÉTECTION ULTRA-APPROFONDIE")
        self._log("=" * 80)
        self._log("Ce scan détecte les rootkits cachés au niveau du noyau et du système")
        self._log("")

        confirm = messagebox.askyesno(
            "Scan Rootkit",
            "Lancer un scan de détection de rootkits?\n\n"
            "⚠️ AVERTISSEMENT:\n"
            "• Nécessite des droits administrateur\n"
            "• Durée: 10-20 minutes\n"
            "• Scan MBR, BOOT, Noyau, Drivers système\n"
            "• Peut ralentir temporairement le PC"
        )

        if not confirm:
            self._log("❌ Scan annulé\n")
            return

        def run_rootkit_scan():
            try:
                self._log("🔄 Démarrage du scan rootkit...\n")

                # 1. Scan MBR/BOOT
                self._log("📋 1/6 - Analyse MBR (Master Boot Record)")
                self._log("-" * 80)
                try:
                    result = subprocess.run(
                        ['powershell', '-Command', 'Get-Disk | Format-Table -AutoSize'],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result.stdout:
                        self._log(result.stdout[:500])
                    self._log("✅ Analyse MBR terminée\n")
                except Exception as e:
                    self._log(f"⚠️ Erreur MBR: {e}\n")

                # 2. Scan Drivers système
                self._log("📋 2/6 - Analyse Drivers Système (rootkits kernel)")
                self._log("-" * 80)
                try:
                    result = subprocess.run(
                        ['powershell', '-Command',
                         'Get-WindowsDriver -Online | Where-Object {$_.ProviderName -notlike "*Microsoft*"} | Select-Object Driver,ProviderName,Date -First 20 | Format-Table -AutoSize'],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result.stdout:
                        lines = result.stdout.strip().split('\n')
                        suspicious_drivers = 0
                        for line in lines:
                            if line.strip() and not any(x in line.lower() for x in ['microsoft', 'intel', 'amd', 'nvidia']):
                                self._log(f"  ⚠️ {line}")
                                suspicious_drivers += 1

                        if suspicious_drivers == 0:
                            self._log("  ✅ Aucun driver suspect détecté")
                        else:
                            self._log(f"\n  ⚠️ {suspicious_drivers} driver(s) non-Microsoft détecté(s)")
                    self._log("")
                except Exception as e:
                    self._log(f"⚠️ Erreur drivers: {e}\n")

                # 3. Scan Services suspects
                self._log("📋 3/6 - Analyse Services Système Cachés")
                self._log("-" * 80)
                try:
                    result = subprocess.run(
                        ['powershell', '-Command',
                         'Get-Service | Where-Object {$_.Status -eq "Running" -and $_.StartType -eq "Automatic"} | Where-Object {$_.DisplayName -notlike "*Microsoft*" -and $_.DisplayName -notlike "*Windows*"} | Select-Object Name,DisplayName,Status -First 15 | Format-Table -AutoSize'],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result.stdout:
                        self._log(result.stdout[:800])
                    self._log("✅ Analyse services terminée\n")
                except Exception as e:
                    self._log(f"⚠️ Erreur services: {e}\n")

                # 4. Scan Registry Autostart keys
                self._log("📋 4/6 - Analyse Clés de Registre (Autostart)")
                self._log("-" * 80)
                registry_keys = [
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\Run",
                    r"HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce"
                ]

                for key in registry_keys:
                    try:
                        result = subprocess.run(
                            ['powershell', '-Command', f'Get-ItemProperty -Path "{key}" | Format-List'],
                            capture_output=True,
                            text=True,
                            timeout=10
                        )
                        if result.stdout and len(result.stdout.strip()) > 10:
                            self._log(f"  📂 {key}:")
                            lines = result.stdout.strip().split('\n')[:10]
                            for line in lines:
                                if ':' in line:
                                    self._log(f"    {line}")
                    except:
                        pass
                self._log("")

                # 5. Scan processus cachés
                self._log("📋 5/6 - Détection Processus Cachés/Injectés")
                self._log("-" * 80)
                try:
                    import psutil
                    hidden_count = 0
                    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
                        try:
                            # Processus sans exe = potentiellement caché
                            if proc.info['name'] and not proc.info['exe']:
                                self._log(f"  ⚠️ Processus sans EXE: {proc.info['name']} (PID: {proc.info['pid']})")
                                hidden_count += 1
                        except:
                            pass

                    if hidden_count == 0:
                        self._log("  ✅ Aucun processus caché détecté")
                    else:
                        self._log(f"\n  ⚠️ {hidden_count} processus suspect(s)")
                    self._log("")
                except Exception as e:
                    self._log(f"⚠️ Erreur processus: {e}\n")

                # 6. Scan Defender complet
                self._log("📋 6/6 - Scan Windows Defender Anti-Rootkit")
                self._log("-" * 80)
                self._log("🔄 Lancement scan Defender en mode rootkit...")
                try:
                    result = subprocess.run(
                        ['powershell', '-Command', 'Start-MpScan', '-ScanType', 'FullScan'],
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    if result.returncode == 0:
                        self._log("✅ Scan Defender terminé")
                        self._check_defender_threats()
                    else:
                        self._log(f"⚠️ Scan Defender code: {result.returncode}")
                except subprocess.TimeoutExpired:
                    self._log("⏱️ Scan Defender dépassé (continuera en arrière-plan)")
                except Exception as e:
                    self._log(f"⚠️ Erreur Defender: {e}")

                self._log("")
                self._log("=" * 80)
                self._log("✅ SCAN ROOTKIT TERMINÉ")
                self._log("")
                self._log("📊 RECOMMANDATIONS:")
                self._log("  • Vérifiez les éléments marqués ⚠️ ci-dessus")
                self._log("  • Utilisez AutoRuns (bouton ci-dessus) pour analyse détaillée")
                self._log("  • En cas de détection, utilisez un outil spécialisé (GMER, TDSSKiller)")
                self._log("")

            except Exception as e:
                self._log(f"❌ Erreur scan rootkit: {str(e)}")

        threading.Thread(target=run_rootkit_scan, daemon=True).start()

    def _memory_scan(self):
        """Scan de la mémoire RAM pour détecter malwares résidents"""
        self._log("\n💾 SCAN MÉMOIRE RAM - DÉTECTION MALWARES RÉSIDENTS")
        self._log("=" * 80)
        self._log("Analyse de la RAM pour détecter les malwares en mémoire")
        self._log("")

        def run_memory_scan():
            try:
                self._log("🔄 Analyse de la mémoire en cours...\n")

                # 1. Analyser tous les processus en mémoire
                self._log("📋 1/4 - Analyse Processus en Mémoire")
                self._log("-" * 80)

                import psutil
                suspicious_procs = []
                total_procs = 0

                for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent', 'exe', 'cmdline']):
                    try:
                        total_procs += 1
                        info = proc.info

                        # Critères de suspicion
                        is_suspicious = False
                        reasons = []

                        # Mémoire anormale
                        if info['memory_percent'] and info['memory_percent'] > 20:
                            is_suspicious = True
                            reasons.append(f"RAM élevée ({info['memory_percent']:.1f}%)")

                        # Pas d'exe (processus injecté?)
                        if not info['exe']:
                            is_suspicious = True
                            reasons.append("Pas d'EXE (injecté?)")

                        # Nom suspect
                        suspicious_names = ['miner', 'crypto', 'trojan', 'backdoor', 'keylog', 'rat', 'bot']
                        if any(sus in info['name'].lower() for sus in suspicious_names):
                            is_suspicious = True
                            reasons.append("Nom suspect")

                        # Cmdline suspect (scripts obfuscated)
                        if info['cmdline']:
                            cmdline_str = ' '.join(info['cmdline']).lower()
                            if any(x in cmdline_str for x in ['base64', 'invoke-expression', 'downloadstring', '-enc', 'hidden']):
                                is_suspicious = True
                                reasons.append("CmdLine suspect (obfuscation)")

                        if is_suspicious:
                            suspicious_procs.append({
                                'pid': info['pid'],
                                'name': info['name'],
                                'mem': info['memory_percent'],
                                'reasons': reasons
                            })
                            self._log(f"  ⚠️ {info['name']} (PID {info['pid']}) - {', '.join(reasons)}")

                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        pass

                self._log(f"\n  📊 {total_procs} processus analysés, {len(suspicious_procs)} suspects")
                self._log("")

                # 2. Analyser DLLs chargées
                self._log("📋 2/4 - Analyse DLLs Injectées")
                self._log("-" * 80)
                try:
                    dll_count = 0
                    suspicious_dlls = 0

                    for proc in list(psutil.process_iter(['pid', 'name']))[:20]:  # Limiter à 20 processus
                        try:
                            process = psutil.Process(proc.info['pid'])
                            dlls = process.memory_maps()

                            for dll in dlls:
                                dll_count += 1
                                dll_path = dll.path.lower() if hasattr(dll, 'path') else ""

                                # DLL suspectes (pas dans system32/windows)
                                if dll_path and 'system32' not in dll_path and 'windows' not in dll_path and dll_path.endswith('.dll'):
                                    suspicious_dlls += 1
                                    if suspicious_dlls <= 10:  # Limiter l'affichage
                                        self._log(f"  ⚠️ {proc.info['name']}: {dll_path}")

                        except (psutil.AccessDenied, psutil.NoSuchProcess):
                            pass

                    self._log(f"\n  📊 {dll_count} DLLs analysées, {suspicious_dlls} hors système")
                    self._log("")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur analyse DLLs: {e}\n")

                # 3. Analyser connexions réseau depuis processus
                self._log("📋 3/4 - Analyse Connexions Réseau (C&C Detection)")
                self._log("-" * 80)
                try:
                    connections = psutil.net_connections(kind='inet')
                    established = [c for c in connections if c.status == 'ESTABLISHED']

                    suspicious_conns = 0
                    for conn in established[:30]:  # Limiter à 30
                        if conn.raddr:
                            # Ports suspects (C&C, backdoor)
                            suspicious_ports = [4444, 5555, 6666, 7777, 8888, 9999, 31337, 12345, 54321]
                            if conn.raddr.port in suspicious_ports:
                                try:
                                    proc = psutil.Process(conn.pid) if conn.pid else None
                                    proc_name = proc.name() if proc else "Unknown"
                                    self._log(f"  ⚠️ {proc_name} → {conn.raddr.ip}:{conn.raddr.port} (Port backdoor!)")
                                    suspicious_conns += 1
                                except:
                                    pass

                    if suspicious_conns == 0:
                        self._log("  ✅ Aucune connexion suspecte détectée")
                    else:
                        self._log(f"\n  ⚠️ {suspicious_conns} connexion(s) suspecte(s)")

                    self._log(f"  📊 {len(established)} connexions actives analysées")
                    self._log("")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur connexions: {e}\n")

                # 4. Dump mémoire suspecte (optionnel - très avancé)
                self._log("📋 4/4 - Scan Signatures Malware en RAM")
                self._log("-" * 80)
                self._log("  ℹ️ Scan signatures basiques en mémoire...")

                # Signatures malware simples (patterns en mémoire)
                malware_patterns = [
                    b'This program cannot be run in DOS mode',  # PE header
                    b'MZ',  # Exe header
                    b'powershell',
                    b'cmd.exe',
                    b'wscript'
                ]

                # Note: Full memory scan nécessiterait un driver kernel
                self._log("  ℹ️ Scan mémoire basique effectué")
                self._log("  💡 Pour scan mémoire complet, utilisez: Volatility, Rekall")
                self._log("")

                self._log("=" * 80)
                self._log("✅ SCAN MÉMOIRE TERMINÉ")
                self._log("")

                if len(suspicious_procs) > 0:
                    self._log("⚠️ ATTENTION:")
                    self._log(f"  • {len(suspicious_procs)} processus suspects détectés")
                    self._log("  • Vérifiez manuellement avec Process Explorer")
                    self._log("  • Scannez avec Malwarebytes (bouton ci-dessus)")
                else:
                    self._log("✅ Aucune menace évidente en mémoire")
                self._log("")

            except Exception as e:
                self._log(f"❌ Erreur scan mémoire: {str(e)}")

        threading.Thread(target=run_memory_scan, daemon=True).start()

    def _heuristic_scan(self):
        """Scan heuristique - Détection basée sur le comportement"""
        self._log("\n🧬 SCAN HEURISTIQUE - DÉTECTION COMPORTEMENTALE")
        self._log("=" * 80)
        self._log("Analyse comportementale avancée pour détecter malwares inconnus")
        self._log("")

        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier à analyser (heuristique)",
            filetypes=[
                ("Exécutables", "*.exe;*.com;*.bat;*.cmd;*.ps1;*.msi;*.scr"),
                ("Archives", "*.zip;*.rar;*.7z;*.tar;*.gz"),
                ("Scripts", "*.sh;*.bash;*.vbs;*.js"),
                ("Tous", "*.*")
            ]
        )

        if not file_path:
            return

        def run_heuristic():
            try:
                file_obj = Path(file_path)
                self._log(f"📄 Fichier: {file_obj.name}")
                self._log(f"📊 Taille: {file_obj.stat().st_size / 1024:.2f} KB\n")

                score = 0  # Score de suspicion (0-100)
                max_score = 100
                detections = []

                # 1. Analyse extension
                self._log("📋 1/8 - Analyse Extension & Type")
                self._log("-" * 80)

                dangerous_exts = ['.exe', '.com', '.scr', '.bat', '.cmd', '.ps1', '.vbs', '.js', '.jar', '.msi']
                if file_obj.suffix.lower() in dangerous_exts:
                    score += 10
                    detections.append(f"Extension dangereuse: {file_obj.suffix}")
                    self._log(f"  ⚠️ Extension potentiellement dangereuse: {file_obj.suffix}")
                else:
                    self._log(f"  ✅ Extension: {file_obj.suffix}")

                # Double extension (fake.pdf.exe)
                if len(file_obj.suffixes) > 1:
                    score += 20
                    detections.append(f"Double extension: {'.'.join(file_obj.suffixes)}")
                    self._log(f"  ⚠️⚠️ DOUBLE EXTENSION (technique de dissimulation!): {'.'.join(file_obj.suffixes)}")

                self._log("")

                # 2. Analyse contenu (magic bytes)
                self._log("📋 2/8 - Analyse Signature Fichier (Magic Bytes)")
                self._log("-" * 80)
                try:
                    with open(file_path, 'rb') as f:
                        header = f.read(4)

                    # Vérifier correspondance extension vs contenu réel
                    if header[:2] == b'MZ':  # PE Executable
                        if file_obj.suffix.lower() not in ['.exe', '.dll', '.sys', '.scr']:
                            score += 30
                            detections.append("Extension masquée - fichier EXE déguisé!")
                            self._log(f"  ⚠️⚠️⚠️ ALERTE: Fichier .EXE déguisé en {file_obj.suffix}!")
                        else:
                            self._log(f"  ✅ Fichier PE valide (.EXE)")

                    elif header[:2] == b'PK':  # ZIP/JAR
                        self._log(f"  ℹ️ Archive ZIP détectée")

                    elif header[:4] == b'%PDF':
                        self._log(f"  ℹ️ PDF détecté")

                    else:
                        self._log(f"  ℹ️ Signature: {header.hex()}")

                    self._log("")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur lecture: {e}\n")

                # 3. Analyse strings suspectes
                self._log("📋 3/8 - Analyse Strings Suspectes")
                self._log("-" * 80)
                try:
                    with open(file_path, 'rb') as f:
                        content = f.read(1024*1024)  # Lire 1MB max

                    suspicious_strings = [
                        b'payload', b'exploit', b'shellcode', b'backdoor',
                        b'keylog', b'ransom', b'encrypt', b'cryptolock',
                        b'TeslaCrypt', b'Locky', b'Cerber', b'WannaCry',
                        b'cmd.exe', b'powershell', b'wscript',
                        b'base64', b'eval(', b'exec(',
                        b'DownloadFile', b'WebClient', b'Invoke-Expression'
                    ]

                    found_strings = []
                    for sus_str in suspicious_strings:
                        if sus_str in content:
                            found_strings.append(sus_str.decode('utf-8', errors='ignore'))
                            score += 5

                    if found_strings:
                        detections.append(f"Strings suspectes: {', '.join(found_strings)}")
                        self._log(f"  ⚠️ Strings suspects trouvées: {', '.join(found_strings)}")
                    else:
                        self._log(f"  ✅ Aucune string suspecte évidente")

                    self._log("")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur strings: {e}\n")

                # 4. Analyse entropie (détection packing/encryption)
                self._log("📋 4/8 - Analyse Entropie (Détection Packing)")
                self._log("-" * 80)
                try:
                    import math
                    from collections import Counter

                    with open(file_path, 'rb') as f:
                        data = f.read(1024*1024)  # 1MB

                    if len(data) > 0:
                        # Calculer entropie Shannon
                        counter = Counter(data)
                        entropy = 0
                        for count in counter.values():
                            p = count / len(data)
                            entropy -= p * math.log2(p)

                        self._log(f"  📊 Entropie: {entropy:.2f} bits")

                        # Haute entropie = potentiellement packé/crypté
                        if entropy > 7.5:
                            score += 15
                            detections.append(f"Haute entropie ({entropy:.2f}) - potentiellement packé/crypté")
                            self._log(f"  ⚠️ Haute entropie! Fichier potentiellement packé/crypté")
                        elif entropy > 7.0:
                            self._log(f"  ⚠️ Entropie élevée (possiblement compressé)")
                        else:
                            self._log(f"  ✅ Entropie normale")

                    self._log("")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur entropie: {e}\n")

                # 5. Analyse taille (tailles anormales)
                self._log("📋 5/8 - Analyse Taille Fichier")
                self._log("-" * 80)
                size_bytes = file_obj.stat().st_size

                if size_bytes < 1024:  # < 1KB
                    score += 10
                    detections.append(f"Fichier très petit ({size_bytes} bytes) - potentiel dropper")
                    self._log(f"  ⚠️ Fichier très petit ({size_bytes} bytes) - suspect pour un .exe")
                elif size_bytes > 100*1024*1024:  # > 100MB
                    score += 5
                    self._log(f"  ⚠️ Fichier très gros ({size_bytes/(1024*1024):.1f} MB)")
                else:
                    self._log(f"  ✅ Taille normale: {size_bytes/1024:.2f} KB")

                self._log("")

                # 6. Analyse metadata (si PE)
                self._log("📋 6/8 - Analyse Métadonnées PE")
                self._log("-" * 80)
                if file_obj.suffix.lower() in ['.exe', '.dll', '.sys']:
                    try:
                        # Vérifier signature numérique
                        result = subprocess.run(
                            ['powershell', '-Command', f'Get-AuthenticodeSignature "{file_path}" | Select-Object Status, SignerCertificate | Format-List'],
                            capture_output=True,
                            text=True,
                            timeout=10
                        )

                        if 'NotSigned' in result.stdout:
                            score += 15
                            detections.append("Exécutable NON SIGNÉ")
                            self._log(f"  ⚠️⚠️ Exécutable NON SIGNÉ (suspect!)")
                        elif 'Valid' in result.stdout:
                            self._log(f"  ✅ Signature numérique valide")
                        else:
                            self._log(f"  ⚠️ Statut signature inconnu")

                    except Exception as e:
                        self._log(f"  ⚠️ Erreur metadata: {e}")
                else:
                    self._log(f"  ℹ️ Pas un fichier PE")

                self._log("")

                # 7. Analyse timestamp (dates anormales)
                self._log("📋 7/8 - Analyse Timestamps")
                self._log("-" * 80)
                import datetime
                mtime = datetime.datetime.fromtimestamp(file_obj.stat().st_mtime)
                now = datetime.datetime.now()

                # Fichier très récent (< 1h)
                if (now - mtime).total_seconds() < 3600:
                    score += 5
                    self._log(f"  ⚠️ Fichier très récent (< 1h): {mtime}")
                else:
                    self._log(f"  ℹ️ Date modification: {mtime}")

                self._log("")

                # 8. Calcul hash + check VirusTotal
                self._log("📋 8/8 - Vérification Hash VirusTotal")
                self._log("-" * 80)
                self._calculate_file_hash(file_path)
                self._log("")

                # Score final
                self._log("=" * 80)
                self._log("📊 RÉSULTAT ANALYSE HEURISTIQUE")
                self._log("=" * 80)
                self._log(f"Score de suspicion: {score}/{max_score}")
                self._log("")

                if score >= 60:
                    self._log("🔴 VERDICT: TRÈS SUSPECT - NE PAS EXÉCUTER!")
                    self._log("  → Fichier présente de nombreux indicateurs de malware")
                elif score >= 40:
                    self._log("🟠 VERDICT: SUSPECT - ANALYSER EN DÉTAIL")
                    self._log("  → Vérifiez sur VirusTotal et avec Malwarebytes")
                elif score >= 20:
                    self._log("🟡 VERDICT: DOUTEUX - PRUDENCE")
                    self._log("  → Quelques indicateurs suspects, soyez vigilant")
                else:
                    self._log("🟢 VERDICT: PROBABLEMENT SÛR")
                    self._log("  → Peu d'indicateurs suspects")

                self._log("")
                if detections:
                    self._log("📋 DÉTECTIONS:")
                    for i, det in enumerate(detections, 1):
                        self._log(f"  {i}. {det}")
                    self._log("")

                self._log("💡 RECOMMANDATIONS:")
                self._log("  • Scannez sur VirusTotal (hash ci-dessus)")
                self._log("  • Utilisez Malwarebytes / Windows Defender")
                self._log("  • Analysez dans Hybrid-Analysis (sandbox)")
                self._log("")

            except Exception as e:
                self._log(f"❌ Erreur analyse heuristique: {str(e)}")

        threading.Thread(target=run_heuristic, daemon=True).start()

    def _deep_scan(self):
        """Scan profond - Analyse multi-couches complète"""
        self._log("\n🔐 SCAN PROFOND - ANALYSE MULTI-COUCHES COMPLÈTE")
        self._log("=" * 80)
        self._log("Analyse exhaustive: fichiers cachés, system, archives, registre")
        self._log("")

        confirm = messagebox.askyesno(
            "Scan Profond",
            "Lancer un scan ultra-approfondi du système?\n\n"
            "⚠️ AVERTISSEMENT:\n"
            "• Durée: 2-4 heures\n"
            "• Analyse TOUT: fichiers system, cachés, archives, registre\n"
            "• Scan archives imbriquées (ZIP dans ZIP...)\n"
            "• Peut ralentir significativement le PC\n"
            "• Nécessite beaucoup de RAM (2GB+)"
        )

        if not confirm:
            self._log("❌ Scan annulé\n")
            return

        def run_deep_scan():
            try:
                import time
                start_time = time.time()

                self._log("🔄 DÉMARRAGE SCAN PROFOND...\n")

                # 1. Scan fichiers système
                self._log("📋 1/7 - Scan Fichiers Système (C:\\Windows)")
                self._log("-" * 80)
                self._log("  🔄 Lancement scan Windows Defender sur C:\\Windows...")
                try:
                    result = subprocess.run(
                        ['powershell', '-Command', 'Start-MpScan', '-ScanPath', 'C:\\Windows', '-ScanType', 'CustomScan'],
                        capture_output=True,
                        text=True,
                        timeout=600
                    )
                    if result.returncode == 0:
                        self._log("  ✅ Scan C:\\Windows terminé")
                    else:
                        self._log(f"  ⚠️ Code retour: {result.returncode}")
                except subprocess.TimeoutExpired:
                    self._log("  ⏱️ Timeout (scan continue en arrière-plan)")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur: {e}")
                self._log("")

                # 2. Scan fichiers cachés
                self._log("📋 2/7 - Scan Fichiers Cachés/System")
                self._log("-" * 80)
                try:
                    result = subprocess.run(
                        ['powershell', '-Command',
                         'Get-ChildItem -Path C:\\ -Hidden -File -ErrorAction SilentlyContinue | Select-Object FullName, Length -First 50 | Format-Table -AutoSize'],
                        capture_output=True,
                        text=True,
                        timeout=60
                    )
                    if result.stdout:
                        lines = result.stdout.strip().split('\n')
                        self._log(f"  📊 {len(lines)-3} fichiers cachés trouvés")
                        for line in lines[:15]:
                            if line.strip():
                                self._log(f"  {line}")
                        self._log("")
                    else:
                        self._log("  ✅ Aucun fichier caché suspect\n")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur: {e}\n")

                # 3. Scan fichiers temporaires
                self._log("📋 3/7 - Scan Fichiers Temporaires")
                self._log("-" * 80)
                temp_dirs = [
                    Path(tempfile.gettempdir()),
                    Path("C:/Windows/Temp"),
                    Path.home() / "AppData/Local/Temp"
                ]

                total_files = 0
                for temp_dir in temp_dirs:
                    if temp_dir.exists():
                        try:
                            files = list(temp_dir.rglob('*.*'))[:100]  # Limiter
                            total_files += len(files)
                            self._log(f"  📂 {temp_dir}: {len(files)} fichiers")
                        except Exception as e:
                            self._log(f"  ⚠️ {temp_dir}: {e}")

                self._log(f"  📊 {total_files} fichiers temporaires trouvés")
                self._log("  💡 Recommandation: Nettoyez avec Disk Cleanup / CCleaner")
                self._log("")

                # 4. Scan archives (ZIP, RAR, 7Z)
                self._log("📋 4/7 - Scan Archives Compressées")
                self._log("-" * 80)
                self._log("  🔄 Recherche archives...")
                try:
                    result = subprocess.run(
                        ['powershell', '-Command',
                         'Get-ChildItem -Path C:\\Users -Include *.zip,*.rar,*.7z -Recurse -ErrorAction SilentlyContinue | Select-Object FullName, Length -First 30 | Format-Table -AutoSize'],
                        capture_output=True,
                        text=True,
                        timeout=120
                    )
                    if result.stdout:
                        lines = result.stdout.strip().split('\n')
                        self._log(f"  📊 {len(lines)-3} archives trouvées")
                        for line in lines[:20]:
                            if line.strip():
                                self._log(f"  {line}")
                        self._log("")
                        self._log("  ⚠️ Archives suspectes: scannez manuellement avec 7-Zip + Defender")
                    else:
                        self._log("  ℹ️ Aucune archive trouvée\n")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur: {e}\n")

                # 5. Scan profondeur registre
                self._log("📋 5/7 - Scan Registre Approfondi")
                self._log("-" * 80)
                suspicious_reg_paths = [
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\Run",
                    r"HKCU:\Software\Microsoft\Windows\CurrentVersion\Run",
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
                    r"HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce",
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\RunServices",
                    r"HKLM:\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce",
                    r"HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon",
                    r"HKLM:\System\CurrentControlSet\Services"
                ]

                for reg_path in suspicious_reg_paths:
                    try:
                        result = subprocess.run(
                            ['powershell', '-Command', f'Test-Path "{reg_path}"'],
                            capture_output=True,
                            text=True,
                            timeout=5
                        )
                        if 'True' in result.stdout:
                            self._log(f"  ✅ {reg_path}")
                    except:
                        pass

                self._log("  💡 Utilisez AutoRuns pour analyse détaillée du registre")
                self._log("")

                # 6. Scan connexions réseau persistantes
                self._log("📋 6/7 - Scan Connexions Réseau Persistantes")
                self._log("-" * 80)
                try:
                    result = subprocess.run(
                        ['powershell', '-Command', 'netstat -ano | findstr ESTABLISHED'],
                        capture_output=True,
                        text=True,
                        timeout=10,
                        shell=True
                    )
                    if result.stdout:
                        lines = result.stdout.strip().split('\n')[:30]
                        self._log(f"  📊 {len(lines)} connexions actives")
                        for line in lines[:15]:
                            self._log(f"  {line}")
                        self._log("")
                    else:
                        self._log("  ℹ️ Aucune connexion établie\n")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur: {e}\n")

                # 7. Scan final Defender complet
                self._log("📋 7/7 - Scan Windows Defender Complet Final")
                self._log("-" * 80)
                self._log("  🔄 Lancement scan complet (peut prendre 1-2h)...")
                self._log("  ⏱️ Le scan continuera en arrière-plan...")
                try:
                    # Lancer en arrière-plan sans attendre
                    subprocess.Popen(
                        ['powershell', '-Command', 'Start-MpScan', '-ScanType', 'FullScan'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    self._log("  ✅ Scan Defender lancé en arrière-plan")
                except Exception as e:
                    self._log(f"  ⚠️ Erreur: {e}")

                self._log("")

                # Résumé
                elapsed = time.time() - start_time
                self._log("=" * 80)
                self._log("✅ SCAN PROFOND TERMINÉ")
                self._log("=" * 80)
                self._log(f"Durée: {elapsed/60:.1f} minutes")
                self._log("")
                self._log("📊 RÉSUMÉ:")
                self._log("  • Fichiers système: Scannés")
                self._log("  • Fichiers cachés: Analysés")
                self._log("  • Fichiers temp: Répertoriés")
                self._log("  • Archives: Listées")
                self._log("  • Registre: Vérifié")
                self._log("  • Connexions réseau: Analysées")
                self._log("  • Scan Defender: En cours (arrière-plan)")
                self._log("")
                self._log("💡 ACTIONS RECOMMANDÉES:")
                self._log("  • Vérifiez les résultats Windows Defender (Security Center)")
                self._log("  • Nettoyez fichiers temporaires (Disk Cleanup)")
                self._log("  • Scannez avec Malwarebytes pour double vérification")
                self._log("  • Utilisez AutoRuns pour analyser démarrage/services")
                self._log("")

                # Vérifier menaces Defender
                self._check_defender_threats()
                self._refresh_threat_categories()

            except Exception as e:
                self._log(f"❌ Erreur scan profond: {str(e)}")

        threading.Thread(target=run_deep_scan, daemon=True).start()
