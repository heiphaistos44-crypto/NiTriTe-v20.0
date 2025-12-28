#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Activation Windows & Office - NiTriTe V20.0
Intégration MAS (Microsoft Activation Scripts) en mode terminal
"""

import customtkinter as ctk
import tkinter as tk
import subprocess
import threading
import tempfile
import os
from pathlib import Path
from v14_mvp.design_system import DesignTokens, ModernCard


class ActivationPage(ctk.CTkFrame):
    """Page d'activation Windows & Office avec MAS intégré"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Header
        header_container = ctk.CTkFrame(self, fg_color="transparent")
        header_container.pack(fill=tk.X, padx=20, pady=15)

        title_frame = ctk.CTkFrame(header_container, fg_color="transparent")
        title_frame.pack(side=tk.LEFT)

        ctk.CTkLabel(
            title_frame,
            text="🔑 Activation Windows & Office",
            font=("Segoe UI", 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_frame,
            text="Activation via MAS (Microsoft Activation Scripts)",
            font=("Segoe UI", 13),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(anchor="w", pady=(5, 0))

        # Scroll frame
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Statut activation
        self._create_status_section(scroll)

        # Terminal MAS intégré
        self._create_terminal_section(scroll)

        # Info MAS
        self._create_info_section(scroll)

    def _create_status_section(self, parent):
        """Section statut activation"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="📊 STATUT D'ACTIVATION",
            font=("Segoe UI", 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(padx=20, pady=(15, 10))

        # Détecter statut Windows
        windows_status = self._check_windows_activation()

        # Frame Windows
        windows_frame = ctk.CTkFrame(
            card,
            fg_color="#E3F2FD" if windows_status['activated'] else "#FFEBEE",
            corner_radius=10,
            border_width=2,
            border_color="#2196F3" if windows_status['activated'] else "#F44336"
        )
        windows_frame.pack(fill=tk.X, padx=20, pady=10)

        header = ctk.CTkFrame(windows_frame, fg_color="transparent")
        header.pack(fill=tk.X, padx=15, pady=12)

        ctk.CTkLabel(
            header,
            text="🪟 Windows",
            font=("Segoe UI", 16, "bold"),
            text_color="#1976D2" if windows_status['activated'] else "#C62828"
        ).pack(side=tk.LEFT)

        ctk.CTkLabel(
            header,
            text=windows_status['status_text'],
            font=("Segoe UI", 13),
            text_color="#1976D2" if windows_status['activated'] else "#C62828"
        ).pack(side=tk.RIGHT)

        # Frame Office
        office_frame = ctk.CTkFrame(
            card,
            fg_color="#FFF3E0",
            corner_radius=10,
            border_width=2,
            border_color="#FF9800"
        )
        office_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        header2 = ctk.CTkFrame(office_frame, fg_color="transparent")
        header2.pack(fill=tk.X, padx=15, pady=12)

        ctk.CTkLabel(
            header2,
            text="📊 Microsoft Office",
            font=("Segoe UI", 16, "bold"),
            text_color="#F57C00"
        ).pack(side=tk.LEFT)

        ctk.CTkLabel(
            header2,
            text="Vérifier via MAS",
            font=("Segoe UI", 13),
            text_color="#F57C00"
        ).pack(side=tk.RIGHT)

    def _check_windows_activation(self):
        """Vérifier statut activation Windows"""
        try:
            result = subprocess.run(
                'cscript //NoLogo %windir%\\System32\\slmgr.vbs /xpr',
                capture_output=True,
                text=True,
                timeout=10,
                shell=True
            )
            status = result.stdout.strip().lower()

            if 'permanently activated' in status or 'activé de manière permanente' in status:
                return {
                    'activated': True,
                    'status_text': "✅ Activé de manière permanente"
                }
            elif 'will expire' in status or 'expirera' in status:
                return {
                    'activated': False,
                    'status_text': "⚠️ Activation temporaire"
                }
            else:
                return {
                    'activated': False,
                    'status_text': "❌ Non activé"
                }
        except:
            return {
                'activated': False,
                'status_text': "❓ Impossible de vérifier"
            }

    def _create_terminal_section(self, parent):
        """Section terminal MAS intégré"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        # Header
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill=tk.X, padx=20, pady=(15, 10))

        ctk.CTkLabel(
            header,
            text="⚡ TERMINAL MAS",
            font=("Segoe UI", 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT)

        # Boutons d'action
        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ctk.CTkButton(
            btn_frame,
            text="🪟 Activer Windows",
            command=lambda: self._run_mas_command("1"),
            width=150,
            height=32,
            font=("Segoe UI", 12, "bold"),
            fg_color="#2196F3",
            hover_color="#1976D2"
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            btn_frame,
            text="📊 Activer Office",
            command=lambda: self._run_mas_command("2"),
            width=150,
            height=32,
            font=("Segoe UI", 12, "bold"),
            fg_color="#FF9800",
            hover_color="#F57C00"
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(
            btn_frame,
            text="🔄 Lancer MAS",
            command=self._launch_mas_interactive,
            width=150,
            height=32,
            font=("Segoe UI", 12, "bold"),
            fg_color="#4CAF50",
            hover_color="#45A049"
        ).pack(side=tk.LEFT, padx=5)

        # Terminal intégré
        terminal_container = ctk.CTkFrame(card, fg_color="transparent")
        terminal_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 20))

        # Zone de texte pour output du terminal
        self.terminal_text = tk.Text(
            terminal_container,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#1E1E1E",
            fg="#00FF00",
            insertbackground="#00FF00",
            selectbackground="#333333",
            height=25,
            relief=tk.FLAT,
            borderwidth=0
        )
        self.terminal_text.pack(fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(terminal_container, command=self.terminal_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.terminal_text.config(yscrollcommand=scrollbar.set)

        # Message initial
        self.terminal_text.insert(tk.END, "🔑 Terminal MAS - Microsoft Activation Scripts\n")
        self.terminal_text.insert(tk.END, "=" * 80 + "\n\n")
        self.terminal_text.insert(tk.END, "Cliquez sur un bouton pour activer Windows ou Office.\n")
        self.terminal_text.insert(tk.END, "Ou cliquez sur 'Lancer MAS' pour le menu interactif complet.\n\n")
        self.terminal_text.config(state=tk.DISABLED)

    def _clear_terminal(self):
        """Effacer le terminal"""
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.delete("1.0", tk.END)

    def _append_to_terminal(self, text):
        """Ajouter texte au terminal"""
        self.terminal_text.config(state=tk.NORMAL)
        self.terminal_text.insert(tk.END, text)
        self.terminal_text.see(tk.END)
        self.terminal_text.config(state=tk.DISABLED)
        self.terminal_text.update()

    def _run_mas_command(self, option):
        """Exécuter commande MAS automatique"""
        self._clear_terminal()
        self._append_to_terminal(f"🔄 Lancement de l'activation automatique...\n\n")

        def run():
            try:
                self._append_to_terminal("📥 Téléchargement du script MAS...\n")

                # Script PowerShell pour activation automatique
                ps_script = f"""
$ErrorActionPreference = 'Stop'
Write-Host "🔄 Téléchargement de MAS..." -ForegroundColor Green
irm https://get.activated.win | iex
Write-Host "⚡ Lancement de l'activation..." -ForegroundColor Green
"""

                with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                    f.write(ps_script)
                    script_path = f.name

                self._append_to_terminal("✅ Script téléchargé\n")
                self._append_to_terminal("⚡ Exécution en cours...\n\n")

                # Exécuter PowerShell
                process = subprocess.Popen(
                    ['powershell', '-ExecutionPolicy', 'Bypass', '-NoProfile', '-File', script_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )

                # Lire output en temps réel
                for line in process.stdout:
                    self._append_to_terminal(line)

                process.wait()

                self._append_to_terminal("\n\n✅ Exécution terminée !\n")
                self._append_to_terminal("Vérifiez le statut ci-dessus.\n")

                # Cleanup
                try:
                    os.remove(script_path)
                except:
                    pass

            except Exception as e:
                self._append_to_terminal(f"\n\n❌ Erreur: {str(e)}\n")

        threading.Thread(target=run, daemon=True).start()

    def _launch_mas_interactive(self):
        """Lancer MAS en mode interactif complet"""
        self._clear_terminal()
        self._append_to_terminal("🔄 Lancement du menu interactif MAS...\n\n")

        def run():
            try:
                self._append_to_terminal("📥 Téléchargement de MAS...\n")

                # Script pour menu interactif
                ps_script = """
irm https://get.activated.win | iex
"""

                with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                    f.write(ps_script)
                    script_path = f.name

                self._append_to_terminal("⚡ Ouverture de la fenêtre PowerShell...\n")
                self._append_to_terminal("ℹ️ Une fenêtre PowerShell va s'ouvrir avec le menu MAS.\n")
                self._append_to_terminal("   Suivez les instructions dans cette fenêtre.\n\n")

                # Lancer dans une nouvelle fenêtre PowerShell
                subprocess.Popen(
                    f'powershell -ExecutionPolicy Bypass -NoExit -File "{script_path}"',
                    shell=True
                )

                self._append_to_terminal("✅ Fenêtre PowerShell lancée !\n")
                self._append_to_terminal("Continuez l'activation dans la fenêtre qui vient de s'ouvrir.\n")

            except Exception as e:
                self._append_to_terminal(f"\n\n❌ Erreur: {str(e)}\n")

        threading.Thread(target=run, daemon=True).start()

    def _create_info_section(self, parent):
        """Section informations MAS"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="ℹ️ À PROPOS DE MAS",
            font=("Segoe UI", 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(padx=20, pady=(15, 10))

        info_text = """MAS (Microsoft Activation Scripts) est une collection de scripts open-source pour activer Windows et Office.

🔹 Sûr et fiable : Code source public sur GitHub
🔹 Méthodes légales : Utilise les clés de licence volume Microsoft officielles (GVLK)
🔹 Sans malware : Aucun fichier suspect, 100% PowerShell
🔹 Gratuit : Complètement gratuit et sans publicité

OPTIONS D'ACTIVATION :

1️⃣ HWID (Windows 10/11) : Activation permanente liée au matériel
2️⃣ Ohook (Office) : Activation Office permanente
3️⃣ KMS38 (Windows) : Activation jusqu'en 2038
4️⃣ Online KMS : Activation 180 jours renouvelable

COMMANDES RAPIDES :

🪟 Activer Windows : Cliquez sur "Activer Windows"
📊 Activer Office : Cliquez sur "Activer Office"
🔄 Menu complet : Cliquez sur "Lancer MAS"

IMPORTANT : Désactivez temporairement votre antivirus si besoin."""

        ctk.CTkLabel(
            card,
            text=info_text,
            font=("Segoe UI", 11),
            text_color=DesignTokens.TEXT_SECONDARY,
            wraplength=800,
            justify="left",
            anchor="w"
        ).pack(padx=20, pady=(0, 15))

        # Lien GitHub
        link_frame = ctk.CTkFrame(card, fg_color="#E3F2FD", corner_radius=8)
        link_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        ctk.CTkLabel(
            link_frame,
            text="🔗 Source : https://github.com/massgravel/Microsoft-Activation-Scripts",
            font=("Segoe UI", 11, "bold"),
            text_color="#1976D2",
            cursor="hand2"
        ).pack(padx=15, pady=10)
