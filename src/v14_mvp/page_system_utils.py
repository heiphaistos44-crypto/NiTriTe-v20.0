#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Utilitaires Système Avancés - NiTriTe V20
Gestionnaire de partitions, ISO, VirtualBox, Dual-boot
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import webbrowser
from pathlib import Path
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader


class SystemUtilitiesPage(ctk.CTkFrame):
    """Page Utilitaires Système Avancés"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self._create_header()
        self._create_content()

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        title_frame = SectionHeader(container, text="💿 Utilitaires Système Avancés")
        title_frame.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            container,
            text="Partitions • ISO • Virtualisation • Dual-Boot",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.RIGHT)

    def _create_content(self):
        """Contenu scrollable"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Section Gestion des Partitions
        self._create_partition_section(scroll)

        # Section Montage ISO
        self._create_iso_section(scroll)

        # Section Machines Virtuelles
        self._create_vm_section(scroll)

        # Section Dual-Boot
        self._create_dualboot_section(scroll)

    def _create_partition_section(self, parent):
        """Section gestion des partitions"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="💾 Gestion des Partitions")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Créer, redimensionner, formater et gérer vos partitions de disque",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Boutons d'outils
        tools_frame = ctk.CTkFrame(content, fg_color="transparent")
        tools_frame.pack(fill=tk.X)

        ModernButton(
            tools_frame,
            text="🪟 Gestion des disques Windows",
            variant="filled",
            command=self._open_disk_management
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="💿 MiniTool Partition Wizard",
            variant="outlined",
            command=lambda: self._download_tool("MiniTool")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="🔧 EaseUS Partition Master",
            variant="outlined",
            command=lambda: self._download_tool("EaseUS")
        ).pack(side=tk.LEFT, padx=5, pady=5)

    def _create_iso_section(self, parent):
        """Section montage ISO"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="💿 Montage & Gravure ISO")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Monter, graver et créer des images ISO",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Boutons
        tools_frame = ctk.CTkFrame(content, fg_color="transparent")
        tools_frame.pack(fill=tk.X)

        ModernButton(
            tools_frame,
            text="📁 Monter ISO (Windows)",
            variant="filled",
            command=self._mount_iso
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="💿 Rufus (Créer USB Bootable)",
            variant="outlined",
            command=lambda: self._download_tool("Rufus")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="🔥 ImgBurn (Gravure)",
            variant="outlined",
            command=lambda: self._download_tool("ImgBurn")
        ).pack(side=tk.LEFT, padx=5, pady=5)

    def _create_vm_section(self, parent):
        """Section machines virtuelles"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="🖥️ Machines Virtuelles")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Installer et gérer des machines virtuelles (VM)",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Boutons
        tools_frame = ctk.CTkFrame(content, fg_color="transparent")
        tools_frame.pack(fill=tk.X)

        ModernButton(
            tools_frame,
            text="📦 VirtualBox (Gratuit)",
            variant="filled",
            command=lambda: self._download_tool("VirtualBox")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="💼 VMware Workstation",
            variant="outlined",
            command=lambda: self._download_tool("VMware")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="🪟 Hyper-V (Windows)",
            variant="outlined",
            command=self._enable_hyperv
        ).pack(side=tk.LEFT, padx=5, pady=5)

    def _create_dualboot_section(self, parent):
        """Section dual-boot"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="⚡ Dual-Boot & Bootloaders")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Gérer plusieurs systèmes d'exploitation sur un même PC",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Boutons
        tools_frame = ctk.CTkFrame(content, fg_color="transparent")
        tools_frame.pack(fill=tk.X)

        ModernButton(
            tools_frame,
            text="🪟 Configuration Boot Windows",
            variant="filled",
            command=self._open_msconfig
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="🐧 EasyBCD (Dual-Boot Manager)",
            variant="outlined",
            command=lambda: self._download_tool("EasyBCD")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tools_frame,
            text="📚 Guide Dual-Boot",
            variant="outlined",
            command=self._open_dualboot_guide
        ).pack(side=tk.LEFT, padx=5, pady=5)

    # === MÉTHODES D'ACTION ===

    def _open_disk_management(self):
        """Ouvrir Gestion des disques Windows"""
        try:
            subprocess.Popen(["diskmgmt.msc"])
            print("✅ Gestion des disques ouverte")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir la gestion des disques:\n\n{str(e)}")

    def _mount_iso(self):
        """Monter un fichier ISO"""
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier ISO",
            filetypes=[("Fichiers ISO", "*.iso"), ("Tous les fichiers", "*.*")]
        )

        if not file_path:
            return

        try:
            # Monter l'ISO avec PowerShell
            subprocess.run(
                ['powershell', '-Command', f'Mount-DiskImage -ImagePath "{file_path}"'],
                check=True
            )
            messagebox.showinfo("Succès", f"ISO monté avec succès:\n\n{Path(file_path).name}")
            print(f"✅ ISO monté: {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de monter l'ISO:\n\n{str(e)}")

    def _open_msconfig(self):
        """Ouvrir MSCONFIG pour gérer le boot"""
        try:
            subprocess.Popen(["msconfig"])
            print("✅ MSCONFIG ouvert")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir MSCONFIG:\n\n{str(e)}")

    def _enable_hyperv(self):
        """Guide pour activer Hyper-V"""
        messagebox.showinfo(
            "Activer Hyper-V",
            "Pour activer Hyper-V sur Windows:\n\n"
            "1. Ouvrir 'Activer ou désactiver des fonctionnalités Windows'\n"
            "2. Cocher 'Hyper-V'\n"
            "3. Redémarrer le PC\n\n"
            "Note: Nécessite Windows 10/11 Pro ou Enterprise"
        )

    def _open_dualboot_guide(self):
        """Ouvrir un guide sur le dual-boot"""
        webbrowser.open("https://www.howtogeek.com/214571/how-to-dual-boot-linux-on-your-pc/")
        print("📚 Guide dual-boot ouvert dans le navigateur")

    def _download_tool(self, tool_name):
        """Télécharger/ouvrir un outil"""
        urls = {
            "MiniTool": "https://www.minitool.com/partition-manager/",
            "EaseUS": "https://www.easeus.com/partition-manager/",
            "Rufus": "https://rufus.ie/",
            "ImgBurn": "https://www.imgburn.com/",
            "VirtualBox": "https://www.virtualbox.org/wiki/Downloads",
            "VMware": "https://www.vmware.com/products/workstation-player.html",
            "EasyBCD": "https://neosmart.net/EasyBCD/"
        }

        if tool_name in urls:
            webbrowser.open(urls[tool_name])
            print(f"🌐 Ouverture de {tool_name}")
        else:
            messagebox.showwarning("Non disponible", f"{tool_name} n'est pas encore configuré.")
