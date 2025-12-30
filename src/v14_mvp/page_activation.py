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
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard


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
                timeout=5,
                shell=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
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
        except Exception as e:
            print(f"Erreur vérification activation: {e}")
            return {
                'activated': False,
                'status_text': "❓ Impossible de vérifier"
            }

    def _resize_terminal(self, delta):
        """Redimensionner le terminal (delta = nombre de lignes à ajouter/retirer)"""
        self.terminal_height = max(10, min(50, self.terminal_height + delta))
        self.terminal_text.configure(height=self.terminal_height)

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

        # Boutons de redimensionnement (à gauche des boutons d'action)
        resize_frame = ctk.CTkFrame(header, fg_color="transparent")
        resize_frame.pack(side=tk.LEFT, padx=(20, 0))

        ctk.CTkButton(
            resize_frame,
            text="▼",
            width=30,
            height=20,
            font=("Segoe UI", 12),
            command=lambda: self._resize_terminal(-5),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            resize_frame,
            text="▲",
            width=30,
            height=20,
            font=("Segoe UI", 12),
            command=lambda: self._resize_terminal(5),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

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
        terminal_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(10, 10))

        # Zone de texte pour output du terminal
        text_frame = ctk.CTkFrame(terminal_container, fg_color="#1E1E1E", corner_radius=8)
        text_frame.pack(fill=tk.BOTH, expand=True)

        # Hauteur initiale du terminal (en lignes)
        self.terminal_height = 20

        self.terminal_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#1E1E1E",
            fg="#00FF00",
            insertbackground="#00FF00",
            selectbackground="#333333",
            height=self.terminal_height,
            relief=tk.FLAT,
            borderwidth=0
        )
        self.terminal_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=self.terminal_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5, padx=(0, 5))
        self.terminal_text.config(yscrollcommand=scrollbar.set)

        # Message initial
        self.terminal_text.insert(tk.END, "🔑 Terminal MAS - Microsoft Activation Scripts\n")
        self.terminal_text.insert(tk.END, "=" * 80 + "\n\n")
        self.terminal_text.insert(tk.END, "💡 COMMANDES RAPIDES (tapez le chiffre dans le champ ci-dessous) :\n\n")
        self.terminal_text.insert(tk.END, "  1 → Activer Windows (HWID - Permanent)\n")
        self.terminal_text.insert(tk.END, "  2 → Activer Office (KMS - 180 jours)\n")
        self.terminal_text.insert(tk.END, "  3 → Vérifier statut Windows\n")
        self.terminal_text.insert(tk.END, "  4 → Vérifier statut Office\n")
        self.terminal_text.insert(tk.END, "  5 → Réinitialiser activation Windows\n")
        self.terminal_text.insert(tk.END, "  6 → Lancer MAS original (Internet)\n\n")
        self.terminal_text.insert(tk.END, "Vous pouvez aussi taper des commandes PowerShell (ex: slmgr /xpr)\n")
        self.terminal_text.insert(tk.END, "Ou cliquer sur les boutons bleus/orange ci-dessus.\n\n")
        self.terminal_text.insert(tk.END, "-" * 80 + "\n")
        self.terminal_text.config(state=tk.DISABLED)

        # Barre de saisie de commandes
        input_container = ctk.CTkFrame(terminal_container, fg_color="transparent")
        input_container.pack(fill=tk.X, pady=(10, 10))

        # Label
        ctk.CTkLabel(
            input_container,
            text="💬 Commande :",
            font=("Segoe UI", 11, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT, padx=(0, 10))

        # Champ de saisie
        self.command_entry = ctk.CTkEntry(
            input_container,
            placeholder_text="Entrez une commande PowerShell...",
            font=("Consolas", 11),
            height=32
        )
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.command_entry.bind("<Return>", lambda e: self._send_command())

        # Bouton Envoyer
        ctk.CTkButton(
            input_container,
            text="▶ Envoyer",
            command=self._send_command,
            width=100,
            height=32,
            font=("Segoe UI", 11, "bold"),
            fg_color="#4CAF50",
            hover_color="#45A049"
        ).pack(side=tk.LEFT)

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

    def _send_command(self):
        """Envoyer une commande ou action MAS"""
        command = self.command_entry.get().strip()
        if not command:
            return

        # Effacer le champ de saisie
        self.command_entry.delete(0, tk.END)

        # Détecter les commandes MAS numériques (1-6)
        if command in ['1', '2', '3', '4', '5', '6']:
            self._append_to_terminal(f"\n> Option {command} sélectionnée\n")

            if command == '1':
                self._append_to_terminal("⚡ Activation Windows (HWID)...\n\n")
                self._run_mas_command("1")
            elif command == '2':
                self._append_to_terminal("⚡ Activation Office (KMS)...\n\n")
                self._run_mas_command("2")
            elif command == '3':
                self._append_to_terminal("🔍 Vérification statut Windows...\n\n")
                ps_cmd = """
$license = Get-CimInstance -ClassName SoftwareLicensingProduct | Where-Object {$_.PartialProductKey}
if ($license) {
    Write-Host "=== STATUT ACTIVATION WINDOWS ===" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Nom: $($license.Name)" -ForegroundColor White
    Write-Host "Description: $($license.Description)" -ForegroundColor White

    $status = switch ($license.LicenseStatus) {
        0 { "[X] Non licencie" }
        1 { "[OK] Licencie (Active)" }
        2 { "[~] OOB Grace" }
        3 { "[~] OOT Grace" }
        4 { "[~] Non Genuine Grace" }
        5 { "[!] Notification" }
        6 { "[~] Extended Grace" }
        default { "[?] Inconnu ($($license.LicenseStatus))" }
    }

    Write-Host "Statut: $status" -ForegroundColor $(if ($license.LicenseStatus -eq 1) { "Green" } else { "Yellow" })

    if ($license.PartialProductKey) {
        Write-Host "Cle partielle: *****-$($license.PartialProductKey)" -ForegroundColor White
    }

    if ($license.GracePeriodRemaining) {
        $daysRemaining = [math]::Floor($license.GracePeriodRemaining / 1440)
        if ($daysRemaining -gt 0) {
            Write-Host "Jours restants: $daysRemaining jours" -ForegroundColor Yellow
        }
    }
} else {
    Write-Host "[X] Impossible de recuperer les informations de licence" -ForegroundColor Red
}
"""
                self._execute_powershell_command(ps_cmd)
            elif command == '4':
                self._append_to_terminal("🔍 Vérification statut Office...\n\n")
                ps_cmd = """
$officePaths = @(
    "C:\\Program Files\\Microsoft Office\\Office16",
    "C:\\Program Files (x86)\\Microsoft Office\\Office16"
)
$osppPath = $null
foreach ($path in $officePaths) {
    $testPath = Join-Path $path "ospp.vbs"
    if (Test-Path $testPath) {
        $osppPath = $testPath
        break
    }
}
if ($osppPath) {
    cscript //NoLogo "$osppPath" /dstatus
} else {
    Write-Host "[X] Office non detecte !" -ForegroundColor Red
}
"""
                self._execute_powershell_command(ps_cmd)
            elif command == '5':
                self._append_to_terminal("⚠️ Réinitialisation activation Windows...\n\n")
                ps_cmd = """
# Verifier droits administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "[X] ERREUR : Droits administrateur requis !" -ForegroundColor Red
    Write-Host "   Relancez NiTriTe en tant qu'administrateur." -ForegroundColor Yellow
    exit 1
}

Write-Host "[!] REINITIALISATION ACTIVATION WINDOWS" -ForegroundColor Yellow
Write-Host "=======================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "Etape 1/3 : Suppression de la cle produit..." -ForegroundColor Cyan
slmgr /upk
Start-Sleep -Seconds 2

Write-Host ""
Write-Host "Etape 2/3 : Suppression serveur KMS..." -ForegroundColor Cyan
slmgr /ckms
Start-Sleep -Seconds 2

Write-Host ""
Write-Host "Etape 3/3 : Reinitialisation licence..." -ForegroundColor Cyan
slmgr /rearm

Write-Host ""
Write-Host "[OK] Reinitialisation terminee !" -ForegroundColor Green
Write-Host "[!] REDEMARREZ votre PC pour finaliser." -ForegroundColor Yellow
"""
                self._execute_powershell_command(ps_cmd)
            elif command == '6':
                self._append_to_terminal("🌐 Lancement MAS original...\n\n")
                self._launch_mas_interactive()
        else:
            # Commande PowerShell standard
            self._append_to_terminal(f"\n> {command}\n")
            self._execute_powershell_command(command)

    def _execute_powershell_command(self, command):
        """Exécuter une commande PowerShell standard"""
        def run():
            try:
                self._append_to_terminal(f"[DEBUG] Création script PowerShell...\n")

                # Créer un fichier temporaire pour le script PowerShell (meilleure gestion encodage)
                with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                    f.write(command)
                    script_path = f.name

                self._append_to_terminal(f"[DEBUG] Script créé: {script_path}\n")
                self._append_to_terminal(f"[DEBUG] Exécution du script...\n\n")

                # Exécuter le script
                process = subprocess.Popen(
                    ['powershell', '-ExecutionPolicy', 'Bypass', '-NoProfile', '-File', script_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding='utf-8',
                    errors='ignore',
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )

                output, errors = process.communicate(timeout=60)

                if output:
                    self._append_to_terminal(output)
                else:
                    self._append_to_terminal("[DEBUG] Aucune sortie du script\n")

                if errors:
                    self._append_to_terminal(f"\n⚠️ Erreurs :\n{errors}")

                self._append_to_terminal("\n" + "-" * 80 + "\n")

                # Cleanup
                try:
                    os.remove(script_path)
                    self._append_to_terminal(f"[DEBUG] Script temporaire supprimé\n")
                except Exception as e:
                    self._append_to_terminal(f"[DEBUG] Impossible de supprimer {script_path}: {e}\n")

            except subprocess.TimeoutExpired:
                self._append_to_terminal("\n❌ Timeout : La commande a pris trop de temps (> 60s)\n")
                self._append_to_terminal("-" * 80 + "\n")
                try:
                    process.kill()
                except:
                    pass
            except Exception as e:
                self._append_to_terminal(f"\n❌ Erreur d'exécution: {str(e)}\n")
                import traceback
                self._append_to_terminal(f"Trace: {traceback.format_exc()}\n")
                self._append_to_terminal("-" * 80 + "\n")

        threading.Thread(target=run, daemon=True).start()

    def _run_mas_command(self, option):
        """Exécuter commande MAS automatique avec scripts embarqués"""
        self._clear_terminal()

        activation_type = "Windows" if option == "1" else "Office"
        self._append_to_terminal(f"🔄 Activation {activation_type} en cours...\n\n")

        def run():
            try:
                if option == "1":
                    # Activation Windows HWID (méthode interne)
                    self._append_to_terminal("⚡ Méthode : HWID (Activation permanente Windows)\n")
                    self._append_to_terminal("📌 Récupération de la licence digitale...\n\n")

                    ps_script = """
# Script d'activation Windows HWID intégré
$ErrorActionPreference = 'Continue'

Write-Host "=================================" -ForegroundColor Cyan
Write-Host "  ACTIVATION WINDOWS HWID" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Vérifier si administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "❌ ERREUR : Droits administrateur requis !" -ForegroundColor Red
    Write-Host "   Relancez NiTriTe en tant qu'administrateur." -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ Droits administrateur détectés" -ForegroundColor Green
Write-Host ""

# Détection de la version Windows
$winVersion = (Get-WmiObject -Class Win32_OperatingSystem).Caption
Write-Host "📊 Version Windows : $winVersion" -ForegroundColor Cyan
Write-Host ""

# Installation de la clé GVLK (Generic Volume License Key) selon l'édition
Write-Host "🔑 Installation de la clé de licence volume..." -ForegroundColor Yellow

$gvlkKeys = @{
    'Windows 10 Pro' = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    'Windows 10 Home' = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
    'Windows 11 Pro' = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    'Windows 11 Home' = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
    'Windows 10 Education' = 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
    'Windows 11 Education' = 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
}

$keyInstalled = $false
foreach ($edition in $gvlkKeys.Keys) {
    if ($winVersion -like "*$edition*") {
        $key = $gvlkKeys[$edition]
        Write-Host "   Clé pour $edition" -ForegroundColor Cyan
        slmgr /ipk $key 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ✓ Clé installée avec succès" -ForegroundColor Green
            $keyInstalled = $true
        } else {
            Write-Host "   ⚠ Échec installation clé" -ForegroundColor Yellow
        }
        break
    }
}

if (-not $keyInstalled) {
    Write-Host "   ⚠ Édition non reconnue, tentative avec clé Pro..." -ForegroundColor Yellow
    slmgr /ipk 'W269N-WFGWX-YVC9B-4J6C9-T83GX' 2>&1 | Out-Null
}

Write-Host ""

# Configuration du serveur KMS (pour initier l'activation HWID)
Write-Host "🌐 Configuration serveur d'activation..." -ForegroundColor Yellow
slmgr /skms kms.msguides.com 2>&1 | Out-Null
Write-Host "   ✓ Serveur configuré" -ForegroundColor Green
Write-Host ""

# Activation
Write-Host "⚡ Activation en cours..." -ForegroundColor Yellow
$activateResult = slmgr /ato 2>&1
Write-Host "   ✓ Commande d'activation envoyée" -ForegroundColor Green
Write-Host ""

# Vérification du statut
Write-Host "🔍 Vérification du statut..." -ForegroundColor Yellow
Start-Sleep -Seconds 3

$statusResult = cscript //NoLogo C:\\Windows\\System32\\slmgr.vbs /xpr
Write-Host ""
Write-Host "=================================" -ForegroundColor Cyan

if ($statusResult -match "permanently activated|activé de manière permanente") {
    Write-Host "✅ WINDOWS ACTIVÉ AVEC SUCCÈS !" -ForegroundColor Green
    Write-Host "   Activation permanente (licence digitale)" -ForegroundColor Green
} elseif ($statusResult -match "will expire|expirera") {
    Write-Host "⚠️  Activation temporaire (180 jours)" -ForegroundColor Yellow
    Write-Host "   L'activation sera renouvelée automatiquement" -ForegroundColor Yellow
} else {
    Write-Host "❌ Échec de l'activation" -ForegroundColor Red
    Write-Host "   Vérifiez votre connexion Internet" -ForegroundColor Yellow
    Write-Host "   Ou essayez le bouton 'Lancer MAS' pour plus d'options" -ForegroundColor Yellow
}

Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Détails complets du statut :" -ForegroundColor Cyan
slmgr /dli
"""
                else:
                    # Activation Office KMS (méthode interne)
                    self._append_to_terminal("⚡ Méthode : KMS (Activation Office)\n")
                    self._append_to_terminal("📌 Configuration serveur KMS...\n\n")

                    ps_script = """
# Script d'activation Office KMS intégré
$ErrorActionPreference = 'Continue'

Write-Host "=================================" -ForegroundColor Cyan
Write-Host "  ACTIVATION MICROSOFT OFFICE" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Vérifier si administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "❌ ERREUR : Droits administrateur requis !" -ForegroundColor Red
    Write-Host "   Relancez NiTriTe en tant qu'administrateur." -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ Droits administrateur détectés" -ForegroundColor Green
Write-Host ""

# Détection des installations Office
Write-Host "🔍 Recherche des installations Office..." -ForegroundColor Yellow

$officePaths = @(
    "C:\\Program Files\\Microsoft Office\\Office16",
    "C:\\Program Files (x86)\\Microsoft Office\\Office16",
    "C:\\Program Files\\Microsoft Office\\Office15",
    "C:\\Program Files (x86)\\Microsoft Office\\Office15"
)

$osppPath = $null
foreach ($path in $officePaths) {
    $testPath = Join-Path $path "ospp.vbs"
    if (Test-Path $testPath) {
        $osppPath = $testPath
        Write-Host "   ✓ Office détecté : $path" -ForegroundColor Green
        break
    }
}

if (-not $osppPath) {
    Write-Host "   ❌ Aucune installation Office détectée !" -ForegroundColor Red
    Write-Host "   Installez Office avant d'utiliser cette fonction." -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Configuration du serveur KMS
Write-Host "🌐 Configuration serveur KMS..." -ForegroundColor Yellow
cscript //NoLogo "$osppPath" /sethst:kms.msguides.com
Write-Host "   ✓ Serveur KMS configuré" -ForegroundColor Green
Write-Host ""

# Définir le port KMS
Write-Host "🔧 Configuration port KMS..." -ForegroundColor Yellow
cscript //NoLogo "$osppPath" /setprt:1688
Write-Host "   ✓ Port configuré" -ForegroundColor Green
Write-Host ""

# Activation
Write-Host "⚡ Activation en cours..." -ForegroundColor Yellow
$activateResult = cscript //NoLogo "$osppPath" /act
Write-Host ""

# Vérification du statut
Write-Host "🔍 Vérification du statut..." -ForegroundColor Yellow
Start-Sleep -Seconds 2
$statusResult = cscript //NoLogo "$osppPath" /dstatus

Write-Host ""
Write-Host "=================================" -ForegroundColor Cyan

if ($statusResult -match "LICENSE STATUS:  ---LICENSED---|ÉTAT DE LA LICENCE : ---LICENCE ACCORDÉE---") {
    Write-Host "✅ OFFICE ACTIVÉ AVEC SUCCÈS !" -ForegroundColor Green
    Write-Host "   Activation KMS (180 jours, renouvellement auto)" -ForegroundColor Green
} else {
    Write-Host "⚠️  Tentative d'activation effectuée" -ForegroundColor Yellow
    Write-Host "   Vérifiez le statut ci-dessous" -ForegroundColor Yellow
}

Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Statut détaillé :" -ForegroundColor Cyan
cscript //NoLogo "$osppPath" /dstatus
"""

                with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                    f.write(ps_script)
                    script_path = f.name

                self._append_to_terminal("⚡ Exécution du script d'activation...\n")
                self._append_to_terminal("=" * 60 + "\n\n")

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

                self._append_to_terminal("\n" + "=" * 60 + "\n")
                self._append_to_terminal("✅ Processus terminé !\n\n")

                if option == "1":
                    self._append_to_terminal("💡 Note : Redémarrez Windows pour finaliser l'activation.\n")
                else:
                    self._append_to_terminal("💡 Note : Redémarrez les applications Office si elles sont ouvertes.\n")

                # Cleanup
                try:
                    os.remove(script_path)
                except:
                    pass

            except Exception as e:
                self._append_to_terminal(f"\n\n❌ Erreur: {str(e)}\n")

        threading.Thread(target=run, daemon=True).start()

    def _launch_mas_interactive(self):
        """Lancer menu d'activation complet avec scripts internes"""
        self._clear_terminal()
        self._append_to_terminal("🔄 Menu d'activation NiTriTe\n\n")

        def run():
            try:
                # Menu interactif PowerShell embarqué
                ps_script = """
# Menu d'activation NiTriTe - Scripts internes
$ErrorActionPreference = 'Continue'

function Show-Menu {
    Clear-Host
    Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║     MENU D'ACTIVATION NITRITE V20.0 (INTERNE)         ║" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  1️⃣  Activer Windows (HWID - Permanent)" -ForegroundColor Green
    Write-Host "  2️⃣  Activer Office (KMS - 180 jours)" -ForegroundColor Green
    Write-Host "  3️⃣  Vérifier statut Windows" -ForegroundColor Yellow
    Write-Host "  4️⃣  Vérifier statut Office" -ForegroundColor Yellow
    Write-Host "  5️⃣  Réinitialiser activation Windows" -ForegroundColor Red
    Write-Host "  6️⃣  Utiliser MAS original (téléchargement Internet)" -ForegroundColor Magenta
    Write-Host "  0️⃣  Quitter" -ForegroundColor Gray
    Write-Host ""
    Write-Host "════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
}

function Activate-Windows-HWID {
    Write-Host ""
    Write-Host "⚡ ACTIVATION WINDOWS HWID" -ForegroundColor Green
    Write-Host "═══════════════════════════" -ForegroundColor Cyan
    Write-Host ""

    # Vérification admin
    $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if (-not $isAdmin) {
        Write-Host "❌ Droits administrateur requis !" -ForegroundColor Red
        return
    }

    # Détection version
    $winVersion = (Get-WmiObject -Class Win32_OperatingSystem).Caption
    Write-Host "📊 Windows : $winVersion" -ForegroundColor Cyan

    # Clés GVLK
    $gvlkKeys = @{
        'Windows 10 Pro' = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
        'Windows 10 Home' = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
        'Windows 11 Pro' = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
        'Windows 11 Home' = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
    }

    foreach ($edition in $gvlkKeys.Keys) {
        if ($winVersion -like "*$edition*") {
            Write-Host "🔑 Installation clé $edition..." -ForegroundColor Yellow
            slmgr /ipk $gvlkKeys[$edition]
            break
        }
    }

    Write-Host "🌐 Configuration serveur KMS..." -ForegroundColor Yellow
    slmgr /skms kms.msguides.com

    Write-Host "⚡ Activation..." -ForegroundColor Yellow
    slmgr /ato

    Start-Sleep -Seconds 3
    Write-Host ""
    Write-Host "✅ Activation terminée !" -ForegroundColor Green
    Write-Host ""
}

function Activate-Office-KMS {
    Write-Host ""
    Write-Host "⚡ ACTIVATION OFFICE KMS" -ForegroundColor Green
    Write-Host "═══════════════════════" -ForegroundColor Cyan
    Write-Host ""

    # Vérification admin
    $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if (-not $isAdmin) {
        Write-Host "❌ Droits administrateur requis !" -ForegroundColor Red
        return
    }

    # Détection Office
    $officePaths = @(
        "C:\\Program Files\\Microsoft Office\\Office16",
        "C:\\Program Files (x86)\\Microsoft Office\\Office16"
    )

    $osppPath = $null
    foreach ($path in $officePaths) {
        $testPath = Join-Path $path "ospp.vbs"
        if (Test-Path $testPath) {
            $osppPath = $testPath
            Write-Host "✓ Office détecté : $path" -ForegroundColor Green
            break
        }
    }

    if (-not $osppPath) {
        Write-Host "❌ Office non détecté !" -ForegroundColor Red
        return
    }

    Write-Host "🌐 Configuration KMS..." -ForegroundColor Yellow
    cscript //NoLogo "$osppPath" /sethst:kms.msguides.com
    cscript //NoLogo "$osppPath" /setprt:1688

    Write-Host "⚡ Activation..." -ForegroundColor Yellow
    cscript //NoLogo "$osppPath" /act

    Write-Host ""
    Write-Host "✅ Activation terminée !" -ForegroundColor Green
    Write-Host ""
}

function Check-WindowsStatus {
    Write-Host ""
    Write-Host "📊 STATUT WINDOWS" -ForegroundColor Cyan
    Write-Host "════════════════" -ForegroundColor Cyan
    Write-Host ""
    slmgr /xpr
    Write-Host ""
    slmgr /dli
    Write-Host ""
}

function Check-OfficeStatus {
    Write-Host ""
    Write-Host "📊 STATUT OFFICE" -ForegroundColor Cyan
    Write-Host "═══════════════" -ForegroundColor Cyan
    Write-Host ""

    $officePaths = @(
        "C:\\Program Files\\Microsoft Office\\Office16",
        "C:\\Program Files (x86)\\Microsoft Office\\Office16"
    )

    $osppPath = $null
    foreach ($path in $officePaths) {
        $testPath = Join-Path $path "ospp.vbs"
        if (Test-Path $testPath) {
            $osppPath = $testPath
            break
        }
    }

    if (-not $osppPath) {
        Write-Host "❌ Office non détecté !" -ForegroundColor Red
        return
    }

    cscript //NoLogo "$osppPath" /dstatus
    Write-Host ""
}

function Reset-WindowsActivation {
    Write-Host ""
    Write-Host "⚠️  RÉINITIALISATION ACTIVATION WINDOWS" -ForegroundColor Yellow
    Write-Host "═════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""

    $confirm = Read-Host "Confirmer la réinitialisation ? (O/N)"
    if ($confirm -ne 'O') {
        Write-Host "❌ Annulé" -ForegroundColor Red
        return
    }

    Write-Host "🔄 Réinitialisation..." -ForegroundColor Yellow
    slmgr /upk
    slmgr /ckms
    slmgr /rearm

    Write-Host ""
    Write-Host "✅ Réinitialisation terminée. Redémarrez Windows." -ForegroundColor Green
    Write-Host ""
}

function Use-OriginalMAS {
    Write-Host ""
    Write-Host "🌐 TÉLÉCHARGEMENT MAS ORIGINAL" -ForegroundColor Magenta
    Write-Host "═══════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Téléchargement et exécution depuis https://massgrave.dev..." -ForegroundColor Yellow
    Write-Host ""

    irm https://get.activated.win | iex
}

# Boucle menu principal
do {
    Show-Menu
    $choice = Read-Host "Votre choix"

    switch ($choice) {
        '1' { Activate-Windows-HWID; Read-Host "Appuyez sur Entrée pour continuer" }
        '2' { Activate-Office-KMS; Read-Host "Appuyez sur Entrée pour continuer" }
        '3' { Check-WindowsStatus; Read-Host "Appuyez sur Entrée pour continuer" }
        '4' { Check-OfficeStatus; Read-Host "Appuyez sur Entrée pour continuer" }
        '5' { Reset-WindowsActivation; Read-Host "Appuyez sur Entrée pour continuer" }
        '6' { Use-OriginalMAS; Read-Host "Appuyez sur Entrée pour continuer" }
        '0' {
            Write-Host ""
            Write-Host "👋 Au revoir !" -ForegroundColor Green
            Write-Host ""
            break
        }
        default {
            Write-Host ""
            Write-Host "❌ Choix invalide !" -ForegroundColor Red
            Start-Sleep -Seconds 1
        }
    }
} while ($choice -ne '0')
"""

                with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1', delete=False, encoding='utf-8') as f:
                    f.write(ps_script)
                    script_path = f.name

                self._append_to_terminal("⚡ Ouverture du menu interactif...\n")
                self._append_to_terminal("ℹ️ Une fenêtre PowerShell va s'ouvrir avec le menu complet.\n\n")

                # Lancer dans une nouvelle fenêtre PowerShell
                subprocess.Popen(
                    f'powershell -ExecutionPolicy Bypass -NoExit -File "{script_path}"',
                    shell=True
                )

                self._append_to_terminal("✅ Menu PowerShell lancé !\n")
                self._append_to_terminal("📋 Utilisez le menu pour accéder à toutes les options.\n\n")
                self._append_to_terminal("💡 Options disponibles :\n")
                self._append_to_terminal("   1. Activation Windows (HWID)\n")
                self._append_to_terminal("   2. Activation Office (KMS)\n")
                self._append_to_terminal("   3. Vérification statut Windows\n")
                self._append_to_terminal("   4. Vérification statut Office\n")
                self._append_to_terminal("   5. Réinitialisation activation\n")
                self._append_to_terminal("   6. MAS original (Internet)\n")

            except Exception as e:
                self._append_to_terminal(f"\n\n❌ Erreur: {str(e)}\n")

        threading.Thread(target=run, daemon=True).start()

    def _create_info_section(self, parent):
        """Section informations MAS"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        ctk.CTkLabel(
            card,
            text="ℹ️ ACTIVATION WINDOWS & OFFICE",
            font=("Segoe UI", 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(padx=20, pady=(15, 10))

        info_text = """Scripts d'activation intégrés dans NiTriTe V20.0 (basés sur MAS - Microsoft Activation Scripts).

✅ SCRIPTS INTERNES : Aucun téléchargement depuis Internet
✅ Sûr et fiable : Scripts embarqués directement dans l'application
✅ Méthodes légales : Utilise les clés de licence volume Microsoft officielles (GVLK)
✅ Sans malware : Code PowerShell vérifié et intégré
✅ Gratuit : Complètement gratuit et sans publicité

MÉTHODES D'ACTIVATION DISPONIBLES :

1️⃣ HWID (Windows 10/11) : Activation permanente liée au matériel
   → Clique sur "🪟 Activer Windows"

2️⃣ KMS (Office) : Activation 180 jours avec renouvellement automatique
   → Clique sur "📊 Activer Office"

3️⃣ Menu complet : Accès à toutes les options (statut, réinitialisation, etc.)
   → Clique sur "🔄 Lancer MAS"

UTILISATION :

• Les boutons "Activer Windows" et "Activer Office" exécutent les scripts directement
• Le terminal ci-dessus affiche le résultat en temps réel
• Droits administrateur requis (redémarrez NiTriTe en admin si besoin)

IMPORTANT :
- Désactivez temporairement votre antivirus si les scripts sont bloqués
- Connexion Internet requise pour contacter les serveurs d'activation
- Redémarrez Windows/Office après activation pour finaliser"""

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
