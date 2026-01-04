#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Statistiques & Rapports - NiTriTe V20
Affichage centralisé de tous les rapports générés (HTML, TXT, MD, JSON)
Vue d'ensemble des rapports de Diagnostic, Scan Total, Batterie, etc.
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os
import sys
import subprocess
import webbrowser
from datetime import datetime
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader, ModernStatsCard


class StatisticsReportsPage(ctk.CTkFrame):
    """Page Statistiques & Rapports - Centre de rapports système"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # Déterminer le dossier racine de l'application
        if getattr(sys, 'frozen', False):
            # Mode PyInstaller
            app_root = Path(sys.executable).parent
        else:
            # Mode développement
            app_root = Path(__file__).parent.parent.parent

        # Dossiers de rapports (chemins dynamiques)
        self.reports_folders = [
            Path.home() / "Documents" / "NiTriTe_Reports",
            app_root / "data" / "logs",
            app_root / "data" / "reports",
            Path.home() / "Downloads",  # Pour rapports PowerCfg, etc.
            Path("C:/Windows/Temp"),  # Rapports temporaires
        ]

        # Créer dossier principal si inexistant
        self.main_reports_folder = self.reports_folders[0]
        self.main_reports_folder.mkdir(parents=True, exist_ok=True)

        self.all_reports = []

        # Configurer grid
        self.grid_rowconfigure(0, weight=0)  # Header
        self.grid_rowconfigure(1, weight=0)  # Stats overview
        self.grid_rowconfigure(2, weight=1)  # Content scrollable
        self.grid_columnconfigure(0, weight=1)

        self._create_header()
        self._create_stats_overview()
        self._create_content()
        self._scan_reports()

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        # Titre
        SectionHeader(container, text="📊 Statistiques & Rapports Système").pack(side=tk.LEFT)

        # Boutons d'action
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)

        ModernButton(
            actions,
            text="🔄 Actualiser",
            variant="outlined",
            command=self._refresh_reports
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="📂 Ouvrir Dossier",
            variant="outlined",
            command=self._open_reports_folder
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            actions,
            text="🗑️ Nettoyer Anciens",
            variant="outlined",
            command=self._cleanup_old_reports
        ).pack(side=tk.LEFT, padx=5)

    def _create_stats_overview(self):
        """Section statistiques visuelles (aperçu rapide) - FIXE (ne scroll pas)"""
        stats_container = ModernCard(self)
        stats_container.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 5))

        SectionHeader(stats_container, text="📊 Aperçu Rapide").pack(pady=(8, 5), padx=15)

        # Grid 4 colonnes pour stats principales (compact)
        stats_grid = ctk.CTkFrame(stats_container, fg_color="transparent")
        stats_grid.pack(fill=tk.X, padx=15, pady=(0, 8))

        for i in range(4):
            stats_grid.grid_columnconfigure(i, weight=1, uniform="stats")

        # Créer les 4 cartes principales
        self.stat_total = ModernStatsCard(
            stats_grid,
            title="📁 Total",
            value="0",
            icon="📁",
            color=DesignTokens.ACCENT_PRIMARY
        )
        self.stat_total.grid(row=0, column=0, padx=5, sticky="ew")

        self.stat_recent = ModernStatsCard(
            stats_grid,
            title="🕐 Récents (7j)",
            value="0",
            icon="🕐",
            color="#10B981"
        )
        self.stat_recent.grid(row=0, column=1, padx=5, sticky="ew")

        self.stat_size = ModernStatsCard(
            stats_grid,
            title="💾 Espace",
            value="0 MB",
            icon="💾",
            color="#F59E0B"
        )
        self.stat_size.grid(row=0, column=2, padx=5, sticky="ew")

        self.stat_categories = ModernStatsCard(
            stats_grid,
            title="📂 Catégories",
            value="0",
            icon="📂",
            color="#8B5CF6"
        )
        self.stat_categories.grid(row=0, column=3, padx=5, sticky="ew")

        # Séparateur visuel (compact)
        separator = ctk.CTkFrame(stats_container, fg_color=DesignTokens.BG_SECONDARY, height=1)
        separator.pack(fill=tk.X, padx=30, pady=(5, 8))

        # Grid 5 colonnes pour types de fichiers (compact)
        SectionHeader(stats_container, text="📄 Répartition par Type").pack(pady=(3, 5), padx=15)

        types_grid = ctk.CTkFrame(stats_container, fg_color="transparent")
        types_grid.pack(fill=tk.X, padx=15, pady=(0, 10))

        for i in range(5):
            types_grid.grid_columnconfigure(i, weight=1, uniform="types")

        # 5 cartes de types
        self.stat_html = ModernStatsCard(
            types_grid,
            title="🌐 HTML",
            value="0",
            icon="🌐",
            color="#3B82F6"
        )
        self.stat_html.grid(row=0, column=0, padx=5, sticky="ew")

        self.stat_txt = ModernStatsCard(
            types_grid,
            title="📝 TXT",
            value="0",
            icon="📝",
            color="#14B8A6"
        )
        self.stat_txt.grid(row=0, column=1, padx=5, sticky="ew")

        self.stat_json = ModernStatsCard(
            types_grid,
            title="📋 JSON",
            value="0",
            icon="📋",
            color="#F59E0B"
        )
        self.stat_json.grid(row=0, column=2, padx=5, sticky="ew")

        self.stat_md = ModernStatsCard(
            types_grid,
            title="📄 Markdown",
            value="0",
            icon="📄",
            color="#A855F7"
        )
        self.stat_md.grid(row=0, column=3, padx=5, sticky="ew")

        self.stat_others = ModernStatsCard(
            types_grid,
            title="📦 Autres",
            value="0",
            icon="📦",
            color="#64748B"
        )
        self.stat_others.grid(row=0, column=4, padx=5, sticky="ew")

    def _create_content(self):
        """Contenu scrollable"""
        self.scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        self.scroll.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

        # Info
        info_card = ModernCard(self.scroll)
        info_card.pack(fill=tk.X, pady=10)

        info_text = ctk.CTkLabel(
            info_card,
            text="ℹ️ Cette page centralise tous les rapports système générés par NiTriTe.\n"
                 "Rapports de diagnostic, scan total, batterie, CrystalDiskInfo, etc.",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            justify="left"
        )
        info_text.pack(padx=20, pady=15)

        # Container pour les rapports (sera rempli par _scan_reports)
        self.reports_container = ctk.CTkFrame(self.scroll, fg_color="transparent")
        self.reports_container.pack(fill=tk.BOTH, expand=True)

    def _scan_reports(self):
        """Scanner tous les dossiers pour trouver les rapports"""
        self.all_reports = []

        # Extensions de rapports supportées
        report_extensions = ['.html', '.txt', '.md', '.json', '.log', '.xml']

        for folder in self.reports_folders:
            if not folder.exists():
                continue

            try:
                for file_path in folder.rglob('*'):
                    if file_path.is_file() and file_path.suffix.lower() in report_extensions:
                        # Filtrer les rapports pertinents
                        file_name_lower = file_path.name.lower()
                        if any(keyword in file_name_lower for keyword in [
                            'rapport', 'report', 'scan', 'diagnostic', 'battery', 'batterie',
                            'crystal', 'disk', 'nitrite', 'system', 'log', 'powercfg'
                        ]):
                            stat = file_path.stat()
                            self.all_reports.append({
                                'path': file_path,
                                'name': file_path.name,
                                'size': stat.st_size,
                                'modified': datetime.fromtimestamp(stat.st_mtime),
                                'type': file_path.suffix.upper()[1:]
                            })
            except Exception as e:
                print(f"Erreur scan dossier {folder}: {e}")

        # Trier par date (plus récent en premier)
        self.all_reports.sort(key=lambda x: x['modified'], reverse=True)

        # Mettre à jour les statistiques
        self._update_stats()

        # Afficher
        self._display_reports()

    def _update_stats(self):
        """Mettre à jour les cartes de statistiques"""
        if not hasattr(self, 'stat_total'):
            return  # Stats pas encore créées

        from datetime import timedelta

        # Calculer les statistiques principales
        total = len(self.all_reports)

        # Rapports récents (7 derniers jours)
        now = datetime.now()
        recent = sum(1 for r in self.all_reports if r['modified'] >= now - timedelta(days=7))

        # Taille totale
        total_size = sum(r['size'] for r in self.all_reports)

        # Nombre de catégories uniques (types de fichiers)
        categories = len(set(r['type'] for r in self.all_reports))

        # Compter par type
        type_counts = {}
        for r in self.all_reports:
            ext = r['type']
            type_counts[ext] = type_counts.get(ext, 0) + 1

        # Mettre à jour les cartes principales
        self.stat_total.update_value(total)
        self.stat_recent.update_value(recent)
        self.stat_size.update_value(self._format_size(total_size))
        self.stat_categories.update_value(categories)

        # Mettre à jour les cartes par type
        self.stat_html.update_value(type_counts.get('HTML', 0))
        self.stat_txt.update_value(type_counts.get('TXT', 0))
        self.stat_json.update_value(type_counts.get('JSON', 0))
        self.stat_md.update_value(type_counts.get('MD', 0))

        # Autres = tous les types sauf HTML, TXT, JSON, MD
        others = sum(count for ext, count in type_counts.items()
                    if ext not in ['HTML', 'TXT', 'JSON', 'MD'])
        self.stat_others.update_value(others)

    def _format_size(self, size_bytes):
        """Formater la taille en unité lisible"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

    def _display_reports(self):
        """Afficher les rapports trouvés"""
        # Nettoyer
        for widget in self.reports_container.winfo_children():
            widget.destroy()

        if not self.all_reports:
            # Aucun rapport
            no_reports = ModernCard(self.reports_container)
            no_reports.pack(fill=tk.X, pady=20)

            ctk.CTkLabel(
                no_reports,
                text="📭 Aucun rapport trouvé\n\nLancez des diagnostics ou scans pour générer des rapports",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_SECONDARY,
                justify="center"
            ).pack(pady=30)
            return

        # Statistiques globales
        stats_card = ModernCard(self.reports_container)
        stats_card.pack(fill=tk.X, pady=10)

        stats_title = SectionHeader(stats_card, text=f"📈 Statistiques - {len(self.all_reports)} rapports trouvés")
        stats_title.pack(pady=10)

        # Compter par type
        type_counts = {}
        total_size = 0
        for report in self.all_reports:
            type_counts[report['type']] = type_counts.get(report['type'], 0) + 1
            total_size += report['size']

        stats_frame = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_frame.pack(fill=tk.X, padx=20, pady=10)

        stats_text = f"📌 Rapports par type: "
        for rtype, count in sorted(type_counts.items()):
            stats_text += f"{rtype}({count})  "
        stats_text += f"\n💾 Taille totale: {self._format_size(total_size)}"

        ctk.CTkLabel(
            stats_frame,
            text=stats_text,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            justify="left"
        ).pack(anchor="w")

        # Liste des rapports
        reports_card = ModernCard(self.reports_container)
        reports_card.pack(fill=tk.BOTH, expand=True, pady=10)

        reports_title = SectionHeader(reports_card, text="📄 Liste des Rapports")
        reports_title.pack(pady=10)

        # Frame scrollable
        reports_scroll = ctk.CTkScrollableFrame(reports_card, fg_color=DesignTokens.BG_SECONDARY, height=500)
        reports_scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Afficher chaque rapport
        for i, report in enumerate(self.all_reports[:100]):  # Limiter à 100 pour performance
            self._create_report_item(reports_scroll, report, i+1)

        # Section logs catégorisés et redimensionnables
        self._create_categorized_logs()

    def _create_report_item(self, parent, report, num):
        """Créer un item de rapport"""
        item_frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_PRIMARY, corner_radius=8)
        item_frame.pack(fill=tk.X, pady=5, padx=5)

        # Numéro
        num_label = ctk.CTkLabel(
            item_frame,
            text=f"#{num}",
            font=(DesignTokens.FONT_FAMILY, 12, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY,
            width=50
        )
        num_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Info rapport
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

        # Icône selon type
        type_icons = {
            'HTML': '🌐',
            'TXT': '📝',
            'MD': '📄',
            'JSON': '🔧',
            'LOG': '📋',
            'XML': '📑'
        }
        icon = type_icons.get(report['type'], '📄')

        ctk.CTkLabel(
            info_frame,
            text=f"{icon} {report['name']}",
            font=(DesignTokens.FONT_FAMILY, 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY,
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            info_frame,
            text=f"Type: {report['type']}  •  Taille: {self._format_size(report['size'])}  •  Modifié: {report['modified'].strftime('%d/%m/%Y %H:%M')}",
            font=(DesignTokens.FONT_FAMILY, 11),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        ).pack(anchor="w", pady=(3, 0))

        # Boutons d'action
        actions_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        actions_frame.pack(side=tk.RIGHT, padx=10)

        ModernButton(
            actions_frame,
            text="📖 Ouvrir",
            variant="filled",
            width=100,
            command=lambda p=report['path']: self._open_report(p)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            actions_frame,
            text="📂 Dossier",
            variant="outlined",
            width=100,
            command=lambda p=report['path']: self._open_report_folder(p)
        ).pack(side=tk.LEFT, padx=3)

        ModernButton(
            actions_frame,
            text="🗑️",
            variant="outlined",
            width=50,
            command=lambda p=report['path']: self._delete_report(p)
        ).pack(side=tk.LEFT, padx=3)

    def _format_size(self, size_bytes):
        """Formater la taille en KB/MB"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"

    def _open_report(self, file_path):
        """Ouvrir un rapport"""
        try:
            if file_path.suffix.lower() == '.html':
                webbrowser.open(str(file_path))
            else:
                os.startfile(str(file_path))
            print(f"✓ Rapport ouvert: {file_path.name}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le rapport:\n\n{str(e)}")

    def _open_report_folder(self, file_path):
        """Ouvrir le dossier contenant le rapport"""
        try:
            subprocess.run(['explorer', '/select,', str(file_path)])
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n\n{str(e)}")

    def _delete_report(self, file_path):
        """Supprimer un rapport"""
        response = messagebox.askyesno(
            "Supprimer le rapport",
            f"Êtes-vous sûr de vouloir supprimer ce rapport ?\n\n{file_path.name}"
        )

        if response:
            try:
                file_path.unlink()
                messagebox.showinfo("Succès", "Rapport supprimé avec succès")
                self._refresh_reports()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de supprimer le rapport:\n\n{str(e)}")

    def _refresh_reports(self):
        """Rafraîchir la liste des rapports"""
        self._scan_reports()

    def _open_reports_folder(self):
        """Ouvrir le dossier principal des rapports"""
        try:
            os.startfile(str(self.main_reports_folder))
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le dossier:\n\n{str(e)}")

    def _cleanup_old_reports(self):
        """Nettoyer les anciens rapports (>30 jours)"""
        response = messagebox.askyesno(
            "Nettoyer les Anciens Rapports",
            "Cette opération va supprimer tous les rapports de plus de 30 jours.\n\n"
            "Continuer ?"
        )

        if not response:
            return

        deleted_count = 0
        cutoff_date = datetime.now().timestamp() - (30 * 24 * 60 * 60)  # 30 jours

        for report in self.all_reports:
            if report['modified'].timestamp() < cutoff_date:
                try:
                    report['path'].unlink()
                    deleted_count += 1
                except Exception as e:
                    print(f"Erreur suppression {report['name']}: {e}")

        messagebox.showinfo(
            "Nettoyage Terminé",
            f"✅ {deleted_count} rapport(s) ancien(s) supprimé(s)"
        )

        self._refresh_reports()

    def _create_categorized_logs(self):
        """Section logs catégorisés et redimensionnables"""
        logs_container = ModernCard(self.scroll)
        logs_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Header avec titre et boutons de redimensionnement
        header_frame = ctk.CTkFrame(logs_container, fg_color="transparent")
        header_frame.pack(fill=tk.X, padx=20, pady=(15, 10))

        SectionHeader(header_frame, text="📋 Logs Détaillés par Catégorie").pack(side=tk.LEFT)

        # Boutons de redimensionnement
        resize_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        resize_frame.pack(side=tk.RIGHT)

        ctk.CTkButton(
            resize_frame,
            text="▲",
            width=40,
            height=30,
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER,
            command=lambda: self._resize_logs(100)
        ).pack(side=tk.LEFT, padx=2)

        ctk.CTkButton(
            resize_frame,
            text="▼",
            width=40,
            height=30,
            font=(DesignTokens.FONT_FAMILY, 16, "bold"),
            fg_color=DesignTokens.ACCENT_PRIMARY,
            hover_color=DesignTokens.ACCENT_HOVER,
            command=lambda: self._resize_logs(-100)
        ).pack(side=tk.LEFT, padx=2)

        # Boutons de catégories
        categories_frame = ctk.CTkFrame(logs_container, fg_color="transparent")
        categories_frame.pack(fill=tk.X, padx=20, pady=(5, 10))

        self.current_log_category = "diagnostic"
        self.category_buttons = {}

        categories = [
            ("diagnostic", "🔍 Diagnostic", "#3B82F6"),
            ("application", "📱 Application", "#10B981"),
            ("system", "⚙️ Système", "#F59E0B"),
            ("security", "🔒 Sécurité", "#EF4444"),
            ("performance", "⚡ Performance", "#8B5CF6")
        ]

        for i, (cat_id, cat_label, cat_color) in enumerate(categories):
            btn = ctk.CTkButton(
                categories_frame,
                text=cat_label,
                font=(DesignTokens.FONT_FAMILY, 14, "bold"),
                fg_color=cat_color if cat_id == "diagnostic" else DesignTokens.BG_TERTIARY,
                hover_color=cat_color,
                command=lambda c=cat_id, col=cat_color: self._switch_log_category(c, col)
            )
            btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
            self.category_buttons[cat_id] = {"button": btn, "color": cat_color}

        # Zone de texte redimensionnable
        self.logs_text_categorized = ctk.CTkTextbox(
            logs_container,
            font=(DesignTokens.FONT_MONO, 11),
            fg_color=DesignTokens.BG_SECONDARY,
            text_color=DesignTokens.TEXT_PRIMARY,
            height=400,
            wrap=tk.WORD
        )
        self.logs_text_categorized.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))

        # Charger la catégorie par défaut
        self._load_diagnostic_logs()

    def _resize_logs(self, delta):
        """Redimensionner la zone de logs"""
        if hasattr(self, 'logs_text_categorized'):
            current_height = self.logs_text_categorized.cget("height")
            new_height = max(200, min(800, current_height + delta))
            self.logs_text_categorized.configure(height=new_height)

    def _switch_log_category(self, category, color):
        """Changer de catégorie de logs"""
        # Mettre à jour l'apparence des boutons
        for cat_id, btn_data in self.category_buttons.items():
            if cat_id == category:
                btn_data["button"].configure(fg_color=btn_data["color"])
            else:
                btn_data["button"].configure(fg_color=DesignTokens.BG_TERTIARY)

        self.current_log_category = category

        # Charger les logs de la catégorie
        if category == "diagnostic":
            self._load_diagnostic_logs()
        elif category == "application":
            self._load_application_logs()
        elif category == "system":
            self._load_system_logs()
        elif category == "security":
            self._load_security_logs()
        elif category == "performance":
            self._load_performance_logs()

    def _load_diagnostic_logs(self):
        """Charger les logs de diagnostic"""
        if not hasattr(self, 'logs_text_categorized'):
            return

        self.logs_text_categorized.delete("1.0", tk.END)
        self.logs_text_categorized.insert("1.0", "=== 🔍 LOGS DIAGNOSTIC ===\n\n")

        # Filtrer les rapports de diagnostic
        diagnostic_reports = [
            r for r in self.all_reports
            if any(keyword in r['name'].lower() for keyword in ['diagnostic', 'scan', 'test', 'check'])
        ]

        if diagnostic_reports:
            self.logs_text_categorized.insert("end", f"Nombre de rapports: {len(diagnostic_reports)}\n\n")
            for report in diagnostic_reports[:50]:  # Limiter à 50
                self.logs_text_categorized.insert(
                    "end",
                    f"📄 {report['name']}\n"
                    f"   📅 Date: {report['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"   📁 Catégorie: {report.get('category', 'N/A')}\n"
                    f"   💾 Taille: {self._format_size(report['size'])}\n\n"
                )
        else:
            self.logs_text_categorized.insert("end", "Aucun rapport de diagnostic trouvé.\n")

    def _load_application_logs(self):
        """Charger les logs d'application"""
        if not hasattr(self, 'logs_text_categorized'):
            return

        self.logs_text_categorized.delete("1.0", tk.END)
        self.logs_text_categorized.insert("1.0", "=== 📱 LOGS APPLICATION ===\n\n")

        # Filtrer les rapports d'application
        app_reports = [
            r for r in self.all_reports
            if any(keyword in r['name'].lower() for keyword in ['app', 'install', 'winget', 'portable'])
        ]

        if app_reports:
            self.logs_text_categorized.insert("end", f"Nombre de rapports: {len(app_reports)}\n\n")
            for report in app_reports[:50]:
                self.logs_text_categorized.insert(
                    "end",
                    f"📄 {report['name']}\n"
                    f"   📅 Date: {report['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"   📁 Catégorie: {report.get('category', 'N/A')}\n"
                    f"   💾 Taille: {self._format_size(report['size'])}\n\n"
                )
        else:
            self.logs_text_categorized.insert("end", "Aucun rapport d'application trouvé.\n")

    def _load_system_logs(self):
        """Charger les logs système"""
        if not hasattr(self, 'logs_text_categorized'):
            return

        self.logs_text_categorized.delete("1.0", tk.END)
        self.logs_text_categorized.insert("1.0", "=== ⚙️ LOGS SYSTÈME ===\n\n")

        # Filtrer les rapports système
        system_reports = [
            r for r in self.all_reports
            if any(keyword in r['name'].lower() for keyword in ['system', 'hardware', 'driver', 'device'])
        ]

        if system_reports:
            self.logs_text_categorized.insert("end", f"Nombre de rapports: {len(system_reports)}\n\n")
            for report in system_reports[:50]:
                self.logs_text_categorized.insert(
                    "end",
                    f"📄 {report['name']}\n"
                    f"   📅 Date: {report['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"   📁 Catégorie: {report.get('category', 'N/A')}\n"
                    f"   💾 Taille: {self._format_size(report['size'])}\n\n"
                )
        else:
            self.logs_text_categorized.insert("end", "Aucun rapport système trouvé.\n")

    def _load_security_logs(self):
        """Charger les logs de sécurité"""
        if not hasattr(self, 'logs_text_categorized'):
            return

        self.logs_text_categorized.delete("1.0", tk.END)
        self.logs_text_categorized.insert("1.0", "=== 🔒 LOGS SÉCURITÉ ===\n\n")

        # Filtrer les rapports de sécurité
        security_reports = [
            r for r in self.all_reports
            if any(keyword in r['name'].lower() for keyword in ['security', 'virus', 'scan', 'malware', 'threat'])
        ]

        if security_reports:
            self.logs_text_categorized.insert("end", f"Nombre de rapports: {len(security_reports)}\n\n")
            for report in security_reports[:50]:
                self.logs_text_categorized.insert(
                    "end",
                    f"📄 {report['name']}\n"
                    f"   📅 Date: {report['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"   📁 Catégorie: {report.get('category', 'N/A')}\n"
                    f"   💾 Taille: {self._format_size(report['size'])}\n\n"
                )
        else:
            self.logs_text_categorized.insert("end", "Aucun rapport de sécurité trouvé.\n")

    def _load_performance_logs(self):
        """Charger les logs de performance"""
        if not hasattr(self, 'logs_text_categorized'):
            return

        self.logs_text_categorized.delete("1.0", tk.END)
        self.logs_text_categorized.insert("1.0", "=== ⚡ LOGS PERFORMANCE ===\n\n")

        # Filtrer les rapports de performance
        perf_reports = [
            r for r in self.all_reports
            if any(keyword in r['name'].lower() for keyword in ['perf', 'speed', 'benchmark', 'monitor'])
        ]

        if perf_reports:
            self.logs_text_categorized.insert("end", f"Nombre de rapports: {len(perf_reports)}\n\n")
            for report in perf_reports[:50]:
                self.logs_text_categorized.insert(
                    "end",
                    f"📄 {report['name']}\n"
                    f"   📅 Date: {report['modified'].strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"   📁 Catégorie: {report.get('category', 'N/A')}\n"
                    f"   💾 Taille: {self._format_size(report['size'])}\n\n"
                )
        else:
            self.logs_text_categorized.insert("end", "Aucun rapport de performance trouvé.\n")
