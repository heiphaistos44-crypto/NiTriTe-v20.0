#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dialogue de Progression avec Logs - NiTriTe V17
Fenêtre de progression pour afficher les installations avec logs en temps réel
"""

import customtkinter as ctk
import tkinter as tk
from typing import Callable, Optional
import threading


class ProgressDialog(ctk.CTkToplevel):
    """Dialogue de progression avec logs CMD style"""

    def __init__(self, parent, title="Installation en cours..."):
        super().__init__(parent)

        self.title(title)
        self.geometry("700x500")
        self.resizable(True, True)

        # Centrer la fenêtre
        self.transient(parent)
        self.grab_set()

        # Configuration
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Variables
        self.is_cancelled = False
        self.is_completed = False

        self._create_ui()

    def _create_ui(self):
        """Créer l'interface"""
        # Container principal
        main_container = ctk.CTkFrame(self, fg_color="#0a0a0a")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titre
        self.title_label = ctk.CTkLabel(
            main_container,
            text="Installation en cours...",
            font=("Segoe UI", 16, "bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=(0, 10))

        # Barre de progression
        self.progress_bar = ctk.CTkProgressBar(
            main_container,
            width=660,
            height=20,
            fg_color="#202020",
            progress_color="#ff6b35"
        )
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        # Label de statut
        self.status_label = ctk.CTkLabel(
            main_container,
            text="Préparation...",
            font=("Segoe UI", 12),
            text_color="#b0b0b0"
        )
        self.status_label.pack(pady=(0, 10))

        # Zone de logs (style CMD)
        logs_frame = ctk.CTkFrame(main_container, fg_color="#000000")
        logs_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar
        scrollbar = ctk.CTkScrollbar(logs_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget pour les logs
        self.logs_text = tk.Text(
            logs_frame,
            bg="#000000",
            fg="#00ff00",  # Vert comme CMD
            font=("Consolas", 10),
            wrap=tk.WORD,
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.configure(command=self.logs_text.yview)

        # Configuration des tags pour coloration
        self.logs_text.tag_config("info", foreground="#00ff00")
        self.logs_text.tag_config("success", foreground="#00ff00", font=("Consolas", 10, "bold"))
        self.logs_text.tag_config("error", foreground="#ff0000", font=("Consolas", 10, "bold"))
        self.logs_text.tag_config("warning", foreground="#ffff00")

        # Boutons
        buttons_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        buttons_frame.pack(fill=tk.X, pady=(10, 0))

        self.cancel_button = ctk.CTkButton(
            buttons_frame,
            text="Annuler",
            command=self.cancel,
            fg_color="#f44336",
            hover_color="#d32f2f",
            width=100
        )
        self.cancel_button.pack(side=tk.LEFT)

        self.close_button = ctk.CTkButton(
            buttons_frame,
            text="Fermer",
            command=self.close,
            fg_color="#4caf50",
            hover_color="#388e3c",
            width=100,
            state=tk.DISABLED
        )
        self.close_button.pack(side=tk.RIGHT)

    def update_progress(self, value: float, status: str = ""):
        """
        Mettre à jour la progression

        Args:
            value: Valeur entre 0 et 1
            status: Texte de statut
        """
        self.progress_bar.set(value)
        if status:
            self.status_label.configure(text=status)
        self.update()

    def add_log(self, message: str, level: str = "info"):
        """
        Ajouter un message au log

        Args:
            message: Message à afficher
            level: "info", "success", "error", "warning"
        """
        self.logs_text.configure(state=tk.NORMAL)

        # Ajouter timestamp
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        # Ajouter le message avec tag
        self.logs_text.insert(tk.END, f"[{timestamp}] ", "info")
        self.logs_text.insert(tk.END, f"{message}\n", level)

        # Auto-scroll
        self.logs_text.see(tk.END)

        self.logs_text.configure(state=tk.DISABLED)
        self.update()

    def set_title_text(self, text: str):
        """Changer le titre"""
        self.title_label.configure(text=text)
        self.update()

    def mark_completed(self, success: bool = True):
        """Marquer comme terminé"""
        self.is_completed = True

        if success:
            self.progress_bar.set(1.0)
            self.status_label.configure(text=" Installation terminée avec succès !")
            self.add_log("=== INSTALLATION TERMINÉE AVEC SUCCÈS ===", "success")
            self.title_label.configure(text=" Installation réussie")
        else:
            self.status_label.configure(text=" Installation échouée")
            self.add_log("=== INSTALLATION ÉCHOUÉE ===", "error")
            self.title_label.configure(text=" Installation échouée")

        self.cancel_button.configure(state=tk.DISABLED)
        self.close_button.configure(state=tk.NORMAL)
        self.update()

    def cancel(self):
        """Annuler l'opération"""
        self.is_cancelled = True
        self.add_log("ANNULATION DEMANDÉE PAR L'UTILISATEUR", "warning")
        self.cancel_button.configure(state=tk.DISABLED)
        self.close_button.configure(state=tk.NORMAL)

    def close(self):
        """Fermer la fenêtre"""
        self.grab_release()
        self.destroy()

    def on_closing(self):
        """Gestion de la fermeture"""
        if not self.is_completed:
            self.cancel()
        else:
            self.close()


class MultiProgressDialog(ctk.CTkToplevel):
    """Dialogue de progression pour installations multiples"""

    def __init__(self, parent, title="Installations multiples"):
        super().__init__(parent)

        self.title(title)
        self.geometry("800x600")
        self.resizable(True, True)

        # Centrer
        self.transient(parent)
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Variables
        self.is_cancelled = False
        self.total_apps = 0
        self.completed_apps = 0
        self.failed_apps = 0

        self._create_ui()

    def _create_ui(self):
        """Créer l'interface"""
        main_container = ctk.CTkFrame(self, fg_color="#0a0a0a")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Titre
        self.title_label = ctk.CTkLabel(
            main_container,
            text="Installation de plusieurs applications",
            font=("Segoe UI", 16, "bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=(0, 10))

        # Progression globale
        progress_container = ctk.CTkFrame(main_container, fg_color="transparent")
        progress_container.pack(fill=tk.X, pady=10)

        self.global_status = ctk.CTkLabel(
            progress_container,
            text="0 / 0 applications installées",
            font=("Segoe UI", 12),
            text_color="#b0b0b0"
        )
        self.global_status.pack()

        self.global_progress = ctk.CTkProgressBar(
            progress_container,
            width=760,
            height=20,
            fg_color="#202020",
            progress_color="#ff6b35"
        )
        self.global_progress.pack(pady=5)
        self.global_progress.set(0)

        # Application en cours
        current_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        current_frame.pack(fill=tk.X, pady=10)

        self.current_app_label = ctk.CTkLabel(
            current_frame,
            text="Application en cours: -",
            font=("Segoe UI", 12, "bold"),
            text_color="#ff6b35"
        )
        self.current_app_label.pack()

        self.current_progress = ctk.CTkProgressBar(
            current_frame,
            width=760,
            height=15,
            fg_color="#202020",
            progress_color="#4caf50"
        )
        self.current_progress.pack(pady=5)
        self.current_progress.set(0)

        # Zone de logs
        logs_frame = ctk.CTkFrame(main_container, fg_color="#000000")
        logs_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = ctk.CTkScrollbar(logs_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.logs_text = tk.Text(
            logs_frame,
            bg="#000000",
            fg="#00ff00",
            font=("Consolas", 9),
            wrap=tk.WORD,
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.configure(command=self.logs_text.yview)

        # Tags
        self.logs_text.tag_config("info", foreground="#00ff00")
        self.logs_text.tag_config("success", foreground="#00ff00", font=("Consolas", 9, "bold"))
        self.logs_text.tag_config("error", foreground="#ff0000", font=("Consolas", 9, "bold"))
        self.logs_text.tag_config("warning", foreground="#ffff00")
        self.logs_text.tag_config("header", foreground="#00ffff", font=("Consolas", 10, "bold"))

        # Boutons
        buttons_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        buttons_frame.pack(fill=tk.X, pady=(10, 0))

        self.cancel_button = ctk.CTkButton(
            buttons_frame,
            text="Annuler tout",
            command=self.cancel,
            fg_color="#f44336",
            hover_color="#d32f2f",
            width=120
        )
        self.cancel_button.pack(side=tk.LEFT)

        self.close_button = ctk.CTkButton(
            buttons_frame,
            text="Fermer",
            command=self.close,
            fg_color="#4caf50",
            hover_color="#388e3c",
            width=120,
            state=tk.DISABLED
        )
        self.close_button.pack(side=tk.RIGHT)

    def set_total_apps(self, total: int):
        """Définir le nombre total d'applications"""
        self.total_apps = total
        self.global_status.configure(text=f"0 / {total} applications installées")

    def start_app(self, app_name: str):
        """Démarrer l'installation d'une app"""
        self.current_app_label.configure(text=f"Application en cours: {app_name}")
        self.current_progress.set(0)
        self.add_log(f"", "info")
        self.add_log(f"{'='*70}", "header")
        self.add_log(f"INSTALLATION: {app_name}", "header")
        self.add_log(f"{'='*70}", "header")

    def update_app_progress(self, value: float, status: str = ""):
        """Mettre à jour la progression de l'app en cours"""
        self.current_progress.set(value)
        if status:
            self.add_log(status, "info")

    def complete_app(self, success: bool):
        """Marquer l'app en cours comme terminée"""
        self.completed_apps += 1
        if not success:
            self.failed_apps += 1

        # Mettre à jour progression globale
        global_value = self.completed_apps / self.total_apps if self.total_apps > 0 else 0
        self.global_progress.set(global_value)
        self.global_status.configure(
            text=f"{self.completed_apps} / {self.total_apps} applications installées "
                 f"({self.failed_apps} échecs)"
        )

    def add_log(self, message: str, level: str = "info"):
        """Ajouter un log"""
        self.logs_text.configure(state=tk.NORMAL)

        if level != "header":
            import datetime
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.logs_text.insert(tk.END, f"[{timestamp}] ", "info")

        self.logs_text.insert(tk.END, f"{message}\n", level)
        self.logs_text.see(tk.END)
        self.logs_text.configure(state=tk.DISABLED)
        self.update()

    def mark_completed(self):
        """Marquer tout comme terminé"""
        success_count = self.completed_apps - self.failed_apps

        self.add_log("", "info")
        self.add_log("="*70, "header")
        self.add_log("INSTALLATION GLOBALE TERMINÉE", "header")
        self.add_log("="*70, "header")
        self.add_log(f"Total: {self.total_apps} applications", "info")
        self.add_log(f"Réussies: {success_count}", "success")
        if self.failed_apps > 0:
            self.add_log(f"Échouées: {self.failed_apps}", "error")

        self.cancel_button.configure(state=tk.DISABLED)
        self.close_button.configure(state=tk.NORMAL)

        if self.failed_apps == 0:
            self.title_label.configure(text=" Toutes les installations réussies !")
        else:
            self.title_label.configure(text=f" {self.failed_apps} installation(s) échouée(s)")

    def cancel(self):
        """Annuler"""
        self.is_cancelled = True
        self.add_log("ANNULATION GLOBALE DEMANDÉE", "warning")
        self.cancel_button.configure(state=tk.DISABLED)

    def close(self):
        """Fermer"""
        self.grab_release()
        self.destroy()

    def on_closing(self):
        """Gestion fermeture"""
        if self.completed_apps < self.total_apps:
            self.cancel()
        else:
            self.close()
