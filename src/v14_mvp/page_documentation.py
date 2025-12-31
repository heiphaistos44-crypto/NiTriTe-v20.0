#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Documentation & Aide - NiTriTe V20
Guides, tutoriels, FAQ et changelog
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import webbrowser
from pathlib import Path
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader


class DocumentationPage(ctk.CTkFrame):
    """Page Documentation & Aide"""

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

        title_frame = SectionHeader(container, text="📚 Documentation & Aide")
        title_frame.pack(side=tk.LEFT)

        subtitle = ctk.CTkLabel(
            container,
            text="Guides • Tutoriels • FAQ • Support",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        )
        subtitle.pack(side=tk.RIGHT)

    def _create_content(self):
        """Contenu scrollable"""
        scroll = ctk.CTkScrollableFrame(self, fg_color=DesignTokens.BG_PRIMARY)
        scroll.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Section Guides d'utilisation
        self._create_guides_section(scroll)

        # Section Tutoriels Windows
        self._create_tutorials_section(scroll)

        # Section FAQ
        self._create_faq_section(scroll)

        # Section Changelog
        self._create_changelog_section(scroll)

    def _create_guides_section(self, parent):
        """Section guides d'utilisation NiTriTe"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="📖 Guides d'Utilisation NiTriTe")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Apprenez à utiliser toutes les fonctionnalités de NiTriTe",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Liste des guides
        guides = [
            ("🚀 Guide de démarrage rapide", "quickstart"),
            ("📱 Installation d'applications", "install_apps"),
            ("🔧 Outils de diagnostic", "diagnostic"),
            ("💾 Sauvegardes et restauration", "backup"),
            ("🛡️ Scanner antivirus", "antivirus"),
            ("⚙️ Optimisations système", "optimizations"),
        ]

        for guide_title, guide_id in guides:
            guide_frame = ctk.CTkFrame(content, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
            guide_frame.pack(fill=tk.X, pady=5)

            guide_container = ctk.CTkFrame(guide_frame, fg_color="transparent")
            guide_container.pack(fill=tk.X, padx=15, pady=10)

            label = ctk.CTkLabel(
                guide_container,
                text=guide_title,
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
                text_color=DesignTokens.TEXT_PRIMARY,
                anchor="w"
            )
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)

            ModernButton(
                guide_container,
                text="📄 Lire",
                variant="outlined",
                size="sm",
                command=lambda gid=guide_id: self._show_guide(gid)
            ).pack(side=tk.RIGHT)

    def _create_tutorials_section(self, parent):
        """Section tutoriels Windows"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="🎓 Tutoriels Windows")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Description
        desc = ctk.CTkLabel(
            content,
            text="Tutoriels pour maîtriser Windows et résoudre les problèmes courants",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w"
        )
        desc.pack(anchor="w", pady=(10, 15))

        # Boutons tutoriels
        tutorials_frame = ctk.CTkFrame(content, fg_color="transparent")
        tutorials_frame.pack(fill=tk.X)

        ModernButton(
            tutorials_frame,
            text="🪟 Optimiser Windows 11/10",
            variant="outlined",
            command=lambda: self._open_tutorial("optimize_windows")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tutorials_frame,
            text="🔧 Résoudre problèmes courants",
            variant="outlined",
            command=lambda: self._open_tutorial("troubleshoot")
        ).pack(side=tk.LEFT, padx=5, pady=5)

        ModernButton(
            tutorials_frame,
            text="🛡️ Sécuriser votre PC",
            variant="outlined",
            command=lambda: self._open_tutorial("security")
        ).pack(side=tk.LEFT, padx=5, pady=5)

    def _create_faq_section(self, parent):
        """Section FAQ"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="❓ Questions Fréquentes (FAQ)")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # FAQ items
        faqs = [
            ("Comment installer plusieurs applications en même temps ?", "Utilisez la page Master Install pour sélectionner et installer plusieurs applications d'un coup."),
            ("NiTriTe nécessite-t-il des droits administrateur ?", "Certaines fonctionnalités comme l'installation d'apps et les scans antivirus nécessitent des droits admin."),
            ("Où sont stockées mes sauvegardes ?", "Les sauvegardes sont stockées dans le dossier 'backups' à côté de l'exécutable NiTriTe."),
            ("Comment mettre à jour NiTriTe ?", "Consultez le site web officiel ou utilisez la fonction de mise à jour automatique (si disponible)."),
            ("Puis-je utiliser NiTriTe hors ligne ?", "Oui, mais certaines fonctions comme le téléchargement d'apps nécessitent une connexion internet."),
        ]

        for question, answer in faqs:
            self._create_faq_item(content, question, answer)

    def _create_faq_item(self, parent, question, answer):
        """Créer un élément FAQ"""
        faq_frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
        faq_frame.pack(fill=tk.X, pady=5)

        faq_container = ctk.CTkFrame(faq_frame, fg_color="transparent")
        faq_container.pack(fill=tk.X, padx=15, pady=12)

        # Question
        q_label = ctk.CTkLabel(
            faq_container,
            text=f"Q: {question}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY,
            anchor="w",
            wraplength=800
        )
        q_label.pack(anchor="w", pady=(0, 5))

        # Réponse
        a_label = ctk.CTkLabel(
            faq_container,
            text=f"R: {answer}",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY,
            anchor="w",
            wraplength=800
        )
        a_label.pack(anchor="w")

    def _create_changelog_section(self, parent):
        """Section changelog"""
        card = ModernCard(parent)
        card.pack(fill=tk.X, pady=10)

        title = SectionHeader(card, text="📋 Historique des Versions")
        title.pack(fill=tk.X)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill=tk.X, padx=20, pady=(0, 15))

        # Versions
        versions = [
            {
                "version": "V20.1.0",
                "date": "31 Décembre 2025",
                "changes": [
                    "Ajout catégorie Utilitaires Système Avancés",
                    "Ajout catégorie Documentation & Aide",
                    "Amélioration page Sauvegarde avec 6 nouvelles options",
                    "Correction bouton Installer dans Applications",
                    "Correction affichage catégories Scan Virus"
                ]
            },
            {
                "version": "V20.0.0",
                "date": "28 Décembre 2025",
                "changes": [
                    "Refonte complète de l'interface",
                    "Système d'icônes colorées",
                    "Intégration serveurs MCP",
                    "Amélioration performances",
                    "Ajout de 170+ scripts Windows"
                ]
            }
        ]

        for ver in versions:
            self._create_version_card(content, ver)

    def _create_version_card(self, parent, version_info):
        """Créer une carte de version"""
        ver_frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
        ver_frame.pack(fill=tk.X, pady=5)

        ver_container = ctk.CTkFrame(ver_frame, fg_color="transparent")
        ver_container.pack(fill=tk.X, padx=15, pady=12)

        # Header version
        header = ctk.CTkFrame(ver_container, fg_color="transparent")
        header.pack(fill=tk.X)

        version_label = ctk.CTkLabel(
            header,
            text=version_info["version"],
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_LG, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY
        )
        version_label.pack(side=tk.LEFT)

        date_label = ctk.CTkLabel(
            header,
            text=version_info["date"],
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_TERTIARY
        )
        date_label.pack(side=tk.RIGHT)

        # Changements
        changes_frame = ctk.CTkFrame(ver_container, fg_color="transparent")
        changes_frame.pack(fill=tk.X, pady=(10, 0))

        for change in version_info["changes"]:
            change_label = ctk.CTkLabel(
                changes_frame,
                text=f"• {change}",
                font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            )
            change_label.pack(anchor="w", pady=2)

    # === MÉTHODES D'ACTION ===

    def _show_guide(self, guide_id):
        """Afficher un guide"""
        guides_content = {
            "quickstart": """GUIDE DE DÉMARRAGE RAPIDE

