#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Logs - Visualisation et analyse des journaux Windows
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton
from v14_mvp.logger_system import logger
import subprocess
import os
from datetime import datetime, timedelta
from pathlib import Path

try:
    import win32evtlog
    import win32evtlogutil
    import win32con
    WIN32_AVAILABLE = True
except ImportError:
    WIN32_AVAILABLE = False
    print(" win32evtlog non disponible - installation: pip install pywin32")


class LogsPage(ctk.CTkFrame):
    """Page de visualisation des logs Windows"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.current_tab = "app"  # "app" ou "windows"

        try:
            logger.info("PageLogs", "Initialisation de la page Logs")
            self._create_header()
            logger.info("PageLogs", "Header créé")
            self._create_tabs()
            logger.info("PageLogs", "Tabs créés")
            self._create_content()
            logger.info("PageLogs", "Contenu créé - Page Logs chargée avec succès")
        except Exception as e:
            logger.log_exception("PageLogs", e, "Erreur lors de l'initialisation de la page Logs")
            # Créer un message d'erreur visible
            error_label = ctk.CTkLabel(
                self,
                text=f" Erreur de chargement de la page Logs:\n\n{str(e)}",
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color="#ff4444"
            )
            error_label.pack(expand=True)

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.pack(fill=tk.X, padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre
        title = ctk.CTkLabel(
            container,
            text=" Journaux Système",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(side=tk.LEFT)

        # Boutons d'action
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(side=tk.RIGHT)

        ModernButton(
            btn_frame,
            text=" Rafraîchir",
            variant="outlined",
            command=self._refresh_logs
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            btn_frame,
            text=" Exporter",
            variant="filled",
            command=self._export_logs
        ).pack(side=tk.LEFT, padx=5)

    def _create_tabs(self):
        """Créer les onglets"""
        tabs_frame = ctk.CTkFrame(self, fg_color="transparent")
        tabs_frame.pack(fill=tk.X, padx=20, pady=10)

        # Boutons d'onglets
        btn_frame = ctk.CTkFrame(tabs_frame, fg_color=DesignTokens.BG_SECONDARY,
                                 corner_radius=DesignTokens.RADIUS_MD)
        btn_frame.pack()

        self.tab_app_btn = ctk.CTkButton(
            btn_frame,
            text=" Logs Application",
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.BG_HOVER,
            command=lambda: self._switch_tab("app"),
            width=200,
            height=40,
            corner_radius=DesignTokens.RADIUS_MD
        )
        self.tab_app_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.tab_windows_btn = ctk.CTkButton(
            btn_frame,
            text="🪟 Logs Windows",
            fg_color="transparent",
            hover_color=DesignTokens.BG_HOVER,
            text_color=DesignTokens.TEXT_SECONDARY,
            command=lambda: self._switch_tab("windows"),
            width=200,
            height=40,
            corner_radius=DesignTokens.RADIUS_MD
        )
        self.tab_windows_btn.pack(side=tk.LEFT, padx=5, pady=5)

    def _switch_tab(self, tab):
        """Changer d'onglet"""
        self.current_tab = tab

        # Mettre à jour l'apparence des boutons
        if tab == "app":
            self.tab_app_btn.configure(
                fg_color=DesignTokens.ACCENT_PRIMARY,
                text_color="white"
            )
            self.tab_windows_btn.configure(
                fg_color="transparent",
                text_color=DesignTokens.TEXT_SECONDARY
            )
        else:
            self.tab_app_btn.configure(
                fg_color="transparent",
                text_color=DesignTokens.TEXT_SECONDARY
            )
            self.tab_windows_btn.configure(
                fg_color=DesignTokens.ACCENT_PRIMARY,
                text_color="white"
            )

        # Recréer le contenu
        self._create_content()

    def _create_content(self):
        """Contenu principal"""
        try:
            # Nettoyer le contenu existant (garder seulement header et tabs)
            children = self.winfo_children()
            logger.debug("PageLogs", f"Nombre de widgets enfants: {len(children)}")

            # Supprimer tous sauf les 2 premiers (header et tabs)
            if len(children) > 2:
                for widget in children[2:]:
                    widget.destroy()
                logger.debug("PageLogs", "Widgets nettoyés")

            # Conteneur avec scroll
            scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
            scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            # Fixer le problème de scroll
            self._bind_scroll_events(scroll)

            logger.debug("PageLogs", f"Scroll frame créé, onglet actuel: {self.current_tab}")

            if self.current_tab == "app":
                # Afficher les logs de l'application
                logger.info("PageLogs", "Affichage des logs application")
                self._create_app_logs_view(scroll)
            else:
                # Afficher les logs Windows
                logger.info("PageLogs", "Affichage des logs Windows")
                # Filtres
                self._create_filters(scroll)

                # Boutons d'actions rapides
                self._create_quick_actions(scroll)

                # Zone d'affichage des logs
                self._create_logs_display(scroll)

            logger.info("PageLogs", "Contenu créé avec succès")

        except Exception as e:
            logger.log_exception("PageLogs", e, "Erreur création contenu")
            # Afficher l'erreur à l'utilisateur
            error_label = ctk.CTkLabel(
                self,
                text=f" Erreur affichage:\n{str(e)}",
                font=(DesignTokens.FONT_FAMILY, 14),
                text_color="#ff4444"
            )
            error_label.pack(expand=True)

    def _create_app_logs_view(self, parent):
        """Affichage des logs de l'application NiTriTe"""
        logger.info("PageLogs", "Création de la vue logs application")

        # Statistiques
        stats_card = ModernCard(parent)
        stats_card.pack(fill=tk.X, pady=10)

        stats_title = ctk.CTkLabel(
            stats_card,
            text=" Statistiques",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        stats_title.pack(padx=20, pady=(15, 10), anchor="w")

        # Récupérer les stats d'erreurs
        error_counts = logger.get_error_count()

        stats_frame = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Erreurs critiques
        self._create_stat_item(stats_frame, " Critiques", error_counts.get("CRITICAL", 0), DesignTokens.ERROR)
        # Erreurs
        self._create_stat_item(stats_frame, " Erreurs", error_counts.get("ERROR", 0), DesignTokens.WARNING)
        # Avertissements
        self._create_stat_item(stats_frame, " Avertissements", error_counts.get("WARNING", 0), DesignTokens.INFO)

        # Boutons d'action
        actions_card = ModernCard(parent)
        actions_card.pack(fill=tk.X, pady=10)

        actions_title = ctk.CTkLabel(
            actions_card,
            text=" Actions",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        actions_title.pack(padx=20, pady=(15, 10), anchor="w")

        actions_btn_frame = ctk.CTkFrame(actions_card, fg_color="transparent")
        actions_btn_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        ModernButton(
            actions_btn_frame,
            text=" Ouvrir Dossier Logs",
            variant="outlined",
            command=self._open_logs_folder
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions_btn_frame,
            text=" Exporter ZIP",
            variant="outlined",
            command=self._export_logs_zip
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions_btn_frame,
            text=" Rafraîchir",
            variant="filled",
            command=lambda: self._create_content()
        ).pack(side=tk.LEFT, padx=5)

        # Affichage des logs
        logs_card = ModernCard(parent)
        logs_card.pack(fill=tk.BOTH, expand=True, pady=10)

        # Header avec boutons de redimensionnement
        header_frame = ctk.CTkFrame(logs_card, fg_color="transparent")
        header_frame.pack(fill=tk.X, padx=20, pady=(15, 10))

        logs_title = ctk.CTkLabel(
            header_frame,
            text=" Derniers Logs (100 entrées)",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        logs_title.pack(side=tk.LEFT)

        # Boutons de taille
        size_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        size_frame.pack(side=tk.RIGHT)

        ctk.CTkButton(
            size_frame,
            text="▼",
            width=30,
            height=20,
            font=(DesignTokens.FONT_FAMILY, 12),
            command=lambda: self._resize_app_logs(-100),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            size_frame,
            text="▲",
            width=30,
            height=20,
            font=(DesignTokens.FONT_FAMILY, 12),
            command=lambda: self._resize_app_logs(100),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        # Zone de texte pour les logs - CORRECTION: bg transparent pour le frame parent
        text_frame = ctk.CTkFrame(logs_card, fg_color="transparent")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        logger.debug("PageLogs", "Création Text widget pour logs app",
                    bg="#1e1e1e", fg="#00ff00")

        # Scrollbar
        scrollbar_app = ctk.CTkScrollbar(text_frame)
        scrollbar_app.pack(side=tk.RIGHT, fill=tk.Y)

        # Hauteur par défaut (initialiser si pas déjà fait)
        if not hasattr(self, 'app_logs_height'):
            self.app_logs_height = 500

        self.app_logs_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            bg="#000000",  # Fond noir
            fg="#00FF00",  # Vert Matrix
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=15,
            pady=15,
            insertbackground="#00FF00",
            yscrollcommand=scrollbar_app.set,
            height=self.app_logs_height
        )
        self.app_logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_app.configure(command=self.app_logs_text.yview)

        logger.debug("PageLogs", "Text widget logs app créé",
                    actual_bg=self.app_logs_text.cget("bg"),
                    actual_fg=self.app_logs_text.cget("fg"),
                    actual_font=self.app_logs_text.cget("font"))

        # Charger les logs
        logger.debug("PageLogs", "Chargement des logs app")
        self._load_app_logs()
        logger.debug("PageLogs", "Logs app chargés")

    def _create_stat_item(self, parent, label, value, color):
        """Créer un élément de statistique"""
        frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED,
                            corner_radius=DesignTokens.RADIUS_MD)
        frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ctk.CTkLabel(
            frame,
            text=str(value),
            font=(DesignTokens.FONT_FAMILY, 32, "bold"),
            text_color=color
        ).pack(pady=(10, 0))

        ctk.CTkLabel(
            frame,
            text=label,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(pady=(0, 10))

    def _load_app_logs(self):
        """Charger les logs de l'application"""
        try:
            logger.debug("PageLogs", "Récupération des logs via logger.get_recent_logs()")
            logs = logger.get_recent_logs(count=100)
            logger.debug("PageLogs", f"Logs récupérés: {len(logs) if logs else 0} lignes")

            self.app_logs_text.config(state=tk.NORMAL)
            self.app_logs_text.delete("1.0", tk.END)
            logger.debug("PageLogs", "Text widget configuré en mode NORMAL et vidé")

            if logs:
                logger.debug("PageLogs", f"Insertion de {len(logs)} lignes de logs")
                for i, log_line in enumerate(logs):
                    self.app_logs_text.insert("end", log_line)
                    if i < 3:  # Log les 3 premières lignes pour debug
                        logger.debug("PageLogs", f"Ligne {i}: {log_line[:100]}")
            else:
                logger.warning("PageLogs", "Aucun log disponible - affichage message par défaut")
                self.app_logs_text.insert("1.0", "Aucun log disponible.\n\n")
                self.app_logs_text.insert("end", "Les logs seront créés lors de l'utilisation de l'application.")

            self.app_logs_text.config(state=tk.DISABLED)
            logger.debug("PageLogs", "Text widget configuré en mode DISABLED")

            # Auto-scroll vers la fin
            self.app_logs_text.see(tk.END)
            logger.debug("PageLogs", "Scroll automatique effectué")

        except Exception as e:
            logger.log_exception("PageLogs", e, "Erreur chargement logs app")
            self.app_logs_text.config(state=tk.NORMAL)
            self.app_logs_text.delete("1.0", tk.END)
            self.app_logs_text.insert("1.0", f"Erreur de chargement des logs:\n\n{str(e)}")
            self.app_logs_text.config(state=tk.DISABLED)

    def _open_logs_folder(self):
        """Ouvrir le dossier des logs"""
        try:
            logs_dir = logger.log_dir
            os.startfile(str(logs_dir))
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n\n{str(e)}")

    def _export_logs_zip(self):
        """Exporter les logs dans un fichier ZIP"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".zip",
                filetypes=[("Fichiers ZIP", "*.zip"), ("Tous les fichiers", "*.*")],
                initialfile=f"nitrite_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            )

            if filename:
                if logger.export_logs_zip(filename):
                    messagebox.showinfo(
                        "Export réussi",
                        f"Les logs ont été exportés vers:\n\n{filename}"
                    )
                else:
                    messagebox.showerror("Erreur", "Échec de l'export des logs")

        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'exporter:\n\n{str(e)}")

    def _create_filters(self, parent):
        """Section de filtrage"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = ctk.CTkLabel(
            card,
            text=" Filtres",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=(15, 10))

        # Frame pour les filtres
        filters_frame = ctk.CTkFrame(card, fg_color="transparent")
        filters_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Type de journal
        log_type_frame = ctk.CTkFrame(filters_frame, fg_color="transparent")
        log_type_frame.pack(fill=tk.X, pady=5)

        ctk.CTkLabel(
            log_type_frame,
            text="Type de journal:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.LEFT, padx=10)

        self.log_type_var = tk.StringVar(value="System")
        log_types = [
            "System",
            "Application",
            "Security",
            "Setup",
            "Microsoft-Windows-PowerShell/Operational",
            "Microsoft-Windows-TaskScheduler/Operational",
            "Microsoft-Windows-Windows Defender/Operational",
            "Microsoft-Windows-WMI-Activity/Operational"
        ]

        # Dropdown pour plus de types
        log_dropdown = ctk.CTkOptionMenu(
            log_type_frame,
            variable=self.log_type_var,
            values=log_types,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            fg_color=DesignTokens.BG_ELEVATED,
            button_color=DesignTokens.ACCENT_PRIMARY,
            button_hover_color=DesignTokens.BG_HOVER,
            width=350
        )
        log_dropdown.pack(side=tk.LEFT, padx=10)

        # Niveau de sévérité
        severity_frame = ctk.CTkFrame(filters_frame, fg_color="transparent")
        severity_frame.pack(fill=tk.X, pady=5)

        ctk.CTkLabel(
            severity_frame,
            text="Niveau:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.LEFT, padx=10)

        self.severity_var = tk.StringVar(value="All")
        severities = ["All", "Error", "Warning", "Information"]

        for severity in severities:
            ctk.CTkRadioButton(
                severity_frame,
                text=severity,
                variable=self.severity_var,
                value=severity,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.TEXT_SECONDARY
            ).pack(side=tk.LEFT, padx=10)

        # Période
        period_frame = ctk.CTkFrame(filters_frame, fg_color="transparent")
        period_frame.pack(fill=tk.X, pady=5)

        ctk.CTkLabel(
            period_frame,
            text="Période:",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(side=tk.LEFT, padx=10)

        self.period_var = tk.StringVar(value="24h")
        periods = ["1h", "24h", "7j", "30j"]

        for period in periods:
            ctk.CTkRadioButton(
                period_frame,
                text=period,
                variable=self.period_var,
                value=period,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.TEXT_SECONDARY
            ).pack(side=tk.LEFT, padx=10)

        # Bouton appliquer filtres
        ModernButton(
            filters_frame,
            text="Appliquer les filtres",
            variant="filled",
            size="sm",
            command=self._apply_filters
        ).pack(pady=10)

    def _create_quick_actions(self, parent):
        """Actions rapides"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = ctk.CTkLabel(
            card,
            text=" Actions Rapides",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(fill=tk.X, padx=20, pady=(15, 10))

        # Boutons
        actions_frame = ctk.CTkFrame(card, fg_color="transparent")
        actions_frame.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Ligne 1
        row1 = ctk.CTkFrame(actions_frame, fg_color="transparent")
        row1.pack(fill=tk.X, pady=5)

        ModernButton(
            row1,
            text=" Ouvrir Observateur d'événements",
            variant="outlined",
            size="md",
            command=self._open_event_viewer
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row1,
            text=" Erreurs critiques (24h)",
            variant="outlined",
            size="md",
            command=lambda: self._show_critical_errors()
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Ligne 2
        row2 = ctk.CTkFrame(actions_frame, fg_color="transparent")
        row2.pack(fill=tk.X, pady=5)

        ModernButton(
            row2,
            text=" Avertissements (24h)",
            variant="outlined",
            size="md",
            command=lambda: self._show_warnings()
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ModernButton(
            row2,
            text=" Nettoyer logs anciens",
            variant="outlined",
            size="md",
            command=self._clean_old_logs
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    def _create_logs_display(self, parent):
        """Zone d'affichage des logs"""
        card = ModernCard(parent)
        card.pack(fill=tk.BOTH, expand=True, pady=10)

        # Header avec boutons de redimensionnement
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill=tk.X, padx=20, pady=(15, 10))

        title = ctk.CTkLabel(
            header_frame,
            text=" Journaux",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        )
        title.pack(side=tk.LEFT)

        # Boutons de taille
        size_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        size_frame.pack(side=tk.RIGHT)

        ctk.CTkButton(
            size_frame,
            text="▼",
            width=30,
            height=20,
            font=(DesignTokens.FONT_FAMILY, 12),
            command=lambda: self._resize_windows_logs(-100),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            size_frame,
            text="▲",
            width=30,
            height=20,
            font=(DesignTokens.FONT_FAMILY, 12),
            command=lambda: self._resize_windows_logs(100),
            fg_color=DesignTokens.BG_ELEVATED,
            hover_color=DesignTokens.BG_HOVER
        ).pack(side=tk.LEFT, padx=2)

        # Zone de texte avec scroll - CORRECTION: bg transparent pour le frame parent
        text_frame = ctk.CTkFrame(card, fg_color="transparent")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        logger.debug("PageLogs", "Création Text widget pour logs Windows",
                    bg="#1e1e1e", fg="#00ff00")

        # Scrollbar
        scrollbar = ctk.CTkScrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Hauteur par défaut (initialiser si pas déjà fait)
        if not hasattr(self, 'windows_logs_height'):
            self.windows_logs_height = 500

        self.logs_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            bg="#000000",  # Fond noir
            fg="#00FF00",  # Vert Matrix
            font=("Consolas", 10),
            relief=tk.FLAT,
            padx=15,
            pady=15,
            insertbackground="#00FF00",
            yscrollcommand=scrollbar.set,
            height=self.windows_logs_height
        )
        self.logs_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.configure(command=self.logs_text.yview)

        logger.debug("PageLogs", "Text widget logs Windows créé",
                    actual_bg=self.logs_text.cget("bg"),
                    actual_fg=self.logs_text.cget("fg"))

        # Message initial
        self.logs_text.insert("1.0", "Cliquez sur 'Appliquer les filtres' pour afficher les journaux...\n\n")
        self.logs_text.insert("end", "Ou utilisez les actions rapides ci-dessus.")
        self.logs_text.config(state=tk.DISABLED)
        logger.debug("PageLogs", "Message initial inséré dans logs Windows")

    def _open_event_viewer(self):
        """Ouvrir l'Observateur d'événements Windows"""
        try:
            subprocess.Popen("eventvwr.msc", shell=True)
            messagebox.showinfo(
                "Observateur d'événements",
                "L'Observateur d'événements Windows a été lancé."
            )
        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible d'ouvrir l'Observateur d'événements:\n\n{str(e)}"
            )

    def _apply_filters(self):
        """Appliquer les filtres et afficher les logs"""
        if not WIN32_AVAILABLE:
            messagebox.showerror(
                "Erreur",
                "Le module pywin32 n'est pas installé.\n\n"
                "Installation: pip install pywin32"
            )
            return

        try:
            log_type = self.log_type_var.get()
            severity = self.severity_var.get()
            period = self.period_var.get()

            # Calculer la date de début selon la période
            now = datetime.now()
            if period == "1h":
                start_time = now - timedelta(hours=1)
            elif period == "24h":
                start_time = now - timedelta(days=1)
            elif period == "7j":
                start_time = now - timedelta(days=7)
            else:  # 30j
                start_time = now - timedelta(days=30)

            # Lire les événements
            events = self._read_event_log(log_type, severity, start_time)

            # Afficher
            self.logs_text.config(state=tk.NORMAL)
            self.logs_text.delete("1.0", tk.END)

            if events:
                self.logs_text.insert("1.0", f"=== Journal: {log_type} | Niveau: {severity} | Période: {period} ===\n\n")
                self.logs_text.insert("end", f"Nombre d'événements: {len(events)}\n")
                self.logs_text.insert("end", "=" * 80 + "\n\n")

                for event in events[:100]:  # Limiter à 100 événements
                    self.logs_text.insert("end", event + "\n")

                if len(events) > 100:
                    self.logs_text.insert("end", f"\n... et {len(events) - 100} autres événements (utilisez 'Exporter' pour voir tous)")
            else:
                self.logs_text.insert("1.0", "Aucun événement trouvé pour ces critères.")

            self.logs_text.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror(
                "Erreur",
                f"Impossible de lire les journaux:\n\n{str(e)}"
            )

    def _read_event_log(self, log_type, severity, start_time):
        """Lire les événements du journal Windows"""
        events = []

        try:
            hand = win32evtlog.OpenEventLog(None, log_type)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

            total = 0
            while True:
                event_list = win32evtlog.ReadEventLog(hand, flags, 0)
                if not event_list:
                    break

                for event in event_list:
                    # Filtrer par date
                    event_time = event.TimeGenerated
                    if event_time < start_time:
                        win32evtlog.CloseEventLog(hand)
                        return events

                    # Filtrer par sévérité
                    event_type = event.EventType
                    type_str = self._get_event_type_string(event_type)

                    if severity != "All" and type_str != severity:
                        continue

                    # Formater l'événement
                    event_str = self._format_event(event, type_str)
                    events.append(event_str)

                    total += 1
                    if total >= 500:  # Limiter pour performance
                        break

                if total >= 500:
                    break

            win32evtlog.CloseEventLog(hand)

        except Exception as e:
            print(f"Erreur lecture event log: {e}")

        return events

    def _get_event_type_string(self, event_type):
        """Convertir le type d'événement en string"""
        if event_type == win32con.EVENTLOG_ERROR_TYPE:
            return "Error"
        elif event_type == win32con.EVENTLOG_WARNING_TYPE:
            return "Warning"
        elif event_type == win32con.EVENTLOG_INFORMATION_TYPE:
            return "Information"
        elif event_type == win32con.EVENTLOG_AUDIT_SUCCESS:
            return "Audit Success"
        elif event_type == win32con.EVENTLOG_AUDIT_FAILURE:
            return "Audit Failure"
        else:
            return "Unknown"

    def _format_event(self, event, type_str):
        """Formater un événement pour l'affichage"""
        time_str = event.TimeGenerated.strftime("%Y-%m-%d %H:%M:%S")
        source = event.SourceName if hasattr(event, 'SourceName') else "Unknown"
        event_id = event.EventID & 0xFFFF  # Masquer les bits hauts

        # Icône selon le type
        if type_str == "Error":
            icon = ""
        elif type_str == "Warning":
            icon = ""
        else:
            icon = "ℹ"

        # Message - Essayer plusieurs méthodes
        msg = None
        try:
            # Méthode 1: SafeFormatMessage
            msg = win32evtlogutil.SafeFormatMessage(event, event.SourceName)
            if msg and msg.strip():
                pass  # Message récupéré avec succès
            else:
                msg = None
        except:
            msg = None

        # Méthode 2: StringInserts (données brutes)
        if not msg:
            try:
                if hasattr(event, 'StringInserts') and event.StringInserts:
                    msg = " | ".join([str(s) for s in event.StringInserts if s])
            except:
                pass

        # Méthode 3: Data (fallback)
        if not msg:
            try:
                if hasattr(event, 'Data') and event.Data:
                    msg = f"Data: {event.Data[:100]}"
            except:
                pass

        # Fallback final
        if not msg or not msg.strip():
            msg = f"Event ID {event_id} - Catégorie: {event.EventCategory if hasattr(event, 'EventCategory') else 'N/A'}"

        # Limiter la longueur du message
        if len(msg) > 300:
            msg = msg[:300] + "..."

        return f"{icon} [{time_str}] {type_str} - {source} (ID: {event_id})\n    {msg}\n"

    def _show_critical_errors(self):
        """Afficher les erreurs critiques des dernières 24h"""
        self.log_type_var.set("System")
        self.severity_var.set("Error")
        self.period_var.set("24h")
        self._apply_filters()

    def _show_warnings(self):
        """Afficher les avertissements des dernières 24h"""
        self.log_type_var.set("System")
        self.severity_var.set("Warning")
        self.period_var.set("24h")
        self._apply_filters()

    def _clean_old_logs(self):
        """Nettoyer les logs anciens (nécessite admin)"""
        response = messagebox.askyesnocancel(
            "Nettoyer les logs",
            "Cette action nécessite des privilèges administrateur.\n\n"
            "Voulez-vous:\n"
            "- Oui: Ouvrir l'Observateur d'événements pour nettoyer manuellement\n"
            "- Non: Annuler",
            icon='warning'
        )

        if response:
            self._open_event_viewer()
            messagebox.showinfo(
                "Instructions",
                "Dans l'Observateur d'événements:\n\n"
                "1. Clic droit sur le journal (System, Application, etc.)\n"
                "2. Sélectionnez 'Effacer le journal...'\n"
                "3. Choisissez si vous voulez sauvegarder avant d'effacer"
            )

    def _refresh_logs(self):
        """Rafraîchir l'affichage"""
        self._apply_filters()

    def _export_logs(self):
        """Exporter les logs vers un fichier texte"""
        try:
            if not WIN32_AVAILABLE:
                messagebox.showerror(
                    "Module manquant",
                    "Le module win32evtlog n'est pas disponible.\n\n"
                    "Installez-le avec: pip install pywin32"
                )
                return

            # Demander l'emplacement du fichier
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
                initialfile=f"logs_windows_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )

            if not filename:
                return

            # Récupérer les filtres actuels
            log_type = self.log_type_var.get()
            severity = self.severity_var.get()
            period = self.period_var.get()

            # Calculer la date de début selon la période
            now = datetime.now()
            if period == "1h":
                start_time = now - timedelta(hours=1)
            elif period == "24h":
                start_time = now - timedelta(hours=24)
            elif period == "7d":
                start_time = now - timedelta(days=7)
            else:  # 30d
                start_time = now - timedelta(days=30)

            # Lire tous les événements (sans limite)
            events = self._read_event_log_full(log_type, severity, start_time)

            # Écrire dans le fichier
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Export des journaux Windows - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
                f.write(f"Journal: {log_type}\n")
                f.write(f"Niveau: {severity}\n")
                f.write(f"Période: {period}\n")
                f.write(f"Nombre d'événements: {len(events)}\n")
                f.write("=" * 80 + "\n\n")

                for event in events:
                    f.write(event + "\n")

            messagebox.showinfo(
                "Export réussi",
                f"Les logs ont été exportés vers:\n\n{filename}\n\n"
                f"Nombre d'événements: {len(events)}"
            )

        except Exception as e:
            messagebox.showerror(
                "Erreur d'export",
                f"Impossible d'exporter les logs:\n\n{str(e)}"
            )

    def _read_event_log_full(self, log_type, severity, start_time):
        """Lire TOUS les événements du journal Windows sans limite"""
        events = []

        try:
            hand = win32evtlog.OpenEventLog(None, log_type)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

            while True:
                event_list = win32evtlog.ReadEventLog(hand, flags, 0)
                if not event_list:
                    break

                for event in event_list:
                    # Filtrer par date
                    event_time = event.TimeGenerated
                    if event_time < start_time:
                        win32evtlog.CloseEventLog(hand)
                        return events

                    # Filtrer par sévérité
                    event_type = event.EventType
                    type_str = self._get_event_type_string(event_type)

                    if severity != "All" and type_str != severity:
                        continue

                    # Formater l'événement
                    event_str = self._format_event(event, type_str)
                    events.append(event_str)

            win32evtlog.CloseEventLog(hand)

        except Exception as e:
            print(f"Erreur lecture event log: {e}")

        return events

    def _resize_app_logs(self, delta):
        """Redimensionner la zone de logs application"""
        self.app_logs_height = max(200, min(1000, self.app_logs_height + delta))
        if hasattr(self, 'app_logs_text'):
            self.app_logs_text.configure(height=self.app_logs_height)

    def _resize_windows_logs(self, delta):
        """Redimensionner la zone de logs Windows"""
        self.windows_logs_height = max(200, min(1000, self.windows_logs_height + delta))
        if hasattr(self, 'logs_text'):
            self.logs_text.configure(height=self.windows_logs_height)

    def _bind_scroll_events(self, widget):
        """Bloquer la propagation du scroll au parent"""
        def on_mouse_wheel(event):
            # Scroll uniquement le widget sous le curseur
            try:
                widget.yview_scroll(-1 * int(event.delta / 120), "units")
            except:
                pass
            return "break"  # Empêche la propagation

        widget.bind("<MouseWheel>", on_mouse_wheel)

        # Bind pour tous les enfants
        def bind_children(w):
            for child in w.winfo_children():
                child.bind("<Enter>", lambda e, wg=widget: wg.bind("<MouseWheel>", on_mouse_wheel))
                child.bind("<Leave>", lambda e, wg=widget: wg.unbind("<MouseWheel>"))
                bind_children(child)

        bind_children(widget)
