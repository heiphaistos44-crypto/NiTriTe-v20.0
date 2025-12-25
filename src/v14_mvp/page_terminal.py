#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Terminal Intégré - NiTriTe V14
Terminal interactif avec CMD, PowerShell et Windows PowerShell
"""

import customtkinter as ctk
import tkinter as tk
import subprocess
import threading
import queue
from typing import Optional
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton


class TerminalPage(ctk.CTkFrame):
    """Page Terminal avec 3 onglets: CMD, PowerShell, Windows PowerShell"""
    
    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)
        
        self._create_header()
        self._create_tabs()
    
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
            text=" Terminal Intégré",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)
        
        subtitle = ctk.CTkLabel(
            left_side,
            text="CMD • PowerShell • Git Bash • Azure Cloud Shell • WSL",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.LEFT, padx=20)
    
    def _create_tabs(self):
        """Créer onglets de terminaux"""
        # Container pour onglets
        tabs_container = ctk.CTkFrame(self, fg_color="transparent")
        tabs_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Barre d'onglets
        tabs_bar = ctk.CTkFrame(
            tabs_container,
            fg_color=DesignTokens.BG_SECONDARY,
            height=50
        )
        tabs_bar.pack(fill=tk.X, pady=(0, 10))
        tabs_bar.pack_propagate(False)
        
        # Container pour contenu des onglets
        self.tabs_content = ctk.CTkFrame(
            tabs_container,
            fg_color=DesignTokens.BG_PRIMARY
        )
        self.tabs_content.pack(fill=tk.BOTH, expand=True)
        
        # État
        self.current_tab = None
        self.tabs = {}
        self.tab_buttons = {}
        
        # Créer onglets
        tab_configs = [
            ("cmd", " CMD", "cmd.exe", DesignTokens.INFO),
            ("powershell", " PowerShell", "powershell.exe", DesignTokens.ACCENT_PRIMARY),
            ("pwsh", " Windows PowerShell", "pwsh.exe", DesignTokens.SUCCESS),
            ("gitbash", " Git Bash", "bash.exe", "#F05032"),
            ("wsl", " WSL (Ubuntu)", "wsl.exe", "#E95420"),
            ("azure", " Azure Cloud Shell", "az", "#0078D4"),
        ]
        
        for tab_id, tab_name, shell_cmd, color in tab_configs:
            # Bouton onglet
            btn = ctk.CTkButton(
                tabs_bar,
                text=tab_name,
                command=lambda tid=tab_id: self._switch_tab(tid),
                fg_color="transparent",
                hover_color=DesignTokens.BG_HOVER,
                text_color=DesignTokens.TEXT_SECONDARY,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
                corner_radius=DesignTokens.RADIUS_SM,
                height=40,
                width=200
            )
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            self.tab_buttons[tab_id] = btn
            
            # Contenu onglet
            tab_frame = self._create_terminal_tab(shell_cmd, color)
            self.tabs[tab_id] = tab_frame
        
        # Sélectionner premier onglet
        self._switch_tab("cmd")
    
    def _create_terminal_tab(self, shell_cmd, color):
        """Créer un onglet de terminal"""
        tab = ctk.CTkFrame(self.tabs_content, fg_color=DesignTokens.BG_PRIMARY)
        
        # Zone de sortie (lecture seule)
        output_container = ctk.CTkFrame(
            tab,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        output_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        
        # Scrollbar + Text widget
        output_frame = ctk.CTkFrame(output_container, fg_color="transparent")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ctk.CTkScrollbar(output_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        output_text = tk.Text(
            output_frame,
            wrap=tk.WORD,
            bg="#1a1a1a",
            fg="#00ff00",
            insertbackground="#00ff00",
            font=("Consolas", 10),
            relief=tk.FLAT,
            borderwidth=0,
            padx=10,
            pady=10,
            yscrollcommand=scrollbar.set
        )
        output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.configure(command=output_text.yview)
        
        # Zone de saisie
        input_container = ctk.CTkFrame(
            tab,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD,
            height=50
        )
        input_container.pack(fill=tk.X, padx=10, pady=(5, 10))
        input_container.pack_propagate(False)
        
        input_frame = ctk.CTkFrame(input_container, fg_color="transparent")
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Prompt
        prompt_label = ctk.CTkLabel(
            input_frame,
            text=">",
            font=("Consolas", 12, "bold"),
            text_color=color,
            width=20
        )
        prompt_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Entry
        input_entry = ctk.CTkEntry(
            input_frame,
            font=("Consolas", 11),
            fg_color="#1a1a1a",
            border_width=0,
            height=30
        )
        input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Bouton exécuter
        exec_btn = ModernButton(
            input_frame,
            text="",
            size="sm",
            command=lambda: self._execute_command(tab, shell_cmd)
        )
        exec_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton clear
        clear_btn = ModernButton(
            input_frame,
            text="",
            variant="text",
            size="sm",
            command=lambda: self._clear_output(tab)
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Store references
        tab.output_text = output_text
        tab.input_entry = input_entry
        tab.shell_cmd = shell_cmd
        tab.process = None
        tab.output_queue = queue.Queue()
        tab.history = []
        tab.history_index = -1
        
        # Bind events
        input_entry.bind('<Return>', lambda e: self._execute_command(tab, shell_cmd))
        input_entry.bind('<Up>', lambda e: self._history_up(tab))
        input_entry.bind('<Down>', lambda e: self._history_down(tab))
        
        # Message de bienvenue
        welcome_msg = f"""
  NiTriTe V20.0 - Terminal Intégré
  Shell: {shell_cmd:<50}


