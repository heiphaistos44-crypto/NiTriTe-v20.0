#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Boutons - NiTriTe V17
Boutons utilitaires système avancés
"""

import customtkinter as ctk
import tkinter as tk
import subprocess
import os
import threading
from tkinter import messagebox
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton


class MasterButtonsWidget(ctk.CTkFrame):
    """Widget contenant les Master Boutons"""

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        self._create_ui()

    def _create_ui(self):
        """Créer l'interface"""
        # Card principal
        card = ModernCard(self)
        card.pack(fill=tk.BOTH, expand=True)

        # Titre
        title = ctk.CTkLabel(
            card,
            text="🔧 Master Outils",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            card,
            text="Utilitaires système avancés",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(pady=(0, 20))

        # Grille de boutons (3x2)
        buttons_grid = ctk.CTkFrame(card, fg_color="transparent")
        buttons_grid.pack(padx=30, pady=(0, 20), fill=tk.BOTH, expand=True)

        # Configurer grille
        for i in range(3):  # 3 colonnes
            buttons_grid.columnconfigure(i, weight=1)

        # Ligne 1
        ModernButton(
            buttons_grid,
            text="🔑 Activation Windows/Office",
            variant="outlined",
            size="md",
            command=self.activate_windows_office
        ).grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        ModernButton(
            buttons_grid,
            text="⚙️ MSCONFIG",
            variant="outlined",
            size="md",
            command=self.open_msconfig
        ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ModernButton(
            buttons_grid,
            text="📊 Gestionnaire des Tâches",
            variant="outlined",
            size="md",
            command=self.open_task_manager
        ).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Ligne 2
        ModernButton(
            buttons_grid,
            text="ℹ️ MSINFO",
            variant="outlined",
            size="md",
            command=self.open_msinfo
        ).grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        ModernButton(
            buttons_grid,
            text="🗂️ Dossier Temp",
            variant="outlined",
            size="md",
            command=self.open_temp_folder
        ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ModernButton(
            buttons_grid,
            text="📁 AppData Local",
            variant="outlined",
            size="md",
            command=self.open_appdata_local
        ).grid(row=1, column=2, padx=5, pady=5, sticky="ew")

    def activate_windows_office(self):
        """Activer Windows et Office"""
        # Demander confirmation
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
            # Créer un script PowerShell temporaire pour éviter les problèmes d'échappement
            import tempfile
            script_content = "irm https://get.activated.win | iex"

            with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                f.write(script_content)
                script_path = f.name

            # Lancer PowerShell en tant qu'admin avec le script
            cmd = f'powershell -Command "Start-Process powershell -ArgumentList \'-ExecutionPolicy Bypass -File \"{script_path}\"\' -Verb RunAs"'

            subprocess.Popen(cmd, shell=True)

            messagebox.showinfo(
                "Activation lancée",
                "Le script MAS a été lancé en mode administrateur.\n\n"
                "Suivez les instructions dans la fenêtre PowerShell qui s'ouvre."
            )

            # Nettoyer le fichier temporaire après 60 secondes
            def cleanup():
                import time
                time.sleep(60)
                try:
                    os.remove(script_path)
                except:
                    pass

            threading.Thread(target=cleanup, daemon=True).start()

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lancer le script d'activation:\n\n{str(e)}"
            )

    def open_msconfig(self):
        """Ouvrir MSCONFIG"""
        try:
            subprocess.Popen("msconfig", shell=True)
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir MSCONFIG:\n\n{str(e)}"
            )

    def open_task_manager(self):
        """Ouvrir le Gestionnaire des tâches"""
        try:
            subprocess.Popen("taskmgr", shell=True)
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir le Gestionnaire des tâches:\n\n{str(e)}"
            )

    def open_msinfo(self):
        """Ouvrir MSINFO32"""
        try:
            subprocess.Popen("msinfo32", shell=True)
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir MSINFO:\n\n{str(e)}"
            )

    def open_temp_folder(self):
        """Ouvrir le dossier Temp"""
        try:
            temp_path = os.path.expandvars("%TEMP%")
            subprocess.Popen(f'explorer "{temp_path}"', shell=True)
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir le dossier Temp:\n\n{str(e)}"
            )

    def open_appdata_local(self):
        """Ouvrir le dossier LocalAppData"""
        try:
            appdata_path = os.path.expandvars("%LOCALAPPDATA%")
            subprocess.Popen(f'explorer "{appdata_path}"', shell=True)
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir AppData Local:\n\n{str(e)}"
            )