Bienvenue dans NiTriTe V20 !

1. NAVIGATION
   - Utilisez le menu latéral pour accéder aux différentes catégories
   - Chaque catégorie contient des outils spécialisés

2. INSTALLER DES APPLICATIONS
   - Allez dans 'Applications' ou 'Master Install'
   - Sélectionnez les applications désirées
   - Cliquez sur 'Installer' pour lancer l'installation

3. DIAGNOSTIC PC
   - La catégorie 'Diagnostic' contient tous les outils d'analyse
   - Lancez un scan pour vérifier l'état de votre PC

4. SAUVEGARDE
   - Créez régulièrement des sauvegardes dans la catégorie 'Sauvegarde'
   - Vous pouvez restaurer une sauvegarde à tout moment

5. SUPPORT
   - Consultez la FAQ pour les questions courantes
   - Visitez la documentation pour plus d'informations""",

            "install_apps": """INSTALLATION D'APPLICATIONS

NiTriTe propose plusieurs façons d'installer des applications :

1. PAGE APPLICATIONS
   - Parcourez par catégorie
   - Cliquez sur 'Installer' pour installer une app
   - Cliquez sur 'Web' pour visiter le site officiel

2. MASTER INSTALL
   - Installez plusieurs applications en une seule fois
   - Sélectionnez vos applications préférées
   - Cliquez sur 'Lancer Installation'

3. APPS PORTABLE
   - Applications qui ne nécessitent pas d'installation
   - Prêtes à l'emploi immédiatement""",

            "diagnostic": """OUTILS DE DIAGNOSTIC

Utilisez les outils de diagnostic pour analyser votre PC :

1. INFORMATIONS SYSTÈME
   - CPU, RAM, stockage
   - Système d'exploitation
   - Carte graphique

2. TESTS DE PERFORMANCE
   - Benchmark CPU/GPU
   - Test vitesse disque
   - Test mémoire RAM

3. ANALYSE SANTÉ
   - État des disques durs
   - Température des composants
   - Programmes au démarrage""",

            "backup": """SAUVEGARDES ET RESTAURATION

Protégez vos données avec les sauvegardes :

1. CRÉER UNE SAUVEGARDE
   - Sélectionnez ce que vous voulez sauvegarder
   - Cliquez sur 'Créer Sauvegarde'
   - La sauvegarde est stockée dans le dossier 'backups'

2. RESTAURER UNE SAUVEGARDE
   - Sélectionnez une sauvegarde dans la liste
   - Cliquez sur 'Restaurer'
   - Suivez les instructions

3. OPTIONS DE SAUVEGARDE
   - Applications installées
   - Drivers système
   - Configuration réseau
   - Variables d'environnement
   - Et plus encore !""",

            "antivirus": """SCANNER ANTIVIRUS

Protégez votre PC contre les menaces :

1. TYPES DE SCAN
   - Scan rapide : 5-10 minutes
   - Scan complet : 1-2 heures
   - Scan personnalisé : fichier ou dossier

2. APRÈS UN SCAN
   - Les menaces sont classées en 3 catégories :
     • Quarantaine
     • À Supprimer
     • Faux Positifs

3. ACTIONS POSSIBLES
   - Mettre en quarantaine
   - Supprimer définitivement
   - Marquer comme faux positif""",

            "optimizations": """OPTIMISATIONS SYSTÈME

Améliorez les performances de votre PC :

1. NETTOYAGE
   - Fichiers temporaires
   - Cache système
   - Registre Windows

2. DÉMARRAGE
   - Désactiver programmes inutiles au démarrage
   - Réduire le temps de démarrage

3. PERFORMANCES
   - Défragmentation
   - Optimisation SSD
   - Gestion mémoire RAM"""
        }

        content = guides_content.get(guide_id, "Guide non disponible")

        # Créer fenêtre de guide
        guide_window = ctk.CTkToplevel(self)
        guide_window.title("Guide NiTriTe")
        guide_window.geometry("700x600")

        # Centrer
        guide_window.update_idletasks()
        x = (guide_window.winfo_screenwidth() // 2) - (700 // 2)
        y = (guide_window.winfo_screenheight() // 2) - (600 // 2)
        guide_window.geometry(f"700x600+{x}+{y}")

        # Contenu
        text_frame = ctk.CTkFrame(guide_window, fg_color=DesignTokens.BG_PRIMARY)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        text_widget = tk.Text(
            text_frame,
            wrap=tk.WORD,
            bg=DesignTokens.BG_ELEVATED,
            fg=DesignTokens.TEXT_PRIMARY,
            font=("Consolas", 11),
            relief=tk.FLAT,
            padx=20,
            pady=20
        )
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert("1.0", content)
        text_widget.configure(state="disabled")

    def _open_tutorial(self, tutorial_id):
        """Ouvrir un tutoriel externe"""
        tutorials = {
            "optimize_windows": "https://www.howtogeek.com/138188/how-to-make-windows-8-or-10-faster/",
            "troubleshoot": "https://support.microsoft.com/windows",
            "security": "https://www.microsoft.com/security/blog/"
        }

        if tutorial_id in tutorials:
            webbrowser.open(tutorials[tutorial_id])
            print(f"📚 Tutoriel ouvert: {tutorial_id}")
        else:
            messagebox.showinfo("Information", "Ce tutoriel sera bientôt disponible.")