Tapez vos commandes ci-dessous et appuyez sur Entrée...
Utilisez ↑/↓ pour naviguer dans l'historique.

"""
        output_text.insert(tk.END, welcome_msg)
        output_text.see(tk.END)
        
        return tab
    
    def _switch_tab(self, tab_id):
        """Changer d'onglet"""
        # Cacher tous
        for tid, tab in self.tabs.items():
            tab.pack_forget()
            self.tab_buttons[tid].configure(
                fg_color="transparent",
                text_color=DesignTokens.TEXT_SECONDARY
            )
        
        # Afficher sélectionné
        if tab_id in self.tabs:
            self.tabs[tab_id].pack(fill=tk.BOTH, expand=True)
            self.tab_buttons[tab_id].configure(
                fg_color=DesignTokens.ACCENT_PRIMARY,
                text_color="white"
            )
            self.current_tab = tab_id
            
            # Focus sur l'input
            self.tabs[tab_id].input_entry.focus_set()
    
    def _execute_command(self, tab, shell_cmd):
        """Exécuter une commande"""
        command = tab.input_entry.get().strip()
        
        if not command:
            return
        
        # Ajouter à l'historique
        if command not in tab.history:
            tab.history.append(command)
        tab.history_index = len(tab.history)
        
        # Afficher commande
        prompt_symbol = ">" if "cmd" in shell_cmd else "PS>"
        tab.output_text.insert(tk.END, f"\n{prompt_symbol} {command}\n")
        tab.output_text.see(tk.END)
        
        # Clear input
        tab.input_entry.delete(0, tk.END)
        
        # Commandes spéciales
        if command.lower() == "clear" or command.lower() == "cls":
            self._clear_output(tab)
            return
        
        if command.lower() == "exit":
            tab.output_text.insert(tk.END, " Utilisez le bouton  pour vider le terminal.\n")
            tab.output_text.see(tk.END)
            return
        
        # Exécuter commande dans un thread
        def run_command():
            try:
                # Construire commande selon le shell
                if "powershell" in shell_cmd.lower() or shell_cmd == "pwsh.exe":
                    full_cmd = [shell_cmd, "-NoProfile", "-Command", command]
                elif "bash" in shell_cmd.lower() or shell_cmd == "bash.exe":
                    full_cmd = [shell_cmd, "-c", command]
                elif shell_cmd == "wsl.exe":
                    full_cmd = [shell_cmd, "--", "bash", "-c", command]
                elif shell_cmd == "az":
                    # Azure Cloud Shell nécessite une connexion
                    full_cmd = ["powershell", "-Command", f"az {command}"]
                else:
                    full_cmd = [shell_cmd, "/C", command]
                
                # Exécuter
                process = subprocess.Popen(
                    full_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
                )
                
                # Lire sortie
                stdout, stderr = process.communicate(timeout=30)
                
                # Afficher résultat
                def show_output():
                    if stdout:
                        tab.output_text.insert(tk.END, stdout)
                    if stderr:
                        tab.output_text.insert(tk.END, f"\n Erreur:\n{stderr}")
                    if process.returncode != 0:
                        tab.output_text.insert(tk.END, f"\n Code de retour: {process.returncode}\n")
                    tab.output_text.insert(tk.END, "\n")
                    tab.output_text.see(tk.END)
                
                tab.output_text.after(0, show_output)
            
            except subprocess.TimeoutExpired:
                def show_timeout():
                    tab.output_text.insert(tk.END, "\n⏱ Timeout (30s) - Commande interrompue\n\n")
                    tab.output_text.see(tk.END)
                tab.output_text.after(0, show_timeout)
            
            except Exception as e:
                def show_error():
                    tab.output_text.insert(tk.END, f"\n Erreur: {str(e)}\n\n")
                    tab.output_text.see(tk.END)
                tab.output_text.after(0, show_error)
        
        thread = threading.Thread(target=run_command, daemon=True)
        thread.start()
    
    def _clear_output(self, tab):
        """Vider le terminal"""
        tab.output_text.delete(1.0, tk.END)
        
        # Réafficher message de bienvenue
        welcome_msg = f"""
  Terminal vidé                                                


"""
        tab.output_text.insert(tk.END, welcome_msg)
        tab.output_text.see(tk.END)
    
    def _history_up(self, tab):
        """Naviguer vers le haut dans l'historique"""
        if not tab.history:
            return
        
        if tab.history_index > 0:
            tab.history_index -= 1
            tab.input_entry.delete(0, tk.END)
            tab.input_entry.insert(0, tab.history[tab.history_index])
    
    def _history_down(self, tab):
        """Naviguer vers le bas dans l'historique"""
        if not tab.history:
            return
        
        if tab.history_index < len(tab.history) - 1:
            tab.history_index += 1
            tab.input_entry.delete(0, tk.END)
            tab.input_entry.insert(0, tab.history[tab.history_index])
        else:
            tab.history_index = len(tab.history)
            tab.input_entry.delete(0, tk.END)