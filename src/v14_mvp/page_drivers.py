#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Drivers - NiTriTe V20.0
Installation silencieuse de drivers depuis le dossier Drivers/
"""

import customtkinter as ctk
import tkinter as tk
from pathlib import Path
import subprocess
import os
import sys
import threading
from datetime import datetime
from tkinter import messagebox
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader

# Import du système de chemins portables
try:
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from portable_paths import get_portable_temp_dir
except ImportError:
    def get_portable_temp_dir(subfolder=None):
        import tempfile
        if subfolder:
            return Path(tempfile.gettempdir()) / "nitrite_temp" / subfolder
        return Path(tempfile.gettempdir()) / "nitrite_temp"


def create_portable_temp_file(suffix='.bat', content=''):
    """
    Créer un fichier temporaire dans le dossier temp portable

    Args:
        suffix: Extension du fichier (.bat, .ps1, etc.)
        content: Contenu à écrire dans le fichier

    Returns:
        str: Chemin absolu du fichier temporaire créé
    """
    import tempfile
    temp_dir = get_portable_temp_dir('scripts')
    temp_file_path = temp_dir / f'script_{os.getpid()}_{int(datetime.now().timestamp())}{suffix}'

    # Déterminer l'encodage selon l'extension
    encoding = 'cp1252' if suffix == '.bat' else 'utf-8'

    with open(temp_file_path, 'w', encoding=encoding) as f:
        f.write(content)

    return str(temp_file_path)


class DriversPage(ctk.CTkFrame):
    """Page de gestion et installation des drivers"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Chemin du dossier drivers
        self.drivers_folder = Path("C:/Users/Utilisateur/Downloads/Nitrite-V20.0/Drivers")

        # Configurer grid layout
        self.grid_rowconfigure(0, weight=0)  # Header fixe
        self.grid_rowconfigure(1, weight=1)  # Contenu scrollable
        self.grid_columnconfigure(0, weight=1)

        self._create_header()
        self._create_content()

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre
        title_frame = SectionHeader(container, text="🔧 Gestionnaire de Drivers")
        title_frame.pack(side=tk.LEFT)

        # Boutons d'action
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)

        ModernButton(
            actions,
            text="🔄 Actualiser",
            variant="outlined",
            command=self._refresh_drivers_list
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="📂 Ouvrir Dossier",
            variant="outlined",
            command=self._open_drivers_folder
        ).pack(side=tk.LEFT, padx=5)

    def _create_content(self):
        """Contenu scrollable avec liste des drivers"""
        # Frame scrollable
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        self.scroll_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

        # Section Pilotes Génériques Windows (PREMIÈRE sous-catégorie)
        self._create_windows_generic_drivers_section()

        # Section Drivers Recommandés
        self._create_recommended_drivers()

        # Charger la liste des drivers depuis le dossier
        self._load_drivers()

    def _create_recommended_drivers(self):
        """Section avec drivers courants recommandés"""
        recommended_card = ModernCard(self.scroll_frame)
        recommended_card.pack(fill=tk.X, padx=20, pady=10)

        container = ctk.CTkFrame(recommended_card, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre section
        SectionHeader(container, text="⭐ Drivers Recommandés").pack(anchor="w", pady=(0, 15))

        # Grid pour les cartes de drivers
        drivers_grid = ctk.CTkFrame(container, fg_color="transparent")
        drivers_grid.pack(fill=tk.X)

        # Définir les drivers recommandés
        recommended = [
            {
                "name": "Microsoft Visual C++ Redistributables",
                "description": "Packs runtime Visual C++ 2015-2022 (x64 et x86)",
                "icon": "📦",
                "command": self._install_vcredist
            },
            {
                "name": "DirectX End-User Runtime",
                "description": "Bibliothèques DirectX pour jeux et applications 3D",
                "icon": "🎮",
                "command": self._install_directx
            },
            {
                "name": "Intel Rapid Storage Technology (RST)",
                "description": "Driver pour contrôleurs SATA/RAID Intel",
                "icon": "💾",
                "command": self._install_rst
            },
            {
                "name": ".NET Framework 4.8 + SDK",
                "description": ".NET Framework 4.8 pour applications Windows",
                "icon": "⚙️",
                "command": self._install_dotnet_sdk
            },
            {
                "name": "Java Runtime Environment (JRE)",
                "description": "Java RE pour exécuter applications Java",
                "icon": "☕",
                "command": self._install_java
            },
            {
                "name": "Python 3.12",
                "description": "Langage Python pour scripts et applications",
                "icon": "🐍",
                "command": self._install_python
            },
            {
                "name": "Realtek Audio Drivers",
                "description": "Drivers audio Realtek HD",
                "icon": "🔊",
                "command": self._install_realtek_audio
            },
            {
                "name": "Bluetooth Drivers",
                "description": "Drivers Bluetooth Intel/Realtek",
                "icon": "📡",
                "command": self._install_bluetooth
            },
            {
                "name": "Chipset Drivers (Intel/AMD)",
                "description": "Drivers chipset pour carte mère",
                "icon": "🔌",
                "command": self._install_chipset
            },
            {
                "name": "GPU Drivers Auto-Detect",
                "description": "Détection et installation drivers GPU (NVIDIA/AMD/Intel)",
                "icon": "🖥️",
                "command": self._install_gpu_drivers
            },
            {
                "name": "Wi-Fi Drivers",
                "description": "Drivers Wi-Fi Intel/Realtek/Broadcom",
                "icon": "📶",
                "command": self._install_wifi
            },
            {
                "name": "Webcam Drivers",
                "description": "Drivers webcam génériques et spécifiques",
                "icon": "📷",
                "command": self._install_webcam
            }
        ]

        # Créer une carte pour chaque driver
        for i, driver in enumerate(recommended):
            row = i // 2
            col = i % 2

            driver_frame = ctk.CTkFrame(drivers_grid, fg_color=DesignTokens.BG_ELEVATED, corner_radius=10)
            driver_frame.grid(row=row, column=col, sticky="ew", padx=5, pady=5)

            # Configurer colonnes
            if col == 0:
                drivers_grid.grid_columnconfigure(0, weight=1)
            else:
                drivers_grid.grid_columnconfigure(1, weight=1)

            # Contenu de la carte
            card_content = ctk.CTkFrame(driver_frame, fg_color="transparent")
            card_content.pack(fill=tk.BOTH, expand=True, padx=15, pady=12)

            # Icône + Nom
            header_frame = ctk.CTkFrame(card_content, fg_color="transparent")
            header_frame.pack(fill=tk.X, pady=(0, 5))

            ctk.CTkLabel(
                header_frame,
                text=driver["icon"],
                font=("Segoe UI", 20)
            ).pack(side=tk.LEFT, padx=(0, 8))

            ctk.CTkLabel(
                header_frame,
                text=driver["name"],
                font=("Segoe UI", 13, "bold"),
                text_color=DesignTokens.TEXT_PRIMARY
            ).pack(side=tk.LEFT)

            # Description
            ctk.CTkLabel(
                card_content,
                text=driver["description"],
                font=("Segoe UI", 10),
                text_color=DesignTokens.TEXT_SECONDARY,
                wraplength=250,
                anchor="w",
                justify="left"
            ).pack(fill=tk.X, pady=(0, 8))

            # Bouton installation
            ModernButton(
                card_content,
                text="📥 Installer",
                variant="filled",
                size="sm",
                command=driver["command"]
            ).pack(anchor="w")

    def _load_drivers(self):
        """Scanner le dossier et afficher les drivers par catégorie"""
        # Recréer les drivers recommandés
        self._create_recommended_drivers()

        # Vérifier si le dossier existe
        if not self.drivers_folder.exists():
            self._show_no_folder_message()
            return

        # Scan des drivers
        drivers = self._scan_drivers_folder()

        if not drivers:
            self._show_no_drivers_message()
            return

        # Afficher statistiques
        self._create_stats_section(len(drivers))

        # Regrouper par catégorie
        categories = {}
        for driver in drivers:
            category = driver['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(driver)

        # Afficher chaque catégorie séparément
        for category_name, category_drivers in sorted(categories.items()):
            self._create_category_section(category_name, category_drivers)

    def _scan_drivers_folder(self):
        """Scanner le dossier et retourner la liste des drivers"""
        drivers = []

        # Extensions de drivers supportées
        driver_extensions = ['.exe', '.msi', '.inf', '.cab']

        try:
            for file_path in self.drivers_folder.rglob('*'):
                if file_path.is_file() and file_path.suffix.lower() in driver_extensions:
                    driver_info = {
                        'name': file_path.name,
                        'path': str(file_path),
                        'size': file_path.stat().st_size,
                        'type': file_path.suffix.lower(),
                        'category': file_path.parent.name if file_path.parent != self.drivers_folder else "Racine"
                    }
                    drivers.append(driver_info)
        except Exception as e:
            print(f"Erreur scan drivers: {e}")

        # Trier par catégorie puis par nom
        drivers.sort(key=lambda x: (x['category'], x['name']))

        return drivers

    def _create_stats_section(self, driver_count):
        """Section statistiques"""
        stats_card = ModernCard(self.scroll_frame)
        stats_card.pack(fill=tk.X, padx=20, pady=10)

        stats_container = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_container.pack(fill=tk.X, padx=20, pady=15)

        # Icône + Texte
        ctk.CTkLabel(
            stats_container,
            text=f"📊 {driver_count} driver(s) détecté(s)",
            font=("Segoe UI", 16, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT)

        # Bouton installer tout
        ModernButton(
            stats_container,
            text="⚡ Installer Tout",
            variant="filled",
            command=self._install_all_drivers
        ).pack(side=tk.RIGHT)

    def _create_category_section(self, category_name, drivers):
        """Créer une section pour une catégorie de drivers"""
        # Carte pour la catégorie
        category_card = ModernCard(self.scroll_frame)
        category_card.pack(fill=tk.X, padx=20, pady=10)

        category_container = ctk.CTkFrame(category_card, fg_color="transparent")
        category_container.pack(fill=tk.X, padx=20, pady=15)

        # Header de la catégorie
        header_frame = ctk.CTkFrame(category_container, fg_color="transparent")
        header_frame.pack(fill=tk.X, pady=(0, 10))

        # Nom de la catégorie
        SectionHeader(
            header_frame,
            text=f"📁 {category_name} ({len(drivers)} driver{'s' if len(drivers) > 1 else ''})"
        ).pack(side=tk.LEFT)

        # Liste des drivers de cette catégorie
        for driver in drivers:
            self._create_driver_card_inline(category_container, driver)

    def _create_driver_card_inline(self, parent, driver):
        """Créer une carte inline pour un driver dans une catégorie"""
        card_frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
        card_frame.pack(fill=tk.X, pady=5)

        container = ctk.CTkFrame(card_frame, fg_color="transparent")
        container.pack(fill=tk.X, padx=15, pady=10)

        # Gauche: Info driver
        left_frame = ctk.CTkFrame(container, fg_color="transparent")
        left_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Icône selon le type
        type_icons = {
            '.exe': '⚙️',
            '.msi': '📦',
            '.inf': '📄',
            '.cab': '🗃️'
        }
        icon = type_icons.get(driver['type'], '📁')

        # Nom du driver
        name_label = ctk.CTkLabel(
            left_frame,
            text=f"{icon} {driver['name']}",
            font=("Segoe UI", 13, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")

        # Détails (sans catégorie car déjà dans le header)
        size_mb = driver['size'] / (1024 * 1024)
        details = f"Taille: {size_mb:.2f} MB • Type: {driver['type'][1:].upper()}"

        ctk.CTkLabel(
            left_frame,
            text=details,
            font=("Segoe UI", 10),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        ).pack(anchor="w", pady=(2, 0))

        # Droite: Boutons d'action
        right_frame = ctk.CTkFrame(container, fg_color="transparent")
        right_frame.pack(side=tk.RIGHT)

        ModernButton(
            right_frame,
            text="▶ Installer",
            variant="filled",
            size="sm",
            command=lambda d=driver: self._install_driver(d)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            right_frame,
            text="🌐 Site Web",
            variant="outlined",
            size="sm",
            command=lambda d=driver: self._open_driver_website(d)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            right_frame,
            text="📂 Ouvrir",
            variant="outlined",
            size="sm",
            command=lambda d=driver: self._open_driver_location(d)
        ).pack(side=tk.LEFT)

    def _install_driver(self, driver):
        """Installer un driver en mode silencieux"""
        driver_path = driver['path']
        driver_name = driver['name']
        driver_type = driver['type']

        # Confirmer installation
        confirm = messagebox.askyesno(
            "Confirmer installation",
            f"Installer le driver :\n\n{driver_name}\n\nL'installation sera silencieuse."
        )

        if not confirm:
            return

        try:
            # Arguments d'installation silencieuse selon le type
            if driver_type == '.exe':
                # Essayer plusieurs flags silencieux communs
                commands = [
                    [driver_path, '/S'],                   # NSIS
                    [driver_path, '/VERYSILENT'],          # Inno Setup
                    [driver_path, '/silent'],              # Générique
                    [driver_path, '/q'],                   # MSI-like
                    [driver_path, '-silent'],              # Alternative
                ]

                success = False
                for cmd in commands:
                    try:
                        subprocess.run(cmd, check=True, timeout=300)
                        success = True
                        break
                    except:
                        continue

                if not success:
                    # Fallback: Installation interactive
                    subprocess.Popen([driver_path], shell=True)
                    messagebox.showinfo(
                        "Installation lancée",
                        f"Installation interactive lancée pour:\n{driver_name}\n\n"
                        "Le mode silencieux n'est pas supporté par cet installeur."
                    )
                    return

            elif driver_type == '.msi':
                # MSI en mode silencieux
                subprocess.run(
                    ['msiexec', '/i', driver_path, '/qn', '/norestart'],
                    check=True,
                    timeout=300
                )

            elif driver_type == '.inf':
                # Installation INF via pnputil
                subprocess.run(
                    ['pnputil', '/add-driver', driver_path, '/install'],
                    check=True,
                    timeout=300
                )

            elif driver_type == '.cab':
                # Installation CAB via DISM
                subprocess.run(
                    ['dism', '/online', '/add-driver', f'/driver:{driver_path}'],
                    check=True,
                    timeout=300
                )

            messagebox.showinfo(
                "Installation réussie",
                f"✅ Driver installé avec succès :\n\n{driver_name}\n\n"
                "Redémarrez si nécessaire."
            )

        except subprocess.TimeoutExpired:
            messagebox.showerror(
                "Timeout",
                f"Installation timeout (>5 min) pour:\n{driver_name}\n\n"
                "Le driver peut toujours s'installer en arrière-plan."
            )
        except Exception as e:
            messagebox.showerror(
                "Erreur installation",
                f"Impossible d'installer le driver:\n{driver_name}\n\nErreur: {str(e)}"
            )

    def _install_all_drivers(self):
        """Installer tous les drivers en séquence"""
        confirm = messagebox.askyesno(
            "Confirmer installation globale",
            "Installer TOUS les drivers détectés ?\n\n"
            "Cette opération peut prendre plusieurs minutes.\n"
            "Les drivers seront installés en séquence."
        )

        if not confirm:
            return

        drivers = self._scan_drivers_folder()
        total = len(drivers)
        installed = 0
        failed = 0

        for i, driver in enumerate(drivers, 1):
            try:
                messagebox.showinfo(
                    f"Installation {i}/{total}",
                    f"Installation du driver:\n{driver['name']}"
                )

                self._install_driver(driver)
                installed += 1
            except:
                failed += 1

        messagebox.showinfo(
            "Installation terminée",
            f"Installation globale terminée:\n\n"
            f"✅ Installés: {installed}/{total}\n"
            f"❌ Échecs: {failed}\n\n"
            "Redémarrez votre PC si nécessaire."
        )

    def _refresh_drivers_list(self):
        """Actualiser la liste des drivers"""
        self._load_drivers()

    def _open_drivers_folder(self):
        """Ouvrir le dossier Drivers dans l'explorateur"""
        try:
            if self.drivers_folder.exists():
                os.startfile(self.drivers_folder)
            else:
                messagebox.showwarning(
                    "Dossier introuvable",
                    f"Le dossier Drivers n'existe pas:\n{self.drivers_folder}"
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n{str(e)}")

    def _open_driver_website(self, driver):
        """Ouvrir le site web pour télécharger le driver"""
        import webbrowser

        # Dictionnaire de correspondance nom de fichier -> URL
        driver_urls = {
            # NVIDIA
            'nvidia': 'https://www.nvidia.com/Download/index.aspx',
            'geforce': 'https://www.nvidia.com/Download/index.aspx',

            # AMD
            'amd': 'https://www.amd.com/en/support',
            'radeon': 'https://www.amd.com/en/support',

            # Intel
            'intel': 'https://www.intel.com/content/www/us/en/download-center/home.html',

            # Realtek
            'realtek': 'https://www.realtek.com/en/downloads',

            # Microsoft
            'vcredist': 'https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist',
            'dotnet': 'https://dotnet.microsoft.com/download',
            'directx': 'https://www.microsoft.com/en-us/download/details.aspx?id=35',

            # Autres
            'chipset': 'https://www.intel.com/content/www/us/en/support/products/details/motherboards.html'
        }

        # Essayer de trouver une URL correspondante
        driver_name = driver['name'].lower()
        url = None

        for keyword, driver_url in driver_urls.items():
            if keyword in driver_name:
                url = driver_url
                break

        # Si pas d'URL trouvée, recherche Google
        if not url:
            search_query = driver['name'].replace('.exe', '').replace('.msi', '').replace('.inf', '').replace('.cab', '')
            url = f"https://www.google.com/search?q={search_query}+download+official+site"

        try:
            webbrowser.open(url)
            messagebox.showinfo(
                "Site Web",
                f"Ouverture du site web pour:\n{driver['name']}\n\nURL: {url}"
            )
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le site web:\n{str(e)}")

    def _open_driver_location(self, driver):
        """Ouvrir l'emplacement d'un driver"""
        try:
            folder_path = Path(driver['path']).parent
            os.startfile(folder_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir l'emplacement:\n{str(e)}")

    def _show_no_folder_message(self):
        """Afficher message si dossier Drivers n'existe pas"""
        card = ModernCard(self.scroll_frame)
        card.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            card,
            text="📁 Dossier Drivers introuvable",
            font=("Segoe UI", 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            card,
            text=f"Le dossier suivant n'existe pas:\n{self.drivers_folder}",
            font=("Segoe UI", 12),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(pady=10)

        ModernButton(
            card,
            text="📂 Créer Dossier",
            variant="filled",
            command=self._create_drivers_folder
        ).pack(pady=20)

    def _show_no_drivers_message(self):
        """Afficher message si aucun driver détecté"""
        card = ModernCard(self.scroll_frame)
        card.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            card,
            text="🔍 Aucun driver détecté",
            font=("Segoe UI", 20, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            card,
            text=f"Aucun fichier driver (.exe, .msi, .inf, .cab) trouvé dans:\n{self.drivers_folder}",
            font=("Segoe UI", 12),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(pady=10)

        ModernButton(
            card,
            text="📂 Ouvrir Dossier",
            variant="outlined",
            command=self._open_drivers_folder
        ).pack(pady=20)

    def _create_drivers_folder(self):
        """Créer le dossier Drivers s'il n'existe pas"""
        try:
            self.drivers_folder.mkdir(parents=True, exist_ok=True)
            messagebox.showinfo(
                "Dossier créé",
                f"Le dossier Drivers a été créé:\n{self.drivers_folder}\n\n"
                "Placez-y vos fichiers drivers (.exe, .msi, .inf, .cab)."
            )
            self._refresh_drivers_list()
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer le dossier:\n{str(e)}")

    def _install_vcredist(self):
        """Installer Visual C++ Redistributables"""
        result = messagebox.askyesno(
            "Visual C++ Redistributables",
            "Cette action va télécharger et installer:\n\n" +
            "• Visual C++ 2015-2022 Redistributable (x64)\n" +
            "• Visual C++ 2015-2022 Redistributable (x86)\n\n" +
            "Continuer?"
        )
        if result:
            import webbrowser
            webbrowser.open("https://aka.ms/vs/17/release/vc_redist.x64.exe")
            webbrowser.open("https://aka.ms/vs/17/release/vc_redist.x86.exe")
            messagebox.showinfo(
                "Téléchargement",
                "Les fichiers s'ouvrent dans votre navigateur.\n" +
                "Exécutez-les pour installer les redistributables."
            )

    def _install_directx(self):
        """Installer DirectX End-User Runtime"""
        result = messagebox.askyesno(
            "DirectX Runtime",
            "Cette action va ouvrir la page de téléchargement\n" +
            "du DirectX End-User Runtime de Microsoft.\n\n" +
            "Continuer?"
        )
        if result:
            import webbrowser
            webbrowser.open("https://www.microsoft.com/en-us/download/details.aspx?id=35")
            messagebox.showinfo(
                "Téléchargement",
                "Page Microsoft ouverte.\n" +
                "Téléchargez et exécutez l'installeur DirectX."
            )

    def _install_rst(self):
        """Installer Intel RST"""
        result = messagebox.askyesno(
            "Intel Rapid Storage Technology",
            "Cette action va ouvrir la page de téléchargement\n" +
            "du driver Intel RST.\n\n" +
            "Continuer?"
        )
        if result:
            import webbrowser
            webbrowser.open("https://www.intel.com/content/www/us/en/download/19512/intel-rapid-storage-technology-driver-installation-software-with-intel-optane-memory-10th-and-11th-gen-platforms.html")
            messagebox.showinfo(
                "Téléchargement",
                "Page Intel ouverte.\n" +
                "Téléchargez la version correspondant à votre système."
            )

    def _install_dotnet_sdk(self):
        """Installer .NET Framework SDK"""
        result = messagebox.askyesno(
            ".NET Framework SDK",
            "Cette action va ouvrir la page de téléchargement\n" +
            "du .NET Framework 4.8 Developer Pack.\n\n" +
            "Continuer?"
        )
        if result:
            import webbrowser
            webbrowser.open("https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48")
            messagebox.showinfo(
                "Téléchargement",
                "Page Microsoft .NET ouverte.\n" +
                "Téléchargez le Developer Pack pour le SDK complet."
            )

    def _install_chipset(self):
        """Installer drivers chipset"""
        # Détecter le fabricant
        try:
            import wmi
            c = wmi.WMI()
            for board in c.Win32_BaseBoard():
                manufacturer = board.Manufacturer.lower()
                if 'intel' in manufacturer:
                    self._install_intel_chipset()
                    return
                elif 'amd' in manufacturer or 'advanced micro' in manufacturer:
                    self._install_amd_chipset()
                    return
        except:
            pass

        # Choix manuel si détection échoue
        response = messagebox.askquestion(
            "Chipset Drivers",
            "Impossible de détecter automatiquement le fabricant.\n\n" +
            "Votre carte mère est-elle Intel?\n" +
            "(Cliquez 'Non' pour AMD)"
        )
        if response == 'yes':
            self._install_intel_chipset()
        else:
            self._install_amd_chipset()

    def _install_intel_chipset(self):
        """Installer chipset Intel"""
        import webbrowser
        webbrowser.open("https://www.intel.com/content/www/us/en/download/19347/chipset-inf-utility.html")
        messagebox.showinfo(
            "Intel Chipset",
            "Page Intel ouverte.\n" +
            "Téléchargez l'Intel Chipset Device Software."
        )

    def _install_amd_chipset(self):
        """Installer chipset AMD"""
        import webbrowser
        webbrowser.open("https://www.amd.com/en/support/chipsets")
        messagebox.showinfo(
            "AMD Chipset",
            "Page AMD ouverte.\n" +
            "Sélectionnez votre chipset et téléchargez le driver."
        )

    def _install_gpu_drivers(self):
        """Installer drivers GPU"""
        try:
            import wmi
            c = wmi.WMI()
            gpu_vendor = None

            for gpu in c.Win32_VideoController():
                name = gpu.Name.lower()
                if 'nvidia' in name or 'geforce' in name or 'rtx' in name or 'gtx' in name:
                    gpu_vendor = 'nvidia'
                    break
                elif 'amd' in name or 'radeon' in name:
                    gpu_vendor = 'amd'
                    break
                elif 'intel' in name and 'hd' in name or 'iris' in name or 'arc' in name:
                    gpu_vendor = 'intel'
                    break

            if gpu_vendor:
                self._install_specific_gpu(gpu_vendor)
            else:
                self._show_gpu_manual_choice()

        except:
            self._show_gpu_manual_choice()

    def _install_specific_gpu(self, vendor):
        """Installer drivers pour un GPU spécifique"""
        import webbrowser

        urls = {
            'nvidia': 'https://www.nvidia.com/Download/index.aspx',
            'amd': 'https://www.amd.com/en/support',
            'intel': 'https://www.intel.com/content/www/us/en/download/785597/intel-arc-iris-xe-graphics-windows.html'
        }

        names = {
            'nvidia': 'NVIDIA GeForce',
            'amd': 'AMD Radeon',
            'intel': 'Intel Graphics'
        }

        webbrowser.open(urls[vendor])
        messagebox.showinfo(
            f"{names[vendor]} Drivers",
            f"Page {names[vendor]} ouverte.\n" +
            f"Téléchargez le driver correspondant à votre GPU."
        )

    def _show_gpu_manual_choice(self):
        """Afficher choix manuel de GPU"""
        response = messagebox.askquestion(
            "GPU Drivers",
            "GPU non détecté automatiquement.\n\n" +
            "Sélectionnez votre fabricant:\n" +
            "• Oui = NVIDIA\n" +
            "• Non = AMD/Intel (autre fenêtre)"
        )

        if response == 'yes':
            self._install_specific_gpu('nvidia')
        else:
            response2 = messagebox.askquestion(
                "GPU Drivers",
                "• Oui = AMD Radeon\n" +
                "• Non = Intel Graphics"
            )
            if response2 == 'yes':
                self._install_specific_gpu('amd')
            else:
                self._install_specific_gpu('intel')

    def _install_java(self):
        """Installer Java Runtime Environment"""
        import webbrowser
        webbrowser.open('https://www.java.com/en/download/')
        messagebox.showinfo(
            "Java JRE",
            "Page de téléchargement Java ouverte.\n" +
            "Téléchargez et installez Java Runtime Environment.\n\n" +
            "Alternative: OpenJDK via winget:\n" +
            "winget install EclipseAdoptium.Temurin.21.JRE"
        )

    def _install_python(self):
        """Installer Python 3.12"""
        import webbrowser
        webbrowser.open('https://www.python.org/downloads/')
        messagebox.showinfo(
            "Python 3.12",
            "Page de téléchargement Python ouverte.\n" +
            "Téléchargez Python 3.12 ou version plus récente.\n\n" +
            "Alternative via winget:\n" +
            "winget install Python.Python.3.12"
        )

    def _install_realtek_audio(self):
        """Installer Realtek Audio Drivers"""
        import webbrowser
        webbrowser.open('https://www.realtek.com/en/component/zoo/category/pc-audio-codecs-high-definition-audio-codecs-software')
        messagebox.showinfo(
            "Realtek Audio Drivers",
            "Page de téléchargement Realtek Audio ouverte.\n\n" +
            "RECOMMANDÉ: Utilisez plutôt Windows Update ou le site\n" +
            "du fabricant de votre PC/carte mère pour obtenir la\n" +
            "version compatible avec votre système.\n\n" +
            "Alternative: Vérifiez sur le site du fabricant de votre\n" +
            "carte mère (ASUS, MSI, Gigabyte, etc.)"
        )

    def _install_bluetooth(self):
        """Installer Bluetooth Drivers"""
        import webbrowser

        response = messagebox.askquestion(
            "Bluetooth Drivers",
            "Fabricant de votre adaptateur Bluetooth:\n\n" +
            "• Oui = Intel Bluetooth\n" +
            "• Non = Realtek/Autre"
        )

        if response == 'yes':
            webbrowser.open('https://www.intel.com/content/www/us/en/download/18649/intel-wireless-bluetooth-for-windows-10-and-windows-11.html')
            messagebox.showinfo(
                "Intel Bluetooth",
                "Page Intel Bluetooth Drivers ouverte.\n" +
                "Téléchargez le driver compatible avec votre système."
            )
        else:
            messagebox.showinfo(
                "Bluetooth Drivers",
                "Pour les adaptateurs Realtek ou autres:\n\n" +
                "1. Vérifiez dans Gestionnaire de périphériques\n" +
                "   le modèle exact de votre adaptateur Bluetooth\n" +
                "2. Recherchez le driver sur le site du fabricant\n" +
                "   de votre PC/carte mère\n" +
                "3. Ou utilisez Windows Update\n\n" +
                "Realtek Bluetooth:\n" +
                "https://www.realtek.com/en/component/zoo/category/rtl8723be-software"
            )

    def _install_wifi(self):
        """Installer Wi-Fi Drivers"""
        import webbrowser

        response = messagebox.askquestion(
            "Wi-Fi Drivers",
            "Fabricant de votre carte Wi-Fi:\n\n" +
            "• Oui = Intel Wi-Fi\n" +
            "• Non = Realtek/Broadcom/Autre"
        )

        if response == 'yes':
            webbrowser.open('https://www.intel.com/content/www/us/en/support/articles/000005511/wireless.html')
            messagebox.showinfo(
                "Intel Wi-Fi",
                "Page Intel Wi-Fi Drivers ouverte.\n" +
                "Téléchargez le driver compatible avec votre carte Wi-Fi."
            )
        else:
            messagebox.showinfo(
                "Wi-Fi Drivers",
                "Pour les cartes Realtek, Broadcom ou autres:\n\n" +
                "1. Identifiez le modèle exact dans Gestionnaire de périphériques\n" +
                "2. Visitez le site du fabricant de votre PC/carte mère\n" +
                "3. Ou utilisez Windows Update\n\n" +
                "Liens utiles:\n" +
                "• Realtek: https://www.realtek.com/en/component/zoo/category/network-interface-controllers-10-100-1000m-gigabit-ethernet-pci-express-software\n" +
                "• Broadcom: Vérifiez sur le site du fabricant de votre PC"
            )

    def _install_webcam(self):
        """Installer Webcam Drivers"""
        import webbrowser

        messagebox.showinfo(
            "Webcam Drivers",
            "Drivers Webcam:\n\n" +
            "La plupart des webcams utilisent des drivers génériques Windows\n" +
            "et ne nécessitent pas d'installation manuelle.\n\n" +
            "Si votre webcam ne fonctionne pas:\n" +
            "1. Vérifiez Windows Update\n" +
            "2. Visitez le site du fabricant (Logitech, Microsoft, etc.)\n" +
            "3. Pour webcams intégrées: site du fabricant du PC\n\n" +
            "Je vais ouvrir la page de support Logitech (fabricant le plus courant)."
        )

        webbrowser.open('https://support.logi.com/hc/en-us/categories/360001433753-Webcams')
        messagebox.showinfo(
            "Logitech Support",
            "Page de support Logitech Webcams ouverte.\n\n" +
            "Si vous avez une autre marque:\n" +
            "• Microsoft: https://www.microsoft.com/accessories/en-us/downloads\n" +
            "• Razer: https://www.razer.com/downloads"
        )

    def _log_to_terminal(self, message):
        """Logger un message (simple print pour cette page)"""
        print(message)

    def _create_windows_generic_drivers_section(self):
        """Section pilotes génériques Windows (PREMIÈRE sous-catégorie)"""
        card = ModernCard(self.scroll_frame)
        card.pack(fill=tk.X, padx=20, pady=10)

        title = SectionHeader(card, text="🪟 Pilotes Génériques Windows")
        title.pack(fill=tk.X)

        # Description
        desc = ctk.CTkLabel(
            card,
            text="Installez les pilotes génériques Windows pour Internet, Audio, Vidéo, etc.\n"
                 "Ces pilotes de base permettent de faire fonctionner votre matériel en attendant les pilotes du constructeur.",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w",
            wraplength=800,
            justify="left"
        )
        desc.pack(fill=tk.X, padx=20, pady=(0, 10))

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Row 1: Réseau et Audio
        row1 = ctk.CTkFrame(content, fg_color="transparent")
        row1.pack(fill=tk.X, pady=5)

        ModernButton(
            row1,
            text="🌐 Installer Pilotes Réseau (Internet)",
            variant="outlined",
            command=self._install_network_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row1,
            text="🔊 Installer Pilotes Audio",
            variant="outlined",
            command=self._install_audio_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Row 2: Vidéo et Tous
        row2 = ctk.CTkFrame(content, fg_color="transparent")
        row2.pack(fill=tk.X, pady=5)

        ModernButton(
            row2,
            text="🎮 Installer Pilotes Vidéo/Graphiques",
            variant="outlined",
            command=self._install_video_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row2,
            text="🎯 Installer TOUS les Pilotes Génériques",
            variant="filled",
            command=self._install_all_generic_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Row 3: USB et Chipset
        row3 = ctk.CTkFrame(content, fg_color="transparent")
        row3.pack(fill=tk.X, pady=5)

        ModernButton(
            row3,
            text="🔌 Installer Pilotes USB",
            variant="outlined",
            command=self._install_usb_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row3,
            text="⚙️ Installer Pilotes Chipset",
            variant="outlined",
            command=self._install_chipset_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Row 4: Bluetooth et Imprimantes
        row4 = ctk.CTkFrame(content, fg_color="transparent")
        row4.pack(fill=tk.X, pady=5)

        ModernButton(
            row4,
            text="📡 Installer Pilotes Bluetooth",
            variant="outlined",
            command=self._install_bluetooth_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row4,
            text="🖨️ Installer Pilotes Imprimantes",
            variant="outlined",
            command=self._install_printer_drivers
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    def _install_network_drivers(self):
        """Installer pilotes réseau génériques (Ethernet/WiFi)"""
        self._log_to_terminal("🌐 Installation des pilotes réseau génériques...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Réseau",
            "Cette opération va installer les pilotes réseau génériques Windows.\n\n"
            "Idéal si vous n'avez pas de connexion Internet après une réinstallation.\n\n"
            "⚠️ Nécessite les droits administrateur.\n\n"
            "Continuer?"
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_network():
            try:
                import tempfile
                import os

                # Créer un script batch temporaire
                script_content = '''@echo off
color 0A
title Installation Pilotes Reseau Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES RESEAU GENERIQUES
echo ================================================
echo.
echo [*] Recherche des pilotes reseau disponibles...
echo     Cela peut prendre plusieurs minutes...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   INSTRUCTIONS IMPORTANTES
echo ================================================
echo.
echo 1. Dans Windows Update, cliquez sur:
echo    "Rechercher des mises a jour"
echo.
echo 2. Les pilotes reseau seront automatiquement
echo    detectes et affiches
echo.
echo 3. Cliquez sur "Installer" pour les installer
echo.
echo ================================================
echo.
pause
'''

                # Créer fichier temporaire portable
                temp_file_path = create_portable_temp_file('.bat', script_content)

                # Lancer le script en admin
                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file_path}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan des pilotes réseau lancé")
                self._log_to_terminal("█ Windows Update s'ouvrira automatiquement")
                self._log_to_terminal(f"█ Script portable: {temp_file_path}")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_network, daemon=True).start()

    def _install_audio_drivers(self):
        """Installer pilotes audio génériques"""
        self._log_to_terminal("🔊 Installation des pilotes audio génériques...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Audio",
            "Cette opération va installer les pilotes audio génériques Windows.\n\n"
            "Idéal si vous n'avez pas de son après une réinstallation.\n\n"
            "⚠️ Nécessite les droits administrateur.\n\n"
            "Continuer?"
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_audio():
            try:
                import tempfile

                script_content = '''@echo off
color 0A
title Installation Pilotes Audio Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES AUDIO GENERIQUES
echo ================================================
echo.
echo [*] Recherche des pilotes audio disponibles...
echo     Cela peut prendre plusieurs minutes...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   INSTRUCTIONS IMPORTANTES
echo ================================================
echo.
echo 1. Dans Windows Update, cliquez sur:
echo    "Rechercher des mises a jour"
echo.
echo 2. Les pilotes audio seront automatiquement
echo    detectes et affiches
echo.
echo 3. Cliquez sur "Installer" pour les installer
echo.
echo ================================================
echo.
pause
'''

                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.bat', delete=False, encoding='cp1252')
                temp_file.write(script_content)
                temp_file.close()

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file.name}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan des pilotes audio lancé")
                self._log_to_terminal("█ Windows Update s'ouvrira automatiquement")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_audio, daemon=True).start()

    def _install_video_drivers(self):
        """Installer pilotes vidéo/graphiques génériques"""
        self._log_to_terminal("🎮 Installation des pilotes vidéo génériques...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Vidéo",
            "Cette opération va installer les pilotes vidéo/graphiques génériques Windows.\n\n"
            "⚠️ Ces pilotes sont basiques. Pour les performances gaming,\n"
            "installez les pilotes NVIDIA/AMD officiels après.\n\n"
            "⚠️ Nécessite les droits administrateur.\n\n"
            "Continuer?"
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_video():
            try:
                import tempfile

                script_content = '''@echo off
color 0A
title Installation Pilotes Video Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES VIDEO GENERIQUES
echo ================================================
echo.
echo [*] Recherche des pilotes video disponibles...
echo     Cela peut prendre plusieurs minutes...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   INSTRUCTIONS IMPORTANTES
echo ================================================
echo.
echo 1. Dans Windows Update, cliquez sur:
echo    "Rechercher des mises a jour"
echo.
echo 2. Les pilotes video seront automatiquement
echo    detectes et affiches
echo.
echo 3. Cliquez sur "Installer" pour les installer
echo.
echo ================================================
echo   IMPORTANT - PERFORMANCES GAMING
echo ================================================
echo.
echo Pour de meilleures performances, installez
echo ensuite les pilotes constructeur:
echo.
echo - NVIDIA GeForce Experience (cartes NVIDIA)
echo - AMD Software Adrenalin (cartes AMD)
echo.
echo ================================================
echo.
pause
'''

                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.bat', delete=False, encoding='cp1252')
                temp_file.write(script_content)
                temp_file.close()

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file.name}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan des pilotes vidéo lancé")
                self._log_to_terminal("█ Windows Update s'ouvrira automatiquement")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_video, daemon=True).start()

    def _install_all_generic_drivers(self):
        """Installer TOUS les pilotes génériques Windows"""
        self._log_to_terminal("📦 Installation de TOUS les pilotes génériques...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer TOUS les Pilotes",
            "Cette opération va scanner et installer TOUS les pilotes génériques Windows:\n\n"
            "✓ Réseau (Ethernet/WiFi)\n"
            "✓ Audio\n"
            "✓ Vidéo/Graphiques\n"
            "✓ USB\n"
            "✓ Chipset\n"
            "✓ Bluetooth\n"
            "✓ Et tous les autres périphériques\n\n"
            "⚠️ Nécessite les droits administrateur.\n"
            "⏱️ Cela peut prendre 10-20 minutes.\n\n"
            "Continuer?"
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_all():
            try:
                import tempfile

                script_content = '''@echo off
color 0A
title Installation Complete - Tous les Pilotes Generiques
echo.
echo ========================================================
echo   INSTALLATION COMPLETE - TOUS LES PILOTES GENERIQUES
echo ========================================================
echo.
echo Cette operation va installer:
echo.
echo [+] Pilotes Reseau (Ethernet/WiFi)
echo [+] Pilotes Audio
echo [+] Pilotes Video/Graphiques
echo [+] Pilotes USB
echo [+] Pilotes Chipset
echo [+] Pilotes Bluetooth
echo [+] Tous les autres peripheriques
echo.
echo ========================================================
echo.
echo [*] Etape 1/2: Scan des peripheriques...
echo     Cela peut prendre plusieurs minutes...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Etape 2/2: Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ========================================================
echo   INSTRUCTIONS IMPORTANTES
echo ========================================================
echo.
echo 1. Dans Windows Update, cliquez sur:
echo    "Rechercher des mises a jour"
echo.
echo 2. Windows va detecter automatiquement:
echo    - Tous les pilotes manquants
echo    - Toutes les mises a jour de pilotes
echo.
echo 3. Cliquez sur "Installer tout" ou installez
echo    les pilotes un par un
echo.
echo 4. Attendez la fin de l'installation
echo    (peut prendre 10-20 minutes)
echo.
echo 5. Redemarrez votre PC apres l'installation
echo.
echo ========================================================
echo   CONSEIL
echo ========================================================
echo.
echo Apres cette installation de base,
echo installez les pilotes constructeurs
echo pour de meilleures performances!
echo.
echo ========================================================
echo.
pause
'''

                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.bat', delete=False, encoding='cp1252')
                temp_file.write(script_content)
                temp_file.close()

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file.name}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Installation complète lancée")
                self._log_to_terminal("█ Scan des périphériques en cours...")
                self._log_to_terminal("█ Windows Update s'ouvrira automatiquement")
                self._log_to_terminal("█ Durée estimée: 10-20 minutes")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_all, daemon=True).start()

    def _install_usb_drivers(self):
        """Installer les pilotes USB génériques"""
        self._log_to_terminal("🔌 Installation des pilotes USB...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes USB",
            "Cette action va:\n\n"
            "1. Scanner tous les contrôleurs USB\n"
            "2. Ouvrir Windows Update\n"
            "3. Vous devrez cliquer sur 'Installer'\n\n"
            "⚠ Droits administrateur requis\n\n"
            "Continuer?",
            icon='question'
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_usb():
            try:
                import tempfile
                import os

                script_content = '''@echo off
color 0A
title Installation Pilotes USB Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES USB GENERIQUES
echo ================================================
echo.
echo [*] Recherche des controleurs USB...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   INSTRUCTIONS
echo ================================================
echo.
echo 1. Cliquez sur "Rechercher des mises a jour"
echo 2. Les pilotes USB seront detectes
echo 3. Cliquez sur "Installer"
echo.
pause
'''

                temp_file_path = create_portable_temp_file('.bat', script_content)

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file_path}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan des pilotes USB lancé")
                self._log_to_terminal(f"█ Script: {temp_file_path}")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_usb, daemon=True).start()

    def _install_chipset_drivers(self):
        """Installer les pilotes Chipset génériques"""
        self._log_to_terminal("💿 Installation des pilotes Chipset...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Chipset",
            "Cette action va:\n\n"
            "1. Scanner le chipset de la carte mère\n"
            "2. Ouvrir Windows Update\n\n"
            "⚠ Pour de meilleures performances, installez les pilotes\n"
            "   du fabricant (Intel, AMD, etc.) après cette étape.\n\n"
            "⚠ Droits administrateur requis\n\n"
            "Continuer?",
            icon='question'
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_chipset():
            try:
                import tempfile
                import os

                script_content = '''@echo off
color 0A
title Installation Pilotes Chipset Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES CHIPSET GENERIQUES
echo ================================================
echo.
echo [*] Recherche du chipset...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   RECOMMANDATION
echo ================================================
echo.
echo Pour de meilleures performances, installez
echo les pilotes du fabricant de votre carte mere:
echo.
echo - Intel: downloadcenter.intel.com
echo - AMD: amd.com/fr/support
echo.
pause
'''

                temp_file_path = create_portable_temp_file('.bat', script_content)

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file_path}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan du chipset lancé")
                self._log_to_terminal(f"█ Script: {temp_file_path}")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_chipset, daemon=True).start()

    def _install_bluetooth_drivers(self):
        """Installer les pilotes Bluetooth génériques"""
        self._log_to_terminal("📡 Installation des pilotes Bluetooth...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Bluetooth",
            "Cette action va:\n\n"
            "1. Scanner les adaptateurs Bluetooth\n"
            "2. Ouvrir Windows Update\n"
            "3. Vous devrez cliquer sur 'Installer'\n\n"
            "⚠ Droits administrateur requis\n\n"
            "Continuer?",
            icon='question'
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_bluetooth():
            try:
                import tempfile
                import os

                script_content = '''@echo off
color 0A
title Installation Pilotes Bluetooth Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES BLUETOOTH GENERIQUES
echo ================================================
echo.
echo [*] Recherche des adaptateurs Bluetooth...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture de Windows Update...
start ms-settings:windowsupdate-action
echo.
echo ================================================
echo   INSTRUCTIONS
echo ================================================
echo.
echo 1. Cliquez sur "Rechercher des mises a jour"
echo 2. Les pilotes Bluetooth seront detectes
echo 3. Cliquez sur "Installer"
echo.
pause
'''

                temp_file_path = create_portable_temp_file('.bat', script_content)

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file_path}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan Bluetooth lancé")
                self._log_to_terminal(f"█ Script: {temp_file_path}")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_bluetooth, daemon=True).start()

    def _install_printer_drivers(self):
        """Installer les pilotes Imprimantes génériques"""
        self._log_to_terminal("🖨️ Installation des pilotes Imprimantes...")

        from tkinter import messagebox

        response = messagebox.askyesno(
            "Installer Pilotes Imprimantes",
            "Cette action va:\n\n"
            "1. Scanner les imprimantes connectées\n"
            "2. Ouvrir les paramètres d'imprimantes Windows\n"
            "3. Windows détectera automatiquement les imprimantes\n\n"
            "⚠ Droits administrateur requis\n\n"
            "Continuer?",
            icon='question'
        )

        if not response:
            self._log_to_terminal("❌ Installation annulée")
            return

        def install_printers():
            try:
                import tempfile
                import os

                script_content = '''@echo off
color 0A
title Installation Pilotes Imprimantes Generiques
echo.
echo ================================================
echo   INSTALLATION PILOTES IMPRIMANTES
echo ================================================
echo.
echo [*] Recherche des imprimantes...
echo.
pnputil /scan-devices
echo.
echo [*] Scan termine!
echo.
echo [*] Ouverture des parametres d'imprimantes...
start ms-settings:printers
echo.
echo ================================================
echo   INSTRUCTIONS
echo ================================================
echo.
echo 1. Cliquez sur "Ajouter une imprimante"
echo 2. Windows detectera automatiquement
echo    les imprimantes connectees
echo 3. Suivez l'assistant d'installation
echo.
echo Pour installer manuellement:
echo - Site du fabricant (HP, Canon, Epson, etc.)
echo.
pause
'''

                temp_file_path = create_portable_temp_file('.bat', script_content)

                subprocess.Popen(
                    f'powershell -Command "Start-Process \'{temp_file_path}\' -Verb RunAs"',
                    shell=True
                )

                self._log_to_terminal("█ Scan des imprimantes lancé")
                self._log_to_terminal(f"█ Script: {temp_file_path}")

            except Exception as e:
                self._log_to_terminal(f"█ ❌ Erreur: {str(e)}")

        threading.Thread(target=install_printers, daemon=True).start()

