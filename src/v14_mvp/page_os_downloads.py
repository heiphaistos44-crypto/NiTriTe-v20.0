#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Téléchargements OS - NiTriTe V18
Téléchargement d'OS et outils de création de clés USB bootables
"""

import customtkinter as ctk
import tkinter as tk
import webbrowser
import requests
import subprocess
from pathlib import Path
from typing import Dict, List
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, ModernStatsCard
from v14_mvp.logger_system import logger


class OSDownloadsPage(ctk.CTkFrame):
    """Page de téléchargement d'OS et outils bootables"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Dossier pour stocker les outils
        self.tools_dir = Path.home() / "Documents" / "NiTriTe_USB_Tools"
        self.tools_dir.mkdir(exist_ok=True)

        self._create_header()
        self._create_content()

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
            text=" Téléchargements OS & Outils Bootables",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            left_side,
            text="Systèmes d'exploitation et créateurs de clés USB",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)

        # Bouton ouvrir dossier outils
        ModernButton(
            container,
            text=" Ouvrir Dossier Outils",
            variant="outlined",
            command=self._open_tools_folder
        ).pack(side=tk.RIGHT)

    def _create_content(self):
        """Contenu principal"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # État d'expansion des sections
        self.expanded_sections = {
            "usb_tools": True,
            "windows": True,
            "linux": True,
            "macos": True,
            "other_os": True
        }

        # Section 1: Outils de création USB (avec téléchargement direct)
        self._create_usb_tools_section(scroll)

        # Section 2: Windows
        self._create_windows_section(scroll)

        # Section 3: Linux
        self._create_linux_section(scroll)

        # Section 4: macOS
        self._create_macos_section(scroll)

        # Section 5: Autres OS
        self._create_other_os_section(scroll)

    def _create_usb_tools_section(self, parent):
        """Section outils de création USB avec téléchargement direct"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header cliquable
        header = ctk.CTkFrame(
            card,
            fg_color="#4CAF50",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        header_content = ctk.CTkFrame(header, fg_color="transparent")
        header_content.pack(fill=tk.X, padx=15, pady=12)

        # Titre avec flèche
        title_frame = ctk.CTkFrame(header_content, fg_color="transparent")
        title_frame.pack(fill=tk.X)

        self.usb_tools_arrow = ctk.CTkLabel(
            title_frame,
            text="",
            font=(DesignTokens.FONT_FAMILY, 14),
            text_color="#FFFFFF"
        )
        self.usb_tools_arrow.pack(side=tk.LEFT, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text=" Outils de Création USB Bootable",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        desc = ctk.CTkLabel(
            header_content,
            text="Téléchargement direct des outils portables - Pas d'installation requise",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color="#FFFFFF"
        )
        desc.pack(anchor="w", pady=(5, 0))

        # Bind click pour toggle
        for widget in [header, header_content, title_frame, title, desc, self.usb_tools_arrow]:
            widget.bind("<Button-1>", lambda e: self._toggle_section("usb_tools", card))

        # Outils (URLs mises à jour pour éviter les 404)
        tools = [
            {
                "name": "Rufus",
                "description": "Outil le plus populaire pour créer des clés USB bootables",
                "url": "https://github.com/pbatard/rufus/releases/latest",
                "icon": "",
                "size": "~1.5 MB"
            },
            {
                "name": "Balena Etcher",
                "description": "Interface simple et moderne pour flasher des images",
                "url": "https://etcher.balena.io/#download-etcher",
                "icon": "",
                "size": "~140 MB"
            },
            {
                "name": "Ventoy",
                "description": "Multi-boot - Plusieurs ISO sur une seule clé USB",
                "url": "https://github.com/ventoy/Ventoy/releases/latest",
                "icon": "",
                "size": "~15 MB"
            },
            {
                "name": "Media Creation Tool",
                "description": "Outil officiel Microsoft pour créer une clé Windows 10/11",
                "url": "https://www.microsoft.com/fr-fr/software-download/windows11",
                "icon": "🪟",
                "size": "~19 MB"
            },
            {
                "name": "UNetbootin",
                "description": "Créateur de clés USB Linux multi-distributions",
                "url": "https://unetbootin.github.io/",
                "icon": "",
                "size": "~5 MB"
            },
            {
                "name": "YUMI",
                "description": "Multiboot USB Creator - Plusieurs OS sur une clé",
                "url": "https://www.pendrivelinux.com/yumi-multiboot-usb-creator/",
                "icon": "",
                "size": "~3 MB"
            },
            {
                "name": "WoeUSB",
                "description": "Créer des clés USB Windows depuis Linux",
                "url": "https://github.com/WoeUSB/WoeUSB-ng/releases/latest",
                "icon": "",
                "size": "Variable"
            },
            {
                "name": "PowerISO",
                "description": "Créer, éditer et graver des images ISO",
                "url": "https://www.poweriso.com/download.php",
                "icon": "",
                "size": "~7 MB"
            }
        ]

        # Grille d'outils (contenu rétractable)
        self.usb_tools_content = ctk.CTkFrame(card, fg_color="transparent")
        self.usb_tools_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        for tool in tools:
            self._create_tool_card(self.usb_tools_content, tool)

    def _create_tool_card(self, parent, tool):
        """Créer une carte d'outil avec bouton de téléchargement"""
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
            text=f"{tool['icon']} {tool['name']}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")

        desc_label = ctk.CTkLabel(
            left,
            text=tool['description'],
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc_label.pack(anchor="w", pady=(2, 0))

        size_label = ctk.CTkLabel(
            left,
            text=f" {tool['size']}",
            font=(DesignTokens.FONT_FAMILY, 10),
            text_color=DesignTokens.TEXT_TERTIARY,
            anchor="w"
        )
        size_label.pack(anchor="w", pady=(2, 0))

        # Bouton télécharger
        ModernButton(
            container,
            text=" Télécharger",
            variant="filled",
            size="sm",
            command=lambda: self._download_tool(tool)
        ).pack(side=tk.RIGHT, padx=5)

    def _download_tool(self, tool):
        """Ouvrir la page de téléchargement de l'outil dans le navigateur"""
        logger.info("OSDownloads", f"Ouverture page téléchargement: {tool['name']}", url=tool['url'])

        # Ouvrir la page de téléchargement dans le navigateur
        webbrowser.open(tool['url'])

        # Message d'information
        from tkinter import messagebox
        messagebox.showinfo(
            f"Téléchargement - {tool['name']}",
            f" Page de téléchargement ouverte dans votre navigateur.\n\n"
            f" Outil: {tool['name']}\n"
            f" Taille approximative: {tool['size']}\n\n"
            f" Après téléchargement, enregistrez le fichier dans:\n"
            f"{self.tools_dir}\n\n"
            f" Astuce: Téléchargez la version portable si disponible."
        )

    def _create_windows_section(self, parent):
        """Section Windows"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header cliquable
        header = ctk.CTkFrame(
            card,
            fg_color="#0078D4",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(fill=tk.X, padx=15, pady=12)

        self.windows_arrow = ctk.CTkLabel(
            title_frame,
            text="",
            font=(DesignTokens.FONT_FAMILY, 14),
            text_color="#FFFFFF"
        )
        self.windows_arrow.pack(side=tk.LEFT, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text="🪟 Windows",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        # Bind click
        for widget in [header, title_frame, title, self.windows_arrow]:
            widget.bind("<Button-1>", lambda e: self._toggle_section("windows", card))

        # OS Windows (liens corrigés, Windows 7 et 8.1 supprimés)
        windows_os = [
            ("Windows 11", "https://www.microsoft.com/fr-fr/software-download/windows11", "Version la plus récente"),
            ("Windows 10", "https://www.microsoft.com/fr-fr/software-download/windows10", "Version stable et populaire"),
            ("Windows Server 2022", "https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022", "Version serveur récente"),
            ("Windows Server 2019", "https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019", "Version serveur stable"),
        ]

        self.windows_content = ctk.CTkFrame(card, fg_color="transparent")
        self.windows_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        for os_name, url, description in windows_os:
            self._create_os_button(self.windows_content, os_name, url, description)

    def _create_linux_section(self, parent):
        """Section Linux"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header cliquable
        header = ctk.CTkFrame(
            card,
            fg_color="#FFA500",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(fill=tk.X, padx=15, pady=12)

        self.linux_arrow = ctk.CTkLabel(
            title_frame,
            text="",
            font=(DesignTokens.FONT_FAMILY, 14),
            text_color="#FFFFFF"
        )
        self.linux_arrow.pack(side=tk.LEFT, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text=" Linux",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        # Bind click
        for widget in [header, title_frame, title, self.linux_arrow]:
            widget.bind("<Button-1>", lambda e: self._toggle_section("linux", card))

        # Distributions Linux (TrueNAS supprimé)
        linux_distros = [
            ("Ubuntu 24.04 LTS", "https://ubuntu.com/download/desktop", "Distribution la plus populaire"),
            ("Ubuntu 22.04 LTS", "https://ubuntu.com/download/desktop", "Version LTS stable"),
            ("Linux Mint", "https://linuxmint.com/download.php", "Ubuntu simplifié pour débutants"),
            ("Debian", "https://www.debian.org/distrib/", "Distribution stable et fiable"),
            ("Fedora", "https://fedoraproject.org/workstation/download", "Technologies récentes et innovantes"),
            ("openSUSE", "https://get.opensuse.org/", "Distribution professionnelle"),
            ("Arch Linux", "https://archlinux.org/download/", "Pour utilisateurs avancés"),
            ("Manjaro", "https://manjaro.org/download/", "Arch Linux simplifié"),
            ("Pop!_OS", "https://pop.system76.com/", "Optimisé pour gaming et dev"),
            ("Elementary OS", "https://elementary.io/", "Interface élégante type macOS"),
            ("Zorin OS", "https://zorin.com/os/download/", "Similaire à Windows"),
            ("Kali Linux", "https://www.kali.org/get-kali/", "Distribution pour sécurité/pentest"),
            ("Proxmox VE", "https://www.proxmox.com/en/downloads", "Virtualisation et containers"),
        ]

        self.linux_content = ctk.CTkFrame(card, fg_color="transparent")
        self.linux_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        for os_name, url, description in linux_distros:
            self._create_os_button(self.linux_content, os_name, url, description)

    def _create_macos_section(self, parent):
        """Section macOS"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header cliquable
        header = ctk.CTkFrame(
            card,
            fg_color="#555555",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(fill=tk.X, padx=15, pady=12)

        self.macos_arrow = ctk.CTkLabel(
            title_frame,
            text="",
            font=(DesignTokens.FONT_FAMILY, 14),
            text_color="#FFFFFF"
        )
        self.macos_arrow.pack(side=tk.LEFT, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text=" macOS",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        # Bind click
        for widget in [header, title_frame, title, self.macos_arrow]:
            widget.bind("<Button-1>", lambda e: self._toggle_section("macos", card))

        self.macos_content = ctk.CTkFrame(card, fg_color="transparent")
        self.macos_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        # Note importante
        note = ctk.CTkLabel(
            self.macos_content,
            text="ℹ Note: Le téléchargement de macOS nécessite un Mac. Les liens redirigent vers l'App Store macOS.",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.WARNING,
            anchor="w"
        )
        note.pack(fill=tk.X, padx=10, pady=5)

        # Versions macOS (liens corrigés vers App Store)
        macos_versions = [
            ("macOS Sonoma", "https://apps.apple.com/us/app/macos-sonoma/id6450717509", "Version 14 (2023)"),
            ("macOS Ventura", "https://apps.apple.com/us/app/macos-ventura/id1638787999", "Version 13 (2022)"),
            ("macOS Monterey", "https://apps.apple.com/us/app/macos-monterey/id1576738294", "Version 12 (2021)"),
            ("macOS Big Sur", "https://apps.apple.com/us/app/macos-big-sur/id1526878132", "Version 11 (2020)"),
            ("macOS Catalina", "https://apps.apple.com/us/app/macos-catalina/id1466841314", "Version 10.15 (2019)"),
            ("macOS Mojave", "https://apps.apple.com/us/app/macos-mojave/id1398502828", "Version 10.14 (2018)"),
        ]

        for os_name, url, description in macos_versions:
            self._create_os_button(self.macos_content, os_name, url, description)

    def _create_other_os_section(self, parent):
        """Section Autres OS"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header cliquable
        header = ctk.CTkFrame(
            card,
            fg_color="#9C27B0",
            corner_radius=DesignTokens.RADIUS_MD,
            cursor="hand2"
        )
        header.pack(fill=tk.X, padx=15, pady=15)

        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(fill=tk.X, padx=15, pady=12)

        self.other_os_arrow = ctk.CTkLabel(
            title_frame,
            text="",
            font=(DesignTokens.FONT_FAMILY, 14),
            text_color="#FFFFFF"
        )
        self.other_os_arrow.pack(side=tk.LEFT, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text=" Autres Systèmes d'Exploitation",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color="#FFFFFF"
        )
        title.pack(side=tk.LEFT)

        # Bind click
        for widget in [header, title_frame, title, self.other_os_arrow]:
            widget.bind("<Button-1>", lambda e: self._toggle_section("other_os", card))

        # Autres OS
        other_os = [
            ("FreeBSD", "https://www.freebsd.org/where/", "Unix-like open source"),
            ("OpenBSD", "https://www.openbsd.org/", "Sécurité et code propre"),
            ("Haiku", "https://www.haiku-os.org/get-haiku", "Inspiré de BeOS"),
            ("ReactOS", "https://reactos.org/download/", "Clone open source de Windows"),
            ("ChromeOS Flex", "https://chromeenterprise.google/intl/fr_fr/os/chromeosflex/", "OS cloud de Google"),
            ("Android x86", "https://www.android-x86.org/download.html", "Android pour PC"),
        ]

        self.other_os_content = ctk.CTkFrame(card, fg_color="transparent")
        self.other_os_content.pack(fill=tk.X, padx=15, pady=(0, 15))

        for os_name, url, description in other_os:
            self._create_os_button(self.other_os_content, os_name, url, description)

    def _create_os_button(self, parent, name, url, description):
        """Créer un bouton pour télécharger un OS"""
        frame = ctk.CTkFrame(
            parent,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=DesignTokens.RADIUS_SM
        )
        frame.pack(fill=tk.X, pady=3)

        container = ctk.CTkFrame(frame, fg_color="transparent")
        container.pack(fill=tk.X, padx=10, pady=8)

        # Info
        left = ctk.CTkFrame(container, fg_color="transparent")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        name_label = ctk.CTkLabel(
            left,
            text=f" {name}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        name_label.pack(anchor="w")

        desc_label = ctk.CTkLabel(
            left,
            text=description,
            font=(DesignTokens.FONT_FAMILY, 10),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc_label.pack(anchor="w")

        # Bouton
        ModernButton(
            container,
            text=" Télécharger",
            variant="text",
            size="sm",
            command=lambda: self._open_download_page(name, url)
        ).pack(side=tk.RIGHT)

    def _open_download_page(self, name, url):
        """Ouvrir la page de téléchargement dans le navigateur"""
        logger.info("OSDownloads", f"Ouverture page téléchargement: {name}", url=url)
        webbrowser.open(url)

    def _toggle_section(self, section_id, card):
        """Basculer l'affichage d'une section"""
        # Toggle l'état
        self.expanded_sections[section_id] = not self.expanded_sections[section_id]
        is_expanded = self.expanded_sections[section_id]

        # Obtenir le contenu et la flèche selon la section
        content_map = {
            "usb_tools": (self.usb_tools_content, self.usb_tools_arrow),
            "windows": (self.windows_content, self.windows_arrow),
            "linux": (self.linux_content, self.linux_arrow),
            "macos": (self.macos_content, self.macos_arrow),
            "other_os": (self.other_os_content, self.other_os_arrow)
        }

        if section_id in content_map:
            content, arrow = content_map[section_id]

            if is_expanded:
                # Afficher le contenu
                content.pack(fill=tk.X, padx=15, pady=(0, 15))
                arrow.configure(text="")
            else:
                # Masquer le contenu
                content.pack_forget()
                arrow.configure(text="")

    def _open_tools_folder(self):
        """Ouvrir le dossier des outils"""
        try:
            subprocess.Popen(f'explorer "{self.tools_dir}"')
            logger.info("OSDownloads", f"Ouverture dossier outils: {self.tools_dir}")
        except Exception as e:
            logger.error("OSDownloads", f"Erreur ouverture dossier: {str(e)}")
