#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Base de Connaissances - NiTriTe V20
Guides complets: Windows, Linux, macOS, NiTriTe, Documentation technique
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton, SectionHeader
from v14_mvp.knowledge_data_complete import COMPLETE_GUIDES_DATA


class KnowledgeBasePage(ctk.CTkFrame):
    """Page Base de Connaissances - Centre de documentation complète"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        self.current_guide = "nitrite_intro"
        self.expanded_categories = {"NiTriTe"}  # Catégorie NiTriTe ouverte par défaut

        # Configurer grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)  # Sidebar
        self.grid_columnconfigure(1, weight=1)  # Content

        self._create_header()
        self._create_sidebar()
        self._create_content()

        # Charger guide par défaut
        self._load_guide("nitrite_intro")

    def _create_header(self):
        """Header de la page"""
        header = ModernCard(self)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

        container = ctk.CTkFrame(header, fg_color="transparent")
        container.pack(fill=tk.X, padx=20, pady=15)

        SectionHeader(container, text="📚 Base de Connaissances - Documentation Complète").pack(side=tk.LEFT)

        # Bouton recherche (futur)
        actions = ctk.CTkFrame(container, fg_color="transparent")
        actions.pack(side=tk.RIGHT)

        ModernButton(
            actions,
            text="🔍 Rechercher",
            variant="outlined",
            command=self._search_guides
        ).pack(side=tk.LEFT, padx=5)

    def _create_sidebar(self):
        """Sidebar avec navigation des guides"""
        sidebar = ctk.CTkScrollableFrame(
            self,
            fg_color=DesignTokens.BG_SECONDARY,
            width=280
        )
        sidebar.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=10)

        # Structure des guides
        self.guides_structure = {
            "NiTriTe": [
                ("nitrite_intro", "🏠 Introduction à NiTriTe"),
                ("nitrite_install", "📥 Installation & Configuration"),
                ("nitrite_features", "⚡ Fonctionnalités Principales"),
                ("nitrite_masterinstall", "🎯 Master Install Mode"),
                ("nitrite_portable", "📦 Applications Portables"),
                ("nitrite_drivers", "🔧 Gestion des Pilotes"),
                ("nitrite_troubleshoot", "🔍 Dépannage NiTriTe"),
            ],
            "Windows 11": [
                ("w11_intro", "🪟 Introduction Windows 11"),
                ("w11_install", "💿 Installation & Configuration"),
                ("w11_optimize", "⚡ Optimisation Performance"),
                ("w11_privacy", "🔒 Confidentialité & Sécurité"),
                ("w11_troubleshoot", "🔧 Dépannage Windows 11"),
            ],
            "Windows 10": [
                ("w10_intro", "🪟 Introduction Windows 10"),
                ("w10_install", "💿 Installation & Activation"),
                ("w10_optimize", "⚡ Optimisation & Tweaks"),
                ("w10_services", "⚙️ Services & Démarrage"),
                ("w10_troubleshoot", "🔧 Résolution de Problèmes"),
            ],
            "Windows 8/8.1": [
                ("w8_intro", "🪟 Introduction Windows 8/8.1"),
                ("w8_install", "💿 Installation"),
                ("w8_optimize", "⚡ Optimisation"),
            ],
            "Windows 7": [
                ("w7_intro", "🪟 Introduction Windows 7"),
                ("w7_install", "💿 Installation & Drivers"),
                ("w7_optimize", "⚡ Optimisation & Tweaks"),
                ("w7_legacy", "📜 Support & Mises à jour"),
            ],
            "Windows Vista": [
                ("vista_intro", "🪟 Windows Vista - Guide"),
                ("vista_optimize", "⚡ Optimisation Vista"),
            ],
            "Windows XP": [
                ("xp_intro", "🪟 Windows XP - Guide Complet"),
                ("xp_legacy", "📜 Utilisation Legacy"),
            ],
            "PowerShell": [
                ("ps_intro", "⚡ Introduction PowerShell"),
                ("ps_basic", "📝 Commandes de Base"),
                ("ps_advanced", "🚀 PowerShell Avancé"),
                ("ps_scripts", "📜 Scripts Utiles"),
            ],
            "CMD (Invite de commandes)": [
                ("cmd_intro", "💻 Introduction CMD"),
                ("cmd_basic", "📝 Commandes Essentielles"),
                ("cmd_batch", "📜 Fichiers Batch"),
                ("cmd_network", "🌐 Commandes Réseau"),
            ],
            "Registre Windows": [
                ("reg_intro", "📋 Introduction au Registre"),
                ("reg_backup", "💾 Sauvegarde & Restauration"),
                ("reg_tweaks", "⚙️ Tweaks Registre"),
                ("reg_security", "🔒 Sécurité Registre"),
            ],
            "Services Windows": [
                ("svc_intro", "⚙️ Gestion des Services"),
                ("svc_optimize", "⚡ Optimisation Services"),
                ("svc_troubleshoot", "🔧 Dépannage Services"),
            ],
            "Dépannage Windows": [
                ("ts_boot", "🔄 Problèmes de Démarrage"),
                ("ts_bsod", "💙 Écrans Bleus (BSOD)"),
                ("ts_drivers", "🔧 Problèmes de Pilotes"),
                ("ts_network", "🌐 Problèmes Réseau"),
                ("ts_performance", "⚡ Problèmes de Performance"),
            ],
            "Optimisation Windows": [
                ("opt_startup", "🚀 Optimiser le Démarrage"),
                ("opt_disk", "💾 Optimisation Disque"),
                ("opt_memory", "🧠 Gestion Mémoire"),
                ("opt_network", "🌐 Optimisation Réseau"),
                ("opt_gaming", "🎮 Optimisation Gaming"),
            ],
            "Sécurité Windows": [
                ("sec_defender", "🛡️ Windows Defender"),
                ("sec_firewall", "🔥 Pare-feu Windows"),
                ("sec_uac", "🔒 Contrôle de Compte (UAC)"),
                ("sec_updates", "⬆️ Mises à jour Sécurité"),
                ("sec_malware", "🦠 Protection Malware"),
            ],
            "Linux - Bases": [
                ("linux_intro", "🐧 Introduction à Linux"),
                ("linux_distros", "📊 Comparaison Distributions"),
                ("linux_install", "💿 Installation Linux"),
                ("linux_terminal", "⚡ Terminal & Ligne de Commande"),
                ("linux_commands", "📝 Commandes Essentielles"),
            ],
            "Linux - Système de Fichiers": [
                ("linux_files", "📁 Système de Fichiers"),
                ("linux_permissions", "🔒 Permissions & Droits"),
            ],
            "Linux - Gestion Processus & Services": [
                ("linux_processes", "⚙️ Gestion des Processus"),
                ("linux_systemd", "🔄 systemd & Services"),
            ],
            "Linux - Gestionnaires de Paquets": [
                ("linux_apt", "📦 APT (Ubuntu/Debian/Mint)"),
                ("linux_dnf", "📦 DNF (Fedora/RHEL)"),
                ("linux_pacman", "📦 Pacman (Arch/Manjaro)"),
            ],
            "Linux - Réseau & Sécurité": [
                ("linux_network", "🌐 Configuration Réseau"),
                ("linux_firewall", "🔥 Firewall (UFW/iptables)"),
                ("linux_ssh", "🔐 SSH & Accès Distant"),
            ],
            "Linux - Gaming & Compatibilité": [
                ("linux_gaming", "🎮 Gaming sur Linux"),
                ("linux_wine", "🍷 Wine & Proton"),
                ("linux_wsl", "🪟 WSL (Windows Subsystem for Linux)"),
            ],
            "Linux - Administration": [
                ("linux_users", "👤 Gestion Utilisateurs"),
                ("linux_backup", "💾 Sauvegardes"),
                ("linux_disk", "💿 Gestion Disques"),
                ("linux_server", "🖥️ Linux Server"),
            ],
            "Linux - Performance & Optimisation": [
                ("linux_performance", "⚡ Optimisation Performances"),
                ("linux_kernel", "🐧 Kernel Linux"),
            ],
            "Linux - Automatisation": [
                ("linux_scripts", "📜 Scripts Shell"),
                ("linux_cron", "⏰ Tâches Automatisées (cron)"),
                ("linux_logs", "📋 Gestion des Logs"),
            ],
            "Linux - Virtualisation & Desktop": [
                ("linux_virtualization", "💻 Virtualisation (KVM/QEMU)"),
                ("linux_desktop", "🖥️ Environnements de Bureau"),
            ],
            "Linux - Développement": [
                ("linux_development", "💻 Développement Linux"),
                ("linux_docker", "🐳 Docker & Conteneurs"),
            ],
            "Linux - Dépannage": [
                ("linux_boot", "🔧 Boot & GRUB"),
                ("linux_troubleshoot", "🔍 Dépannage Général"),
            ],
            "macOS": [
                ("macos_intro", "🍎 Introduction macOS"),
                ("macos_install", "💿 Installation macOS"),
                ("macos_terminal", "⚡ Terminal macOS"),
                ("macos_homebrew", "🍺 Homebrew"),
                ("macos_optimize", "⚡ Optimisation macOS"),
                ("macos_troubleshoot", "🔧 Dépannage macOS"),
            ],
            "Réseau": [
                ("net_basics", "🌐 Bases du Réseau"),
                ("net_tcp_ip", "📡 TCP/IP & Protocoles"),
                ("net_dns", "🔍 DNS Configuration"),
                ("net_troubleshoot", "🔧 Dépannage Réseau"),
                ("net_vpn", "🔒 VPN & Sécurité"),
            ],
            "Matériel (Hardware)": [
                ("hw_cpu", "🧠 Processeurs (CPU)"),
                ("hw_gpu", "🎨 Cartes Graphiques (GPU)"),
                ("hw_ram", "💾 Mémoire RAM"),
                ("hw_storage", "💿 Stockage (SSD/HDD)"),
                ("hw_troubleshoot", "🔧 Dépannage Matériel"),
            ],
            "Logiciels": [
                ("sw_essential", "⭐ Logiciels Essentiels"),
                ("sw_productivity", "📊 Productivité"),
                ("sw_multimedia", "🎬 Multimédia"),
                ("sw_development", "💻 Développement"),
                ("sw_security", "🔒 Sécurité & Antivirus"),
            ],
        }

        # Créer sections avec accordéon (repliable)
        self.category_frames = {}  # Stocker les frames de guides
        self.category_buttons = {}  # Stocker les boutons de catégories

        for category, guides in self.guides_structure.items():
            # Bouton en-tête catégorie (cliquable pour replier/déplier)
            is_expanded = category in self.expanded_categories
            arrow = "▼" if is_expanded else "▶"

            cat_button = ctk.CTkButton(
                sidebar,
                text=f"{arrow} {category}",
                font=(DesignTokens.FONT_FAMILY, 13, "bold"),
                text_color=DesignTokens.ACCENT_PRIMARY,
                fg_color=DesignTokens.BG_ELEVATED,
                hover_color=DesignTokens.BG_HOVER,
                anchor="w",
                command=lambda cat=category: self._toggle_category(cat)
            )
            cat_button.pack(fill=tk.X, padx=5, pady=(10, 2))
            self.category_buttons[category] = cat_button

            # Frame pour les guides de cette catégorie
            guides_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
            self.category_frames[category] = guides_frame

            # Guides de la catégorie
            for guide_id, guide_title in guides:
                btn = ctk.CTkButton(
                    guides_frame,
                    text=guide_title,
                    font=(DesignTokens.FONT_FAMILY, 12),
                    text_color=DesignTokens.TEXT_SECONDARY,
                    fg_color="transparent",
                    hover_color=DesignTokens.BG_HOVER,
                    anchor="w",
                    command=lambda gid=guide_id: self._load_guide(gid)
                )
                btn.pack(fill=tk.X, padx=5, pady=2)

            # Afficher la frame si la catégorie est ouverte
            if is_expanded:
                guides_frame.pack(fill=tk.X, padx=10, pady=(0, 5))

    def _create_content(self):
        """Zone de contenu principal"""
        self.content_scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=DesignTokens.BG_PRIMARY
        )
        self.content_scroll.grid(row=1, column=1, sticky="nsew", padx=(10, 20), pady=10)

    def _toggle_category(self, category):
        """Ouvrir/Fermer une catégorie dans la sidebar (accordéon)"""
        if category in self.expanded_categories:
            # Fermer la catégorie
            self.expanded_categories.remove(category)
            self.category_frames[category].pack_forget()
        else:
            # Ouvrir la catégorie
            self.expanded_categories.add(category)
            # Remettre la frame APRÈS le bouton de la catégorie pour maintenir l'ordre
            cat_button = self.category_buttons[category]
            self.category_frames[category].pack(fill=tk.X, padx=10, pady=(0, 5), after=cat_button)

        # Rafraîchir la sidebar pour mettre à jour les flèches
        self._refresh_sidebar()

    def _refresh_sidebar(self):
        """Rafraîchir la sidebar (met à jour les flèches des catégories)"""
        # Mettre à jour tous les boutons de catégorie
        for category, button in self.category_buttons.items():
            is_expanded = category in self.expanded_categories
            arrow = "▼" if is_expanded else "▶"
            button.configure(text=f"{arrow} {category}")

    def _load_guide(self, guide_id):
        """Charger un guide spécifique"""
        self.current_guide = guide_id

        # Nettoyer contenu
        for widget in self.content_scroll.winfo_children():
            widget.destroy()

        # Récupérer contenu du guide
        guide_data = self._get_guide_content(guide_id)

        # Carte principale
        card = ModernCard(self.content_scroll)
        card.pack(fill=tk.BOTH, expand=True, pady=10)

        # Titre du guide
        title = ctk.CTkLabel(
            card,
            text=guide_data["title"],
            font=(DesignTokens.FONT_FAMILY, 28, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        )
        title.pack(pady=(20, 10), padx=30)

        # Contenu du guide
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        # Afficher sections
        for section in guide_data["sections"]:
            self._create_section(content_frame, section)

    def _create_section(self, parent, section):
        """Créer une section de guide"""
        # Titre section
        if "title" in section:
            section_title = ctk.CTkLabel(
                parent,
                text=section["title"],
                font=(DesignTokens.FONT_FAMILY, 20, "bold"),
                text_color=DesignTokens.ACCENT_PRIMARY,
                anchor="w"
            )
            section_title.pack(fill=tk.X, pady=(20, 10))

        # Contenu section
        if "content" in section:
            content_label = ctk.CTkLabel(
                parent,
                text=section["content"],
                font=(DesignTokens.FONT_FAMILY, 13),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w",
                justify="left",
                wraplength=900
            )
            content_label.pack(fill=tk.X, pady=5)

        # Liste à puces
        if "bullets" in section:
            for bullet in section["bullets"]:
                bullet_frame = ctk.CTkFrame(parent, fg_color="transparent")
                bullet_frame.pack(fill=tk.X, pady=3)

                ctk.CTkLabel(
                    bullet_frame,
                    text="  • " + bullet,
                    font=(DesignTokens.FONT_FAMILY, 12),
                    text_color=DesignTokens.TEXT_SECONDARY,
                    anchor="w",
                    justify="left",
                    wraplength=880
                ).pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Code block
        if "code" in section:
            code_frame = ctk.CTkFrame(parent, fg_color=DesignTokens.BG_ELEVATED, corner_radius=8)
            code_frame.pack(fill=tk.X, pady=10)

            code_label = ctk.CTkLabel(
                code_frame,
                text=section["code"],
                font=("Consolas", 11),
                text_color="#88C0D0",
                anchor="w",
                justify="left"
            )
            code_label.pack(padx=15, pady=15, anchor="w")

        # Warning/Info box
        if "warning" in section:
            warn_frame = ctk.CTkFrame(parent, fg_color="#3d2a00", corner_radius=8)
            warn_frame.pack(fill=tk.X, pady=10)

            ctk.CTkLabel(
                warn_frame,
                text="⚠️ " + section["warning"],
                font=(DesignTokens.FONT_FAMILY, 12),
                text_color="#FFA500",
                anchor="w",
                justify="left",
                wraplength=880
            ).pack(padx=15, pady=10)

        if "info" in section:
            info_frame = ctk.CTkFrame(parent, fg_color="#1a2d3d", corner_radius=8)
            info_frame.pack(fill=tk.X, pady=10)

            ctk.CTkLabel(
                info_frame,
                text="ℹ️ " + section["info"],
                font=(DesignTokens.FONT_FAMILY, 12),
                text_color="#4682B4",
                anchor="w",
                justify="left",
                wraplength=880
            ).pack(padx=15, pady=10)

    def _get_guide_content(self, guide_id):
        """Récupérer le contenu d'un guide"""
        # Fusionner guides existants avec guides complets importés
        guides = {
            "nitrite_intro": {
                "title": "🏠 Introduction à NiTriTe V20",
                "sections": [
                    {
                        "title": "Qu'est-ce que NiTriTe?",
                        "content": "NiTriTe est une suite complète d'outils pour Windows permettant de gérer, installer et optimiser votre PC de manière professionnelle. C'est l'outil ultime pour les techniciens informatiques et les utilisateurs avancés."
                    },
                    {
                        "title": "Fonctionnalités Principales",
                        "bullets": [
                            "Installation automatique de programmes via Winget",
                            "Gestion complète des applications portables",
                            "Outils de diagnostic et optimisation système",
                            "Scanner de pilotes avancé",
                            "Scanner antivirus multi-moteurs",
                            "Scripts Windows automatisés (170+ scripts)",
                            "Agents IA pour assistance technique",
                            "Gestion des sauvegardes et restauration",
                            "Terminal intégré PowerShell/CMD",
                            "Activation Windows et Office"
                        ]
                    },
                    {
                        "title": "Pourquoi utiliser NiTriTe?",
                        "bullets": [
                            "Gain de temps considérable pour les installations",
                            "Interface moderne et intuitive",
                            "Tout-en-un: pas besoin de 20 outils différents",
                            "Mode portable: aucune installation nécessaire",
                            "Mis à jour régulièrement",
                            "Support complet Windows 11/10/8/7"
                        ]
                    },
                    {
                        "info": "NiTriTe est développé par OrdiPlus et est mis à jour régulièrement avec de nouvelles fonctionnalités."
                    }
                ]
            },
            "nitrite_install": {
                "title": "📥 Installation & Configuration de NiTriTe",
                "sections": [
                    {
                        "title": "Installation",
                        "content": "NiTriTe est disponible en version portable. Aucune installation n'est nécessaire:"
                    },
                    {
                        "bullets": [
                            "Téléchargez NiTriTe_V20_Portable.exe depuis GitHub",
                            "Placez l'exécutable dans un dossier de votre choix",
                            "Double-cliquez pour lancer NiTriTe",
                            "Au premier lancement, NiTriTe créera ses dossiers de configuration"
                        ]
                    },
                    {
                        "title": "Configuration Initiale",
                        "bullets": [
                            "Accédez à Paramètres (⚙️) dans la navigation",
                            "Configurez vos préférences de thème (Clair/Sombre)",
                            "Définissez vos dossiers de téléchargement",
                            "Configurez les agents IA si nécessaire"
                        ]
                    },
                    {
                        "title": "Prérequis Système",
                        "bullets": [
                            "Windows 7 SP1 ou supérieur (Windows 10/11 recommandé)",
                            "4 GB RAM minimum (8 GB recommandé)",
                            "500 MB d'espace disque",
                            "Connexion Internet pour téléchargements",
                            "Droits administrateur pour certaines fonctions"
                        ]
                    },
                    {
                        "warning": "Pour utiliser toutes les fonctionnalités (drivers, optimisations), NiTriTe doit être exécuté en tant qu'administrateur."
                    }
                ]
            },
            "nitrite_features": {
                "title": "⚡ Fonctionnalités Principales de NiTriTe",
                "sections": [
                    {
                        "title": "1. Master Install - Installation Automatisée",
                        "content": "Le mode Master Install permet d'installer rapidement tous vos programmes favoris:"
                    },
                    {
                        "bullets": [
                            "Plus de 500 programmes disponibles via Winget",
                            "Installation par lots (sélectionnez plusieurs programmes)",
                            "Packs personnalisés (créez vos propres listes)",
                            "Intégration OrdiPlus (configuration automatique)",
                            "Suivi en temps réel de l'installation"
                        ]
                    },
                    {
                        "title": "2. Applications Portables",
                        "bullets": [
                            "Catalogue de 100+ applications portables",
                            "Téléchargement et extraction automatique",
                            "Lancement direct depuis NiTriTe",
                            "Gestion des versions",
                            "Mise à jour automatique"
                        ]
                    },
                    {
                        "title": "3. Scanner de Pilotes Avancé",
                        "bullets": [
                            "Scan complet de tous les drivers système",
                            "Détection des pilotes obsolètes",
                            "Sauvegarde complète des pilotes",
                            "Restauration depuis sauvegarde",
                            "Compatible Windows Update"
                        ]
                    },
                    {
                        "title": "4. Scanner Antivirus Multi-Moteurs",
                        "bullets": [
                            "Scan avec plusieurs moteurs antivirus",
                            "Détection des malwares et PUP",
                            "Quarantaine automatique",
                            "Rapports détaillés",
                            "Scan planifié"
                        ]
                    },
                    {
                        "title": "5. Scripts Windows (170+ scripts)",
                        "bullets": [
                            "Optimisation du démarrage",
                            "Configuration des services",
                            "Tweaks de performance",
                            "Sécurité et confidentialité",
                            "Troubleshooting automatisé"
                        ]
                    },
                    {
                        "title": "6. Diagnostic Système Complet",
                        "bullets": [
                            "Informations système détaillées",
                            "Test de performance (CPU/GPU/Disque)",
                            "Analyse de santé du système",
                            "Détection de problèmes",
                            "Rapports HTML exportables"
                        ]
                    }
                ]
            },
            "w11_intro": {
                "title": "🪟 Introduction à Windows 11",
                "sections": [
                    {
                        "title": "Windows 11 - Le nouveau Windows",
                        "content": "Windows 11 est la dernière version du système d'exploitation Microsoft, lancée en octobre 2021. Il apporte une interface modernisée, de meilleures performances gaming, et une sécurité renforcée."
                    },
                    {
                        "title": "Nouveautés Principales",
                        "bullets": [
                            "Interface redessinée avec coins arrondis",
                            "Menu Démarrer centré (personnalisable)",
                            "Widgets intégrés",
                            "Support Android (via Microsoft Store)",
                            "DirectStorage pour gaming",
                            "Auto HDR pour jeux",
                            "Snap Layouts améliorés",
                            "Microsoft Teams intégré",
                            "Sécurité: TPM 2.0 + Secure Boot obligatoires"
                        ]
                    },
                    {
                        "title": "Configuration Requise",
                        "bullets": [
                            "Processeur: 1 GHz 64-bit, 2+ cœurs",
                            "RAM: 4 GB minimum",
                            "Stockage: 64 GB minimum",
                            "Carte graphique: DirectX 12 compatible",
                            "TPM: Version 2.0 OBLIGATOIRE",
                            "UEFI + Secure Boot",
                            "Écran: 720p, >9 pouces"
                        ]
                    },
                    {
                        "warning": "Windows 11 nécessite OBLIGATOIREMENT TPM 2.0 et Secure Boot. Vérifiez la compatibilité de votre PC avant la mise à niveau."
                    },
                    {
                        "title": "Avantages vs Windows 10",
                        "bullets": [
                            "Interface plus moderne et cohérente",
                            "Meilleures performances gaming (DirectStorage, Auto HDR)",
                            "Sécurité renforcée (TPM 2.0, VBS)",
                            "Gestion améliorée des écrans multiples",
                            "Widgets pratiques",
                            "Support plus long (jusqu'en 2031)"
                        ]
                    },
                    {
                        "title": "Inconvénients",
                        "bullets": [
                            "Configuration matérielle stricte (TPM 2.0)",
                            "Barre des tâches moins personnalisable",
                            "Certaines fonctionnalités retirées (Cortana, Timeline)",
                            "Consommation RAM légèrement supérieure",
                            "Widgets nécessitent un compte Microsoft"
                        ]
                    }
                ]
            },
            "w11_optimize": {
                "title": "⚡ Optimisation Performance Windows 11",
                "sections": [
                    {
                        "title": "1. Optimiser le Démarrage",
                        "bullets": [
                            "Désactiver programmes au démarrage (Gestionnaire des tâches > Démarrage)",
                            "Activer le démarrage rapide (Panneau de configuration > Options d'alimentation)",
                            "Désactiver services inutiles avec NiTriTe Scripts",
                            "Nettoyer le dossier TEMP régulièrement"
                        ]
                    },
                    {
                        "title": "2. Optimisations Visuelles",
                        "content": "Pour améliorer les performances, réduisez les effets visuels:"
                    },
                    {
                        "code": "Paramètres > Système > Affichage > Effets visuels\n- Désactiver transparence\n- Désactiver animations\n- Réduire effets"
                    },
                    {
                        "title": "3. Optimiser la Mémoire",
                        "bullets": [
                            "Augmenter le fichier d'échange (Pagefile) si <16 GB RAM",
                            "Désactiver SuperFetch/SysMain (SSD uniquement)",
                            "Limiter les programmes en arrière-plan",
                            "Utiliser le nettoyage de disque régulièrement"
                        ]
                    },
                    {
                        "title": "4. Gaming - Optimisations",
                        "bullets": [
                            "Activer le Mode Jeu (Paramètres > Jeux)",
                            "Activer DirectStorage (jeux compatibles)",
                            "Activer Auto HDR",
                            "Désactiver Game Bar si non utilisé",
                            "Définir priorité GPU (Paramètres graphiques)",
                            "Désactiver VBS pour +5-10% FPS (réduit sécurité)"
                        ]
                    },
                    {
                        "title": "5. Réseau",
                        "bullets": [
                            "Désactiver Wi-Fi Sense",
                            "Optimiser DNS (utiliser 1.1.1.1 ou 8.8.8.8)",
                            "Désactiver IPv6 si non utilisé",
                            "Limiter bande passante Windows Update"
                        ]
                    },
                    {
                        "warning": "Désactiver VBS (Virtualization-Based Security) améliore les performances gaming mais réduit la sécurité. À utiliser uniquement sur PC gaming personnel."
                    }
                ]
            },
            "ps_intro": {
                "title": "⚡ Introduction à PowerShell",
                "sections": [
                    {
                        "title": "Qu'est-ce que PowerShell?",
                        "content": "PowerShell est un shell en ligne de commande moderne et un langage de script développé par Microsoft. Bien plus puissant que CMD, il permet d'automatiser pratiquement n'importe quelle tâche Windows."
                    },
                    {
                        "title": "Avantages vs CMD",
                        "bullets": [
                            "Syntaxe orientée objet (cmdlets)",
                            "Pipeline de données avancé",
                            "Intégration .NET Framework",
                            "Scripting puissant avec variables, boucles, conditions",
                            "Gestion complète de Windows (WMI, COM, .NET)",
                            "Cross-platform (PowerShell Core sur Linux/macOS)"
                        ]
                    },
                    {
                        "title": "Lancer PowerShell",
                        "bullets": [
                            "Windows + X > Windows PowerShell",
                            "Rechercher 'PowerShell' dans le menu Démarrer",
                            "Win + R > powershell > Entrée",
                            "PowerShell ISE (environnement de script intégré)"
                        ]
                    },
                    {
                        "title": "Commandes de Base (Cmdlets)",
                        "content": "Les cmdlets PowerShell suivent la convention Verbe-Nom:"
                    },
                    {
                        "code": "# Obtenir de l'aide\nGet-Help Get-Process\nGet-Help *service*\n\n# Lister les processus\nGet-Process\n\n# Lister les services\nGet-Service\n\n# Informations système\nGet-ComputerInfo\n\n# Lister fichiers\nGet-ChildItem C:\\\n\n# Créer dossier\nNew-Item -Path 'C:\\Test' -ItemType Directory"
                    },
                    {
                        "title": "Execution Policy",
                        "content": "Par défaut, PowerShell bloque l'exécution de scripts pour la sécurité:"
                    },
                    {
                        "code": "# Voir la politique actuelle\nGet-ExecutionPolicy\n\n# Autoriser scripts locaux (Admin requis)\nSet-ExecutionPolicy RemoteSigned\n\n# Bypass temporaire\nSet-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
                    },
                    {
                        "warning": "Modifier l'Execution Policy peut exposer votre système. N'exécutez que des scripts de sources fiables."
                    }
                ]
            },
            "bash_intro": {
                "title": "⚡ Introduction au Terminal Bash",
                "sections": [
                    {
                        "title": "Qu'est-ce que Bash?",
                        "content": "Bash (Bourne Again Shell) est le shell de commandes par défaut sur la plupart des distributions Linux et macOS. C'est un outil extrêmement puissant pour l'administration système et l'automatisation."
                    },
                    {
                        "title": "Navigation de Base",
                        "code": "# Afficher le répertoire actuel\npwd\n\n# Lister fichiers\nls\nls -la  # Détaillé avec fichiers cachés\n\n# Changer de répertoire\ncd /home/user\ncd ..  # Remonter d'un niveau\ncd ~   # Aller au home\n\n# Créer dossier\nmkdir mon_dossier\n\n# Supprimer fichier\nrm fichier.txt\n\n# Supprimer dossier\nrm -r mon_dossier"
                    },
                    {
                        "title": "Gestion de Fichiers",
                        "code": "# Copier fichier\ncp source.txt destination.txt\n\n# Déplacer/Renommer\nmv ancien.txt nouveau.txt\n\n# Afficher contenu fichier\ncat fichier.txt\nless fichier.txt  # Navigation page par page\n\n# Rechercher dans fichier\ngrep 'mot' fichier.txt\n\n# Compter lignes/mots\nwc -l fichier.txt"
                    },
                    {
                        "title": "Permissions",
                        "code": "# Voir permissions\nls -l\n\n# Modifier permissions (rwx = 7, rw- = 6, r-- = 4)\nchmod 755 script.sh  # rwxr-xr-x\nchmod +x script.sh   # Ajouter exécution\n\n# Changer propriétaire\nsudo chown user:group fichier.txt"
                    },
                    {
                        "title": "Processus",
                        "code": "# Lister processus\nps aux\ntop        # Temps réel\nhtop       # Interface améliorée\n\n# Tuer processus\nkill PID\nkill -9 PID  # Force\nkillall nom_process"
                    },
                    {
                        "title": "Pipe & Redirection",
                        "code": "# Pipe (|) - sortie vers commande suivante\nls -la | grep '.txt'\n\n# Redirection (>) - sortie vers fichier\nls > liste.txt\n\n# Append (>>) - ajouter à fichier\necho 'texte' >> fichier.txt\n\n# Input (<) - depuis fichier\nsort < liste.txt"
                    },
                    {
                        "info": "Le pipe (|) est l'un des concepts les plus puissants de Bash. Il permet de chaîner plusieurs commandes pour créer des workflows complexes."
                    }
                ]
            },
            "ubuntu_intro": {
                "title": "🐧 Introduction à Ubuntu Linux",
                "sections": [
                    {
                        "title": "Ubuntu - Le Linux Accessible",
                        "content": "Ubuntu est la distribution Linux la plus populaire pour les débutants. Développée par Canonical, elle offre un équilibre parfait entre facilité d'utilisation et puissance."
                    },
                    {
                        "title": "Pourquoi Ubuntu?",
                        "bullets": [
                            "Interface graphique intuitive (GNOME)",
                            "Grande communauté et support",
                            "Logithèque complète (snap, apt)",
                            "Support LTS (Long Term Support) - 5 ans",
                            "Excellent pour serveurs et postes de travail",
                            "Compatible avec beaucoup de matériel",
                            "Mises à jour régulières et sécurisées"
                        ]
                    },
                    {
                        "title": "Versions Ubuntu",
                        "bullets": [
                            "Ubuntu Desktop: Pour ordinateurs personnels",
                            "Ubuntu Server: Pour serveurs (sans interface graphique)",
                            "Ubuntu LTS: Versions Long Term Support (18.04, 20.04, 22.04, 24.04)",
                            "Kubuntu: Avec KDE Plasma",
                            "Xubuntu: Avec XFCE (léger)",
                            "Lubuntu: Avec LXQt (très léger)"
                        ]
                    },
                    {
                        "title": "Commandes Essentielles",
                        "code": "# Mettre à jour le système\nsudo apt update\nsudo apt upgrade\n\n# Installer un programme\nsudo apt install firefox\n\n# Rechercher programme\napt search vlc\n\n# Supprimer programme\nsudo apt remove firefox\nsudo apt autoremove  # Nettoyer dépendances\n\n# Informations système\nuname -a\nlsb_release -a"
                    },
                    {
                        "title": "Structure des Dossiers",
                        "bullets": [
                            "/home/user - Dossier personnel",
                            "/etc - Fichiers de configuration système",
                            "/var - Données variables (logs, cache)",
                            "/usr - Programmes installés",
                            "/tmp - Fichiers temporaires",
                            "/opt - Logiciels optionnels",
                            "/bin - Commandes essentielles",
                            "/boot - Fichiers de démarrage"
                        ]
                    }
                ]
            },
            "macos_intro": {
                "title": "🍎 Introduction à macOS",
                "sections": [
                    {
                        "title": "macOS - Le système Apple",
                        "content": "macOS est le système d'exploitation d'Apple pour Mac. Basé sur Unix (Darwin), il combine puissance, sécurité et design élégant."
                    },
                    {
                        "title": "Versions Récentes",
                        "bullets": [
                            "macOS Sequoia (15) - 2024",
                            "macOS Sonoma (14) - 2023",
                            "macOS Ventura (13) - 2022",
                            "macOS Monterey (12) - 2021",
                            "macOS Big Sur (11) - 2020",
                            "macOS Catalina (10.15) - 2019"
                        ]
                    },
                    {
                        "title": "Raccourcis Clavier Essentiels",
                        "bullets": [
                            "Cmd + C/V/X - Copier/Coller/Couper",
                            "Cmd + Q - Quitter application",
                            "Cmd + W - Fermer fenêtre",
                            "Cmd + Tab - Changer d'application",
                            "Cmd + Space - Spotlight (recherche)",
                            "Cmd + , - Préférences",
                            "Cmd + Option + Esc - Forcer à quitter",
                            "Cmd + Shift + 3/4 - Capture d'écran"
                        ]
                    },
                    {
                        "title": "Terminal macOS",
                        "content": "Le Terminal macOS utilise Zsh (anciennement Bash) et offre un accès complet au système Unix:"
                    },
                    {
                        "code": "# Ouvrir Terminal\nCmd + Space > Terminal\n\n# Commandes de base (identiques à Linux)\nls -la\ncd ~\npwd\n\n# Homebrew (gestionnaire de paquets)\n/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'\n\n# Installer logiciel avec Homebrew\nbrew install wget\nbrew install --cask firefox"
                    },
                    {
                        "title": "Finder - Astuces",
                        "bullets": [
                            "Cmd + Shift + . - Afficher fichiers cachés",
                            "Cmd + Shift + G - Aller au dossier (path direct)",
                            "Cmd + I - Informations fichier",
                            "Cmd + Delete - Supprimer fichier",
                            "Space - Aperçu rapide (Quick Look)"
                        ]
                    },
                    {
                        "title": "Maintenance macOS",
                        "bullets": [
                            "Mettre à jour: Préférences Système > Mise à jour",
                            "Nettoyer cache: ~/Library/Caches",
                            "Réparer permissions: Utilitaire de disque",
                            "Reset PRAM: Cmd + Option + P + R au démarrage",
                            "Reset SMC: Varie selon modèle Mac"
                        ]
                    }
                ]
            },
            # Default pour guides non encore implémentés
            "default": {
                "title": "📖 Guide en Construction",
                "sections": [
                    {
                        "content": "Ce guide est en cours de rédaction. Il sera disponible prochainement avec un contenu complet et détaillé."
                    },
                    {
                        "info": "Consultez les autres guides disponibles dans la barre latérale. La base de connaissances s'enrichit régulièrement."
                    }
                ]
            }
        }

        # Fusionner avec les guides complets importés (priorité aux importés)
        all_guides = {**guides, **COMPLETE_GUIDES_DATA}

        # Retourner le guide ou le template par défaut
        return all_guides.get(guide_id, guides.get("default", {
            "title": "📖 Guide en Construction",
            "sections": [{"content": "Ce guide est en cours de rédaction."}]
        }))

    def _search_guides(self):
        """Recherche dans les guides (future implémentation)"""
        messagebox.showinfo(
            "Recherche",
            "La fonction de recherche sera disponible prochainement.\n\n"
            "En attendant, utilisez la navigation par catégories dans la barre latérale."
        )
