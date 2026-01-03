#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base de données complète pour tous les guides de la Base de Connaissances
Contenu complet pour priorités 1-6: NiTriTe, Windows, PowerShell, etc.
"""

# DONNÉES COMPLÈTES POUR TOUS LES GUIDES
COMPLETE_GUIDES_DATA = {
    # =========================================================================
    # PRIORITÉ 1: GUIDES NITRITE (7 guides)
    # =========================================================================

    "nitrite_intro": {
        "title": "🏠 Introduction à NiTriTe V20",
        "sections": [
            {
                "title": "Qu'est-ce que NiTriTe?",
                "content": "NiTriTe V20 est une suite d'outils professionnelle tout-en-un conçue pour les techniciens informatiques, administrateurs système et utilisateurs avancés. Elle regroupe tous les outils essentiels pour installer, configurer, diagnostiquer et optimiser des systèmes Windows en un seul logiciel portable."
            },
            {
                "title": "Pourquoi utiliser NiTriTe?",
                "bullets": [
                    "Gain de temps massif: Installation batch de dizaines d'applications en un clic",
                    "Suite complète: Plus besoin de chercher 50 outils différents",
                    "Mode portable: Fonctionne depuis une clé USB, aucune installation requise",
                    "Interface moderne: Design intuitif avec thèmes personnalisables",
                    "Open Source: Code transparent, pas de télémétrie cachée",
                    "Gratuit: 100% gratuit, pas de version premium ou d'abonnement",
                    "Professionnel: Conçu pour un usage technique intensif"
                ]
            },
            {
                "title": "Fonctionnalités Clés",
                "bullets": [
                    "🎯 Master Install: Installation automatisée de +500 programmes via Winget",
                    "🔧 Scanner Pilotes: Détection et mise à jour de tous les drivers système",
                    "🦠 Scanner Antivirus: Protection multi-moteurs avec quarantaine",
                    "📦 Apps Portables: Gestion de 100+ applications portables",
                    "🔑 Activation: Windows et Office via Microsoft Activation Scripts",
                    "💻 Terminal: PowerShell/CMD intégré avec auto-complétion",
                    "📊 Statistiques: Rapports système détaillés et monitoring",
                    "🤖 Agent IA: Assistant intelligent pour support technique",
                    "📚 Base de Connaissances: Documentation complète intégrée"
                ]
            },
            {
                "title": "Pour qui est NiTriTe?",
                "bullets": [
                    "Techniciens informatiques: Installation rapide de PC clients",
                    "Administrateurs système: Déploiement standardisé d'applications",
                    "Support technique: Diagnostic et résolution de problèmes",
                    "Power users: Optimisation et personnalisation avancée",
                    "Gamers: Configuration gaming optimale",
                    "Créateurs de contenu: Installation de suites créatives complètes"
                ]
            },
            {
                "title": "Comparaison avec d'autres outils",
                "content": "NiTriTe se positionne comme une alternative complète à:\n\n• Ninite: Installation batch mais catalogue limité (90 apps vs 500+ pour NiTriTe)\n• Chocolatey: Ligne de commande complexe vs interface graphique intuitive\n• Snappy Driver: Scanner de pilotes mais outil unique vs suite complète\n• Multiple outils séparés: Tout regroupé en un seul logiciel portable"
            },
            {
                "info": "💡 Astuce: NiTriTe est conçu pour être utilisé depuis une clé USB. Créez votre 'clé USB du technicien' avec NiTriTe et tous vos outils favoris!"
            },
            {
                "warning": "⚠️ Important: NiTriTe nécessite des droits administrateur pour installer des programmes et modifier des paramètres système."
            }
        ]
    },

    "nitrite_install": {
        "title": "📥 Installation & Configuration de NiTriTe",
        "sections": [
            {
                "title": "Prérequis Système",
                "bullets": [
                    "Windows 10 (version 1809+) ou Windows 11",
                    "Python 3.12 ou supérieur (inclus dans le package portable)",
                    "4 GB RAM minimum (8 GB recommandé)",
                    "500 MB d'espace disque pour NiTriTe",
                    "10 GB+ d'espace pour les applications à installer",
                    "Connexion Internet active (pour Winget et téléchargements)",
                    "Droits administrateur Windows"
                ]
            },
            {
                "title": "Méthode 1: Version Portable (Recommandée)",
                "bullets": [
                    "Étape 1: Téléchargez NiTriTe_V20_Portable.exe depuis GitHub Releases",
                    "Étape 2: Copiez l'exécutable sur votre clé USB ou disque dur",
                    "Étape 3: Double-cliquez sur NiTriTe_V20_Portable.exe",
                    "Étape 4: L'application se lance directement, aucune installation requise",
                    "Étape 5: Au premier lancement, les dossiers data/ et logs/ sont créés automatiquement"
                ]
            },
            {
                "title": "Méthode 2: Depuis le Code Source",
                "bullets": [
                    "Étape 1: Installez Python 3.12+ depuis python.org",
                    "Étape 2: Clonez le dépôt: git clone https://github.com/heiphaistos44-crypto/NiTriTe-v20.0",
                    "Étape 3: Accédez au dossier: cd NiTriTe-v20.0",
                    "Étape 4: Installez les dépendances: pip install -r requirements.txt",
                    "Étape 5: Lancez l'application: python -m src.v14_mvp.main_app",
                    "Note: Cette méthode est pour les développeurs ou tests"
                ]
            },
            {
                "title": "Configuration Initiale",
                "bullets": [
                    "Au premier lancement, NiTriTe configure automatiquement:",
                    "• Création du dossier Documents/NiTriTe_Reports pour les rapports",
                    "• Création du dossier data/logs pour les journaux",
                    "• Vérification de Winget (installé automatiquement si absent)",
                    "• Chargement de la base de données de 500+ programmes",
                    "• Configuration du thème par défaut (modifiable dans Paramètres)"
                ]
            },
            {
                "title": "Personnalisation des Paramètres",
                "bullets": [
                    "Ouvrez la page 'Paramètres' dans le menu de navigation",
                    "Thème: Choisissez entre Dark Mode, Light Mode ou Custom",
                    "Langue: Français, Anglais (autres langues à venir)",
                    "Dossier de téléchargement: Modifiez le chemin par défaut",
                    "Notifications: Activez/désactivez les popups de succès",
                    "Auto-update: Configuration des mises à jour automatiques"
                ]
            },
            {
                "title": "Installation de Winget (si nécessaire)",
                "bullets": [
                    "Winget est requis pour le Master Install et l'installation de programmes",
                    "Si Winget n'est pas détecté au lancement:",
                    "Méthode automatique: Cliquez sur 'Installer Winget' dans le popup",
                    "Méthode manuelle: Téléchargez depuis github.com/microsoft/winget-cli",
                    "Windows 11: Winget est pré-installé",
                    "Windows 10: Installation via Microsoft Store ou package .msixbundle"
                ]
            },
            {
                "title": "Vérification de l'Installation",
                "bullets": [
                    "Pour vérifier que tout fonctionne correctement:",
                    "1. Ouvrez la page 'Terminal' et tapez: winget --version",
                    "2. La version de Winget devrait s'afficher (ex: v1.7.10582)",
                    "3. Ouvrez la page 'Master Install' et vérifiez que les programmes sont listés",
                    "4. Testez l'installation d'un petit programme comme 7-Zip",
                    "5. Consultez les logs dans 'Logs Système' pour vérifier qu'il n'y a pas d'erreurs"
                ]
            },
            {
                "title": "Création d'une Clé USB du Technicien",
                "bullets": [
                    "NiTriTe est idéal pour créer une clé USB bootable complète:",
                    "Étape 1: Formatez une clé USB 32GB+ en NTFS",
                    "Étape 2: Copiez NiTriTe_V20_Portable.exe à la racine",
                    "Étape 3: Ajoutez un dossier 'Tools' avec vos utilitaires favoris",
                    "Étape 4: Ajoutez un dossier 'Drivers' avec des packs de pilotes génériques",
                    "Étape 5: Créez un fichier README.txt avec vos notes personnelles",
                    "Bonus: Ajoutez Ventoy ou Rufus pour créer des USB bootables sur site"
                ]
            },
            {
                "warning": "⚠️ Première exécution: L'antivirus Windows Defender peut scanner NiTriTe et bloquer temporairement l'exécution. Cliquez sur 'Plus d'infos' puis 'Exécuter quand même'. C'est normal pour un nouvel exécutable portable."
            },
            {
                "info": "💡 Astuce: Pour une installation ultra-rapide sur un nouveau PC, préparez un pack personnalisé dans Master Install avec tous vos programmes favoris, puis sauvegardez-le. Vous pourrez le réutiliser sur tous les PC que vous configurez!"
            },
            {
                "title": "Dépannage Installation",
                "bullets": [
                    "Problème: 'Python introuvable'",
                    "→ Solution: Réinstallez Python 3.12+ et cochez 'Add to PATH'",
                    "",
                    "Problème: 'Winget n'est pas reconnu'",
                    "→ Solution: Installez Winget depuis Microsoft Store ou github.com/microsoft/winget-cli",
                    "",
                    "Problème: 'Erreur de module customtkinter'",
                    "→ Solution: pip install customtkinter --upgrade",
                    "",
                    "Problème: L'application ne se lance pas",
                    "→ Solution: Vérifiez les logs dans data/logs/error.log pour diagnostiquer"
                ]
            }
        ]
    },

    "nitrite_features": {
        "title": "⚡ Fonctionnalités Principales de NiTriTe",
        "sections": [
            {
                "title": "Vue d'Ensemble",
                "content": "NiTriTe V20 offre une suite complète d'outils professionnels pour la gestion, l'installation et l'optimisation de Windows. Chaque fonctionnalité est conçue pour faire gagner du temps aux techniciens et utilisateurs avancés."
            },
            {
                "title": "Master Install - Installation Automatisée",
                "bullets": [
                    "Installation batch de +500 programmes via Winget",
                    "Packs prédéfinis: Gaming, Bureautique, Développement, Création",
                    "Packs personnalisés: créez vos propres listes",
                    "Progression en temps réel avec barre de progression",
                    "Logs détaillés de chaque installation",
                    "Gestion automatique des échecs et retry"
                ]
            },
            {
                "title": "Scanner de Pilotes Avancé",
                "bullets": [
                    "Scan complet de TOUS les pilotes système",
                    "Détection automatique: Laptop vs Desktop",
                    "Catégorisation intelligente (Audio, Display, Network, etc.)",
                    "Statistiques par catégorie (top 5)",
                    "Mise à jour des drivers via Windows Update",
                    "Sauvegarde et restauration de drivers",
                    "Export de la liste complète"
                ]
            },
            {
                "title": "Scanner Antivirus Multi-Moteurs",
                "bullets": [
                    "Intégration de 10+ moteurs antivirus",
                    "Scan en temps réel avec progression",
                    "Détection des menaces critiques",
                    "Quarantaine automatique",
                    "Rapports détaillés",
                    "Gestion des faux positifs",
                    "Nettoyage automatique"
                ]
            },
            {
                "title": "Terminal Intégré PowerShell/CMD",
                "bullets": [
                    "Terminal moderne intégré",
                    "Support PowerShell 7+ et CMD",
                    "Historique des commandes",
                    "Auto-complétion",
                    "Taille de police ajustable",
                    "Hauteur personnalisable",
                    "Exécution de scripts .ps1/.bat"
                ]
            },
            {
                "title": "Activation Windows & Office",
                "bullets": [
                    "Intégration de Microsoft Activation Scripts (MAS)",
                    "Détection automatique du statut d'activation",
                    "Support Windows 11/10/8/7",
                    "Support Office 2024/2021/2019/2016",
                    "Méthodes: HWID, KMS, OEM",
                    "Terminal intégré pour MAS",
                    "Vérification en temps réel"
                ]
            },
            {
                "title": "Applications Portables",
                "bullets": [
                    "Catalogue de 100+ apps portables",
                    "Téléchargement automatique depuis PortableApps",
                    "Installation sans droits admin",
                    "Gestion centralisée",
                    "Mises à jour automatiques",
                    "Export de configurations"
                ]
            },
            {
                "title": "Scripts Windows Automatisés",
                "bullets": [
                    "170+ scripts d'optimisation Windows",
                    "Catégories: BOOT, Services, Sécurité, Performance",
                    "Scripts Atlas OS intégrés",
                    "Désactivation télémétrie",
                    "Optimisation gaming",
                    "Tweaks système avancés"
                ]
            },
            {
                "title": "Agents IA Intelligents",
                "bullets": [
                    "Assistant IA contextuel",
                    "Analyse d'intention avancée",
                    "Recommandations personnalisées",
                    "Support technique automatisé",
                    "Base de connaissances intégrée",
                    "Apprentissage continu"
                ]
            },
            {
                "info": "💡 Astuce: Toutes les fonctionnalités sont accessibles depuis le menu de navigation latéral. Explorez chaque section pour découvrir tous les outils disponibles."
            }
        ]
    },

    "nitrite_masterinstall": {
        "title": "🎯 Master Install Mode - Installation Batch",
        "sections": [
            {
                "title": "Qu'est-ce que le Master Install?",
                "content": "Le Master Install est le mode d'installation automatisée de programmes qui permet d'installer des dizaines d'applications en un seul clic via Winget. Idéal pour configurer un nouveau PC ou réinstaller rapidement un système."
            },
            {
                "title": "Comment utiliser le Master Install",
                "bullets": [
                    "Étape 1: Ouvrez la page 'Master Install' dans le menu",
                    "Étape 2: Choisissez un pack prédéfini (Gaming, Bureautique, Dev) ou créez un pack personnalisé",
                    "Étape 3: Sélectionnez les programmes individuels à installer",
                    "Étape 4: Cliquez sur 'Lancer Installation'",
                    "Étape 5: Suivez la progression en temps réel",
                    "Étape 6: Consultez le rapport d'installation final"
                ]
            },
            {
                "title": "Packs Prédéfinis Disponibles",
                "bullets": [
                    "🎮 Gaming: Steam, Discord, OBS, GeForce Experience, Epic Games, etc.",
                    "💼 Bureautique: Office, LibreOffice, Adobe Reader, Notion, Teams, etc.",
                    "👨‍💻 Développement: VS Code, Git, Node.js, Python, Docker, Postman, etc.",
                    "🎨 Création: GIMP, Inkscape, Audacity, DaVinci Resolve, Blender, etc.",
                    "🌐 Navigateurs: Chrome, Firefox, Brave, Edge, Opera, etc.",
                    "🛠️ Utilitaires: 7-Zip, VLC, Rufus, Everything, ShareX, etc."
                ]
            },
            {
                "title": "Créer un Pack Personnalisé",
                "bullets": [
                    "Cliquez sur '➕ Nouveau Pack'",
                    "Nommez votre pack (ex: 'Pack Technicien')",
                    "Ajoutez des programmes depuis le catalogue",
                    "Réorganisez l'ordre d'installation (drag & drop)",
                    "Sauvegardez le pack",
                    "Réutilisez-le sur plusieurs PC"
                ]
            },
            {
                "title": "Suivi de l'Installation",
                "content": "Pendant l'installation, NiTriTe affiche:"
            },
            {
                "bullets": [
                    "Barre de progression globale (X/Y programmes)",
                    "Programme en cours d'installation",
                    "Statut de chaque programme (✅ Succès, ❌ Échec, ⏭️ Ignoré)",
                    "Temps estimé restant",
                    "Logs détaillés en temps réel",
                    "Rapport final avec résumé"
                ]
            },
            {
                "title": "Gestion des Échecs",
                "bullets": [
                    "Retry automatique (3 tentatives)",
                    "Pause/Reprise possible",
                    "Annulation à tout moment",
                    "Liste des échecs dans le rapport",
                    "Recommandations de correction",
                    "Possibilité de réinstaller les échecs uniquement"
                ]
            },
            {
                "warning": "⚠️ Important: Une connexion Internet stable est requise. L'installation peut prendre de quelques minutes à plusieurs heures selon le nombre de programmes et votre débit."
            },
            {
                "info": "💡 Astuce Pro: Créez un pack 'Post-Install Windows' avec tous les programmes essentiels pour gagner 2-3 heures sur chaque installation Windows."
            }
        ]
    },

    "nitrite_portable": {
        "title": "📦 Applications Portables - Gestion Centralisée",
        "sections": [
            {
                "title": "Qu'est-ce qu'une Application Portable?",
                "content": "Une application portable est un logiciel qui fonctionne sans installation. Tout est contenu dans un dossier unique, sans entrées dans le registre Windows. Idéal pour clés USB, dépannage ou environnements sans droits admin."
            },
            {
                "title": "Avantages des Portables",
                "bullets": [
                    "✅ Aucune installation nécessaire",
                    "✅ Pas de droits administrateur requis",
                    "✅ Transportable sur clé USB/disque externe",
                    "✅ Pas de traces dans le système",
                    "✅ Plusieurs versions simultanées possibles",
                    "✅ Suppression = simple suppression de dossier",
                    "✅ Configurations sauvegardées avec l'app"
                ]
            },
            {
                "title": "Catalogue NiTriTe (100+ Apps)",
                "content": "NiTriTe intègre un catalogue complet d'applications portables depuis PortableApps.com:"
            },
            {
                "bullets": [
                    "🌐 Navigateurs: Firefox, Chrome, Opera",
                    "📝 Bureautique: LibreOffice, AbiWord, PDF readers",
                    "🎨 Multimédia: VLC, GIMP, Audacity, Inkscape",
                    "👨‍💻 Développement: Notepad++, VS Code Portable, Python",
                    "🛠️ Utilitaires: 7-Zip, Everything, CCleaner",
                    "🔐 Sécurité: KeePass, ClamWin Antivirus",
                    "💬 Communication: Thunderbird, Skype",
                    "🎮 Gaming: emulateurs portables"
                ]
            },
            {
                "title": "Installation d'une App Portable",
                "bullets": [
                    "Étape 1: Ouvrez 'Applications Portables' dans le menu",
                    "Étape 2: Parcourez le catalogue par catégorie",
                    "Étape 3: Cliquez sur 'Télécharger' pour l'app souhaitée",
                    "Étape 4: Choisissez le dossier de destination",
                    "Étape 5: Attendez le téléchargement et extraction",
                    "Étape 6: Lancez l'app directement depuis NiTriTe"
                ]
            },
            {
                "title": "Gestion Centralisée",
                "bullets": [
                    "Vue d'ensemble de toutes les portables installées",
                    "Lancement rapide depuis NiTriTe",
                    "Mise à jour automatique disponible",
                    "Suppression en un clic",
                    "Export de la configuration",
                    "Synchronisation multi-machines"
                ]
            },
            {
                "title": "Création d'un Kit USB de Dépannage",
                "content": "Utilisez les portables pour créer une clé USB de technicien complète:"
            },
            {
                "bullets": [
                    "1. Installez NiTriTe sur une clé USB (8GB+)",
                    "2. Ajoutez les portables essentiels:",
                    "   • Firefox Portable (navigation)",
                    "   • 7-Zip Portable (archives)",
                    "   • Notepad++ Portable (édition)",
                    "   • VLC Portable (multimédia)",
                    "   • CrystalDiskInfo Portable (disques)",
                    "   • HWiNFO Portable (hardware)",
                    "3. Votre clé est prête pour tout dépannage!"
                ]
            },
            {
                "info": "💡 Les applications portables sont parfaites pour les techniciens IT qui interviennent sur différents PC sans pouvoir installer de logiciels."
            }
        ]
    },

    "nitrite_drivers": {
        "title": "🔧 Gestion des Pilotes - Scanner Avancé",
        "sections": [
            {
                "title": "Scanner de Pilotes - Fonctionnement",
                "content": "Le scanner de pilotes NiTriTe analyse TOUS les pilotes installés sur votre système via PowerShell et WMI. Il détecte automatiquement le type de PC (portable/bureau) et catégorise intelligemment chaque driver."
            },
            {
                "title": "Lancer un Scan Complet",
                "bullets": [
                    "1. Ouvrez 'Scanner Pilotes Avancé' dans le menu",
                    "2. Cliquez sur '🔍 Scanner Maintenant'",
                    "3. Attendez 10-30 secondes (scan PowerShell)",
                    "4. Consultez les résultats par catégorie",
                    "5. Statistiques top 5 affichées automatiquement"
                ]
            },
            {
                "title": "Catégories de Pilotes",
                "bullets": [
                    "🔊 Audio - Cartes son, pilotes Realtek/Creative",
                    "🖥️ Display - Cartes graphiques NVIDIA/AMD/Intel",
                    "🌐 Network - Ethernet, WiFi, Bluetooth",
                    "⚙️ System - Chipset, ACPI, BIOS",
                    "🔌 USB - Contrôleurs USB 2.0/3.0/C",
                    "🖱️ HID - Souris, claviers, touchpads",
                    "💾 Storage - Contrôleurs SATA/NVMe",
                    "📷 Imaging - Webcams, scanners",
                    "🖨️ Printers - Imprimantes"
                ]
            },
            {
                "title": "Mettre à Jour un Pilote",
                "content": "Chaque pilote dispose d'un bouton '🔄 MAJ' pour mise à jour automatique:"
            },
            {
                "bullets": [
                    "1. Cliquez sur '🔄 MAJ' à côté du pilote",
                    "2. Confirmez la mise à jour",
                    "3. NiTriTe recherche via Windows Update",
                    "4. Téléchargement et installation automatiques",
                    "5. Redémarrage si nécessaire",
                    "6. Notification de succès/échec"
                ]
            },
            {
                "title": "Sauvegarde de Pilotes",
                "content": "Sauvegardez TOUS vos pilotes avant une réinstallation:"
            },
            {
                "bullets": [
                    "1. Cliquez sur '💾 Sauvegarder Pilotes'",
                    "2. Choisissez le dossier de destination",
                    "3. NiTriTe exporte tous les .inf et fichiers",
                    "4. Sauvegarde horodatée créée",
                    "5. Utilisez '♻️ Restaurer' pour réinstaller"
                ]
            },
            {
                "title": "Restauration de Pilotes",
                "bullets": [
                    "1. Après réinstallation Windows, ouvrez NiTriTe",
                    "2. Cliquez sur '♻️ Restaurer Sauvegarde'",
                    "3. Sélectionnez la sauvegarde (date)",
                    "4. Instructions affichées pour restauration manuelle via Gestionnaire de périphériques",
                    "5. Ou utilisez pnputil en ligne de commande"
                ]
            },
            {
                "title": "Export de la Liste",
                "bullets": [
                    "Cliquez sur '📋 Exporter Liste'",
                    "Format HTML généré avec tous les drivers",
                    "Informations: Nom, Fabricant, Version, Date",
                    "Utile pour documentation ou audit",
                    "Ouvrez avec navigateur pour consultation"
                ]
            },
            {
                "warning": "⚠️ Sauvegardez TOUJOURS vos pilotes avant une mise à jour majeure de Windows ou une réinstallation. Certains pilotes spécifiques (OEM) ne sont disponibles que sur le site du fabricant."
            },
            {
                "info": "💡 Les pilotes GPU (NVIDIA/AMD) ne sont PAS sauvegardés car ils sont trop volumineux. Téléchargez-les depuis le site officiel."
            }
        ]
    },

    "nitrite_troubleshoot": {
        "title": "🔍 Dépannage NiTriTe - Solutions aux Problèmes",
        "sections": [
            {
                "title": "Problèmes Courants & Solutions",
                "content": "Cette section regroupe les problèmes fréquents rencontrés avec NiTriTe et leurs solutions."
            },
            {
                "title": "Winget ne fonctionne pas",
                "bullets": [
                    "Symptôme: Erreur 'winget n'est pas reconnu comme commande'",
                    "Cause: Winget n'est pas installé ou désactivé",
                    "Solution 1: Installez App Installer depuis le Microsoft Store",
                    "Solution 2: Téléchargez winget depuis GitHub (microsoft/winget-cli)",
                    "Solution 3: Vérifiez PATH système (winget.exe dans AppData)",
                    "Test: Ouvrez PowerShell > tapez 'winget --version'"
                ]
            },
            {
                "title": "Master Install bloque/crash",
                "bullets": [
                    "Symptôme: Installation s'arrête, fenêtre se ferme",
                    "Cause 1: Manque de droits administrateur",
                    "Solution: Lancez NiTriTe en 'Exécuter en tant qu'administrateur'",
                    "Cause 2: Antivirus bloque l'installation",
                    "Solution: Ajoutez NiTriTe aux exceptions",
                    "Cause 3: Connexion Internet instable",
                    "Solution: Vérifiez votre connexion, utilisez Ethernet si possible"
                ]
            },
            {
                "title": "Scanner de pilotes ne détecte rien",
                "bullets": [
                    "Symptôme: '0 pilotes trouvés' après scan",
                    "Cause: PowerShell bloqué par stratégie d'exécution",
                    "Solution: Ouvrez PowerShell Admin > tapez:",
                    "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser",
                    "Relancez le scan dans NiTriTe"
                ]
            },
            {
                "title": "Page Activation ne détecte pas Windows activé",
                "bullets": [
                    "Symptôme: Windows affiché 'non activé' alors qu'il l'est",
                    "Cause: Timeout WMI trop court",
                    "Solution: Le timeout a été augmenté à 20s dans V20.1+",
                    "Workaround: Vérifiez manuellement > Paramètres > Activation",
                    "Si vraiment activé, ignorez l'erreur NiTriTe"
                ]
            },
            {
                "title": "Applications portables ne se téléchargent pas",
                "bullets": [
                    "Symptôme: Erreur téléchargement ou timeout",
                    "Cause 1: Pare-feu Windows bloque",
                    "Solution: Autorisez NiTriTe dans pare-feu Windows",
                    "Cause 2: Proxy/VPN interfère",
                    "Solution: Désactivez temporairement proxy/VPN",
                    "Cause 3: Site PortableApps.com hors ligne",
                    "Solution: Réessayez plus tard"
                ]
            },
            {
                "title": "Interface graphique floue/pixelisée",
                "bullets": [
                    "Symptôme: Texte flou sur écran haute résolution",
                    "Cause: Mise à l'échelle Windows incorrecte",
                    "Solution 1: Clic droit sur NiTriTe.exe > Propriétés > Compatibilité",
                    "Cochez 'Remplacer le comportement PPP élevé'",
                    "Solution 2: Ajustez mise à l'échelle Windows à 100% ou 125%"
                ]
            },
            {
                "title": "Impossible de créer un pack personnalisé",
                "bullets": [
                    "Symptôme: Bouton 'Sauvegarder' ne fonctionne pas",
                    "Cause: Dossier de configuration verrouillé",
                    "Solution: Fermez NiTriTe > Supprimez data/config/*.lock",
                    "Relancez NiTriTe en administrateur"
                ]
            },
            {
                "title": "Logs d'erreur inexistants",
                "bullets": [
                    "Problème: Impossible de trouver les logs",
                    "Solution: Les logs sont dans:",
                    "• C:\\Users\\[User]\\Downloads\\Nitrite-V20.0\\data\\logs\\",
                    "• Fichiers .txt/.html datés",
                    "• Consultez-les pour diagnostic détaillé"
                ]
            },
            {
                "warning": "⚠️ Si aucune solution ne fonctionne, créez un ticket sur GitHub avec les logs complets et la description du problème."
            },
            {
                "info": "💡 Astuce: 90% des problèmes sont résolus en lançant NiTriTe en tant qu'administrateur et en vérifiant que Winget est installé."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 2: WINDOWS 10/11 + DÉPANNAGE (15 guides)
    # =========================================================================

    "w11_intro": {
        "title": "🪟 Introduction à Windows 11",
        "sections": [
            {
                "title": "Qu'est-ce que Windows 11?",
                "content": "Windows 11 est la dernière version du système d'exploitation de Microsoft, lancée en octobre 2021. Il apporte une interface modernisée, des performances améliorées et de nouvelles fonctionnalités centrées sur la productivité et le gaming."
            },
            {
                "title": "Nouveautés par rapport à Windows 10",
                "bullets": [
                    "Interface repensée: Menu Démarrer centré, coins arrondis, animations fluides",
                    "Widgets: Panneau d'informations personnalisables (météo, news, calendrier)",
                    "Snap Layouts: Disposition rapide des fenêtres en multi-tâches",
                    "DirectStorage: Chargement ultra-rapide des jeux (GPU décompression)",
                    "Auto HDR: Amélioration graphique automatique des jeux",
                    "Android Apps: Support des applications Android via Amazon AppStore",
                    "Microsoft Teams intégré: Communication unifiée dans la barre des tâches",
                    "Performance améliorée: Meilleure gestion mémoire et économie batterie"
                ]
            },
            {
                "title": "Configuration Requise",
                "bullets": [
                    "Processeur: 64-bit 1 GHz+ avec 2+ cœurs (liste compatibilité stricte)",
                    "RAM: 4 GB minimum (8 GB recommandé)",
                    "Stockage: 64 GB minimum",
                    "Firmware: UEFI, Secure Boot capable",
                    "TPM: Trusted Platform Module 2.0 (obligatoire)",
                    "Carte graphique: Compatible DirectX 12 / WDDM 2.x",
                    "Écran: HD 720p (1280x720) minimum, 9 pouces+",
                    "Connexion Internet: Requise pour l'installation (Edition Home)"
                ]
            },
            {
                "title": "Éditions de Windows 11",
                "bullets": [
                    "Windows 11 Home: Usage personnel, fonctionnalités de base",
                    "Windows 11 Pro: Professionnels, gestion réseau, BitLocker, Hyper-V",
                    "Windows 11 Pro for Workstations: Puissance maximale (serveurs, rendu 3D)",
                    "Windows 11 Enterprise: Grandes entreprises, sécurité avancée",
                    "Windows 11 Education: Établissements scolaires, version Enterprise simplifiée"
                ]
            },
            {
                "title": "Dois-je passer à Windows 11?",
                "content": "Avantages:\n• Interface moderne et épurée\n• Meilleures performances gaming (DirectStorage, Auto HDR)\n• Productivité améliorée (Snap Layouts, Virtual Desktops)\n• Support à long terme (mises à jour jusqu'en 2031+)\n• Optimisations pour PC récents\n\nInconvénients:\n• Compatibilité matérielle stricte (TPM 2.0, CPU récent)\n• Changements d'interface déstabilisants (menu Démarrer, clic droit)\n• Quelques bugs sur nouveaux PC (résolu progressivement)\n• Télémétrie plus invasive (configurable)"
            },
            {
                "warning": "⚠️ Important: Vérifiez la compatibilité de votre PC avec l'outil 'PC Health Check' de Microsoft avant de mettre à jour. Un PC incompatible ne pourra pas installer Windows 11 officiellement."
            },
            {
                "info": "💡 Astuce: Si votre PC est incompatible mais puissant (ex: CPU 7ème gen Intel), il existe des méthodes non-officielles pour contourner les restrictions TPM/CPU. Utilisez à vos risques, mais c'est possible via Rufus ou modification du registre."
            }
        ]
    },

    "w11_install": {
        "title": "💿 Installation & Configuration de Windows 11",
        "sections": [
            {
                "title": "Prérequis avant Installation",
                "bullets": [
                    "Vérifier compatibilité: Téléchargez 'PC Health Check' de Microsoft",
                    "Sauvegarder vos données: Disque externe ou cloud (OneDrive, Google Drive)",
                    "Récupérer clé de licence: Utilisez ProduKey ou Speccy",
                    "Lister vos programmes: Pour réinstallation après (utilisez NiTriTe!)",
                    "Télécharger drivers: Réseau, chipset, GPU (au cas où)",
                    "Créer point de restauration: Si mise à jour (pas installation propre)"
                ]
            },
            {
                "title": "Méthode 1: Mise à Jour depuis Windows 10",
                "bullets": [
                    "Étape 1: Ouvrez Windows Update (Paramètres > Mise à jour)",
                    "Étape 2: Cliquez sur 'Rechercher des mises à jour'",
                    "Étape 3: Si éligible, 'Windows 11 est prêt' apparaît",
                    "Étape 4: Cliquez sur 'Télécharger et installer'",
                    "Étape 5: Le téléchargement démarre (4-6 GB)",
                    "Étape 6: Installation automatique au redémarrage (30-60 minutes)",
                    "Étape 7: Configuration initiale (compte Microsoft, confidentialité)",
                    "Note: Vos fichiers et programmes sont conservés"
                ]
            },
            {
                "title": "Méthode 2: Installation Propre (Clean Install)",
                "bullets": [
                    "Étape 1: Téléchargez l'outil de création de média Windows 11",
                    "Étape 2: Créez une clé USB bootable (8 GB minimum) avec Rufus ou l'outil Microsoft",
                    "Étape 3: Branchez la clé USB et redémarrez le PC",
                    "Étape 4: Accédez au BIOS/UEFI (F2, F12, Del selon fabricant)",
                    "Étape 5: Configurez le boot sur USB en priorité",
                    "Étape 6: Démarrez sur la clé USB",
                    "Étape 7: Cliquez sur 'Installer maintenant'",
                    "Étape 8: Entrez votre clé de licence (ou 'Je n'ai pas de clé')",
                    "Étape 9: Choisissez 'Installation personnalisée'",
                    "Étape 10: Formatez la partition Windows (ATTENTION: Efface tout!)",
                    "Étape 11: Sélectionnez la partition et cliquez 'Suivant'",
                    "Étape 12: Installation (20-40 minutes)",
                    "Étape 13: Configuration OOBE (compte, région, confidentialité)"
                ]
            },
            {
                "title": "Méthode 3: Contourner Restrictions TPM/CPU",
                "bullets": [
                    "Si votre PC est refusé à cause de TPM 2.0 ou CPU non listé:",
                    "Méthode Rufus (Recommandée):",
                    "1. Téléchargez Rufus 3.19+",
                    "2. Créez une clé USB bootable avec ISO Windows 11",
                    "3. Cochez 'Remove TPM requirement' et 'Remove Secure Boot requirement'",
                    "4. Créez la clé et installez normalement",
                    "",
                    "Méthode Registre (Pendant installation):",
                    "1. Quand bloqué, appuyez sur Shift+F10 (ouvre CMD)",
                    "2. Tapez: regedit",
                    "3. Allez à HKEY_LOCAL_MACHINE\\SYSTEM\\Setup",
                    "4. Créez clé: LabConfig",
                    "5. Créez DWORD: BypassTPMCheck = 1",
                    "6. Créez DWORD: BypassSecureBootCheck = 1",
                    "7. Fermez regedit et continuez l'installation"
                ]
            },
            {
                "title": "Configuration Post-Installation",
                "bullets": [
                    "Activer Windows: Utilisez NiTriTe > Activation (MAS scripts)",
                    "Installer drivers: NiTriTe > Scanner Pilotes ou site fabricant",
                    "Mettre à jour Windows: Paramètres > Windows Update (toutes les mises à jour)",
                    "Installer programmes essentiels: NiTriTe > Master Install",
                    "Configurer confidentialité: Désactiver télémétrie (voir guide W11 Privacy)",
                    "Optimiser performances: Désactiver animations, effets (voir guide W11 Optimize)",
                    "Créer point de restauration: Protection du système > Créer",
                    "Configurer sauvegarde: Windows Backup ou logiciel tiers (Veeam, Macrium)"
                ]
            },
            {
                "title": "Optimisations Immédiates Recommandées",
                "bullets": [
                    "Désactiver Widgets si non utilisés: Barre des tâches > Widgets (Désactiver)",
                    "Centrer ou aligner à gauche le menu Démarrer: Personnalisation > Barre des tâches",
                    "Configurer Snap Layouts: Personnalisation > Multitâche",
                    "Désactiver Microsoft Teams auto-start: Paramètres > Applications > Démarrage",
                    "Nettoyer bloatware: Désinstaller Candy Crush, Solitaire Collection, etc.",
                    "Désactiver indexation si SSD: Services > Windows Search (Désactiver)",
                    "Activer mode performances: Paramètres > Alimentation > Meilleures performances"
                ]
            },
            {
                "title": "Installation de Windows 11 sur PC Non-Supporté",
                "content": "Microsoft ne bloque PAS les mises à jour de sécurité sur PC non-supportés. Vous pouvez utiliser Windows 11 même sur CPU de 6ème/7ème génération Intel sans problème. Les seuls risques:\n\n• Pas de support officiel Microsoft (mais communauté très active)\n• Mises à jour fonctionnelles possibles problèmes (rares)\n• Performances légèrement réduites sur vieux CPU (< 10%)\n\nConclusion: Si votre PC a 8 GB RAM et SSD, Windows 11 fonctionnera bien même sans TPM 2.0."
            },
            {
                "warning": "⚠️ Installation propre: Sauvegardez TOUT avant de formater! Fichiers personnels, favoris navigateurs, sauvegardes emails, clés de licences. Une fois formaté, impossible de récupérer."
            },
            {
                "info": "💡 Astuce: Pour une installation ultra-rapide de tous vos programmes après Windows 11, utilisez NiTriTe Master Install avec un pack personnalisé créé à l'avance. Gain de temps: 2-3 heures → 30 minutes!"
            },
            {
                "title": "Dépannage Installation",
                "bullets": [
                    "Erreur: 'Ce PC ne peut pas exécuter Windows 11'",
                    "→ Solution: Utilisez Rufus ou méthode registre pour contourner TPM",
                    "",
                    "Erreur: Blocage à 0% pendant installation",
                    "→ Solution: Débranchez périphériques USB (sauf souris/clavier), désactivez antivirus",
                    "",
                    "Erreur: Écran noir après installation",
                    "→ Solution: Drivers graphiques manquants, démarrez en mode sans échec et installez drivers",
                    "",
                    "Erreur: Pas de connexion Internet après installation",
                    "→ Solution: Drivers réseau manquants, installez depuis clé USB ou smartphone USB tethering"
                ]
            }
        ]
    },

    "w11_optimize": {
        "title": "⚡ Optimisation Performance Windows 11",
        "sections": [
            {
                "title": "Désactiver la Télémétrie",
                "content": "Windows 11 envoie beaucoup de données à Microsoft. Réduisez la collecte:"
            },
            {
                "bullets": [
                    "Paramètres > Confidentialité et sécurité > Diagnostics et commentaires",
                    "Définir niveau diagnostic sur 'Données de diagnostic nécessaires'",
                    "Désactiver 'Améliorer l'écriture manuscrite et la saisie'",
                    "Désactiver 'Personnaliser les expériences'",
                    "Désactiver 'Historique des activités'"
                ]
            },
            {
                "title": "Désactiver les Services Inutiles",
                "code": "# Ouvrir Services.msc\nservices.msc\n\n# Désactiver (Type de démarrage > Désactivé):\n- Xbox Live Auth Manager\n- Xbox Live Game Save\n- Xbox Live Networking Service\n- dmwappushservice (Routage de messages Push WAP)\n- DiagTrack (Télémétrie)\n- SysMain (Superfetch - si SSD)\n- Windows Search (si vous n'utilisez pas la recherche)"
            },
            {
                "title": "Optimisations Visuelles",
                "bullets": [
                    "Paramètres > Système > Affichage > Graphismes > Modifier paramètres graphiques par défaut",
                    "Activer 'Planification GPU à accélération matérielle' (gaming)",
                    "Paramètres > Accessibilité > Effets visuels > Désactiver animations",
                    "Panneau de configuration > Système > Paramètres système avancés > Performances",
                    "Ajuster pour de meilleures performances (désactive effets)"
                ]
            },
            {
                "title": "Nettoyer le Démarrage",
                "bullets": [
                    "Gestionnaire des tâches (Ctrl + Shift + Esc) > Démarrage",
                    "Désactiver les programmes inutiles au démarrage",
                    "Garder uniquement: Antivirus, pilotes essentiels",
                    "Supprimer: Skype, OneDrive (si non utilisé), Teams, etc."
                ]
            },
            {
                "title": "Optimiser le Stockage",
                "bullets": [
                    "Paramètres > Système > Stockage",
                    "Activer 'Assistant stockage' pour nettoyage auto",
                    "Nettoyer Fichiers temporaires (Nettoyage disque)",
                    "Désinstaller applications Microsoft Store inutiles",
                    "Vider Corbeille et Téléchargements régulièrement"
                ]
            },
            {
                "title": "Désactiver Cortana et Widgets",
                "bullets": [
                    "Barre des tâches > Clic droit > Désactiver 'Widgets'",
                    "Recherche Windows > Désactiver 'Afficher les tendances de recherche'",
                    "Registre: HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search",
                    "Créer DWORD 'AllowCortana' = 0"
                ]
            },
            {
                "title": "Optimisation Gaming",
                "bullets": [
                    "Paramètres > Gaming > Mode Jeu > Activer",
                    "Xbox Game Bar > Désactiver si non utilisée",
                    "NVIDIA/AMD: Activer 'Performance maximale' dans panneau GPU",
                    "Désactiver DVR de jeu Windows (si non utilisé)",
                    "Activer HAGS (Hardware Accelerated GPU Scheduling)"
                ]
            },
            {
                "warning": "⚠️ Ne désactivez PAS Windows Defender sauf si vous avez un autre antivirus. Ne désactivez PAS Windows Update complètement."
            },
            {
                "info": "💡 Pour une optimisation poussée, utilisez les scripts Windows inclus dans NiTriTe (170+ scripts d'optimisation)."
            }
        ]
    },

    "w11_privacy": {
        "title": "🔒 Confidentialité & Sécurité Windows 11",
        "sections": [
            {
                "title": "Paramètres de Confidentialité Essentiels",
                "content": "Windows 11 collecte beaucoup de données. Voici comment limiter:"
            },
            {
                "bullets": [
                    "Paramètres > Confidentialité et sécurité > Général",
                    "Désactiver TOUTES les options (ID de publicité, suivi, suggestions)",
                    "Confidentialité > Voix - Désactiver reconnaissance vocale en ligne",
                    "Confidentialité > Activité - Effacer et désactiver historique",
                    "Confidentialité > Diagnostics - Minimum de données"
                ]
            },
            {
                "title": "Contrôler les Autorisations d'Applications",
                "bullets": [
                    "Confidentialité > Autorisations d'application",
                    "Désactiver pour chaque app inutile:",
                    "• Emplacement",
                    "• Caméra (sauf apps vidéo)",
                    "• Microphone (sauf apps audio/vidéo)",
                    "• Contacts, Calendrier, E-mail",
                    "• Système de fichiers"
                ]
            },
            {
                "title": "Désactiver OneDrive et Synchronisation",
                "code": "# Désactiver OneDrive\n1. Barre des tâches > OneDrive > Paramètres\n2. Compte > Dissocier ce PC\n3. Désinstaller OneDrive:\n   winget uninstall Microsoft.OneDrive\n\n# Ou via Registre (désactivation complète):\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\OneDrive\" /v DisableFileSyncNGSC /t REG_DWORD /d 1 /f"
            },
            {
                "title": "Bloquer les Connexions Télémétrie",
                "content": "Bloquez les serveurs Microsoft de télémétrie via le fichier hosts:"
            },
            {
                "code": "# Éditez C:\\Windows\\System32\\drivers\\etc\\hosts (admin)\n# Ajoutez ces lignes:\n\n0.0.0.0 vortex.data.microsoft.com\n0.0.0.0 vortex-win.data.microsoft.com\n0.0.0.0 telecommand.telemetry.microsoft.com\n0.0.0.0 oca.telemetry.microsoft.com\n0.0.0.0 sqm.telemetry.microsoft.com\n0.0.0.0 watson.telemetry.microsoft.com\n0.0.0.0 redir.metaservices.microsoft.com\n0.0.0.0 choice.microsoft.com\n0.0.0.0 df.telemetry.microsoft.com\n0.0.0.0 reports.wes.df.telemetry.microsoft.com\n0.0.0.0 wes.df.telemetry.microsoft.com\n0.0.0.0 services.wes.df.telemetry.microsoft.com\n0.0.0.0 sqm.df.telemetry.microsoft.com"
            },
            {
                "title": "Pare-feu Windows",
                "bullets": [
                    "Sécurité Windows > Pare-feu et protection réseau",
                    "Paramètres avancés > Règles de trafic sortant",
                    "Bloquer applications non essentielles",
                    "Créer règles pour apps de confiance uniquement",
                    "Activer 'Bloquer toutes les connexions entrantes'"
                ]
            },
            {
                "title": "Chiffrement BitLocker (Pro/Enterprise)",
                "bullets": [
                    "Panneau de configuration > BitLocker",
                    "Activer BitLocker sur disque système",
                    "Choisir mot de passe fort (20+ caractères)",
                    "Sauvegarder clé de récupération (USB ou compte Microsoft)",
                    "Chiffrer disques de données également"
                ]
            },
            {
                "title": "Comptes Utilisateurs",
                "bullets": [
                    "Utilisez un compte LOCAL (pas compte Microsoft) si possible",
                    "Créer compte admin séparé pour maintenance",
                    "Utiliser compte standard pour usage quotidien",
                    "Activer Windows Hello (PIN, empreinte) pour sécurité",
                    "Désactiver questions de sécurité (trop faciles à deviner)"
                ]
            },
            {
                "warning": "⚠️ Le blocage complet de la télémétrie peut empêcher Windows Update de fonctionner correctement. Testez avant de déployer."
            },
            {
                "info": "💡 Utilisez les scripts 'Sécurité' de NiTriTe pour appliquer automatiquement ces paramètres de confidentialité."
            }
        ]
    },

    "w11_troubleshoot": {
        "title": "🔧 Dépannage Windows 11 - Résolution Problèmes",
        "sections": [
            {
                "title": "Windows Update bloqué/échoue",
                "bullets": [
                    "Symptôme: Mise à jour reste à 0% ou erreur 0x80070002",
                    "Solution 1: Windows Update Troubleshooter",
                    "  Paramètres > Système > Résolution des problèmes > Windows Update",
                    "Solution 2: Réinitialiser composants Windows Update:",
                    "  cmd admin > net stop wuauserv && net stop bits",
                    "  ren C:\\Windows\\SoftwareDistribution SoftwareDistribution.old",
                    "  net start wuauserv && net start bits",
                    "Solution 3: Outil Microsoft (Windows Update Assistant)"
                ]
            },
            {
                "title": "Menu Démarrer ne s'ouvre pas",
                "bullets": [
                    "Symptôme: Clic sur Démarrer sans réaction",
                    "Solution 1: Redémarrer Explorateur Windows",
                    "  Gestionnaire des tâches > Processus > Explorateur Windows > Redémarrer",
                    "Solution 2: PowerShell admin:",
                    "  Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register '$($_.InstallLocation)\\AppXManifest.xml'}",
                    "Solution 3: Créer nouveau compte utilisateur si persistant"
                ]
            },
            {
                "title": "Écran bleu BSOD fréquent",
                "bullets": [
                    "1. Noter le code d'erreur (ex: SYSTEM_SERVICE_EXCEPTION)",
                    "2. Analyser dump: Panneau > Outils admin > Observateur d'événements",
                    "3. Causes communes:",
                    "   - Pilotes obsolètes/corrompus (GPU surtout) → Mettre à jour",
                    "   - RAM défectueuse → Tester avec MemTest86",
                    "   - SSD/HDD défaillant → Vérifier avec CrystalDiskInfo",
                    "   - Overclocking instable → Reset BIOS defaults",
                    "4. Commande vérification système:",
                    "   sfc /scannow",
                    "   DISM /Online /Cleanup-Image /RestoreHealth"
                ]
            },
            {
                "title": "Performances lentes/lag",
                "bullets": [
                    "Diagnostic: Gestionnaire des tâches > Performance",
                    "Si CPU 100%: Identifier process > Désactiver/désinstaller",
                    "Si RAM saturée: Fermer apps, ajouter RAM si <8GB",
                    "Si Disque 100%: Désactiver Superfetch/Windows Search si SSD",
                    "  services.msc > SysMain > Désactivé",
                    "Si GPU élevé sans raison: Désactiver accélération matérielle navigateur",
                    "Nettoyer démarrage: msconfig > Démarrage sélectif"
                ]
            },
            {
                "title": "WiFi ne se connecte pas",
                "bullets": [
                    "1. Redémarrer routeur ET PC",
                    "2. Oublier réseau et reconnecter",
                    "3. Réinitialiser pile réseau:",
                    "   cmd admin > netsh winsock reset",
                    "   netsh int ip reset",
                    "   ipconfig /release && ipconfig /renew",
                    "   ipconfig /flushdns",
                    "4. Mettre à jour pilote WiFi (Gestionnaire périphériques)",
                    "5. Désactiver IPv6 si problème persiste"
                ]
            },
            {
                "title": "Applications ne s'installent pas (Microsoft Store)",
                "bullets": [
                    "Symptôme: Erreur 0x80073CF9 ou impossible de télécharger",
                    "Solution 1: Réinitialiser cache Store:",
                    "  Exécuter > wsreset.exe",
                    "Solution 2: PowerShell admin:",
                    "  Get-AppxPackage *store* | Remove-AppxPackage",
                    "  Add-AppxPackage -register 'C:\\Program Files\\WindowsApps\\*Store*\\AppxManifest.xml' -DisableDevelopmentMode",
                    "Solution 3: Vérifier date/heure système (doit être correcte)"
                ]
            },
            {
                "title": "Son ne fonctionne pas",
                "bullets": [
                    "1. Vérifier icône son (muté?)",
                    "2. Paramètres > Son > Sélectionner bon périphérique sortie",
                    "3. Gestionnaire périphériques > Contrôleurs audio > Mettre à jour pilote",
                    "4. Services.msc > Windows Audio > Démarrer (Automatique)",
                    "5. Réinstaller pilote audio (Realtek/Conexant selon fabricant)"
                ]
            },
            {
                "title": "Activation Windows expire/erreur",
                "bullets": [
                    "Symptôme: Filigrane 'Activer Windows' en bas à droite",
                    "Solution 1: Paramètres > Activation > Résoudre les problèmes",
                    "Solution 2: Si changement matériel, réactiver avec clé",
                    "Solution 3: Utiliser NiTriTe > Page Activation > MAS (HWID permanent)",
                    "Solution 4: Contacter support Microsoft si licence légitime"
                ]
            },
            {
                "warning": "⚠️ Avant toute manipulation registre ou système, créez un point de restauration système!"
            },
            {
                "info": "💡 Pour diagnostics avancés, utilisez les outils NiTriTe: Scanner Pilotes, Rapports Système, Logs détaillés."
            }
        ]
    },

    "w10_intro": {
        "title": "🪟 Introduction à Windows 10",
        "sections": [
            {
                "title": "Qu'est-ce que Windows 10?",
                "content": "Windows 10 est le système d'exploitation phare de Microsoft lancé en juillet 2015. C'est le successeur de Windows 8.1 et a apporté le retour du menu Démarrer, des bureaux virtuels et des améliorations majeures de performance. Toujours largement utilisé en 2025 malgré Windows 11."
            },
            {
                "title": "Pourquoi Windows 10 reste pertinent en 2025?",
                "bullets": [
                    "Stabilité éprouvée: 10 ans de mises à jour et corrections de bugs",
                    "Compatibilité maximale: Supporte quasi tous les PC depuis 2010",
                    "Pas de restrictions matérielles: Pas besoin de TPM 2.0",
                    "Interface familière: Menu Démarrer classique, barre des tâches traditionnelle",
                    "Support étendu: Mises à jour de sécurité jusqu'en octobre 2025",
                    "Gaming performant: DirectX 12, Game Mode, Xbox Game Bar",
                    "Moins de télémétrie: Configurable plus facilement que W11",
                    "Ressources réduites: Fonctionne bien sur PC modestes (4 GB RAM)"
                ]
            },
            {
                "title": "Configuration Requise (Minimale/Recommandée)",
                "bullets": [
                    "Processeur: 1 GHz ou plus rapide / Intel Core i3+ ou AMD Ryzen 3+",
                    "RAM: 1 GB (32-bit) ou 2 GB (64-bit) / 8 GB recommandé",
                    "Espace disque: 16 GB (32-bit) ou 32 GB (64-bit) / 256 GB SSD recommandé",
                    "Carte graphique: DirectX 9 / DirectX 12 pour gaming",
                    "Écran: 800x600 / 1920x1080 Full HD",
                    "Note: Aucun TPM requis, fonctionne sur quasi tout PC"
                ]
            },
            {
                "title": "Éditions de Windows 10",
                "bullets": [
                    "Windows 10 Home: Usage personnel, toutes fonctionnalités de base",
                    "Windows 10 Pro: Professionnels, BitLocker, domaines, Hyper-V, bureau à distance",
                    "Windows 10 Pro for Workstations: PC haute performance, serveurs fichiers",
                    "Windows 10 Enterprise: Grandes entreprises, gestion centralisée, sécurité avancée",
                    "Windows 10 Education: Écoles et universités, version Enterprise simplifiée",
                    "Windows 10 LTSC: Long-Term Servicing Channel, sans bloatware, support 10 ans"
                ]
            },
            {
                "title": "Windows 10 vs Windows 11: Que choisir?",
                "content": "Choisissez Windows 10 si:\n• Votre PC n'a pas de TPM 2.0 ou CPU récent\n• Vous préférez une interface classique et stable\n• Vous utilisez des logiciels anciens (meilleure compatibilité)\n• Vous voulez moins de télémétrie\n• Vous avez un PC modeste (< 8 GB RAM)\n\nChoisissez Windows 11 si:\n• PC récent compatible (2018+)\n• Vous voulez les dernières fonctionnalités (DirectStorage, Auto HDR)\n• Interface moderne vous plait\n• Support long terme (2031+ vs 2025 pour W10)"
            },
            {
                "title": "Versions de Windows 10",
                "bullets": [
                    "Version 1507 (RTM): Juillet 2015, sortie initiale",
                    "Version 1909 (November 2019 Update): Dernière version 32-bit",
                    "Version 2004 (May 2020 Update): Améliorations WSL2, Virtual Desktops",
                    "Version 21H2 (November 2021 Update): Dernière version 'feature update'",
                    "Version 22H2 (October 2022 Update): Dernière version finale, support jusqu'en octobre 2025",
                    "Note: Utilisez toujours la version 22H2 pour un support maximal"
                ]
            },
            {
                "warning": "⚠️ Fin de support: Windows 10 ne recevra plus de mises à jour de sécurité après octobre 2025. Prévoyez une migration vers Windows 11 ou Linux avant cette date si vous voulez rester sécurisé."
            },
            {
                "info": "💡 Astuce: Windows 10 LTSC (Long-Term Servicing Channel) est une version ultra-stable sans bloatware (pas de Cortana, Store, Edge) avec support de 10 ans. Parfaite pour usage professionnel ou gaming pur."
            }
        ]
    },

    "w10_install": {
        "title": "💿 Installation & Activation de Windows 10",
        "sections": [
            {
                "title": "Prérequis avant Installation",
                "bullets": [
                    "Sauvegarder données: Disque externe, cloud, clé USB (TOUT vos fichiers importants)",
                    "Récupérer clé de licence: ProduKey, Speccy ou autocollant PC",
                    "Télécharger drivers: Réseau (LAN/Wi-Fi), chipset, GPU depuis site fabricant",
                    "Lister programmes installés: Pour réinstallation (ou utilisez NiTriTe Master Install!)",
                    "Vérifier BIOS/UEFI: Mode Legacy ou UEFI selon votre PC",
                    "Préparer clé USB 8 GB: Pour création du média d'installation"
                ]
            },
            {
                "title": "Télécharger Windows 10 ISO Officiel",
                "bullets": [
                    "Méthode 1 - Media Creation Tool (Recommandée):",
                    "1. Allez sur microsoft.com/fr-fr/software-download/windows10",
                    "2. Cliquez 'Télécharger l'outil maintenant'",
                    "3. Lancez MediaCreationTool.exe en admin",
                    "4. Choisissez 'Créer un média d'installation'",
                    "5. Sélectionnez langue (Français), édition (Windows 10), architecture (64-bit)",
                    "6. Choisissez 'Clé USB' ou 'Fichier ISO'",
                    "7. Attendez le téléchargement (4-5 GB) et création",
                    "",
                    "Méthode 2 - ISO Direct:",
                    "1. Utilisez Rufus pour télécharger ISO directement",
                    "2. Ou visitez uup.rg-adguard.net pour ISO officiels"
                ]
            },
            {
                "title": "Installation Propre (Clean Install)",
                "bullets": [
                    "Étape 1: Insérez la clé USB bootable et redémarrez le PC",
                    "Étape 2: Appuyez sur F2/F12/Del/Esc (selon fabricant) pour BIOS",
                    "Étape 3: Boot Priority > Placez USB en premier",
                    "Étape 4: Sauvegardez et redémarrez (F10 généralement)",
                    "Étape 5: Appuyez sur une touche quand 'Press any key to boot from USB' apparaît",
                    "Étape 6: Sélectionnez langue, format heure, clavier > Suivant",
                    "Étape 7: Cliquez 'Installer maintenant'",
                    "Étape 8: Entrez clé de licence ou cliquez 'Je n'ai pas de clé produit'",
                    "Étape 9: Sélectionnez édition (Home, Pro, etc.)",
                    "Étape 10: Acceptez conditions de licence",
                    "Étape 11: Choisissez 'Personnalisée: installer Windows uniquement'",
                    "Étape 12: Sélectionnez partition système et cliquez 'Formater' (ATTENTION: Efface tout!)",
                    "Étape 13: Sélectionnez partition formatée et cliquez 'Suivant'",
                    "Étape 14: Installation démarre (15-30 minutes selon PC)",
                    "Étape 15: PC redémarre plusieurs fois (automatique)",
                    "Étape 16: Configuration OOBE (région, clavier, compte, confidentialité)"
                ]
            },
            {
                "title": "Mise à Jour depuis Windows 7/8/8.1",
                "bullets": [
                    "Note: La migration gratuite Windows 7→10 a officiellement expiré mais fonctionne toujours (2025)",
                    "Étape 1: Téléchargez Media Creation Tool",
                    "Étape 2: Lancez-le et choisissez 'Mettre à niveau ce PC maintenant'",
                    "Étape 3: Téléchargement automatique de Windows 10 (4-5 GB)",
                    "Étape 4: Installation démarre (conserve fichiers et programmes)",
                    "Étape 5: Redémarrages automatiques (30-60 minutes total)",
                    "Étape 6: Windows 10 activé automatiquement si Windows 7/8 était activé",
                    "Note: Vos fichiers et programmes sont conservés (mais sauvegardez quand même!)"
                ]
            },
            {
                "title": "Configuration Post-Installation",
                "bullets": [
                    "Priorité 1 - Drivers:",
                    "• Utilisez NiTriTe > Scanner Pilotes pour auto-détection",
                    "• Ou téléchargez depuis: Chipset, GPU, Audio, LAN/Wi-Fi, USB (site fabricant)",
                    "• Redémarrez après installation drivers",
                    "",
                    "Priorité 2 - Mises à jour Windows:",
                    "• Paramètres > Mise à jour et sécurité > Windows Update",
                    "• Cliquez 'Rechercher des mises à jour' plusieurs fois (peut prendre 1-2h)",
                    "• Installez TOUTES les mises à jour jusqu'à version 22H2",
                    "",
                    "Priorité 3 - Activation:",
                    "• Si clé valide: Paramètres > Mise à jour > Activation > Modifier clé",
                    "• Sinon: Utilisez NiTriTe > Activation > MAS Scripts (HWID permanent)",
                    "",
                    "Priorité 4 - Programmes:",
                    "• NiTriTe > Master Install > Pack Gaming/Bureautique/Dev",
                    "• Gain de temps massif vs installation manuelle"
                ]
            },
            {
                "title": "Activer Windows 10 (MAS - Microsoft Activation Scripts)",
                "bullets": [
                    "Méthode recommandée par NiTriTe (100% sûre, open-source):",
                    "1. Ouvrez NiTriTe > Page Activation",
                    "2. Cliquez sur 'Activer Windows' > HWID (recommandé)",
                    "3. Le terminal s'ouvre avec script MAS",
                    "4. Tapez '1' pour HWID Activation (activation permanente)",
                    "5. Attendez 10-30 secondes",
                    "6. Windows activé à vie! Même après réinstallation",
                    "",
                    "Alternative manuelle:",
                    "1. Allez sur massgrave.dev",
                    "2. Téléchargez le script MAS",
                    "3. Clic droit > Exécuter en tant qu'administrateur",
                    "4. Choisissez option HWID"
                ]
            },
            {
                "title": "Optimisations Immédiates Post-Installation",
                "bullets": [
                    "Désactiver Cortana: Barre de recherche > Paramètres Cortana > Désactivé",
                    "Désinstaller bloatware: Applications > Candy Crush, Xbox, Solitaire, etc.",
                    "Désactiver animations: Paramètres système > À propos > Paramètres système avancés > Performances > Ajuster pour les meilleures performances",
                    "Activer Game Mode: Paramètres > Jeux > Mode Jeu (pour gamers)",
                    "Désactiver télémétrie: Utilisez scripts NiTriTe > Scripts Windows > Désactiver télémétrie",
                    "Configurer Windows Update: Paramètres > Mise à jour > Options avancées > Désactiver redémarrages automatiques",
                    "Créer point de restauration: Panneau > Système > Protection système > Créer"
                ]
            },
            {
                "warning": "⚠️ Installation propre: Tout sera effacé! Triple-vérifiez que vous avez sauvegardé: Photos, Documents, Musique, Vidéos, Favoris navigateur, Sauvegardes emails, Clés de licences logiciels."
            },
            {
                "info": "💡 Astuce Gaming: Après installation Windows 10, utilisez NiTriTe > Scripts Windows > Optimisation Gaming pour désactiver DVR Xbox, désactiver Fullscreen Optimizations, et tweaker timer resolution. Gain FPS: +5-15%!"
            },
            {
                "title": "Dépannage Installation",
                "bullets": [
                    "Erreur: 'Windows ne peut pas être installé sur ce disque'",
                    "→ Solution: Convertir disque en GPT (si UEFI) ou MBR (si Legacy) avec diskpart",
                    "",
                    "Erreur: 'Aucun pilote de périphérique n'a été trouvé'",
                    "→ Solution: Drivers USB 3.0 manquants, utilisez port USB 2.0 ou intégrez drivers",
                    "",
                    "Erreur: Écran noir après installation",
                    "→ Solution: Mode sans échec (F8) > Installer drivers GPU",
                    "",
                    "Erreur: Activation impossible",
                    "→ Solution: Utilisez MAS HWID (NiTriTe > Activation) - toujours fonctionnel"
                ]
            }
        ]
    },

    "w10_optimize": {
        "title": "⚡ Optimisation Windows 10",
        "sections": [
            {
                "content": "Consultez le guide Windows 11 Optimisation - les méthodes sont identiques ou très similaires. Différences principales: interface Paramètres légèrement différente, quelques fonctionnalités en moins (Widgets n'existe pas sur W10)."
            },
            {
                "bullets": [
                    "Désactiver Cortana (W10 uniquement)",
                    "Désactiver mise à jour automatique pilotes",
                    "Game DVR moins intrusif que W11",
                    "Pas de Teams intégré dans W10 (avant 22H2)"
                ]
            }
        ]
    },

    "w10_services": {
        "title": "⚙️ Services & Démarrage Windows 10",
        "sections": [
            {
                "title": "Services Sûrs à Désactiver",
                "bullets": [
                    "dmwappushservice - Push messages WAP",
                    "DiagTrack - Télémétrie",
                    "WMPNetworkSvc - Partage média Windows Media Player",
                    "XboxGipSvc, XblAuthManager, XblGameSave - Services Xbox",
                    "RetailDemo - Mode démo magasins",
                    "Fax - Service fax (si pas de fax)",
                    "MapsBroker - Gestionnaire cartes téléchargées",
                    "lfsvc - Service géolocalisation"
                ]
            },
            {
                "title": "Services à NE PAS Désactiver",
                "bullets": [
                    "Windows Update - Mises à jour critiques",
                    "Windows Defender - Protection antivirus",
                    "DNS Client - Résolution noms domaines",
                    "Windows Audio - Son",
                    "Plug and Play - Détection matériel",
                    "RPC - Communication inter-processus",
                    "Windows Firewall - Pare-feu",
                    "Cryptographic Services - Chiffrement/certificats"
                ]
            },
            {
                "code": "# Ouvrir Services\nservices.msc\n\n# Ou PowerShell\nGet-Service | Where-Object {$_.Status -eq 'Running'}\n\n# Désactiver service (exemple DiagTrack)\nSet-Service -Name 'DiagTrack' -StartupType Disabled\nStop-Service -Name 'DiagTrack' -Force"
            }
        ]
    },

    "w10_troubleshoot": {
        "title": "🔧 Résolution Problèmes Windows 10",
        "sections": [
            {
                "content": "La plupart des solutions Windows 11 s'appliquent aussi à Windows 10. Consultez le guide W11 Troubleshoot pour plus de détails."
            },
            {
                "title": "Spécifique Windows 10",
                "bullets": [
                    "Échec mise à jour 2004/20H2: Désinstaller antivirus tiers temporairement",
                    "Loop redémarrage après update: Démarrer en mode sans échec > Désinstaller dernière MAJ",
                    "Edge Legacy vs Edge Chromium: Désinstaller ancienne version",
                    "Cortana CPU élevé: Désactiver complètement via Registre"
                ]
            }
        ]
    },

    # Guides Dépannage Windows (section commune W10/W11)

    "ts_boot": {
        "title": "🔄 Dépannage - Problèmes de Démarrage Windows",
        "sections": [
            {
                "title": "Symptômes Courants",
                "bullets": [
                    "PC ne démarre pas, écran noir",
                    "Boucle de redémarrage infinie",
                    "Message 'Bootmgr is missing'",
                    "Écran bleu au démarrage (BSOD)",
                    "Windows démarre en mode sans échec uniquement",
                    "Logo Windows figé indéfiniment"
                ]
            },
            {
                "title": "Solution 1: Réparation Automatique (Windows RE)",
                "bullets": [
                    "Étape 1: Créez une clé USB Windows 10/11 bootable (autre PC)",
                    "Étape 2: Démarrez sur la clé USB (F2/F12/Del au boot)",
                    "Étape 3: Cliquez 'Réparer l'ordinateur' (pas Installer)",
                    "Étape 4: Dépannage > Options avancées",
                    "Étape 5: Choisissez:",
                    "  • Réparation du démarrage (automatique, essayez d'abord)",
                    "  • Restauration système (si point de restauration existe)",
                    "  • Invite de commandes (pour solutions manuelles ci-dessous)"
                ]
            },
            {
                "title": "Solution 2: Réparer BCD et MBR (CMD)",
                "bullets": [
                    "Depuis Windows RE > Invite de commandes:",
                    "1. Réparer le MBR:",
                    "   bootrec /fixmbr",
                    "   bootrec /fixboot",
                    "2. Reconstruire BCD:",
                    "   bootrec /rebuildbcd",
                    "3. Si erreur 'Element not found':",
                    "   bcdedit /export C:\\bcdbackup",
                    "   attrib C:\\boot\\bcd -h -r -s",
                    "   ren C:\\boot\\bcd bcd.old",
                    "   bootrec /rebuildbcd",
                    "4. Redémarrez"
                ]
            },
            {
                "title": "Solution 3: Vérifier et Réparer Partition Système",
                "bullets": [
                    "Dans CMD (Windows RE):",
                    "1. Lister disques: diskpart > list disk",
                    "2. Sélectionner disque système: select disk 0",
                    "3. Lister partitions: list partition",
                    "4. Sélectionner partition système (100-500MB): select partition 1",
                    "5. Marquer active: active",
                    "6. Assigner lettre: assign letter=Z",
                    "7. Réparer boot: bcdboot C:\\Windows /s Z: /f UEFI",
                    "8. Exit > Redémarrer"
                ]
            },
            {
                "title": "Solution 4: Mode Sans Échec",
                "bullets": [
                    "Forcer mode sans échec si Windows boucle:",
                    "Méthode 1 - Interruption forcée (3x):",
                    "1. Allumez PC, attendez logo Windows",
                    "2. Appuyez LONGUEMENT sur bouton Power (10s) pour éteindre",
                    "3. Répétez 3 fois total",
                    "4. Au 4ème démarrage, Windows RE charge automatiquement",
                    "",
                    "Méthode 2 - Clé USB:",
                    "1. Démarrez sur clé USB Windows",
                    "2. Réparer > Dépannage > Options avancées",
                    "3. Paramètres de démarrage > Redémarrer",
                    "4. Appuyez F4 (Mode sans échec) ou F5 (avec réseau)"
                ]
            },
            {
                "title": "Solution 5: Désactiver Démarrage Rapide",
                "bullets": [
                    "Si Windows démarre mais freeze au logo:",
                    "1. Entrez en mode sans échec (F8 ou méthode ci-dessus)",
                    "2. Panneau de configuration > Options d'alimentation",
                    "3. Choisir action boutons > Modifier paramètres indisponibles",
                    "4. Décochez 'Activer le démarrage rapide'",
                    "5. Redémarrez normalement"
                ]
            },
            {
                "warning": "⚠️ Si aucune solution ne fonctionne et que vos données sont critiques, NE PAS réinstaller Windows! Utilisez un Linux Live USB pour récupérer vos fichiers d'abord."
            },
            {
                "info": "💡 Astuce Prévention: Créez toujours un point de restauration après installation Windows propre. Activez 'Protection du système' sur disque C:."
            }
        ]
    },

    "ts_bsod": {
        "title": "💙 Dépannage - Écrans Bleus (BSOD)",
        "sections": [
            {
                "title": "Qu'est-ce qu'un BSOD?",
                "content": "Un Blue Screen of Death (BSOD) est une erreur critique Windows qui force un redémarrage immédiat pour protéger les données. Causé par: drivers défectueux (60%), RAM défaillante (20%), overclocking instable (10%), corruption système (10%)."
            },
            {
                "title": "Codes d'Erreur BSOD Fréquents",
                "bullets": [
                    "IRQL_NOT_LESS_OR_EQUAL: Driver défectueux ou RAM",
                    "SYSTEM_SERVICE_EXCEPTION: Driver système corrompu",
                    "PAGE_FAULT_IN_NONPAGED_AREA: RAM défaillante ou driver",
                    "KERNEL_DATA_INPAGE_ERROR: Disque dur défaillant",
                    "DRIVER_VERIFIER_DETECTED_VIOLATION: Driver incompatible",
                    "CRITICAL_PROCESS_DIED: Processus système crashé",
                    "DPC_WATCHDOG_VIOLATION: Driver ancien/incompatible",
                    "MEMORY_MANAGEMENT: Problème RAM ou fichier de pagination"
                ]
            },
            {
                "title": "Diagnostic 1: Identifier le Driver Fautif",
                "bullets": [
                    "Méthode automatique:",
                    "1. Téléchargez BlueScreenView (Nirsoft) ou WhoCrashed",
                    "2. Lancez l'outil (analyse dumps C:\\Windows\\Minidump)",
                    "3. Cherchez 'Caused by Driver:' dans le rapport",
                    "4. Notez le nom du fichier .sys (ex: nvlddmkm.sys = NVIDIA)",
                    "",
                    "Méthode manuelle:",
                    "1. Windows RE > CMD",
                    "2. dir C:\\Windows\\Minidump",
                    "3. Copiez les dumps sur clé USB",
                    "4. Analysez avec WinDbg (Windows Debugger)"
                ]
            },
            {
                "title": "Solution 1: Désinstaller/Mettre à Jour Driver",
                "bullets": [
                    "Une fois driver identifié:",
                    "1. Démarrez en mode sans échec (F8)",
                    "2. Gestionnaire de périphériques",
                    "3. Trouvez périphérique correspondant au driver",
                    "4. Clic droit > Désinstaller (cochez 'Supprimer le pilote')",
                    "5. Redémarrez",
                    "6. Réinstallez driver depuis site fabricant (PAS Windows Update)",
                    "",
                    "Drivers problématiques fréquents:",
                    "• nvlddmkm.sys → GPU NVIDIA",
                    "• atikmpag.sys → GPU AMD",
                    "• igdkmd64.sys → GPU Intel",
                    "• rt640x64.sys → LAN Realtek",
                    "• ntkrnlpa.exe → Kernel Windows (corruption système)"
                ]
            },
            {
                "title": "Solution 2: Test Mémoire RAM",
                "bullets": [
                    "Si BSOD aléatoires ou codes RAM:",
                    "Méthode Windows:",
                    "1. Recherche Windows > 'Diagnostic mémoire Windows'",
                    "2. Redémarrer maintenant et vérifier",
                    "3. Test automatique (5-20 minutes)",
                    "4. Résultats après redémarrage",
                    "",
                    "Méthode MemTest86 (plus fiable):",
                    "1. Téléchargez MemTest86 (passmark.com)",
                    "2. Créez clé USB bootable",
                    "3. Démarrez dessus, lancez test",
                    "4. Laissez tourner 8+ heures (4+ passes)",
                    "5. Si erreurs → RAM défaillante, remplacer"
                ]
            },
            {
                "title": "Solution 3: Vérifier Santé Disque",
                "bullets": [
                    "Si code KERNEL_DATA_INPAGE_ERROR:",
                    "CMD Admin:",
                    "1. Test SMART: wmic diskdrive get status",
                    "   → Si 'Pred Fail': Disque mourrant, sauvegardez TOUT!",
                    "2. Check erreurs: chkdsk C: /f /r",
                    "   (Redémarre et scanne au boot, 1-4h)",
                    "3. Installez CrystalDiskInfo:",
                    "   → Vérifiez health percentage et secteurs réalloués",
                    "   → Si <80% ou secteurs réalloués >10: Remplacer disque"
                ]
            },
            {
                "title": "Solution 4: Désactiver Overclocking",
                "bullets": [
                    "Si BSOD pendant jeux ou charge CPU/GPU:",
                    "1. Entrez BIOS/UEFI (F2/Del au démarrage)",
                    "2. Cherchez options Overclocking/XMP",
                    "3. Désactivez:",
                    "   • XMP/DOCP (profils RAM OC)",
                    "   • CPU Core Ratio (multiplier CPU)",
                    "   • GPU Boost (si option BIOS)",
                    "4. Restaurez 'Defaults' si option existe",
                    "5. Sauvegardez et redémarrez",
                    "Si stable ensuite → Overclock instable était la cause"
                ]
            },
            {
                "title": "Solution 5: Réparation Système (SFC + DISM)",
                "bullets": [
                    "Si BSOD avec ntkrnlpa.exe ou ntoskrnl.exe:",
                    "CMD Admin:",
                    "1. sfc /scannow",
                    "   (Vérifie fichiers système, 10-30 min)",
                    "2. Si erreurs trouvées mais non réparées:",
                    "   DISM /Online /Cleanup-Image /RestoreHealth",
                    "   (Répare image Windows, 20-60 min)",
                    "3. Relancez sfc /scannow",
                    "4. Redémarrez"
                ]
            },
            {
                "warning": "⚠️ Si BSOD constants après toutes solutions: Probablement matériel défaillant (RAM/Disque/Carte-mère). Testez avec autre RAM/Disque. Si persiste = Carte-mère HS."
            },
            {
                "info": "💡 Activez mini dumps pour diagnostic: Système > Paramètres système avancés > Démarrage et récupération > Écrire informations de débogage > 'Petit vidage mémoire'"
            }
        ]
    },

    "ts_drivers": {
        "title": "🔧 Dépannage - Problèmes de Pilotes",
        "sections": [
            {
                "title": "Symptômes de Drivers Défectueux",
                "bullets": [
                    "Périphérique non détecté/non fonctionnel",
                    "Point d'exclamation jaune (Gestionnaire périphériques)",
                    "BSOD fréquents avec nom .sys",
                    "Performances réduites (GPU, réseau, disque)",
                    "Erreur 'Code 10', 'Code 28', 'Code 43'",
                    "Freeze/lag système aléatoires"
                ]
            },
            {
                "title": "Diagnostic: Identifier Drivers Problématiques",
                "bullets": [
                    "Méthode 1 - Gestionnaire Périphériques:",
                    "1. Clic droit Démarrer > Gestionnaire de périphériques",
                    "2. Cherchez symboles:",
                    "   △ Jaune = Driver manquant/défectueux",
                    "   ⚠ Rouge = Désactivé",
                    "   ? = Non reconnu",
                    "3. Double-clic > Onglet 'Pilote' > Détails",
                    "4. Notez version, date, fournisseur",
                    "",
                    "Méthode 2 - NiTriTe Scanner Pilotes:",
                    "1. Ouvrez NiTriTe > Scanner Pilotes Avancé",
                    "2. Cliquez 'Scanner Maintenant'",
                    "3. Consultez résultats par catégorie",
                    "4. Identifiez drivers obsolètes (date >2 ans)"
                ]
            },
            {
                "title": "Solution 1: Mettre à Jour Driver",
                "bullets": [
                    "⚠️ NE PAS utiliser 'Rechercher automatiquement' Windows Update!",
                    "Méthode correcte:",
                    "1. Identifiez matériel exact:",
                    "   • GPU: CPU-Z, GPU-Z, ou Panneau NVIDIA/AMD",
                    "   • Autres: Gestionnaire périphériques > Propriétés > Détails > ID matériel",
                    "2. Allez sur site fabricant:",
                    "   • GPU NVIDIA: nvidia.com/drivers (Game Ready ou Studio)",
                    "   • GPU AMD: amd.com/support",
                    "   • Intel: intel.com/support",
                    "   • Realtek (Audio/LAN): realtek.com",
                    "3. Téléchargez version STABLE (pas Beta)",
                    "4. Désinstallez ancien driver (DDU pour GPU)",
                    "5. Installez nouveau driver",
                    "6. Redémarrez"
                ]
            },
            {
                "title": "Solution 2: Rollback Driver",
                "bullets": [
                    "Si problème APRÈS mise à jour driver:",
                    "1. Mode sans échec (si Windows crash)",
                    "2. Gestionnaire périphériques",
                    "3. Clic droit périphérique > Propriétés",
                    "4. Onglet 'Pilote' > Restaurer pilote précédent",
                    "5. Si grisé (pas dispo):",
                    "   • Désinstaller driver actuel",
                    "   • Télécharger version antérieure sur site fabricant",
                    "   • Installer manuellement",
                    "6. Redémarrez"
                ]
            },
            {
                "title": "Solution 3: DDU (Display Driver Uninstaller)",
                "bullets": [
                    "Pour GPU NVIDIA/AMD avec problèmes persistants:",
                    "1. Téléchargez DDU (guru3d.com/ddu)",
                    "2. Redémarrez en mode sans échec",
                    "3. Lancez DDU",
                    "4. Sélectionnez GPU > 'Clean and Restart'",
                    "5. Windows redémarre avec driver basique Microsoft",
                    "6. Installez driver NVIDIA/AMD propre depuis site officiel",
                    "",
                    "Note: DDU retire TOUS résidus de drivers précédents (indispensable switch NVIDIA↔AMD)"
                ]
            },
            {
                "title": "Solution 4: Forcer Installation Driver Non-Signé",
                "bullets": [
                    "Si driver refuse de s'installer ('signature numérique'):",
                    "⚠️ Risque de sécurité - Utilisez UNIQUEMENT avec drivers de confiance!",
                    "1. CMD Admin:",
                    "   bcdedit /set nointegritychecks on",
                    "   bcdedit /set testsigning on",
                    "2. Redémarrez",
                    "3. Installez driver non-signé",
                    "4. Réactivez sécurité:",
                    "   bcdedit /set nointegritychecks off",
                    "   bcdedit /set testsigning off",
                    "5. Redémarrez"
                ]
            },
            {
                "title": "Solution 5: Réinitialiser Périphérique USB",
                "bullets": [
                    "Si périphérique USB non reconnu:",
                    "1. Débranchez TOUS périphériques USB",
                    "2. Gestionnaire périphériques",
                    "3. Affichage > Afficher périphériques cachés",
                    "4. Contrôleurs USB > Désinstallez TOUS 'Unknown Device'",
                    "5. Redémarrez PC",
                    "6. Rebranchez périphériques UN PAR UN",
                    "7. Windows réinstalle drivers automatiquement"
                ]
            },
            {
                "warning": "⚠️ Drivers génériques Windows Update: Fonctionnent mais performances réduites. Toujours préférer drivers fabricant pour GPU/Audio/LAN."
            },
            {
                "info": "💡 NiTriTe inclut un scanner de pilotes qui détecte automatiquement les drivers obsolètes et propose mises à jour via Windows Update intégré."
            }
        ]
    },

    "ts_network": {
        "title": "🌐 Dépannage - Problèmes Réseau",
        "sections": [
            {
                "title": "Symptômes Réseau Courants",
                "bullets": [
                    "Pas de connexion Internet (Wi-Fi/Ethernet)",
                    "Icône globe/point d'exclamation jaune",
                    "Connecté mais pas d'accès Internet",
                    "DNS lent ou erreurs 'Serveur introuvable'",
                    "Déconnexions aléatoires Wi-Fi",
                    "Vitesse extrêmement lente"
                ]
            },
            {
                "title": "Diagnostic Rapide",
                "bullets": [
                    "Test 1 - Ping local:",
                    "CMD: ping 192.168.1.1 (ou IP routeur)",
                    "→ Si succès: Routeur OK, problème Internet/DNS",
                    "→ Si échec: Problème carte réseau ou câble",
                    "",
                    "Test 2 - Ping Internet:",
                    "CMD: ping 8.8.8.8 (Google DNS)",
                    "→ Si succès: Internet OK, problème DNS uniquement",
                    "→ Si échec: Problème connexion Internet",
                    "",
                    "Test 3 - Résolution DNS:",
                    "CMD: nslookup google.com",
                    "→ Si timeout: DNS défaillant",
                    "→ Si OK: DNS fonctionne"
                ]
            },
            {
                "title": "Solution 1: Réinitialiser Réseau (Windows)",
                "bullets": [
                    "Méthode GUI:",
                    "1. Paramètres > Réseau et Internet",
                    "2. État > Réinitialisation du réseau",
                    "3. Réinitialiser maintenant",
                    "4. Redémarrez",
                    "",
                    "Méthode CMD (plus complète):",
                    "CMD Admin, tapez ligne par ligne:",
                    "netsh winsock reset",
                    "netsh int ip reset",
                    "ipconfig /release",
                    "ipconfig /renew",
                    "ipconfig /flushdns",
                    "netsh int tcp reset",
                    "Redémarrez PC"
                ]
            },
            {
                "title": "Solution 2: Changer Serveurs DNS",
                "bullets": [
                    "Si lenteur ou sites inaccessibles:",
                    "1. Panneau > Réseau et partage > Modifier paramètres carte",
                    "2. Clic droit connexion active > Propriétés",
                    "3. IPv4 > Propriétés",
                    "4. Cochez 'Utiliser DNS suivants:'",
                    "   Préféré: 1.1.1.1 (Cloudflare) ou 8.8.8.8 (Google)",
                    "   Auxiliaire: 1.0.0.1 (Cloudflare) ou 8.8.4.4 (Google)",
                    "5. OK > Fermer",
                    "6. CMD: ipconfig /flushdns",
                    "",
                    "Test vitesse DNS: namebench.com ou DNS Benchmark"
                ]
            },
            {
                "title": "Solution 3: Réinstaller Driver Réseau",
                "bullets": [
                    "Si carte réseau non détectée ou erreur:",
                    "1. Téléchargez driver LAN/Wi-Fi depuis site fabricant (autre PC)",
                    "2. Copiez sur clé USB",
                    "3. Mode sans échec avec réseau",
                    "4. Gestionnaire périphériques > Cartes réseau",
                    "5. Désinstallez carte (cochez 'Supprimer pilote')",
                    "6. Redémarrez",
                    "7. Installez driver depuis clé USB",
                    "",
                    "Alternative: NiTriTe > Scanner Pilotes > Mettre à jour LAN/Wi-Fi"
                ]
            },
            {
                "title": "Solution 4: Désactiver IPv6",
                "bullets": [
                    "Si connexion instable ou très lente:",
                    "1. Panneau > Réseau > Modifier paramètres carte",
                    "2. Clic droit connexion > Propriétés",
                    "3. Décochez 'Protocole Internet version 6 (TCP/IPv6)'",
                    "4. OK",
                    "5. Redémarrez PC",
                    "",
                    "Note: IPv6 rarement utilisé en résidentiel, cause parfois conflits"
                ]
            },
            {
                "title": "Solution 5: Réinitialiser Routeur",
                "bullets": [
                    "Si tous appareils ont problème réseau:",
                    "Méthode douce:",
                    "1. Débranchez alimentation routeur",
                    "2. Attendez 30 secondes",
                    "3. Rebranchez",
                    "4. Attendez 2-3 minutes (démarrage complet)",
                    "",
                    "Méthode reset complet (si persistant):",
                    "1. Bouton Reset routeur (trou, 10+ secondes)",
                    "2. Routeur redémarre avec config usine",
                    "3. Reconfigurez Wi-Fi (SSID, mot de passe)",
                    "⚠️ Sauvegardez config routeur AVANT reset si possible!"
                ]
            },
            {
                "title": "Solution 6: Problèmes Wi-Fi Spécifiques",
                "bullets": [
                    "Signal faible/déconnexions:",
                    "• Changez canal Wi-Fi (1, 6, 11 en 2.4GHz)",
                    "• Passez en 5GHz si routeur compatible (moins d'interférences)",
                    "• Rapprochez-vous routeur ou ajoutez répéteur/mesh",
                    "",
                    "Wi-Fi lent mais Ethernet rapide:",
                    "• Drivers Wi-Fi obsolètes (mettre à jour)",
                    "• Interférences (micro-ondes, Bluetooth, murs épais)",
                    "• Limitez appareils connectés simultanément",
                    "",
                    "Windows bloque Wi-Fi:",
                    "CMD Admin: netsh wlan show drivers",
                    "Vérifiez 'Hosted network supported: Yes'",
                    "Si 'No': Driver Wi-Fi incompatible, mettre à jour"
                ]
            },
            {
                "warning": "⚠️ Si aucune solution ne fonctionne: Testez avec Live Linux USB (Ubuntu). Si réseau OK sur Linux → Problème Windows. Si KO aussi → Carte réseau HS ou problème FAI."
            },
            {
                "info": "💡 Outils diagnostic réseau: Wireshark (trafic), NetSpot (Wi-Fi mapping), PingPlotter (latence), iperf3 (vitesse LAN)"
            }
        ]
    },

    "ts_performance": {
        "title": "⚡ Dépannage - Problèmes de Performance",
        "sections": [
            {
                "title": "Symptômes Performance Dégradée",
                "bullets": [
                    "Démarrage Windows très lent (>3 minutes)",
                    "Freeze/lag constant pendant utilisation",
                    "100% CPU/RAM/Disque sans raison",
                    "Jeux FPS réduits vs avant",
                    "Applications mettent longtemps à s'ouvrir",
                    "Ventilateur tourne à fond en permanence"
                ]
            },
            {
                "title": "Diagnostic: Identifier la Cause",
                "bullets": [
                    "Gestionnaire des Tâches (Ctrl+Shift+Esc):",
                    "1. Onglet Performances:",
                    "   • CPU 100%? → Processus gourmand ou malware",
                    "   • RAM >90%? → Mémoire insuffisante",
                    "   • Disque 100%? → HDD lent ou défaillant",
                    "   • GPU 0% en jeu? → Jeu utilise GPU intégré au lieu dédié",
                    "2. Onglet Processus:",
                    "   • Triez par CPU/Mémoire/Disque",
                    "   • Identifiez processus gourmands",
                    "3. Onglet Démarrage:",
                    "   • Comptez programmes au démarrage",
                    "   • Impact élevé = ralentit boot"
                ]
            },
            {
                "title": "Solution 1: Désactiver Programmes Démarrage",
                "bullets": [
                    "Si boot lent:",
                    "1. Gestionnaire des tâches > Démarrage",
                    "2. Désactivez TOUT sauf:",
                    "   • Antivirus (Windows Defender OK si activé)",
                    "   • Drivers essentiels (GPU, Audio)",
                    "3. Clic droit > Désactiver",
                    "4. Redémarrez",
                    "",
                    "Gain attendu: 30s → 15s démarrage",
                    "",
                    "Programmes souvent inutiles au démarrage:",
                    "• Teams, Skype, Discord (lancez manuellement)",
                    "• Adobe Creative Cloud, Steam, Epic Games",
                    "• OneDrive, Dropbox (si non utilisé activement)",
                    "• Applications fabricant PC (HP, Dell bloatware)"
                ]
            },
            {
                "title": "Solution 2: Upgrade HDD → SSD",
                "bullets": [
                    "Si Disque 100% constant (HDD):",
                    "⭐ Solution définitive: Installer Windows sur SSD",
                    "1. Achetez SSD 256GB+ (Samsung 870 EVO, Crucial MX500)",
                    "2. Clonez disque actuel: Macrium Reflect Free, Clonezilla",
                    "3. Remplacez disque",
                    "4. Bootez sur SSD",
                    "",
                    "Gains attendus:",
                    "• Boot: 2-3 minutes → 15-30 secondes",
                    "• Ouverture apps: 10-30s → 1-3s",
                    "• Utilisation disque: 100% → 5-20%",
                    "",
                    "Palliatif temporaire (HDD):",
                    "• Défragmentez: dfrgui.exe",
                    "• Désactivez indexation: Services > Windows Search",
                    "• Désactivez Superfetch: Services > SysMain"
                ]
            },
            {
                "title": "Solution 3: Ajouter RAM",
                "bullets": [
                    "Si RAM >85% constamment:",
                    "Vérification:",
                    "1. Gestionnaire tâches > Performances > Mémoire",
                    "2. Notez 'Emplacements utilisés: X sur Y'",
                    "3. Si slots libres → Ajoutez barrettes",
                    "4. Si full → Remplacez par capacité supérieure",
                    "",
                    "Minimum moderne:",
                    "• Windows 10/11: 8 GB (16 GB recommandé)",
                    "• Gaming: 16 GB (32 GB pour 2025+)",
                    "• Création (Photoshop, rendu 3D): 32-64 GB",
                    "",
                    "Palliatif (pas de RAM dispo):",
                    "• Fermez programmes inutilisés",
                    "• Désactivez Chrome en arrière-plan",
                    "• Augmentez fichier pagination (16 GB fixe)"
                ]
            },
            {
                "title": "Solution 4: Nettoyer Disque et Fichiers Temporaires",
                "bullets": [
                    "Si disque plein (>90%):",
                    "1. Nettoyage disque intégré:",
                    "   cleanmgr.exe > Sélectionner C: > Nettoyer fichiers système",
                    "   Cochez: Temp, Downloads, Corbeille, Anciennes mises à jour (20+ GB)",
                    "2. Désinstaller bloatware:",
                    "   Paramètres > Applications",
                    "   Supprimez: Jeux Microsoft, Candy Crush, Xbox, Netflix, etc.",
                    "3. Vider dossiers manuellement:",
                    "   %temp% → Ctrl+A → Delete",
                    "   C:\\Windows\\Temp → Delete",
                    "   C:\\Windows\\SoftwareDistribution\\Download → Delete",
                    "4. Analyser grands fichiers:",
                    "   Installez WinDirStat ou TreeSize Free",
                    "   Identifiez dossiers volumineux inutiles"
                ]
            },
            {
                "title": "Solution 5: Désactiver Effets Visuels",
                "bullets": [
                    "Si PC ancien/faible:",
                    "1. Panneau > Système > Paramètres système avancés",
                    "2. Performances > Paramètres",
                    "3. Sélectionnez 'Ajuster afin d'obtenir les meilleures performances'",
                    "4. OU personnalisé, gardez uniquement:",
                    "   • Afficher miniatures (pas icônes)",
                    "   • Lisser polices écran",
                    "5. OK > Appliquer",
                    "",
                    "Gain CPU: 5-10% sur PC faibles"
                ]
            },
            {
                "title": "Solution 6: Scan Malwares",
                "bullets": [
                    "Si CPU/RAM élevés sans raison:",
                    "1. Windows Defender:",
                    "   Sécurité Windows > Protection virus > Analyse rapide",
                    "2. Malwarebytes (gratuit):",
                    "   malwarebytes.com > Télécharger > Scanner",
                    "3. ADWCleaner (bloatware/PUP):",
                    "   malwarebytes.com/adwcleaner",
                    "4. NiTriTe Scanner Antivirus:",
                    "   Multi-moteurs, détection avancée",
                    "",
                    "Processus malware fréquents:",
                    "• svchost.exe (multiple, >200 MB chacun)",
                    "• csrss.exe (hors System32)",
                    "• Noms aléatoires (ex: xmrig, cryptominer)"
                ]
            },
            {
                "warning": "⚠️ Si performances restent mauvaises après TOUTES solutions: Matériel trop ancien ou défaillant. Envisagez upgrade CPU/GPU ou PC neuf."
            },
            {
                "info": "💡 Scripts NiTriTe: Page 'Scripts Windows' inclut +170 scripts d'optimisation automatique (désactiver télémétrie, services inutiles, tweaks gaming)."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3: POWERSHELL, CMD, OPTIMISATION (13 guides)
    # =========================================================================

    # --- POWERSHELL (4 guides) ---

    "ps_intro": {
        "title": "⚡ Introduction à PowerShell",
        "sections": [
            {
                "title": "Qu'est-ce que PowerShell?",
                "content": "PowerShell est un shell en ligne de commande moderne et un langage de script développé par Microsoft pour l'automatisation système. Contrairement à CMD (ancien shell MS-DOS), PowerShell utilise des objets .NET au lieu de texte brut, offrant une puissance et une flexibilité incomparables."
            },
            {
                "title": "PowerShell vs CMD",
                "bullets": [
                    "✅ PowerShell: Objets structurés, pipe intelligent, syntaxe moderne, cross-platform (PowerShell 7+)",
                    "❌ CMD: Texte brut uniquement, limité aux commandes DOS, Windows seulement",
                    "Exemple: PowerShell peut filtrer processus par propriétés (CPU, mémoire), CMD ne peut que lister",
                    "PowerShell 5.1 est intégré à Windows 10/11 par défaut",
                    "PowerShell 7+ (Core) fonctionne sur Windows, Linux, macOS"
                ]
            },
            {
                "title": "Ouvrir PowerShell",
                "bullets": [
                    "Méthode 1: Win + X → 'Windows PowerShell' ou 'Terminal'",
                    "Méthode 2: Menu Démarrer → taper 'PowerShell'",
                    "Méthode 3: Shift + Clic droit dans dossier → 'Ouvrir PowerShell ici'",
                    "Administrateur: Clic droit PowerShell → 'Exécuter en tant qu'administrateur'"
                ]
            },
            {
                "title": "Philosophie PowerShell: Verb-Noun",
                "content": "Toutes les commandes PowerShell (cmdlets) suivent le format Verb-Noun (Verbe-Nom) pour faciliter la découverte et la cohérence. Exemples: Get-Process (obtenir processus), Set-Location (définir emplacement), New-Item (créer élément), Remove-Item (supprimer élément)."
            },
            {
                "title": "Verbes Courants",
                "bullets": [
                    "Get: Obtenir information (Get-Service, Get-Process, Get-ChildItem)",
                    "Set: Définir/modifier (Set-ExecutionPolicy, Set-Content, Set-Location)",
                    "New: Créer nouveau (New-Item, New-ADUser, New-ScheduledTask)",
                    "Remove: Supprimer (Remove-Item, Remove-Service, Remove-ADUser)",
                    "Start/Stop: Démarrer/arrêter (Start-Process, Stop-Service)",
                    "Enable/Disable: Activer/désactiver (Enable-PSRemoting, Disable-WindowsOptionalFeature)"
                ]
            },
            {
                "title": "Alias et Raccourcis",
                "code": "# PowerShell a des alias pour faciliter transition depuis CMD/Bash\nls    # Alias de Get-ChildItem (comme Linux ls)\ndir   # Alias de Get-ChildItem (comme CMD dir)\ncd    # Alias de Set-Location\npwd   # Alias de Get-Location (comme Linux pwd)\ncls   # Alias de Clear-Host\n\n# Voir tous les alias\nGet-Alias\n\n# Trouver alias d'une commande\nGet-Alias -Definition Get-ChildItem  # Retourne: ls, dir, gci\n\n# Créer alias personnel\nSet-Alias -Name np -Value notepad.exe"
            },
            {
                "title": "Aide Intégrée (Essentiel!)",
                "code": "# Aide complète d'une commande\nGet-Help Get-Process\n\n# Exemples pratiques (TRÈS utile)\nGet-Help Get-Process -Examples\n\n# Aide détaillée avec tous paramètres\nGet-Help Get-Process -Full\n\n# Ouvrir aide en fenêtre séparée\nGet-Help Get-Process -ShowWindow\n\n# Mettre à jour l'aide (recommandé)\nUpdate-Help -Force  # Nécessite admin et internet"
            },
            {
                "title": "Découverte de Commandes",
                "code": "# Chercher commandes contenant un mot\nGet-Command *service*  # Toutes commandes avec 'service'\nGet-Command *network*  # Toutes commandes avec 'network'\n\n# Commandes d'un module spécifique\nGet-Command -Module NetTCPIP\n\n# Toutes cmdlets Get-*\nGet-Command -Verb Get\n\n# Toutes commandes manipulant 'Process'\nGet-Command -Noun Process"
            },
            {
                "title": "Execution Policy (Sécurité Scripts)",
                "content": "Par défaut, Windows bloque l'exécution de scripts PowerShell pour des raisons de sécurité. Vous devez ajuster l'Execution Policy pour exécuter vos propres scripts."
            },
            {
                "title": "Niveaux d'Execution Policy",
                "bullets": [
                    "Restricted: Aucun script autorisé (défaut Windows client)",
                    "RemoteSigned: Scripts locaux OK, scripts téléchargés doivent être signés (RECOMMANDÉ)",
                    "Unrestricted: Tous scripts autorisés (DANGEREUX)",
                    "Bypass: Tout passe sans avertissement (scripts automatisation uniquement)"
                ]
            },
            {
                "title": "Changer Execution Policy",
                "code": "# Vérifier policy actuelle\nGet-ExecutionPolicy\n\n# Définir RemoteSigned (RECOMMANDÉ - nécessite Admin)\nSet-ExecutionPolicy RemoteSigned -Scope CurrentUser\n\n# Ou pour tous utilisateurs (nécessite Admin)\nSet-ExecutionPolicy RemoteSigned -Scope LocalMachine\n\n# Bypass temporaire pour un script\npowershell -ExecutionPolicy Bypass -File .\\MonScript.ps1"
            },
            {
                "info": "💡 Astuce: Utilisez Tab pour auto-complétion de commandes, paramètres et chemins. Ctrl+R pour chercher dans l'historique."
            },
            {
                "warning": "⚠️ PowerShell est TRÈS puissant. Une commande mal utilisée peut supprimer des fichiers système ou modifier des paramètres critiques. Testez toujours avec -WhatIf quand disponible."
            }
        ]
    },

    "ps_basic": {
        "title": "📝 PowerShell - Commandes de Base",
        "sections": [
            {
                "title": "Navigation et Système de Fichiers",
                "code": "# Répertoire actuel\nGet-Location  # ou pwd\n\n# Changer de répertoire\nSet-Location C:\\Windows  # ou cd C:\\Windows\n\n# Remonter d'un niveau\nSet-Location ..  # ou cd ..\n\n# Lister fichiers/dossiers\nGet-ChildItem  # ou ls, dir\nGet-ChildItem -Force  # Inclure fichiers cachés\nGet-ChildItem -Recurse  # Récursif (sous-dossiers)\n\n# Chercher fichiers par extension\nGet-ChildItem -Filter *.txt\nGet-ChildItem -Recurse -Include *.log, *.txt\nGet-ChildItem -Recurse -Exclude *.tmp"
            },
            {
                "title": "Manipulation Fichiers/Dossiers",
                "code": "# Créer fichier vide\nNew-Item -ItemType File -Name 'test.txt'\nNew-Item -ItemType File -Path 'C:\\Temp\\data.json'\n\n# Créer dossier\nNew-Item -ItemType Directory -Name 'MonDossier'\nmkdir NouveauDossier  # Alias\n\n# Copier\nCopy-Item source.txt destination.txt\nCopy-Item C:\\Source\\*.* C:\\Destination\\ -Recurse  # Copie récursive\n\n# Déplacer\nMove-Item file.txt C:\\Temp\\\nMove-Item *.log C:\\Logs\\ -Force  # Force si conflit\n\n# Renommer\nRename-Item old.txt new.txt\n\n# Supprimer\nRemove-Item file.txt\nRemove-Item C:\\Temp\\* -Recurse -Force  # Suppression récursive forcée\nRemove-Item *.tmp -WhatIf  # Simulation (affiche ce qui serait supprimé)"
            },
            {
                "title": "Lire/Écrire Fichiers",
                "code": "# Lire contenu fichier texte\nGet-Content file.txt  # ou cat, type\nGet-Content file.txt | Select-Object -First 10  # 10 premières lignes\nGet-Content file.txt | Select-Object -Last 20   # 20 dernières lignes\n\n# Écrire contenu (écrase fichier)\nSet-Content file.txt 'Nouveau contenu'\n'Texte direct' | Set-Content file.txt\n\n# Ajouter contenu (append)\nAdd-Content file.txt 'Ligne supplémentaire'\n'Autre ligne' | Add-Content file.txt\n\n# Créer fichier avec contenu\n@'\nLigne 1\nLigne 2\nLigne 3\n'@ | Set-Content multiline.txt"
            },
            {
                "title": "Gestion Processus",
                "code": "# Lister tous processus\nGet-Process\n\n# Processus spécifique\nGet-Process -Name chrome\nGet-Process chrome  # Raccourci\n\n# Trier par CPU/Mémoire\nGet-Process | Sort-Object CPU -Descending\nGet-Process | Sort-Object WorkingSet -Descending  # RAM\n\n# Top 10 processus RAM\nGet-Process | Sort-Object WS -Descending | Select-Object -First 10 Name, WS\n\n# Démarrer programme\nStart-Process notepad.exe\nStart-Process 'C:\\Program Files\\MyApp\\app.exe'\nStart-Process powershell.exe -Verb RunAs  # En admin\n\n# Arrêter processus\nStop-Process -Name notepad\nStop-Process -Id 1234  # Par PID\nGet-Process chrome | Stop-Process  # Pipe\nStop-Process -Name app -Force  # Force si bloqué"
            },
            {
                "title": "Gestion Services Windows",
                "code": "# Lister tous services\nGet-Service\n\n# Services en cours d'exécution\nGet-Service | Where-Object {$_.Status -eq 'Running'}\n\n# Service spécifique\nGet-Service -Name 'Spooler'  # Service impression\nGet-Service *network*  # Cherche par nom\n\n# Démarrer service (ADMIN requis)\nStart-Service -Name 'Spooler'\n\n# Arrêter service (ADMIN requis)\nStop-Service -Name 'Spooler'\n\n# Redémarrer service (ADMIN requis)\nRestart-Service -Name 'Spooler'\n\n# Changer type démarrage (ADMIN requis)\nSet-Service -Name 'Spooler' -StartupType Automatic  # Auto\nSet-Service -Name 'Spooler' -StartupType Manual     # Manuel\nSet-Service -Name 'Spooler' -StartupType Disabled   # Désactivé"
            },
            {
                "title": "Informations Système",
                "code": "# Infos système complètes (lent mais exhaustif)\nGet-ComputerInfo\n\n# Nom de l'ordinateur\n$env:COMPUTERNAME\nhostname  # Équivalent CMD\n\n# Version Windows\n(Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion').ProductName\n\n# Uptime (temps depuis dernier démarrage)\n(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime\n\n# Espace disque\nGet-PSDrive -PSProvider FileSystem\nGet-PSDrive C | Select-Object Used, Free\n\n# RAM totale/libre\nGet-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory\n\n# Mises à jour installées\nGet-HotFix\nGet-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10"
            },
            {
                "title": "Réseau (Basique)",
                "code": "# Configuration IP\nGet-NetIPAddress\nGet-NetIPAddress -AddressFamily IPv4  # IPv4 seulement\n\n# Adaptateurs réseau\nGet-NetAdapter\nGet-NetAdapter | Where-Object {$_.Status -eq 'Up'}  # Actifs seulement\n\n# Test connexion (ping)\nTest-Connection google.com\nTest-Connection 8.8.8.8 -Count 4  # 4 pings\nTest-Connection google.com -Quiet  # Retourne True/False\n\n# DNS lookup\nResolve-DnsName google.com\n\n# Connexions actives\nGet-NetTCPConnection\nGet-NetTCPConnection -State Established  # Connexions établies\nGet-NetTCPConnection -LocalPort 80  # Port spécifique"
            },
            {
                "title": "Redémarrage/Extinction PC",
                "code": "# Redémarrer PC (ADMIN requis)\nRestart-Computer\nRestart-Computer -Force  # Force immédiate\nRestart-Computer -ComputerName PC01, PC02  # PCs distants\n\n# Éteindre PC (ADMIN requis)\nStop-Computer\nStop-Computer -Force  # Force immédiate\n\n# Mise en veille\nrundll32.exe powrprof.dll,SetSuspendState 0,1,0\n\n# Déconnexion utilisateur\nlogoff  # Session actuelle\nlogoff /server:PC01  # Session distante"
            },
            {
                "info": "💡 Utilisez le paramètre -WhatIf sur les commandes destructives (Remove, Stop, Set) pour prévisualiser l'action sans l'exécuter."
            }
        ]
    },

    "ps_advanced": {
        "title": "🚀 PowerShell Avancé - Scripts & Automatisation",
        "sections": [
            {
                "title": "Variables et Types",
                "code": "# Déclaration variables\n$name = 'Jean'\n$age = 30\n$price = 19.99\n$isActive = $true\n\n# Afficher variables\nWrite-Host \"Nom: $name, Age: $age\"\n\"Prix: $price euros\"  # Interpolation automatique\n\n# Arrays (tableaux)\n$servers = @('Server1', 'Server2', 'Server3')\n$numbers = 1..10  # Séquence 1 à 10\n$servers[0]  # Premier élément\n$servers.Count  # Nombre d'éléments\n\n# Hashtables (dictionnaires)\n$user = @{\n    Name = 'Jean'\n    Age = 30\n    Role = 'Admin'\n}\n$user.Name  # Accès par clé\n$user['Age']  # Accès alternatif\n\n# Variables d'environnement\n$env:COMPUTERNAME\n$env:USERNAME\n$env:PATH"
            },
            {
                "title": "Pipe et Filtrage Avancé",
                "code": "# Where-Object pour filtrer\nGet-Process | Where-Object {$_.CPU -gt 100}  # Processus CPU > 100\nGet-Service | Where-Object {$_.Status -eq 'Running'}  # Services actifs\nGet-ChildItem | Where-Object {$_.Length -gt 1MB}  # Fichiers > 1MB\n\n# Syntaxe raccourcie (PowerShell 3+)\nGet-Process | ? {$_.CPU -gt 100}  # ? = Where-Object\nGet-Service | ? Status -eq 'Running'  # Syntaxe simplifiée\n\n# Select-Object pour choisir propriétés\nGet-Process | Select-Object Name, CPU, WorkingSet\nGet-Service | Select-Object Name, Status, StartType\n\n# Propriétés calculées\nGet-Process | Select-Object Name, \n    @{Name='CPU(%)';Expression={[math]::Round($_.CPU, 2)}},\n    @{Name='RAM(MB)';Expression={[math]::Round($_.WS/1MB, 2)}}\n\n# Sort-Object pour trier\nGet-Process | Sort-Object CPU -Descending\nGet-ChildItem | Sort-Object Length -Descending\n\n# Measure-Object pour statistiques\nGet-Process | Measure-Object WorkingSet -Sum -Average -Maximum\n(Get-ChildItem -Recurse | Measure-Object -Property Length -Sum).Sum / 1GB"
            },
            {
                "title": "Boucles",
                "code": "# ForEach-Object (pipe)\nGet-ChildItem *.txt | ForEach-Object {\n    Write-Host \"Fichier: $($_.Name)\"\n}\n\n# Raccourci %\nGet-Process | % { $_.Name }  # % = ForEach-Object\n\n# Boucle ForEach classique\n$servers = @('Server1', 'Server2', 'Server3')\nforeach ($server in $servers) {\n    Test-Connection $server -Count 1 -Quiet\n    Write-Host \"$server est accessible\"\n}\n\n# Boucle For\nfor ($i = 1; $i -le 10; $i++) {\n    Write-Host \"Itération $i\"\n}\n\n# Boucle While\n$counter = 0\nwhile ($counter -lt 5) {\n    Write-Host \"Compteur: $counter\"\n    $counter++\n}\n\n# Boucle Do-While\ndo {\n    $input = Read-Host \"Entrez 'quit' pour sortir\"\n} while ($input -ne 'quit')"
            },
            {
                "title": "Conditions If/Else",
                "code": "# If simple\n$age = 25\nif ($age -gt 18) {\n    Write-Host \"Majeur\"\n}\n\n# If/Else\nif ($age -ge 18) {\n    Write-Host \"Majeur\"\n} else {\n    Write-Host \"Mineur\"\n}\n\n# If/ElseIf/Else\n$score = 75\nif ($score -ge 90) {\n    Write-Host \"Excellent\"\n} elseif ($score -ge 70) {\n    Write-Host \"Bien\"\n} elseif ($score -ge 50) {\n    Write-Host \"Passable\"\n} else {\n    Write-Host \"Échec\"\n}\n\n# Opérateurs de comparaison\n# -eq (égal), -ne (différent), -gt (supérieur), -ge (sup/égal)\n# -lt (inférieur), -le (inf/égal), -like (pattern), -match (regex)\n\n# Switch (pour multiples cas)\n$day = 'Lundi'\nswitch ($day) {\n    'Lundi' { Write-Host \"Début de semaine\" }\n    'Vendredi' { Write-Host \"Fin de semaine\" }\n    'Samedi' { Write-Host \"Weekend!\" }\n    'Dimanche' { Write-Host \"Weekend!\" }\n    default { Write-Host \"Jour normal\" }\n}"
            },
            {
                "title": "Fonctions Réutilisables",
                "code": "# Fonction simple\nfunction Say-Hello {\n    Write-Host \"Bonjour!\"\n}\nSay-Hello  # Appel\n\n# Fonction avec paramètres\nfunction Get-DiskSpace {\n    param(\n        [string]$ComputerName = $env:COMPUTERNAME,\n        [switch]$ShowGB\n    )\n    \n    $disks = Get-CimInstance Win32_LogicalDisk -ComputerName $ComputerName |\n             Where-Object {$_.DriveType -eq 3}\n    \n    foreach ($disk in $disks) {\n        if ($ShowGB) {\n            $size = [math]::Round($disk.Size / 1GB, 2)\n            $free = [math]::Round($disk.FreeSpace / 1GB, 2)\n            Write-Host \"$($disk.DeviceID) - Taille: $size GB, Libre: $free GB\"\n        } else {\n            Write-Host \"$($disk.DeviceID) - Libre: $($disk.FreeSpace) bytes\"\n        }\n    }\n}\n\n# Utilisation\nGet-DiskSpace\nGet-DiskSpace -ShowGB\nGet-DiskSpace -ComputerName 'Server01' -ShowGB\n\n# Fonction avec retour\nfunction Get-DoubleValue {\n    param([int]$Number)\n    return $Number * 2\n}\n$result = Get-DoubleValue -Number 10\nWrite-Host $result  # 20"
            },
            {
                "title": "Gestion Erreurs Try/Catch",
                "code": "# Try/Catch basique\ntry {\n    # Code susceptible d'échouer\n    Stop-Service 'ServiceInexistant' -ErrorAction Stop\n    Write-Host \"Service arrêté\"\n} catch {\n    # Gérer l'erreur\n    Write-Host \"Erreur: $($_.Exception.Message)\" -ForegroundColor Red\n}\n\n# Try/Catch/Finally\ntry {\n    $file = Get-Content 'C:\\inexistant.txt' -ErrorAction Stop\n} catch {\n    Write-Host \"Fichier introuvable!\" -ForegroundColor Red\n    # Logger erreur\n    $_ | Out-File 'error.log' -Append\n} finally {\n    # Exécuté dans tous les cas (succès ou erreur)\n    Write-Host \"Nettoyage effectué\" -ForegroundColor Green\n}\n\n# Captures spécifiques\ntry {\n    $result = 10 / 0\n} catch [System.DivideByZeroException] {\n    Write-Host \"Division par zéro!\"\n} catch {\n    Write-Host \"Autre erreur: $_\"\n}"
            },
            {
                "title": "WMI et CIM (Gestion Windows)",
                "code": "# CIM (moderne, recommandé)\nGet-CimInstance Win32_OperatingSystem  # Infos OS\nGet-CimInstance Win32_ComputerSystem   # Infos PC\nGet-CimInstance Win32_Processor        # Infos CPU\nGet-CimInstance Win32_PhysicalMemory   # Infos RAM\nGet-CimInstance Win32_LogicalDisk      # Infos disques\nGet-CimInstance Win32_NetworkAdapter   # Cartes réseau\nGet-CimInstance Win32_Service          # Services\n\n# Filtrer résultats CIM\nGet-CimInstance Win32_Service | Where-Object {$_.State -eq 'Running'}\nGet-CimInstance Win32_NetworkAdapter | Where-Object {$_.NetEnabled -eq $true}\n\n# Gestion distante via CIM\nGet-CimInstance -ClassName Win32_Process -ComputerName Server01\nRestart-Computer -ComputerName Server01, Server02 -Force\n\n# WMI (ancien, mais encore utilisé)\nGet-WmiObject Win32_OperatingSystem\nGet-WmiObject Win32_BIOS\n\n# Informations utiles\n# Version Windows\n(Get-CimInstance Win32_OperatingSystem).Caption\n\n# Uptime\n(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime\n\n# Fabricant/Modèle PC\n(Get-CimInstance Win32_ComputerSystem).Manufacturer\n(Get-CimInstance Win32_ComputerSystem).Model"
            },
            {
                "title": "Export/Import Données",
                "code": "# Export CSV\nGet-Process | Export-Csv 'processes.csv' -NoTypeInformation\nGet-Service | Export-Csv 'services.csv' -NoTypeInformation -Encoding UTF8\n\n# Import CSV\n$data = Import-Csv 'processes.csv'\n$data | Where-Object {$_.CPU -gt 10}\n\n# Export JSON\nGet-Service | ConvertTo-Json | Out-File 'services.json'\n$users = @(\n    @{Name='Jean'; Age=30},\n    @{Name='Marie'; Age=25}\n)\n$users | ConvertTo-Json | Out-File 'users.json'\n\n# Import JSON\n$services = Get-Content 'services.json' | ConvertFrom-Json\n\n# Export XML (CLIXML - préserve types PowerShell)\nGet-Process | Export-Clixml 'processes.xml'\n\n# Import XML\n$procs = Import-Clixml 'processes.xml'\n\n# Export TXT simple\nGet-Process | Out-File 'processes.txt'\nGet-Service | Format-Table -AutoSize | Out-File 'services.txt'"
            },
            {
                "title": "Tâches Planifiées",
                "code": "# Créer tâche planifiée\n$action = New-ScheduledTaskAction -Execute 'Powershell.exe' `\n    -Argument '-NoProfile -ExecutionPolicy Bypass -File C:\\Scripts\\backup.ps1'\n\n$trigger = New-ScheduledTaskTrigger -Daily -At 2am\n\n$principal = New-ScheduledTaskPrincipal -UserId 'SYSTEM' `\n    -LogonType ServiceAccount -RunLevel Highest\n\nRegister-ScheduledTask -TaskName 'BackupDaily' `\n    -Action $action -Trigger $trigger -Principal $principal\n\n# Lister tâches\nGet-ScheduledTask\nGet-ScheduledTask | Where-Object {$_.State -eq 'Ready'}\n\n# Exécuter manuellement\nStart-ScheduledTask -TaskName 'BackupDaily'\n\n# Désactiver tâche\nDisable-ScheduledTask -TaskName 'BackupDaily'\n\n# Supprimer tâche\nUnregister-ScheduledTask -TaskName 'BackupDaily' -Confirm:$false"
            },
            {
                "warning": "⚠️ Les scripts PowerShell peuvent avoir un impact système majeur. Testez TOUJOURS sur environnement de test avant production."
            },
            {
                "info": "💡 Utilisez ISE PowerShell (Integrated Scripting Environment) ou VS Code avec extension PowerShell pour éditer/débugger scripts complexes."
            }
        ]
    },

    "ps_scripts": {
        "title": "📜 PowerShell - Scripts Utiles",
        "sections": [
            {
                "title": "Script 1: Nettoyage Disque Automatisé",
                "content": "Script qui nettoie fichiers temporaires, cache, corbeille, et génère un rapport."
            },
            {
                "code": "# CleanupDisk.ps1\nparam(\n    [switch]$DryRun  # Simulation sans suppression\n)\n\n$sizeBefore = (Get-PSDrive C).Free / 1GB\nWrite-Host \"=== Nettoyage Disque C: ===\"\nWrite-Host \"Espace libre avant: $([math]::Round($sizeBefore, 2)) GB\"\n\n# Chemins à nettoyer\n$paths = @(\n    \"$env:TEMP\\*\",\n    \"C:\\Windows\\Temp\\*\",\n    \"C:\\Windows\\Prefetch\\*\",\n    \"$env:LOCALAPPDATA\\Microsoft\\Windows\\Explorer\\thumbcache_*.db\",\n    \"C:\\`$Recycle.Bin\"\n)\n\nforeach ($path in $paths) {\n    try {\n        if ($DryRun) {\n            $files = Get-ChildItem $path -Recurse -Force -ErrorAction SilentlyContinue\n            $size = ($files | Measure-Object -Property Length -Sum).Sum / 1MB\n            Write-Host \"[SIMULATION] Suppression $path : $([math]::Round($size, 2)) MB\"\n        } else {\n            Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue\n            Write-Host \"[OK] $path nettoyé\" -ForegroundColor Green\n        }\n    } catch {\n        Write-Host \"[ERREUR] $path : $($_.Exception.Message)\" -ForegroundColor Red\n    }\n}\n\n# Vider corbeille\nClear-RecycleBin -Force -ErrorAction SilentlyContinue\n\n$sizeAfter = (Get-PSDrive C).Free / 1GB\n$freed = $sizeAfter - $sizeBefore\nWrite-Host \"\\nEspace libre après: $([math]::Round($sizeAfter, 2)) GB\"\nWrite-Host \"Espace libéré: $([math]::Round($freed, 2)) GB\" -ForegroundColor Cyan"
            },
            {
                "title": "Script 2: Backup Automatique avec Rotation",
                "content": "Script qui crée une sauvegarde ZIP horodatée et supprime les sauvegardes anciennes."
            },
            {
                "code": "# AutoBackup.ps1\nparam(\n    [string]$SourcePath = \"C:\\ImportantData\",\n    [string]$BackupPath = \"D:\\Backups\",\n    [int]$RetentionDays = 30  # Garder sauvegardes < 30 jours\n)\n\n# Vérifier Compress-Archive (PowerShell 5+)\nif (-not (Get-Command Compress-Archive -ErrorAction SilentlyContinue)) {\n    Write-Host \"Erreur: Compress-Archive non disponible (PowerShell 5+ requis)\" -ForegroundColor Red\n    exit 1\n}\n\n# Créer dossier backup si inexistant\nif (-not (Test-Path $BackupPath)) {\n    New-Item -ItemType Directory -Path $BackupPath | Out-Null\n}\n\n# Nom backup horodaté\n$timestamp = Get-Date -Format \"yyyyMMdd_HHmmss\"\n$backupFile = Join-Path $BackupPath \"Backup_$timestamp.zip\"\n\ntry {\n    Write-Host \"Création sauvegarde: $backupFile\"\n    Compress-Archive -Path $SourcePath -DestinationPath $backupFile -CompressionLevel Optimal\n    \n    $size = (Get-Item $backupFile).Length / 1MB\n    Write-Host \"✅ Sauvegarde créée: $([math]::Round($size, 2)) MB\" -ForegroundColor Green\n    \n    # Rotation: Supprimer sauvegardes anciennes\n    $cutoffDate = (Get-Date).AddDays(-$RetentionDays)\n    $oldBackups = Get-ChildItem $BackupPath -Filter \"Backup_*.zip\" |\n                  Where-Object {$_.LastWriteTime -lt $cutoffDate}\n    \n    if ($oldBackups) {\n        Write-Host \"\\nSuppression sauvegardes > $RetentionDays jours:\"\n        foreach ($old in $oldBackups) {\n            Remove-Item $old.FullName -Force\n            Write-Host \"  - $($old.Name) supprimé\" -ForegroundColor Yellow\n        }\n    }\n    \n} catch {\n    Write-Host \"❌ Erreur: $($_.Exception.Message)\" -ForegroundColor Red\n    exit 1\n}"
            },
            {
                "title": "Script 3: Inventaire Système Complet",
                "content": "Génère un rapport HTML détaillé des composants système (CPU, RAM, disques, OS, réseau)."
            },
            {
                "code": "# SystemInventory.ps1\n$outputFile = \"C:\\SystemInventory_$(Get-Date -Format 'yyyyMMdd_HHmmss').html\"\n\n# Récupérer infos\n$os = Get-CimInstance Win32_OperatingSystem\n$cpu = Get-CimInstance Win32_Processor\n$ram = Get-CimInstance Win32_PhysicalMemory\n$disks = Get-CimInstance Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3}\n$network = Get-CimInstance Win32_NetworkAdapterConfiguration | Where-Object {$_.IPEnabled -eq $true}\n$bios = Get-CimInstance Win32_BIOS\n$computer = Get-CimInstance Win32_ComputerSystem\n\n# Générer HTML\n$html = @\"\n<!DOCTYPE html>\n<html>\n<head>\n    <meta charset='UTF-8'>\n    <title>Inventaire Système - $($env:COMPUTERNAME)</title>\n    <style>\n        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }\n        h1 { color: #0078D4; }\n        table { border-collapse: collapse; width: 100%; margin: 20px 0; background: white; }\n        th { background: #0078D4; color: white; padding: 10px; text-align: left; }\n        td { padding: 8px; border-bottom: 1px solid #ddd; }\n        tr:hover { background: #f0f0f0; }\n    </style>\n</head>\n<body>\n    <h1>📊 Inventaire Système - $($env:COMPUTERNAME)</h1>\n    <p><strong>Date:</strong> $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')</p>\n    \n    <h2>💻 Système d'Exploitation</h2>\n    <table>\n        <tr><th>Propriété</th><th>Valeur</th></tr>\n        <tr><td>OS</td><td>$($os.Caption)</td></tr>\n        <tr><td>Version</td><td>$($os.Version)</td></tr>\n        <tr><td>Architecture</td><td>$($os.OSArchitecture)</td></tr>\n        <tr><td>Uptime</td><td>$([math]::Round(((Get-Date) - $os.LastBootUpTime).TotalHours, 2)) heures</td></tr>\n    </table>\n    \n    <h2>⚙️ Processeur</h2>\n    <table>\n        <tr><th>Propriété</th><th>Valeur</th></tr>\n        <tr><td>Nom</td><td>$($cpu.Name)</td></tr>\n        <tr><td>Cœurs</td><td>$($cpu.NumberOfCores)</td></tr>\n        <tr><td>Threads</td><td>$($cpu.NumberOfLogicalProcessors)</td></tr>\n    </table>\n    \n    <h2>🧠 Mémoire RAM</h2>\n    <table>\n        <tr><th>Barrette</th><th>Capacité</th><th>Vitesse</th></tr>\n\"@\n\nforeach ($stick in $ram) {\n    $html += \"<tr><td>$($stick.DeviceLocator)</td><td>$([math]::Round($stick.Capacity / 1GB, 2)) GB</td><td>$($stick.Speed) MHz</td></tr>\"\n}\n\n$html += @\"\n    </table>\n    \n    <h2>💾 Disques</h2>\n    <table>\n        <tr><th>Lettre</th><th>Taille</th><th>Libre</th><th>Utilisé</th></tr>\n\"@\n\nforeach ($disk in $disks) {\n    $used = $disk.Size - $disk.FreeSpace\n    $usedPercent = [math]::Round(($used / $disk.Size) * 100, 1)\n    $html += \"<tr><td>$($disk.DeviceID)</td><td>$([math]::Round($disk.Size / 1GB, 2)) GB</td><td>$([math]::Round($disk.FreeSpace / 1GB, 2)) GB</td><td>$usedPercent%</td></tr>\"\n}\n\n$html += \"</table></body></html>\"\n\n# Enregistrer\n$html | Out-File $outputFile -Encoding UTF8\nWrite-Host \"✅ Rapport généré: $outputFile\" -ForegroundColor Green\nStart-Process $outputFile  # Ouvrir dans navigateur"
            },
            {
                "title": "Script 4: Surveillance Processus avec Alerte",
                "content": "Surveille un processus et envoie une alerte si CPU/RAM dépasse seuil."
            },
            {
                "code": "# ProcessMonitor.ps1\nparam(\n    [string]$ProcessName = \"chrome\",\n    [int]$CPUThreshold = 80,  # % CPU\n    [int]$RAMThreshold = 1024  # MB RAM\n)\n\nWrite-Host \"🔍 Surveillance de $ProcessName (CPU > $CPUThreshold%, RAM > $RAMThreshold MB)\"\nWrite-Host \"Appuyez sur Ctrl+C pour arrêter...\\n\"\n\nwhile ($true) {\n    $processes = Get-Process -Name $ProcessName -ErrorAction SilentlyContinue\n    \n    if ($processes) {\n        foreach ($proc in $processes) {\n            $cpu = [math]::Round($proc.CPU, 2)\n            $ram = [math]::Round($proc.WorkingSet / 1MB, 2)\n            \n            $status = \"[OK]\"\n            $color = \"Green\"\n            \n            if ($cpu -gt $CPUThreshold -or $ram -gt $RAMThreshold) {\n                $status = \"[ALERTE]\"\n                $color = \"Red\"\n                # Ici: Envoyer email, log, notification Windows, etc.\n                [System.Windows.Forms.MessageBox]::Show(\n                    \"$ProcessName dépasse les seuils!\\nCPU: $cpu% | RAM: $ram MB\",\n                    \"Alerte Processus\",\n                    [System.Windows.Forms.MessageBoxButtons]::OK,\n                    [System.Windows.Forms.MessageBoxIcon]::Warning\n                )\n            }\n            \n            Write-Host \"$status PID:$($proc.Id) | CPU: $cpu% | RAM: $ram MB\" -ForegroundColor $color\n        }\n    } else {\n        Write-Host \"[INFO] $ProcessName non actif\" -ForegroundColor Yellow\n    }\n    \n    Start-Sleep -Seconds 5\n}"
            },
            {
                "title": "Script 5: Installer Programmes depuis Liste",
                "content": "Installe automatiquement une liste de programmes via Winget (équivalent simplifié de Master Install)."
            },
            {
                "code": "# InstallPrograms.ps1\n# Liste programmes à installer (Winget IDs)\n$programs = @(\n    \"7zip.7zip\",\n    \"Mozilla.Firefox\",\n    \"Google.Chrome\",\n    \"Microsoft.VisualStudioCode\",\n    \"VideoLAN.VLC\",\n    \"Notepad++.Notepad++\",\n    \"Adobe.Acrobat.Reader.64-bit\"\n)\n\n# Vérifier Winget installé\nif (-not (Get-Command winget -ErrorAction SilentlyContinue)) {\n    Write-Host \"Erreur: Winget non installé!\" -ForegroundColor Red\n    Write-Host \"Installez App Installer depuis Microsoft Store.\" -ForegroundColor Yellow\n    exit 1\n}\n\nWrite-Host \"=== Installation de $($programs.Count) programmes ===\\n\"\n\n$success = 0\n$failed = 0\n\nforeach ($program in $programs) {\n    Write-Host \"\\n[$(($success + $failed + 1))/$($programs.Count)] Installation: $program\" -ForegroundColor Cyan\n    \n    try {\n        $result = winget install --id $program --exact --silent --accept-package-agreements --accept-source-agreements\n        \n        if ($LASTEXITCODE -eq 0) {\n            Write-Host \"  ✅ $program installé\" -ForegroundColor Green\n            $success++\n        } else {\n            Write-Host \"  ❌ $program échoué (code: $LASTEXITCODE)\" -ForegroundColor Red\n            $failed++\n        }\n    } catch {\n        Write-Host \"  ❌ $program échoué: $($_.Exception.Message)\" -ForegroundColor Red\n        $failed++\n    }\n}\n\nWrite-Host \"\\n=== Résumé ===\"\nWrite-Host \"✅ Réussis: $success\" -ForegroundColor Green\nWrite-Host \"❌ Échoués: $failed\" -ForegroundColor Red"
            },
            {
                "info": "💡 Pour exécuter un script: Clic droit → 'Exécuter avec PowerShell' OU ouvrir PowerShell et taper: .\\MonScript.ps1"
            },
            {
                "warning": "⚠️ N'exécutez JAMAIS de scripts PowerShell provenant de sources non fiables. Lisez toujours le code avant exécution."
            }
        ]
    },

    # --- CMD (Invite de commandes) (4 guides) ---

    "cmd_intro": {
        "title": "💻 Introduction à CMD (Invite de commandes)",
        "sections": [
            {
                "title": "Qu'est-ce que CMD?",
                "content": "CMD (Command Prompt / Invite de commandes) est le shell en ligne de commande historique de Windows, basé sur MS-DOS. Bien que moins puissant que PowerShell, CMD reste essentiel pour l'administration système et le dépannage Windows, et est compatible avec tous les scripts batch (.bat) legacy."
            },
            {
                "title": "CMD vs PowerShell",
                "bullets": [
                    "CMD: Simple, rapide, compatible scripts batch, manipule texte uniquement",
                    "PowerShell: Puissant, objets structurés, syntaxe moderne, mais plus complexe",
                    "Quand utiliser CMD: Scripts batch existants, commandes rapides, environnements legacy",
                    "Quand utiliser PowerShell: Automatisation complexe, gestion distante, administration Active Directory"
                ]
            },
            {
                "title": "Ouvrir CMD",
                "bullets": [
                    "Méthode 1: Win + R → taper 'cmd' → Entrée",
                    "Méthode 2: Menu Démarrer → taper 'cmd' ou 'Invite de commandes'",
                    "Méthode 3: Shift + Clic droit dans dossier → 'Ouvrir fenêtre de commandes ici'",
                    "Administrateur: Clic droit CMD → 'Exécuter en tant qu'administrateur' (NÉCESSAIRE pour commandes système)"
                ]
            },
            {
                "title": "Anatomie d'une Commande CMD",
                "content": "Format général: COMMANDE [options] [arguments]. Exemple: 'dir /s C:\\' liste tous fichiers de C:\\ récursivement. '/s' est une option (switch), 'C:\\' est l'argument."
            },
            {
                "title": "Options Communes (Switches)",
                "bullets": [
                    "/? - Affiche l'aide de la commande (ex: dir /?)",
                    "/s - Récursif, inclut sous-dossiers (ex: dir /s)",
                    "/a - Inclut fichiers cachés/système (ex: dir /a)",
                    "/f - Force l'action (ex: del /f fichier.txt)",
                    "/q - Mode silencieux/quiet (ex: del /q)",
                    "/y - Répondre 'Oui' automatiquement (ex: copy /y)"
                ]
            },
            {
                "title": "Raccourcis Clavier Essentiels",
                "bullets": [
                    "Tab: Auto-complétion chemins/fichiers (très utile!)",
                    "↑/↓: Naviguer historique commandes",
                    "F7: Afficher historique commandes complet",
                    "Ctrl+C: Annuler commande en cours",
                    "Ctrl+V: Coller (ou Clic droit)",
                    "Alt+Enter: Plein écran / Fenêtré"
                ]
            },
            {
                "title": "Aide et Documentation",
                "code": "REM Aide d'une commande spécifique\ndir /?\nping /?\nnetstat /?\n\nREM Lister toutes commandes disponibles\nhelp\n\nREM Aide détaillée d'une commande via HELP\nhelp dir\nhelp copy"
            },
            {
                "title": "Navigation de Base",
                "code": "REM Afficher répertoire actuel\ncd\n\nREM Changer de répertoire\ncd C:\\Windows\ncd \"C:\\Program Files\"  REM Guillemets si espaces!\n\nREM Remonter d'un niveau\ncd ..\n\nREM Aller à la racine du disque\ncd \\\n\nREM Changer de disque\nD:\nE:"
            },
            {
                "title": "Variables d'Environnement",
                "code": "REM Afficher toutes variables\nset\n\nREM Variables système utiles\necho %COMPUTERNAME%  REM Nom PC\necho %USERNAME%      REM Nom utilisateur\necho %USERPROFILE%   REM C:\\Users\\VotreNom\necho %TEMP%          REM Dossier temporaire\necho %WINDIR%        REM C:\\Windows\necho %PROGRAMFILES%  REM C:\\Program Files\necho %PATH%          REM Chemins exécutables\n\nREM Définir variable temporaire\nset MYVAR=valeur\necho %MYVAR%"
            },
            {
                "title": "Redirection et Pipes",
                "code": "REM Rediriger sortie vers fichier (écrase)\ndir > liste.txt\n\nREM Ajouter à un fichier existant\ndir >> liste.txt\n\nREM Supprimer sortie (silence)\ncommand > NUL\n\nREM Rediriger erreurs\ncommand 2> erreurs.txt\n\nREM Pipe (chaîner commandes)\ndir | find \".txt\"\ntasklist | findstr chrome\nnetstat -ano | find \"ESTABLISHED\""
            },
            {
                "title": "Caractères Spéciaux",
                "bullets": [
                    "& - Exécuter commandes séquentiellement (dir & cd ..)",
                    "&& - Exécuter si précédente réussie (mkdir test && cd test)",
                    "|| - Exécuter si précédente échoue (ping google.com || echo Offline)",
                    "| - Pipe, envoyer sortie à autre commande (dir | find \"txt\")",
                    "> - Redirection sortie vers fichier (dir > liste.txt)",
                    "^ - Caractère d'échappement (echo Bonjour^! → affiche Bonjour!)"
                ]
            },
            {
                "info": "💡 Astuce: Utilisez 'doskey /history' pour voir historique complet des commandes de la session actuelle."
            },
            {
                "warning": "⚠️ CMD ne peut pas être annulé! Les commandes comme 'del', 'format', 'rd' sont IRRÉVERSIBLES. Vérifiez toujours vos commandes avant Entrée."
            }
        ]
    },

    "cmd_basic": {
        "title": "📝 CMD - Commandes Essentielles",
        "sections": [
            {
                "title": "Gestion Fichiers et Dossiers",
                "code": "REM Lister fichiers/dossiers\ndir                   REM Répertoire actuel\ndir /s                REM Récursif (sous-dossiers)\ndir /a                REM Inclure cachés/système\ndir /b                REM Format basique (noms seulement)\ndir *.txt             REM Filtrer par extension\ndir /s /b *.log       REM Chercher .log partout\n\nREM Créer dossier\nmkdir NouveauDossier\nmkdir \"Dossier avec espaces\"\n\nREM Copier fichiers\ncopy source.txt destination.txt\ncopy *.txt C:\\Backup\\  REM Tous .txt\ncopy /y file.txt dest.txt  REM Sans confirmation\n\nREM Déplacer fichiers\nmove file.txt C:\\Temp\\\nmove *.log C:\\Logs\\\n\nREM Renommer\nren ancien.txt nouveau.txt\nrename file.old file.new\n\nREM Supprimer fichiers\ndel file.txt\ndel *.tmp             REM Tous .tmp\ndel /f /q fichier.txt REM Force + silencieux\n\nREM Supprimer dossiers\nrmdir DossierVide     REM Vide seulement\nrd /s /q Dossier      REM Récursif + force + silencieux\n\nREM Afficher contenu fichier\ntype file.txt\ntype file.txt | more  REM Page par page\n\nREM Créer fichier avec contenu\necho Bonjour > fichier.txt     REM Écrase\necho Nouvelle ligne >> fichier.txt  REM Ajoute"
            },
            {
                "title": "Arbre de Fichiers",
                "code": "REM Afficher arborescence\ntree\ntree /f               REM Inclure fichiers\ntree /a               REM Caractères ASCII (copier/coller)\ntree C:\\Windows /f > arbre.txt  REM Sauvegarder"
            },
            {
                "title": "Recherche de Fichiers",
                "code": "REM Chercher fichier par nom\ndir /s /b \"nom.txt\"\ndir /s /b C:\\*.log    REM Tous .log sur C:\n\nREM Chercher texte dans fichiers\nfind \"texte\" fichier.txt\nfind /i \"erreur\" *.log  REM Insensible casse\nfind /c \"WARNING\" log.txt  REM Compter occurrences\n\nREM FINDSTR (plus puissant, regex)\nfindstr \"error\" *.log\nfindstr /s /i \"exception\" C:\\Logs\\*  REM Récursif + casse\nfindstr /r \"ERROR.*failed\" log.txt  REM Regex"
            },
            {
                "title": "Informations Système",
                "code": "REM Infos système détaillées\nsysteminfo\nsysteminfo | find \"OS\"  REM Filtrer OS\nsysteminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\"\n\nREM Nom PC\nhostname\n\nREM Version Windows\nver\nwinver  REM Interface graphique\n\nREM Variables système\nset\nset COMPUTERNAME\nset USERNAME\n\nREM Date/Heure\ndate /t\ntime /t"
            },
            {
                "title": "Gestion Processus",
                "code": "REM Lister processus\ntasklist\ntasklist | find \"chrome\"\ntasklist /svc  REM Avec services associés\n\nREM Tuer processus\ntaskkill /IM notepad.exe\ntaskkill /IM chrome.exe /F  REM Force\ntaskkill /PID 1234 /F       REM Par ID processus\ntaskkill /IM app.exe /T     REM + processus enfants"
            },
            {
                "title": "Gestion Services",
                "code": "REM Lister services (nécessite NET ou SC)\nnet start  REM Services actifs\nsc query   REM Tous services\nsc query state= all  REM Vraiment tous\n\nREM Démarrer service (ADMIN)\nnet start \"Spooler\"\nsc start Spooler\n\nREM Arrêter service (ADMIN)\nnet stop \"Spooler\"\nsc stop Spooler\n\nREM Config service (ADMIN)\nsc config Spooler start= auto     REM Automatique\nsc config Spooler start= demand   REM Manuel\nsc config Spooler start= disabled REM Désactivé"
            },
            {
                "title": "Réseau - Basique",
                "code": "REM Configuration IP\nipconfig\nipconfig /all  REM Détails complets\n\nREM Libérer/Renouveler IP DHCP\nipconfig /release\nipconfig /renew\n\nREM Vider cache DNS\nipconfig /flushdns\n\nREM Ping\nping google.com\nping -t 8.8.8.8  REM Continu (Ctrl+C pour arrêter)\nping -n 10 192.168.1.1  REM 10 paquets\n\nREM Trace route\ntracert google.com\n\nREM DNS lookup\nnslookup google.com\nnslookup google.com 8.8.8.8  REM Via DNS Google"
            },
            {
                "title": "Disque et Partitions",
                "code": "REM Vérifier disque (ADMIN, redémarrage)\nchkdsk C:\nchkdsk C: /f     REM Réparer erreurs\nchkdsk C: /r     REM Réparer + récupérer secteurs\nchkdsk C: /scan  REM Scan rapide (Win10+)\n\nREM Espace disque\ndir C:\\ | find \"octets libres\"\n\nREM Formater (DANGER! ADMIN)\nformat E: /fs:NTFS /q  REM Format rapide E: en NTFS\nformat E: /fs:FAT32    REM FAT32"
            },
            {
                "title": "Utilisateurs (ADMIN)",
                "code": "REM Lister utilisateurs\nnet user\n\nREM Infos utilisateur\nnet user NomUtilisateur\n\nREM Créer utilisateur\nnet user jean MotDePasse /add\n\nREM Supprimer utilisateur\nnet user jean /delete\n\nREM Changer mot de passe\nnet user jean NouveauMotDePasse\n\nREM Ajouter aux administrateurs\nnet localgroup Administrateurs jean /add"
            },
            {
                "title": "Redémarrage/Extinction",
                "code": "REM Éteindre PC\nshutdown /s /t 0     REM Immédiat\nshutdown /s /t 60    REM Dans 60 secondes\nshutdown /s /t 300 /c \"Extinction dans 5 min\"  REM Avec message\n\nREM Redémarrer\nshutdown /r /t 0\n\nREM Annuler extinction planifiée\nshutdown /a\n\nREM Hiberner\nshutdown /h\n\nREM Déconnexion\nlogoff"
            },
            {
                "info": "💡 Utilisez 'command /?' pour voir toutes les options d'une commande (ex: dir /?, ping /?)."
            },
            {
                "warning": "⚠️ Les commandes marquées (ADMIN) nécessitent CMD lancé en tant qu'administrateur. Clic droit CMD → Exécuter en tant qu'administrateur."
            }
        ]
    },

    "cmd_batch": {
        "title": "📜 CMD - Fichiers Batch (.bat)",
        "sections": [
            {
                "title": "Qu'est-ce qu'un Fichier Batch?",
                "content": "Un fichier batch (.bat ou .cmd) est un script texte contenant une série de commandes CMD exécutées séquentiellement. Idéal pour automatiser tâches répétitives, installations, sauvegardes, nettoyages, etc. Les fichiers batch sont simples, portables, et fonctionnent sur tous Windows depuis XP."
            },
            {
                "title": "Créer un Fichier Batch",
                "bullets": [
                    "Étape 1: Ouvrir Bloc-notes (notepad.exe)",
                    "Étape 2: Écrire commandes CMD (une par ligne)",
                    "Étape 3: Enregistrer sous → Choisir 'Tous les fichiers' → Nom: script.bat",
                    "Étape 4: Double-cliquer script.bat pour exécuter",
                    "Alternative: Clic droit → Modifier pour éditer"
                ]
            },
            {
                "title": "Structure Basique d'un Script Batch",
                "code": "@echo off\nREM =====================================================\nREM Script de Démonstration\nREM Auteur: Votre Nom\nREM Date: 2025-01-03\nREM =====================================================\n\nREM Désactiver affichage commandes\ntitle Mon Premier Script Batch\n\nREM Commentaire: Cette ligne ne s'exécute pas\necho Bonjour, bienvenue dans mon script!\n\nREM Pause pour voir résultats\npause\n\nREM Fin du script\nexit"
            },
            {
                "title": "Commandes Spéciales Batch",
                "bullets": [
                    "@echo off - Désactive affichage des commandes (ligne 1 recommandée)",
                    "REM commentaire - Commentaire (ignoré à l'exécution)",
                    ":: commentaire - Commentaire alternatif (plus rapide)",
                    "echo texte - Afficher texte à l'écran",
                    "echo. - Ligne vide",
                    "pause - Attendre appui touche utilisateur",
                    "title Titre - Changer titre fenêtre CMD",
                    "cls - Effacer écran",
                    "exit - Fermer script (ou exit /b pour sortir sans fermer)",
                    "goto :label - Sauter à une étiquette"
                ]
            },
            {
                "title": "Variables dans Batch",
                "code": "@echo off\nREM Définir variables\nset NAME=Jean\nset AGE=30\nset FOLDER=C:\\Backup\n\nREM Utiliser variables (avec %)\necho Bonjour %NAME%, vous avez %AGE% ans.\necho Dossier: %FOLDER%\n\nREM Demander input utilisateur\nset /p USERNAME=\"Entrez votre nom: \"\necho Bonjour %USERNAME%!\n\nREM Variables d'environnement système\necho PC: %COMPUTERNAME%\necho User: %USERNAME%\necho Temp: %TEMP%\n\nREM Calculs\nset /a RESULT=10+5\necho 10 + 5 = %RESULT%\n\nset /a YEAR=2025\nset /a NEXT_YEAR=%YEAR%+1\necho Année prochaine: %NEXT_YEAR%\n\npause"
            },
            {
                "title": "Conditions If/Else",
                "code": "@echo off\nREM Vérifier si fichier existe\nif exist \"C:\\test.txt\" (\n    echo Fichier existe!\n    del \"C:\\test.txt\"\n) else (\n    echo Fichier introuvable.\n    echo Création fichier...\n    echo Contenu > C:\\test.txt\n)\n\nREM Comparer valeurs\nset /p AGE=\"Votre âge: \"\nif %AGE% GEQ 18 (\n    echo Vous êtes majeur.\n) else (\n    echo Vous êtes mineur.\n)\n\nREM Comparer chaînes (insensible casse avec /i)\nset /p CHOICE=\"Continuer? (oui/non): \"\nif /i \"%CHOICE%\"==\"oui\" (\n    echo OK, on continue!\n) else (\n    echo Arrêt du script.\n    exit\n)\n\nREM Vérifier dossier\nif exist \"C:\\Backup\\\" (\n    echo Dossier Backup existe.\n) else (\n    mkdir \"C:\\Backup\"\n    echo Dossier Backup créé.\n)\n\npause"
            },
            {
                "title": "Boucles For",
                "code": "@echo off\nREM Boucle sur fichiers\necho Liste fichiers .txt:\nfor %%f in (*.txt) do (\n    echo - %%f\n)\n\nREM Boucle récursive (/r)\necho Tous .log dans C:\\Logs:\nfor /r \"C:\\Logs\" %%f in (*.log) do (\n    echo %%f\n)\n\nREM Boucle sur dossiers (/d)\nfor /d %%d in (C:\\*) do (\n    echo Dossier: %%d\n)\n\nREM Boucle numérique (/l)\necho Compteur 1 à 10:\nfor /l %%i in (1,1,10) do (\n    echo %%i\n)\n\nREM Boucle sur lignes fichier (/f)\necho Lire fichier ligne par ligne:\nfor /f \"tokens=*\" %%a in (fichier.txt) do (\n    echo %%a\n)\n\nREM Boucle sur résultat commande\nfor /f \"tokens=*\" %%a in ('dir /b *.txt') do (\n    echo Fichier trouvé: %%a\n)\n\npause"
            },
            {
                "title": "Fonctions (Étiquettes et CALL)",
                "code": "@echo off\n\nREM Appeler fonctions\ncall :SayHello\ncall :Backup \"C:\\ImportantData\" \"D:\\Backups\"\ngoto :EOF\n\nREM ===== FONCTIONS =====\n\n:SayHello\necho =============================\necho   Bienvenue dans le script!\necho =============================\ngoto :EOF\n\n:Backup\nset SOURCE=%~1\nset DEST=%~2\necho Sauvegarde %SOURCE% vers %DEST%...\nxcopy \"%SOURCE%\" \"%DEST%\" /E /I /Y\nif %ERRORLEVEL%==0 (\n    echo [OK] Sauvegarde réussie!\n) else (\n    echo [ERREUR] Échec sauvegarde!\n)\ngoto :EOF"
            },
            {
                "title": "Gestion Erreurs (ERRORLEVEL)",
                "code": "@echo off\nREM Tester succès commande\n\nping google.com -n 1 >NUL 2>&1\nif %ERRORLEVEL%==0 (\n    echo Internet: OK\n) else (\n    echo Internet: OFFLINE\n    exit /b 1\n)\n\nREM Créer dossier et vérifier\nmkdir \"C:\\Test\" 2>NUL\nif %ERRORLEVEL%==0 (\n    echo Dossier créé.\n) else (\n    echo Dossier existe déjà ou erreur.\n)\n\nREM Copier et vérifier\ncopy source.txt dest.txt >NUL 2>&1\nif %ERRORLEVEL%==0 (\n    echo Copie réussie!\n) else (\n    echo Erreur copie! Code: %ERRORLEVEL%\n    exit /b %ERRORLEVEL%\n)\n\npause"
            },
            {
                "title": "Script Batch Complet: Sauvegarde Automatique",
                "code": "@echo off\ntitle Sauvegarde Automatique\ncolor 0A\n\nREM =====================================================\nREM Script de Sauvegarde avec Horodatage et Logs\nREM =====================================================\n\nREM Configuration\nset SOURCE=C:\\ImportantData\nset DEST=D:\\Backups\nset LOGFILE=%DEST%\\backup_log.txt\n\nREM Vérifier source existe\nif not exist \"%SOURCE%\" (\n    echo [ERREUR] Source introuvable: %SOURCE%\n    echo [ERREUR] Source introuvable: %SOURCE% >> \"%LOGFILE%\"\n    pause\n    exit /b 1\n)\n\nREM Créer dossier destination si besoin\nif not exist \"%DEST%\" mkdir \"%DEST%\"\n\nREM Horodatage\nfor /f \"tokens=2 delims==\" %%a in ('wmic OS Get localdatetime /value') do set datetime=%%a\nset TIMESTAMP=%datetime:~0,8%_%datetime:~8,6%\nset BACKUP_FOLDER=%DEST%\\Backup_%TIMESTAMP%\n\nREM Démarrer sauvegarde\necho =============================\necho  Sauvegarde en cours...\necho =============================\necho.\necho Source: %SOURCE%\necho Destination: %BACKUP_FOLDER%\necho.\n\nREM Copie avec XCOPY (robuste)\nxcopy \"%SOURCE%\" \"%BACKUP_FOLDER%\\\" /E /I /Y /H /R\n\nREM Vérifier résultat\nif %ERRORLEVEL%==0 (\n    echo.\n    echo [OK] Sauvegarde terminée avec succès!\n    echo %date% %time% - Sauvegarde OK: %BACKUP_FOLDER% >> \"%LOGFILE%\"\n    color 0A\n) else (\n    echo.\n    echo [ERREUR] Échec sauvegarde! Code: %ERRORLEVEL%\n    echo %date% %time% - ERREUR sauvegarde (code %ERRORLEVEL%) >> \"%LOGFILE%\"\n    color 0C\n    pause\n    exit /b %ERRORLEVEL%\n)\n\nREM Nettoyage: supprimer sauvegardes > 30 jours\necho.\necho Nettoyage anciennes sauvegardes (>30 jours)...\nforfiles /p \"%DEST%\" /m Backup_* /d -30 /c \"cmd /c echo Suppression: @path & rd /s /q @path\" 2>NUL\n\necho.\necho Terminé!\npause"
            },
            {
                "info": "💡 Pour débugger un batch: Retirez '@echo off' pour voir chaque commande exécutée, ou ajoutez 'echo' avant commandes problématiques."
            },
            {
                "warning": "⚠️ Les scripts batch peuvent exécuter commandes destructives (del, format, rd). TESTEZ TOUJOURS sur données non critiques avant production."
            }
        ]
    },

    "cmd_network": {
        "title": "🌐 CMD - Commandes Réseau Avancées",
        "sections": [
            {
                "title": "Diagnostics Réseau Complets",
                "code": "REM Configuration IP détaillée\nipconfig /all\nipconfig /all > config_reseau.txt  REM Sauvegarder\n\nREM Adaptateurs réseau\nipconfig /all | find \"Carte\"\n\nREM Libérer/Renouveler IP (DHCP)\nipconfig /release\nipconfig /renew\nipconfig /renew \"Ethernet\"  REM Adaptateur spécifique\n\nREM Vider caches réseau\nipconfig /flushdns        REM Cache DNS\nnetsh winsock reset       REM Winsock (ADMIN, redémarrage)\nnetsh int ip reset        REM Stack TCP/IP (ADMIN, redémarrage)\n\nREM Afficher cache DNS\nipconfig /displaydns\nipconfig /displaydns | find \"google\""
            },
            {
                "title": "Ping Avancé",
                "code": "REM Ping basique\nping google.com\nping 8.8.8.8\n\nREM Ping continu (Ctrl+C pour arrêter)\nping -t google.com\n\nREM Nombre de paquets spécifique\nping -n 100 8.8.8.8    REM 100 pings\n\nREM Taille paquet custom\nping -l 1500 google.com  REM 1500 bytes (test MTU)\n\nREM Ping avec timeout\nping -w 5000 192.168.1.1  REM Timeout 5 secondes\n\nREM Ne pas fragmenter (test MTU)\nping -f -l 1472 google.com  REM Taille max sans fragmentation\n\nREM Ping via route spécifique (loose source route)\nping -j 192.168.1.1 google.com\n\nREM IPv6\nping -6 google.com\nping ::1  REM Localhost IPv6"
            },
            {
                "title": "Traceroute (Tracert)",
                "code": "REM Tracer route vers destination\ntracert google.com\ntracert 8.8.8.8\n\nREM Ne pas résoudre noms (plus rapide)\ntracert -d google.com\n\nREM Max sauts custom\ntracert -h 20 google.com  REM 20 sauts max (défaut: 30)\n\nREM Timeout custom\ntracert -w 2000 google.com  REM 2 secondes\n\nREM Chemin complet\ntracert -d -h 50 google.com > traceroute.txt"
            },
            {
                "title": "NetStat - Connexions Actives",
                "code": "REM Toutes connexions actives\nnetstat\n\nREM Avec adresses numériques (plus rapide)\nnetstat -n\n\nREM Ports en écoute\nnetstat -a         REM Tous\nnetstat -an        REM Numériques\nnetstat -ano       REM + PID processus (très utile!)\n\nREM Filtrer par protocole\nnetstat -an | find \"ESTABLISHED\"  REM Connexions établies\nnetstat -an | find \"LISTENING\"    REM Ports en écoute\nnetstat -an | find \":80\"          REM Port 80 (HTTP)\nnetstat -an | find \":443\"         REM Port 443 (HTTPS)\n\nREM Statistiques protocoles\nnetstat -s         REM Statistiques détaillées\nnetstat -s -p tcp  REM TCP seulement\nnetstat -s -p udp  REM UDP seulement\n\nREM Table routage\nnetstat -r\nroute print  REM Équivalent\n\nREM Programmes utilisant réseau (ADMIN)\nnetstat -b     REM Avec noms exécutables\nnetstat -bano  REM Complet (connexions + programmes + PID)\n\nREM Rafraîchir toutes les 5 secondes\nnetstat -ano 5"
            },
            {
                "title": "NSLookup - DNS",
                "code": "REM Lookup DNS basique\nnslookup google.com\n\nREM Utiliser serveur DNS spécifique\nnslookup google.com 8.8.8.8        REM DNS Google\nnslookup google.com 1.1.1.1        REM DNS Cloudflare\nnslookup google.com 208.67.222.222 REM DNS OpenDNS\n\nREM Types d'enregistrements\nnslookup -type=A google.com     REM Adresses IPv4\nnslookup -type=AAAA google.com  REM Adresses IPv6\nnslookup -type=MX google.com    REM Serveurs mail\nnslookup -type=NS google.com    REM Serveurs DNS autoritaires\nnslookup -type=TXT google.com   REM Enregistrements TXT\nnslookup -type=CNAME www.google.com  REM Alias\n\nREM Mode interactif\nnslookup\n> server 8.8.8.8\n> set type=MX\n> google.com\n> exit"
            },
            {
                "title": "Netsh - Configuration Réseau (ADMIN)",
                "code": "REM Afficher interfaces\nnetsh interface show interface\nnetsh interface ipv4 show config\n\nREM Configurer IP statique (ADMIN)\nnetsh interface ipv4 set address \"Ethernet\" static 192.168.1.100 255.255.255.0 192.168.1.1\n\nREM Configurer DNS (ADMIN)\nnetsh interface ipv4 set dns \"Ethernet\" static 8.8.8.8\nnetsh interface ipv4 add dns \"Ethernet\" 8.8.4.4 index=2\n\nREM Revenir en DHCP (ADMIN)\nnetsh interface ipv4 set address \"Ethernet\" dhcp\nnetsh interface ipv4 set dns \"Ethernet\" dhcp\n\nREM Reset stack TCP/IP (ADMIN, redémarrage)\nnetsh int ip reset\nnetsh winsock reset\n\nREM Désactiver/Activer interface (ADMIN)\nnetsh interface set interface \"Ethernet\" disable\nnetsh interface set interface \"Ethernet\" enable\n\nREM Profils WiFi\nnetsh wlan show profiles\nnetsh wlan show profile name=\"MonWiFi\" key=clear  REM Mot de passe WiFi\nnetsh wlan export profile name=\"MonWiFi\" folder=C:\\  REM Exporter\n\nREM Pare-feu Windows\nnetsh advfirewall show allprofiles\nnetsh advfirewall set allprofiles state on   REM Activer (ADMIN)\nnetsh advfirewall set allprofiles state off  REM Désactiver (ADMIN)"
            },
            {
                "title": "ARP - Table ARP",
                "code": "REM Afficher table ARP\narp -a\n\nREM ARP spécifique\narp -a 192.168.1.1\n\nREM Ajouter entrée statique (ADMIN)\narp -s 192.168.1.100 00-11-22-33-44-55\n\nREM Supprimer entrée\narp -d 192.168.1.100\n\nREM Vider table ARP\narp -d *"
            },
            {
                "title": "PathPing - Traceroute + Ping Hybride",
                "code": "REM Analyse réseau approfondie (lent mais précis)\npathping google.com\npathping -n google.com  REM Sans résolution DNS\npathping -h 20 -q 10 google.com  REM 20 sauts, 10 pings par saut"
            },
            {
                "title": "GetMAC - Adresse MAC",
                "code": "REM Afficher adresses MAC\ngetmac\ngetmac /v         REM Verbose\ngetmac /v /fo table  REM Format tableau\n\nREM MAC ordinateur distant\ngetmac /s NomPC /u Utilisateur /p MotDePasse"
            },
            {
                "title": "Script Diagnostic Réseau Complet",
                "code": "@echo off\ntitle Diagnostic Réseau Complet\ncolor 0B\necho =====================================================\necho          DIAGNOSTIC RESEAU COMPLET\necho =====================================================\necho.\n\nset LOGFILE=diagnostic_reseau_%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%.txt\necho Rapport: %LOGFILE%\necho.\n\nREM Configuration IP\necho [1/7] Configuration IP...\nipconfig /all >> \"%LOGFILE%\"\necho OK\n\nREM DNS Cache\necho [2/7] Cache DNS...\nipconfig /displaydns >> \"%LOGFILE%\"\necho OK\n\nREM Connexions actives\necho [3/7] Connexions actives...\nnetstat -ano >> \"%LOGFILE%\"\necho OK\n\nREM Table routage\necho [4/7] Table de routage...\nroute print >> \"%LOGFILE%\"\necho OK\n\nREM ARP\necho [5/7] Table ARP...\narp -a >> \"%LOGFILE%\"\necho OK\n\nREM Test connectivité\necho [6/7] Tests connectivité...\necho. >> \"%LOGFILE%\"\necho === PING TESTS === >> \"%LOGFILE%\"\necho Passerelle:\nping -n 4 %gateway% >> \"%LOGFILE%\"\necho DNS Google:\nping -n 4 8.8.8.8 >> \"%LOGFILE%\"\necho Internet:\nping -n 4 google.com >> \"%LOGFILE%\"\necho OK\n\nREM Traceroute\necho [7/7] Traceroute...\necho. >> \"%LOGFILE%\"\necho === TRACEROUTE === >> \"%LOGFILE%\"\ntracert -d -h 15 google.com >> \"%LOGFILE%\"\necho OK\n\necho.\necho =====================================================\necho Diagnostic terminé!\necho Rapport sauvegardé: %LOGFILE%\necho =====================================================\npause\nnotepad \"%LOGFILE%\""
            },
            {
                "info": "💡 Pour identifier quel programme utilise un port: 'netstat -ano | find \":PORT\"' puis 'tasklist | find \"PID\"'."
            },
            {
                "warning": "⚠️ Commandes netsh modifiant la config réseau nécessitent ADMIN et peuvent couper votre connexion. Notez config actuelle avant modifications."
            }
        ]
    },

    # --- OPTIMISATION WINDOWS (5 guides) ---

    "opt_startup": {
        "title": "🚀 Optimiser le Démarrage de Windows",
        "sections": [
            {
                "title": "Pourquoi Optimiser le Démarrage?",
                "content": "Un démarrage lent de Windows est souvent causé par trop de programmes se lançant automatiquement. Optimiser le démarrage peut réduire le temps de boot de plusieurs minutes à quelques secondes, et améliorer significativement les performances globales du PC."
            },
            {
                "title": "Identifier les Programmes au Démarrage",
                "code": "# PowerShell - Lister programmes démarrage\nGet-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location\n\n# CMD - Via Gestionnaire des tâches\ntaskmgr  # Onglet 'Démarrage'\n\n# CMD - Via msconfig\nmsconfig  # Onglet 'Démarrage'\n\n# PowerShell - Dossiers startup\nGet-ChildItem \"$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"\nGet-ChildItem \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\""
            },
            {
                "title": "Méthode 1: Gestionnaire des Tâches (Windows 10/11)",
                "bullets": [
                    "Étape 1: Ctrl + Shift + Esc (ouvrir Gestionnaire des tâches)",
                    "Étape 2: Onglet 'Démarrage'",
                    "Étape 3: Identifier programmes avec 'Impact au démarrage' élevé",
                    "Étape 4: Clic droit → 'Désactiver' sur programmes non essentiels",
                    "Programmes SÛRS à désactiver: Skype, Spotify, Discord, Steam, Epic Games, Teams",
                    "Programmes À NE PAS désactiver: Antivirus, Drivers GPU/Audio, Windows Defender"
                ]
            },
            {
                "title": "Méthode 2: MSConfig (Toutes Versions Windows)",
                "bullets": [
                    "Étape 1: Win + R → taper 'msconfig' → Entrée",
                    "Étape 2: Onglet 'Démarrage'",
                    "Étape 3: Décocher programmes non nécessaires",
                    "Étape 4: Appliquer → OK → Redémarrer",
                    "Note: Windows 10/11 redirigent vers Gestionnaire des tâches"
                ]
            },
            {
                "title": "Méthode 3: PowerShell (Avancé)",
                "code": "# Désactiver programme démarrage via registre\n# ATTENTION: Modifier registre comporte des risques!\n\n# Lister clés démarrage\nGet-ItemProperty \"HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\"\nGet-ItemProperty \"HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\"\n\n# Supprimer entrée (exemple: OneDrive)\nRemove-ItemProperty -Path \"HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" -Name \"OneDrive\" -ErrorAction SilentlyContinue\n\n# Sauvegarder clés avant modification\nreg export \"HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" \"C:\\Backup_StartupRun_HKLM.reg\"\nreg export \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" \"C:\\Backup_StartupRun_HKCU.reg\""
            },
            {
                "title": "Méthode 4: Dossiers Startup",
                "bullets": [
                    "Dossier utilisateur: %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
                    "Dossier système: C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup",
                    "Supprimer raccourcis des programmes non voulus",
                    "Ou Win + R → 'shell:startup' pour accès rapide"
                ]
            },
            {
                "title": "Optimisations BIOS/UEFI",
                "bullets": [
                    "Activer Fast Boot (démarrage rapide UEFI)",
                    "Désactiver Logo écran démarrage",
                    "Définir SSD comme 1er périphérique boot",
                    "Désactiver périphériques boot inutilisés (lecteur réseau, etc.)",
                    "Activer AHCI pour SSD (si disponible)",
                    "Note: Accès BIOS généralement via F2/Del/F12 au démarrage"
                ]
            },
            {
                "title": "Services Windows à Désactiver (ADMIN)",
                "code": "# PowerShell - Désactiver services inutiles (ADMIN requis)\n\n# Bluetooth (si non utilisé)\nSet-Service -Name bthserv -StartupType Disabled\nStop-Service bthserv -Force\n\n# Fax (rarement utilisé)\nSet-Service -Name Fax -StartupType Disabled\nStop-Service Fax -Force\n\n# Print Spooler (si pas d'imprimante)\nSet-Service -Name Spooler -StartupType Disabled\nStop-Service Spooler -Force\n\n# Windows Search (si non utilisé, économise RAM)\nSet-Service -Name WSearch -StartupType Disabled\nStop-Service WSearch -Force\n\n# Xbox services (si non gamer)\nSet-Service -Name XblAuthManager -StartupType Disabled\nSet-Service -Name XblGameSave -StartupType Disabled\nSet-Service -Name XboxNetApiSvc -StartupType Disabled"
            },
            {
                "title": "Script PowerShell: Analyse Démarrage",
                "code": "# AnalyzeStartup.ps1\nWrite-Host \"=== ANALYSE DEMARRAGE WINDOWS ===\" -ForegroundColor Cyan\n\n# Programmes démarrage\nWrite-Host \"\\n1. Programmes au démarrage:\" -ForegroundColor Yellow\n$startup = Get-CimInstance Win32_StartupCommand\nforeach ($item in $startup) {\n    Write-Host \"  - $($item.Name): $($item.Command)\"\n}\n\n# Services auto\nWrite-Host \"\\n2. Services démarrage automatique:\" -ForegroundColor Yellow\n$autoServices = Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -eq 'Running'}\nWrite-Host \"  Total: $($autoServices.Count) services\"\n$autoServices | Select-Object Name, DisplayName | Format-Table -AutoSize\n\n# Tâches planifiées actives\nWrite-Host \"\\n3. Tâches planifiées actives:\" -ForegroundColor Yellow\n$tasks = Get-ScheduledTask | Where-Object {$_.State -eq 'Ready'}\nWrite-Host \"  Total: $($tasks.Count) tâches\"\n\n# Temps démarrage (uptime)\nWrite-Host \"\\n4. Uptime système:\" -ForegroundColor Yellow\n$uptime = (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime\nWrite-Host \"  Dernier démarrage: $([math]::Round($uptime.TotalMinutes, 2)) minutes\"\n\nWrite-Host \"\\n=== FIN ANALYSE ===\" -ForegroundColor Cyan"
            },
            {
                "title": "Fast Startup (Démarrage Rapide Windows)",
                "bullets": [
                    "Windows 10/11 ont 'Fast Startup' activé par défaut",
                    "Fast Startup = Hibernation partielle du noyau Windows",
                    "Avantage: Démarrage 30-50% plus rapide",
                    "Inconvénient: Peut causer problèmes dual-boot et pilotes",
                    "Désactiver si: Dual-boot Linux, problèmes réveil, mises à jour non appliquées"
                ]
            },
            {
                "title": "Désactiver Fast Startup",
                "code": "# PowerShell (ADMIN)\npowercfg /h off  # Désactive hibernation ET Fast Startup\n\n# OU garder hibernation mais désactiver Fast Startup via registre\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power\" -Name \"HiberbootEnabled\" -Value 0\n\n# Réactiver\npowercfg /h on\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power\" -Name \"HiberbootEnabled\" -Value 1"
            },
            {
                "info": "💡 Après optimisation, mesurez l'amélioration: Ouvrez Gestionnaire des tâches → Onglet 'Performance' → 'Durée d'activité' (temps depuis dernier démarrage)."
            },
            {
                "warning": "⚠️ NE désactivez JAMAIS: Antivirus, Windows Update, Drivers critiques (GPU, réseau). Cela peut compromettre sécurité et stabilité."
            }
        ]
    },

    "opt_disk": {
        "title": "💾 Optimisation Disque - Nettoyage & Performance",
        "sections": [
            {
                "title": "Pourquoi Optimiser le Disque?",
                "content": "Un disque encombré de fichiers temporaires, caches obsolètes, et applications inutiles ralentit Windows et occupe de l'espace précieux. Un nettoyage régulier améliore performances et prévient erreurs. Sur SSD, l'optimisation est DIFFÉRENTE de HDD (pas de défragmentation!)."
            },
            {
                "title": "SSD vs HDD: Différences Critiques",
                "bullets": [
                    "HDD (Disque Dur): Défragmenter AMÉLIORE performances (réorganise données physiquement)",
                    "SSD (Solid State): Défragmenter RÉDUIT durée de vie! (usure inutile)",
                    "SSD: Utiliser TRIM au lieu de défragmentation",
                    "Windows 10/11 gèrent automatiquement SSD vs HDD (optimisation planifiée)",
                    "Vérifier type disque: Gestionnaire des tâches → Performance → Sélectionner disque → Type affiché"
                ]
            },
            {
                "title": "Méthode 1: Nettoyage de Disque Windows (Intégré)",
                "bullets": [
                    "Étape 1: Ouvrir Explorateur → Clic droit disque C: → Propriétés",
                    "Étape 2: Onglet 'Général' → Bouton 'Nettoyage de disque'",
                    "Étape 3: Cocher: Fichiers temporaires, Corbeille, Miniatures, Téléchargements",
                    "Étape 4: 'Nettoyer fichiers système' (ADMIN) pour plus d'options",
                    "Étape 5: Cocher: Anciennes installations Windows, Fichiers journaux Windows Update",
                    "Étape 6: OK → Confirmer",
                    "Gain typique: 5-20 GB"
                ]
            },
            {
                "title": "Méthode 2: Paramètres Stockage Windows 10/11",
                "bullets": [
                    "Paramètres → Système → Stockage",
                    "Activer 'Assistant Stockage' (nettoyage automatique)",
                    "Cliquer 'Fichiers temporaires' → Cocher tout → Supprimer",
                    "Analyser 'Autres' pour trouver gros fichiers",
                    "Déplacer Documents/Images/Vidéos vers autre disque si possible"
                ]
            },
            {
                "title": "Méthode 3: PowerShell - Nettoyage Avancé",
                "code": "# Nettoyer fichiers temporaires (ADMIN recommandé)\n\n# 1. Dossier Temp utilisateur\nRemove-Item \"$env:TEMP\\*\" -Recurse -Force -ErrorAction SilentlyContinue\n\n# 2. Dossier Temp Windows\nRemove-Item \"C:\\Windows\\Temp\\*\" -Recurse -Force -ErrorAction SilentlyContinue\n\n# 3. Prefetch (cache programmes)\nRemove-Item \"C:\\Windows\\Prefetch\\*\" -Force -ErrorAction SilentlyContinue\n\n# 4. Vider corbeille\nClear-RecycleBin -Force -ErrorAction SilentlyContinue\n\n# 5. Cache thumbnails\nRemove-Item \"$env:LOCALAPPDATA\\Microsoft\\Windows\\Explorer\\thumbcache_*.db\" -Force -ErrorAction SilentlyContinue\n\n# 6. Logs Windows\nGet-ChildItem \"C:\\Windows\\Logs\" -Recurse -Filter *.log | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-30)} | Remove-Item -Force\n\n# 7. Fichiers téléchargements anciens (>90 jours)\n$downloadsPath = (New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path\nGet-ChildItem $downloadsPath | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-90)} | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue\n\nWrite-Host \"Nettoyage terminé!\" -ForegroundColor Green"
            },
            {
                "title": "Analyser Utilisation Disque",
                "code": "# PowerShell - Trouver gros fichiers/dossiers\n\n# Top 20 fichiers les plus gros sur C:\nGet-ChildItem C:\\ -Recurse -File -ErrorAction SilentlyContinue |\n    Sort-Object Length -Descending |\n    Select-Object -First 20 FullName, @{Name='Size(GB)';Expression={[math]::Round($_.Length/1GB, 2)}} |\n    Format-Table -AutoSize\n\n# Top 10 dossiers les plus gros\nGet-ChildItem C:\\ -Directory -ErrorAction SilentlyContinue |\n    ForEach-Object {\n        $size = (Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum\n        [PSCustomObject]@{\n            Folder = $_.FullName\n            'Size(GB)' = [math]::Round($size / 1GB, 2)\n        }\n    } |\n    Sort-Object 'Size(GB)' -Descending |\n    Select-Object -First 10 |\n    Format-Table -AutoSize"
            },
            {
                "title": "Défragmentation (HDD SEULEMENT!)",
                "code": "# CMD/PowerShell - Défragmenter disque dur (PAS SSD!)\n\n# Analyser fragmentation\ndefrag C: /A\n\n# Défragmenter (ADMIN, long)\ndefrag C: /O\n\n# Défragmentation complète\ndefrag C: /U /V\n\n# Planifier défragmentation hebdomadaire (ADMIN)\ndefrag C: /O /H /U"
            },
            {
                "title": "TRIM pour SSD (Optimisation SSD)",
                "code": "# PowerShell - Vérifier TRIM activé (ADMIN)\nfsutil behavior query DisableDeleteNotify\n# Résultat 0 = TRIM activé (bon)\n# Résultat 1 = TRIM désactivé (à corriger)\n\n# Activer TRIM si désactivé (ADMIN)\nfsutil behavior set DisableDeleteNotify 0\n\n# Optimiser SSD manuellement (Windows fait déjà auto)\nOptimize-Volume -DriveLetter C -ReTrim -Verbose\n\n# CMD équivalent\ndefrag C: /L  # /L = TRIM pour SSD"
            },
            {
                "title": "Désinstaller Programmes Inutiles",
                "bullets": [
                    "Paramètres → Applications → Applications et fonctionnalités",
                    "Trier par taille pour identifier gros programmes",
                    "Désinstaller: Bloatware, trials expirés, doublons",
                    "Outils tiers recommandés: Revo Uninstaller, Geek Uninstaller (suppression complète)"
                ]
            },
            {
                "title": "Désinstaller via PowerShell/Winget",
                "code": "# PowerShell - Lister applications installées\nGet-AppxPackage | Select-Object Name, Version\n\n# Désinstaller application Windows Store\nGet-AppxPackage *CandyCrush* | Remove-AppxPackage\n\n# Winget - Lister programmes\nwinget list\n\n# Désinstaller via Winget\nwinget uninstall --id NomProgramme"
            },
            {
                "title": "Windows.old (Anciennes Installations)",
                "bullets": [
                    "Windows.old = Ancienne version Windows conservée après mise à jour",
                    "Taille: 10-30 GB généralement",
                    "Supprimer si tout fonctionne bien (irréversible!)",
                    "Nettoyage disque → Cocher 'Installations Windows précédentes'",
                    "Ou: Paramètres → Stockage → Fichiers temporaires → Cocher 'Installations Windows précédentes'"
                ]
            },
            {
                "title": "WinSxS (Windows Side-by-Side)",
                "content": "WinSxS est un dossier système (C:\\Windows\\WinSxS) pouvant atteindre 10-15 GB. NE PAS supprimer manuellement! Windows l'utilise pour composants système. Nettoyer via:"
            },
            {
                "code": "# DISM - Nettoyer WinSxS (ADMIN, lent)\nDISM /Online /Cleanup-Image /AnalyzeComponentStore  # Analyse\nDISM /Online /Cleanup-Image /StartComponentCleanup   # Nettoyage\nDISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase  # Nettoyage agressif (irréversible)"
            },
            {
                "title": "Hiberfil.sys (Fichier Hibernation)",
                "bullets": [
                    "Hiberfil.sys = Fichier hibernation (taille = RAM installée)",
                    "Exemple: 16 GB RAM = 16 GB fichier",
                    "Supprimer si: Jamais utiliser hibernation, PC fixe, SSD petit",
                    "Conserver si: Laptop, utilise hibernation/Fast Startup"
                ]
            },
            {
                "code": "# PowerShell - Désactiver hibernation (supprime hiberfil.sys)\npowercfg /h off\n\n# Réactiver\npowercfg /h on\n\n# Réduire taille (50% RAM)\npowercfg /h /type reduced"
            },
            {
                "info": "💡 Outils tiers recommandés: WinDirStat (visualiser espace disque), TreeSize Free, CCleaner (avec prudence)."
            },
            {
                "warning": "⚠️ JAMAIS défragmenter un SSD! Cela réduit sa durée de vie sans bénéfice. Utilisez TRIM uniquement. Vérifiez type disque avant optimisation."
            }
        ]
    },

    "opt_memory": {
        "title": "🧠 Gestion Mémoire RAM - Optimisation",
        "sections": [
            {
                "title": "Comprendre l'Utilisation RAM",
                "content": "Windows utilise la RAM pour charger programmes et données actifs. Plus de RAM libre = meilleures performances. Cependant, Windows CACHE intelligemment: RAM 'utilisée' n'est pas toujours mauvais. Le problème apparaît quand RAM physique est saturée et Windows utilise fichier d'échange (swap) sur disque, causant ralentissements majeurs."
            },
            {
                "title": "Vérifier Utilisation RAM Actuelle",
                "code": "# PowerShell - Infos RAM\nGet-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory, @{Name='UsedMemory(GB)';Expression={[math]::Round(($_.TotalVisibleMemorySize - $_.FreePhysicalMemory)/1MB, 2)}}\n\n# CMD - Systeminfo\nsysteminfo | find \"Mémoire\"\n\n# PowerShell - Processus consommant le plus de RAM\nGet-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Name, @{Name='RAM(MB)';Expression={[math]::Round($_.WS/1MB, 2)}} | Format-Table -AutoSize"
            },
            {
                "title": "Identifier Processus Gourmands",
                "bullets": [
                    "Ctrl + Shift + Esc → Gestionnaire des tâches",
                    "Onglet 'Processus' → Trier par 'Mémoire'",
                    "Processus normalement gourmands: Chrome/Edge (plusieurs onglets), IDEs, jeux",
                    "Processus suspects: Inconnus, multiples instances, consommation excessive constante",
                    "Clic droit suspect → 'Fin de tâche' (ou 'Rechercher en ligne' pour identifier)"
                ]
            },
            {
                "title": "Libérer RAM Rapidement",
                "code": "# PowerShell - Vider cache RAM (effet temporaire)\n\n# Méthode 1: Clear Standby Cache (nécessite RAMMap/Sysinternals)\n# Télécharger RAMMap: https://docs.microsoft.com/sysinternals/downloads/rammap\n# Exécuter: RAMMap.exe -Ew  (vide cache standby)\n\n# Méthode 2: Script PowerShell (effet limité)\n[System.GC]::Collect()\n[System.GC]::WaitForPendingFinalizers()\n\n# Méthode 3: Arrêter processus non essentiels\nGet-Process | Where-Object {$_.ProcessName -like '*chrome*' -or $_.ProcessName -like '*Teams*'} | Stop-Process -Force\n\n# Méthode 4: Vider cache DNS\nipconfig /flushdns\n\n# Méthode 5: Redémarrer Explorer.exe\nStop-Process -Name explorer -Force\nStart-Process explorer"
            },
            {
                "title": "Désactiver Programmes en Arrière-Plan",
                "bullets": [
                    "Paramètres → Confidentialité → Applications en arrière-plan",
                    "Désactiver applications non nécessaires",
                    "Windows 11: Paramètres → Applications → Applications installées → Cliquer app → Options avancées → Autorisations arrière-plan → Jamais"
                ]
            },
            {
                "title": "Optimiser Effets Visuels (Économise RAM)",
                "bullets": [
                    "Panneau de configuration → Système → Paramètres système avancés",
                    "Onglet 'Performances' → Bouton 'Paramètres'",
                    "Sélectionner 'Ajuster afin d'obtenir les meilleures performances'",
                    "Ou personnaliser: Garder 'Lisser polices écran', désactiver reste",
                    "Gain: 200-500 MB RAM selon configuration"
                ]
            },
            {
                "title": "Fichier d'Échange (Pagefile.sys)",
                "content": "Le fichier d'échange (swap) est utilisé quand RAM physique est pleine. Windows y stocke données RAM rarement utilisées. SSD rend swap acceptable, mais HDD le rend TRÈS lent. Optimisations possibles:"
            },
            {
                "title": "Configurer Taille Pagefile",
                "bullets": [
                    "Paramètres → Système → À propos → Paramètres système avancés",
                    "Onglet 'Avancé' → Performances → Paramètres → Onglet 'Avancé'",
                    "Mémoire virtuelle → Modifier",
                    "Recommandation standard: 1.5x RAM (Taille initiale = 1.5x RAM, Max = 3x RAM)",
                    "Exemple: 16 GB RAM → Initial 24 GB, Max 48 GB",
                    "Sur SSD: Réduire ou désactiver si 16+ GB RAM",
                    "Sur HDD: Garder actif mais mettre sur disque le plus rapide"
                ]
            },
            {
                "code": "# PowerShell - Config pagefile (ADMIN)\n\n# Désactiver gestion automatique\n$sys = Get-WmiObject Win32_ComputerSystem -EnableAllPrivileges\n$sys.AutomaticManagedPagefile = $false\n$sys.Put()\n\n# Définir taille custom (exemple: 4096 MB initial, 8192 MB max)\n$pagefileset = Get-WmiObject Win32_PageFileSetting\n$pagefileset.InitialSize = 4096\n$pagefileset.MaximumSize = 8192\n$pagefileset.Put()\n\n# Réactiver gestion automatique\n$sys.AutomaticManagedPagefile = $true\n$sys.Put()"
            },
            {
                "title": "Superfetch/SysMain (Préchargement RAM)",
                "content": "Superfetch (SysMain sur Win10+) précharge programmes fréquents en RAM. Utile sur HDD, mais inutile/problématique sur SSD. Désactiver sur SSD pour libérer RAM."
            },
            {
                "code": "# PowerShell - Désactiver Superfetch/SysMain (ADMIN)\nStop-Service -Name \"SysMain\" -Force\nSet-Service -Name \"SysMain\" -StartupType Disabled\n\n# Réactiver (si HDD)\nSet-Service -Name \"SysMain\" -StartupType Automatic\nStart-Service -Name \"SysMain\""
            },
            {
                "title": "Windows Search Indexing",
                "content": "L'indexation Windows (service 'Windows Search') consomme RAM et CPU pour indexer fichiers. Utile si recherche fréquente de fichiers, mais peut être désactivé sur PC avec SSD ou si recherche rarement utilisée."
            },
            {
                "code": "# PowerShell - Désactiver Windows Search (ADMIN)\nStop-Service -Name \"WSearch\" -Force\nSet-Service -Name \"WSearch\" -StartupType Disabled\n\n# Réactiver\nSet-Service -Name \"WSearch\" -StartupType Automatic\nStart-Service -Name \"WSearch\""
            },
            {
                "title": "Fuites Mémoire (Memory Leaks)",
                "content": "Une fuite mémoire survient quand un programme ne libère pas RAM après usage, causant augmentation progressive consommation RAM jusqu'à saturation. Identifier:"
            },
            {
                "bullets": [
                    "Surveillance Gestionnaire des tâches: RAM d'un processus augmente constamment",
                    "Redémarrage programme résout temporairement",
                    "Solutions: Mettre à jour programme, signaler bug développeur, redémarrer régulièrement",
                    "Programmes connus pour fuites: Chrome (nombreux onglets), Electron apps, drivers mal codés"
                ]
            },
            {
                "title": "Script Surveillance RAM",
                "code": "# PowerShell - Surveiller RAM temps réel\nparam([int]$Threshold = 80)  # Alerte si >80% RAM utilisée\n\nWrite-Host \"Surveillance RAM (seuil: $Threshold%)\" -ForegroundColor Cyan\nWrite-Host \"Appuyez sur Ctrl+C pour arrêter...\\n\"\n\nwhile ($true) {\n    $os = Get-CimInstance Win32_OperatingSystem\n    $totalRAM = $os.TotalVisibleMemorySize / 1MB\n    $freeRAM = $os.FreePhysicalMemory / 1MB\n    $usedRAM = $totalRAM - $freeRAM\n    $usedPercent = [math]::Round(($usedRAM / $totalRAM) * 100, 1)\n    \n    $color = \"Green\"\n    if ($usedPercent -gt $Threshold) {\n        $color = \"Red\"\n        # Top 5 processus RAM\n        $topProcs = Get-Process | Sort-Object WS -Descending | Select-Object -First 5\n        Write-Host \"\\n[ALERTE] RAM > $Threshold% !\" -ForegroundColor Red\n        Write-Host \"Top 5 processus:\" -ForegroundColor Yellow\n        foreach ($proc in $topProcs) {\n            Write-Host \"  - $($proc.Name): $([math]::Round($proc.WS/1MB, 2)) MB\"\n        }\n    }\n    \n    Write-Host \"[$([datetime]::Now.ToString('HH:mm:ss'))] RAM: $([math]::Round($usedRAM, 2)) GB / $([math]::Round($totalRAM, 2)) GB ($usedPercent%)\" -ForegroundColor $color\n    \n    Start-Sleep -Seconds 5\n}"
            },
            {
                "info": "💡 Règle d'or: Si utilisation RAM >85% constante, envisager upgrade RAM (ex: 8→16 GB). Optimisations logicielles ont limites."
            },
            {
                "warning": "⚠️ Désactiver fichier d'échange (pagefile) sur PC avec <16 GB RAM peut causer crashes. Conserver au minimum 2-4 GB même avec 32 GB RAM."
            }
        ]
    },

    "opt_network": {
        "title": "🌐 Optimisation Réseau - Performance & Latence",
        "sections": [
            {
                "title": "Pourquoi Optimiser le Réseau?",
                "content": "Une connexion Internet lente ou instable peut provenir de mauvaise configuration réseau Windows, DNS lents, ou paramètres TCP/IP non optimisés. Optimiser le réseau réduit latence (ping), améliore vitesse téléchargement, et stabilise connexion, essentiels pour gaming, streaming, et travail à distance."
            },
            {
                "title": "Diagnostiquer Problèmes Réseau",
                "code": "# PowerShell - Tests basiques\n# 1. Test connectivité Internet\nTest-Connection 8.8.8.8 -Count 4  # Ping DNS Google\n\n# 2. Test DNS\nResolve-DnsName google.com\n\n# 3. Test vitesse (nécessite Speedtest-CLI)\n# Installer: winget install Ookla.Speedtest.CLI\nspeedtest  # Mesure download/upload/ping\n\n# 4. Adaptateur réseau\nGet-NetAdapter\nGet-NetIPAddress -AddressFamily IPv4"
            },
            {
                "title": "Optimisation #1: Changer DNS (Impact Majeur!)",
                "content": "DNS lents (souvent ceux du FAI) causent lenteur chargement pages. Utiliser DNS publics rapides réduit latence de 20-100ms."
            },
            {
                "bullets": [
                    "DNS Google: 8.8.8.8 / 8.8.4.4 (fiable, rapide)",
                    "Cloudflare: 1.1.1.1 / 1.0.0.1 (le plus rapide généralement)",
                    "OpenDNS: 208.67.222.222 / 208.67.220.220 (filtrage contenu)",
                    "Quad9: 9.9.9.9 / 149.112.112.112 (sécurité/privacy)"
                ]
            },
            {
                "title": "Changer DNS via Interface Windows",
                "bullets": [
                    "Étape 1: Panneau de configuration → Centre Réseau → Modifier paramètres carte",
                    "Étape 2: Clic droit carte réseau → Propriétés",
                    "Étape 3: Sélectionner 'Protocole Internet version 4 (TCP/IPv4)' → Propriétés",
                    "Étape 4: Cocher 'Utiliser l'adresse de serveur DNS suivante'",
                    "Étape 5: DNS préféré: 1.1.1.1 / DNS auxiliaire: 1.0.0.1",
                    "Étape 6: OK → Fermer",
                    "Étape 7: Ouvrir CMD → ipconfig /flushdns"
                ]
            },
            {
                "title": "Changer DNS via PowerShell (ADMIN)",
                "code": "# Lister adaptateurs\nGet-NetAdapter | Where-Object {$_.Status -eq 'Up'}\n\n# Définir DNS Cloudflare (exemple: Ethernet)\nSet-DnsClientServerAddress -InterfaceAlias \"Ethernet\" -ServerAddresses (\"1.1.1.1\", \"1.0.0.1\")\n\n# Définir DNS Google\nSet-DnsClientServerAddress -InterfaceAlias \"Ethernet\" -ServerAddresses (\"8.8.8.8\", \"8.8.4.4\")\n\n# Revenir DNS automatique (DHCP)\nSet-DnsClientServerAddress -InterfaceAlias \"Ethernet\" -ResetServerAddresses\n\n# Vider cache DNS\nClear-DnsClientCache"
            },
            {
                "title": "Optimisation #2: Reset Stack TCP/IP",
                "content": "Corruption stack TCP/IP cause déconnexions, lenteur, erreurs réseau. Reset netsh résout 80% problèmes réseau inexpliqués."
            },
            {
                "code": "# CMD/PowerShell (ADMIN - REDÉMARRAGE REQUIS)\n\n# 1. Reset Winsock (couche réseau Windows)\nnetsh winsock reset\n\n# 2. Reset stack TCP/IP\nnetsh int ip reset\n\n# 3. Vider cache DNS, ARP, NetBIOS\nipconfig /flushdns\narp -d *\nnbtstat -R\n\n# 4. Renouveler IP\nipconfig /release\nipconfig /renew\n\n# 5. Redémarrer\nshutdown /r /t 0"
            },
            {
                "title": "Optimisation #3: Tweaks Registre TCP/IP (Avancé)",
                "code": "# PowerShell (ADMIN) - Optimiser paramètres TCP/IP\n\n# Désactiver Auto-Tuning (parfois cause problèmes)\nnetsh int tcp set global autotuninglevel=disabled\n\n# OU Activer Auto-Tuning (améliore débit)\nnetsh int tcp set global autotuninglevel=normal\n\n# Augmenter taille fenêtre TCP (meilleur débit)\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\" -Name \"Tcp1323Opts\" -Value 3\n\n# Désactiver Nagle Algorithm (réduit latence gaming)\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\*\" -Name \"TcpAckFrequency\" -Value 1\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\*\" -Name \"TCPNoDelay\" -Value 1\n\n# Activer RSS (Receive Side Scaling) pour multi-core\nnetsh int tcp set global rss=enabled"
            },
            {
                "title": "Optimisation #4: QoS (Quality of Service)",
                "content": "Windows réserve 20% bande passante pour QoS par défaut. Désactiver libère bande passante (gain marginal mais facile)."
            },
            {
                "code": "# PowerShell (ADMIN) - Désactiver réservation QoS\nSet-ItemProperty -Path \"HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\" -Name \"NonBestEffortLimit\" -Value 0 -Force\n\n# Ou via Éditeur de stratégie de groupe (gpedit.msc)\n# Configuration ordinateur → Modèles admin → Réseau → Planificateur QoS\n# \"Limiter bande passante réservable\" → Activé → 0%"
            },
            {
                "title": "Optimisation #5: Désactiver IPv6 (Si Non Utilisé)",
                "content": "IPv6 rarement utilisé par FAI résidentiels. Désactiver évite conflits et accélère résolution DNS."
            },
            {
                "code": "# PowerShell (ADMIN)\nDisable-NetAdapterBinding -Name \"Ethernet\" -ComponentID ms_tcpip6\n\n# Réactiver si nécessaire\nEnable-NetAdapterBinding -Name \"Ethernet\" -ComponentID ms_tcpip6\n\n# Ou via registre (désactive globalement)\nSet-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip6\\Parameters\" -Name \"DisabledComponents\" -Value 0xFF"
            },
            {
                "title": "Optimisation #6: MTU (Maximum Transmission Unit)",
                "content": "MTU optimal évite fragmentation packets. MTU standard Ethernet = 1500. PPPoE (ADSL/VDSL) = 1492. Valeur incorrecte cause lenteur."
            },
            {
                "code": "# PowerShell - Trouver MTU optimal\n# Ping avec packets sans fragmentation (taille croissante)\nping google.com -f -l 1472  # 1472 + 28 headers = 1500\n# Si échec, réduire: ping google.com -f -l 1464, etc.\n\n# Définir MTU (ADMIN)\nnetsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent\n\n# Vérifier MTU actuel\nnetsh interface ipv4 show subinterfaces"
            },
            {
                "title": "Optimisation #7: Drivers Carte Réseau",
                "content": "Drivers réseau obsolètes causent déconnexions et lenteur. Mettre à jour améliore stabilité."
            },
            {
                "bullets": [
                    "Site fabricant: Intel, Realtek, Killer, Broadcom",
                    "Ou Gestionnaire périphériques → Cartes réseau → Clic droit → Mettre à jour",
                    "Désactiver gestion alimentation: Propriétés → Gestion alimentation → Décocher 'Autoriser PC à éteindre périphérique'"
                ]
            },
            {
                "title": "Script PowerShell: Optimisation Complète",
                "code": "# OptimizeNetwork.ps1 (ADMIN requis)\nWrite-Host \"=== OPTIMISATION RESEAU WINDOWS ===\" -ForegroundColor Cyan\n\n# 1. DNS Cloudflare\nWrite-Host \"\\n[1/6] Configuration DNS Cloudflare...\" -ForegroundColor Yellow\n$adapter = (Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | Select-Object -First 1).Name\nSet-DnsClientServerAddress -InterfaceAlias $adapter -ServerAddresses (\"1.1.1.1\", \"1.0.0.1\")\nWrite-Host \"✅ DNS: 1.1.1.1 / 1.0.0.1\"\n\n# 2. Vider caches\nWrite-Host \"\\n[2/6] Nettoyage caches...\" -ForegroundColor Yellow\nClear-DnsClientCache\nipconfig /flushdns | Out-Null\nWrite-Host \"✅ Caches vidés\"\n\n# 3. TCP Auto-Tuning\nWrite-Host \"\\n[3/6] TCP Auto-Tuning...\" -ForegroundColor Yellow\nnetsh int tcp set global autotuninglevel=normal | Out-Null\nWrite-Host \"✅ Auto-Tuning activé\"\n\n# 4. QoS\nWrite-Host \"\\n[4/6] Désactivation réservation QoS...\" -ForegroundColor Yellow\nSet-ItemProperty -Path \"HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\" -Name \"NonBestEffortLimit\" -Value 0 -Force -ErrorAction SilentlyContinue\nWrite-Host \"✅ QoS: 0% réservé\"\n\n# 5. IPv6\nWrite-Host \"\\n[5/6] Désactivation IPv6...\" -ForegroundColor Yellow\nDisable-NetAdapterBinding -Name $adapter -ComponentID ms_tcpip6 -ErrorAction SilentlyContinue\nWrite-Host \"✅ IPv6 désactivé\"\n\n# 6. Test final\nWrite-Host \"\\n[6/6] Test connectivité...\" -ForegroundColor Yellow\n$ping = Test-Connection 8.8.8.8 -Count 4 -Quiet\nif ($ping) {\n    Write-Host \"✅ Internet: OK\" -ForegroundColor Green\n} else {\n    Write-Host \"❌ Internet: OFFLINE\" -ForegroundColor Red\n}\n\nWrite-Host \"\\n=== OPTIMISATION TERMINÉE ===\" -ForegroundColor Cyan\nWrite-Host \"Redémarrez pour appliquer tous changements.\" -ForegroundColor Yellow"
            },
            {
                "info": "💡 Mesurez ping avant/après optimisations: ouvrez CMD → 'ping 8.8.8.8 -n 50' (moyenne sur 50 pings)."
            },
            {
                "warning": "⚠️ Reset TCP/IP (netsh int ip reset) nécessite redémarrage et peut requérir reconfiguration réseau. Notez config actuelle avant."
            }
        ]
    },

    "opt_gaming": {
        "title": "🎮 Optimisation Gaming - FPS & Latence",
        "sections": [
            {
                "title": "Optimisations Gaming Essentielles",
                "content": "Optimiser Windows pour le gaming implique réduire latence, augmenter FPS, désactiver services inutiles, et allouer ressources aux jeux. Gain typique: +10-30% FPS et -20-50ms latence selon config."
            },
            {
                "title": "Optimisation #1: Mode Jeu Windows (Game Mode)",
                "bullets": [
                    "Paramètres → Jeux → Mode Jeu → Activer",
                    "Prioritise ressources CPU/GPU pour jeu actif",
                    "Désactive mises à jour Windows/notifications pendant jeu",
                    "Gain: +5-15 FPS selon config"
                ]
            },
            {
                "title": "Optimisation #2: Désactiver Optimisations Plein Écran",
                "bullets": [
                    "Clic droit .exe jeu → Propriétés → Compatibilité",
                    "Cocher 'Désactiver optimisations plein écran'",
                    "Réduit input lag et améliore frametime",
                    "Essentiel pour jeux compétitifs (CS:GO, Valorant, Overwatch)"
                ]
            },
            {
                "title": "Optimisation #3: HAGS (Hardware Accelerated GPU Scheduling)",
                "content": "HAGS délègue gestion GPU au GPU lui-même (au lieu CPU), réduisant latence et libérant CPU. Disponible RTX 20xx+, GTX 10xx+, RX 5xxx+."
            },
            {
                "bullets": [
                    "Paramètres → Système → Affichage → Paramètres graphiques",
                    "Activer 'Planification GPU accélérée par matériel'",
                    "Redémarrer",
                    "Gain: Latence -5-10ms, +5-10 FPS",
                    "Note: Peut causer instabilité sur anciens drivers, désactiver si crashes"
                ]
            },
            {
                "code": "# PowerShell - Vérifier/Activer HAGS (ADMIN)\n# Vérifier si supporté\n$path = \"HKLM:\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\"\nGet-ItemProperty -Path $path -Name \"HwSchMode\" -ErrorAction SilentlyContinue\n# 1 = Désactivé, 2 = Activé\n\n# Activer HAGS\nSet-ItemProperty -Path $path -Name \"HwSchMode\" -Value 2\n\n# Désactiver HAGS (si problèmes)\nSet-ItemProperty -Path $path -Name \"HwSchMode\" -Value 1\n\n# Redémarrer pour appliquer"
            },
            {
                "title": "Optimisation #4: Power Plan Haute Performance",
                "bullets": [
                    "Panneau configuration → Options alimentation",
                    "Sélectionner 'Performances élevées' (ou créer plan custom)",
                    "Désactive throttling CPU, boost max fréquences",
                    "Essentiel laptop gaming (évite baisse FPS sur batterie)"
                ]
            },
            {
                "code": "# PowerShell - Activer Haute Performance (ADMIN)\npowercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61\npowercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c\n\n# Ou Ultimate Performance (Windows 10 Pro Workstation)\npowercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61\npowercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61"
            },
            {
                "title": "Optimisation #5: Priorité Processus",
                "content": "Définir priorité 'Haute' pour .exe jeu alloue plus ressources CPU/RAM."
            },
            {
                "code": "# PowerShell - Définir priorité (pendant jeu actif)\nGet-Process game.exe | ForEach-Object { $_.PriorityClass = 'High' }\n\n# Ou Gestionnaire tâches:\n# Ctrl+Shift+Esc → Détails → Clic droit game.exe → Priorité → Haute"
            },
            {
                "title": "Optimisation #6: Affinité CPU (Multi-Core)",
                "content": "Sur CPU 8+ cores, réserver cores physiques pour jeu évite partage avec processus background."
            },
            {
                "bullets": [
                    "Gestionnaire tâches → Détails → Clic droit game.exe → Affinité",
                    "Décocher Cores 0-1 (réservés système)",
                    "Cocher Cores 2-7 (exemple 8 cores)",
                    "Ou Process Lasso (outil tiers automatisation)"
                ]
            },
            {
                "title": "Optimisation #7: Désactiver Services Background",
                "code": "# PowerShell (ADMIN) - Désactiver services inutiles gaming\n\n# Windows Search (économise CPU/RAM)\nStop-Service WSearch -Force\nSet-Service WSearch -StartupType Disabled\n\n# SysMain/Superfetch\nStop-Service SysMain -Force\nSet-Service SysMain -StartupType Disabled\n\n# Print Spooler (si pas imprimante)\nStop-Service Spooler -Force\nSet-Service Spooler -StartupType Disabled\n\n# Xbox services (si non utilisés)\nStop-Service XblAuthManager, XblGameSave, XboxNetApiSvc -Force\nSet-Service XblAuthManager, XblGameSave, XboxNetApiSvc -StartupType Disabled"
            },
            {
                "title": "Optimisation #8: Tweaks GPU (NVIDIA)",
                "bullets": [
                    "NVIDIA Control Panel → Gérer paramètres 3D → Paramètres globaux:",
                    "Anisotropic Filtering: Application",
                    "Low Latency Mode: Ultra (réduit input lag)",
                    "Power Management: Prefer Maximum Performance",
                    "Texture Filtering Quality: High Performance",
                    "Vertical Sync: Off (ou G-Sync/FreeSync si supporté)",
                    "Max Frame Rate: Illimité (ou limite +10 FPS de taux rafraîchissement moniteur)"
                ]
            },
            {
                "title": "Optimisation #9: Tweaks GPU (AMD)",
                "bullets": [
                    "AMD Radeon Software → Gaming → Graphics:",
                    "Radeon Anti-Lag: Enabled (réduit latence)",
                    "Radeon Boost: Enabled (gain FPS dynamique)",
                    "Radeon Chill: Disabled (cap FPS indésirable)",
                    "Wait for Vertical Refresh: Off (ou FreeSync si supporté)",
                    "Texture Filtering Quality: Performance"
                ]
            },
            {
                "title": "Optimisation #10: MSI Mode (Interruptions GPU)",
                "content": "MSI Mode force GPU à utiliser Message Signaled Interrupts au lieu d'interruptions legacy, réduisant latence. Avancé!"
            },
            {
                "code": "# PowerShell (ADMIN) - Activer MSI Mode GPU\n# Télécharger MSI Utility V3: https://forums.guru3d.com/threads/windows-line-based-vs-message-signaled-based-interrupts-msi-tool.378044/\n# Ou via registre (exemple NVIDIA):\n\n$gpuPath = Get-ChildItem \"HKLM:\\SYSTEM\\CurrentControlSet\\Enum\\PCI\" -Recurse | Where-Object {$_.GetValue(\"DeviceDesc\") -like \"*NVIDIA*\"} | Select-Object -First 1\n$msiPath = Join-Path $gpuPath.PSPath \"Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties\"\nSet-ItemProperty -Path $msiPath -Name \"MSISupported\" -Value 1"
            },
            {
                "title": "Optimisation #11: Débloquer FPS (Config In-Game)",
                "bullets": [
                    "Désactiver V-Sync (sauf si screen tearing)",
                    "Définir limite FPS illimitée (ou 2x taux refresh)",
                    "Réduire qualité graphique inutile: Ombres (Medium), Anti-Aliasing (FXAA/TAA), Post-Processing (Low)",
                    "Prioriser: Textures (High si VRAM suffisante), View Distance, Model Detail"
                ]
            },
            {
                "title": "Optimisation #12: Overclock GPU/CPU (Avancé)",
                "bullets": [
                    "GPU: MSI Afterburner (+100-200 MHz core, +500-1000 MHz mémoire)",
                    "CPU: BIOS/UEFI ou Ryzen Master/Intel XTU",
                    "⚠️ Risques: Instabilité, crash, réduction durée vie si voltages excessifs",
                    "Testez avec: FurMark (GPU), Prime95 (CPU), 3DMark",
                    "Surveillez températures: <85°C GPU, <90°C CPU"
                ]
            },
            {
                "title": "Script PowerShell: Boost Gaming",
                "code": "# BoostGaming.ps1 (ADMIN requis)\nWrite-Host \"=== BOOST MODE GAMING ===\" -ForegroundColor Cyan\n\n# 1. Haute Performance\nWrite-Host \"\\n[1/5] Mode Haute Performance...\" -ForegroundColor Yellow\npowercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c\nWrite-Host \"✅ Activé\"\n\n# 2. Arrêter services inutiles\nWrite-Host \"\\n[2/5] Arrêt services background...\" -ForegroundColor Yellow\nStop-Service WSearch, SysMain -Force -ErrorAction SilentlyContinue\nWrite-Host \"✅ Services stoppés\"\n\n# 3. Vider RAM\nWrite-Host \"\\n[3/5] Nettoyage RAM...\" -ForegroundColor Yellow\n[System.GC]::Collect()\nWrite-Host \"✅ RAM libérée\"\n\n# 4. Optimisations réseau gaming\nWrite-Host \"\\n[4/5] Optimisation réseau...\" -ForegroundColor Yellow\nnetsh int tcp set global autotuninglevel=normal | Out-Null\nnetsh int tcp set global rss=enabled | Out-Null\nWrite-Host \"✅ Réseau optimisé\"\n\n# 5. Infos système\nWrite-Host \"\\n[5/5] État système:\" -ForegroundColor Yellow\n$os = Get-CimInstance Win32_OperatingSystem\n$gpu = Get-CimInstance Win32_VideoController | Select-Object -First 1\n$cpu = Get-CimInstance Win32_Processor\n$ramFree = [math]::Round($os.FreePhysicalMemory / 1MB, 2)\nWrite-Host \"  GPU: $($gpu.Name)\"\nWrite-Host \"  CPU: $($cpu.Name)\"\nWrite-Host \"  RAM libre: $ramFree GB\"\n\nWrite-Host \"\\n=== PRÊT POUR GAMING ===\" -ForegroundColor Green\nWrite-Host \"Lancez votre jeu! Pour désactiver, redémarrez PC.\" -ForegroundColor Yellow"
            },
            {
                "info": "💡 Mesurez FPS avant/après: Activez compteur FPS in-game ou utilisez MSI Afterburner/RivaTuner OSD."
            },
            {
                "warning": "⚠️ Overclocking comporte risques. Commencez conservativement (+50 MHz), testez stabilité, augmentez progressivement. Surveillez températures!"
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3D: REGISTRE WINDOWS (4 guides)
    # =========================================================================

    "reg_intro": {
        "title": "📋 Introduction au Registre Windows",
        "sections": [
            {
                "title": "Qu'est-ce que le Registre Windows?",
                "content": "Le Registre Windows est une base de données hiérarchique qui stocke TOUTES les configurations du système d'exploitation, des logiciels installés, des profils utilisateurs et des matériels. C'est le cerveau de Windows: toute modification a un impact direct sur le fonctionnement du système."
            },
            {
                "title": "Structure du Registre - Les 5 Ruches Principales",
                "bullets": [
                    "HKEY_LOCAL_MACHINE (HKLM) - Configuration globale de la machine (tous utilisateurs)",
                    "HKEY_CURRENT_USER (HKCU) - Configuration de l'utilisateur actuellement connecté",
                    "HKEY_USERS (HKU) - Profils de TOUS les utilisateurs de la machine",
                    "HKEY_CLASSES_ROOT (HKCR) - Associations de fichiers, extensions, objets COM",
                    "HKEY_CURRENT_CONFIG (HKCC) - Profil matériel actuel (alias de HKLM\\SYSTEM\\CurrentControlSet)"
                ]
            },
            {
                "title": "Anatomie d'une Clé de Registre",
                "content": "Exemple: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\n\n• HKEY_LOCAL_MACHINE = Ruche (hive)\n• SOFTWARE = Sous-clé de niveau 1\n• Microsoft\\Windows\\CurrentVersion = Chemin\n• Run = Clé finale (contient des valeurs)\n\nChaque clé peut contenir:\n• Des valeurs (paires nom/données)\n• Des sous-clés (structure arborescente)\n• Des permissions d'accès"
            },
            {
                "title": "Types de Valeurs du Registre",
                "bullets": [
                    "REG_SZ - Chaîne de caractères (texte simple)",
                    "REG_DWORD - Nombre entier 32-bit (0-4294967295)",
                    "REG_QWORD - Nombre entier 64-bit",
                    "REG_BINARY - Données binaires brutes",
                    "REG_MULTI_SZ - Chaînes multiples (liste)",
                    "REG_EXPAND_SZ - Chaîne avec variables d'environnement (%USERPROFILE%)",
                    "REG_LINK - Lien symbolique vers autre clé"
                ]
            },
            {
                "title": "Ouvrir l'Éditeur de Registre (RegEdit)",
                "bullets": [
                    "Méthode 1: Win + R → tapez 'regedit' → Entrée",
                    "Méthode 2: Recherche Windows → 'Éditeur du Registre'",
                    "Méthode 3: PowerShell/CMD → regedit",
                    "Note: Nécessite droits administrateur pour modifications système"
                ]
            },
            {
                "title": "Navigation dans RegEdit",
                "bullets": [
                    "Interface arborescente (comme Explorateur de fichiers)",
                    "Panneau gauche: Arbre des clés",
                    "Panneau droit: Valeurs de la clé sélectionnée",
                    "Favoris: Ctrl+D pour ajouter une clé fréquente",
                    "Recherche: Ctrl+F (cherche clés, valeurs, données)",
                    "Barre d'adresse: Copier chemin complet de la clé"
                ]
            },
            {
                "title": "Commandes Registre en CMD/PowerShell",
                "code": "# CMD - Commande REG\nreg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion  # Lire\nreg add HKCU\\Software\\Test /v Value1 /t REG_SZ /d \"Hello\" /f  # Ajouter\nreg delete HKCU\\Software\\Test /v Value1 /f  # Supprimer valeur\nreg delete HKCU\\Software\\Test /f  # Supprimer clé entière\n\n# PowerShell - Cmdlets natives\nGet-ItemProperty -Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'\nSet-ItemProperty -Path 'HKCU:\\Software\\Test' -Name 'Value1' -Value 'Hello'\nNew-Item -Path 'HKCU:\\Software\\Test'\nRemove-ItemProperty -Path 'HKCU:\\Software\\Test' -Name 'Value1'\nRemove-Item -Path 'HKCU:\\Software\\Test' -Recurse"
            },
            {
                "title": "Clés Système Importantes (À NE PAS Modifier)",
                "bullets": [
                    "⛔ HKLM\\SAM - Comptes utilisateurs et mots de passe (Security Account Manager)",
                    "⛔ HKLM\\SECURITY - Stratégies de sécurité du domaine",
                    "⛔ HKLM\\SYSTEM\\CurrentControlSet - Configuration matérielle active (peut rendre Windows non bootable)",
                    "⚠️ HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion - Version Windows (modifications risquées)",
                    "⚠️ HKCR - Associations fichiers (erreurs peuvent casser l'ouverture de fichiers)"
                ]
            },
            {
                "title": "Clés Utiles pour Utilisateurs Avancés",
                "bullets": [
                    "✅ HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run - Programmes au démarrage (utilisateur)",
                    "✅ HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run - Programmes au démarrage (système)",
                    "✅ HKCU\\Control Panel\\Desktop - Paramètres bureau (fond d'écran, économiseur)",
                    "✅ HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer - Options de l'Explorateur",
                    "✅ HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall - Programmes installés"
                ]
            },
            {
                "warning": "⚠️ DANGER: Une modification incorrecte du Registre peut rendre Windows complètement INUTILISABLE. TOUJOURS créer une sauvegarde avant toute modification (voir guide reg_backup)."
            },
            {
                "info": "💡 Astuce: Pour copier le chemin complet d'une clé dans RegEdit, cliquez dessus puis copiez depuis la barre d'adresse en bas de l'Éditeur."
            }
        ]
    },

    "reg_backup": {
        "title": "💾 Sauvegarde & Restauration du Registre",
        "sections": [
            {
                "title": "Pourquoi Sauvegarder le Registre?",
                "content": "Avant toute modification du Registre, il est CRITIQUE de créer une sauvegarde. Une erreur peut:\n• Empêcher Windows de démarrer\n• Désactiver des fonctionnalités système\n• Corrompre des programmes installés\n• Nécessiter une réinstallation complète de Windows\n\nUne sauvegarde permet de restaurer rapidement l'état fonctionnel."
            },
            {
                "title": "Méthode 1: Point de Restauration Système (Recommandé)",
                "bullets": [
                    "Étape 1: Win + R → 'rstrui.exe' → Entrée",
                    "Ou: Panneau de configuration → Système → Protection du système",
                    "Étape 2: Cliquez sur 'Créer' (pas 'Restauration du système')",
                    "Étape 3: Nommez le point (ex: 'Avant modif registre 2026-01-03')",
                    "Étape 4: Cliquez 'Créer' et attendez (1-5 minutes)",
                    "Avantages: Sauvegarde TOUT (registre + fichiers système + pilotes)",
                    "Utilisation: En cas de problème, restaurez via Mode Sans Échec ou WinRE"
                ]
            },
            {
                "title": "Méthode 2: Export via RegEdit (Clés Spécifiques)",
                "bullets": [
                    "Étape 1: Ouvrez RegEdit (Win + R → regedit)",
                    "Étape 2: Naviguez vers la clé à modifier",
                    "Étape 3: Clic droit sur la clé → 'Exporter'",
                    "Étape 4: Choisissez emplacement et nom (ex: backup_run_keys.reg)",
                    "Étape 5: Vérifiez 'Branche sélectionnée' est coché",
                    "Étape 6: Cliquez 'Enregistrer'",
                    "Résultat: Fichier .reg texte contenant la clé exportée",
                    "Restauration: Double-clic sur le .reg et confirmer fusion"
                ]
            },
            {
                "title": "Méthode 3: Export Complet via RegEdit",
                "bullets": [
                    "Étape 1: Ouvrez RegEdit",
                    "Étape 2: Sélectionnez 'Ordinateur' (tout en haut de l'arbre)",
                    "Étape 3: Fichier → Exporter",
                    "Étape 4: Choisissez 'Tout' au lieu de 'Branche sélectionnée'",
                    "Étape 5: Sauvegardez (ex: full_registry_backup.reg)",
                    "⚠️ Attention: Fichier TRÈS volumineux (200+ MB)",
                    "⚠️ Import complet DÉCONSEILLÉ (risque de corruption)"
                ]
            },
            {
                "title": "Méthode 4: Commande REG EXPORT (CMD/PowerShell)",
                "code": "REM CMD - Export clé spécifique\nreg export \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" \"C:\\Backups\\run_keys_backup.reg\" /y\n\nREM Export ruche complète\nreg export HKLM \"C:\\Backups\\HKLM_backup.reg\" /y\nreg export HKCU \"C:\\Backups\\HKCU_backup.reg\" /y\n\nREM PowerShell - Export via cmdlet\nreg export \"HKLM\\SOFTWARE\\MyApp\" \"C:\\Backups\\myapp.reg\"\n\nREM Restaurer (importer)\nreg import \"C:\\Backups\\run_keys_backup.reg\""
            },
            {
                "title": "Méthode 5: Sauvegarde Automatisée (Script PowerShell)",
                "code": "# BackupRegistry.ps1 (ADMIN)\n$backupPath = \"C:\\RegistryBackups\"\n$date = Get-Date -Format \"yyyy-MM-dd_HHmmss\"\n$backupFolder = \"$backupPath\\Backup_$date\"\n\n# Créer dossier\nNew-Item -ItemType Directory -Path $backupFolder -Force | Out-Null\n\n# Export clés critiques\n$keys = @(\n    @{Hive='HKLM'; Path='SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run'; Name='HKLM_Run'},\n    @{Hive='HKCU'; Path='Software\\Microsoft\\Windows\\CurrentVersion\\Run'; Name='HKCU_Run'},\n    @{Hive='HKLM'; Path='SYSTEM\\CurrentControlSet\\Services'; Name='Services'}\n)\n\nforeach ($key in $keys) {\n    $fullPath = \"$($key.Hive)\\$($key.Path)\"\n    $outFile = \"$backupFolder\\$($key.Name).reg\"\n    reg export $fullPath $outFile /y | Out-Null\n    if ($?) {\n        Write-Host \"✓ Sauvegardé: $($key.Name)\" -ForegroundColor Green\n    }\n}\n\nWrite-Host \"\\n✅ Sauvegarde terminée: $backupFolder\" -ForegroundColor Cyan"
            },
            {
                "title": "Restaurer une Sauvegarde",
                "bullets": [
                    "Méthode rapide: Double-cliquez sur le fichier .reg → Confirmer fusion",
                    "Méthode RegEdit: Fichier → Importer → Sélectionnez .reg",
                    "Méthode CMD: reg import \"C:\\Backups\\backup.reg\"",
                    "Point de Restauration: rstrui.exe → Choisir point → Suivant → Terminer"
                ]
            },
            {
                "title": "Restauration en Mode Sans Échec (Si Windows ne démarre pas)",
                "bullets": [
                    "Étape 1: Redémarrez PC → Appuyez F8 (ou Shift+F8) au boot",
                    "Ou: Depuis WinRE (3 démarrages forcés échoués)",
                    "Étape 2: Choisissez 'Mode Sans Échec avec Invite de commandes'",
                    "Étape 3: Connectez-vous en tant qu'administrateur",
                    "Étape 4: reg import \"C:\\Backups\\backup.reg\"",
                    "Ou: rstrui.exe pour point de restauration",
                    "Étape 5: Redémarrez normalement"
                ]
            },
            {
                "title": "Sauvegardes Automatiques de Windows",
                "content": "Windows crée automatiquement des sauvegardes du Registre:\n\n• RegBack (W10 1803-): C:\\Windows\\System32\\config\\RegBack\n  - Sauvegarde quotidienne automatique (derniers 5 jours)\n  - ⚠️ Désactivé par défaut depuis Windows 10 1803!\n\n• Transaction Logs: C:\\Windows\\System32\\config\n  - Fichiers .LOG1, .LOG2 (journaux de transactions)\n  - Utilisés pour récupération automatique au boot\n\nActiver RegBack (Windows 10 1803+):\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Configuration Manager\" /v EnablePeriodicBackup /t REG_DWORD /d 1 /f"
            },
            {
                "warning": "⚠️ Les Points de Restauration peuvent être supprimés par Windows pour libérer de l'espace disque. Créez des exports .reg manuels pour modifications critiques."
            },
            {
                "info": "💡 Astuce Pro: Créez un dossier 'C:\\RegistryBackups' et exportez TOUJOURS avant modifications. Nommez les fichiers avec la date et description (ex: '2026-01-03_avant_tweak_telemetrie.reg')."
            }
        ]
    },

    "reg_tweaks": {
        "title": "⚙️ Tweaks Registre - Optimisations & Personnalisations",
        "sections": [
            {
                "title": "⚠️ AVERTISSEMENT CRITIQUE",
                "content": "Ces tweaks modifient des paramètres système. TOUJOURS:\n1. Créer un Point de Restauration avant\n2. Exporter les clés à modifier\n3. Tester sur machine virtuelle si possible\n4. Appliquer un tweak à la fois (pas tous ensemble)\n5. Redémarrer entre chaque modification majeure"
            },
            {
                "title": "Performance - Désactiver Animations & Effets Visuels",
                "code": "REM Désactiver toutes animations Windows\nreg add \"HKCU\\Control Panel\\Desktop\\WindowMetrics\" /v MinAnimate /t REG_SZ /d 0 /f\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects\" /v VisualFXSetting /t REG_DWORD /d 2 /f\n\nREM Accélérer Menu Démarrer (délai 0ms)\nreg add \"HKCU\\Control Panel\\Desktop\" /v MenuShowDelay /t REG_SZ /d 0 /f\n\nREM Désactiver transparence barre des tâches\nreg add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\" /v EnableTransparency /t REG_DWORD /d 0 /f\n\nREM Désactiver animations fenêtres\nreg add \"HKCU\\Control Panel\\Desktop\" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f"
            },
            {
                "title": "Performance - Optimisations Mémoire & CPU",
                "code": "REM Désactiver Superfetch/SysMain (SSD uniquement!)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\SysMain\" /v Start /t REG_DWORD /d 4 /f\n\nREM Désactiver Windows Search Indexing\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\WSearch\" /v Start /t REG_DWORD /d 4 /f\n\nREM Priorité processeur pour programmes (non arrière-plan)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl\" /v Win32PrioritySeparation /t REG_DWORD /d 38 /f\n\nREM Désactiver veille disques durs (gaming/performance)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power\" /v HiberbootEnabled /t REG_DWORD /d 0 /f\npowercfg -h off"
            },
            {
                "title": "Confidentialité - Désactiver Télémétrie & Tracking",
                "code": "REM Télémétrie Microsoft (niveau minimum)\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v AllowTelemetry /t REG_DWORD /d 0 /f\n\nREM Désactiver ID publicité\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo\" /v Enabled /t REG_DWORD /d 0 /f\n\nREM Désactiver suivi de localisation\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location\" /v Value /t REG_SZ /d Deny /f\n\nREM Désactiver suggestions Cortana/Démarrer\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v SystemPaneSuggestionsEnabled /t REG_DWORD /d 0 /f\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v SubscribedContent-338388Enabled /t REG_DWORD /d 0 /f\n\nREM Désactiver Windows Spotlight (écran verrouillage)\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" /v RotatingLockScreenEnabled /t REG_DWORD /d 0 /f"
            },
            {
                "title": "Interface - Personnalisations Explorateur",
                "code": "REM Afficher extensions de fichiers\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v HideFileExt /t REG_DWORD /d 0 /f\n\nREM Afficher fichiers cachés\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v Hidden /t REG_DWORD /d 1 /f\n\nREM Afficher dossiers système protégés\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v ShowSuperHidden /t REG_DWORD /d 1 /f\n\nREM Désactiver regroupement barre des tâches\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v TaskbarGlomLevel /t REG_DWORD /d 2 /f\n\nREM Ouvrir Explorateur sur Ce PC (pas Accès rapide)\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v LaunchTo /t REG_DWORD /d 1 /f\n\nREM Activer mode sombre\nreg add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\" /v AppsUseLightTheme /t REG_DWORD /d 0 /f\nreg add \"HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\" /v SystemUsesLightTheme /t REG_DWORD /d 0 /f"
            },
            {
                "title": "Interface - Désactiver Fonctionnalités Inutiles",
                "code": "REM Désactiver Cortana\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v AllowCortana /t REG_DWORD /d 0 /f\n\nREM Désactiver recherche web dans Démarrer\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search\" /v BingSearchEnabled /t REG_DWORD /d 0 /f\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search\" /v CortanaConsent /t REG_DWORD /d 0 /f\n\nREM Désactiver widgets Windows 11\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Dsh\" /v AllowNewsAndInterests /t REG_DWORD /d 0 /f\n\nREM Désactiver Meet Now (icône barre des tâches)\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v HideSCAMeetNow /t REG_DWORD /d 1 /f\n\nREM Désactiver Actualités et Centres d'intérêt\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Feeds\" /v EnableFeeds /t REG_DWORD /d 0 /f"
            },
            {
                "title": "Sécurité - Renforcement Système",
                "code": "REM Désactiver SMBv1 (vulnérable à WannaCry)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters\" /v SMB1 /t REG_DWORD /d 0 /f\n\nREM Activer DEP (Data Execution Prevention) pour tous programmes\nbcdedit /set nx AlwaysOn\n\nREM Désactiver AutoRun/AutoPlay USB (malwares)\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v NoDriveTypeAutoRun /t REG_DWORD /d 255 /f\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v NoDriveTypeAutoRun /t REG_DWORD /d 255 /f\n\nREM Désactiver exécution macros Office par défaut\nreg add \"HKCU\\Software\\Microsoft\\Office\\16.0\\Word\\Security\" /v VBAWarnings /t REG_DWORD /d 4 /f\nreg add \"HKCU\\Software\\Microsoft\\Office\\16.0\\Excel\\Security\" /v VBAWarnings /t REG_DWORD /d 4 /f\n\nREM Désactiver Remote Desktop (si non utilisé)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 1 /f"
            },
            {
                "title": "Gaming - Optimisations FPS & Latence",
                "code": "REM Game Mode activé\nreg add \"HKCU\\Software\\Microsoft\\GameBar\" /v AllowAutoGameMode /t REG_DWORD /d 1 /f\nreg add \"HKCU\\Software\\Microsoft\\GameBar\" /v AutoGameModeEnabled /t REG_DWORD /d 1 /f\n\nREM Désactiver GameDVR/enregistrements (économise RAM)\nreg add \"HKCU\\System\\GameConfigStore\" /v GameDVR_Enabled /t REG_DWORD /d 0 /f\nreg add \"HKLM\\SOFTWARE\\Microsoft\\PolicyManager\\default\\ApplicationManagement\\AllowGameDVR\" /v value /t REG_DWORD /d 0 /f\n\nREM Priorité GPU pour jeux\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\" /v \"GPU Priority\" /t REG_DWORD /d 8 /f\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\" /v Priority /t REG_DWORD /d 6 /f\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\" /v \"Scheduling Category\" /t REG_SZ /d High /f\n\nREM HAGS (Hardware Accelerated GPU Scheduling) - RTX 20xx+/RX 5xxx+\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\" /v HwSchMode /t REG_DWORD /d 2 /f"
            },
            {
                "title": "Réseau - Optimisations Latence",
                "code": "REM TCP Auto-Tuning Level Normal\nnetsh int tcp set global autotuninglevel=normal\n\nREM Désactiver Nagle Algorithm (réduit latence gaming)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\" /v TcpAckFrequency /t REG_DWORD /d 1 /f\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\" /v TCPNoDelay /t REG_DWORD /d 1 /f\n\nREM Désactiver Large Send Offload (peut causer lag)\nnetsh int tcp set global chimney=disabled\n\nREM QoS: 0% réservation bande passante\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\" /v NonBestEffortLimit /t REG_DWORD /d 0 /f"
            },
            {
                "title": "Script PowerShell: Appliquer Tous Tweaks",
                "code": "# ApplyAllTweaks.ps1 (ADMIN REQUIS)\nWrite-Host \"=== APPLICATION TWEAKS REGISTRE ===\" -ForegroundColor Cyan\n\n# Créer point de restauration\nWrite-Host \"\\n[1/6] Création point de restauration...\" -ForegroundColor Yellow\nCheckpoint-Computer -Description \"Avant tweaks registre\" -RestorePointType \"MODIFY_SETTINGS\"\n\n# Performance\nWrite-Host \"[2/6] Tweaks performance...\" -ForegroundColor Yellow\nreg add \"HKCU\\Control Panel\\Desktop\" /v MenuShowDelay /t REG_SZ /d 0 /f | Out-Null\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects\" /v VisualFXSetting /t REG_DWORD /d 2 /f | Out-Null\n\n# Confidentialité\nWrite-Host \"[3/6] Tweaks confidentialité...\" -ForegroundColor Yellow\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v AllowTelemetry /t REG_DWORD /d 0 /f | Out-Null\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo\" /v Enabled /t REG_DWORD /d 0 /f | Out-Null\n\n# Interface\nWrite-Host \"[4/6] Tweaks interface...\" -ForegroundColor Yellow\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v HideFileExt /t REG_DWORD /d 0 /f | Out-Null\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" /v Hidden /t REG_DWORD /d 1 /f | Out-Null\n\n# Gaming\nWrite-Host \"[5/6] Tweaks gaming...\" -ForegroundColor Yellow\nreg add \"HKCU\\Software\\Microsoft\\GameBar\" /v AutoGameModeEnabled /t REG_DWORD /d 1 /f | Out-Null\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers\" /v HwSchMode /t REG_DWORD /d 2 /f | Out-Null\n\n# Sécurité\nWrite-Host \"[6/6] Tweaks sécurité...\" -ForegroundColor Yellow\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v NoDriveTypeAutoRun /t REG_DWORD /d 255 /f | Out-Null\n\nWrite-Host \"\\n✅ Tweaks appliqués! Redémarrez pour appliquer.\" -ForegroundColor Green\nWrite-Host \"Pour annuler: rstrui.exe → Choisir point de restauration\" -ForegroundColor Yellow"
            },
            {
                "warning": "⚠️ NE MODIFIEZ JAMAIS: HKLM\\SAM, HKLM\\SECURITY, HKLM\\SYSTEM\\CurrentControlSet\\Control (sauf sous-clés documentées). Risque de briquage Windows!"
            },
            {
                "info": "💡 Les scripts Windows inclus dans NiTriTe appliquent ces tweaks de façon sécurisée avec vérifications. Utilisez-les plutôt que les commandes manuelles."
            }
        ]
    },

    "reg_security": {
        "title": "🔒 Sécurité du Registre Windows",
        "sections": [
            {
                "title": "Pourquoi Sécuriser le Registre?",
                "content": "Le Registre Windows est une cible privilégiée des malwares car il permet:\n• Démarrage automatique de programmes malveillants\n• Modification paramètres système (désactiver antivirus, pare-feu)\n• Vol d'informations sensibles (mots de passe, clés logicielles)\n• Persistence (survivre aux redémarrages)\n• Élévation de privilèges\n\nSécuriser le Registre est essentiel pour protéger Windows."
            },
            {
                "title": "Clés Registre Utilisées par les Malwares",
                "bullets": [
                    "⚠️ HKLM/HKCU\\...\\CurrentVersion\\Run - Exécution au démarrage",
                    "⚠️ HKLM/HKCU\\...\\CurrentVersion\\RunOnce - Exécution unique au boot",
                    "⚠️ HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon - Scripts de connexion",
                    "⚠️ HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders - Redirection dossiers",
                    "⚠️ HKLM\\SYSTEM\\CurrentControlSet\\Services - Installation de drivers/services malveillants",
                    "⚠️ HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options - Hijacking d'exécutables"
                ]
            },
            {
                "title": "Auditer les Clés de Démarrage Automatique",
                "code": "# PowerShell - Scanner toutes clés Run\n$runKeys = @(\n    'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',\n    'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\n    'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',\n    'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\n    'HKLM:\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run'\n)\n\nforeach ($key in $runKeys) {\n    if (Test-Path $key) {\n        Write-Host \"\\n=== $key ===\" -ForegroundColor Cyan\n        Get-ItemProperty -Path $key | Select-Object * -ExcludeProperty PS* | Format-List\n    }\n}\n\n# Vérifier programmes au démarrage suspects\nGet-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User | Format-Table -AutoSize"
            },
            {
                "title": "Vérifier Services Malveillants",
                "code": "# PowerShell - Lister services non-Microsoft\nGet-Service | Where-Object {\n    $_.DisplayName -notlike \"*Microsoft*\" -and\n    $_.DisplayName -notlike \"*Windows*\"\n} | Select-Object Name, DisplayName, Status, StartType | Format-Table -AutoSize\n\n# Vérifier clés services dans registre\nGet-ChildItem \"HKLM:\\SYSTEM\\CurrentControlSet\\Services\" | Where-Object {\n    $imagePath = (Get-ItemProperty -Path $_.PSPath -ErrorAction SilentlyContinue).ImagePath\n    $imagePath -and $imagePath -notmatch 'C:\\\\Windows'\n} | Select-Object PSChildName, @{Name='ImagePath';Expression={(Get-ItemProperty $_.PSPath).ImagePath}}"
            },
            {
                "title": "Permissions du Registre - Restreindre l'Accès",
                "bullets": [
                    "Étape 1: Ouvrez RegEdit et naviguez vers une clé critique",
                    "Étape 2: Clic droit → Autorisations",
                    "Étape 3: Sélectionnez un groupe/utilisateur",
                    "Étape 4: Cochez 'Refuser' pour 'Modifier' (empêche modifications)",
                    "Étape 5: Appliquez et confirmez",
                    "Note: Les administrateurs peuvent override les permissions",
                    "Utilité: Protège clés système contre modifications accidentelles/malveillantes"
                ]
            },
            {
                "title": "Auditer Modifications du Registre (Audit Logs)",
                "code": "# PowerShell (ADMIN) - Activer audit modifications registre\n# 1. Ouvrir stratégie de groupe locale\nsecpol.msc\n\n# 2. Navigation manuelle:\n# Configuration ordinateur → Paramètres Windows → Paramètres de sécurité →\n# Stratégies locales → Stratégie d'audit → Auditer les accès au service d'annuaire\n\n# Via PowerShell/CMD:\nauditpol /set /subcategory:\"Registry\" /success:enable /failure:enable\n\n# Vérifier config\nauditpol /get /subcategory:\"Registry\"\n\n# Consulter logs (Event Viewer)\n# Windows Logs → Security → Filtrer Event ID 4657 (modification registre)"
            },
            {
                "title": "Désactiver Remote Registry Service",
                "code": "# PowerShell (ADMIN) - Désactiver Remote Registry\nStop-Service RemoteRegistry -Force\nSet-Service RemoteRegistry -StartupType Disabled\n\n# Vérifier\nGet-Service RemoteRegistry\n\n# CMD équivalent\nsc stop RemoteRegistry\nsc config RemoteRegistry start= disabled"
            },
            {
                "title": "Nettoyer Traces de Programmes Désinstallés",
                "code": "# PowerShell - Lister programmes désinstallés (clés orphelines)\n$uninstallKeys = @(\n    'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*',\n    'HKLM:\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*',\n    'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*'\n)\n\n$programs = Get-ItemProperty -Path $uninstallKeys -ErrorAction SilentlyContinue |\n    Where-Object {$_.DisplayName} |\n    Select-Object DisplayName, Publisher, InstallDate, InstallLocation |\n    Sort-Object DisplayName\n\n$programs | Format-Table -AutoSize\n\n# Identifier programmes sans InstallLocation (probablement désinstallés)\n$programs | Where-Object {-not $_.InstallLocation}\n\n# ⚠️ Suppression manuelle via RegEdit (vérifier AVANT!)"
            },
            {
                "title": "Bloquer Modifications Registre pour Utilisateurs Standard",
                "code": "# PowerShell (ADMIN) - Désactiver RegEdit pour utilisateurs standard\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableRegistryTools /t REG_DWORD /d 1 /f\n\n# Réactiver\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableRegistryTools /t REG_DWORD /d 0 /f\n\n# Note: Administrateurs peuvent toujours accéder\n# Bloquer pour administrateurs (extrême, déconseillé):\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableRegistryTools /t REG_DWORD /d 2 /f"
            },
            {
                "title": "Scanner Hijacking d'Exécutables (IFEO)",
                "code": "# PowerShell - Vérifier Image File Execution Options (hijacking)\n$ifeoPath = 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options'\n\nGet-ChildItem $ifeoPath | ForEach-Object {\n    $debugger = (Get-ItemProperty -Path $_.PSPath -ErrorAction SilentlyContinue).Debugger\n    if ($debugger) {\n        [PSCustomObject]@{\n            Executable = $_.PSChildName\n            Debugger = $debugger\n            Suspicious = ($debugger -notmatch 'ntsd|cdb' -and $debugger)\n        }\n    }\n} | Where-Object {$_.Suspicious} | Format-Table -AutoSize\n\n# Légitime: ntsd.exe, cdb.exe (Windows Debuggers)\n# Suspect: Tout autre exécutable (possible malware redirection)"
            },
            {
                "title": "Restaurer Paramètres de Sécurité par Défaut",
                "code": "# PowerShell (ADMIN) - Reset permissions registre (DANGER!)\n# ⚠️ SEULEMENT si registre corrompu/inaccessible\n\n# Reprendre possession clé\ntakeown /f \"C:\\Windows\\System32\\config\\SYSTEM\" /r /d y\nicacls \"C:\\Windows\\System32\\config\\SYSTEM\" /grant administrators:F /t\n\n# Réparer permissions via DISM\nDISM /Online /Cleanup-Image /RestoreHealth\n\n# SFC scan système\nsfc /scannow\n\n# Via Point de Restauration (recommandé)\nrstrui.exe"
            },
            {
                "title": "Outils de Sécurité Registre Recommandés",
                "bullets": [
                    "Autoruns (Sysinternals) - Scanner exhaustif démarrages auto",
                    "Process Monitor (Sysinternals) - Surveiller accès registre en temps réel",
                    "RegShot - Comparer registre avant/après installation",
                    "CCleaner - Nettoyer clés obsolètes (avec précaution)",
                    "Malwarebytes - Scanner malwares registre",
                    "HijackThis - Analyser hijacking navigateur/système"
                ]
            },
            {
                "warning": "⚠️ NE SUPPRIMEZ JAMAIS une clé de registre sans être 100% sûr de son rôle. Recherchez le nom de la clé/valeur en ligne avant suppression."
            },
            {
                "info": "💡 Astuce Sécurité: Créez une tâche planifiée hebdomadaire qui exporte les clés Run et vous envoie le fichier par email. Comparez-le chaque semaine pour détecter ajouts suspects."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3E: SERVICES WINDOWS (3 guides)
    # =========================================================================

    "svc_intro": {
        "title": "⚙️ Gestion des Services Windows",
        "sections": [
            {
                "title": "Qu'est-ce qu'un Service Windows?",
                "content": "Un service Windows est un programme qui s'exécute en arrière-plan sans interface graphique. Les services démarrent automatiquement au boot et fonctionnent même sans utilisateur connecté. Ils gèrent des fonctionnalités système critiques: réseau, audio, impressions, mises à jour, sécurité, etc."
            },
            {
                "title": "Types de Services",
                "bullets": [
                    "Automatique - Démarre au boot de Windows",
                    "Automatique (Démarrage différé) - Démarre 2 minutes après le boot",
                    "Manuel - Démarre uniquement quand requis par un programme",
                    "Désactivé - Ne peut pas démarrer"
                ]
            },
            {
                "title": "Ouvrir le Gestionnaire de Services",
                "bullets": [
                    "Méthode 1: Win + R → services.msc → Entrée",
                    "Méthode 2: Gestionnaire des tâches → Onglet Services",
                    "Méthode 3: Panneau config → Outils d'admin → Services",
                    "Méthode 4: PowerShell → Get-Service"
                ]
            },
            {
                "title": "Lister Services (PowerShell)",
                "code": "# Tous les services\nGet-Service | Format-Table -AutoSize\n\n# Services en cours d'exécution\nGet-Service | Where-Object {$_.Status -eq 'Running'}\n\n# Services arrêtés\nGet-Service | Where-Object {$_.Status -eq 'Stopped'}\n\n# Service spécifique\nGet-Service -Name 'wuauserv'  # Windows Update\n\n# Trier par statut\nGet-Service | Sort-Object Status | Format-Table Name, DisplayName, Status, StartType"
            },
            {
                "title": "Démarrer/Arrêter un Service",
                "code": "# PowerShell (ADMIN)\nStart-Service -Name 'wuauserv'\nStop-Service -Name 'wuauserv' -Force\nRestart-Service -Name 'wuauserv'\n\n# Vérifier statut\nGet-Service -Name 'wuauserv'\n\n# CMD (ADMIN)\nnet start wuauserv\nnet stop wuauserv\nsc start wuauserv\nsc stop wuauserv"
            },
            {
                "title": "Modifier Type de Démarrage",
                "code": "# PowerShell (ADMIN)\nSet-Service -Name 'wuauserv' -StartupType Automatic\nSet-Service -Name 'wuauserv' -StartupType Manual\nSet-Service -Name 'wuauserv' -StartupType Disabled\nSet-Service -Name 'wuauserv' -StartupType 'Automatic (Delayed Start)'\n\n# CMD (ADMIN)\nsc config wuauserv start= auto\nsc config wuauserv start= demand  # Manuel\nsc config wuauserv start= disabled"
            },
            {
                "title": "Services Critiques (NE PAS DÉSACTIVER)",
                "bullets": [
                    "⛔ RpcSs - Appel de procédure distante (système crashe sans)",
                    "⛔ DcomLaunch - DCOM Server Process Launcher",
                    "⛔ PlugPlay - Plug-and-Play (détection matériel)",
                    "⛔ Power - Gestion alimentation",
                    "⛔ ProfSvc - Service de profil utilisateur",
                    "⛔ SENS - Service de notification d'événements système",
                    "⛔ LanmanWorkstation - Partage réseau Windows"
                ]
            },
            {
                "title": "Informations Détaillées d'un Service",
                "code": "# PowerShell\nGet-Service -Name 'wuauserv' | Select-Object *\nGet-WmiObject Win32_Service | Where-Object {$_.Name -eq 'wuauserv'} | Format-List *\n\n# Chemin de l'exécutable\n(Get-WmiObject Win32_Service -Filter \"Name='wuauserv'\").PathName\n\n# CMD\nsc qc wuauserv  # Query Config\nsc queryex wuauserv  # Query Extended"
            },
            {
                "warning": "⚠️ ATTENTION: Désactiver le mauvais service peut rendre Windows instable ou non bootable. Recherchez en ligne avant de désactiver un service inconnu."
            },
            {
                "info": "💡 Services 'Automatique (Démarrage différé)' réduisent le temps de boot. Préférez ce mode pour services non critiques."
            }
        ]
    },

    "svc_optimize": {
        "title": "⚡ Optimisation des Services Windows",
        "sections": [
            {
                "title": "Pourquoi Optimiser les Services?",
                "content": "Windows démarre 50-100+ services au boot, dont beaucoup sont inutiles pour un usage normal. Désactiver les services superflus permet de:\n• Réduire le temps de démarrage (20-40%)\n• Libérer de la RAM (200-500 MB)\n• Réduire l'usage CPU en arrière-plan\n• Améliorer performances globales\n• Renforcer la sécurité (moins de services exposés)"
            },
            {
                "title": "Services SÛRS à Désactiver (Usage Personnel)",
                "bullets": [
                    "✅ Bluetooth Support Service (bthserv) - Si pas de Bluetooth",
                    "✅ Print Spooler (Spooler) - Si pas d'imprimante",
                    "✅ Windows Search (WSearch) - Si n'utilisez pas la recherche Windows",
                    "✅ Superfetch/SysMain (SysMain) - Sur SSD uniquement",
                    "✅ Remote Desktop Services - Si n'utilisez pas Bureau à distance",
                    "✅ Fax (Fax) - Qui utilise encore le fax?",
                    "✅ Windows Biometric Service (WbioSrvc) - Si pas de lecteur empreintes",
                    "✅ Tablet PC Input Service (TabletInputService) - PC non tactile",
                    "✅ Téléphonie (TapiSrv) - Si pas de modem/téléphonie",
                    "✅ Xbox services (XblAuthManager, XblGameSave, XboxNetApiSvc) - Si pas de gaming Xbox"
                ]
            },
            {
                "title": "Script PowerShell: Désactiver Services Inutiles",
                "code": "# DisableUnnecessaryServices.ps1 (ADMIN)\n$servicesToDisable = @(\n    'bthserv',          # Bluetooth\n    'Spooler',          # Print Spooler\n    'WSearch',          # Windows Search\n    'SysMain',          # Superfetch (SSD only)\n    'TabletInputService', # Tablet Input\n    'Fax',              # Fax\n    'WbioSrvc',         # Biometric\n    'TapiSrv',          # Telephony\n    'XblAuthManager',   # Xbox Live Auth\n    'XblGameSave',      # Xbox Live Game Save\n    'XboxNetApiSvc'     # Xbox Networking\n)\n\nforeach ($svc in $servicesToDisable) {\n    $service = Get-Service -Name $svc -ErrorAction SilentlyContinue\n    if ($service) {\n        Stop-Service $svc -Force -ErrorAction SilentlyContinue\n        Set-Service $svc -StartupType Disabled\n        Write-Host \"✓ $svc désactivé\" -ForegroundColor Green\n    }\n}"
            },
            {
                "title": "Services à Mettre en 'Manuel' (Démarrage à la demande)",
                "bullets": [
                    "Windows Update (wuauserv) - Lancer manuellement quand besoin",
                    "Windows Defender Update (WdNisSvc) - Si autre antivirus",
                    "Remote Registry (RemoteRegistry) - Sécurité",
                    "Distributed Link Tracking Client (TrkWks) - Rarement nécessaire",
                    "IP Helper (iphlpsvc) - Si pas IPv6",
                    "Program Compatibility Assistant (PcaSvc) - Rarement utilisé"
                ]
            },
            {
                "title": "Script: Mettre Services en Manuel",
                "code": "# SetServicesToManual.ps1 (ADMIN)\n$servicesToManual = @('wuauserv', 'RemoteRegistry', 'TrkWks', 'iphlpsvc', 'PcaSvc')\n\nforeach ($svc in $servicesToManual) {\n    Set-Service -Name $svc -StartupType Manual -ErrorAction SilentlyContinue\n    Write-Host \"✓ $svc → Manuel\" -ForegroundColor Yellow\n}"
            },
            {
                "title": "Services Gaming - Optimiser pour FPS",
                "code": "# Gaming optimization (ADMIN)\n# Désactiver services inutiles en jeu\n$gamingDisable = @(\n    'WSearch',      # Windows Search\n    'SysMain',      # Superfetch\n    'Themes',       # Thèmes (économise GPU)\n    'WbioSrvc'      # Biometric\n)\n\nforeach ($svc in $gamingDisable) {\n    Stop-Service $svc -Force -ErrorAction SilentlyContinue\n    Set-Service $svc -StartupType Disabled\n}\n\n# Priorité haute pour services gaming\n$gamingServices = @('Audiosrv', 'AudioEndpointBuilder')\nforeach ($svc in $gamingServices) {\n    sc config $svc type= own  # Service propre (pas partagé)\n}"
            },
            {
                "title": "Restaurer Services par Défaut",
                "code": "# RestoreDefaultServices.ps1 (ADMIN)\n# Réactiver tous services Windows par défaut\n\n# Liste services système importants\n$defaultServices = @(\n    @{Name='wuauserv'; Type='Manual'},\n    @{Name='Spooler'; Type='Automatic'},\n    @{Name='WSearch'; Type='Automatic (Delayed)'},\n    @{Name='bthserv'; Type='Manual'}\n)\n\nforeach ($svc in $defaultServices) {\n    Set-Service -Name $svc.Name -StartupType $svc.Type -ErrorAction SilentlyContinue\n    Write-Host \"✓ $($svc.Name) restauré → $($svc.Type)\" -ForegroundColor Cyan\n}\n\nWrite-Host \"\\nServices restaurés aux valeurs par défaut Windows\" -ForegroundColor Green"
            },
            {
                "title": "Comparer Services Avant/Après Optimisation",
                "code": "# Exporter liste services AVANT optimisation\nGet-Service | Export-Csv \"services_before.csv\" -NoTypeInformation\n\n# [Appliquer optimisations]\n\n# Exporter APRÈS\nGet-Service | Export-Csv \"services_after.csv\" -NoTypeInformation\n\n# Comparer\n$before = Import-Csv \"services_before.csv\"\n$after = Import-Csv \"services_after.csv\"\n\nCompare-Object $before $after -Property Name, Status, StartType | Format-Table"
            },
            {
                "warning": "⚠️ Testez après chaque désactivation. Si un problème survient, réactivez le dernier service désactivé."
            },
            {
                "info": "💡 Les scripts Windows de NiTriTe incluent des optimisations de services testées et sécurisées. Utilisez-les plutôt que de désactiver manuellement."
            }
        ]
    },

    "svc_troubleshoot": {
        "title": "🔧 Dépannage des Services Windows",
        "sections": [
            {
                "title": "Problèmes Courants avec les Services",
                "content": "Les services peuvent causer divers problèmes: démarrage lent, erreurs système, fonctionnalités cassées, crashes. Ce guide couvre les problèmes fréquents et leurs solutions."
            },
            {
                "title": "Service ne Démarre Pas (Erreur 1053)",
                "bullets": [
                    "Symptôme: 'Le service n'a pas répondu à temps'",
                    "Cause: Timeout trop court, service bloqué, corruption",
                    "Solution 1: Augmenter timeout registre",
                    "Solution 2: Vérifier dépendances du service",
                    "Solution 3: Réenregistrer le service"
                ]
            },
            {
                "code": "# Augmenter timeout services (ADMIN)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\" /v ServicesPipeTimeout /t REG_DWORD /d 180000 /f\n\n# Vérifier dépendances\nsc qc NomDuService\n\n# Réenregistrer service\nsc delete NomDuService\nsc create NomDuService binPath= \"C:\\chemin\\vers\\service.exe\""
            },
            {
                "title": "Service se Bloque/Crash en Boucle",
                "code": "# PowerShell - Vérifier logs événements\nGet-EventLog -LogName System -Source \"Service Control Manager\" -Newest 50 | Where-Object {$_.EntryType -eq 'Error'}\n\n# Désactiver redémarrage automatique (temporaire)\nsc failure NomDuService reset= 0 actions= \"\"\n\n# Démarrer service en mode debug\nsc start NomDuService\n\n# Consulter Event Viewer\neventvwr.msc  # Windows Logs → System"
            },
            {
                "title": "Erreur 'Accès Refusé' lors Démarrage",
                "bullets": [
                    "Cause: Permissions insuffisantes, compte service incorrect",
                    "Solution 1: Exécuter en tant qu'Administrateur",
                    "Solution 2: Vérifier le compte de connexion du service",
                    "Solution 3: Réinitialiser permissions"
                ]
            },
            {
                "code": "# Vérifier compte du service\nsc qc NomDuService\n\n# Changer compte vers LocalSystem\nsc config NomDuService obj= LocalSystem\n\n# Ou compte NetworkService\nsc config NomDuService obj= \"NT AUTHORITY\\NetworkService\"\n\n# Ou compte LocalService\nsc config NomDuService obj= \"NT AUTHORITY\\LocalService\""
            },
            {
                "title": "Réinitialiser TOUS les Services Windows par Défaut",
                "code": "# CMD (ADMIN) - Reset vers config d'usine\n# ⚠️ DANGEREUX - Créer point de restauration d'abord!\n\n# Via DISM (réparer image Windows)\nDISM /Online /Cleanup-Image /RestoreHealth\n\n# SFC (vérifier fichiers système)\nsfc /scannow\n\n# Réinitialiser base de registre services\nreg delete \"HKLM\\SYSTEM\\CurrentControlSet\\Services\" /f\nreg copy \"HKLM\\SYSTEM\\ControlSet001\\Services\" \"HKLM\\SYSTEM\\CurrentControlSet\\Services\" /s /f\n\n# ⚠️ Redémarrage OBLIGATOIRE après"
            },
            {
                "title": "Service Consomme Trop de Ressources (CPU/RAM)",
                "code": "# Identifier service gourmand\nGet-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, CPU, WS\n\n# Associer PID au service\ntasklist /svc | findstr PID\n\n# Redémarrer service\nRestart-Service -Name NomDuService -Force\n\n# Si problème persiste: Logs\nGet-WinEvent -LogName System | Where-Object {$_.ProviderName -like '*NomDuService*'}"
            },
            {
                "title": "Dépendances de Service Manquantes",
                "code": "# Lister dépendances d'un service\nGet-Service -Name wuauserv -RequiredServices  # Services requis\nGet-Service -Name wuauserv -DependentServices # Services dépendants\n\n# CMD\nsc enumdepend wuauserv\n\n# Démarrer service avec dépendances\nnet start wuauserv /y  # /y = démarrer dépendances aussi"
            },
            {
                "title": "Service Introuvable/Supprimé par Erreur",
                "code": "# Réinstaller service Windows Update (exemple)\nsc create wuauserv binPath= \"C:\\Windows\\System32\\svchost.exe -k netsvcs\" start= auto\nsc description wuauserv \"Enables the detection, download, and installation of updates for Windows and other programs.\"\n\n# Ou via installation .inf\npnputil /add-driver C:\\Windows\\inf\\wuaueng.inf /install\n\n# Réparer tous services: DISM + SFC\nDISM /Online /Cleanup-Image /RestoreHealth\nsfc /scannow"
            },
            {
                "title": "Mode Sans Échec pour Dépannage Services",
                "bullets": [
                    "Windows démarre uniquement services essentiels en Mode Sans Échec",
                    "Utile pour isoler un service problématique",
                    "Étape 1: Redémarrer en Mode Sans Échec (msconfig → Boot → Safe boot)",
                    "Étape 2: Désactiver services suspects",
                    "Étape 3: Redémarrer normalement et tester"
                ]
            },
            {
                "warning": "⚠️ Ne supprimez JAMAIS un service système critique. Utilisez 'Désactivé' au lieu de 'sc delete' sauf si vous êtes 100% sûr."
            },
            {
                "info": "💡 L'outil Autoruns (Sysinternals) affiche TOUS les services avec leurs détails. Indispensable pour dépannage avancé."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3F: SÉCURITÉ WINDOWS (5 guides)
    # =========================================================================

    "sec_defender": {
        "title": "🛡️ Windows Defender - Antivirus Intégré",
        "sections": [
            {
                "title": "Windows Defender - Protection Gratuite Efficace",
                "content": "Windows Defender (Microsoft Defender Antivirus) est l'antivirus gratuit intégré à Windows 10/11. Autrefois médiocre, il est désormais l'un des meilleurs antivirus gratuits avec protection en temps réel, analyse cloud, et protection contre ransomwares."
            },
            {
                "title": "Activer/Désactiver Windows Defender",
                "code": "# PowerShell (ADMIN) - Activer protection temps réel\nSet-MpPreference -DisableRealtimeMonitoring $false\n\n# Désactiver (temporaire, pour tests)\nSet-MpPreference -DisableRealtimeMonitoring $true\n\n# Vérifier statut\nGet-MpComputerStatus\n\n# Via Registre (désactivation permanente - déconseillé)\nreg add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\" /v DisableAntiSpyware /t REG_DWORD /d 1 /f"
            },
            {
                "title": "Scanner Rapide/Complet",
                "code": "# PowerShell - Scan rapide\nStart-MpScan -ScanType QuickScan\n\n# Scan complet (long)\nStart-MpScan -ScanType FullScan\n\n# Scan personnalisé\nStart-MpScan -ScanType CustomScan -ScanPath \"C:\\Dossier\"\n\n# Scan hors ligne (redémarre en WinRE)\nStart-MpWDOScan"
            },
            {
                "title": "Mettre à Jour Définitions",
                "code": "# PowerShell\nUpdate-MpSignature\n\n# Forcer mise à jour cloud\nUpdate-MpSignature -UpdateSource MicrosoftUpdateServer\n\n# CMD\n\"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe\" -SignatureUpdate"
            },
            {
                "title": "Exclusions - Fichiers/Dossiers",
                "code": "# Ajouter exclusion dossier\nAdd-MpPreference -ExclusionPath \"C:\\MesJeux\"\n\n# Ajouter exclusion extension\nAdd-MpPreference -ExclusionExtension \".exe\"\n\n# Ajouter exclusion processus\nAdd-MpPreference -ExclusionProcess \"game.exe\"\n\n# Lister exclusions\nGet-MpPreference | Select-Object -ExpandProperty ExclusionPath\n\n# Supprimer exclusion\nRemove-MpPreference -ExclusionPath \"C:\\MesJeux\""
            },
            {
                "title": "Historique des Menaces",
                "code": "# Lister menaces détectées\nGet-MpThreat\n\n# Détails menace\nGet-MpThreat | Format-List *\n\n# Supprimer menaces quarantaine\nRemove-MpThreat\n\n# Restaurer fichier de quarantaine (faux positif)\nRestore-MpPreference"
            },
            {
                "warning": "⚠️ NE désactivez JAMAIS Windows Defender sans installer un autre antivirus. Un PC sans protection est compromis en minutes sur internet."
            }
        ]
    },

    "sec_firewall": {
        "title": "🔥 Pare-feu Windows - Configuration",
        "sections": [
            {
                "title": "Pare-feu Windows - Protection Réseau",
                "content": "Le Pare-feu Windows filtre le trafic réseau entrant/sortant pour bloquer connexions non autorisées. Essentiel pour sécurité, même derrière un routeur."
            },
            {
                "title": "Activer/Désactiver Pare-feu",
                "code": "# PowerShell (ADMIN)\nSet-NetFirewallProfile -Profile Domain,Public,Private -Enabled True\n\n# Désactiver (déconseillé)\nSet-NetFirewallProfile -Profile Domain,Public,Private -Enabled False\n\n# CMD\nnetsh advfirewall set allprofiles state on\nnetsh advfirewall set allprofiles state off\n\n# Vérifier statut\nGet-NetFirewallProfile | Select-Object Name, Enabled"
            },
            {
                "title": "Créer Règle de Pare-feu",
                "code": "# Bloquer programme\nNew-NetFirewallRule -DisplayName \"Bloquer Chrome\" -Direction Outbound -Program \"C:\\Program Files\\Google\\Chrome\\chrome.exe\" -Action Block\n\n# Autoriser programme\nNew-NetFirewallRule -DisplayName \"Autoriser Serveur\" -Direction Inbound -Program \"C:\\serveur.exe\" -Action Allow\n\n# Bloquer port\nNew-NetFirewallRule -DisplayName \"Bloquer Port 80\" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Block\n\n# Autoriser port\nNew-NetFirewallRule -DisplayName \"Ouvrir Port 8080\" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow"
            },
            {
                "title": "Lister/Supprimer Règles",
                "code": "# Lister toutes règles\nGet-NetFirewallRule | Format-Table DisplayName, Enabled, Direction, Action\n\n# Règles actives seulement\nGet-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'}\n\n# Supprimer règle\nRemove-NetFirewallRule -DisplayName \"Bloquer Chrome\"\n\n# Désactiver règle\nDisable-NetFirewallRule -DisplayName \"Nom de la règle\""
            },
            {
                "title": "Réinitialiser Pare-feu",
                "code": "# Reset complet (ADMIN)\nnetsh advfirewall reset\n\n# Restaurer valeurs par défaut\nnetsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound"
            }
        ]
    },

    "sec_uac": {
        "title": "🔒 Contrôle de Compte Utilisateur (UAC)",
        "sections": [
            {
                "title": "UAC - Protection Élévation Privilèges",
                "content": "L'UAC (User Account Control) demande confirmation avant exécution de programmes nécessitant droits admin. Empêche malwares de modifier système sans votre accord."
            },
            {
                "title": "Niveaux UAC",
                "bullets": [
                    "Toujours notifier - Sécurité maximale, nombreux popups",
                    "Notifier seulement si programmes modifient PC - Par défaut, équilibre",
                    "Notifier seulement (pas d'atténuation écran) - Moins sécurisé",
                    "Ne jamais notifier - Dangereux, tout s'exécute en admin"
                ]
            },
            {
                "title": "Modifier Niveau UAC",
                "code": "# Via interface\nUserAccountControlSettings.exe\n\n# PowerShell - Désactiver UAC (déconseillé)\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v EnableLUA /t REG_DWORD /d 0 /f\n\n# Activer UAC\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v EnableLUA /t REG_DWORD /d 1 /f\n\n# ⚠️ Redémarrage requis"
            },
            {
                "title": "Exécuter en Tant qu'Administrateur",
                "code": "# PowerShell - Démarrer processus en admin\nStart-Process powershell -Verb RunAs\nStart-Process cmd -Verb RunAs\nStart-Process \"C:\\programme.exe\" -Verb RunAs\n\n# Vérifier si processus actuel est admin\n([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]\"Administrator\")"
            },
            {
                "warning": "⚠️ Ne désactivez JAMAIS l'UAC sur un PC utilisé quotidiennement. C'est une protection essentielle contre malwares."
            }
        ]
    },

    "sec_updates": {
        "title": "⬆️ Mises à Jour de Sécurité Windows",
        "sections": [
            {
                "title": "Importance des Mises à Jour",
                "content": "Les mises à jour Windows corrigent vulnérabilités de sécurité critiques. Les PC non mis à jour sont compromis par exploits connus (WannaCry, EternalBlue, etc.)."
            },
            {
                "title": "Vérifier Mises à Jour",
                "code": "# PowerShell\nGet-WindowsUpdate\n\n# Installer toutes mises à jour\nInstall-WindowsUpdate -AcceptAll -AutoReboot\n\n# Windows Update via CMD\nusoclient StartScan\nusoclient StartDownload\nusoclient StartInstall\n\n# Via settings\nms-settings:windowsupdate"
            },
            {
                "title": "Historique des Mises à Jour",
                "code": "# Lister mises à jour installées\nGet-HotFix | Format-Table -AutoSize\n\n# Trier par date\nGet-HotFix | Sort-Object InstalledOn -Descending\n\n# Mise à jour spécifique\nGet-HotFix -Id KB5000001\n\n# Via WMIC\nwmic qfe list brief /format:table"
            },
            {
                "title": "Désinstaller Mise à Jour Problématique",
                "code": "# PowerShell\n$kb = \"KB5000001\"\nwusa /uninstall /kb:$kb /quiet /norestart\n\n# Ou via Panneau de configuration\nappwiz.cpl  # → Afficher mises à jour installées"
            }
        ]
    },

    "sec_malware": {
        "title": "🦠 Protection contre Malwares",
        "sections": [
            {
                "title": "Types de Malwares",
                "bullets": [
                    "Virus - Se réplique en infectant fichiers",
                    "Trojan - Se déguise en programme légitime",
                    "Ransomware - Chiffre fichiers et demande rançon",
                    "Spyware - Vole données personnelles",
                    "Adware - Affiche publicités intrusives",
                    "Rootkit - Cache présence malware, contrôle total système"
                ]
            },
            {
                "title": "Scanner avec Windows Defender",
                "code": "# PowerShell - Scan rapide\nStart-MpScan -ScanType QuickScan\n\n# Scan complet\nStart-MpScan -ScanType FullScan\n\n# Scan hors ligne (boot WinRE)\nStart-MpWDOScan\n\n# CMD\n\"%ProgramFiles%\\Windows Defender\\MpCmdRun.exe\" -Scan -ScanType 2"
            },
            {
                "title": "Outils Gratuits Anti-Malware Recommandés",
                "bullets": [
                    "Malwarebytes - Excellent scanner gratuit",
                    "HitmanPro - Scan cloud multi-moteurs",
                    "AdwCleaner - Spécialisé adwares/toolbars",
                    "ESET Online Scanner - Scan ponctuel efficace",
                    "Kaspersky Virus Removal Tool - Scanner gratuit",
                    "ComboFix - Outil avancé (expert seulement)"
                ]
            },
            {
                "title": "Nettoyage Manuel (Avancé)",
                "code": "# Démarrer en Mode Sans Échec\nmsconfig  # → Onglet Démarrage → Mode sans échec\n\n# Scanner démarrages suspects\nautoruns.exe  # (Sysinternals)\n\n# Vérifier processus actifs\ntasklist /v\n\n# Scanner clés Run\nregedit  # → HKLM/HKCU\\...\\Run\n\n# Nettoyer temp\ndel /q /f /s %TEMP%\\*"
            },
            {
                "warning": "⚠️ Si infection ransomware: Débranchez IMMÉDIATEMENT internet, n'éteignez PAS le PC. Consultez expert avant action."
            },
            {
                "info": "💡 Le scanner de virus de NiTriTe utilise plusieurs moteurs antivirus pour détection multi-couches."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3G: WINDOWS LEGACY (10 guides) - Windows 8/7/Vista/XP
    # =========================================================================

    "w8_intro": {
        "title": "🪟 Introduction à Windows 8/8.1",
        "sections": [
            {
                "title": "Windows 8/8.1 - L'Ère Tactile",
                "content": "Windows 8 (2012) et 8.1 (2013) ont introduit l'interface Modern UI tactile avec tuiles animées. Controversé à cause de la suppression du menu Démarrer, il a été rapidement remplacé par Windows 10. Support terminé en 2023."
            },
            {
                "title": "Nouveautés Windows 8",
                "bullets": [
                    "Interface Modern UI (Metro) - Tuiles tactiles",
                    "Écran d'accueil remplace Menu Démarrer",
                    "Windows Store - Magasin d'applications",
                    "Démarrage ultra-rapide (Fast Boot)",
                    "Gestionnaire des tâches amélioré",
                    "Montage ISO natif",
                    "Réinitialisation PC intégrée"
                ]
            },
            {
                "title": "Configuration Requise",
                "bullets": [
                    "Processeur: 1 GHz ou plus rapide",
                    "RAM: 1 GB (32-bit) / 2 GB (64-bit)",
                    "Disque: 16 GB (32-bit) / 20 GB (64-bit)",
                    "Carte graphique: DirectX 9 avec WDDM 1.0",
                    "Écran: 1024x768 (1366x768 pour snap apps)"
                ]
            },
            {
                "title": "Raccourcis Clés Windows 8",
                "code": "Win + C           # Charms bar (paramètres)\nWin + X           # Menu avancé (Power User)\nWin + Tab         # Basculer apps Modern\nWin + D           # Bureau classique\nWin + I           # Paramètres\nWin + Q           # Rechercher apps\nWin + W           # Rechercher paramètres\nWin + F           # Rechercher fichiers"
            },
            {
                "warning": "⚠️ Windows 8.1 n'est plus supporté depuis janvier 2023. Passez à Windows 10/11 pour sécurité."
            }
        ]
    },

    "w8_install": {
        "title": "💿 Installation Windows 8/8.1",
        "sections": [
            {
                "title": "Obtenir Windows 8.1",
                "content": "Windows 8.1 n'est plus vendu officiellement. Pour installer:\n• Télécharger ISO depuis archive Microsoft (si clé valide)\n• Utiliser clé de produit Windows 8 existante\n• Mise à niveau depuis Windows 7 (si encore activé)"
            },
            {
                "title": "Créer USB Bootable",
                "code": "# Télécharger Windows 8.1 ISO\n# Utiliser Rufus ou Media Creation Tool\n\n# Via CMD (DiskPart)\ndiskpart\nlist disk\nselect disk 1  # Votre clé USB\nclean\ncreate partition primary\nselect partition 1\nactive\nformat fs=fat32 quick\nassign\nexit\n\n# Copier contenu ISO sur USB\nxcopy D:\\* E:\\ /E /H /F  # D=ISO monté, E=USB"
            },
            {
                "title": "Installation Propre",
                "bullets": [
                    "1. Booter sur USB (F12/DEL au démarrage)",
                    "2. Choisir langue → Suivant",
                    "3. Installer maintenant",
                    "4. Entrer clé produit (ou passer)",
                    "5. Accepter licence",
                    "6. Personnalisée (installation propre)",
                    "7. Sélectionner partition → Suivant",
                    "8. Attendre installation (20-40 min)",
                    "9. Configurer compte utilisateur"
                ]
            },
            {
                "info": "💡 Préférez Windows 8.1 Update à Windows 8 RTM. Téléchargez toujours la dernière version ISO."
            }
        ]
    },

    "w8_optimize": {
        "title": "⚡ Optimisation Windows 8/8.1",
        "sections": [
            {
                "title": "Désactiver Modern UI / Restaurer Menu Démarrer",
                "content": "Solutions pour retrouver interface classique:\n• Classic Shell (gratuit) - Menu Démarrer classique\n• Start8 (payant) - Menu Start personnalisable\n• StartIsBack (payant) - Interface Windows 7\n• Windows 8.1 Update - Bouton Démarrer limité intégré"
            },
            {
                "title": "Optimisations Performances",
                "code": "# Désactiver animations\nSystemPropertiesPerformance.exe\n# → Ajuster pour performance maximale\n\n# Désactiver indexation (SSD)\nsc config WSearch start= disabled\n\n# Désactiver Superfetch (SSD)\nsc config SysMain start= disabled\n\n# Nettoyer disque\ncleanmgr /sageset:1\ncleanmgr /sagerun:1"
            },
            {
                "title": "Désactiver Apps Modern Inutiles",
                "code": "# PowerShell (ADMIN) - Supprimer apps préinstallées\nGet-AppxPackage *bingfinance* | Remove-AppxPackage\nGet-AppxPackage *bingnews* | Remove-AppxPackage\nGet-AppxPackage *bingsports* | Remove-AppxPackage\nGet-AppxPackage *xboxapp* | Remove-AppxPackage\nGet-AppxPackage *zunemusic* | Remove-AppxPackage\nGet-AppxPackage *zunevideo* | Remove-AppxPackage\nGet-AppxPackage *solitaire* | Remove-AppxPackage"
            },
            {
                "info": "💡 Windows 8.1 est plus rapide que Windows 7 sur SSD grâce à optimisations boot/hybernation."
            }
        ]
    },

    "w7_intro": {
        "title": "🪟 Introduction à Windows 7",
        "sections": [
            {
                "title": "Windows 7 - Le Classique Aimé",
                "content": "Windows 7 (2009) est considéré comme l'un des meilleurs Windows jamais créés. Interface Aero élégante, stabilité excellente, compatibilité logicielle maximale. Support étendu terminé en janvier 2020, mais encore utilisé par millions d'utilisateurs."
            },
            {
                "title": "Éditions Windows 7",
                "bullets": [
                    "Starter - Netbooks uniquement, très limité",
                    "Home Basic - Marché émergents, pas d'Aero",
                    "Home Premium - Grand public, Aero, Media Center",
                    "Professional - Entreprises, domaine, XP Mode",
                    "Ultimate - Toutes fonctionnalités, BitLocker, 35 langues",
                    "Enterprise - Entreprises uniquement (licence volume)"
                ]
            },
            {
                "title": "Configuration Requise",
                "bullets": [
                    "Processeur: 1 GHz 32/64-bit",
                    "RAM: 1 GB (32-bit) / 2 GB (64-bit)",
                    "Disque: 16 GB (32-bit) / 20 GB (64-bit)",
                    "Carte graphique: DirectX 9 avec WDDM 1.0 (pour Aero)",
                    "Recommandé: 4 GB RAM, processeur dual-core"
                ]
            },
            {
                "title": "Fonctionnalités Clés",
                "bullets": [
                    "Interface Aero - Effets vitrés, Flip 3D, Peek",
                    "Bibliothèques - Organisation virtuelle fichiers",
                    "Jump Lists - Accès rapide tâches récentes",
                    "Snap - Ancrage fenêtres (Win+Flèches)",
                    "XP Mode - Virtualisation Windows XP (Pro+)",
                    "Media Center - Divertissement (Home Premium+)",
                    "HomeGroup - Partage réseau simplifié"
                ]
            },
            {
                "warning": "⚠️ Windows 7 ne reçoit PLUS de mises à jour de sécurité depuis 2020. Utilisation non recommandée sur internet."
            }
        ]
    },

    "w7_install": {
        "title": "💿 Installation Windows 7 & Drivers",
        "sections": [
            {
                "title": "Obtenir Windows 7 ISO",
                "content": "Microsoft ne vend plus Windows 7 officiellement. Options:\n• Télécharger ISO officiel depuis archives Microsoft (avec clé valide)\n• Utiliser DVD d'installation original\n• Version MSDN/TechNet (licence entreprise)\n\n⚠️ Support terminé = Pas de mises à jour sécurité!"
            },
            {
                "title": "Installation Propre Windows 7",
                "bullets": [
                    "1. Créer USB bootable (Rufus recommandé)",
                    "2. Booter sur USB (modifier ordre boot BIOS)",
                    "3. Choisir langue, format heure, clavier",
                    "4. Installer maintenant",
                    "5. Entrer clé produit 25 caractères",
                    "6. Choisir édition (si clé générique)",
                    "7. Accepter termes de licence",
                    "8. Personnalisée (installation propre)",
                    "9. Sélectionner partition / Formater si nécessaire",
                    "10. Attendre copie fichiers (20-40 minutes)",
                    "11. Créer utilisateur et mot de passe",
                    "12. Entrer clé (si pas fait) et activer"
                ]
            },
            {
                "title": "Drivers Windows 7 (PC Récents)",
                "content": "Problème: PC modernes (2016+) n'ont PAS de drivers Windows 7 officiels.\n\nSolutions:\n• Drivers génériques USB 3.0 (Intel/AMD)\n• Intégrer drivers dans ISO avec NTLite\n• Utiliser Snappy Driver Installer\n• Télécharger drivers fabricant (Lenovo, Dell, HP)\n• Passer en Windows 10/11 (recommandé)"
            },
            {
                "title": "Intégrer USB 3.0 dans ISO Windows 7",
                "code": "# Télécharger NTLite ou DISM++\n# Télécharger drivers USB 3.0 Intel/AMD\n\n# Via DISM (avancé)\nDism /Mount-Image /ImageFile:C:\\Win7\\sources\\install.wim /Index:1 /MountDir:C:\\Mount\nDism /Image:C:\\Mount /Add-Driver /Driver:C:\\Drivers\\USB3 /Recurse\nDism /Unmount-Image /MountDir:C:\\Mount /Commit\n\n# Créer nouveau ISO avec oscdimg"
            },
            {
                "title": "Post-Installation Essentielle",
                "bullets": [
                    "1. Installer drivers chipset (priorité #1)",
                    "2. Installer drivers graphiques (NVIDIA/AMD/Intel)",
                    "3. Installer drivers réseau (Ethernet/WiFi)",
                    "4. Installer drivers audio (Realtek)",
                    "5. Windows Update (si serveurs encore actifs)",
                    "6. Service Pack 1 + Convenience Rollup (updates groupées)",
                    "7. .NET Framework 4.8",
                    "8. DirectX End-User Runtime",
                    "9. Visual C++ Redistributables (toutes versions)"
                ]
            },
            {
                "info": "💡 Snappy Driver Installer Origin (SDIO) détecte et installe TOUS les drivers Windows 7 automatiquement. Indispensable!"
            }
        ]
    },

    "w7_optimize": {
        "title": "⚡ Optimisation & Tweaks Windows 7",
        "sections": [
            {
                "title": "Tweaks Performances Visuelles",
                "code": "# Désactiver Aero (gain RAM)\nsc stop uxsms\nsc config uxsms start= disabled\n\n# Ou ajuster effets visuels\nSystemPropertiesPerformance.exe\n# → Ajuster pour performance maximale\n\n# Désactiver transparence uniquement\nreg add \"HKCU\\Software\\Microsoft\\Windows\\DWM\" /v EnableAeroPeek /t REG_DWORD /d 0 /f\nreg add \"HKCU\\Software\\Microsoft\\Windows\\DWM\" /v CompositionPolicy /t REG_DWORD /d 0 /f"
            },
            {
                "title": "Optimiser Démarrage",
                "code": "# Désactiver programmes démarrage\nmsconfig  # → Onglet Démarrage\n\n# Services inutiles à désactiver\nsc config TabletInputService start= disabled  # Tablet PC\nsc config Fax start= disabled\nsc config HomeGroupListener start= disabled\nsc config HomeGroupProvider start= disabled\nsc config WMPNetworkSvc start= disabled  # Windows Media Player Network\nsc config WSearch start= disabled  # Windows Search (si SSD)"
            },
            {
                "title": "Nettoyer Disque Système",
                "code": "# Nettoyage disque automatisé\ncleanmgr /sageset:1  # Configurer\ncleanmgr /sagerun:1  # Exécuter\n\n# Supprimer fichiers Windows.old\nrd /s /q C:\\Windows.old\n\n# Désactiver hibernation (libère Go)\npowercfg -h off\n\n# Réduire taille System Restore\nvssadmin Resize ShadowStorage /For=C: /On=C: /MaxSize=2GB"
            },
            {
                "title": "Tweaks Registre Windows 7",
                "code": "# Accélérer menu contextuel\nreg add \"HKCU\\Control Panel\\Desktop\" /v MenuShowDelay /t REG_SZ /d 0 /f\n\n# Désactiver messages sécurité UAC\nreg add \"HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f\n\n# Désactiver défragmentation auto (SSD)\nschtasks /Change /TN \"\\Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /DISABLE\n\n# Désactiver Customer Experience Program\nreg add \"HKLM\\SOFTWARE\\Microsoft\\SQMClient\\Windows\" /v CEIPEnable /t REG_DWORD /d 0 /f"
            },
            {
                "info": "💡 Windows 7 sur SSD avec 4GB+ RAM et tweaks = Expérience ultra-rapide, meilleure que Windows 10 sur vieux PC."
            }
        ]
    },

    "w7_legacy": {
        "title": "📜 Windows 7 - Support & Mises à Jour Post-2020",
        "sections": [
            {
                "title": "Fin de Support - Que Faire?",
                "content": "Support étendu Windows 7 terminé le 14 janvier 2020. Depuis cette date:\n• Aucune mise à jour de sécurité (sauf ESU payant entreprises)\n• Vulnérabilités non corrigées\n• Nouveaux logiciels incompatibles (Chrome, Firefox versions récentes)\n• Risque malware élevé sur internet\n\nOptions:\n1. Passer à Windows 10/11 (recommandé)\n2. Utiliser hors ligne uniquement (machine virtuelle, gaming rétro)\n3. Linux (Ubuntu, Mint) pour redonner vie au PC\n4. Continuer avec précautions (antivirus renforcé, pas de données sensibles)"
            },
            {
                "title": "Dernières Mises à Jour Disponibles",
                "bullets": [
                    "Service Pack 1 (SP1) - KB976932 - Obligatoire",
                    "Convenience Rollup - KB3125574 - Updates groupées jusqu'à 2016",
                    "Update KB4474419 - Dernier rollup septembre 2019",
                    "Update KB4490628 - Mars 2019 SHA-2",
                    ".NET Framework 4.8 - Dernier runtime",
                    "Internet Explorer 11 - Dernier IE (mais obsolète)"
                ]
            },
            {
                "title": "Installer Convenience Rollup",
                "code": "# Ordre d'installation (CRITIQUE)\n# 1. Service Pack 1 d'abord\nwusa Windows6.1-KB976932-X64.msu /quiet /norestart\n\n# 2. Prérequis Servicing Stack\nwusa Windows6.1-KB3020369-x64.msu /quiet /norestart\n\n# 3. Convenience Rollup (toutes updates jusqu'à 2016)\nwusa Windows6.1-KB3125574-v4-x64.msu /quiet /norestart\n\n# 4. Dernier rollup mensuel\nwusa Windows6.1-KB4490628-x64.msu /quiet /norestart\n\n# Redémarrer\nshutdown /r /t 0"
            },
            {
                "title": "Continuer à Utiliser Windows 7 (Précautions)",
                "bullets": [
                    "✅ Installer antivirus tiers à jour (Avast, AVG, Kaspersky supportent encore W7)",
                    "✅ Utiliser navigateur à jour: Firefox ESR ou Brave (supportent encore W7 en 2024)",
                    "✅ Bloquer ports avec pare-feu matériel (routeur)",
                    "✅ Pas de données bancaires/sensibles",
                    "✅ Sauvegardes régulières (en cas ransomware)",
                    "✅ 0patch (service tiers payant - patches non officiels)",
                    "❌ Ne PAS utiliser pour travail professionnel",
                    "❌ Ne PAS ouvrir emails/pièces jointes suspectes",
                    "❌ Ne PAS télécharger logiciels inconnus"
                ]
            },
            {
                "title": "Migration Windows 7 → Windows 10/11",
                "code": "# Vérifier compatibilité matérielle\n# Windows 10: quasi tous PC Windows 7\n# Windows 11: TPM 2.0 + CPU 8ème gen Intel/2ème gen Ryzen\n\n# Télécharger Media Creation Tool\n# https://www.microsoft.com/software-download/windows10\n\n# Mise à niveau (conserve fichiers)\n# Lancer MediaCreationTool → Mettre à niveau ce PC\n\n# Ou installation propre (recommandé)\n# Sauvegarder données → Boot USB → Installation propre"
            },
            {
                "warning": "⚠️ Utiliser Windows 7 en 2024+ sur internet = DANGER. Passez à Windows 10 ou Linux."
            },
            {
                "info": "💡 Si PC trop vieux pour Windows 10: Linux Mint ressemble à Windows 7 et redonne vie aux vieux PC."
            }
        ]
    },

    "vista_intro": {
        "title": "🪟 Windows Vista - Guide Rapide",
        "sections": [
            {
                "title": "Windows Vista (2006-2017)",
                "content": "Windows Vista, lancé en 2006, a introduit l'interface Aero vitrée, UAC, et la recherche instantanée. Initialement critiqué pour bugs et lenteur, il s'est amélioré avec le SP2. Remplacé par Windows 7 en 2009. Support terminé en 2017."
            },
            {
                "title": "Nouveautés Vista",
                "bullets": [
                    "Interface Aero Glass - Effets vitrés translucides",
                    "UAC (User Account Control) - Sécurité renforcée",
                    "Windows Defender intégré",
                    "Recherche instantanée",
                    "Windows DVD Maker",
                    "ReadyBoost - Utiliser USB comme cache",
                    "SuperFetch - Préchargement apps",
                    "DirectX 10 (exclusif Vista à l'époque)"
                ]
            },
            {
                "title": "Configuration Minimale (Réaliste)",
                "bullets": [
                    "Processeur: Dual-core 2 GHz minimum",
                    "RAM: 2 GB minimum, 4 GB recommandé",
                    "Disque: 40 GB",
                    "Carte graphique: 512 MB VRAM pour Aero",
                    "Note: Vista est TRÈS gourmand pour l'époque"
                ]
            },
            {
                "warning": "⚠️ Windows Vista non supporté depuis 2017. N'utilisez PAS sur internet. Passez à Windows 10 ou Linux."
            }
        ]
    },

    "vista_optimize": {
        "title": "⚡ Optimisation Windows Vista",
        "sections": [
            {
                "title": "Installer Service Pack 2 (Obligatoire)",
                "content": "SP2 corrige ÉNORMÉMENT de bugs Vista. Installation obligatoire.\n\n1. Installer SP1 d'abord (prérequis SP2)\n2. Installer SP2\n3. Installer Platform Update (améliore perfs)\n\nTéléchargement: Microsoft Update Catalog (archives)"
            },
            {
                "title": "Tweaks Performances",
                "code": "# Désactiver Aero (gros gain RAM/GPU)\nsc stop uxsms\nsc config uxsms start= disabled\n\n# Désactiver indexation\nsc config WSearch start= disabled\n\n# Désactiver SuperFetch (SSD uniquement)\nsc config SysMain start= disabled\n\n# Désactiver Sidebar\nreg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\" /v Sidebar /t REG_SZ /d \"\" /f\n\n# Plan alimentation Haute Performance\npowercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
            },
            {
                "title": "ReadyBoost (Si pas de SSD)",
                "bullets": [
                    "Insérer clé USB rapide (4GB+)",
                    "Propriétés clé → Onglet ReadyBoost",
                    "Utiliser ce périphérique",
                    "Allouer espace maximum",
                    "Windows utilise USB comme cache RAM"
                ]
            },
            {
                "info": "💡 Vista SP2 + 4GB RAM + SSD + tweaks = Performances correctes. Mais Windows 7 reste meilleur."
            }
        ]
    },

    "xp_intro": {
        "title": "🪟 Windows XP - Guide Complet Legacy",
        "sections": [
            {
                "title": "Windows XP (2001-2014) - Le Légendaire",
                "content": "Windows XP, sorti en 2001, est le Windows le plus emblématique. Interface Luna colorée, stabilité NT, compatibilité maximale. Dominé le marché pendant 13 ans. Support terminé en 2014, mais encore utilisé dans systèmes embarqués et vieux PC."
            },
            {
                "title": "Éditions Windows XP",
                "bullets": [
                    "Home Edition - Grand public, pas de domaine",
                    "Professional - Entreprises, Remote Desktop, domaine",
                    "Media Center Edition - PC multimédia (Dell, HP)",
                    "Tablet PC Edition - Tablettes (stylet)",
                    "Professional x64 - 64-bit (rare, pour workstations)"
                ]
            },
            {
                "title": "Configuration Requise",
                "bullets": [
                    "Processeur: 233 MHz minimum, 1 GHz recommandé",
                    "RAM: 64 MB minimum, 512 MB recommandé",
                    "Disque: 1.5 GB",
                    "Carte graphique: Super VGA (800x600)",
                    "Note: Fonctionne sur TOUT, même Pentium II!"
                ]
            },
            {
                "title": "Pourquoi XP est Encore Utilisé?",
                "bullets": [
                    "Logiciels industriels anciens (CNC, automates)",
                    "Jeux rétro (2000-2010)",
                    "Matériel ancien sans drivers récents",
                    "Nostalgie / Collection",
                    "VM pour tester vieux logiciels",
                    "PC très anciens (Pentium III, 256MB RAM)"
                ]
            },
            {
                "warning": "⚠️ Windows XP non supporté depuis 2014. Vulnérabilités CRITIQUES non corrigées (EternalBlue, etc.). N'utilisez JAMAIS sur internet!"
            }
        ]
    },

    "xp_legacy": {
        "title": "📜 Utilisation Legacy Windows XP",
        "sections": [
            {
                "title": "Dernières Mises à Jour XP",
                "bullets": [
                    "Service Pack 3 (SP3) - Obligatoire, dernière version officielle",
                    "Update Rollup 1 (post-SP3) - KB2559049",
                    ".NET Framework 4.0 - Dernier runtime compatible",
                    "Internet Explorer 8 - Dernier IE pour XP",
                    "Windows Media Player 11",
                    "DirectX 9.0c - Dernier DirectX XP"
                ]
            },
            {
                "title": "Utiliser XP en Sécurité (Hors Ligne)",
                "bullets": [
                    "✅ Machine virtuelle (VirtualBox, VMware)",
                    "✅ PC dédié SANS connexion internet",
                    "✅ Réseau local isolé uniquement",
                    "✅ Sauvegardes fréquentes (snapshots VM)",
                    "✅ Antivirus tiers (Avast Free supportait XP jusqu'à 2018)",
                    "❌ NE JAMAIS connecter à internet",
                    "❌ NE JAMAIS insérer USB d'origine inconnue",
                    "❌ NE PAS utiliser pour données importantes"
                ]
            },
            {
                "title": "Navigateurs Compatibles XP (2024)",
                "bullets": [
                    "Aucun navigateur moderne ne supporte XP",
                    "Dernières versions compatibles:",
                    "• Chrome 49 (2016) - Obsolète, dangereux",
                    "• Firefox 52 ESR (2018) - Obsolète, dangereux",
                    "• Opera 36 (2016) - Obsolète",
                    "• Pale Moon 27 (fork Firefox, support XP prolongé mais limité)",
                    "⚠️ Tous obsolètes = vulnérables!"
                ]
            },
            {
                "title": "XP en Machine Virtuelle",
                "code": "# Installer VirtualBox\n# Télécharger ISO Windows XP SP3\n\n# Paramètres VM recommandés:\n# RAM: 512 MB (ou 1024 MB pour confort)\n# Disque: 10 GB dynamique\n# Réseau: Intérieur (pas NAT, pas de net!)\n# Guest Additions: Installer pour performance\n\n# Snapshot après install propre\nVBoxManage snapshot \"WinXP\" take \"Clean Install\"\n\n# Restaurer snapshot si corruption\nVBoxManage snapshot \"WinXP\" restore \"Clean Install\""
            },
            {
                "title": "Jeux Rétro sur XP",
                "content": "Windows XP est parfait pour jeux 2000-2010:\n• Age of Empires II\n• Need for Speed Underground 1/2\n• GTA San Andreas, Vice City\n• Half-Life 2, Counter-Strike 1.6\n• The Sims 2\n• Warcraft III\n• Command & Conquer series\n\nBcp de ces jeux ne fonctionnent PAS correctement sur Windows 10/11."
            },
            {
                "info": "💡 XP Mode de Windows 7 Pro = Machine virtuelle XP intégrée officielle. Parfait pour compatibilité logiciels anciens."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3J: RÉSEAU (5 guides)
    # =========================================================================

    "net_basics": {
        "title": "🌐 Bases du Réseau - Concepts Essentiels",
        "sections": [
            {
                "title": "Qu'est-ce qu'un Réseau?",
                "content": "Un réseau informatique relie plusieurs appareils (PC, smartphones, imprimantes, serveurs) pour partager données et ressources. Types: LAN (local), WAN (étendu), Internet (mondial)."
            },
            {
                "title": "Composants Réseau de Base",
                "bullets": [
                    "Routeur - Dirige trafic entre réseaux, connecte à internet",
                    "Switch - Connecte appareils dans un réseau local",
                    "Point d'accès WiFi - Réseau sans fil",
                    "Modem - Convertit signal internet (câble/fibre/ADSL)",
                    "Câble Ethernet - RJ45, Cat5e/Cat6/Cat6a/Cat7",
                    "Carte réseau - Ethernet (RJ45) ou WiFi (sans fil)"
                ]
            },
            {
                "title": "Adresse IP - Identifiant Réseau",
                "content": "Chaque appareil a une adresse IP unique sur le réseau.\n\nIPv4 (ancien): 192.168.1.100\n• Format: 4 nombres 0-255 séparés par points\n• Privé: 192.168.x.x, 10.x.x.x, 172.16-31.x.x\n• Public: Attribué par FAI, visible sur internet\n\nIPv6 (nouveau): 2001:0db8:85a3::8a2e:0370:7334\n• Format: 8 groupes hexadécimaux\n• Espace d'adressage quasi infini"
            },
            {
                "title": "Masque de Sous-Réseau",
                "content": "Définit quelle partie de l'IP identifie le réseau vs l'appareil.\n\nExemples:\n• 255.255.255.0 (/24) - 254 appareils max\n• 255.255.0.0 (/16) - 65534 appareils\n• 255.255.255.252 (/30) - 2 appareils (liaison point-à-point)"
            },
            {
                "title": "Passerelle (Gateway)",
                "content": "Routeur qui connecte votre réseau local à internet.\n\nTypiquement: 192.168.1.1 ou 192.168.0.1\n\nConfiguration:\n• IP PC: 192.168.1.100\n• Masque: 255.255.255.0\n• Passerelle: 192.168.1.1"
            },
            {
                "title": "DNS (Domain Name System)",
                "content": "Traduit noms de domaine en adresses IP.\n\nExemple: google.com → 142.250.185.46\n\nServeurs DNS:\n• Cloudflare: 1.1.1.1 / 1.0.0.1 (rapide)\n• Google: 8.8.8.8 / 8.8.4.4\n• OpenDNS: 208.67.222.222 / 208.67.220.220"
            },
            {
                "title": "DHCP - Attribution IP Automatique",
                "content": "Serveur DHCP (routeur) attribue automatiquement IP, masque, passerelle, DNS aux appareils.\n\nDHCP activé (défaut): Configuration automatique\nIP statique: Configuration manuelle (serveurs, imprimantes)"
            },
            {
                "title": "Commandes Réseau de Base",
                "code": "# Afficher configuration IP\nipconfig /all        # Windows\nip addr             # Linux\n\n# Tester connectivité\nping google.com\nping 8.8.8.8\n\n# Tracer route\ntracert google.com  # Windows\ntraceroute google.com  # Linux\n\n# Résoudre DNS\nnslookup google.com\n\n# Afficher table routage\nroute print         # Windows\nip route            # Linux"
            },
            {
                "info": "💡 192.168.x.x et 10.x.x.x sont adresses privées, JAMAIS routées sur internet. Votre routeur fait NAT (traduction) vers IP publique."
            }
        ]
    },

    "net_tcp_ip": {
        "title": "📡 TCP/IP & Protocoles Réseau",
        "sections": [
            {
                "title": "Modèle TCP/IP (4 Couches)",
                "bullets": [
                    "Couche 4 - Application: HTTP, FTP, DNS, SMTP (logiciels)",
                    "Couche 3 - Transport: TCP (fiable), UDP (rapide)",
                    "Couche 2 - Internet: IP (adressage, routage)",
                    "Couche 1 - Accès réseau: Ethernet, WiFi (physique)"
                ]
            },
            {
                "title": "TCP vs UDP",
                "content": "TCP (Transmission Control Protocol):\n• Fiable - Garantit livraison et ordre paquets\n• Lent - Handshake 3-way, vérifications\n• Usage: Web (HTTP), Email (SMTP), Fichiers (FTP)\n\nUDP (User Datagram Protocol):\n• Rapide - Pas de vérification, pas d'ordre\n• Non fiable - Paquets peuvent se perdre\n• Usage: Streaming vidéo, VoIP, Gaming, DNS"
            },
            {
                "title": "Ports - Portes d'Entrée Services",
                "bullets": [
                    "Port 80 - HTTP (Web non sécurisé)",
                    "Port 443 - HTTPS (Web sécurisé SSL/TLS)",
                    "Port 21 - FTP (Transfert fichiers)",
                    "Port 22 - SSH (Shell sécurisé Linux)",
                    "Port 25 - SMTP (Envoi email)",
                    "Port 53 - DNS",
                    "Port 3389 - RDP (Bureau à distance Windows)",
                    "Port 3306 - MySQL",
                    "Ports 0-1023: Réservés (wellknown)",
                    "Ports 1024-49151: Enregistrés",
                    "Ports 49152-65535: Dynamiques/Privés"
                ]
            },
            {
                "title": "Voir Ports Ouverts/Connexions",
                "code": "# Windows - Netstat\nnetstat -ano           # Toutes connexions + PID\nnetstat -an | find \"LISTENING\"  # Ports en écoute\nnetstat -an | find \":80\"  # Connexions port 80\n\n# Associer PID à programme\ntasklist | find \"PID\"\n\n# Linux\nnetstat -tulpn        # Tous ports écoute\nss -tulpn             # Alternative moderne\nlsof -i :80           # Quel process utilise port 80"
            },
            {
                "title": "NAT (Network Address Translation)",
                "content": "Le routeur traduit IP privées (192.168.x.x) en IP publique unique.\n\nExemple:\n• PC1: 192.168.1.10\n• PC2: 192.168.1.20\n• Routeur IP publique: 203.0.113.5\n\nQuand PC1 accède à internet, le routeur remplace l'IP source par l'IP publique. Permet à tout le réseau de partager 1 seule IP publique."
            },
            {
                "info": "💡 Port Forwarding (redirection de port) permet d'exposer un service interne (serveur web, jeu) sur internet via routeur."
            }
        ]
    },

    "net_dns": {
        "title": "🔍 Configuration DNS & Optimisation",
        "sections": [
            {
                "title": "DNS - Qu'est-ce que c'est?",
                "content": "Le DNS (Domain Name System) est l'annuaire d'internet. Il traduit noms de domaine lisibles (google.com) en adresses IP (142.250.185.46).\n\nSans DNS, vous devriez taper 142.250.185.46 au lieu de google.com!"
            },
            {
                "title": "Meilleurs Serveurs DNS Publics (2024)",
                "bullets": [
                    "Cloudflare (1.1.1.1): Le + rapide, privacy-focused",
                    "Google (8.8.8.8): Rapide, fiable, logs conservés",
                    "OpenDNS (208.67.222.222): Filtrage contenu optionnel",
                    "Quad9 (9.9.9.9): Sécurisé, bloque malware/phishing",
                    "AdGuard DNS (94.140.14.14): Bloque pubs"
                ]
            },
            {
                "title": "Changer DNS sur Windows",
                "code": "# Via PowerShell (ADMIN)\n$adapter = (Get-NetAdapter | Where-Object {$_.Status -eq 'Up'}).Name\nSet-DnsClientServerAddress -InterfaceAlias $adapter -ServerAddresses (\"1.1.1.1\", \"1.0.0.1\")\n\n# Vérifier\nGet-DnsClientServerAddress -InterfaceAlias $adapter\n\n# Via CMD\nnetsh interface ip set dns \"Ethernet\" static 1.1.1.1\nnetsh interface ip add dns \"Ethernet\" 1.0.0.1 index=2\n\n# Revenir au DHCP (automatique)\nnetsh interface ip set dns \"Ethernet\" dhcp"
            },
            {
                "title": "Changer DNS via Interface Windows",
                "bullets": [
                    "1. Panneau de configuration → Centre Réseau",
                    "2. Modifier paramètres carte",
                    "3. Clic droit sur Ethernet/WiFi → Propriétés",
                    "4. Protocole Internet version 4 (TCP/IPv4) → Propriétés",
                    "5. Utiliser les adresses DNS suivantes:",
                    "   • Préféré: 1.1.1.1",
                    "   • Auxiliaire: 1.0.0.1",
                    "6. OK → OK → Fermer",
                    "7. Redémarrer connexion"
                ]
            },
            {
                "title": "Vider Cache DNS",
                "code": "# Windows\nipconfig /flushdns\n\n# Linux\nsudo systemd-resolve --flush-caches\n# Ou\nsudo service nscd restart\n\n# macOS\nsudo dscacheutil -flushcache\nsudo killall -HUP mDNSResponder"
            },
            {
                "title": "Tester Vitesse DNS",
                "code": "# PowerShell - Tester résolution DNS\nMeasure-Command {Resolve-DnsName google.com -Server 1.1.1.1}\nMeasure-Command {Resolve-DnsName google.com -Server 8.8.8.8}\n\n# CMD - NSLookup\nnslookup google.com 1.1.1.1\nnslookup google.com 8.8.8.8\n\n# Outil tiers: DNS Benchmark (GRC.com)"
            },
            {
                "title": "DNS sur Routeur (Recommandé)",
                "bullets": [
                    "Avantage: Configure DNS pour TOUS appareils réseau",
                    "1. Accéder interface routeur (192.168.1.1)",
                    "2. Connexion admin (user: admin, pass: voir étiquette)",
                    "3. Paramètres WAN / Internet",
                    "4. DNS primaire: 1.1.1.1",
                    "5. DNS secondaire: 1.0.0.1",
                    "6. Sauvegarder et redémarrer routeur"
                ]
            },
            {
                "info": "💡 Cloudflare DNS (1.1.1.1) réduit temps de chargement pages de 14-20ms en moyenne vs DNS FAI. Gratuit!"
            }
        ]
    },

    "net_troubleshoot": {
        "title": "🔧 Dépannage Réseau - Problèmes Courants",
        "sections": [
            {
                "title": "Pas d'Internet - Diagnostic Étape par Étape",
                "bullets": [
                    "Étape 1: Vérifier câbles physiques / WiFi activé",
                    "Étape 2: Redémarrer routeur (débrancher 30 sec)",
                    "Étape 3: Redémarrer PC",
                    "Étape 4: Vérifier autres appareils (problème PC ou réseau?)",
                    "Étape 5: Tester avec câble Ethernet (si WiFi ne marche pas)",
                    "Étape 6: Vérifier config IP (ipconfig)",
                    "Étape 7: Ping passerelle (ping 192.168.1.1)",
                    "Étape 8: Ping DNS (ping 8.8.8.8)",
                    "Étape 9: Ping domaine (ping google.com)",
                    "Étape 10: Reset réseau Windows"
                ]
            },
            {
                "title": "Diagnostic Rapide - Commandes Essentielles",
                "code": "# 1. Configuration IP\nipconfig /all\n\n# 2. Libérer/Renouveler IP (DHCP)\nipconfig /release\nipconfig /renew\n\n# 3. Vider cache DNS\nipconfig /flushdns\n\n# 4. Ping passerelle\nping 192.168.1.1\n\n# 5. Ping internet\nping 8.8.8.8\n\n# 6. Test DNS\nping google.com\nnslookup google.com\n\n# 7. Tracer route\ntracert google.com\n\n# 8. Ports en écoute\nnetstat -an"
            },
            {
                "title": "Reset Complet Réseau Windows",
                "code": "# PowerShell/CMD (ADMIN) - Reset tout\nnetsh winsock reset\nnetsh int ip reset\nipconfig /release\nipconfig /renew\nipconfig /flushdns\n\n# Réinitialiser carte réseau\nnetsh interface set interface \"Ethernet\" disabled\nnetsh interface set interface \"Ethernet\" enabled\n\n# Ou via GUI\nms-settings:network-status\n# → Réinitialisation du réseau\n\n# Redémarrer obligatoire\nshutdown /r /t 0"
            },
            {
                "title": "WiFi Connecté mais Pas d'Internet",
                "bullets": [
                    "Symptôme: WiFi affiche 'Connecté' mais sites ne chargent pas",
                    "Cause 1: DNS incorrect → Changer pour 1.1.1.1/8.8.8.8",
                    "Cause 2: IP en double → ipconfig /release + /renew",
                    "Cause 3: Routeur bloqué → Redémarrer routeur",
                    "Cause 4: FAI coupé → Vérifier avec autre appareil",
                    "Cause 5: Pare-feu bloque → Désactiver temporairement pour test"
                ]
            },
            {
                "title": "Vitesse Lente / Latence Élevée",
                "code": "# Tester vitesse\n# speedtest.net (navigateur)\n# Ou via PowerShell\nInvoke-WebRequest -Uri https://speed.cloudflare.com\n\n# Identifier appareils gourmands\nnetstat -ano | find \"ESTABLISHED\"\n\n# Moniteur ressources réseau\nresmon.exe  # → Onglet Réseau\n\n# QoS: Limiter bande passante app\n# Panneau config → Réseau → Carte → Propriétés → QoS"
            },
            {
                "title": "Erreur 'DNS_PROBE_FINISHED_NXDOMAIN'",
                "bullets": [
                    "Signification: Domaine introuvable (problème DNS)",
                    "Solution 1: Vider cache DNS → ipconfig /flushdns",
                    "Solution 2: Changer DNS → 1.1.1.1/8.8.8.8",
                    "Solution 3: Désactiver VPN/Proxy temporairement",
                    "Solution 4: Vérifier fichier hosts (C:\\Windows\\System32\\drivers\\etc\\hosts)"
                ]
            },
            {
                "info": "💡 90% des problèmes réseau sont résolus par: 1) Redémarrer routeur, 2) ipconfig /release + /renew, 3) Changer DNS."
            }
        ]
    },

    "net_vpn": {
        "title": "🔒 VPN & Sécurité Réseau",
        "sections": [
            {
                "title": "VPN - Qu'est-ce que c'est?",
                "content": "Un VPN (Virtual Private Network) chiffre votre connexion internet et masque votre adresse IP en routant trafic via serveur distant.\n\nUsages:\n• Confidentialité: Cache activité au FAI\n• Sécurité: WiFi public sécurisé\n• Contourner géo-blocage: Netflix US, etc.\n• Travail distant: Accès réseau entreprise"
            },
            {
                "title": "VPN Gratuits vs Payants",
                "bullets": [
                    "VPN Gratuits (méfiance!):",
                    "• ProtonVPN Free - Fiable, limité vitesse",
                    "• Windscribe Free - 10GB/mois",
                    "⚠️ Évitez VPN gratuits douteux (revendent vos données)",
                    "",
                    "VPN Payants Recommandés:",
                    "• NordVPN - Rapide, gros réseau",
                    "• Mullvad - Privacy absolu, €5/mois",
                    "• ProtonVPN - Suisse, no-logs vérifié",
                    "• Surfshark - Connexions illimitées"
                ]
            },
            {
                "title": "Configurer VPN sur Windows",
                "code": "# Via GUI\nms-settings:network-vpn\n# → Ajouter connexion VPN\n\n# Via PowerShell (L2TP/IPsec)\nAdd-VpnConnection -Name \"MonVPN\" `\n    -ServerAddress \"vpn.example.com\" `\n    -TunnelType L2tp `\n    -EncryptionLevel Required `\n    -AuthenticationMethod MSChapv2 `\n    -L2tpPsk \"CléPartagée\" `\n    -Force\n\n# Connecter\nrasdial MonVPN utilisateur motdepasse\n\n# Déconnecter\nrasdial MonVPN /disconnect"
            },
            {
                "title": "Vérifier si VPN Fonctionne",
                "code": "# Vérifier IP publique\ncurl ifconfig.me\ncurl ipinfo.io\n\n# PowerShell\n(Invoke-WebRequest -Uri \"https://api.ipify.org\").Content\n\n# Avec VPN: IP doit être celle du serveur VPN, pas votre vraie IP\n# Tester DNS leak: dnsleaktest.com"
            },
            {
                "title": "Kill Switch - Sécurité VPN",
                "content": "Un Kill Switch bloque tout trafic si VPN se déconnecte (empêche fuite IP).\n\nConfiguration manuelle:\n1. Pare-feu Windows → Règles sortantes\n2. Bloquer TOUTES connexions sauf VPN\n3. Autoriser uniquement interface TAP VPN\n\nOu utiliser VPN avec kill switch intégré (NordVPN, ProtonVPN)."
            },
            {
                "title": "WireGuard - VPN Moderne Rapide",
                "content": "WireGuard est protocole VPN nouveau, ultra-rapide et sécurisé.\n\nAvantages vs OpenVPN:\n• 10x plus rapide\n• Code 4000 lignes vs 100000 (moins de bugs)\n• Consommation batterie réduite\n\nInstallez client WireGuard officiel ou via Mullvad/NordVPN."
            },
            {
                "warning": "⚠️ VPN ne vous rend PAS anonyme. Logs peuvent exister. Pour anonymat: Tor Browser (mais très lent)."
            },
            {
                "info": "💡 Sur WiFi public (café, aéroport): TOUJOURS utiliser VPN. Risque d'interception Man-in-the-Middle sinon."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3K: MATÉRIEL / HARDWARE (5 guides)
    # =========================================================================

    "hw_cpu": {
        "title": "🧠 Processeurs (CPU) - Guide Complet",
        "sections": [
            {
                "title": "CPU - Le Cerveau du PC",
                "content": "Le processeur (CPU - Central Processing Unit) exécute toutes les instructions programmes. Performances dépendent de: fréquence (GHz), nombre de cœurs, architecture, cache."
            },
            {
                "title": "Intel vs AMD (2024)",
                "bullets": [
                    "Intel (13ème/14ème gen - 2023/2024):",
                    "• i9-14900K: 24 cœurs (8P+16E), gaming/productivité",
                    "• i7-14700K: 20 cœurs, sweet spot gaming",
                    "• i5-14600K: 14 cœurs, excellent rapport qualité/prix",
                    "",
                    "AMD Ryzen (7000/9000 series - 2023/2024):",
                    "• Ryzen 9 9950X: 16 cœurs, workstation",
                    "• Ryzen 7 9700X: 8 cœurs, gaming parfait",
                    "• Ryzen 5 9600X: 6 cœurs, budget gaming"
                ]
            },
            {
                "title": "Informations CPU (Windows)",
                "code": "# PowerShell\nGet-WmiObject Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed\n\n# CMD\nwmic cpu get name, numberofcores, numberoflogicalprocessors, maxclockspeed\n\n# Utilisation temps réel\nGet-Counter '\\Processor(_Total)\\% Processor Time'\n\n# Gestionnaire des tâches\ntaskmgr  # → Onglet Performances"
            },
            {
                "title": "Température CPU",
                "bullets": [
                    "Outils gratuits:",
                    "• HWiNFO64 - Le plus complet",
                    "• Core Temp - Léger, simple",
                    "• Open Hardware Monitor",
                    "• Ryzen Master (AMD)",
                    "• Intel XTU (Intel)",
                    "",
                    "Températures normales:",
                    "• Repos: 30-45°C",
                    "• Charge: 60-80°C",
                    "• Gaming: 65-85°C",
                    "⚠️ >90°C: Dangereux, vérifier refroidissement"
                ]
            },
            {
                "title": "Optimiser Performances CPU",
                "code": "# Plan alimentation Haute Performance\npowercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c\n\n# Désactiver CPU parking (Windows 10)\nreg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583\" /v ValueMax /t REG_DWORD /d 0 /f\n\n# Désactiver C-States (BIOS) pour latence minimale gaming\n# Entrée BIOS → CPU Config → C-States → Disabled"
            },
            {
                "info": "💡 Hyperthreading (Intel) / SMT (AMD) double threads logiques. Utile pour multitâche, moins pour gaming pur."
            }
        ]
    },

    "hw_gpu": {
        "title": "🎨 Cartes Graphiques (GPU) - Guide",
        "sections": [
            {
                "title": "GPU - Moteur Graphique",
                "content": "La carte graphique (GPU) traite affichage et calculs parallèles massifs (gaming, rendu 3D, IA, mining crypto)."
            },
            {
                "title": "NVIDIA vs AMD (2024)",
                "bullets": [
                    "NVIDIA GeForce RTX 40-series (2023):",
                    "• RTX 4090: Flagship, 4K 144Hz gaming",
                    "• RTX 4080: High-end 4K",
                    "• RTX 4070: Sweet spot 1440p gaming",
                    "• RTX 4060: Budget 1080p",
                    "",
                    "AMD Radeon RX 7000-series (2023):",
                    "• RX 7900 XTX: Concurrent 4090",
                    "• RX 7800 XT: 1440p excellent",
                    "• RX 7600: Budget 1080p",
                    "",
                    "Intel Arc (2023):",
                    "• A770: Compétitif budget, drivers en amélioration"
                ]
            },
            {
                "title": "Voir Infos GPU",
                "code": "# PowerShell\nGet-WmiObject Win32_VideoController | Select-Object Name, DriverVersion, VideoModeDescription, AdapterRAM\n\n# CMD\nwmic path win32_videocontroller get name,driverversion,adapterram\n\n# NVIDIA\nnvidia-smi  # Si drivers installés\n\n# DirectX\ndxdiag  # → Onglet Affichage"
            },
            {
                "title": "Mettre à Jour Drivers GPU",
                "bullets": [
                    "NVIDIA:",
                    "• GeForce Experience (auto-update)",
                    "• Ou nvidia.com/drivers (manuel)",
                    "",
                    "AMD:",
                    "• AMD Software Adrenalin (auto-update)",
                    "• Ou amd.com/support (manuel)",
                    "",
                    "Intel:",
                    "• Intel Driver & Support Assistant",
                    "• Ou intel.com/content/www/us/en/download-center"
                ]
            },
            {
                "title": "Température & Monitoring GPU",
                "bullets": [
                    "Outils:",
                    "• MSI Afterburner - Le meilleur, OSD in-game",
                    "• GPU-Z - Infos détaillées",
                    "• HWiNFO64 - Monitoring complet",
                    "",
                    "Températures normales GPU:",
                    "• Repos: 30-45°C",
                    "• Gaming: 60-85°C",
                    "• ⚠️ >90°C: Throttling, vérifier refroidissement"
                ]
            },
            {
                "title": "Overclocking GPU (MSI Afterburner)",
                "bullets": [
                    "1. Installer MSI Afterburner",
                    "2. Augmenter Power Limit à 110-120%",
                    "3. Core Clock: +50 MHz → tester stabilité",
                    "4. Si stable: +100/+150 progressivement",
                    "5. Memory Clock: +200 MHz → tester",
                    "6. Surveiller températures (<85°C)",
                    "7. Tester avec FurMark ou 3DMark",
                    "8. Sauvegarder profil si stable"
                ]
            },
            {
                "warning": "⚠️ Overclocking annule garantie et peut endommager GPU si mal fait. Augmentez progressivement et surveillez températures!"
            }
        ]
    },

    "hw_ram": {
        "title": "💾 Mémoire RAM - Guide Complet",
        "sections": [
            {
                "title": "RAM - Mémoire Vive",
                "content": "La RAM (Random Access Memory) stocke données temporaires actives. Plus de RAM = plus de programmes ouverts simultanément sans ralentissement."
            },
            {
                "title": "Types de RAM (2024)",
                "bullets": [
                    "DDR5 (2021+): Nouvelle génération, 4800-7200 MT/s",
                    "• PC modernes (Intel 12ème+ gen, AMD Ryzen 7000+)",
                    "• Plus rapide mais + cher",
                    "",
                    "DDR4 (2014-présent): Standard actuel, 2133-3600 MT/s",
                    "• Majorité PC (Intel 6-11ème gen, Ryzen 1000-5000)",
                    "• Meilleur rapport qualité/prix",
                    "",
                    "DDR3 (2007-2015): Ancien, 800-2133 MT/s",
                    "• PC anciens, incompatible DDR4/DDR5"
                ]
            },
            {
                "title": "Combien de RAM?",
                "bullets": [
                    "8 GB: Minimum, bureautique légère",
                    "16 GB: Sweet spot 2024, gaming 1080p/1440p",
                    "32 GB: Gaming 4K, streaming, montage vidéo",
                    "64 GB+: Workstation, rendu 3D, VMs multiples",
                    "",
                    "Note: Windows 11 recommande 8GB minimum"
                ]
            },
            {
                "title": "Voir Infos RAM",
                "code": "# PowerShell - Infos RAM\nGet-WmiObject Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed, PartNumber\n\n# Total RAM installée\n(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB\n\n# Utilisation actuelle\nGet-Counter '\\Memory\\Available MBytes'\n\n# CMD\nwmic memorychip get capacity,speed,manufacturer,partnumber\n\n# Ou Gestionnaire des tâches → Performances → Mémoire"
            },
            {
                "title": "Tester Stabilité RAM (MemTest)",
                "bullets": [
                    "MemTest86 (bootable USB):",
                    "1. Télécharger memtest86.com",
                    "2. Créer USB bootable",
                    "3. Booter dessus",
                    "4. Lancer test complet (8+ passes, 4-12h)",
                    "5. 0 erreur = RAM stable",
                    "6. Erreurs = RAM défectueuse ou OC instable",
                    "",
                    "Windows Memory Diagnostic:",
                    "• mdsched.exe → Redémarrer et tester"
                ]
            },
            {
                "title": "Activer XMP/DOCP (Overclock RAM)",
                "bullets": [
                    "XMP (Intel) / DOCP (AMD) active profil RAM haute vitesse.",
                    "",
                    "1. Entrer BIOS (DEL/F2 au boot)",
                    "2. Chercher 'XMP' ou 'DOCP' ou 'A-XMP'",
                    "3. Activer profil 1 (fréquence max RAM)",
                    "4. Sauvegarder et redémarrer",
                    "5. Vérifier vitesse: Task Manager → Perf → Mémoire",
                    "",
                    "Exemple: RAM 3200 MHz → Active XMP → Passe de 2133 à 3200",
                    "Gain gaming: +5-15 FPS selon jeu"
                ]
            },
            {
                "info": "💡 Dual Channel double bande passante RAM. Utilisez 2 barrettes identiques sur slots 2+4 (consultez manuel carte mère)."
            }
        ]
    },

    "hw_storage": {
        "title": "💿 Stockage (SSD/HDD) - Guide",
        "sections": [
            {
                "title": "SSD vs HDD - Différences",
                "content": "SSD (Solid State Drive):\n✅ Rapide: 500-7000 MB/s\n✅ Silencieux, résistant chocs\n✅ Faible consommation\n❌ Cher par GB\n❌ Durée vie limitée (TBW)\n\nHDD (Hard Disk Drive):\n✅ Pas cher, capacités énormes\n❌ Lent: 80-160 MB/s\n❌ Fragile (disques mécaniques)\n❌ Bruyant"
            },
            {
                "title": "Types de SSD",
                "bullets": [
                    "NVMe M.2 (PCIe 4.0/5.0): Ultra-rapide, 3500-14000 MB/s",
                    "• Format stick, se branche sur carte mère",
                    "• Recommandé: Samsung 990 Pro, WD Black SN850X",
                    "",
                    "SATA SSD (2.5\"): Rapide, 500-550 MB/s",
                    "• Même format que HDD laptop",
                    "• Moins cher que NVMe",
                    "• Recommandé: Samsung 870 EVO, Crucial MX500",
                    "",
                    "M.2 SATA: M.2 mais vitesse SATA (550 MB/s max)",
                    "• Vérifiez compatibilité slot M.2 (NVMe ou SATA)"
                ]
            },
            {
                "title": "Voir Santé SSD/HDD",
                "code": "# PowerShell - Infos disques\nGet-PhysicalDisk | Select-Object FriendlyName, MediaType, Size, HealthStatus\n\n# SMART status\nwmic diskdrive get model,status\n\n# Outils tiers recommandés:\n# - CrystalDiskInfo: Santé S.M.A.R.T, température\n# - Samsung Magician: Samsung SSD\n# - WD Dashboard: Western Digital\n# - Crucial Storage Executive: Crucial SSD"
            },
            {
                "title": "Optimiser SSD (Windows)",
                "code": "# Vérifier TRIM activé (essentiel SSD)\nfsutil behavior query DisableDeleteNotify\n# NTFS DisableDeleteNotify = 0 → TRIM activé ✅\n\n# Activer TRIM si désactivé\nfsutil behavior set DisableDeleteNotify 0\n\n# Désactiver défragmentation SSD (Windows le fait auto)\nschtasks /Change /TN \"\\Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /DISABLE\n\n# Désactiver Superfetch (SSD uniquement)\nsc config SysMain start= disabled"
            },
            {
                "title": "Cloner Disque (HDD → SSD Migration)",
                "bullets": [
                    "Outils de clonage gratuits:",
                    "• Macrium Reflect Free - Excellent",
                    "• Clonezilla - Open source, bootable",
                    "• Samsung Data Migration - Samsung SSD",
                    "• Acronis True Image WD - WD SSD",
                    "",
                    "Étapes:",
                    "1. Brancher nouveau SSD (USB ou SATA)",
                    "2. Lancer logiciel de clonage",
                    "3. Source: HDD actuel, Destination: SSD",
                    "4. Démarrer clonage (30min - 3h)",
                    "5. Éteindre PC, installer SSD à la place du HDD",
                    "6. Booter, vérifier fonctionnement",
                    "7. Formater ancien HDD comme stockage secondaire"
                ]
            },
            {
                "warning": "⚠️ NE défragmentez JAMAIS un SSD! Ça use les cellules flash inutilement. Windows désactive défrag auto sur SSD."
            },
            {
                "info": "💡ème gen AMD): 500-550 MB/s max. Utilisez NVMe pour vitesses >1000 MB/s."
            }
        ]
    },

    "hw_troubleshoot": {
        "title": "🔧 Dépannage Matériel PC",
        "sections": [
            {
                "title": "PC Ne Démarre Pas - Checklist",
                "bullets": [
                    "1. Vérifier alimentation branchée, interrupteur PSU ON",
                    "2. Tester prise murale avec autre appareil",
                    "3. Vérifier câble alimentation PSU",
                    "4. Appuyer bouton power 10 secondes (décharge résiduelle)",
                    "5. Débrancher TOUS périphériques sauf clavier",
                    "6. Retirer 1 barette RAM, tester (puis inverser)",
                    "7. Vérifier connexions: 24-pin MB, 8-pin CPU, 6/8-pin GPU",
                    "8. Retirer GPU, booter sur GPU intégré (si existe)",
                    "9. Reset CMOS (retirer pile 30 sec ou jumper clear)",
                    "10. Si rien: PSU mort ou carte mère HS"
                ]
            },
            {
                "title": "Écrans Bleus (BSOD) Fréquents",
                "bullets": [
                    "Causes courantes:",
                    "• Drivers obsolètes/corrompus",
                    "• RAM défectueuse ou OC instable",
                    "• Disque dur défaillant",
                    "• Surchauffe CPU/GPU",
                    "• Malware",
                    "",
                    "Solutions:",
                    "1. Noter code erreur STOP (ex: IRQL_NOT_LESS_OR_EQUAL)",
                    "2. Analyser dump: BlueScreenView (Nirsoft)",
                    "3. Tester RAM: MemTest86 (8+ passes)",
                    "4. Vérifier températures: HWiNFO64",
                    "5. Mettre à jour tous drivers (GPU, chipset)",
                    "6. SFC + DISM: sfc /scannow + DISM /RestoreHealth",
                    "7. Désactiver OC RAM/CPU temporairement"
                ]
            },
            {
                "title": "Surchauffe PC",
                "code": "# Vérifier températures\n# HWiNFO64, Core Temp, MSI Afterburner\n\n# Températures critiques:\n# CPU: >95°C → Throttling, arrêt\n# GPU: >95°C → Throttling\n# Disque: >60°C → Ralentissement, risque données\n\n# Solutions:\n# 1. Nettoyer poussière (bombe air comprimé)\n# 2. Renouveler pâte thermique CPU (tous les 2-3 ans)\n# 3. Améliorer flux d'air (ventilateurs intake/exhaust)\n# 4. Undervolt CPU/GPU (réduire voltage, moins chaleur)\n# 5. Watercooling AIO (CPU seulement ou custom loop)"
            },
            {
                "title": "Disque Non Détecté",
                "bullets": [
                    "1. Vérifier câble SATA/M.2 bien branché",
                    "2. Tester autre port SATA carte mère",
                    "3. Tester câble SATA avec autre disque",
                    "4. BIOS: Vérifier si disque listé",
                    "5. Windows: Gestion des disques (diskmgmt.msc)",
                    "6. Si 'Non initialisé': Clic droit → Initialiser",
                    "7. Si 'Non alloué': Clic droit → Nouveau volume simple",
                    "8. M.2: Vérifier slot M.2 supporte NVMe (certains = SATA only)"
                ]
            },
            {
                "title": "Bips au Démarrage (Beep Codes)",
                "content": "Les bips au démarrage indiquent erreurs matérielles (code varie selon BIOS).\n\nAMI BIOS:\n• 1 bip court: OK (POST réussi)\n• 1 bip long: Problème RAM\n• 2 bips courts: Erreur parité RAM\n• 3 bips courts: Échec test mémoire\n• 5 bips courts: Erreur processeur\n• 1 long + 3 courts: Erreur carte graphique\n\nAward BIOS:\n• 1 bip long + 2 courts: Erreur vidéo\n• Bips continus: RAM mal insérée\n\nSolution: Réinsérer composant concerné ou tester avec composant fonctionnel."
            },
            {
                "info": "💡 Avant de démonter PC: Prenez photos des câbles/positions composants. Facilite remontage!"
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3L: LOGICIELS (5 guides)
    # =========================================================================

    "sw_essential": {
        "title": "⭐ Logiciels Essentiels Post-Install Windows",
        "sections": [
            {
                "title": "Navigateurs Web",
                "bullets": [
                    "🌐 Google Chrome - Le plus populaire, synchronisation Google",
                    "🦊 Mozilla Firefox - Open source, privacy-focused",
                    "🦁 Brave - Bloque pubs nativement, basé Chromium",
                    "🎭 Opera GX - Gaming, RAM Limiter, CPU Limiter",
                    "🌊 Microsoft Edge - Chromium, intégré Windows 11"
                ]
            },
            {
                "title": "Sécurité",
                "bullets": [
                    "🛡️ Malwarebytes - Anti-malware gratuit excellent",
                    "🔥 Windows Defender - Antivirus intégré, suffisant",
                    "🔒 Bitwarden - Gestionnaire mots de passe open source",
                    "🌐 uBlock Origin - Bloqueur pubs (extension navigateur)"
                ]
            },
            {
                "title": "Utilitaires Système",
                "bullets": [
                    "📦 7-Zip - Archiveur gratuit (.zip, .rar, .7z)",
                    "🔍 Everything - Recherche fichiers instantanée",
                    "📋 Notepad++ - Éditeur texte avancé",
                    "🖼️ IrfanView - Visionneuse images rapide",
                    "🎬 VLC Media Player - Lecteur vidéo universel",
                    "📊 WinDirStat - Visualiser espace disque",
                    "🧹 BleachBit - Nettoyeur système (alt CCleaner)",
                    "💾 CrystalDiskInfo - Santé SSD/HDD"
                ]
            },
            {
                "title": "Communication",
                "bullets": [
                    "💬 Discord - Communication gaming/communautés",
                    "📞 Zoom - Visioconférence pro",
                    "💼 Microsoft Teams - Collaboration entreprise",
                    "📧 Thunderbird - Client email open source"
                ]
            },
            {
                "title": "Installation Rapide via Winget",
                "code": "# PowerShell - Installer tous essentiels\nwinget install Google.Chrome\nwinget install Mozilla.Firefox\nwinget install 7zip.7zip\nwinget install voidtools.Everything\nwinget install Notepad++.Notepad++\nwinget install VideoLAN.VLC\nwinget install Malwarebytes.Malwarebytes\nwinget install Discord.Discord\nwinget install Adobe.Acrobat.Reader.64-bit"
            },
            {
                "info": "💡 NiTriTe Master Install permet d'installer 50+ programmes essentiels en un clic via packs prédéfinis!"
            }
        ]
    },

    "sw_productivity": {
        "title": "📊 Logiciels de Productivité",
        "sections": [
            {
                "title": "Suites Bureautiques",
                "bullets": [
                    "📄 Microsoft Office (Payant):",
                    "• Word, Excel, PowerPoint, Outlook",
                    "• Standard entreprise",
                    "• Microsoft 365: €7/mois, 1TB OneDrive",
                    "",
                    "📄 LibreOffice (Gratuit):",
                    "• Writer, Calc, Impress (équivalents Office)",
                    "• Open source, compatible fichiers Office",
                    "• Parfait pour usage personnel",
                    "",
                    "☁️ Google Workspace (Gratuit/Payant):",
                    "• Docs, Sheets, Slides (en ligne)",
                    "• Collaboration temps réel",
                    "• 15GB stockage gratuit"
                ]
            },
            {
                "title": "Prise de Notes",
                "bullets": [
                    "📝 Notion - All-in-one workspace, bases de données",
                    "📓 Obsidian - Markdown, graphe connaissances",
                    "🐘 Evernote - Classique, synchronisation cloud",
                    "🌲 Joplin - Open source, chiffrement E2E",
                    "✏️ OneNote - Microsoft, gratuit, stylet support"
                ]
            },
            {
                "title": "Gestion Projets / Tâches",
                "bullets": [
                    "✅ Todoist - To-do lists, rappels, priorités",
                    "🎯 Trello - Kanban boards, collaboration",
                    "⚡ Asana - Gestion projets pro",
                    "🔔 TickTick - Todo + Pomodoro timer",
                    "📅 Microsoft To Do - Simple, intégré Outlook"
                ]
            },
            {
                "title": "PDF",
                "bullets": [
                    "📕 Adobe Acrobat Reader - Lecteur standard",
                    "📘 Foxit Reader - Alternatif léger",
                    "📗 Sumatra PDF - Ultra-léger, rapide",
                    "🔧 PDFtk - Fusionner/Séparer PDF (CLI)",
                    "✏️ PDF-XChange Editor - Annoter PDF gratuit"
                ]
            },
            {
                "title": "Capture d'Écran / Enregistrement",
                "bullets": [
                    "📸 ShareX - Capture, annotation, upload auto (gratuit)",
                    "🎬 OBS Studio - Enregistrement écran, streaming",
                    "🎥 ScreenToGif - GIFs animés faciles",
                    "⚡ Windows Snipping Tool - Intégré (Win+Shift+S)",
                    "🖼️ Greenshot - Capture + annotation simple"
                ]
            },
            {
                "code": "# Installer outils productivité\nwinget install Notion.Notion\nwinget install Obsidian.Obsidian\nwinget install LibreOffice.LibreOffice\nwinget install ShareX.ShareX\nwinget install OBSProject.OBSStudio\nwinget install Adobe.Acrobat.Reader.64-bit"
            }
        ]
    },

    "sw_multimedia": {
        "title": "🎬 Logiciels Multimédia - Création",
        "sections": [
            {
                "title": "Montage Vidéo",
                "bullets": [
                    "🎞️ DaVinci Resolve - Pro gratuit, color grading",
                    "🎬 Adobe Premiere Pro - Standard industrie (payant)",
                    "✂️ Shotcut - Open source, simple",
                    "🎥 Kdenlive - Open source, Linux/Windows",
                    "⚡ VEGAS Pro - Alternatif Adobe (payant)",
                    "🆓 Capcut - Gratuit, TikTok/Reels"
                ]
            },
            {
                "title": "Retouche Photo",
                "bullets": [
                    "🎨 GIMP - Photoshop gratuit open source",
                    "🖌️ Adobe Photoshop - Pro (payant)",
                    "🎭 Paint.NET - Simple, Windows uniquement",
                    "📷 RawTherapee - RAW processing gratuit",
                    "✨ Photopea - En ligne, gratuit (photopea.com)"
                ]
            },
            {
                "title": "Graphisme Vectoriel",
                "bullets": [
                    "🎨 Inkscape - Illustrator gratuit open source",
                    "✏️ Adobe Illustrator - Pro (payant)",
                    "🎭 Affinity Designer - Alternatif Illustrator (achat unique)",
                    "🖍️ Figma - UI/UX design (gratuit/payant)"
                ]
            },
            {
                "title": "Audio / Musique",
                "bullets": [
                    "🎵 Audacity - Éditeur audio gratuit",
                    "🎹 FL Studio - Production musicale (payant)",
                    "🎚️ Ableton Live - DAW pro (payant)",
                    "🎧 Reaper - DAW abordable ($60)",
                    "🔊 Ocenaudio - Simple, gratuit",
                    "🎼 MuseScore - Partitions musicales"
                ]
            },
            {
                "title": "3D / Animation",
                "bullets": [
                    "🎭 Blender - 3D complet gratuit (modeling, animation, VFX)",
                    "🏗️ SketchUp - 3D architecture (gratuit/pro)",
                    "🎬 Cinema 4D - Motion graphics pro (payant)",
                    "🔮 Autodesk Maya - VFX/animation (payant)",
                    "🎨 ZBrush - Sculpture digitale (payant)"
                ]
            },
            {
                "code": "# Installer outils création\nwinget install GIMP.GIMP\nwinget install Inkscape.Inkscape\nwinget install Audacity.Audacity\nwinget install BlenderFoundation.Blender\nwinget install OBSProject.OBSStudio\nwinget install Shotcut.Shotcut"
            },
            {
                "info": "💡 DaVinci Resolve (gratuit) est suffisant pour 95% des créateurs. Version Studio ($295) ajoute features pros."
            }
        ]
    },

    "sw_development": {
        "title": "💻 Logiciels de Développement",
        "sections": [
            {
                "title": "Éditeurs de Code / IDE",
                "bullets": [
                    "⚡ Visual Studio Code - Le meilleur gratuit, extensions infinies",
                    "🧠 JetBrains IntelliJ IDEA - Java/Kotlin pro (payant)",
                    "🐍 PyCharm - Python (gratuit Community / payant Pro)",
                    "🌊 WebStorm - JavaScript/TypeScript (payant)",
                    "⚛️ Atom - Open source, léger (discontinué → VSCode)",
                    "📝 Sublime Text - Rapide, payant ($99)",
                    "🎯 Vim/Neovim - Terminal, courbe apprentissage"
                ]
            },
            {
                "title": "Gestion Versions (Git)",
                "bullets": [
                    "📦 Git - CLI essentiel",
                    "🐙 GitHub Desktop - Interface graphique GitHub",
                    "🦊 GitKraken - Git GUI avancé (gratuit/payant)",
                    "🌳 SourceTree - Git GUI Atlassian (gratuit)",
                    "💎 Git Extensions - Windows Git GUI"
                ]
            },
            {
                "title": "Langages / Runtimes",
                "bullets": [
                    "🐍 Python 3.12 - Scripting, data science, IA",
                    "☕ Node.js - JavaScript backend",
                    "☕ OpenJDK / Oracle JDK - Java",
                    "💎 Ruby - Scripting, Rails",
                    "🦀 Rust - Systèmes, performance",
                    "🔷 .NET SDK - C#, F#",
                    "🐘 PHP - Web backend"
                ]
            },
            {
                "title": "Bases de Données",
                "bullets": [
                    "🐬 MySQL - SQL populaire",
                    "🐘 PostgreSQL - SQL avancé, open source",
                    "📊 Microsoft SQL Server - Enterprise",
                    "🍃 MongoDB - NoSQL document",
                    "🔥 Redis - Cache in-memory",
                    "🗄️ SQLite - Embedded, zéro config"
                ]
            },
            {
                "title": "API Testing / DevOps",
                "bullets": [
                    "📬 Postman - API testing, collections",
                    "⚡ Insomnia - API client simple",
                    "🐳 Docker Desktop - Containers",
                    "☸️ Kubernetes - Orchestration containers",
                    "🔧 cURL - CLI HTTP",
                    "🌊 Wireshark - Network analyzer"
                ]
            },
            {
                "code": "# Stack développement complet\nwinget install Microsoft.VisualStudioCode\nwinget install Git.Git\nwinget install GitHub.GitHubDesktop\nwinget install Python.Python.3.12\nwinget install OpenJS.NodeJS.LTS\nwinget install Postman.Postman\nwinget install Docker.DockerDesktop\nwinget install Oracle.JavaRuntimeEnvironment"
            },
            {
                "info": "💡 VSCode + extensions (Prettier, ESLint, GitLens, Python) = IDE complet gratuit pour 90% des devs."
            }
        ]
    },

    "sw_security": {
        "title": "🔒 Sécurité & Antivirus - Logiciels",
        "sections": [
            {
                "title": "Antivirus Gratuits Fiables",
                "bullets": [
                    "🛡️ Windows Defender - Intégré, excellent (recommandé)",
                    "🦠 Malwarebytes Free - Scanner malware ponctuel",
                    "🟢 Avast Free - Features extras (VPN, firewall)",
                    "🔵 AVG Free - Similaire Avast (même société)",
                    "🔴 Kaspersky Security Cloud Free - Protection forte",
                    "⚠️ Évitez: McAfee, Norton (bloatware, ralentissent PC)"
                ]
            },
            {
                "title": "Antivirus Payants (Si Besoin Pro)",
                "bullets": [
                    "💰 Bitdefender Total Security - Meilleur détection 2024",
                    "💰 Kaspersky Total Security - Excellent, controversé (Russie)",
                    "💰 ESET NOD32 - Léger, efficace",
                    "💰 Malwarebytes Premium - Protection temps réel",
                    "💰 Norton 360 Deluxe - VPN + Password Manager inclus"
                ]
            },
            {
                "title": "Scanners Anti-Malware Complémentaires",
                "bullets": [
                    "🔍 AdwCleaner - Adwares/Toolbars (gratuit Malwarebytes)",
                    "⚔️ HitmanPro - Scan cloud multi-moteurs (30j trial)",
                    "🎯 ESET Online Scanner - Scan ponctuel gratuit",
                    "🛠️ Kaspersky Virus Removal Tool - Gratuit",
                    "🔧 ComboFix - Avancé, utiliser avec précaution",
                    "🦠 RogueKiller - Anti-rootkit, anti-malware"
                ]
            },
            {
                "title": "Gestionnaires Mots de Passe",
                "bullets": [
                    "🔐 Bitwarden - Open source, gratuit, excellent",
                    "🔑 1Password - Pro, interface élégante (payant)",
                    "🔒 LastPass - Gratuit limité, payant complet",
                    "🗝️ KeePass - Local, open source, pas de cloud",
                    "🌐 Dashlane - Premium, VPN inclus (payant)"
                ]
            },
            {
                "title": "VPN (Vie Privée)",
                "bullets": [
                    "🔐 ProtonVPN - Free 3 pays, payant illimité",
                    "🌐 NordVPN - Rapide, gros réseau (payant)",
                    "🛡️ Mullvad - Privacy absolu, €5/mois",
                    "🦈 Surfshark - Connexions illimitées (payant)",
                    "⚡ Windscribe - 10GB/mois gratuit"
                ]
            },
            {
                "title": "Outils Sécurité Avancés",
                "bullets": [
                    "🔍 Process Explorer - Sysinternals, monitor processus",
                    "🚀 Autoruns - Sysinternals, programmes démarrage",
                    "🌐 Wireshark - Analyse trafic réseau",
                    "🔥 GlassWire - Firewall + monitor réseau visuel",
                    "🛡️ VeraCrypt - Chiffrement disques/partitions"
                ]
            },
            {
                "code": "# Installer suite sécurité\nwinget install Malwarebytes.Malwarebytes\nwinget install Bitwarden.Bitwarden\nwinget install ProtonTechnologies.ProtonVPN\nwinget install Microsoft.Sysinternals.Autoruns\nwinget install WiresharkFoundation.Wireshark"
            },
            {
                "warning": "⚠️ N'installez JAMAIS 2 antivirus en même temps (sauf Windows Defender + Malwarebytes). Ils se conflictent et ralentissent PC."
            },
            {
                "info": "💡 Windows Defender + Malwarebytes Free (scans ponctuels) + uBlock Origin (bloqueur pubs) = Protection complète gratuite."
            }
        ]
    },

    # =========================================================================
    # PRIORITÉ 3I: macOS (6 guides)
    # =========================================================================

    "macos_intro": {
        "title": "🍎 Introduction à macOS",
        "sections": [
            {
                "title": "macOS - Système d'Apple",
                "content": "macOS est le système d'exploitation d'Apple pour Mac (iMac, MacBook, Mac Mini, Mac Studio, Mac Pro). Basé sur Unix (BSD), réputé pour design élégant, stabilité, et intégration écosystème Apple."
            },
            {
                "title": "Versions macOS Récentes",
                "bullets": [
                    "🍎 macOS Sonoma (14) - 2023, widgets bureau",
                    "🏔️ macOS Ventura (13) - 2022, Stage Manager",
                    "🌄 macOS Monterey (12) - 2021, Universal Control",
                    "🏔️ macOS Big Sur (11) - 2020, design iOS-like",
                    "🌃 macOS Catalina (10.15) - 2019, dernier support 32-bit",
                    "🏜️ macOS Mojave (10.14) - 2018, Dark Mode",
                    "🏔️ macOS High Sierra (10.13) - 2017, APFS"
                ]
            },
            {
                "title": "Apple Silicon vs Intel",
                "content": "Transition Apple Silicon (2020+):\n\n🍎 Apple Silicon (M1/M2/M3):\n• CPU ARM custom Apple\n• Performances excellentes, batterie incroyable\n• Pas de Boot Camp Windows (VM seulement)\n• Apps Intel via Rosetta 2 (traduction)\n\n💻 Intel Mac (pré-2020):\n• CPU Intel x86\n• Boot Camp Windows natif\n• Chauffe plus, batterie moins bonne\n• Support terminera progressivement"
            },
            {
                "title": "Avantages macOS",
                "bullets": [
                    "✅ Interface élégante, cohérente",
                    "✅ Stabilité, pas de virus (quasi)",
                    "✅ Intégration iPhone/iPad (Handoff, AirDrop, Continuity)",
                    "✅ Terminal Unix puissant (Bash/Zsh)",
                    "✅ Optimisé matériel Apple (batterie)",
                    "✅ Final Cut Pro, Logic Pro (exclusifs)",
                    "❌ Prix élevé",
                    "❌ Moins de jeux",
                    "❌ Matériel non upgradable (soudé)"
                ]
            },
            {
                "info": "💡 MacBook Air M2/M3 (2023/2024) = Excellent laptop polyvalent, 15-20h batterie, silencieux (pas de ventilateur)."
            }
        ]
    },

    "macos_install": {
        "title": "💿 Installation & Configuration macOS",
        "sections": [
            {
                "title": "Clean Install macOS (Réinstallation Propre)",
                "bullets": [
                    "1. Sauvegarder données (Time Machine ou externe)",
                    "2. Redémarrer Mac",
                    "3. Cmd + R au démarrage (Recovery Mode)",
                    "4. Utilitaire de disque → Effacer disque (APFS)",
                    "5. Réinstaller macOS",
                    "6. Sélectionner disque destination",
                    "7. Téléchargement macOS depuis internet (30min-2h)",
                    "8. Installation (30-60min)",
                    "9. Configuration initiale (Apple ID, iCloud, etc.)"
                ]
            },
            {
                "title": "Mise à Jour vers Nouvelle Version",
                "bullets": [
                    "1. Vérifier compatibilité Mac (apple.com/macos)",
                    "2. Sauvegarder via Time Machine",
                    "3. Préférences Système → Mise à jour logiciels",
                    "4. Télécharger macOS [Version]",
                    "5. Installer maintenant",
                    "6. Redémarrage automatique (30-60min)",
                    "7. Tester apps critiques (certaines incompatibles)"
                ]
            },
            {
                "title": "Migration Assistant - Transférer Données",
                "bullets": [
                    "Transfer données ancien Mac → nouveau Mac:",
                    "1. Connecter Macs sur même WiFi ou câble Thunderbolt",
                    "2. Nouveau Mac: Assistant migration (setup initial)",
                    "3. Ancien Mac: Utilitaires → Assistant migration",
                    "4. Sélectionner source (ancien Mac)",
                    "5. Choisir données à transférer",
                    "6. Attendre transfert (1-8h selon quantité)",
                    "7. Nouveau Mac identique à ancien"
                ]
            },
            {
                "title": "Bootcamp (Intel Mac Seulement)",
                "content": "Boot Camp permet installer Windows nativement sur Mac Intel.\n\n⚠️ Impossible sur Apple Silicon (M1/M2/M3)!\n\nÉtapes:\n1. Applications → Utilitaires → Assistant Boot Camp\n2. Télécharger ISO Windows 10/11\n3. Partitionner disque (min 64GB Windows)\n4. Installer Windows\n5. Redémarrer: Maintenir Option pour choisir OS"
            },
            {
                "info": "💡 Sur Apple Silicon: Utilisez Parallels Desktop ou VMware Fusion pour virtualiser Windows ARM (pas x86 natif)."
            }
        ]
    },

    "macos_terminal": {
        "title": "⚡ Terminal macOS - Commandes de Base",
        "sections": [
            {
                "title": "Terminal - Shell Unix",
                "content": "Le Terminal macOS donne accès au shell Unix (Zsh par défaut depuis Catalina). Puissant pour automation, development, administration système."
            },
            {
                "title": "Commandes Essentielles",
                "code": "# Navigation\npwd                  # Répertoire actuel\nls                   # Lister fichiers\nls -la               # Détaillé + cachés\ncd /chemin           # Changer répertoire\ncd ~                 # Dossier utilisateur\ncd ..                # Remonter\n\n# Fichiers\ntouch fichier.txt    # Créer fichier vide\ncat fichier.txt      # Afficher contenu\nnano fichier.txt     # Éditer (simple)\nvim fichier.txt      # Éditer (avancé)\ncp source dest       # Copier\nmv source dest       # Déplacer/Renommer\nrm fichier.txt       # Supprimer\nmkdir dossier        # Créer dossier\nrmdir dossier        # Supprimer dossier vide\nrm -rf dossier       # Supprimer dossier + contenu\n\n# Système\ntop                  # Processus CPU\nps aux               # Tous processus\nkill PID             # Tuer processus\nsudo command         # Exécuter en admin\ndf -h                # Espace disque\ndu -sh dossier       # Taille dossier\nwhich command        # Chemin commande"
            },
            {
                "title": "Homebrew - Gestionnaire Paquets",
                "content": "Homebrew = apt-get/winget pour macOS. Installe logiciels ligne de commande facilement."
            },
            {
                "code": "# Installer Homebrew\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"\n\n# Utilisation\nbrew install wget         # Installer package\nbrew install git\nbrew install python@3.12\n\n# Rechercher\nbrew search firefox\n\n# Mettre à jour\nbrew update              # MAJ Homebrew\nbrew upgrade             # MAJ tous packages\nbrew upgrade wget        # MAJ package spécifique\n\n# Désinstaller\nbrew uninstall wget\n\n# Lister installés\nbrew list\n\n# Apps graphiques (Cask)\nbrew install --cask google-chrome\nbrew install --cask visual-studio-code\nbrew install --cask vlc"
            },
            {
                "title": "Raccourcis Terminal",
                "bullets": [
                    "Ctrl + C - Interrompre commande",
                    "Ctrl + D - Quitter shell / EOF",
                    "Ctrl + L - Effacer écran (ou 'clear')",
                    "Ctrl + A - Début de ligne",
                    "Ctrl + E - Fin de ligne",
                    "Ctrl + U - Effacer jusqu'au début",
                    "Ctrl + K - Effacer jusqu'à la fin",
                    "Tab - Auto-complétion",
                    "↑/↓ - Historique commandes",
                    "Cmd + T - Nouvel onglet",
                    "Cmd + W - Fermer onglet"
                ]
            },
            {
                "info": "💡 Oh My Zsh améliore Zsh avec thèmes et plugins. Installation: sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\""
            }
        ]
    },

    "macos_homebrew": {
        "title": "🍺 Homebrew - Gestionnaire de Paquets",
        "sections": [
            {
                "title": "Homebrew - Essentiel pour Dev macOS",
                "content": "Homebrew est LE gestionnaire de paquets macOS. Installe outils CLI, langages, et apps graphiques. Indispensable pour développeurs."
            },
            {
                "title": "Installation Homebrew",
                "code": "# Terminal - Installer Homebrew\n/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"\n\n# Suivre instructions post-install (ajouter au PATH)\n# Pour Apple Silicon:\necho 'eval \"$(/opt/homebrew/bin/brew shellenv)\"' >> ~/.zprofile\neval \"$(/opt/homebrew/bin/brew shellenv)\"\n\n# Vérifier installation\nbrew --version\nbrew doctor  # Diagnostiquer problèmes"
            },
            {
                "title": "Commandes Homebrew Essentielles",
                "code": "# Rechercher package\nbrew search python\nbrew search /^git$/  # Recherche exacte\n\n# Installer\nbrew install wget\nbrew install node\nbrew install python@3.12\n\n# Infos package\nbrew info wget\n\n# Lister installés\nbrew list\n\n# Mettre à jour\nbrew update              # MAJ Homebrew lui-même\nbrew outdated            # Packages à MAJ\nbrew upgrade             # MAJ tout\nbrew upgrade wget        # MAJ spécifique\n\n# Désinstaller\nbrew uninstall wget\nbrew autoremove          # Supprimer dépendances inutiles\n\n# Nettoyer cache\nbrew cleanup\nbrew cleanup -s  # Libérer espace max"
            },
            {
                "title": "Homebrew Cask - Applications Graphiques",
                "code": "# Installer apps graphiques\nbrew install --cask google-chrome\nbrew install --cask visual-studio-code\nbrew install --cask vlc\nbrew install --cask discord\nbrew install --cask notion\nbrew install --cask spotify\nbrew install --cask docker\nbrew install --cask iterm2  # Terminal amélioré\n\n# Rechercher casks\nbrew search --cask firefox\n\n# Lister casks installés\nbrew list --cask\n\n# MAJ casks\nbrew upgrade --cask"
            },
            {
                "title": "Packages Utiles Développeurs",
                "code": "# Outils essentiels\nbrew install git\nbrew install wget\nbrew install curl\nbrew install htop        # top amélioré\nbrew install tree        # Arbre fichiers\nbrew install neofetch    # Infos système\n\n# Langages\nbrew install python@3.12\nbrew install node\nbrew install go\nbrew install rust\nbrew install openjdk\n\n# Bases de données\nbrew install postgresql@15\nbrew install mysql\nbrew install redis\nbrew install mongodb-community\n\n# DevOps\nbrew install docker\nbrew install kubectl\nbrew install terraform"
            },
            {
                "title": "Brewfile - Sauvegar Installation",
                "code": "# Exporter packages installés\nbrew bundle dump --file=~/Brewfile\n\n# Contenu Brewfile (exemple)\n# tap \"homebrew/cask\"\n# brew \"git\"\n# brew \"node\"\n# cask \"google-chrome\"\n# cask \"visual-studio-code\"\n\n# Installer depuis Brewfile (nouveau Mac)\nbrew bundle --file=~/Brewfile\n\n# Cleanup après Brewfile\nbrew bundle cleanup --file=~/Brewfile"
            },
            {
                "info": "💡 Homebrew installe dans /usr/local (Intel) ou /opt/homebrew (Apple Silicon). Ne nécessite jamais sudo (sauf install initial)."
            }
        ]
    },

    "macos_optimize": {
        "title": "⚡ Optimisation macOS - Performance",
        "sections": [
            {
                "title": "Désactiver Animations",
                "code": "# Terminal - Désactiver animations fenêtres\ndefaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false\n\n# Désactiver ouverture apps\ndefaults write NSGlobalDomain NSWindowResizeTime -float 0.001\n\n# Dock apparition instantanée\ndefaults write com.apple.dock autohide-delay -float 0\ndefaults write com.apple.dock autohide-time-modifier -float 0\n\n# Mission Control instantané\ndefaults write com.apple.dock expose-animation-duration -float 0.1\n\n# Relancer Dock\nkillall Dock\n\n# Restaurer (supprimer préférences)\ndefaults delete com.apple.dock"
            },
            {
                "title": "Libérer Espace Disque",
                "bullets": [
                    "1. Stockage: Préférences Système → Stockage → Gérer",
                    "2. Vider corbeille + Téléchargements",
                    "3. Désinstaller apps inutiles",
                    "4. Vider caches: ~/Library/Caches (attention!)",
                    "5. Time Machine snapshots locaux: sudo tmutil listlocalsnapshots / → deletelocalsnapshots",
                    "6. Outils tiers: DaisyDisk, OmniDiskSweeper"
                ]
            },
            {
                "title": "Optimiser RAM",
                "code": "# Voir utilisation RAM\ntop -l 1 | head -n 10\nvm_stat\n\n# Purger RAM (force caches)\nsudo purge\n\n# Désactiver apps en arrière-plan\n# Préférences Système → Général → Autoriser en arrière-plan\n\n# Moniteur activité\nopen -a \"Activity Monitor\""
            },
            {
                "title": "Désactiver Spotlight Indexation",
                "code": "# Désactiver Spotlight (gros gain CPU/batterie)\nsudo mdutil -a -i off\n\n# Réactiver\nsudo mdutil -a -i on\n\n# Exclure dossiers de Spotlight\n# Préférences Système → Spotlight → Confidentialité\n# Ajouter dossiers à exclure"
            },
            {
                "title": "Maintenance Système",
                "code": "# Vérifier/Réparer disque\nsudo diskutil verifyVolume /\nsudo diskutil repairVolume /\n\n# Permissions (ancien macOS)\nsudo diskutil repairPermissions /\n\n# Reconstruire Spotlight\nsudo mdutil -E /\n\n# Reset SMC (Intel Mac - problèmes batterie/ventilateur)\n# Éteindre → Shift+Ctrl+Option (gauche) + Power 10 sec\n\n# Reset NVRAM\n# Redémarrer → Cmd+Option+P+R jusqu'au 2e bong"
            },
            {
                "title": "Apps Optimisation Recommandées",
                "bullets": [
                    "🧹 CleanMyMac X - Nettoyage complet (payant)",
                    "💿 DaisyDisk - Visualiser espace disque",
                    "📊 iStat Menus - Monitoring système (payant)",
                    "🔋 AlDente - Limiter charge batterie (gratuit/pro)",
                    "⚡ TG Pro - Contrôle ventilateurs/température",
                    "🗑️ AppCleaner - Désinstallation complète (gratuit)"
                ]
            },
            {
                "info": "💡 macOS gère très bien la RAM. Pas besoin de 'nettoyeurs RAM'. Laisser macOS gérer = meilleur perfs."
            }
        ]
    },

    "macos_troubleshoot": {
        "title": "🔧 Dépannage macOS - Problèmes Courants",
        "sections": [
            {
                "title": "Mac Lent - Solutions",
                "bullets": [
                    "1. Moniteur activité: Apps CPU/RAM gourmandes?",
                    "2. Redémarrer (simple mais efficace!)",
                    "3. Vérifier espace disque (<10GB = lent)",
                    "4. Désactiver programmes démarrage: Préfs Sys → Utilisateurs",
                    "5. Réinitialiser SMC (Intel) ou cycle marche/arrêt (Apple Silicon)",
                    "6. Réinitialiser NVRAM: Cmd+Option+P+R au boot",
                    "7. Mode sans échec: Maintenir Shift au démarrage",
                    "8. Vérifier mises à jour macOS",
                    "9. Vérifier disque: Utilitaire de disque → S.O.S"
                ]
            },
            {
                "title": "Mac Ne Démarre Pas",
                "bullets": [
                    "Écran noir:",
                    "1. Vérifier charge batterie/alimentation",
                    "2. Forcer redémarrage: Power 10 secondes",
                    "3. Reset SMC (Intel)",
                    "4. Mode diagnostic: D au démarrage",
                    "",
                    "Bloqué sur pomme:",
                    "1. Mode sans échec: Shift au boot",
                    "2. Mode recovery: Cmd+R",
                    "3. Utilitaire disque → S.O.S sur Macintosh HD",
                    "4. Réinstaller macOS (conserve données)"
                ]
            },
            {
                "title": "Apps Plantent / Freeze",
                "code": "# Forcer quitter app\nCmd + Option + Esc  # GUI\n\n# Terminal\npkill -9 \"Nom de l'app\"\n# Ou\nkillall \"Nom de l'app\"\n\n# Supprimer préférences app (corruption)\nrm ~/Library/Preferences/com.app.plist\n\n# Supprimer caches app\nrm -rf ~/Library/Caches/com.app\n\n# Réinstaller app"
            },
            {
                "title": "Wifi/Bluetooth Problèmes",
                "bullets": [
                    "WiFi lent/déconnexions:",
                    "1. Désactiver/Réactiver WiFi",
                    "2. Supprimer réseau → Reconnecter",
                    "3. Renouveler bail DHCP: Avancé → TCP/IP → Renouveler",
                    "4. Supprimer préférences WiFi: sudo rm /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist",
                    "5. Reset SMC",
                    "",
                    "Bluetooth:",
                    "1. Désactiver/Réactiver Bluetooth",
                    "2. Oublier appareil → Ré-appairer",
                    "3. Reset Bluetooth: Shift+Option+clic icône BT → Debug → Reset module",
                    "4. Supprimer: sudo rm /Library/Preferences/com.apple.Bluetooth.plist"
                ]
            },
            {
                "title": "Modes Spéciaux macOS",
                "bullets": [
                    "Mode Recovery (Cmd+R): Utilitaire disque, réinstaller macOS",
                    "Mode sans échec (Shift): Démarre avec minimum extensions",
                    "Mode diagnostic (D): Test matériel Apple",
                    "Mode verbose (Cmd+V): Boot avec logs détaillés",
                    "Mode utilisateur unique (Cmd+S): Shell root",
                    "Mode Target (T): Mac devient disque externe Thunderbolt"
                ]
            },
            {
                "title": "Réinitialisation Complète (Factory Reset)",
                "bullets": [
                    "1. Sauvegarder données (Time Machine/externe)",
                    "2. Déconnexion iCloud: Préfs Sys → Apple ID → Se déconnecter",
                    "3. Déconnecter Messages/FaceTime",
                    "4. Désautoriser iTunes/Music: Compte → Autorisations → Tout",
                    "5. Redémarrer en Recovery: Cmd+R",
                    "6. Utilitaire de disque → Effacer Macintosh HD (APFS)",
                    "7. Réinstaller macOS",
                    "8. Configuration comme neuf"
                ]
            },
            {
                "warning": "⚠️ Reset SMC/NVRAM résout 80% problèmes hardware bizarres (batterie, ventilateur, son, écran). Essayez d'abord!"
            },
            {
                "info": "💡 Apple Diagnostics (D au boot) teste RAM, disque, batterie, capteurs. Code erreur → apple.com/support."
            }
        ]
    },

    # ============================================================
    # PHASE 3H - LINUX (35 GUIDES)
    # ============================================================

    "linux_intro": {
        "title": "🐧 Introduction à Linux",
        "sections": [
            {
                "title": "Qu'est-ce que Linux?",
                "content": "Linux est un système d'exploitation open-source basé sur Unix, créé par Linus Torvalds en 1991. Contrairement à Windows/macOS, Linux est GRATUIT, hautement personnalisable et existe en centaines de variantes appelées \"distributions\" (distros). Linux alimente 90% des serveurs web, tous les supercalculateurs, Android, et gagne en popularité sur desktop grâce à sa stabilité, sécurité et performance."
            },
            {
                "title": "Avantages de Linux (2024)",
                "bullets": [
                    "✅ 100% Gratuit - Aucun coût de licence (vs Windows €145+, macOS = Mac obligatoire)",
                    "✅ Open Source - Code source auditable, pas de télémétrie forcée",
                    "✅ Performance - Démarre en <10s, tourne sur PC de 2010+",
                    "✅ Sécurité - Moins de virus/malwares, permissions strictes",
                    "✅ Confidentialité - Pas de tracking Microsoft/Apple par défaut",
                    "✅ Personnalisation - Changez TOUT (interface, kernel, bootloader)",
                    "✅ Gaming - Proton/Steam Deck = 80%+ jeux Windows compatibles",
                    "✅ Terminal puissant - Automatisation facile avec bash/scripts",
                    "✅ Communauté - Forums actifs, wiki détaillés (Arch Wiki = bible)"
                ]
            },
            {
                "title": "Inconvénients à Connaître",
                "bullets": [
                    "❌ Courbe d'apprentissage - Terminal parfois requis",
                    "❌ Support logiciels - Adobe/Office 365 natif inexistant (alternatives: GIMP, LibreOffice)",
                    "❌ Drivers - Certains fabricants ignorent Linux (NVIDIA improving)",
                    "❌ Gaming - Pas 100% jeux (anti-cheat kernel souvent bloqués)",
                    "❌ Fragmentation - Trop de distros/choix peut être confus"
                ]
            },
            {
                "title": "Philosophie Linux - Tout est Fichier",
                "content": "Sur Linux, TOUT est traité comme un fichier: disques (/dev/sda), processus (/proc/1234), réseau (/sys/class/net). Cette uniformité permet des manipulations puissantes avec des commandes simples. Pas de Registre comme Windows - la config est dans des fichiers texte lisibles (/etc/*)."
            },
            {
                "title": "Composants Principaux",
                "bullets": [
                    "Kernel Linux - Cœur du système (gestion hardware/mémoire/processus)",
                    "GNU Coreutils - Commandes de base (ls, cp, mv, grep, etc.)",
                    "Shell - Interface commande (bash par défaut, zsh alternatif populaire)",
                    "Display Server - Affichage graphique (X11 legacy, Wayland moderne)",
                    "Desktop Environment - Interface complète (GNOME, KDE, XFCE, etc.)",
                    "Window Manager - Gestion fenêtres (i3, Sway pour utilisateurs avancés)",
                    "Package Manager - Installateur logiciels (apt, dnf, pacman selon distro)"
                ]
            },
            {
                "title": "Ligne de Commande - Pourquoi?",
                "content": "Le terminal Linux est PLUS RAPIDE que GUI pour beaucoup de tâches. Exemple: mettre à jour 200 paquets = 1 commande 'sudo apt update && sudo apt upgrade' vs cliquer 200× dans un store. Les commandes sont scriptables/automatisables. Une fois maîtrisé, vous ne voudrez plus revenir."
            },
            {
                "info": "💡 Débutant? Commencez par Ubuntu/Linux Mint (interface familière type Windows). Avancé? Arch Linux/Fedora pour contrôle total."
            },
            {
                "warning": "⚠️ Linux n'est PAS Windows: Ne pas chercher équivalents exacts (Paint.NET → GIMP). Adoptez la philosophie Linux = mieux."
            }
        ]
    },

    "linux_distros": {
        "title": "🌐 Distributions Linux Principales",
        "sections": [
            {
                "title": "Qu'est-ce qu'une Distribution?",
                "content": "Une distribution (distro) = Linux kernel + logiciels pré-installés + gestionnaire de paquets + philosophie. Il existe 600+ distros, mais 5-10 dominent. Choisir selon: facilité, stabilité, fraîcheur des paquets, communauté."
            },
            {
                "title": "Ubuntu (Debian-based) - Le Plus Populaire",
                "bullets": [
                    "🟠 Ubuntu 24.04 LTS (Long Term Support = 5 ans de mises à jour)",
                    "• Débutant-friendly: Installation graphique, store intégré",
                    "• Package manager: APT (30 000+ paquets)",
                    "• Desktop: GNOME par défaut (customisable)",
                    "• Support: Forums massifs, docs complètes",
                    "• Idéal pour: Débutants, bureautique, développement web",
                    "",
                    "Variantes populaires:",
                    "• Kubuntu (KDE Plasma - Windows-like)",
                    "• Xubuntu (XFCE - léger pour vieux PC)",
                    "• Ubuntu MATE (interface traditionnelle)",
                    "• Pop!_OS (System76 - optimisé gaming/dev)"
                ]
            },
            {
                "title": "Linux Mint - Ubuntu Sans les Défauts",
                "bullets": [
                    "🟢 Linux Mint 21.3 (basé Ubuntu LTS)",
                    "• Plus Windows-like qu'Ubuntu (menu type Start)",
                    "• Desktop: Cinnamon (élégant, performant)",
                    "• Pas de Snap (controversé sur Ubuntu) → AppImages/Flatpak",
                    "• Codecs multimédia pré-installés (MP3, DVD)",
                    "• Idéal pour: Migrants Windows, multimédia, stabilité"
                ]
            },
            {
                "title": "Fedora - Moderne & Innovant",
                "bullets": [
                    "🔵 Fedora 40 (Red Hat sponsorisé)",
                    "• Paquets très récents (kernel 6.8+, GNOME 46)",
                    "• Package manager: DNF (rpm-based)",
                    "• Technologies de pointe (Wayland par défaut depuis 2016)",
                    "• Cycle: Nouvelle version tous les 6 mois",
                    "• Idéal pour: Développeurs, testing nouvelles technos, workstations",
                    "",
                    "Variantes:",
                    "• Fedora Workstation (GNOME)",
                    "• Fedora KDE Spin",
                    "• Fedora Silverblue (immutable OS - avancé)"
                ]
            },
            {
                "title": "Arch Linux - DIY Absolu",
                "bullets": [
                    "⚙️ Arch Linux (rolling release = mises à jour continues)",
                    "• Installation manuelle via terminal (courbe d'apprentissage RAIDE)",
                    "• Package manager: Pacman + AUR (Arch User Repository = 80 000+ paquets)",
                    "• Philosophie: Simplicité, minimalisme, contrôle total",
                    "• Arch Wiki = Meilleure documentation Linux (utile même pour autres distros)",
                    "• Idéal pour: Experts Linux, customisation extrême",
                    "",
                    "Dérivés faciles:",
                    "• Manjaro (Arch avec installateur graphique)",
                    "• EndeavourOS (Arch quasi-vanilla mais installable)",
                    "• Garuda Linux (gaming-optimized Arch)"
                ]
            },
            {
                "title": "Debian - La Base Solide",
                "bullets": [
                    "🔴 Debian 12 \"Bookworm\"",
                    "• Mère d'Ubuntu/Mint/Pop!_OS",
                    "• Ultra-stable mais paquets anciens (Firefox 115 vs 123 ailleurs)",
                    "• Parfait pour serveurs (uptime de mois/années)",
                    "• 3 branches: Stable (serveurs), Testing (desktop acceptable), Unstable/Sid (experts)",
                    "• Idéal pour: Serveurs, utilisateurs avancés voulant stabilité"
                ]
            },
            {
                "title": "Autres Distros Notables",
                "bullets": [
                    "openSUSE Tumbleweed - Rolling release stable (YaST = outil config puissant)",
                    "Zorin OS - Clone Windows/macOS parfait (payant pour version Ultimate)",
                    "elementary OS - Clone macOS élégant (Pantheon desktop)",
                    "MX Linux - Léger, rapide, Debian-based",
                    "Kali Linux - Pentest/hacking éthique (ne PAS utiliser comme OS principal)",
                    "Gentoo - Compile TOUT from source (experts hardcore)"
                ]
            },
            {
                "title": "Comment Choisir?",
                "bullets": [
                    "Débutant ex-Windows → Linux Mint Cinnamon",
                    "Débutant ex-macOS → elementary OS / Ubuntu",
                    "Gaming → Pop!_OS / Garuda Linux / Nobara",
                    "Développement → Fedora Workstation / Ubuntu",
                    "Vieux PC (<4GB RAM) → Lubuntu / Xubuntu / antiX",
                    "Serveur → Debian Stable / Ubuntu Server / Rocky Linux",
                    "Expert contrôle total → Arch / Gentoo / Void",
                    "Vie privée max → Tails (OS amnésique) / Qubes OS"
                ]
            },
            {
                "info": "💡 Test avant install: Créez une clé USB bootable avec Ventoy/Rufus, testez 3-4 distros en live (sans installer). Voyez laquelle vous plaît."
            },
            {
                "warning": "⚠️ Évitez distros obscures (<1000 utilisateurs). Risque d'abandon, failles sécurité non patchées, pas de support communauté."
            }
        ]
    },

    "linux_install": {
        "title": "💿 Installation Linux - Guide Complet",
        "sections": [
            {
                "title": "Préparation - Avant d'Installer",
                "bullets": [
                    "1. Choisir la distro (voir guide linux_distros)",
                    "2. Vérifier compatibilité hardware (laptop récent = vérifier WiFi/GPU)",
                    "3. Sauvegarder données Windows si dual-boot",
                    "4. Désactiver Secure Boot si problèmes (BIOS/UEFI)",
                    "5. Désactiver Fast Boot Windows (Panneau config → Alimentation)",
                    "6. Libérer espace disque (50GB+ recommandé)"
                ]
            },
            {
                "title": "Créer Clé USB Bootable (Windows)",
                "code": "# Méthode 1: Rufus (Recommandé Windows)\n1. Télécharger ISO Ubuntu/Mint depuis site officiel\n2. Télécharger Rufus: https://rufus.ie\n3. Insérer clé USB 8GB+\n4. Rufus:\n   - Périphérique: Votre clé USB\n   - Sélection démarrage: DISK ou ISO (choisir ISO)\n   - Schéma partition: GPT (UEFI moderne) ou MBR (BIOS legacy)\n   - Système fichier: FAT32\n   - Démarrer → Attendre fin\n\n# Méthode 2: Ventoy (Multi-ISO sur 1 clé)\n1. Installer Ventoy sur clé USB\n2. Copier plusieurs fichiers ISO directement\n3. Au boot: Menu pour choisir distro"
            },
            {
                "title": "Modes d'Installation",
                "bullets": [
                    "Installation Complète (Efface Windows):",
                    "• Linux devient seul OS",
                    "• Le plus simple, aucun conflit",
                    "• ⚠️ Windows DÉFINITIVEMENT supprimé",
                    "",
                    "Dual-Boot (Linux + Windows):",
                    "• Garde Windows, ajoute Linux sur partition séparée",
                    "• Menu GRUB au démarrage pour choisir OS",
                    "• Partage possible de fichiers (NTFS accessible depuis Linux)",
                    "• ⚠️ Updates Windows peuvent casser GRUB (réparable)",
                    "",
                    "Machine Virtuelle (VirtualBox/VMware):",
                    "• Linux DANS Windows comme application",
                    "• Aucun risque pour Windows",
                    "• Performance réduite (30-50% selon config)",
                    "• Idéal pour tester avant vraie installation",
                    "",
                    "WSL (Windows Subsystem for Linux):",
                    "• Terminal Linux dans Windows 10/11",
                    "• Pas de vrai boot Linux, juste CLI",
                    "• Parfait pour développeurs (Docker, git, etc.)"
                ]
            },
            {
                "title": "Installation Ubuntu/Mint (Étapes Graphiques)",
                "bullets": [
                    "1. Brancher clé USB, redémarrer PC",
                    "2. Appuyer F12/F2/Del (selon fabricant) pour Boot Menu",
                    "3. Sélectionner clé USB UEFI",
                    "4. Choisir 'Try Ubuntu' (test sans installer) ou 'Install'",
                    "5. Langue: Français",
                    "6. Clavier: Français AZERTY",
                    "7. Updates: Télécharger updates pendant install ✓",
                    "8. Partitionnement:",
                    "   - Débutant: 'Effacer disque et installer' (SIMPLE)",
                    "   - Dual-boot: 'Installer à côté de Windows' (AUTO)",
                    "   - Expert: 'Autre chose' (partitions manuelles)",
                    "9. Timezone: Europe/Paris",
                    "10. Compte utilisateur: Nom, mot de passe",
                    "11. Installation (~15-30 min)",
                    "12. Redémarrer, retirer clé USB",
                    "13. Premier boot Linux!"
                ]
            },
            {
                "title": "Partitionnement Manuel (Avancé)",
                "bullets": [
                    "Schéma classique (50GB+ disque):",
                    "",
                    "EFI System Partition (si UEFI):",
                    "• 512 MB, FAT32, point montage /boot/efi",
                    "",
                    "/ (root - système):",
                    "• 30-50 GB, ext4, point montage /",
                    "• Contient OS, programmes",
                    "",
                    "/home (données utilisateur):",
                    "• Reste espace, ext4, point montage /home",
                    "• Vos documents/downloads/config",
                    "• Avantage: Réinstaller OS sans perdre /home",
                    "",
                    "swap (mémoire virtuelle):",
                    "• Si RAM <8GB: swap = 2× RAM",
                    "• Si RAM 8-16GB: swap = RAM",
                    "• Si RAM >16GB: swap = 8GB ou aucun",
                    "• Type: linux-swap"
                ]
            },
            {
                "title": "Post-Installation - Premières Étapes",
                "code": "# Ubuntu/Mint/Debian\nsudo apt update && sudo apt upgrade -y\n\n# Installer codecs multimédia\nsudo apt install ubuntu-restricted-extras -y\n\n# Installer drivers NVIDIA (si carte NVIDIA)\nubuntu-drivers devices  # Liste drivers disponibles\nsudo ubuntu-drivers autoinstall  # Installe recommandés\n\n# Activer Firewall\nsudo ufw enable\n\n# Installer logiciels essentiels\nsudo apt install git curl wget vim htop neofetch -y\n\n# Flatpak (store universel)\nsudo apt install flatpak -y\nflatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo\n\n# Redémarrer pour appliquer drivers\nsudo reboot"
            },
            {
                "title": "Dual-Boot: Ordre de Boot GRUB",
                "code": "# Windows apparaît après Linux dans menu? Changer ordre:\n\nsudo nano /etc/default/grub\n\n# Trouver ligne:\nGRUB_DEFAULT=0\n\n# Changer selon position Windows (0=premier, 1=deuxième, etc.)\nGRUB_DEFAULT=2  # Si Windows est 3ème option\n\n# Ou utiliser saved:\nGRUB_DEFAULT=saved\nGRUB_SAVEDEFAULT=true  # Retient dernier OS choisi\n\n# Appliquer changements:\nsudo update-grub\nsudo reboot"
            },
            {
                "warning": "⚠️ Dual-boot: TOUJOURS installer Windows AVANT Linux. Windows écrase bootloader. Si Linux déjà installé, Windows Update peut casser GRUB → boot-repair nécessaire."
            },
            {
                "info": "💡 Clonage disque: Utilisez Clonezilla (live USB) pour backup complète installation Linux avant gros changements."
            }
        ]
    },

    "linux_terminal": {
        "title": "💻 Terminal Linux & Shell",
        "sections": [
            {
                "title": "Qu'est-ce que le Terminal?",
                "content": "Le terminal (ou console) est l'interface texte pour interagir avec Linux. Contrairement à l'interface graphique (GUI), le terminal permet d'exécuter des commandes directement. Un 'shell' (bash, zsh, fish) interprète ces commandes. Sur Linux, le terminal est PUISSANT: automatisation, administration système, scripts, accès à des outils GUI-less."
            },
            {
                "title": "Shells Populaires",
                "bullets": [
                    "Bash (Bourne Again Shell) - Défaut sur 90% distros",
                    "• Syntaxe POSIX standard",
                    "• Scripts compatibles la plupart systèmes Unix",
                    "• Fichiers config: ~/.bashrc (interactif), ~/.bash_profile (login)",
                    "",
                    "Zsh (Z Shell) - Moderne, puissant",
                    "• Autocomplétion avancée",
                    "• Thèmes (Oh-My-Zsh framework populaire)",
                    "• Compatible bash mais avec extras",
                    "• Défaut sur macOS depuis Catalina",
                    "",
                    "Fish (Friendly Interactive Shell)",
                    "• Suggestions auto (comme fish bowl 🐟)",
                    "• Syntaxe différente de bash (incompatible scripts)",
                    "• Très user-friendly pour débutants",
                    "",
                    "Dash - Minimaliste POSIX strict (scripts système rapides)"
                ]
            },
            {
                "title": "Anatomie d'une Commande",
                "code": "# Structure générale:\ncommande [options] [arguments]\n\n# Exemples:\nls                    # Commande seule\nls -la                # Commande + options\nls -la /home          # Commande + options + argument\ncp file1.txt file2.txt  # Commande + 2 arguments\n\n# Options:\n-a, -l, -h  # Format court (1 lettre)\n--all, --list, --help  # Format long (mot complet)\n\n# Combiner options:\nls -l -a -h   # Séparées\nls -lah       # Combinées (équivalent)"
            },
            {
                "title": "Raccourcis Clavier Essentiels",
                "bullets": [
                    "Navigation:",
                    "• Ctrl+A: Début de ligne",
                    "• Ctrl+E: Fin de ligne",
                    "• Ctrl+U: Effacer avant curseur",
                    "• Ctrl+K: Effacer après curseur",
                    "• Ctrl+W: Effacer mot précédent",
                    "• Ctrl+L: Clear screen (ou commande 'clear')",
                    "",
                    "Contrôle processus:",
                    "• Ctrl+C: Tuer processus actuel (SIGINT)",
                    "• Ctrl+Z: Suspendre processus (reprendre avec 'fg')",
                    "• Ctrl+D: EOF (fermer terminal si ligne vide)",
                    "",
                    "Historique:",
                    "• ↑/↓: Naviguer commandes précédentes",
                    "• Ctrl+R: Recherche interactive dans historique",
                    "• !!: Répéter dernière commande",
                    "• !123: Répéter commande #123 de l'historique",
                    "",
                    "Autocomplétion:",
                    "• Tab: Compléter commande/fichier",
                    "• Tab Tab: Afficher toutes possibilités si ambiguïté"
                ]
            },
            {
                "title": "Redirections & Pipes",
                "code": "# Redirection sortie (>)\nls -la > liste.txt         # Écrit sortie dans fichier (écrase)\nls -la >> liste.txt        # Ajoute à la fin du fichier\n\n# Redirection entrée (<)\nwc -l < fichier.txt        # Lit depuis fichier\n\n# Erreurs (stderr = 2)\ncommande 2> erreurs.txt    # Redirige erreurs uniquement\ncommande &> tout.txt       # Stdout + stderr\ncommande 2>&1              # Stderr vers stdout\n\n# Pipe (|) - Sortie commande1 → Entrée commande2\nls -la | grep '.txt'                # Filtrer fichiers .txt\ncat /var/log/syslog | grep error    # Chercher erreurs dans log\nps aux | grep firefox               # Trouver processus Firefox\n\n# Chaîner pipes:\ncat fichier.txt | grep 'motif' | sort | uniq | wc -l\n# Compte lignes uniques contenant 'motif'\n\n# Tee - Afficher ET sauvegarder\nls -la | tee liste.txt     # Affiche dans terminal + sauvegarde"
            },
            {
                "title": "Variables d'Environnement",
                "code": "# Afficher variable:\necho $HOME          # /home/utilisateur\necho $PATH          # Chemins exécutables\necho $USER          # Nom utilisateur\necho $SHELL         # Shell actuel (/bin/bash)\n\n# Définir variable (session actuelle):\nexport MA_VARIABLE=\"valeur\"\necho $MA_VARIABLE\n\n# Variable permanente (ajouter à ~/.bashrc):\necho 'export MA_VARIABLE=\"valeur\"' >> ~/.bashrc\nsource ~/.bashrc    # Recharger config\n\n# Variables utiles:\nPATH     # Chemins de recherche commandes\nHOME     # Répertoire utilisateur\nPWD      # Répertoire actuel\nOLDPWD   # Répertoire précédent\nLANG     # Langue système"
            },
            {
                "title": "Alias - Raccourcis de Commandes",
                "code": "# Créer alias temporaire:\nalias ll='ls -lah'\nalias update='sudo apt update && sudo apt upgrade'\nalias ..='cd ..'\nalias ...='cd ../..'\n\n# Alias permanent (ajouter à ~/.bashrc):\necho \"alias ll='ls -lah'\" >> ~/.bashrc\nsource ~/.bashrc\n\n# Lister alias:\nalias\n\n# Supprimer alias:\nunalias ll\n\n# Alias utiles communs:\nalias df='df -h'          # Espace disque lisible\nalias free='free -h'      # RAM lisible\nalias ps='ps auxf'        # Processus détaillés\nalias mkdir='mkdir -pv'   # Créer parents + verbose"
            },
            {
                "title": "Historique des Commandes",
                "code": "# Afficher historique:\nhistory\n\n# Afficher dernières 20:\nhistory 20\n\n# Exécuter commande #123:\n!123\n\n# Dernière commande:\n!!\n\n# Dernière commande contenant 'apt':\n!apt\n\n# Effacer historique:\nhistory -c\n\n# Taille historique (dans ~/.bashrc):\nHISTSIZE=10000         # Commandes en mémoire\nHISTFILESIZE=20000     # Lignes dans ~/.bash_history\n\n# Ignorer commandes spécifiques:\nHISTIGNORE=\"ls:cd:pwd:clear\""
            },
            {
                "title": "Job Control - Gestion Processus",
                "code": "# Lancer en arrière-plan (&):\nfirefox &\nlong_script.sh &\n\n# Lister jobs:\njobs\n# [1]+ Running    firefox &\n\n# Mettre job actuel en arrière-plan:\nCtrl+Z          # Suspend\nbg              # Reprend en background\n\n# Ramener job au premier plan:\nfg              # Job actuel\nfg %1           # Job #1\n\n# Tuer job:\nkill %1         # Job #1\nkill -9 %1      # Force kill\n\n# Détacher complètement (survive logout):\nnohup long_script.sh &\n# Ou\nscreen          # Terminal virtuel persistant\ntmux            # Alternative moderne à screen"
            },
            {
                "info": "💡 Personnaliser prompt: Modifiez PS1 dans ~/.bashrc. Générateurs en ligne: bashrcgenerator.com, ezprompt.net."
            },
            {
                "warning": "⚠️ Attention 'rm -rf': Aucune corbeille! Fichiers supprimés = IRRÉCUPÉRABLES. Utilisez 'trash-cli' (corbeille CLI) si peur."
            }
        ]
    },

    "linux_commands": {
        "title": "⌨️ Commandes Linux Essentielles",
        "sections": [
            {
                "title": "Navigation Système de Fichiers",
                "code": "# pwd - Print Working Directory (où suis-je?)\npwd\n# /home/utilisateur\n\n# ls - Lister fichiers\nls                # Basique\nls -l             # Format long (permissions, taille, date)\nls -a             # Inclure cachés (.fichier)\nls -lh            # Tailles lisibles (KB, MB, GB)\nls -lah           # Tout combiné\nls -lt            # Trier par date (récent en haut)\nls -lS            # Trier par taille\n\n# cd - Change Directory\ncd /home          # Absolu\ncd Documents      # Relatif\ncd ..             # Parent\ncd -              # Répertoire précédent\ncd ~              # Home (/home/utilisateur)\ncd                # Home aussi\n\n# tree - Arborescence visuelle\ntree              # Arbre récursif\ntree -L 2         # Profondeur 2\ntree -d           # Dossiers seulement"
            },
            {
                "title": "Manipulation Fichiers & Dossiers",
                "code": "# mkdir - Créer dossiers\nmkdir nouveau_dossier\nmkdir -p dossier/sous/dossier    # Créer parents si inexistants\n\n# touch - Créer fichier vide / mettre à jour timestamp\ntouch fichier.txt\ntouch fichier1.txt fichier2.txt fichier3.txt\n\n# cp - Copier\ncp fichier.txt copie.txt                # Fichier\ncp fichier.txt /chemin/destination/\ncp -r dossier/ copie_dossier/           # Dossier (récursif)\ncp -i fichier.txt existant.txt          # Demander confirmation si écrase\n\n# mv - Déplacer / Renommer\nmv ancien.txt nouveau.txt               # Renommer\nmv fichier.txt /autre/dossier/          # Déplacer\nmv *.txt Documents/                     # Tous les .txt\n\n# rm - Supprimer (DÉFINITIF!)\nrm fichier.txt\nrm -r dossier/                          # Dossier récursif\nrm -rf dossier/                         # Force (pas de confirmation)\nrm -i fichier.txt                       # Demander confirmation\n\n# rmdir - Supprimer dossier VIDE\nrmdir dossier_vide/"
            },
            {
                "title": "Lecture & Recherche de Contenu",
                "code": "# cat - Afficher contenu fichier\ncat fichier.txt\ncat fichier1.txt fichier2.txt           # Concaténer\n\n# less - Lire fichier (navigable)\nless fichier.txt\n# Navigation: ↑↓, Page Up/Down, q pour quitter, /motif pour chercher\n\n# head - Premières lignes\nhead fichier.txt                        # 10 premières\nhead -n 20 fichier.txt                  # 20 premières\n\n# tail - Dernières lignes\ntail fichier.txt                        # 10 dernières\ntail -n 50 fichier.txt                  # 50 dernières\ntail -f /var/log/syslog                 # Suivi temps réel (logs)\n\n# grep - Chercher motif dans fichiers\ngrep 'motif' fichier.txt\ngrep -i 'motif' fichier.txt             # Insensible casse\ngrep -r 'motif' /dossier/               # Récursif dans dossier\ngrep -n 'motif' fichier.txt             # Afficher numéros lignes\ngrep -v 'motif' fichier.txt             # Inverser (lignes NE contenant PAS)\ngrep -E 'regex' fichier.txt             # Regex étendue\n\n# find - Chercher fichiers\nfind /home -name '*.txt'                # Par nom\nfind /home -name '*.txt' -type f        # Fichiers seulement\nfind /home -size +100M                  # Fichiers >100MB\nfind /home -mtime -7                    # Modifiés <7 jours\nfind /home -name '*.log' -delete        # Chercher et SUPPRIMER\n\n# wc - Compter\nwc fichier.txt                          # Lignes, mots, caractères\nwc -l fichier.txt                       # Lignes seulement\nwc -w fichier.txt                       # Mots seulement"
            },
            {
                "title": "Compression & Archives",
                "code": "# tar - Archivage (tape archive)\n# Créer archive .tar.gz (gzip compressé)\ntar -czvf archive.tar.gz dossier/\n# c: create, z: gzip, v: verbose, f: file\n\n# Extraire .tar.gz\ntar -xzvf archive.tar.gz\n# x: extract\n\n# Lister contenu sans extraire:\ntar -tzvf archive.tar.gz\n\n# .tar.bz2 (bzip2 - meilleure compression, plus lent)\ntar -cjvf archive.tar.bz2 dossier/     # Créer\ntar -xjvf archive.tar.bz2              # Extraire\n\n# .tar.xz (xz - meilleure compression encore)\ntar -cJvf archive.tar.xz dossier/\ntar -xJvf archive.tar.xz\n\n# zip/unzip (compatibilité Windows)\nzip -r archive.zip dossier/            # Créer\nunzip archive.zip                      # Extraire\nunzip -l archive.zip                   # Lister\n\n# gzip/gunzip (fichiers individuels)\ngzip fichier.txt                       # Crée fichier.txt.gz (supprime original)\ngzip -k fichier.txt                    # Garde original\ngunzip fichier.txt.gz                  # Décompresse"
            },
            {
                "title": "Permissions & Propriétés",
                "code": "# ls -l - Lire permissions\nls -l fichier.txt\n# -rw-r--r-- 1 user group 1234 Jan 01 12:00 fichier.txt\n# ^^^ ^^^ ^^^\n# user group autres\n\n# chmod - Changer permissions\nchmod +x script.sh                     # Ajouter exécution\nchmod -x script.sh                     # Retirer exécution\nchmod 755 script.sh                    # rwxr-xr-x (user=7, group=5, other=5)\nchmod 644 fichier.txt                  # rw-r--r-- (standard fichier)\nchmod -R 755 dossier/                  # Récursif\n\n# Valeurs numériques:\n# r=4, w=2, x=1\n# 7=4+2+1 (rwx), 6=4+2 (rw-), 5=4+1 (r-x), 4=4 (r--)\n\n# chown - Changer propriétaire\nsudo chown utilisateur fichier.txt     # Nouveau propriétaire\nsudo chown utilisateur:groupe fichier.txt  # Propriétaire + groupe\nsudo chown -R utilisateur dossier/     # Récursif\n\n# chgrp - Changer groupe\nsudo chgrp groupe fichier.txt"
            },
            {
                "title": "Informations Système",
                "code": "# uname - Système\nuname -a              # Tout\nuname -r              # Version kernel\nuname -m              # Architecture (x86_64, aarch64)\n\n# df - Espace disque\ndf -h                 # Human-readable\ndf -h /home           # Partition spécifique\n\n# du - Taille dossiers\ndu -sh *              # Taille chaque item dans dossier actuel\ndu -sh /home/user     # Taille totale dossier\ndu -ah | sort -rh | head -20  # 20 plus gros fichiers/dossiers\n\n# free - Mémoire RAM\nfree -h               # Human-readable\n\n# top / htop - Processus temps réel\ntop                   # Basique (q pour quitter)\nhtop                  # Avancé coloré (F10 pour quitter)\n\n# ps - Processus snapshot\nps aux                # Tous processus détaillés\nps aux | grep firefox # Chercher processus\n\n# uptime - Uptime système\nuptime\n# 12:34:56 up 5 days, 3:21, 2 users, load average: 0.5, 0.3, 0.2\n\n# lscpu - Infos CPU\nlscpu\n\n# lsblk - Disques et partitions\nlsblk\n\n# lsusb - Périphériques USB\nlsusb\n\n# lspci - Périphériques PCI (GPU, carte réseau, etc.)\nlspci | grep VGA      # Carte graphique"
            },
            {
                "title": "Réseau",
                "code": "# ip - Configuration réseau (remplace ifconfig)\nip addr show          # Adresses IP\nip link show          # Interfaces réseau\nip route show         # Table routage\n\n# ping - Tester connectivité\nping google.com       # Ctrl+C pour arrêter\nping -c 4 google.com  # 4 paquets seulement\n\n# curl - Télécharger / requêtes HTTP\ncurl https://example.com               # Afficher HTML\ncurl -o fichier.zip https://url.com    # Télécharger\ncurl -I https://example.com            # Headers seulement\n\n# wget - Télécharger fichiers\nwget https://url.com/fichier.zip\nwget -c https://url.com/gros_fichier.iso  # Reprendre si interrompu\n\n# ss - Sockets réseau (remplace netstat)\nss -tuln              # Ports en écoute\nss -tunap             # Toutes connexions\n\n# dig / nslookup - DNS\ndig google.com\nnslookup google.com"
            },
            {
                "title": "Gestion Utilisateurs (sudo requis)",
                "code": "# adduser - Créer utilisateur\nsudo adduser nouveau_user\n\n# deluser - Supprimer utilisateur\nsudo deluser ancien_user              # Garde /home\nsudo deluser --remove-home ancien_user  # Supprime /home aussi\n\n# passwd - Changer mot de passe\npasswd                # Son propre mdp\nsudo passwd user      # Mdp d'un autre user\n\n# usermod - Modifier utilisateur\nsudo usermod -aG sudo user            # Ajouter au groupe sudo\nsudo usermod -s /bin/zsh user         # Changer shell\n\n# groups - Groupes d'un utilisateur\ngroups\ngroups user\n\n# who / w - Utilisateurs connectés\nwho\nw"
            },
            {
                "info": "💡 Commande inconnue? Essayez 'man commande' (manuel) ou 'commande --help'. Ou utilisez 'tldr commande' (install: npm install -g tldr) pour exemples pratiques."
            },
            {
                "warning": "⚠️ 'sudo rm -rf /' = Destruction complète système. JAMAIS exécuter commandes random d'internet sans comprendre!"
            }
        ]
    },

    "linux_files": {
        "title": "📂 Système de Fichiers Linux",
        "sections": [
            {
                "title": "Hiérarchie FHS (Filesystem Hierarchy Standard)",
                "content": "Contrairement à Windows (C:\\, D:\\), Linux a une SEULE racine '/' avec une hiérarchie standardisée. Tous les disques, partitions, périphériques sont 'montés' dans cette arborescence. Exemple: Clé USB devient /media/usb, disque externe /mnt/disque."
            },
            {
                "title": "Répertoires Principaux",
                "bullets": [
                    "/ (root) - Racine absolue du système",
                    "",
                    "/home - Répertoires utilisateurs",
                    "• /home/alice, /home/bob",
                    "• Équivalent C:\\Users\\Alice sur Windows",
                    "• Vos documents, config perso",
                    "",
                    "/root - Home de l'utilisateur 'root' (admin)",
                    "• Séparé de /home pour sécurité",
                    "",
                    "/etc - Fichiers de configuration système",
                    "• /etc/fstab (montage disques)",
                    "• /etc/hosts (résolution DNS locale)",
                    "• /etc/passwd (utilisateurs)",
                    "• Fichiers TEXTE éditables",
                    "",
                    "/bin - Binaires essentiels (ls, cp, mv, bash)",
                    "• Commandes utilisables même en mode minimal",
                    "",
                    "/sbin - Binaires système (admin seulement)",
                    "• fsck, iptables, reboot",
                    "",
                    "/usr - Applications utilisateur",
                    "• /usr/bin (programmes installés)",
                    "• /usr/lib (bibliothèques partagées)",
                    "• /usr/share (données partagées, docs)",
                    "• /usr/local (programmes compilés manuellement)",
                    "",
                    "/var - Données variables",
                    "• /var/log (journaux système/applications)",
                    "• /var/cache (caches divers)",
                    "• /var/tmp (fichiers temporaires persistants)",
                    "",
                    "/tmp - Fichiers temporaires (vidés au reboot)",
                    "• Accessible à tous, utile pour tests",
                    "",
                    "/dev - Fichiers de périphériques",
                    "• /dev/sda (disque 1), /dev/sdb (disque 2)",
                    "• /dev/null (trou noir, supprime données)",
                    "• /dev/random (générateur aléatoire)",
                    "",
                    "/proc - Système de fichiers virtuel (processus)",
                    "• /proc/cpuinfo (infos CPU)",
                    "• /proc/meminfo (RAM)",
                    "• /proc/1234 (infos processus PID 1234)",
                    "",
                    "/sys - Informations kernel/hardware",
                    "• Virtuel, géré par kernel",
                    "",
                    "/mnt - Point de montage temporaire",
                    "• Mount manuel: sudo mount /dev/sdb1 /mnt",
                    "",
                    "/media - Montage automatique (USB, CD)",
                    "• Géré par système (udisks2)",
                    "",
                    "/boot - Fichiers de démarrage",
                    "• Kernel Linux (vmlinuz)",
                    "• initramfs (système initial)",
                    "• GRUB config",
                    "",
                    "/opt - Applications optionnelles (tierces)",
                    "• Google Chrome, TeamViewer, etc.",
                    "",
                    "/srv - Données services (web, ftp)",
                    "• /srv/http (Apache/Nginx content)"
                ]
            },
            {
                "title": "Chemins Absolus vs Relatifs",
                "code": "# Chemin ABSOLU (commence par /)\n/home/alice/Documents/fichier.txt\n/etc/fstab\n\n# Chemin RELATIF (depuis répertoire actuel)\n# Si dans /home/alice:\nDocuments/fichier.txt         # /home/alice/Documents/fichier.txt\n../bob/fichier.txt            # /home/bob/fichier.txt\n../../etc/fstab               # /etc/fstab\n\n# Symboles spéciaux:\n.     # Répertoire actuel\n..    # Répertoire parent\n~     # Home utilisateur (/home/alice)\n~bob  # Home de bob (/home/bob)\n-     # Répertoire précédent (cd -)"
            },
            {
                "title": "Types de Fichiers",
                "bullets": [
                    "Fichiers réguliers (-)",
                    "• fichier.txt, script.sh, image.jpg",
                    "",
                    "Répertoires (d)",
                    "• Dossiers",
                    "",
                    "Liens symboliques (l)",
                    "• Raccourcis type Windows (ln -s cible lien)",
                    "• Exemple: /usr/bin/python → /usr/bin/python3.12",
                    "",
                    "Liens durs (hard links)",
                    "• Plusieurs noms pour même inode (données disque)",
                    "• Supprimer un lien ne supprime pas fichier tant qu'autres existent",
                    "",
                    "Fichiers spéciaux:",
                    "• c (caractère): /dev/tty",
                    "• b (bloc): /dev/sda",
                    "• p (pipe): FIFO",
                    "• s (socket): Communication inter-processus"
                ]
            },
            {
                "title": "Liens Symboliques vs Durs",
                "code": "# Lien symbolique (symlink) - comme raccourci Windows\nln -s /chemin/vers/fichier_original lien_symb\n# Si original supprimé → lien cassé (broken link)\n\n# Exemple pratique:\nsudo ln -s /opt/application/bin/app /usr/local/bin/app\n# Maintenant 'app' accessible partout\n\n# Lien dur (hard link)\nln fichier_original lien_dur\n# Même inode, même données disque\n# Supprimer original ne casse PAS lien_dur\n# Ne marche PAS entre partitions\n\n# Voir destination symlink:\nls -l lien_symb\nreadlink lien_symb\nreadlink -f lien_symb  # Chemin absolu résolu"
            },
            {
                "title": "Montage de Systèmes de Fichiers",
                "code": "# Lister montages actuels:\nmount\ndf -h\nlsblk\n\n# Monter partition manuellement:\nsudo mkdir /mnt/disque_externe\nsudo mount /dev/sdb1 /mnt/disque_externe\ncd /mnt/disque_externe\nls\n\n# Démonter:\nsudo umount /mnt/disque_externe\n# Ou\nsudo umount /dev/sdb1\n\n# Montage automatique au boot (/etc/fstab):\nsudo nano /etc/fstab\n# Ajouter ligne:\nUUID=xxxx-xxxx /mnt/disque ext4 defaults 0 2\n\n# Obtenir UUID:\nsudo blkid\n\n# Monter partition Windows NTFS:\nsudo apt install ntfs-3g -y\nsudo mount -t ntfs-3g /dev/sda2 /mnt/windows\n\n# Montage réseau (SMB/CIFS - partage Windows):\nsudo mount -t cifs //192.168.1.10/Partage /mnt/partage -o username=user,password=pass"
            },
            {
                "title": "Fichiers Cachés",
                "code": "# Fichiers/dossiers commençant par . sont CACHÉS\nls          # Ne les affiche pas\nls -a       # Les affiche\n\n# Exemples:\n.bashrc           # Config bash\n.config/          # Configs applications\n.ssh/             # Clés SSH\n.local/share/     # Données applications\n\n# Créer fichier caché:\ntouch .mon_fichier_secret\n\n# Dossiers cachés importants:\n~/.config         # Configs modernes (XDG)\n~/.local/share    # Données apps\n~/.cache          # Caches (safe de supprimer)"
            },
            {
                "title": "Systèmes de Fichiers Supportés",
                "bullets": [
                    "ext4 (Fourth Extended) - Standard Linux",
                    "• Journaling (récupération après crash)",
                    "• Fichiers jusqu'à 16 TB, partitions 1 EB",
                    "• Performant, stable",
                    "",
                    "Btrfs (B-tree FS) - Moderne",
                    "• Snapshots, compression, RAID intégré",
                    "• Copy-on-write (CoW)",
                    "• Utilisé par Fedora, openSUSE",
                    "",
                    "XFS - Haute performance (gros fichiers)",
                    "• Serveurs, bases de données",
                    "• Redimensionnement limité",
                    "",
                    "F2FS (Flash-Friendly) - Optimisé SSD/eMMC",
                    "• Smartphones, cartes SD",
                    "",
                    "NTFS (Windows) - Support lecture/écriture",
                    "• Via ntfs-3g (installer séparément)",
                    "• Permissions Windows ignorées",
                    "",
                    "FAT32/exFAT - Compatibilité universelle",
                    "• Clés USB, cartes SD",
                    "• Pas de permissions Linux",
                    "• FAT32: Fichiers <4GB max",
                    "",
                    "ZFS - Enterprise (via module externe)",
                    "• Snapshots, compression, déduplication",
                    "• Licence incompatible kernel Linux (install manuel)"
                ]
            },
            {
                "info": "💡 Configuration perso? Toujours dans ~/.config ou ~/.<app>. Système global dans /etc. Ne JAMAIS modifier /proc ou /sys manuellement!"
            },
            {
                "warning": "⚠️ /tmp vidé au reboot! Données importantes → /home. /var/tmp persiste entre reboots."
            }
        ]
    },

    "linux_permissions": {
        "title": "🔐 Permissions & Propriétés Linux",
        "sections": [
            {
                "title": "Modèle de Permissions Unix",
                "content": "Linux utilise un système de permissions strict pour CHAQUE fichier/dossier. Chaque élément a un propriétaire (user), un groupe (group) et des permissions pour 3 catégories: propriétaire, groupe, autres. Ce modèle empêche un utilisateur normal de modifier système ou fichiers d'autrui."
            },
            {
                "title": "Lecture des Permissions (ls -l)",
                "code": "ls -l fichier.txt\n# -rw-r--r-- 1 alice developers 1234 Jan 15 12:00 fichier.txt\n# │││││││││││ │ │     │          │    │           └─ nom\n# │││││││││││ │ │     │          │    └─ date modification\n# │││││││││││ │ │     │          └─ taille (bytes)\n# │││││││││││ │ │     └─ groupe propriétaire\n# │││││││││││ │ └─ utilisateur propriétaire\n# │││││││││││ └─ nombre hard links\n# │││││││││└─ autres: r--  (read)\n# ││││││└─── groupe:  r--  (read)\n# │││└────── user:    rw-  (read, write)\n# │└──────── type: - (fichier), d (dossier), l (lien)\n\n# Décomposition:\n# Position 1:     Type fichier\n# Positions 2-4:  Permissions utilisateur (rwx)\n# Positions 5-7:  Permissions groupe (rwx)\n# Positions 8-10: Permissions autres (rwx)"
            },
            {
                "title": "Types de Permissions",
                "bullets": [
                    "r (read = 4) - Lecture",
                    "• Fichier: Lire contenu",
                    "• Dossier: Lister contenu (ls)",
                    "",
                    "w (write = 2) - Écriture",
                    "• Fichier: Modifier, supprimer",
                    "• Dossier: Créer/supprimer fichiers dedans",
                    "• ⚠️ w sur dossier sans x = inutile!",
                    "",
                    "x (execute = 1) - Exécution",
                    "• Fichier: Exécuter comme programme/script",
                    "• Dossier: Traverser (cd dedans)",
                    "• ⚠️ Dossier sans x = inaccessible même avec r!",
                    "",
                    "- (none = 0) - Aucune permission"
                ]
            },
            {
                "title": "chmod - Changer Permissions",
                "code": "# MÉTHODE SYMBOLIQUE (+ - =)\n\n# Ajouter (+)\nchmod +x script.sh              # Ajoute exécution pour tous\nchmod u+x script.sh             # User seulement\nchmod g+w fichier.txt           # Groupe seulement\nchmod o+r fichier.txt           # Autres seulement\nchmod a+x script.sh             # All (u+g+o)\n\n# Retirer (-)\nchmod -x script.sh              # Retire exécution pour tous\nchmod u-w fichier.txt           # User ne peut plus écrire\n\n# Définir exactement (=)\nchmod u=rwx,g=rx,o=r fichier.txt  # User rwx, groupe rx, autres r\n\n# Combiner\nchmod u+x,g-w,o=r fichier.txt\n\n# MÉTHODE NUMÉRIQUE (octale)\n# Calcul: r=4, w=2, x=1\n# Somme pour chaque catégorie (user, group, other)\n\n# Exemples courants:\nchmod 755 script.sh\n# 7 = 4+2+1 = rwx (user)\n# 5 = 4+0+1 = r-x (group)\n# 5 = 4+0+1 = r-x (other)\n# = -rwxr-xr-x\n\nchmod 644 fichier.txt\n# 6 = 4+2 = rw- (user)\n# 4 = 4   = r-- (group)\n# 4 = 4   = r-- (other)\n# = -rw-r--r--\n\nchmod 700 secret.txt\n# 7 = rwx (user seulement)\n# 0 = --- (groupe aucun)\n# 0 = --- (autres aucun)\n# = -rwx------\n\nchmod 777 fichier.txt  # DANGEREUX! Tout le monde peut tout faire\nchmod 000 fichier.txt  # Personne (même root peut via sudo)\n\n# Récursif (dossiers + contenu):\nchmod -R 755 /dossier/\n\n# Permissions spéciales:\nchmod u+s programme    # SUID (s'exécute avec droits propriétaire)\nchmod g+s dossier      # SGID (fichiers créés héritent groupe)\nchmod +t /tmp          # Sticky bit (seul proprio peut supprimer)"
            },
            {
                "title": "chown - Changer Propriétaire",
                "code": "# Changer utilisateur propriétaire:\nsudo chown alice fichier.txt\n\n# Changer utilisateur ET groupe:\nsudo chown alice:developers fichier.txt\n\n# Changer groupe seulement:\nsudo chown :developers fichier.txt\n# Ou\nsudo chgrp developers fichier.txt\n\n# Récursif:\nsudo chown -R alice:developers /dossier/\n\n# Copier permissions d'un fichier:\nchmod --reference=fichier1.txt fichier2.txt\nchown --reference=fichier1.txt fichier2.txt\n\n# Exemples pratiques:\n# Reprendre possession dossier:\nsudo chown -R $USER:$USER /home/$USER/dossier/\n\n# Donner fichier à www-data (serveur web):\nsudo chown www-data:www-data /var/www/html/index.html"
            },
            {
                "title": "umask - Permissions Par Défaut",
                "code": "# umask définit permissions RETIRÉES lors création fichier/dossier\n\n# Afficher umask actuel:\numask\n# 0022 (format octal)\n\n# Calcul permissions par défaut:\n# Fichiers: 666 - umask = permissions finales\n# Dossiers: 777 - umask = permissions finales\n\n# Exemple umask 0022:\n# Nouveau fichier: 666 - 022 = 644 (rw-r--r--)\n# Nouveau dossier: 777 - 022 = 755 (rwxr-xr-x)\n\n# Changer umask (session actuelle):\numask 0077  # Fichiers 600, dossiers 700 (privé total)\numask 0002  # Fichiers 664, dossiers 775 (groupe peut écrire)\n\n# Permanent (ajouter à ~/.bashrc):\necho \"umask 0077\" >> ~/.bashrc\n\n# umasks courants:\n# 0022 - Défaut (fichiers rw-r--r--, dossiers rwxr-xr-x)\n# 0077 - Privé (fichiers rw-------, dossiers rwx------)\n# 0002 - Collaboratif (fichiers rw-rw-r--, dossiers rwxrwxr-x)"
            },
            {
                "title": "Permissions Spéciales",
                "bullets": [
                    "SUID (Set User ID) - Bit s sur user",
                    "• Programme s'exécute avec permissions du propriétaire",
                    "• Exemple: /usr/bin/passwd (s'exécute en root pour changer mdp)",
                    "• chmod u+s ou chmod 4755",
                    "• ls affiche: -rwsr-xr-x",
                    "• ⚠️ Risque sécurité si mal utilisé!",
                    "",
                    "SGID (Set Group ID) - Bit s sur group",
                    "• Fichier: Exécute avec groupe propriétaire",
                    "• Dossier: Nouveaux fichiers héritent du groupe du dossier (pas créateur)",
                    "• chmod g+s ou chmod 2755",
                    "• ls affiche: -rwxr-sr-x",
                    "• Utile: Dossiers partagés entre équipe",
                    "",
                    "Sticky Bit - Bit t sur others",
                    "• Sur dossier: Seul propriétaire du fichier peut le supprimer",
                    "• Exemple: /tmp (tout le monde écrit, chacun supprime le sien seulement)",
                    "• chmod +t ou chmod 1777",
                    "• ls affiche: drwxrwxrwt",
                    "",
                    "Notation numérique 4 chiffres:",
                    "• chmod 4755 (SUID)",
                    "• chmod 2755 (SGID)",
                    "• chmod 1755 (Sticky)",
                    "• chmod 7755 (Tous = 4+2+1)"
                ]
            },
            {
                "title": "ACL - Access Control Lists (Avancé)",
                "code": "# Permissions étendues au-delà user/group/other\n# Installer si absent:\nsudo apt install acl -y\n\n# Voir ACL:\ngetfacl fichier.txt\n\n# Donner permissions à utilisateur spécifique:\nsetfacl -m u:bob:rw fichier.txt\n# Bob peut lire/écrire même si pas dans groupe\n\n# Donner à groupe spécifique:\nsetfacl -m g:developers:rwx dossier/\n\n# Retirer ACL:\nsetfacl -x u:bob fichier.txt\n\n# Récursif + défaut (nouveaux fichiers héritent):\nsetfacl -R -m u:bob:rwx dossier/\nsetfacl -R -m d:u:bob:rwx dossier/  # Défaut\n\n# Supprimer toutes ACL:\nsetfacl -b fichier.txt\n\n# Copier ACL:\ngetfacl fichier1.txt | setfacl --set-file=- fichier2.txt"
            },
            {
                "title": "Attributs Étendus (chattr/lsattr)",
                "code": "# Protection supplémentaire au-delà chmod\n\n# Voir attributs:\nlsattr fichier.txt\n# ----i--------e----- fichier.txt\n\n# Immuable (i) - Personne (même root) ne peut modifier/supprimer:\nsudo chattr +i fichier_critique.txt\nsudo rm fichier_critique.txt  # Erreur!\n# Retirer:\nsudo chattr -i fichier_critique.txt\n\n# Append only (a) - Ajouter seulement, pas modifier/supprimer:\nsudo chattr +a /var/log/critique.log\necho \"nouvelle ligne\" >> /var/log/critique.log  # OK\nrm /var/log/critique.log  # Erreur!\n\n# Pas de dump (d) - Exclure des sauvegardes dump:\nchattr +d fichier_temp.txt\n\n# Secure delete (s) - Écrase données au delete:\nchattr +s fichier_secret.txt\n\n# Undeletable (u) - Récupérable après suppression:\nchattr +u fichier_important.txt"
            },
            {
                "info": "💡 Script bash non exécutable? chmod +x script.sh. Erreur 'Permission denied' en ./script.sh? Vérifiez x."
            },
            {
                "warning": "⚠️ chmod 777 = MAUVAISE pratique! Tout le monde peut tout faire. Utilisez 755 (fichiers exécutables) ou 644 (fichiers normaux)."
            }
        ]
    },

    "linux_processes": {
        "title": "⚙️ Processus & Services Linux",
        "sections": [
            {
                "title": "Qu'est-ce qu'un Processus?",
                "content": "Un processus est une instance d'un programme en exécution. Chaque processus a un PID (Process ID) unique, un propriétaire, une priorité, et consomme CPU/RAM. Linux est multitâche: des centaines de processus tournent simultanément (services système, applications, démons)."
            },
            {
                "title": "ps - Lister Processus",
                "code": "# Processus utilisateur actuel:\nps\n\n# Tous processus (format BSD):\nps aux\n# a: Tous utilisateurs\n# u: Format détaillé (user, cpu, mem)\n# x: Inclure processus sans terminal\n\n# Sortie ps aux:\n# USER  PID %CPU %MEM    VSZ   RSS TTY   STAT START TIME COMMAND\n# alice 1234 15.3  2.1 123456 54321 pts/1 S    12:00 0:05 firefox\n\n# Colonnes importantes:\n# PID: Process ID\n# %CPU: Utilisation CPU\n# %MEM: Utilisation RAM (%)\n# VSZ: Mémoire virtuelle (KB)\n# RSS: Mémoire résidente physique (KB)\n# STAT: État (R=running, S=sleeping, Z=zombie, D=uninterruptible)\n# COMMAND: Commande lancée\n\n# Processus d'un utilisateur:\nps -u alice\n\n# Arbre de processus (hiérarchie parent-enfant):\nps auxf     # Format forêt\npstree      # Arbre visuel\npstree -p   # Avec PID\n\n# Chercher processus:\nps aux | grep firefox\n# Ou (plus rapide):\npgrep firefox        # Juste PID\npgrep -a firefox     # PID + commande complète"
            },
            {
                "title": "top & htop - Monitoring Temps Réel",
                "code": "# top - Monitoring basique\ntop\n# Navigation:\n# q: Quitter\n# k: Kill processus (demande PID)\n# r: Renice (changer priorité)\n# M: Trier par mémoire\n# P: Trier par CPU\n# 1: Afficher tous cœurs CPU\n# h: Aide\n\n# htop - Version améliorée (colorée, souris)\nhtop\n# F6: Trier par colonne\n# F9: Kill processus\n# F5: Arbre\n# F10: Quitter\n# / : Chercher\n\n# Installer htop:\nsudo apt install htop -y\n\n# Alternatives modernes:\nsudo apt install btop -y     # btop++ (encore plus joli)\nsudo apt install glances -y  # Multi-système (CPU, RAM, réseau, disque)"
            },
            {
                "title": "kill - Arrêter Processus",
                "code": "# Envoyer signal à processus\n\n# kill normal (SIGTERM = termine proprement):\nkill 1234           # PID 1234\nkill $(pgrep firefox)  # Par nom\n\n# Force kill (SIGKILL = tue immédiatement, pas de cleanup):\nkill -9 1234\nkill -SIGKILL 1234  # Équivalent\nkillall -9 firefox  # Tous processus firefox\n\n# Autres signaux utiles:\nkill -1 1234   # SIGHUP (recharger config)\nkill -15 1234  # SIGTERM (défaut, terminaison propre)\nkill -19 1234  # SIGSTOP (suspendre, comme Ctrl+Z)\nkill -18 1234  # SIGCONT (reprendre)\n\n# killall - Par nom de commande:\nkillall firefox\nkillall -9 firefox\n\n# pkill - Par pattern:\npkill fire            # Tue tout contenant 'fire'\npkill -u alice        # Tous processus de alice\npkill -9 -u alice     # Force kill tous processus alice\n\n# Tuer tous processus d'une application:\nps aux | grep firefox | awk '{print $2}' | xargs kill -9\n# Ou simplement:\npkill -9 firefox"
            },
            {
                "title": "nice & renice - Priorité Processus",
                "code": "# Priorité (niceness): -20 (max priorité) à 19 (min priorité)\n# Défaut: 0\n# Seul root peut mettre <0 (haute priorité)\n\n# Lancer avec priorité:\nnice -n 10 ./script_long.sh      # Basse priorité (gentil envers autres)\nnice -n -5 ./critique.sh         # Haute priorité (root requis)\n\n# Changer priorité processus existant:\nrenice -n 15 -p 1234             # PID 1234 → priorité 15\nsudo renice -n -10 -p 1234       # Haute priorité (root requis)\n\n# Par utilisateur:\nsudo renice -n 10 -u alice       # Tous processus alice\n\n# Voir niceness:\nps -el | grep 1234               # Colonne NI\ntop                              # Colonne NI\n\n# Exemple: Compilation en arrière-plan sans ralentir PC:\nnice -n 19 make -j8  # Priorité minimale"
            },
            {
                "title": "Background & Foreground Jobs",
                "code": "# Lancer en arrière-plan (&):\n./script_long.sh &\nfirefox &\n\n# Lister jobs actifs:\njobs\n# [1]  Running    ./script_long.sh &\n# [2]- Running    firefox &\n# [3]+ Stopped    vim fichier.txt\n\n# Suspendre job actuel:\nCtrl+Z\n# Job mis en pause\n\n# Reprendre en arrière-plan:\nbg           # Dernier job suspendu\nbg %1        # Job #1\n\n# Reprendre en premier plan:\nfg           # Dernier job\nfg %2        # Job #2\n\n# Tuer job:\nkill %1      # Job #1\nkill %2\n\n# Détacher complètement (survit logout):\nnohup ./script.sh &\n# Sortie dans nohup.out\n\n# Ou utiliser screen/tmux:\nscreen -S session_nom\n./script.sh\nCtrl+A puis D  # Détacher\nscreen -r session_nom  # Rattacher\n\n# tmux (moderne):\ntmux new -s session_nom\n./script.sh\nCtrl+B puis D  # Détacher\ntmux attach -t session_nom"
            },
            {
                "title": "systemd & systemctl - Services Système",
                "content": "systemd est le système d'init moderne (PID 1) sur la majorité des distros Linux récentes. Il gère le démarrage du système, les services (démons), les montages, les timers (cron-like). Les services sont définis par des unit files (.service) dans /lib/systemd/system/ ou /etc/systemd/system/."
            },
            {
                "title": "systemctl - Gestion Services",
                "code": "# Statut service:\nsystemctl status ssh\nsystemctl status apache2\n\n# Démarrer service:\nsudo systemctl start ssh\n\n# Arrêter service:\nsudo systemctl stop ssh\n\n# Redémarrer service:\nsudo systemctl restart ssh\n\n# Recharger config (sans redémarrer):\nsudo systemctl reload ssh\n\n# Activer au démarrage:\nsudo systemctl enable ssh\n# Crée symlink dans /etc/systemd/system/\n\n# Désactiver au démarrage:\nsudo systemctl disable ssh\n\n# Activer ET démarrer:\nsudo systemctl enable --now ssh\n\n# Lister tous services:\nsystemctl list-units --type=service\nsystemctl list-units --type=service --state=running  # Actifs seulement\nsystemctl list-units --type=service --state=failed   # Échoués\n\n# Lister services démarrés au boot:\nsystemctl list-unit-files --type=service | grep enabled\n\n# Voir logs service:\nsudo journalctl -u ssh              # Tous logs\nsudo journalctl -u ssh -f           # Suivi temps réel\nsudo journalctl -u ssh --since today\nsudo journalctl -u ssh --since \"2024-01-01 12:00\"\n\n# Recharger systemd (après modification .service):\nsudo systemctl daemon-reload\n\n# Exemples services courants:\n# ssh.service - Serveur SSH\n# apache2.service / nginx.service - Serveurs web\n# mysql.service / postgresql.service - Bases de données\n# bluetooth.service - Bluetooth\n# NetworkManager.service - Gestion réseau"
            },
            {
                "title": "Créer Service systemd Personnalisé",
                "code": "# Créer fichier /etc/systemd/system/mon_service.service\n\nsudo nano /etc/systemd/system/mon_service.service\n\n# Contenu exemple:\n[Unit]\nDescription=Mon Application Python\nAfter=network.target\n\n[Service]\nType=simple\nUser=alice\nWorkingDirectory=/home/alice/app\nExecStart=/usr/bin/python3 /home/alice/app/main.py\nRestart=on-failure\nRestartSec=5s\n\n[Install]\nWantedBy=multi-user.target\n\n# Activer:\nsudo systemctl daemon-reload\nsudo systemctl enable mon_service\nsudo systemctl start mon_service\nsudo systemctl status mon_service\n\n# Types de service:\n# simple - Processus principal (défaut)\n# forking - Fork en arrière-plan (daemon classique)\n# oneshot - Exécute puis termine (scripts)\n# notify - Notifie systemd quand prêt"
            },
            {
                "info": "💡 Processus zombie (Z)? Processus mort dont parent n'a pas lu exit status. Généralement inoffensif. Si nombreux: bug dans programme parent."
            },
            {
                "warning": "⚠️ kill -9 = dernier recours! Processus n'a pas le temps de sauvegarder/cleanup. Préférez kill normal (SIGTERM) d'abord."
            }
        ]
    },

    "linux_apt": {
        "title": "📦 APT - Package Manager (Debian/Ubuntu)",
        "sections": [
            {
                "title": "Qu'est-ce qu'APT?",
                "content": "APT (Advanced Package Tool) est le gestionnaire de paquets pour Debian, Ubuntu, Linux Mint et dérivés. Il gère l'installation, mise à jour, et suppression de logiciels depuis des dépôts officiels (repositories). APT résout automatiquement les dépendances: installer Firefox installera aussi toutes bibliothèques requises. Plus moderne et user-friendly que dpkg bas-niveau."
            },
            {
                "title": "Commandes APT Essentielles",
                "code": "# Mettre à jour liste des paquets disponibles:\nsudo apt update\n# À lancer AVANT tout install/upgrade (rafraîchit index)\n\n# Mettre à jour tous paquets installés:\nsudo apt upgrade           # Met à jour (garde anciens paquets)\nsudo apt full-upgrade      # Met à jour + supprime obsolètes (recommandé)\n\n# Combo classique:\nsudo apt update && sudo apt upgrade -y\n# -y = répondre automatiquement 'yes'\n\n# Installer paquet:\nsudo apt install firefox\nsudo apt install vim git curl wget htop\n\n# Réinstaller paquet (si corrompu):\nsudo apt reinstall firefox\n\n# Supprimer paquet:\nsudo apt remove firefox           # Garde fichiers config\nsudo apt purge firefox            # Supprime config aussi (recommandé)\nsudo apt autoremove               # Supprimer dépendances orphelines\n\n# Combo nettoyage complet:\nsudo apt purge firefox && sudo apt autoremove\n\n# Chercher paquet:\napt search firefox\napt search \"web browser\"\n\n# Infos sur paquet:\napt show firefox                  # Description, version, taille, dépendances\napt policy firefox                # Versions disponibles, repo source\n\n# Lister paquets installés:\napt list --installed\napt list --installed | grep firefox\n\n# Lister mises à jour disponibles:\napt list --upgradable\n\n# Voir dépendances:\napt depends firefox\napt rdepends firefox              # Paquets dépendant de firefox"
            },
            {
                "title": "apt vs apt-get - Quelle Différence?",
                "bullets": [
                    "apt - Commande moderne (depuis 2014)",
                    "• Interface user-friendly (barre progression, couleurs)",
                    "• Combine apt-get + apt-cache",
                    "• Recommandée pour utilisation interactive",
                    "",
                    "apt-get - Commande legacy (stable depuis 1998)",
                    "• Plus stable pour scripts (syntaxe ne change jamais)",
                    "• Moins de features visuelles",
                    "• apt-cache (chercher) séparé",
                    "",
                    "Équivalences:",
                    "• apt update = apt-get update",
                    "• apt upgrade = apt-get upgrade",
                    "• apt install = apt-get install",
                    "• apt remove = apt-get remove",
                    "• apt search = apt-cache search",
                    "• apt show = apt-cache show",
                    "",
                    "Conseil: Utilisez 'apt' en CLI manuel, 'apt-get' dans scripts."
                ]
            },
            {
                "title": "Gestion des Dépôts (Repositories)",
                "code": "# Lister dépôts actifs:\napt policy\ncat /etc/apt/sources.list\nls /etc/apt/sources.list.d/\n\n# Ajouter dépôt PPA (Ubuntu seulement):\nsudo add-apt-repository ppa:user/ppa-name\nsudo apt update\n\n# Exemple: PPA OBS Studio\nsudo add-apt-repository ppa:obsproject/obs-studio\nsudo apt update\nsudo apt install obs-studio\n\n# Supprimer PPA:\nsudo add-apt-repository --remove ppa:user/ppa-name\n\n# Activer composants (universe, multiverse):\nsudo add-apt-repository universe\nsudo add-apt-repository multiverse\nsudo apt update\n\n# Éditer sources manuellement (avancé):\nsudo nano /etc/apt/sources.list\n\n# Format ligne repo:\ndeb http://archive.ubuntu.com/ubuntu/ jammy main restricted\n# deb     = paquets binaires\n# deb-src = paquets sources (code)\n# jammy   = version Ubuntu (focal=20.04, jammy=22.04, noble=24.04)\n# main    = composant (main, universe, restricted, multiverse)"
            },
            {
                "title": "Nettoyage & Maintenance",
                "code": "# Supprimer paquets inutilisés (dépendances orphelines):\nsudo apt autoremove\n\n# Nettoyer cache téléchargements (.deb):\nsudo apt clean         # Supprime tout cache\nsudo apt autoclean     # Supprime versions obsolètes seulement\n\n# Voir taille cache:\ndu -sh /var/cache/apt/archives/\n\n# Réparer paquets cassés:\nsudo apt --fix-broken install\nsudo apt --fix-missing install\n\n# Reconfigurer paquet:\nsudo dpkg-reconfigure paquet_name\n# Exemple: reconfigurer timezone:\nsudo dpkg-reconfigure tzdata\n\n# Forcer mise à jour complète (upgrade distribution):\nsudo apt dist-upgrade\n# Ou (moderne):\nsudo apt full-upgrade\n\n# Lister fichiers d'un paquet installé:\ndpkg -L firefox\n\n# Trouver quel paquet contient un fichier:\ndpkg -S /usr/bin/firefox\n# Ou (pour fichiers non installés):\napt-file search /usr/bin/firefox  # Installer apt-file d'abord"
            },
            {
                "title": "Verrouiller Versions (Hold)",
                "code": "# Empêcher mise à jour paquet (hold):\nsudo apt-mark hold firefox\n\n# Lister paquets verrouillés:\napt-mark showhold\n\n# Déverrouiller:\nsudo apt-mark unhold firefox\n\n# Installer version spécifique:\nsudo apt install firefox=123.0+build1-0ubuntu0.22.04.1\n\n# Lister versions disponibles:\napt-cache policy firefox\n\n# Downgrade (installer version ancienne):\nsudo apt install firefox=122.0+build1-0ubuntu0.22.04.1\nsudo apt-mark hold firefox  # Empêcher re-upgrade"
            },
            {
                "title": "Logs & Historique",
                "code": "# Voir historique installations/suppressions:\ncat /var/log/apt/history.log\nzcat /var/log/apt/history.log.*.gz  # Logs archivés\n\n# Logs détaillés (erreurs):\ncat /var/log/apt/term.log\n\n# Historique dpkg (plus détaillé):\ncat /var/log/dpkg.log\n\n# Chercher installation spécifique:\ngrep \" install \" /var/log/dpkg.log | grep firefox\ngrep \" remove \" /var/log/dpkg.log"
            },
            {
                "info": "💡 Erreur 'Could not get lock /var/lib/apt/lists/lock'? Un autre process APT tourne (Software Updater). Fermez-le ou attendez fin."
            },
            {
                "warning": "⚠️ JAMAIS 'sudo apt upgrade' sans 'sudo apt update' avant! Risque paquets incompatibles. Toujours: update PUIS upgrade."
            }
        ]
    },

    "linux_dnf": {
        "title": "🔴 DNF - Package Manager (Fedora/RHEL)",
        "sections": [
            {
                "title": "Qu'est-ce que DNF?",
                "content": "DNF (Dandified Yum) est le gestionnaire de paquets pour Fedora, Red Hat Enterprise Linux (RHEL), CentOS Stream, Rocky Linux, AlmaLinux. Il remplace Yum (encore compatible). DNF gère les paquets RPM (.rpm) et résout automatiquement les dépendances. Plus rapide et intelligent que Yum legacy."
            },
            {
                "title": "Commandes DNF Essentielles",
                "code": "# Mettre à jour cache + installer mises à jour:\nsudo dnf upgrade              # Met à jour tout (remplace 'update')\nsudo dnf update               # Alias de upgrade (legacy Yum)\n\n# Installer paquet:\nsudo dnf install firefox\nsudo dnf install vim git curl wget htop\n\n# Installer plusieurs paquets:\nsudo dnf install package1 package2 package3\n\n# Supprimer paquet:\nsudo dnf remove firefox\n\n# Supprimer + dépendances orphelines:\nsudo dnf autoremove firefox\n\n# Chercher paquet:\ndnf search firefox\ndnf search \"web browser\"\n\n# Infos sur paquet:\ndnf info firefox\n\n# Lister paquets installés:\ndnf list installed\ndnf list installed | grep firefox\n\n# Lister mises à jour disponibles:\ndnf check-update\n# Ou:\ndnf list updates\n\n# Réinstaller paquet:\nsudo dnf reinstall firefox\n\n# Downgrade (version précédente):\nsudo dnf downgrade firefox"
            },
            {
                "title": "Groupes de Paquets",
                "code": "# DNF permet installer groupes (ensembles de paquets liés)\n\n# Lister groupes disponibles:\ndnf group list\ndnf grouplist\n\n# Infos sur groupe:\ndnf group info \"Development Tools\"\n\n# Installer groupe:\nsudo dnf group install \"Development Tools\"\nsudo dnf groupinstall \"Development Tools\"  # Alias\n\n# Exemples groupes utiles:\nsudo dnf groupinstall \"Development Tools\"         # gcc, make, autotools\nsudo dnf groupinstall \"C Development Tools and Libraries\"\nsudo dnf groupinstall \"GNOME Desktop Environment\"\nsudo dnf groupinstall \"KDE Plasma Workspaces\"\n\n# Supprimer groupe:\nsudo dnf group remove \"Development Tools\""
            },
            {
                "title": "Gestion des Dépôts (Repositories)",
                "code": "# Lister dépôts actifs:\ndnf repolist\ndnf repolist --all         # Tous (actifs + désactivés)\n\n# Infos dépôt:\ndnf repoinfo fedora\n\n# Activer dépôt:\nsudo dnf config-manager --set-enabled repo_id\n\n# Désactiver dépôt:\nsudo dnf config-manager --set-disabled repo_id\n\n# Ajouter dépôt tiers:\n# Exemple: RPM Fusion (codecs multimédia, drivers NVIDIA)\nsudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm\nsudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm\n\n# Fichiers config dépôts:\nls /etc/yum.repos.d/\nsudo nano /etc/yum.repos.d/fedora.repo\n\n# Format fichier .repo:\n[repo-id]\nname=Repository Name\nbaseurl=https://url.com/repo/\nenabled=1\ngpgcheck=1\ngpgkey=https://url.com/key.asc"
            },
            {
                "title": "Nettoyage & Maintenance",
                "code": "# Supprimer paquets orphelins:\nsudo dnf autoremove\n\n# Nettoyer cache:\nsudo dnf clean all         # Tout\nsudo dnf clean packages    # Paquets .rpm téléchargés\nsudo dnf clean metadata    # Métadonnées repos\n\n# Taille cache:\ndu -sh /var/cache/dnf/\n\n# Reconstruire cache:\nsudo dnf makecache\n\n# Historique DNF:\ndnf history\n# Affiche ID transaction, date, commande, paquets modifiés\n\n# Détails transaction:\ndnf history info 25        # Transaction #25\n\n# Annuler transaction (rollback):\nsudo dnf history undo 25   # Annule transaction #25\nsudo dnf history undo last # Annule dernière transaction\n\n# Refaire transaction:\nsudo dnf history redo 25"
            },
            {
                "title": "Recherche Avancée",
                "code": "# Chercher fichier dans paquets:\ndnf provides /usr/bin/firefox\ndnf whatprovides /usr/bin/firefox  # Alias\n\n# Exemple: Trouver quel paquet contient gcc:\ndnf provides */bin/gcc\n\n# Lister fichiers d'un paquet installé:\nrpm -ql firefox\n\n# Lister fichiers paquet non installé:\ndnf repoquery -l firefox\n\n# Dépendances paquet:\ndnf repoquery --requires firefox\n\n# Paquets dépendant de X:\ndnf repoquery --whatrequires firefox"
            },
            {
                "title": "Upgrade Distribution (Fedora)",
                "code": "# Upgrade Fedora version (ex: 39 → 40)\n\n# 1. Mettre à jour système actuel:\nsudo dnf upgrade --refresh\nsudo dnf install dnf-plugin-system-upgrade\n\n# 2. Télécharger nouvelle version:\nsudo dnf system-upgrade download --releasever=40\n# Vérifiez conflits affichés\n\n# 3. Redémarrer et upgrader:\nsudo dnf system-upgrade reboot\n# PC redémarre, upgrade en mode texte (~15-30 min)\n\n# 4. Après reboot, nettoyer:\nsudo dnf autoremove\nsudo dnf clean all\n\n# Vérifier version:\ncat /etc/fedora-release"
            },
            {
                "info": "💡 RPM Fusion = dépôt essentiel sur Fedora! Contient codecs (MP3, H.264), drivers NVIDIA, Steam, Discord, etc. Installez-le en priorité."
            },
            {
                "warning": "⚠️ Différence Fedora vs RHEL: Fedora = paquets très récents (bleeding edge), RHEL/Rocky/Alma = stables (anciens mais testés). Ne mélangez PAS repos!"
            }
        ]
    },

    "linux_pacman": {
        "title": "⚙️ Pacman - Package Manager (Arch Linux)",
        "sections": [
            {
                "title": "Qu'est-ce que Pacman?",
                "content": "Pacman est le gestionnaire de paquets ultra-rapide d'Arch Linux, Manjaro, EndeavourOS, et dérivés. Plus minimaliste qu'APT/DNF, mais très puissant. Arch est 'rolling release': pas de versions (20.04, 40, etc.), mises à jour continues. Pacman + AUR (Arch User Repository) = 80 000+ paquets disponibles."
            },
            {
                "title": "Commandes Pacman Essentielles",
                "code": "# Mettre à jour système COMPLET:\nsudo pacman -Syu\n# -S: Sync (installer/mettre à jour)\n# -y: refresh package list (update)\n# -u: upgrade (mettre à jour tout)\n\n# Installer paquet:\nsudo pacman -S firefox\nsudo pacman -S vim git curl wget htop\n\n# Installer plusieurs paquets:\nsudo pacman -S package1 package2 package3\n\n# Supprimer paquet (garde dépendances):\nsudo pacman -R firefox\n\n# Supprimer paquet + dépendances inutilisées:\nsudo pacman -Rs firefox\n# -s: Supprimer dépendances orphelines\n\n# Supprimer paquet + config + dépendances:\nsudo pacman -Rns firefox\n# -n: Supprimer fichiers config aussi\n\n# Chercher paquet (repo officiel):\npacman -Ss firefox\npacman -Ss \"web browser\"\n\n# Infos sur paquet:\npacman -Si firefox            # Non installé\npacman -Qi firefox            # Installé\n\n# Lister fichiers d'un paquet:\npacman -Ql firefox            # Installé\npacman -Fl firefox            # Non installé (database requise)\n\n# Lister paquets installés:\npacman -Q\npacman -Q | grep firefox\n\n# Lister paquets installés explicitement (par vous):\npacman -Qe\n\n# Lister paquets orphelins (dépendances non utilisées):\npacman -Qdt"
            },
            {
                "title": "Opérations Avancées",
                "code": "# Supprimer tous paquets orphelins:\nsudo pacman -Rns $(pacman -Qdtq)\n# -Q: Query\n# -d: Dépendances\n# -t: Non requises\n# -q: Quiet (juste noms)\n\n# Downgrade paquet (installer version ancienne):\n# Nécessite paquet 'downgrade' (AUR):\nyay -S downgrade\nsudo downgrade firefox\n\n# Nettoyer cache:\nsudo pacman -Sc               # Versions obsolètes\nsudo pacman -Scc              # Tout cache (⚠️ perte rollback)\n\n# Taille cache:\ndu -sh /var/cache/pacman/pkg/\n\n# Forcer refresh database:\nsudo pacman -Syy              # Double -y = force refresh\n\n# Réinstaller paquet:\nsudo pacman -S firefox --overwrite '*'  # Force overwrite si conflits\n\n# Installer paquet local .pkg.tar.zst:\nsudo pacman -U /chemin/vers/package.pkg.tar.zst\n\n# Trouver quel paquet possède fichier:\npacman -Qo /usr/bin/firefox\n# Ou (non installé):\npacman -F /usr/bin/firefox    # Nécessite: sudo pacman -Fy"
            },
            {
                "title": "Miroirs - Accélérer Téléchargements",
                "code": "# Fichier miroirs:\nsudo nano /etc/pacman.d/mirrorlist\n\n# Générer liste miroirs rapides (reflector):\nsudo pacman -S reflector\n\n# Trouver 10 miroirs les plus rapides:\nsudo reflector --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist\n\n# Backup mirrorlist avant modification:\nsudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup\n\n# Tester vitesse manuellement:\nping -c 3 mirror.url.com"
            },
            {
                "title": "AUR - Arch User Repository",
                "code": "# AUR = dépôt communautaire (80 000+ paquets)\n# Paquets NON officiels, compilés from source\n# Nécessite AUR helper (yay, paru)\n\n# Installer yay (AUR helper populaire):\nsudo pacman -S --needed git base-devel\ngit clone https://aur.archlinux.org/yay.git\ncd yay\nmakepkg -si\ncd ..\nrm -rf yay\n\n# Utiliser yay (syntaxe identique pacman):\nyay -Syu                      # Update système + AUR\nyay -S google-chrome          # Installer depuis AUR\nyay -Ss spotify               # Chercher AUR\nyay -R google-chrome          # Supprimer\n\n# Installer manuellement depuis AUR (sans helper):\ngit clone https://aur.archlinux.org/package-name.git\ncd package-name\nless PKGBUILD                 # ⚠️ VÉRIFIER code (sécurité!)\nmakepkg -si\n# -s: installer dépendances\n# -i: installer paquet après build\n\n# Exemples paquets AUR populaires:\nyay -S google-chrome visual-studio-code-bin spotify discord"
            },
            {
                "title": "Configuration /etc/pacman.conf",
                "code": "# Éditer config:\nsudo nano /etc/pacman.conf\n\n# Options utiles à décommenter/ajouter:\n\n# Barre de progression colorée:\nColor\nILoveCandy          # Pacman mange points (Easter egg)\n\n# Parallel downloads (pacman 6.0+):\nParallelDownloads = 5\n\n# Activer multilib (paquets 32-bit sur 64-bit):\n[multilib]\nInclude = /etc/pacman.d/mirrorlist\n\n# Après modif:\nsudo pacman -Syy              # Refresh databases"
            },
            {
                "title": "Gestion Hooks (Automatisation)",
                "code": "# Hooks = scripts auto-exécutés lors install/upgrade\n# Fichiers dans /etc/pacman.d/hooks/\n\n# Exemple: Hook pour nettoyer cache auto:\nsudo nano /etc/pacman.d/hooks/clean-cache.hook\n\n[Trigger]\nOperation = Upgrade\nOperation = Install\nOperation = Remove\nType = Package\nTarget = *\n\n[Action]\nDescription = Cleaning pacman cache...\nWhen = PostTransaction\nExec = /usr/bin/paccache -rk2\n# -r: remove\n# -k2: keep 2 latest versions\n\n# Activer hook:\nsudo pacman -S pacman-contrib  # Pour paccache"
            },
            {
                "info": "💡 Arch = rolling release: JAMAIS 'partial upgrade' (pacman -Sy package). Toujours 'pacman -Syu' (full system upgrade) sinon casse système!"
            },
            {
                "warning": "⚠️ AUR = paquets NON vérifiés! Lisez TOUJOURS PKGBUILD avant installer. Code malveillant possible. Privilégiez paquets bien notés/populaires."
            }
        ]
    },

    "linux_systemd": {
        "title": "⚡ Systemd - Init System Avancé",
        "sections": [
            {
                "title": "Systemd - Au-delà de systemctl",
                "content": "Systemd (PID 1) est bien plus qu'un gestionnaire de services. C'est un écosystème complet: journald (logs), networkd (réseau), timesyncd (NTP), logind (sessions), resolved (DNS), et 50+ autres composants. Remplace SysVinit/Upstart sur 90%+ distros modernes. Controversé pour sa complexité mais ultra-puissant."
            },
            {
                "title": "Units Systemd - Types Principaux",
                "bullets": [
                    ".service - Services/démons",
                    "• ssh.service, apache2.service, docker.service",
                    "",
                    ".socket - Sockets réseau/IPC",
                    "• Activation à la demande (socket listening)",
                    "",
                    ".timer - Tâches planifiées (cron-like)",
                    "• Calendrier ou délais",
                    "",
                    ".mount - Points de montage",
                    "• Alternative à /etc/fstab",
                    "",
                    ".target - Groupes d'units",
                    "• multi-user.target (runlevel 3)",
                    "• graphical.target (runlevel 5)",
                    "",
                    ".path - Surveillance fichiers/dossiers",
                    "• Déclenche action si fichier créé/modifié",
                    "",
                    ".device - Périphériques hardware",
                    "• Auto-généré par udev"
                ]
            },
            {
                "title": "Timers - Remplacer Cron",
                "code": "# Créer timer pour script backup\n\n# 1. Service (/etc/systemd/system/backup.service)\n[Unit]\nDescription=Backup Script\n\n[Service]\nType=oneshot\nExecStart=/usr/local/bin/backup.sh\n\n# 2. Timer (/etc/systemd/system/backup.timer)\n[Unit]\nDescription=Run backup daily\n\n[Timer]\nOnCalendar=daily\n# Ou: OnCalendar=*-*-* 02:00:00  # Chaque jour à 2h\n# Ou: OnCalendar=Mon *-*-* 00:00:00  # Chaque lundi\nPersistent=true  # Rattrape si PC éteint\n\n[Install]\nWantedBy=timers.target\n\n# Activer timer:\nsudo systemctl daemon-reload\nsudo systemctl enable --now backup.timer\n\n# Lister timers:\nsystemctl list-timers\nsystemctl list-timers --all\n\n# Statut timer:\nsystemctl status backup.timer\n\n# Forcer exécution immédiate:\nsudo systemctl start backup.service\n\n# Syntaxe OnCalendar:\n# minutely, hourly, daily, weekly, monthly, yearly\n# *-*-* HH:MM:SS (année-mois-jour heure:minute:seconde)\n# Mon,Tue,Wed 10:00 (lundi/mardi/mercredi à 10h)"
            },
            {
                "title": "journalctl - Logs Systemd",
                "code": "# Voir tous logs:\njournalctl\n\n# Logs depuis dernier boot:\njournalctl -b\njournalctl -b -1  # Boot précédent\n\n# Logs service spécifique:\njournalctl -u ssh.service\njournalctl -u apache2 -f  # Suivi temps réel (-f = follow)\n\n# Filtrer par date/heure:\njournalctl --since \"2024-01-01\"\njournalctl --since \"2024-01-01 10:00\" --until \"2024-01-01 12:00\"\njournalctl --since yesterday\njournalctl --since \"1 hour ago\"\njournalctl --since today\n\n# Filtrer par priorité:\njournalctl -p err       # Erreurs seulement\njournalctl -p warning   # Warnings et plus grave\n# Priorités: emerg, alert, crit, err, warning, notice, info, debug\n\n# Logs kernel:\njournalctl -k\njournalctl --dmesg\n\n# Par utilisateur/PID:\njournalctl _UID=1000\njournalctl _PID=1234\n\n# Reverse (plus récents en premier):\njournalctl -r\n\n# Limiter nombre lignes:\njournalctl -n 50       # 50 dernières\n\n# Format sortie:\njournalctl -o json     # JSON\njournalctl -o json-pretty\njournalctl -o short    # Défaut\njournalctl -o verbose  # Tout afficher\n\n# Taille logs:\njournalctl --disk-usage\n\n# Nettoyer vieux logs:\nsudo journalctl --vacuum-time=7d    # Garder 7 jours\nsudo journalctl --vacuum-size=500M  # Max 500MB"
            },
            {
                "title": "Targets - Runlevels Systemd",
                "code": "# Targets = groupes d'units (équivalent runlevels SysVinit)\n\n# Lister targets:\nsystemctl list-units --type=target\n\n# Target actuel:\nsystemctl get-default\n\n# Changer target par défaut:\nsudo systemctl set-default multi-user.target   # CLI seulement (runlevel 3)\nsudo systemctl set-default graphical.target    # GUI (runlevel 5)\n\n# Changer target immédiatement (sans reboot):\nsudo systemctl isolate multi-user.target\nsudo systemctl isolate graphical.target\n\n# Targets importants:\n# poweroff.target      - Arrêt système\n# rescue.target        - Mode rescue (single-user)\n# multi-user.target    - Multi-user CLI\n# graphical.target     - GUI\n# reboot.target        - Redémarrage\n\n# Équivalences runlevels:\n# 0 = poweroff.target\n# 1 = rescue.target\n# 3 = multi-user.target\n# 5 = graphical.target\n# 6 = reboot.target"
            },
            {
                "title": "Analyse Performances Boot",
                "code": "# Temps boot total:\nsystemd-analyze\n# Startup finished in 2.5s (kernel) + 8.3s (userspace) = 10.8s\n\n# Services les plus lents:\nsystemd-analyze blame\n\n# Chaîne critique (goulot d'étranglement):\nsystemd-analyze critical-chain\n\n# Graphique SVG boot:\nsystemd-analyze plot > boot.svg\nfirefox boot.svg\n\n# Vérifier unit file (syntaxe):\nsystemd-analyze verify /etc/systemd/system/mon_service.service"
            },
            {
                "info": "💡 Timers systemd > cron: Logs centralisés (journalctl), dépendances (After=network), pas besoin root, rattrapage si PC éteint (Persistent=true)."
            },
            {
                "warning": "⚠️ systemctl daemon-reload OBLIGATOIRE après modification .service/.timer! Systemd ne voit pas changements sinon."
            }
        ]
    },

    "linux_network": {
        "title": "🌐 Configuration Réseau Linux",
        "sections": [
            {
                "title": "Outils Réseau Modernes vs Legacy",
                "bullets": [
                    "MODERNE (utilisez ceci):",
                    "• ip (remplace ifconfig) - Configuration IP/routes",
                    "• ss (remplace netstat) - Sockets/connexions",
                    "• NetworkManager (nmcli) - Gestion réseau haut niveau",
                    "",
                    "LEGACY (obsolète mais encore vu):",
                    "• ifconfig (net-tools) - Config interfaces",
                    "• netstat (net-tools) - Connexions",
                    "• route - Table routage"
                ]
            },
            {
                "title": "ip - Configuration IP",
                "code": "# Afficher interfaces:\nip addr show              # Toutes interfaces\nip a                      # Raccourci\nip addr show eth0         # Interface spécifique\n\n# Ajouter IP:\nsudo ip addr add 192.168.1.100/24 dev eth0\n\n# Supprimer IP:\nsudo ip addr del 192.168.1.100/24 dev eth0\n\n# Activer/désactiver interface:\nsudo ip link set eth0 up\nsudo ip link set eth0 down\n\n# Routes:\nip route show             # Table routage\nip r                      # Raccourci\n\n# Ajouter route:\nsudo ip route add 10.0.0.0/8 via 192.168.1.1\n\n# Route par défaut (gateway):\nsudo ip route add default via 192.168.1.1\n\n# Supprimer route:\nsudo ip route del 10.0.0.0/8\n\n# Voir voisins ARP:\nip neigh show\n\n# Stats interfaces:\nip -s link                # Paquets RX/TX, erreurs"
            },
            {
                "title": "NetworkManager (nmcli) - GUI/CLI",
                "code": "# NetworkManager = gestionnaire réseau moderne (Ubuntu, Fedora, etc.)\n# GUI: nm-applet (icône réseau), nmtui (TUI)\n# CLI: nmcli\n\n# Statut:\nnmcli general status\nnmcli device status        # Liste interfaces\n\n# Lister connexions:\nnmcli connection show\nnmcli con show            # Raccourci\n\n# Activer/désactiver connexion:\nnmcli con up \"Wired connection 1\"\nnmcli con down \"Wired connection 1\"\n\n# WiFi - Lister réseaux:\nnmcli device wifi list\n\n# Connecter WiFi:\nnmcli device wifi connect \"SSID\" password \"motdepasse\"\n\n# Configuration IP statique:\nnmcli con mod \"Wired connection 1\" ipv4.addresses 192.168.1.100/24\nnmcli con mod \"Wired connection 1\" ipv4.gateway 192.168.1.1\nnmcli con mod \"Wired connection 1\" ipv4.dns \"8.8.8.8 8.8.4.4\"\nnmccli con mod \"Wired connection 1\" ipv4.method manual\nnmcli con up \"Wired connection 1\"\n\n# Retour DHCP:\nnmcli con mod \"Wired connection 1\" ipv4.method auto\nnmcli con up \"Wired connection 1\"\n\n# Créer nouvelle connexion:\nnmcli con add type ethernet con-name \"Ma Connexion\" ifname eth0 ipv4.method auto\n\n# Supprimer connexion:\nnmcli con delete \"Ma Connexion\"\n\n# Désactiver/activer WiFi:\nnmcli radio wifi off\nnmcli radio wifi on"
            },
            {
                "title": "Configuration Manuelle (/etc/network/interfaces - Debian)",
                "code": "# Fichier: /etc/network/interfaces (Debian/Ubuntu sans NetworkManager)\n\nsudo nano /etc/network/interfaces\n\n# IP statique:\nauto eth0\niface eth0 inet static\n    address 192.168.1.100\n    netmask 255.255.255.0\n    gateway 192.168.1.1\n    dns-nameservers 8.8.8.8 8.8.4.4\n\n# DHCP:\nauto eth0\niface eth0 inet dhcp\n\n# Appliquer changements:\nsudo systemctl restart networking\n# Ou\nsudo ifdown eth0 && sudo ifup eth0"
            },
            {
                "title": "Netplan (Ubuntu 18.04+)",
                "code": "# Netplan = config réseau YAML (Ubuntu moderne)\n# Fichiers: /etc/netplan/*.yaml\n\nsudo nano /etc/netplan/01-netcfg.yaml\n\n# DHCP:\nnetwork:\n  version: 2\n  renderer: networkd\n  ethernets:\n    eth0:\n      dhcp4: true\n\n# IP statique:\nnetwork:\n  version: 2\n  renderer: networkd\n  ethernets:\n    eth0:\n      addresses:\n        - 192.168.1.100/24\n      gateway4: 192.168.1.1\n      nameservers:\n        addresses:\n          - 8.8.8.8\n          - 8.8.4.4\n\n# WiFi:\nnetwork:\n  version: 2\n  renderer: networkd\n  wifis:\n    wlan0:\n      access-points:\n        \"SSID\":\n          password: \"motdepasse\"\n      dhcp4: true\n\n# Tester config (dry-run):\nsudo netplan try\n# Appuyer Enter si ça marche, sinon rollback auto après 120s\n\n# Appliquer:\nsudo netplan apply\n\n# Debug:\nsudo netplan --debug apply"
            },
            {
                "title": "DNS - Configuration",
                "code": "# Fichier DNS (legacy):\ncat /etc/resolv.conf\n\n# Modifier DNS temporairement:\nsudo nano /etc/resolv.conf\nnameserver 8.8.8.8\nnameserver 8.8.4.4\n# ⚠️ Écrasé au reboot par NetworkManager/systemd-resolved\n\n# DNS permanent (NetworkManager):\nnmcli con mod \"Wired connection 1\" ipv4.dns \"8.8.8.8 8.8.4.4\"\nnmcli con up \"Wired connection 1\"\n\n# DNS permanent (Netplan):\n# Voir section Netplan ci-dessus (nameservers)\n\n# systemd-resolved (Ubuntu/Fedora moderne):\nsudo systemctl status systemd-resolved\nresolvectl status         # Voir config DNS actuelle\nresolvectl query google.com  # Tester résolution\n\n# DNS populaires:\n# Google: 8.8.8.8, 8.8.4.4\n# Cloudflare: 1.1.1.1, 1.0.0.1\n# Quad9: 9.9.9.9, 149.112.112.112"
            },
            {
                "title": "Tests Réseau - Diagnostic",
                "code": "# Ping:\nping -c 4 google.com      # 4 paquets\nping -c 4 8.8.8.8         # Test connectivité IP (pas DNS)\n\n# Traceroute (chemin réseau):\ntraceroute google.com\ntracepath google.com      # Alternative sans root\n\n# DNS lookup:\nnslookup google.com\ndig google.com\ndig google.com +short     # Juste IP\n\n# Ports ouverts (ss):\nss -tuln                  # TCP/UDP listening\nss -tunap                 # Toutes connexions + programmes\nss -t state established   # Connexions TCP établies\n\n# Netcat (test port):\nnc -zv 192.168.1.1 22     # Teste si port 22 ouvert\n# -z: scan, -v: verbose\n\n# Vitesse réseau (iperf3):\nsudo apt install iperf3 -y\n# Serveur:\niperf3 -s\n# Client:\niperf3 -c 192.168.1.100\n\n# Whois (infos domaine):\nwhois google.com\n\n# MTR (ping + traceroute continu):\nmtr google.com"
            },
            {
                "info": "💡 NetworkManager vs systemd-networkd: NetworkManager = desktop (WiFi facile), systemd-networkd = serveurs (léger, pas GUI)."
            },
            {
                "warning": "⚠️ /etc/resolv.conf souvent symlink vers systemd-resolved. Modifier directement = écrasé! Utilisez nmcli/netplan pour DNS permanent."
            }
        ]
    },

    "linux_firewall": {
        "title": "🔥 Firewall Linux (ufw/iptables)",
        "sections": [
            {
                "title": "ufw - Uncomplicated Firewall (Débutant)",
                "content": "ufw est une interface simplifiée pour iptables. Par défaut sur Ubuntu/Debian. Plus facile que iptables brut mais moins flexible. Parfait pour desktop/serveur simple. Règles persistantes automatiquement."
            },
            {
                "title": "ufw - Commandes Essentielles",
                "code": "# Installer (si absent):\nsudo apt install ufw -y\n\n# Statut:\nsudo ufw status\nsudo ufw status verbose\nsudo ufw status numbered       # Avec numéros règles\n\n# Activer/désactiver:\nsudo ufw enable                # ⚠️ Active au boot\nsudo ufw disable\n\n# Règles par défaut:\nsudo ufw default deny incoming    # Bloquer tout entrant\nsudo ufw default allow outgoing   # Autoriser tout sortant\n\n# Autoriser port:\nsudo ufw allow 22                 # SSH\nsudo ufw allow 80                 # HTTP\nsudo ufw allow 443                # HTTPS\nsudo ufw allow 22/tcp             # TCP seulement\nsudo ufw allow 53/udp             # UDP seulement\n\n# Autoriser range ports:\nsudo ufw allow 6000:6007/tcp\n\n# Bloquer port:\nsudo ufw deny 23                  # Telnet\n\n# Autoriser service (par nom):\nsudo ufw allow ssh\nsudo ufw allow http\nsudo ufw allow https\n# Services définis dans /etc/services\n\n# Autoriser depuis IP spécifique:\nsudo ufw allow from 192.168.1.100\nsudo ufw allow from 192.168.1.0/24  # Subnet\n\n# Autoriser IP vers port:\nsudo ufw allow from 192.168.1.100 to any port 22\n\n# Supprimer règle:\nsudo ufw delete allow 80\n# Ou par numéro:\nsudo ufw status numbered\nsudo ufw delete 3                 # Supprime règle #3\n\n# Logging:\nsudo ufw logging on\nsudo ufw logging off\nsudo ufw logging low/medium/high/full\n\n# Logs:\nsudo tail -f /var/log/ufw.log\n\n# Reset (supprimer toutes règles):\nsudo ufw reset"
            },
            {
                "title": "ufw - Exemples Pratiques",
                "code": "# Serveur web basique:\nsudo ufw default deny incoming\nsudo ufw default allow outgoing\nsudo ufw allow ssh\nsudo ufw allow http\nsudo ufw allow https\nsudo ufw enable\n\n# SSH seulement depuis réseau local:\nsudo ufw allow from 192.168.1.0/24 to any port 22\nsudo ufw deny 22  # Bloque SSH du reste du monde\n\n# Limiter tentatives SSH (anti brute-force):\nsudo ufw limit ssh\n# 6 connexions max en 30s depuis même IP\n\n# Autoriser ping (ICMP):\nsudo ufw allow proto icmp\n\n# Bloquer IP spécifique:\nsudo ufw deny from 123.45.67.89\n\n# Serveur gaming (Minecraft exemple):\nsudo ufw allow 25565/tcp"
            },
            {
                "title": "iptables - Firewall Avancé",
                "content": "iptables est le firewall Linux bas-niveau (kernel netfilter). Très puissant mais syntaxe complexe. ufw/firewalld sont des frontends pour iptables. Utilisez iptables si besoin contrôle total: NAT, port forwarding complexe, règles conditionnelles avancées."
            },
            {
                "title": "iptables - Concepts de Base",
                "bullets": [
                    "Tables:",
                    "• filter (défaut): Filtrage paquets (INPUT, OUTPUT, FORWARD)",
                    "• nat: Network Address Translation (PREROUTING, POSTROUTING)",
                    "• mangle: Modification paquets avancée",
                    "",
                    "Chaînes (filter table):",
                    "• INPUT: Paquets entrants vers machine",
                    "• OUTPUT: Paquets sortants depuis machine",
                    "• FORWARD: Paquets traversant machine (routeur)",
                    "",
                    "Actions (targets):",
                    "• ACCEPT: Autoriser",
                    "• DROP: Rejeter silencieusement",
                    "• REJECT: Rejeter avec message ICMP",
                    "• LOG: Logger sans bloquer",
                    "• MASQUERADE: NAT (IP source dynamique)"
                ]
            },
            {
                "title": "iptables - Commandes de Base",
                "code": "# Lister règles:\nsudo iptables -L                  # Liste filter table\nsudo iptables -L -v -n            # Verbose, numérique (pas DNS)\nsudo iptables -L INPUT            # Chaîne INPUT seulement\nsudo iptables -t nat -L           # Table NAT\n\n# Ajouter règle (append -A):\nsudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT\n# -A INPUT: Append à chaîne INPUT\n# -p tcp: Protocole TCP\n# --dport 22: Port destination 22\n# -j ACCEPT: Action ACCEPT\n\n# Insérer règle en position (insert -I):\nsudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT\n# Position 1 (début chaîne)\n\n# Supprimer règle:\nsudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT\n# Ou par numéro:\nsudo iptables -L INPUT --line-numbers\nsudo iptables -D INPUT 3          # Supprime règle #3\n\n# Vider toutes règles:\nsudo iptables -F                  # Flush\nsudo iptables -t nat -F           # Flush NAT\n\n# Politique par défaut:\nsudo iptables -P INPUT DROP       # Bloquer tout entrant\nsudo iptables -P OUTPUT ACCEPT    # Autoriser tout sortant\nsudo iptables -P FORWARD DROP     # Pas de forwarding\n\n# Sauvegarder règles:\nsudo apt install iptables-persistent -y\nsudo netfilter-persistent save\n# Ou manuel:\nsudo iptables-save > /etc/iptables/rules.v4\n\n# Restaurer règles:\nsudo iptables-restore < /etc/iptables/rules.v4"
            },
            {
                "title": "iptables - Exemples Avancés",
                "code": "# Autoriser connexions établies/related:\nsudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT\n# CRUCIAL! Autorise réponses à connexions sortantes\n\n# Autoriser loopback:\nsudo iptables -A INPUT -i lo -j ACCEPT\nsudo iptables -A OUTPUT -o lo -j ACCEPT\n\n# Autoriser SSH depuis IP spécifique:\nsudo iptables -A INPUT -p tcp -s 192.168.1.100 --dport 22 -j ACCEPT\n\n# Limiter tentatives SSH (anti brute-force):\nsudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --set\nsudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 4 -j DROP\n# Max 4 connexions par minute\n\n# Logger paquets droppés:\nsudo iptables -A INPUT -j LOG --log-prefix \"[iptables DROP] \" --log-level 4\nsudo iptables -A INPUT -j DROP\n\n# NAT - Partage connexion Internet (routeur):\nsudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE\nsudo sysctl -w net.ipv4.ip_forward=1  # Activer forwarding\necho \"net.ipv4.ip_forward=1\" | sudo tee -a /etc/sysctl.conf\n\n# Port forwarding (redirection):\nsudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80\n# Redirige port 8080 → 80"
            },
            {
                "title": "firewalld (Fedora/RHEL/CentOS)",
                "code": "# firewalld = frontend iptables pour RHEL/Fedora\n# Concepts: Zones (public, home, work, dmz, etc.)\n\n# Statut:\nsudo firewall-cmd --state\nsudo systemctl status firewalld\n\n# Lister zones:\nfirewall-cmd --get-zones\nfirewall-cmd --get-active-zones\n\n# Zone par défaut:\nfirewall-cmd --get-default-zone\nsudo firewall-cmd --set-default-zone=public\n\n# Autoriser service:\nsudo firewall-cmd --zone=public --add-service=http\nsudo firewall-cmd --zone=public --add-service=https\nsudo firewall-cmd --zone=public --add-service=ssh\n\n# Permanent (survit reboot):\nsudo firewall-cmd --zone=public --add-service=http --permanent\nsudo firewall-cmd --reload  # Appliquer changements permanents\n\n# Autoriser port:\nsudo firewall-cmd --zone=public --add-port=8080/tcp\nsudo firewall-cmd --zone=public --add-port=8080/tcp --permanent\n\n# Lister règles:\nfirewall-cmd --zone=public --list-all\n\n# Supprimer service/port:\nsudo firewall-cmd --zone=public --remove-service=http\nsudo firewall-cmd --zone=public --remove-port=8080/tcp"
            },
            {
                "info": "💡 Débutant? ufw. Serveur RHEL? firewalld. Expert? iptables brut. Ne mélangez PAS ufw + iptables manuel = conflits!"
            },
            {
                "warning": "⚠️ 'ufw enable' avec SSH? TOUJOURS 'ufw allow 22' AVANT 'ufw enable' sinon vous vous verrouillez hors du serveur distant!"
            }
        ]
    },

    "linux_ssh": {
        "title": "🔑 SSH - Accès Distant Sécurisé",
        "sections": [
            {
                "title": "SSH - Secure Shell",
                "content": "SSH permet connexion sécurisée à distance (chiffrée). Remplace Telnet (non chiffré). Utilisations: Administration serveurs, transfert fichiers (scp/sftp), tunneling, X11 forwarding. Port par défaut: 22."
            },
            {
                "title": "Installation & Démarrage",
                "code": "# Installer serveur SSH:\nsudo apt install openssh-server -y    # Ubuntu/Debian\nsudo dnf install openssh-server -y    # Fedora\nsudo pacman -S openssh -y             # Arch\n\n# Démarrer/activer SSH:\nsudo systemctl start sshd\nsudo systemctl enable sshd    # Démarre au boot\nsudo systemctl status sshd\n\n# Vérifier port écoute:\nss -tuln | grep :22"
            },
            {
                "title": "Connexion SSH Basique",
                "code": "# Se connecter:\nssh user@192.168.1.100\nssh user@hostname.com\n\n# Port non standard:\nssh -p 2222 user@192.168.1.100\n\n# Exécuter commande à distance:\nssh user@server 'ls -la /var/log'\nssh user@server 'sudo systemctl restart apache2'\n\n# Verbose (debug connexion):\nssh -v user@server            # Niveau 1\nssh -vv user@server           # Niveau 2\nssh -vvv user@server          # Niveau 3 (max)\n\n# Première connexion:\n# Affiche fingerprint clé serveur\n# Tapez 'yes' pour accepter (ajouté à ~/.ssh/known_hosts)"
            },
            {
                "title": "Clés SSH - Authentification Sans Mot de Passe",
                "code": "# Générer paire clés (client):\nssh-keygen -t ed25519 -C \"mon@email.com\"\n# Ou RSA 4096 (compatible ancien):\nssh-keygen -t rsa -b 4096 -C \"mon@email.com\"\n\n# Fichiers créés:\n# ~/.ssh/id_ed25519 (privée, GARDEZ SECRÈTE!)\n# ~/.ssh/id_ed25519.pub (publique, partageable)\n\n# Copier clé publique vers serveur:\nssh-copy-id user@server\n# Demande mot de passe UNE fois, puis plus jamais\n\n# Ou manuellement:\ncat ~/.ssh/id_ed25519.pub | ssh user@server 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'\n\n# Permissions correctes (important!):\nchmod 700 ~/.ssh\nchmod 600 ~/.ssh/id_ed25519\nchmod 644 ~/.ssh/id_ed25519.pub\nchmod 600 ~/.ssh/authorized_keys  # Sur serveur\n\n# Tester connexion (clé):\nssh user@server\n# Aucun mot de passe demandé!\n\n# Spécifier clé spécifique:\nssh -i ~/.ssh/autre_cle user@server\n\n# Agent SSH (éviter retaper passphrase clé):\neval \"$(ssh-agent -s)\"\nssh-add ~/.ssh/id_ed25519\n# Passphrase demandée une fois par session"
            },
            {
                "title": "Configuration SSH (~/.ssh/config)",
                "code": "# Fichier config client (facilite connexions):\nnano ~/.ssh/config\n\n# Exemple:\nHost serveur1\n    HostName 192.168.1.100\n    User admin\n    Port 22\n    IdentityFile ~/.ssh/id_ed25519\n\nHost serveur2\n    HostName server2.example.com\n    User bob\n    Port 2222\n\nHost github\n    HostName github.com\n    User git\n    IdentityFile ~/.ssh/github_key\n\n# Connexion simplifiée:\nssh serveur1              # Au lieu de: ssh admin@192.168.1.100\nssh serveur2\nssh github\n\n# Wildcards:\nHost 192.168.1.*\n    User admin\n    IdentityFile ~/.ssh/local_key\n\n# Options utiles:\n# ServerAliveInterval 60        # Keep-alive toutes 60s\n# ServerAliveCountMax 3         # Max tentatives\n# Compression yes               # Compresser données\n# ForwardAgent yes              # Forwarding agent SSH\n# ForwardX11 yes                # X11 forwarding (GUI)"
            },
            {
                "title": "Sécurisation Serveur SSH",
                "code": "# Éditer config serveur:\nsudo nano /etc/ssh/sshd_config\n\n# Changements recommandés:\n\n# 1. Changer port (évite scans automatiques):\nPort 2222\n\n# 2. Désactiver login root:\nPermitRootLogin no\n\n# 3. Authentification par clé seulement:\nPasswordAuthentication no\nPubkeyAuthentication yes\n\n# 4. Désactiver X11 forwarding si inutilisé:\nX11Forwarding no\n\n# 5. Limiter utilisateurs:\nAllowUsers alice bob\n# Ou groupes:\nAllowGroups ssh-users\n\n# 6. Protocole 2 seulement (v1 obsolète):\nProtocol 2\n\n# 7. Timeout inactivité:\nClientAliveInterval 300       # 5 minutes\nClientAliveCountMax 2\n\n# 8. Limiter tentatives authentification:\nMaxAuthTries 3\nMaxSessions 5\n\n# Appliquer changements:\nsudo systemctl restart sshd\n\n# Tester config AVANT redémarrage:\nsudo sshd -t\n# Si erreur: affiche problème, config actuelle reste"
            },
            {
                "title": "Transfert Fichiers - scp & sftp",
                "code": "# scp - Secure Copy\n\n# Copier fichier local → serveur:\nscp fichier.txt user@server:/chemin/destination/\nscp -r dossier/ user@server:/chemin/  # Récursif\n\n# Copier serveur → local:\nscp user@server:/chemin/fichier.txt /local/\nscp -r user@server:/chemin/dossier/ /local/\n\n# Entre 2 serveurs:\nscp user1@server1:/fichier user2@server2:/destination/\n\n# Port non standard:\nscp -P 2222 fichier.txt user@server:/destination/\n# ⚠️ scp utilise -P (majuscule), ssh utilise -p (minuscule)\n\n# Verbose:\nscp -v fichier.txt user@server:/destination/\n\n# Limiter bande passante (KB/s):\nscp -l 1024 gros_fichier.iso user@server:/destination/\n# 1024 KB/s = 1 MB/s\n\n# sftp - Secure FTP (interactive)\n\nsftp user@server\n# Commandes sftp:\nsftp> ls                      # Liste serveur\nsftp> lls                     # Liste local\nsftp> pwd                     # Dossier serveur\nsftp> lpwd                    # Dossier local\nsftp> get fichier.txt         # Télécharger\nsftp> put fichier.txt         # Uploader\nsftp> get -r dossier/         # Télécharger récursif\nsftp> put -r dossier/         # Uploader récursif\nsftp> cd /chemin              # Changer dossier serveur\nsftp> lcd /chemin             # Changer dossier local\nsftp> exit                    # Quitter"
            },
            {
                "title": "SSH Tunneling - Port Forwarding",
                "code": "# Local Port Forwarding (accès service distant via local):\nssh -L 8080:localhost:80 user@server\n# localhost:8080 → server:80\n# Utilisez http://localhost:8080 pour accéder site sur serveur\n\n# Exemple: Accéder base de données distante:\nssh -L 3306:localhost:3306 user@db_server\n# Connectez client MySQL à localhost:3306\n\n# Remote Port Forwarding (exposer service local sur serveur):\nssh -R 8080:localhost:80 user@server\n# server:8080 → localhost:80 (votre machine)\n# Serveur peut accéder votre localhost:80 via son port 8080\n\n# Dynamic Port Forwarding (SOCKS proxy):\nssh -D 1080 user@server\n# Proxy SOCKS sur localhost:1080\n# Configure navigateur: SOCKS5 proxy localhost:1080\n# Tout trafic passe par serveur (VPN-like)\n\n# Background (-f) + no command (-N):\nssh -fN -L 8080:localhost:80 user@server\n# Tunnel en arrière-plan\n\n# Keep-alive:\nssh -L 8080:localhost:80 -o ServerAliveInterval=60 user@server"
            },
            {
                "info": "💡 GitHub/GitLab: Générez clé SSH dédiée (ssh-keygen), ajoutez .pub dans settings web. Plus sécurisé que HTTPS + mot de passe."
            },
            {
                "warning": "⚠️ Clé privée (~/.ssh/id_*) = ULTRA SENSIBLE! Jamais commit Git, jamais partager. Si compromise: ssh-keygen nouvelle + supprimer .pub des serveurs."
            }
        ]
    },

    "linux_wsl": {
        "title": "🪟 WSL - Windows Subsystem for Linux",
        "sections": [
            {
                "title": "Qu'est-ce que WSL?",
                "content": "WSL permet d'exécuter un environnement Linux complet DANS Windows 10/11, sans VM ni dual-boot. WSL2 (kernel Linux réel) offre performance quasi-native. Parfait pour développeurs: accès bash, outils Unix, Docker, tout en gardant Windows. Fichiers Windows accessibles depuis Linux (/mnt/c/)."
            },
            {
                "title": "Installation WSL2 (Windows 11 / Windows 10 22H2+)",
                "code": "# Méthode moderne (PowerShell admin):\nwsl --install\n# Installe WSL2 + Ubuntu par défaut, redémarre PC\n\n# Choisir distro spécifique:\nwsl --install -d Debian\nwsl --install -d kali-linux\n\n# Lister distros disponibles:\nwsl --list --online\nwsl -l -o\n\n# Après reboot, Ubuntu lance auto:\n# Créez username/password Linux\n\n# Vérifier version WSL:\nwsl --version\nwsl --status\n\n# Lister distros installées:\nwsl --list --verbose\nwsl -l -v\n# NAME      STATE           VERSION\n# Ubuntu    Running         2"
            },
            {
                "title": "Installation Manuelle (Windows 10 ancien)",
                "code": "# 1. Activer WSL + Virtual Machine Platform (PowerShell admin):\ndism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart\ndism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart\n\n# 2. Redémarrer PC\n\n# 3. Télécharger kernel update WSL2:\n# https://aka.ms/wsl2kernel\n\n# 4. Définir WSL2 par défaut:\nwsl --set-default-version 2\n\n# 5. Installer distro depuis Microsoft Store:\n# Ubuntu, Debian, Kali, openSUSE, etc."
            },
            {
                "title": "Utilisation Basique WSL",
                "code": "# Lancer distro par défaut:\nwsl\n# Ou:\nubuntu\ndebian\nkali\n\n# Lancer commande unique:\nwsl ls -la\nwsl uname -a\n\n# Lancer distro spécifique:\nwsl -d Ubuntu\nwsl -d Debian\n\n# User spécifique:\nwsl -u root\nwsl -d Ubuntu -u alice\n\n# Arrêter distro:\nwsl --terminate Ubuntu\nwsl -t Ubuntu\n\n# Arrêter toutes:\nwsl --shutdown\n\n# Exporter distro (backup):\nwsl --export Ubuntu C:\\backup\\ubuntu.tar\n\n# Importer distro:\nwsl --import Ubuntu-Copy C:\\WSL\\Ubuntu-Copy C:\\backup\\ubuntu.tar\n\n# Supprimer distro:\nwsl --unregister Ubuntu\n# ⚠️ Supprime DÉFINITIVEMENT (backup d'abord!)"
            },
            {
                "title": "Accès Fichiers Windows ↔ Linux",
                "code": "# DEPUIS LINUX: Accéder disques Windows\ncd /mnt/c/Users/VotreNom/Documents\nls /mnt/d/  # Disque D:\n\n# Chemins Windows → Linux:\n# C:\\Users\\Alice → /mnt/c/Users/Alice\n# D:\\Projets → /mnt/d/Projets\n\n# DEPUIS WINDOWS: Accéder filesystem Linux\n# Explorateur: \\\\wsl$\\Ubuntu\\home\\alice\n# Ou: \\\\wsl.localhost\\Ubuntu\\home\\alice\n\n# Ouvrir explorateur depuis WSL:\nexplorer.exe .\n\n# Éditer fichier Linux avec VS Code Windows:\ncode ~/.bashrc\n# Nécessite VS Code + extension Remote-WSL\n\n# ⚠️ IMPORTANT: Fichiers Linux dans /home/\n# Performance: Travaillez dans /home/user/, PAS /mnt/c/\n# /mnt/c/ = lent (système fichiers Windows)\n# /home/ = rapide (ext4 natif)"
            },
            {
                "title": "Intégration Windows - Commandes",
                "code": "# Lancer apps Windows depuis WSL:\nexplorer.exe .                # Ouvre dossier actuel\nnotepad.exe fichier.txt       # Notepad Windows\ncode .                        # VS Code (si installé)\nchrome.exe https://google.com # Chrome\n\n# Lancer commandes WSL depuis cmd/PowerShell:\nwsl ls -la\nwsl grep \"pattern\" fichier.txt\n\n# Pipes Windows ↔ WSL:\ndir | wsl grep \"txt\"          # PowerShell → WSL\nwsl cat fichier.txt | findstr \"motif\"  # WSL → cmd\n\n# Variables environnement partagées:\nwsl echo $PATH\n# Contient chemins Windows + Linux\n\n# Désactiver interop (si problème):\necho \"[interop]\nenabled=false\" | sudo tee -a /etc/wsl.conf\nwsl --shutdown\nwsl"
            },
            {
                "title": "Configuration WSL (/etc/wsl.conf)",
                "code": "# Fichier config distro WSL:\nsudo nano /etc/wsl.conf\n\n[boot]\nsystemd=true              # Activer systemd (WSL 0.67.6+)\n\n[automount]\nenabled=true\nroot=/mnt/\noptions=\"metadata,umask=22,fmask=11\"\n\n[network]\ngenerateHosts=true\ngenerateResolvConf=true   # Auto-config DNS\n\n[interop]\nenabled=true              # Lancer .exe Windows\nappendWindowsPath=true    # PATH Windows dans WSL\n\n[user]\ndefault=alice             # User par défaut\n\n# Appliquer changements:\nwsl --shutdown\nwsl\n\n# Config globale WSL2 (C:\\Users\\VotreNom\\.wslconfig):\n[wsl2]\nmemory=8GB                # Limiter RAM (défaut: 50% RAM PC)\nprocessors=4              # Limiter CPU cores\nswap=2GB\nlocalhostForwarding=true  # Forwarding ports\n\n# Appliquer:\nwsl --shutdown"
            },
            {
                "title": "Développement avec WSL",
                "code": "# Git (utilisez version Linux!):\nsudo apt install git -y\ngit config --global user.name \"Votre Nom\"\ngit config --global user.email \"vous@email.com\"\n\n# Node.js/npm (via nvm):\ncurl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash\nsource ~/.bashrc\nnvm install --lts\nnode --version\n\n# Python (préinstallé):\npython3 --version\nsudo apt install python3-pip -y\n\n# Docker (via Docker Desktop Windows):\n# Installer Docker Desktop → Settings → Use WSL2 engine\ndocker --version          # Depuis WSL\ndocker ps\n\n# VS Code Remote-WSL:\n# 1. Installer extension \"Remote - WSL\"\n# 2. Depuis WSL: code .\n# 3. VS Code s'ouvre en mode WSL\n# Terminal intégré = bash WSL\n\n# SSH keys:\nssh-keygen -t ed25519\n# Clés dans ~/.ssh/ (Linux)\n# Réutilisables pour git/GitHub"
            },
            {
                "title": "Troubleshooting WSL",
                "code": "# WSL ne démarre pas:\nwsl --shutdown\nwsl\n\n# Reset distro (⚠️ perte données!):\nwsl --unregister Ubuntu\nwsl --install -d Ubuntu\n\n# Erreur réseau/DNS:\nsudo rm /etc/resolv.conf\nsudo bash -c 'echo \"nameserver 8.8.8.8\" > /etc/resolv.conf'\nwsl --shutdown\nwsl\n\n# Compact disque virtuel (libérer espace):\nwsl --shutdown\n# PowerShell admin:\noptimize-vhd -Path C:\\Users\\VotreNom\\AppData\\Local\\Packages\\CanonicalGroupLimited...\\LocalState\\ext4.vhdx -Mode full\n# Ou:\nDiskpart\nselect vdisk file=\"C:\\Users\\...\\ext4.vhdx\"\nattach vdisk readonly\ncompact vdisk\ndetach vdisk\n\n# Logs WSL:\nwsl --debug-shell\ndmesg | tail\njournalctl -xe\n\n# Version WSL:\nwsl --version\nwsl --update              # Mettre à jour WSL"
            },
            {
                "info": "💡 WSL2 > WSL1: Performance I/O 20× meilleure, vrai kernel Linux, Docker natif. Migrer: wsl --set-version Ubuntu 2"
            },
            {
                "warning": "⚠️ Travaillez dans /home/user/ (rapide), PAS /mnt/c/ (lent)! Git clone dans ~/, pas C:\\. Performance I/O cruciale."
            }
        ]
    },

    "linux_troubleshoot": {
        "title": "🔧 Dépannage Linux Général",
        "sections": [
            {
                "title": "Méthodologie de Dépannage",
                "bullets": [
                    "1. Reproduire le problème (fiable?)",
                    "2. Lire messages d'erreur COMPLETS (ne pas ignorer!)",
                    "3. Consulter logs (journalctl, /var/log/)",
                    "4. Isoler la cause (hardware? software? config?)",
                    "5. Chercher erreur exacte (Google, forums, Arch Wiki)",
                    "6. Tester solutions une par une",
                    "7. Documenter solution (pour futur)"
                ]
            },
            {
                "title": "Système Ne Boot Pas",
                "code": "# Boot en mode recovery (GRUB):\n# Au boot GRUB, appuyer 'e' sur entrée\n# Ajouter à ligne linux: systemd.unit=rescue.target\n# Ctrl+X pour booter\n\n# Ou emergency mode:\nsystemd.unit=emergency.target\n\n# Depuis live USB:\n# 1. Booter sur USB\n# 2. Monter partition système:\nsudo mount /dev/sda2 /mnt\nsudo mount /dev/sda1 /mnt/boot/efi  # Si UEFI\n\n# 3. Chroot:\nsudo arch-chroot /mnt    # Arch/Manjaro\n# Ou:\nsudo mount --bind /dev /mnt/dev\nsudo mount --bind /proc /mnt/proc\nsudo mount --bind /sys /mnt/sys\nsudo chroot /mnt /bin/bash\n\n# 4. Réparer (voir guides grub/boot)\n\n# Vérifier filesystem:\nsudo fsck /dev/sda2\n# ⚠️ Partition doit être DÉMONTÉE!"
            },
            {
                "title": "Système Lent / Freeze",
                "code": "# Identifier processus gourmand:\ntop                       # CPU\nhtop                      # Mieux\nps aux --sort=-%cpu | head -10  # Top 10 CPU\nps aux --sort=-%mem | head -10  # Top 10 RAM\n\n# I/O disk (iotop):\nsudo apt install iotop -y\nsudo iotop\n\n# Vérifier RAM:\nfree -h\n# Si swap utilisé massivement = manque RAM\n\n# Vérifier disque plein:\ndf -h\ndu -sh /* | sort -rh | head -10  # 10 plus gros dossiers racine\n\n# Kernel logs (crashes):\ndmesg | tail -50\njournalctl -p err -b      # Erreurs boot actuel\n\n# Services failed:\nsystemctl --failed\n\n# Température CPU (lm-sensors):\nsudo apt install lm-sensors -y\nsensors\n# >80°C = surchauffe possible\n\n# Tuer processus bloqué:\nsudo killall -9 nom_processus\n# Ou via htop: F9 (SIGKILL)\n\n# Redémarrer interface graphique:\nsudo systemctl restart display-manager\n# Ou:\nsudo systemctl restart gdm    # GNOME\nsudo systemctl restart sddm   # KDE\nsudo systemctl restart lightdm  # XFCE/LXDE"
            },
            {
                "title": "Réseau Ne Fonctionne Pas",
                "code": "# Vérifier interface UP:\nip link show\n# DOWN? Activer:\nsudo ip link set eth0 up\n\n# Obtenir IP (DHCP):\nsudo dhclient eth0\n# Ou (NetworkManager):\nsudo systemctl restart NetworkManager\nnmcli con up \"Wired connection 1\"\n\n# Tester connectivité:\nping -c 4 8.8.8.8         # Test IP (pas DNS)\nping -c 4 google.com      # Test DNS\n\n# Pas de ping 8.8.8.8? Vérifier route:\nip route show\n# Pas de default via? Ajouter gateway:\nsudo ip route add default via 192.168.1.1\n\n# DNS ne résout pas? Vérifier /etc/resolv.conf:\ncat /etc/resolv.conf\n# Vide/mauvais? Ajouter temporairement:\necho \"nameserver 8.8.8.8\" | sudo tee /etc/resolv.conf\n\n# NetworkManager problème:\nsudo systemctl status NetworkManager\nsudo systemctl restart NetworkManager\n\n# Reset complet réseau:\nsudo systemctl stop NetworkManager\nsudo ip addr flush dev eth0\nsudo ip link set eth0 down\nsudo ip link set eth0 up\nsudo systemctl start NetworkManager\n\n# Drivers WiFi manquants:\nlspci | grep -i network   # Identifier carte\nlsmod | grep iwl          # Modules chargés?\nsudo modprobe iwlwifi     # Charger module Intel WiFi\n\n# Logs réseau:\njournalctl -u NetworkManager -f"
            },
            {
                "title": "Son Ne Fonctionne Pas",
                "code": "# Vérifier PulseAudio/Pipewire:\nsystemctl --user status pulseaudio\nsystemctl --user status pipewire\n\n# Restart audio:\nsystemctl --user restart pulseaudio\n# Ou:\npulseaudio -k             # Kill\npulseaudio --start        # Redémarre auto\n\n# Mixer audio (alsamixer):\nalsamixer\n# Flèches: naviguer\n# M: unmute (00 visible si muted)\n# Échap: quitter\n\n# Lister devices audio:\naplay -l                  # Playback\narecord -l                # Recording\n\n# Tester son:\nspeaker-test -c 2         # Stereo test\n# Ctrl+C pour arrêter\n\n# Sélectionner device (pavucontrol):\nsudo apt install pavucontrol -y\npavucontrol\n# Onglet Configuration: choisir profile\n\n# Reinstaller PulseAudio:\nsudo apt remove --purge pulseaudio\nsudo apt install pulseaudio\nsudo reboot\n\n# Logs audio:\njournalctl --user -u pulseaudio"
            },
            {
                "title": "Paquets Cassés / Dépendances",
                "code": "# APT (Debian/Ubuntu):\nsudo apt --fix-broken install\nsudo apt --fix-missing update\nsudo dpkg --configure -a\nsudo apt autoremove\n\n# Forcer réinstallation paquet:\nsudo apt install --reinstall nom_paquet\n\n# Supprimer paquet bloquant:\nsudo dpkg --remove --force-remove-reinstreq nom_paquet\n\n# Reset cache APT:\nsudo rm -rf /var/lib/apt/lists/*\nsudo apt clean\nsudo apt update\n\n# DNF (Fedora):\nsudo dnf check\nsudo dnf distro-sync\n\n# Pacman (Arch):\nsudo pacman -Syyu         # Full system upgrade\nsudo pacman -Scc          # Clean cache\nsudo pacman-key --refresh-keys  # Si erreur signatures"
            },
            {
                "title": "Interface Graphique Ne Démarre Pas",
                "code": "# Basculer en TTY (Ctrl+Alt+F2)\n# Login en CLI\n\n# Vérifier display manager:\nsudo systemctl status gdm         # GNOME\nsudo systemctl status sddm        # KDE\nsudo systemctl status lightdm     # XFCE\n\n# Failed? Voir logs:\njournalctl -u gdm -b\n\n# Tenter redémarrer:\nsudo systemctl restart gdm\n\n# Reconfigurer:\nsudo dpkg-reconfigure gdm\n\n# Réinstaller:\nsudo apt install --reinstall gdm3\n\n# Vérifier serveur X:\nstartx                    # Test manuel\n# Erreurs affichées?\n\n# Drivers GPU (NVIDIA souvent coupable):\nubuntu-drivers devices\nsudo ubuntu-drivers autoinstall\nsudo reboot\n\n# Retour Ctrl+Alt+F1 (ou F7) pour GUI\n\n# Target graphique désactivé?\nsystemctl get-default\n# multi-user.target? Changer:\nsudo systemctl set-default graphical.target\nsudo reboot"
            },
            {
                "title": "Outils Diagnostic Essentiels",
                "code": "# Infos système:\nneofetch                  # Overview stylé\ninxi -F                   # Détails complets hardware\n\n# Hardware:\nlspci                     # Devices PCI\nlsusb                     # Devices USB\nlsblk                     # Disques/partitions\nlshw                      # Hardware complet\n\n# Logs:\njournalctl -xe            # Récents + explications\njournalctl -b -p err      # Erreurs boot actuel\ndmesg | tail -50          # Kernel messages\ncat /var/log/syslog | tail -100  # Syslog\n\n# Performance:\nvmstat 1                  # Stats CPU/RAM/IO par seconde\niostat -x 1               # I/O disque\nsar -u 1 10               # CPU stats (sysstat)\n\n# Réseau:\nss -tuln                  # Ports listening\nip addr                   # IPs\nip route                  # Routes\n\n# Processus:\nps auxf                   # Tree\npstree -p                 # Tree avec PID\nlsof -i :80               # Quel process sur port 80?"
            },
            {
                "info": "💡 Avant modifications système: Backup! sudo timeshift --create (snapshots), rsync -av /home/ /backup/, ou dd si=/dev/sda of=backup.img"
            },
            {
                "warning": "⚠️ 'sudo rm -rf' sans vérifier = destruction garantie. TOUJOURS double-check chemins. Pas de corbeille en CLI!"
            }
        ]
    },

    "linux_gaming": {
        "title": "🎮 Gaming sur Linux (2024)",
        "sections": [
            {
                "title": "Gaming Linux - État en 2024",
                "content": "Grâce à Proton (Wine + DXVK + optimisations Valve), 80%+ jeux Windows fonctionnent sur Linux. Steam Deck (Arch Linux) a propulsé compatibilité. Jeux natifs Linux: minorité mais croissants. Anti-cheats kernel mode (Valorant, Destiny 2) = bloqués. Gaming compétitif problématique, solo/coop excellent."
            },
            {
                "title": "Proton - Couche Compatibilité Windows",
                "bullets": [
                    "Proton = Wine + DXVK + VKD3D + optimisations Valve",
                    "• Intégré Steam (activer dans paramètres)",
                    "• Traduit DirectX → Vulkan en temps réel",
                    "• Performance souvent équivalente Windows (parfois meilleure!)",
                    "",
                    "ProtonDB - Base compatibilité:",
                    "• protondb.com - Notes communauté par jeu",
                    "• Platine/Or = fonctionne parfaitement",
                    "• Argent = tweaks mineurs requis",
                    "• Bronze/Borked = problèmes majeurs"
                ]
            },
            {
                "title": "Steam - Configuration Gaming",
                "code": "# Installer Steam:\nsudo apt install steam -y         # Ubuntu/Debian\nsudo dnf install steam -y         # Fedora (RPM Fusion requis)\nsudo pacman -S steam -y           # Arch\n\n# Activer Proton pour TOUS jeux (Steam):\n# Steam → Settings → Compatibility\n# ✓ Enable Steam Play for all other titles\n# Sélectionner: Proton Experimental (ou dernière version stable)\n\n# Forcer Proton version spécifique par jeu:\n# Bibliothèque → Clic droit jeu → Propriétés → Compatibility\n# Force use of: Proton 8.0, GE-Proton, etc.\n\n# Variables lancement (améliorer perf/compatibilité):\n# Propriétés jeu → Launch Options:\n\n# Force Vulkan (si DirectX problème):\nDXVK_HUD=fps %command%\n\n# Gamescope (compositeur gaming Valve):\ngamescope -W 1920 -H 1080 -f -- %command%\n\n# AMD GPU (ACO compiler - meilleure perf):\nRADV_PERFTEST=aco %command%\n\n# NVIDIA (force Vulkan layers):\n__GL_SHADER_DISK_CACHE=1 __GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1 %command%\n\n# Logs Proton (debug):\nPROTON_LOG=1 %command%\n# Logs dans: ~/.steam/steam/steamapps/compatdata/<game_id>/proton.log"
            },
            {
                "title": "Lutris - Lanceur Jeux Universel",
                "code": "# Installer Lutris:\nsudo add-apt-repository ppa:lutris-team/lutris -y  # Ubuntu\nsudo apt update && sudo apt install lutris -y\n\n# Fedora:\nsudo dnf install lutris -y\n\n# Arch:\nsudo pacman -S lutris -y\n\n# Lutris permet installer:\n# - Jeux Epic Games Store\n# - Battle.net (Blizzard)\n# - GOG\n# - EA App\n# - Ubisoft Connect\n# - Jeux standalone (EXE Windows)\n\n# Installer jeu depuis Lutris:\n# 1. Lutris.net → Games → Chercher jeu\n# 2. Cliquer \"Install\"\n# 3. Script auto-installe Wine + dépendances + jeu\n\n# Wine versions dans Lutris:\n# Lutris → ☰ → Manage runners → Wine\n# Installer: wine-ge, wine-staging, proton-ge\n\n# Exemples jeux populaires via Lutris:\n# - League of Legends (fonctionne!)\n# - Overwatch 2 (via Battle.net)\n# - Cyberpunk 2077 (GOG)\n# - Diablo IV (Battle.net)"
            },
            {
                "title": "Drivers GPU - Gaming Performance",
                "code": "# NVIDIA (propriétaire recommandé):\n# Ubuntu:\nsudo ubuntu-drivers devices\nsudo ubuntu-drivers autoinstall\nsudo reboot\n\n# Arch:\nsudo pacman -S nvidia nvidia-utils nvidia-settings\n\n# Fedora (RPM Fusion requis):\nsudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda\n\n# Vérifier driver:\nnvidia-smi\nnvidia-settings\n\n# AMD (open-source RADV/Mesa - excellent!):\n# Pré-installé sur distros récentes\n# Vérifier:\nglxinfo | grep \"OpenGL renderer\"\n# Doit afficher: AMD RADV ou AMDGPU\n\n# Mesa récente (PPA Ubuntu):\nsudo add-apt-repository ppa:kisak/kisak-mesa -y\nsudo apt update && sudo apt upgrade -y\n\n# Vulkan:\nsudo apt install mesa-vulkan-drivers vulkan-tools -y  # AMD\nsudo apt install nvidia-vulkan-driver vulkan-tools -y  # NVIDIA\n\n# Tester Vulkan:\nvulkaninfo | grep deviceName\nvkcube  # Cube 3D rotatif\n\n# Intel (intégré):\n# Mesa open-source (pré-installé)\nsudo apt install mesa-vulkan-drivers intel-media-va-driver -y"
            },
            {
                "title": "Heroic Games Launcher - Epic/GOG",
                "code": "# Alternative graphique à Lutris pour Epic/GOG\n\n# Flatpak (recommandé):\nflatpak install flathub com.heroicgameslauncher.hgl -y\nflatpak run com.heroicgameslauncher.hgl\n\n# AppImage:\nwget https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest/download/Heroic.AppImage\nchmod +x Heroic.AppImage\n./Heroic.AppImage\n\n# Features:\n# - Login Epic Games + GOG\n# - Installer/lancer jeux\n# - Proton/Wine intégré\n# - Cloud saves sync\n# - Interface moderne (Electron)"
            },
            {
                "title": "GameMode - Optimisations Runtime",
                "code": "# GameMode (Feral Interactive):\n# Optimise CPU governor, priorité processus, GPU clocks\n\nsudo apt install gamemode -y      # Ubuntu\nsudo dnf install gamemode -y      # Fedora\nsudo pacman -S gamemode -y        # Arch\n\n# Utiliser GameMode:\n# Méthode 1: Préfixe commande\ngamemoderun ./jeu.exe\ngamemoderun %command%  # Steam launch options\n\n# Méthode 2: Mangohud (overlay + gamemode auto)\nmangohud %command%\n\n# Vérifier GameMode actif:\ngamemoded -s\n# Ou pendant jeu:\ngamemoded -t  # Liste processes en gamemode\n\n# Config GameMode:\nsudo nano /etc/gamemode.ini\n\n[general]\nrenice=10\n\n[gpu]\napply_gpu_optimisations=accept\ngpu_device=0\n\n[cpu]\ngov=performance\npin_cores=0-7"
            },
            {
                "title": "MangoHud - Overlay FPS/Stats",
                "code": "# MangoHud = overlay affichant FPS, CPU, GPU, RAM, etc.\n\nsudo apt install mangohud -y\nsudo dnf install mangohud -y\nsudo pacman -S mangohud -y\n\n# Utiliser:\nmangohud ./jeu\nmangohud %command%  # Steam\n\n# Config:\nmkdir -p ~/.config/MangoHud\nnano ~/.config/MangoHud/MangoHud.conf\n\n# Exemple config:\nfps_limit=144\nvsync=0\nfps\nframetime\ngpu_stats\ngpu_temp\ncpu_stats\ncpu_temp\nram\nvram\nposition=top-right\nfont_size=24\n\n# Raccourcis (in-game):\n# Shift_R+F12: Toggle overlay\n# Shift_R+F11: Screenshot stats\n# Shift_R+F10: Toggle logging"
            },
            {
                "title": "Anti-Cheat - Compatibilité",
                "bullets": [
                    "Fonctionnent (userspace):",
                    "• Easy Anti-Cheat (EAC) - Si dev active support Proton",
                    "• BattlEye - Si dev active support Proton",
                    "• VAC (Valve Anti-Cheat) - Natif Linux",
                    "",
                    "Exemples jeux EAC/BattlEye OK:",
                    "• Apex Legends, Dead by Daylight, Elden Ring",
                    "• Lost Ark, New World, War Thunder",
                    "",
                    "NE fonctionnent PAS (kernel mode):",
                    "• Valorant (Vanguard)",
                    "• FACEIT AC",
                    "• Destiny 2",
                    "• Rainbow Six Siege (BattlEye non activé)",
                    "",
                    "Vérifier: areweanticheatyet.com"
                ]
            },
            {
                "info": "💡 ProtonDB + Lutris = 80%+ jeux Windows. Steam Deck verified = garantie fonctionne. Préférez jeux solo/coop, évitez compétitif avec anti-cheat agressif."
            },
            {
                "warning": "⚠️ Dual-boot recommandé si gaming compétitif (Valorant, FACEIT). VM Windows = performance -30%. Cloud gaming (GeForce NOW, Xbox Cloud) = alternative."
            }
        ]
    },

    "linux_users": {
        "title": "👤 Gestion Utilisateurs & Groupes",
        "sections": [
            {
                "title": "Utilisateurs Linux - Concepts",
                "content": "Chaque utilisateur Linux a: UID (User ID numérique), home directory (/home/username), shell par défaut (bash, zsh...), appartenance à groupes. Root (UID 0) = administrateur tout-puissant. Comptes système (UID < 1000) pour services. Utilisateurs normaux (UID ≥ 1000)."
            },
            {
                "title": "Créer Utilisateur",
                "code": "# Méthode complète (useradd):\nsudo useradd -m -s /bin/bash -c \"Jean Dupont\" -G sudo,audio,video jean\n# -m: Créer home directory\n# -s: Shell par défaut\n# -c: Commentaire (nom complet)\n# -G: Groupes secondaires\n\n# Définir mot de passe:\nsudo passwd jean\n# Entre nouveau mot de passe...\n\n# Méthode interactive (adduser - Debian/Ubuntu):\nsudo adduser jean\n# Pose questions: nom, tél, bureau, etc.\n\n# Créer user système (pour service):\nsudo useradd -r -s /usr/sbin/nologin -d /var/lib/monservice monservice\n# -r: Système (UID < 1000)\n# -s /usr/sbin/nologin: Pas de login shell\n\n# Vérifier création:\nid jean\n# uid=1001(jean) gid=1001(jean) groups=1001(jean),27(sudo)...\n\ncat /etc/passwd | grep jean\n# jean:x:1001:1001:Jean Dupont:/home/jean:/bin/bash"
            },
            {
                "title": "Modifier Utilisateur",
                "code": "# Changer shell:\nsudo usermod -s /bin/zsh jean\n\n# Ajouter à groupe (append):\nsudo usermod -aG docker jean\n# -a: Append (IMPORTANT! Sans -a, remplace tous groupes)\n\n# Remplacer groupes:\nsudo usermod -G sudo,audio jean\n# Retire des autres groupes!\n\n# Changer home directory:\nsudo usermod -d /home/nouveau_home -m jean\n# -m: Déplacer contenu ancien → nouveau\n\n# Verrouiller compte (désactiver login):\nsudo usermod -L jean\n# Ou:\nsudo passwd -l jean\n\n# Déverrouiller:\nsudo usermod -U jean\nsudo passwd -u jean\n\n# Renommer user:\nsudo usermod -l nouveau_nom ancien_nom\n# ⚠️ Ne renomme PAS home directory automatiquement!\n\n# Changer UID:\nsudo usermod -u 2000 jean\n# ⚠️ Fichiers existants gardent ancien UID!"
            },
            {
                "title": "Supprimer Utilisateur",
                "code": "# Supprimer user (garder home):\nsudo userdel jean\n\n# Supprimer user + home directory:\nsudo userdel -r jean\n# Supprime /home/jean et mail spool\n\n# Forcer suppression (même si logged in):\nsudo userdel -f jean\n# ⚠️ Peut casser processus en cours!\n\n# Trouver fichiers appartenant à user supprimé:\nsudo find / -user 1001 2>/dev/null\n# 1001 = ancien UID\n\n# Réattribuer fichiers à autre user:\nsudo find / -user 1001 -exec chown alice:alice {} \\;\n\n# Ou supprimer:\nsudo find / -user 1001 -delete"
            },
            {
                "title": "Groupes - Gestion",
                "code": "# Créer groupe:\nsudo groupadd developers\n\n# Créer avec GID spécifique:\nsudo groupadd -g 3000 developers\n\n# Ajouter user à groupe:\nsudo usermod -aG developers jean\n# Ou:\nsudo gpasswd -a jean developers\n\n# Retirer user du groupe:\nsudo gpasswd -d jean developers\n\n# Supprimer groupe:\nsudo groupdel developers\n# ⚠️ Groupe doit être vide (pas de primary group)\n\n# Lister membres groupe:\ngetent group developers\n# developers:x:3000:jean,alice,bob\n\n# Ou:\ngrep developers /etc/group\n\n# Voir groupes d'un user:\ngroups jean\n# jean : jean sudo docker developers\n\nid jean\n# uid=1001(jean) gid=1001(jean) groups=1001(jean),27(sudo),999(docker),3000(developers)"
            },
            {
                "title": "Sudo - Droits Administrateur",
                "code": "# Ajouter user au groupe sudo:\nsudo usermod -aG sudo jean       # Debian/Ubuntu\nsudo usermod -aG wheel jean      # Fedora/RHEL/Arch\n\n# ⚠️ User doit se RE-LOGIN pour appliquer!\n\n# Fichier sudoers (NE JAMAIS ÉDITER DIRECTEMENT!):\nsudo visudo\n# Utilise TOUJOURS visudo (vérifie syntaxe)\n\n# Exemples règles sudoers:\n# Permettre user spécifique:\njean ALL=(ALL:ALL) ALL\n\n# Groupe sudo:\n%sudo ALL=(ALL:ALL) ALL\n\n# Sans mot de passe (DANGEREUX!):\njean ALL=(ALL) NOPASSWD: ALL\n\n# Commandes spécifiques uniquement:\njean ALL=(ALL) /usr/bin/apt, /usr/bin/systemctl\n\n# Fichiers sudoers.d (méthode propre):\nsudo visudo -f /etc/sudoers.d/jean\n# Ajouter: jean ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx\n\n# Tester sudo:\nsudo -l\n# Liste permissions sudo pour user actuel\n\n# Devenir autre user:\nsudo -u alice bash\n# Ou:\nsudo su - alice"
            },
            {
                "title": "su - Switch User",
                "code": "# Devenir root:\nsu -\n# Ou:\nsu - root\n# Demande mot de passe ROOT (pas user actuel)\n\n# Devenir autre user:\nsu - jean\n# Demande mot de passe de jean\n\n# Sans charger environnement:\nsu jean\n# Reste dans dossier actuel, garde variables\n\n# Avec - : Login shell complet\nsu - jean\n# Charge ~/.bashrc, change vers /home/jean\n\n# Exécuter commande en tant que user:\nsu -c \"whoami\" jean\n# Affiche: jean\n\n# sudo vs su:\n# sudo: Demande MOT DE PASSE USER ACTUEL, permissions granulaires\n# su: Demande MOT DE PASSE USER CIBLE (root), tout ou rien"
            },
            {
                "title": "Fichiers Système Utilisateurs",
                "code": "# /etc/passwd - Base données users:\ncat /etc/passwd\n# Format: username:x:UID:GID:comment:home:shell\n# jean:x:1001:1001:Jean Dupont:/home/jean:/bin/bash\n\n# x = Mot de passe dans /etc/shadow\n\n# /etc/shadow - Mots de passe chiffrés:\nsudo cat /etc/shadow\n# Format: username:$encrypted$:last_change:min:max:warn:inactive:expire\n# jean:$6$rounds=5000$...:19000:0:99999:7:::\n\n# Lecture seule ROOT!\n\n# /etc/group - Groupes:\ncat /etc/group\n# Format: groupname:x:GID:members\n# sudo:x:27:jean,alice\n\n# /etc/gshadow - Mots de passe groupes (rarement utilisé):\nsudo cat /etc/gshadow\n\n# /etc/login.defs - Paramètres par défaut:\ncat /etc/login.defs\n# UID_MIN, PASSWORD_MAX_DAYS, etc.\n\n# /etc/skel/ - Template home directory:\nls -la /etc/skel/\n# Copié vers /home/newuser à création"
            },
            {
                "title": "Permissions Fichiers Utilisateur",
                "code": "# Changer propriétaire fichier:\nsudo chown jean fichier.txt\n\n# Changer propriétaire + groupe:\nsudo chown jean:developers fichier.txt\n\n# Récursif (dossiers):\nsudo chown -R jean:developers /var/www/monsite/\n\n# Changer groupe uniquement:\nsudo chgrp developers fichier.txt\n\n# Vérifier propriétaire:\nls -l fichier.txt\n# -rw-r--r-- 1 jean developers 1234 Jan 3 10:00 fichier.txt\n#              ^^^^ ^^^^^^^^^^^\n#            owner   group\n\n# Trouver fichiers d'un user:\nfind /home -user jean\n\n# Trouver fichiers d'un groupe:\nfind /var/www -group developers"
            },
            {
                "info": "💡 TOUJOURS utiliser usermod -aG (append) pour ajouter groupes. Sans -a, REMPLACE tous groupes existants!"
            },
            {
                "warning": "⚠️ Ne jamais éditer /etc/passwd, /etc/shadow, /etc/group directement! Utiliser useradd, usermod, groupadd. Pour sudoers: visudo UNIQUEMENT!"
            },
            {
                "warning": "⚠️ User doit se RE-LOGIN après ajout à groupe (ou: newgrp groupname). Les changements ne s'appliquent PAS à session en cours!"
            }
        ]
    },

    "linux_disk": {
        "title": "💾 Gestion Disques & Partitions",
        "sections": [
            {
                "title": "Concepts Stockage Linux",
                "bullets": [
                    "Disque physique: /dev/sda, /dev/nvme0n1 (NVMe)",
                    "Partitions: /dev/sda1, /dev/sda2, /dev/nvme0n1p1",
                    "• MBR (ancien): Max 4 partitions primaires, 2 To max",
                    "• GPT (moderne): 128 partitions, > 2 To, UEFI requis",
                    "",
                    "Filesystem: ext4, XFS, Btrfs, FAT32, NTFS",
                    "• ext4: Standard Linux, journalisé, fiable",
                    "• Btrfs: Moderne, snapshots, compression",
                    "• XFS: Performance, gros fichiers",
                    "",
                    "Point de montage: Dossier où partition accessible",
                    "• / (root), /home, /boot, /var"
                ]
            },
            {
                "title": "Lister Disques & Partitions",
                "code": "# Méthode simple (lsblk):\nlsblk\n# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS\n# sda      8:0    0 465.8G  0 disk\n# ├─sda1   8:1    0   512M  0 part /boot/efi\n# ├─sda2   8:2    0    16G  0 part [SWAP]\n# └─sda3   8:3    0 449.3G  0 part /\n\n# Détails + UUID:\nlsblk -f\n# Affiche filesystem, label, UUID\n\n# Méthode détaillée (fdisk):\nsudo fdisk -l\n# Liste TOUS disques + partitions + tailles\n\n# Disques uniquement:\nls -l /dev/sd*      # SATA/SAS\nls -l /dev/nvme*    # NVMe SSD\n\n# Espace utilisé/disponible:\ndf -h\n# Filesystem      Size  Used Avail Use% Mounted on\n# /dev/sda3       450G  120G  307G  29% /\n# /dev/sda1       511M   34M  478M   7% /boot/efi\n\n# Espace par dossier:\ndu -sh /*\ndu -sh /home/*      # Par utilisateur\n\n# Trouver gros fichiers:\nsudo du -ah / | sort -rh | head -20\n# 20 plus gros fichiers/dossiers"
            },
            {
                "title": "Créer Partitions (fdisk/parted)",
                "code": "# fdisk (MBR ou GPT - interactif):\nsudo fdisk /dev/sdb\n# Commandes:\n# m: Aide\n# p: Print (afficher partitions)\n# n: Nouvelle partition\n# d: Supprimer partition\n# t: Changer type\n# w: Write (sauvegarder et quitter)\n# q: Quit sans sauver\n\n# Exemple création partition:\n# n → p (primaire) → 1 (numéro) → Enter (début défaut) → +50G (taille)\n# w (sauvegarder)\n\n# parted (GPT recommandé - scriptable):\nsudo parted /dev/sdb\n\n# Commandes parted:\n(parted) print                    # Afficher partitions\n(parted) mklabel gpt              # Créer table GPT (⚠️ EFFACE TOUT!)\n(parted) mkpart primary ext4 0% 50%   # Partition 50% disque\n(parted) mkpart primary ext4 50% 100% # Reste du disque\n(parted) quit\n\n# Ou en une ligne:\nsudo parted /dev/sdb mklabel gpt mkpart primary ext4 0% 100%\n\n# ⚠️ parted applique IMMÉDIATEMENT (pas de confirmation w)"
            },
            {
                "title": "Formater Partitions (mkfs)",
                "code": "# ext4 (recommandé Linux):\nsudo mkfs.ext4 /dev/sdb1\n\n# ext4 avec label:\nsudo mkfs.ext4 -L \"MesDonnees\" /dev/sdb1\n\n# XFS:\nsudo mkfs.xfs /dev/sdb1\n\n# Btrfs:\nsudo mkfs.btrfs /dev/sdb1\n\n# FAT32 (compatible Windows/Mac):\nsudo mkfs.vfat -F 32 /dev/sdb1\n\n# NTFS (Windows):\nsudo mkfs.ntfs /dev/sdb1\n# Ou (ntfs-3g):\nsudo apt install ntfs-3g -y\nsudo mkfs.ntfs -f /dev/sdb1\n\n# ⚠️ mkfs EFFACE toutes données partition!\n\n# Vérifier filesystem:\nsudo blkid /dev/sdb1\n# /dev/sdb1: UUID=\"abc-123...\" TYPE=\"ext4\" LABEL=\"MesDonnees\""
            },
            {
                "title": "Monter Partitions (mount)",
                "code": "# Créer point de montage:\nsudo mkdir -p /mnt/disque\n\n# Monter partition:\nsudo mount /dev/sdb1 /mnt/disque\n\n# Vérifier montage:\nmount | grep sdb1\ndf -h /mnt/disque\n\n# Démonter:\nsudo umount /mnt/disque\n# Ou par device:\nsudo umount /dev/sdb1\n\n# Démonter force (si busy):\nsudo umount -f /mnt/disque\n# Ou lazy (détache, démontera quand possible):\nsudo umount -l /mnt/disque\n\n# Trouver qui utilise partition:\nsudo lsof +D /mnt/disque\n# Ou:\nsudo fuser -vm /mnt/disque\n\n# Tuer processus utilisant:\nsudo fuser -km /mnt/disque\n# ⚠️ Tue processus!\n\n# Montage read-only:\nsudo mount -o ro /dev/sdb1 /mnt/disque\n\n# Montage avec permissions:\nsudo mount -o uid=1000,gid=1000 /dev/sdb1 /mnt/disque"
            },
            {
                "title": "Montage Automatique (/etc/fstab)",
                "code": "# Fichier /etc/fstab: Montages au boot\n\n# Obtenir UUID partition:\nsudo blkid /dev/sdb1\n# UUID=\"abc-123-def-456\"\n\n# Éditer fstab:\nsudo nano /etc/fstab\n\n# Format fstab:\n# <device>  <mount_point>  <type>  <options>  <dump>  <pass>\n\n# Exemples:\n# Par UUID (recommandé - stable même si /dev change):\nUUID=abc-123-def-456  /mnt/disque  ext4  defaults  0  2\n\n# Par label:\nLABEL=MesDonnees  /mnt/disque  ext4  defaults  0  2\n\n# Par device (⚠️ peut changer!):\n/dev/sdb1  /mnt/disque  ext4  defaults  0  2\n\n# NTFS (Windows):\nUUID=abc-123  /mnt/windows  ntfs-3g  defaults,uid=1000,gid=1000  0  0\n\n# Options courantes:\n# defaults: rw,suid,dev,exec,auto,nouser,async\n# noatime: Pas d'update access time (performance)\n# ro: Read-only\n# nofail: Boot même si partition absent (USB)\n\n# Exemple complet:\nUUID=abc-123  /home  ext4  defaults,noatime  0  2\n\n# Tester fstab AVANT reboot:\nsudo mount -a\n# Monte toutes partitions fstab\n# Si erreur → corrigez AVANT reboot!\n\n# Derniers champs:\n# dump: 0=pas backup, 1=backup\n# pass: 0=pas fsck, 1=fsck priority (root), 2=fsck après root"
            },
            {
                "title": "Vérifier & Réparer Filesystem (fsck)",
                "code": "# ⚠️ fsck UNIQUEMENT sur partition DÉMONTÉE!\n\n# Vérifier partition:\nsudo fsck /dev/sdb1\n\n# Auto-réparer (dangereux!):\nsudo fsck -y /dev/sdb1\n# -y: Répond \"yes\" à toutes questions\n\n# ext4 spécifique:\nsudo e2fsck /dev/sdb1\nsudo e2fsck -f /dev/sdb1  # Force (même si clean)\n\n# XFS:\nsudo xfs_repair /dev/sdb1\n\n# Vérifier root partition (au boot):\n# Créer fichier /forcefsck:\nsudo touch /forcefsck\nsudo reboot\n# Au boot, fsck s'exécute puis supprime /forcefsck\n\n# Ou paramètre GRUB:\n# Éditer boot: ajouter fsck.mode=force à ligne linux\n\n# Logs fsck:\nsudo journalctl | grep fsck\n\n# ⚠️ Ne JAMAIS fsck partition montée!\n# Démonter d'abord:\nsudo umount /dev/sdb1\nsudo fsck /dev/sdb1"
            },
            {
                "title": "Redimensionner Partitions",
                "code": "# Réduire/Agrandir ext4:\n\n# 1. Démonter partition:\nsudo umount /dev/sdb1\n\n# 2. Vérifier filesystem:\nsudo e2fsck -f /dev/sdb1\n\n# 3. Réduire filesystem:\nsudo resize2fs /dev/sdb1 50G\n# Réduit filesystem à 50G (⚠️ AVANT réduire partition!)\n\n# 4. Réduire partition (parted):\nsudo parted /dev/sdb\n(parted) resizepart 1 50GB\n(parted) quit\n\n# Agrandir partition + filesystem:\n# 1. Agrandir partition (parted):\nsudo parted /dev/sdb\n(parted) resizepart 1 100GB\n(parted) quit\n\n# 2. Agrandir filesystem:\nsudo resize2fs /dev/sdb1\n# Sans taille: Utilise tout espace partition\n\n# ⚠️ Backup AVANT redimensionner!\n\n# GParted (GUI):\nsudo apt install gparted -y\nsudo gparted\n# Interface graphique, plus sûr pour débutants"
            },
            {
                "title": "LVM - Logical Volume Manager",
                "code": "# LVM = Flexibilité: Redimensionner partitions SANS reboot\n\n# Concepts:\n# PV (Physical Volume): Disque/partition physique\n# VG (Volume Group): Pool de PV\n# LV (Logical Volume): Partition virtuelle dans VG\n\n# Créer LVM:\n# 1. Créer PV:\nsudo pvcreate /dev/sdb1\nsudo pvcreate /dev/sdc1\n\n# 2. Créer VG:\nsudo vgcreate mon_vg /dev/sdb1 /dev/sdc1\n# mon_vg = pool combinant sdb1 + sdc1\n\n# 3. Créer LV:\nsudo lvcreate -L 50G -n home_lv mon_vg\n# Crée volume logique 50G nommé home_lv\n\n# 4. Formater LV:\nsudo mkfs.ext4 /dev/mon_vg/home_lv\n\n# 5. Monter:\nsudo mount /dev/mon_vg/home_lv /home\n\n# Lister LVM:\nsudo pvs     # Physical Volumes\nsudo vgs     # Volume Groups\nsudo lvs     # Logical Volumes\n\n# Agrandir LV:\nsudo lvextend -L +20G /dev/mon_vg/home_lv\nsudo resize2fs /dev/mon_vg/home_lv\n\n# Réduire LV:\nsudo resize2fs /dev/mon_vg/home_lv 30G\nsudo lvreduce -L 30G /dev/mon_vg/home_lv\n\n# Snapshot (backup instantané):\nsudo lvcreate -L 10G -s -n home_snapshot /dev/mon_vg/home_lv\n# Restaurer:\nsudo lvconvert --merge /dev/mon_vg/home_snapshot"
            },
            {
                "title": "RAID Logiciel (mdadm)",
                "code": "# RAID = Redundancy/Performance avec plusieurs disques\n\n# Types RAID:\n# RAID 0: Striping (performance, AUCUNE redondance)\n# RAID 1: Mirroring (redondance, même données 2 disques)\n# RAID 5: Striping + parité (1 disque panne OK, min 3 disques)\n# RAID 10: Mirroring + Striping (4 disques min)\n\n# Créer RAID 1 (mirroring):\nsudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1\n\n# Vérifier RAID:\ncat /proc/mdstat\nsudo mdadm --detail /dev/md0\n\n# Formater RAID:\nsudo mkfs.ext4 /dev/md0\n\n# Monter:\nsudo mount /dev/md0 /mnt/raid\n\n# Sauvegarder config RAID:\nsudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf\nsudo update-initramfs -u\n\n# Remplacer disque défaillant:\n# 1. Marquer failed:\nsudo mdadm --manage /dev/md0 --fail /dev/sdb1\n\n# 2. Retirer:\nsudo mdadm --manage /dev/md0 --remove /dev/sdb1\n\n# 3. Ajouter nouveau:\nsudo mdadm --manage /dev/md0 --add /dev/sdd1\n# Rebuild auto\n\n# Surveiller:\nsudo mdadm --monitor --scan --daemonise"
            },
            {
                "info": "💡 UUID stable entre reboots (vs /dev/sdb qui peut changer). Toujours utiliser UUID dans /etc/fstab!"
            },
            {
                "warning": "⚠️ Backup AVANT partitionner/formater/redimensionner! fdisk/parted ne demandent PAS confirmation. mkfs EFFACE TOUT!"
            },
            {
                "warning": "⚠️ fsck UNIQUEMENT sur partition DÉMONTÉE! Sur partition montée = corruption garantie. Root partition: fsck au boot via /forcefsck."
            }
        ]
    },

    "linux_backup": {
        "title": "💼 Sauvegardes & Restauration",
        "sections": [
            {
                "title": "Stratégie Sauvegarde 3-2-1",
                "bullets": [
                    "Règle 3-2-1 (recommandée):",
                    "• 3 copies données (1 originale + 2 backups)",
                    "• 2 supports différents (disque local + NAS/cloud)",
                    "• 1 copie hors-site (cloud, autre location)",
                    "",
                    "Fréquence recommandée:",
                    "• Données critiques: Quotidien (automatisé)",
                    "• Système: Avant maj majeures (snapshot)",
                    "• Home: Hebdomadaire minimum",
                    "",
                    "Test restauration: Au moins 1× par trimestre!"
                ]
            },
            {
                "title": "rsync - Synchronisation Incrémentale",
                "code": "# rsync = Outil puissant, copie seulement fichiers modifiés\n\n# Backup simple:\nrsync -av /home/user/ /backup/home/\n# -a: Archive (préserve permissions, dates, liens)\n# -v: Verbose (affiche fichiers)\n\n# Options recommandées:\nrsync -avh --progress /home/user/ /backup/home/\n# -h: Human-readable (tailles)\n# --progress: Barre progression\n\n# Delete (synchronisation exacte):\nrsync -av --delete /source/ /destination/\n# ⚠️ Supprime fichiers dans destination absents de source\n\n# Dry-run (test sans copier):\nrsync -avn --delete /source/ /destination/\n# -n: Dry-run (simule)\n\n# Exclure fichiers:\nrsync -av --exclude='*.tmp' --exclude='cache/' /home/user/ /backup/\n\n# Backup via SSH:\nrsync -avz -e ssh /home/user/ user@serveur:/backup/home/\n# -z: Compression (réseau)\n\n# Bandwidth limit:\nrsync -av --bwlimit=1000 /source/ /destination/\n# 1000 KB/s max\n\n# Snapshot-style backup (hard links):\nrsync -av --link-dest=/backup/previous/ /home/user/ /backup/current/\n# Fichiers identiques = hard links (économise espace)"
            },
            {
                "title": "tar - Archives Complètes",
                "code": "# Créer archive TAR:\ntar -cvf backup.tar /home/user/\n# -c: Create\n# -v: Verbose\n# -f: File\n\n# Compression gzip:\ntar -czvf backup.tar.gz /home/user/\n# -z: Gzip\n\n# Compression bzip2 (meilleure, plus lente):\ntar -cjvf backup.tar.bz2 /home/user/\n# -j: Bzip2\n\n# Compression xz (meilleure encore):\ntar -cJvf backup.tar.xz /home/user/\n# -J: Xz\n\n# Exclure dossiers:\ntar -czvf backup.tar.gz /home/user/ --exclude='/home/user/Downloads' --exclude='*.tmp'\n\n# Extraire archive:\ntar -xzvf backup.tar.gz\n# -x: Extract\n\n# Extraire vers dossier spécifique:\ntar -xzvf backup.tar.gz -C /restore/\n\n# Lister contenu sans extraire:\ntar -tzvf backup.tar.gz\n# -t: List\n\n# Extraire fichier spécifique:\ntar -xzvf backup.tar.gz home/user/documents/important.txt\n\n# Backup système complet:\nsudo tar -czvf /backup/system_$(date +%Y%m%d).tar.gz \\\n  --exclude=/proc \\\n  --exclude=/sys \\\n  --exclude=/dev \\\n  --exclude=/run \\\n  --exclude=/mnt \\\n  --exclude=/media \\\n  --exclude=/tmp \\\n  --exclude=/backup \\\n  /\n# ⚠️ Exclure filesystems virtuels essentiels!"
            },
            {
                "title": "Timeshift - Snapshots Système",
                "code": "# Timeshift = Time Machine pour Linux (snapshots Btrfs/rsync)\n\n# Installer:\nsudo apt install timeshift -y      # Ubuntu/Debian\nsudo dnf install timeshift -y      # Fedora\nsudo pacman -S timeshift -y        # Arch\n\n# GUI:\nsudo timeshift-gtk\n\n# CLI - Créer snapshot:\nsudo timeshift --create --comments \"Avant maj système\"\n\n# Lister snapshots:\nsudo timeshift --list\n\n# Restaurer snapshot:\nsudo timeshift --restore --snapshot '2024-01-03_10-00-01'\n# ⚠️ Reboot requis après restore\n\n# Supprimer snapshot:\nsudo timeshift --delete --snapshot '2024-01-03_10-00-01'\n\n# Configuration:\nsudo timeshift --snapshot-device /dev/sda2\nsudo timeshift --schedule daily  # daily, weekly, monthly\n\n# Mode Btrfs (recommandé si filesystem Btrfs):\n# Snapshots instantanés, peu d'espace\n# Setup Timeshift: Type → BTRFS\n\n# Mode rsync:\n# Fonctionne sur ext4/XFS\n# Setup Timeshift: Type → RSYNC\n\n# Exclure dossiers:\n# Settings → Filters → Exclude:\n# /home/*/.cache\n# /var/tmp\n# /var/cache"
            },
            {
                "title": "Borg Backup - Déduplication",
                "code": "# Borg = Backup incrémental avec déduplication + chiffrement\n\n# Installer:\nsudo apt install borgbackup -y\nsudo dnf install borgbackup -y\nsudo pacman -S borg -y\n\n# Créer repo borg:\nborg init --encryption=repokey /backup/borg-repo\n# Demande passphrase (GARDEZ PRÉCIEUSEMENT!)\n\n# Créer backup:\nborg create /backup/borg-repo::backup-{now} /home/user/\n# {now} = timestamp auto\n\n# Avec exclusions:\nborg create /backup/borg-repo::backup-{now} /home/user/ \\\n  --exclude '*/cache/*' \\\n  --exclude '*.tmp'\n\n# Lister backups:\nborg list /backup/borg-repo\n\n# Lister fichiers dans backup:\nborg list /backup/borg-repo::backup-2024-01-03T10:00:00\n\n# Restaurer backup:\nborg extract /backup/borg-repo::backup-2024-01-03T10:00:00\n# Extrait dans dossier actuel\n\n# Monter backup (browse):\nmkdir /mnt/borg\nborg mount /backup/borg-repo::backup-2024-01-03T10:00:00 /mnt/borg\n# Parcourir comme filesystem normal\nborg umount /mnt/borg\n\n# Vérifier intégrité:\nborg check /backup/borg-repo\n\n# Pruner (supprimer anciens):\nborg prune /backup/borg-repo \\\n  --keep-daily=7 \\\n  --keep-weekly=4 \\\n  --keep-monthly=6\n# Garde: 7 daily, 4 weekly, 6 monthly\n\n# Stats repo:\nborg info /backup/borg-repo\n# Affiche déduplication, compression\n\n# Backup automatique (cron):\ncrontab -e\n# Ajouter:\n0 2 * * * borg create /backup/borg-repo::{now} /home/user/ && borg prune /backup/borg-repo --keep-daily=7"
            },
            {
                "title": "dd - Clonage Disque Complet",
                "code": "# dd = Copie bit-à-bit (disque entier ou partition)\n\n# Cloner disque:\nsudo dd if=/dev/sda of=/dev/sdb bs=64K status=progress\n# if: Input (source)\n# of: Output (destination)\n# bs: Block size (64K = bon compromis)\n# status=progress: Affiche progression\n\n# ⚠️ Destination ÉCRASÉE complètement!\n# Vérifier DEUX FOIS if/of!\n\n# Backup disque vers image:\nsudo dd if=/dev/sda of=/backup/disk.img bs=64K status=progress\n\n# Compresser image (économiser espace):\nsudo dd if=/dev/sda bs=64K status=progress | gzip -c > /backup/disk.img.gz\n\n# Restaurer image:\nsudo gzip -dc /backup/disk.img.gz | dd of=/dev/sda bs=64K status=progress\n\n# Cloner partition:\nsudo dd if=/dev/sda1 of=/dev/sdb1 bs=64K status=progress\n\n# Backup MBR (512 octets):\nsudo dd if=/dev/sda of=/backup/mbr.img bs=512 count=1\n\n# Restaurer MBR:\nsudo dd if=/backup/mbr.img of=/dev/sda bs=512 count=1\n\n# Effacer disque (zéros):\nsudo dd if=/dev/zero of=/dev/sda bs=1M status=progress\n# ⚠️ DESTRUCTION COMPLÈTE!\n\n# Effacer aléatoire (plus sécurisé):\nsudo dd if=/dev/urandom of=/dev/sda bs=1M status=progress\n\n# ⚠️ dd = \"Disk Destroyer\" si mauvais paramètres!"
            },
            {
                "title": "Clonezilla - Clonage GUI",
                "code": "# Clonezilla = Alternative GUI à dd, plus sûr\n\n# Télécharger ISO:\n# https://clonezilla.org/downloads.php\n\n# Créer USB bootable:\nsudo dd if=clonezilla.iso of=/dev/sdb bs=4M status=progress\n# Ou Ventoy/Rufus sous Windows\n\n# Booter sur USB Clonezilla:\n# Mode: device-image (disque → image)\n# Ou: device-device (clonage direct)\n\n# Options recommandées:\n# - Beginner mode\n# - savedisk (sauvegarder disque)\n# - Choisir source/destination\n# - Vérifier image après création\n\n# Avantages vs dd:\n# - Interface guidée\n# - Saute blocs vides (plus rapide)\n# - Compression intégrée\n# - Vérification intégrité\n# - Redimensionnement partition possible\n\n# CLI Clonezilla (automatisation):\n# /usr/sbin/ocs-sr -q2 -c -j2 -z1p -i 4096 -sfsck -senc -p true savedisk nom_image sda\n# Voir doc: man ocs-sr"
            },
            {
                "title": "Cloud Backup - rclone",
                "code": "# rclone = rsync pour cloud (Google Drive, Dropbox, S3, etc.)\n\n# Installer:\nsudo apt install rclone -y\nsudo dnf install rclone -y\nsudo pacman -S rclone -y\n\n# Configurer remote:\nrclone config\n# Suivre wizard interactif:\n# n) New remote\n# name> gdrive\n# Storage> drive (Google Drive)\n# Suivre auth OAuth\n\n# Lister remotes configurés:\nrclone listremotes\n\n# Lister fichiers remote:\nrclone ls gdrive:\nrclone lsd gdrive:  # Dossiers uniquement\n\n# Upload fichier:\nrclone copy /home/user/documents/ gdrive:Backup/\n\n# Sync (bidirectionnel):\nrclone sync /home/user/documents/ gdrive:Backup/\n# ⚠️ Supprime fichiers dans destination absents de source\n\n# Dry-run:\nrclone sync /source/ gdrive:Backup/ --dry-run -vv\n\n# Chiffrement (crypte avant upload):\nrclone config\n# n) New remote\n# name> gdrive-crypt\n# Storage> crypt\n# Remote> gdrive:Backup/encrypted\n# Password...\n\n# Upload chiffré:\nrclone copy /home/user/private/ gdrive-crypt:\n\n# Mount cloud comme filesystem:\nmkdir ~/gdrive\nrclone mount gdrive: ~/gdrive --daemon\n# Accès comme dossier local\n\n# Umount:\nfusermount -u ~/gdrive\n\n# Backup automatique (cron):\ncrontab -e\n# 0 3 * * * rclone sync /home/user/documents/ gdrive:Backup/ >> /var/log/rclone.log 2>&1"
            },
            {
                "title": "Script Backup Automatisé",
                "code": "#!/bin/bash\n# /usr/local/bin/backup.sh\n\nBACKUP_DIR=\"/backup\"\nSOURCE=\"/home/user\"\nDATE=$(date +%Y%m%d_%H%M%S)\nLOGFILE=\"/var/log/backup.log\"\n\necho \"[$(date)] Début backup\" >> $LOGFILE\n\n# Créer dossier backup si inexistant\nmkdir -p $BACKUP_DIR\n\n# Rsync incrémental\nrsync -avh --delete \\\n  --exclude='.cache' \\\n  --exclude='Downloads' \\\n  --exclude='*.tmp' \\\n  $SOURCE/ $BACKUP_DIR/latest/ >> $LOGFILE 2>&1\n\nif [ $? -eq 0 ]; then\n    echo \"[$(date)] Backup réussi\" >> $LOGFILE\n    \n    # Archive hebdomadaire\n    if [ $(date +%u) -eq 7 ]; then  # Dimanche\n        tar -czf $BACKUP_DIR/weekly_$DATE.tar.gz $BACKUP_DIR/latest/\n        echo \"[$(date)] Archive hebdo créée\" >> $LOGFILE\n    fi\n    \n    # Nettoyer archives >30j\n    find $BACKUP_DIR -name \"weekly_*.tar.gz\" -mtime +30 -delete\nelse\n    echo \"[$(date)] ERREUR backup!\" >> $LOGFILE\n    exit 1\nfi\n\necho \"[$(date)] Fin backup\" >> $LOGFILE\n\n# Rendre exécutable:\n# sudo chmod +x /usr/local/bin/backup.sh\n\n# Cron (tous les jours 2h):\n# crontab -e\n# 0 2 * * * /usr/local/bin/backup.sh"
            },
            {
                "info": "💡 Testez TOUJOURS restauration! Backup non testé = pas de backup. Simulez perte données 1× par trimestre minimum."
            },
            {
                "warning": "⚠️ dd = AUCUNE confirmation! Inverser if/of = destruction garantie. TRIPLE-CHECK avant lancer! Préférez Clonezilla si débutant."
            },
            {
                "warning": "⚠️ Chiffrez backups contenant données sensibles! Borg/rclone crypt. Passphrase perdue = backup irrécupérable, sauvegardez-la!"
            }
        ]
    },

    "linux_security": {
        "title": "🔒 Sécurité & Durcissement Système",
        "sections": [
            {
                "title": "Principes Sécurité Linux",
                "bullets": [
                    "Moindre privilège: User normal par défaut, sudo uniquement si nécessaire",
                    "Mises à jour régulières: Failles corrigées rapidement",
                    "Firewall actif: ufw/iptables bloquent ports inutiles",
                    "Services minimaux: Désactiver services non utilisés",
                    "Logs surveillance: Détecter activité suspecte",
                    "Chiffrement: Disque (LUKS), réseau (SSH), backup",
                    "Authentification forte: Clés SSH, 2FA si possible"
                ]
            },
            {
                "title": "Mises à Jour Sécurité",
                "code": "# Debian/Ubuntu - Mises à jour automatiques:\nsudo apt install unattended-upgrades -y\nsudo dpkg-reconfigure -plow unattended-upgrades\n# Active auto-updates sécurité\n\n# Config /etc/apt/apt.conf.d/50unattended-upgrades:\n# Décommenter:\n// \"${distro_id}:${distro_codename}-security\";\n\n# Vérifier updates disponibles:\nsudo apt update\napt list --upgradable\n\n# Installer updates sécurité uniquement:\nsudo apt upgrade\n\n# Full upgrade (kernel, etc.):\nsudo apt full-upgrade\n\n# Fedora - Updates auto:\nsudo dnf install dnf-automatic -y\nsudo systemctl enable --now dnf-automatic.timer\n\n# Arch - Updates manuels (TOUJOURS!):\nsudo pacman -Syu\n# ⚠️ Lire Arch News AVANT update!\n\n# Vérifier CVE système:\nsudo apt install debsecan -y  # Debian\ndebsecan --suite bookworm --format detail\n\n# Ubuntu:\nubuntu-security-status"
            },
            {
                "title": "Firewall - ufw (Simple)",
                "code": "# ufw = Uncomplicated Firewall (frontend iptables)\n\n# Installer:\nsudo apt install ufw -y\n\n# Politique par défaut (RECOMMANDÉ):\nsudo ufw default deny incoming\nsudo ufw default allow outgoing\n\n# Autoriser SSH (AVANT activer firewall!):\nsudo ufw allow ssh\n# Ou port spécifique:\nsudo ufw allow 22/tcp\n\n# Autoriser HTTP/HTTPS:\nsudo ufw allow 80/tcp\nsudo ufw allow 443/tcp\n# Ou:\nsudo ufw allow 'Apache Full'\n\n# Autoriser depuis IP spécifique:\nsudo ufw allow from 192.168.1.100\nsudo ufw allow from 192.168.1.0/24 to any port 22\n\n# Activer firewall:\nsudo ufw enable\n\n# Status:\nsudo ufw status verbose\nsudo ufw status numbered  # Avec numéros règles\n\n# Supprimer règle:\nsudo ufw delete allow 80/tcp\n# Ou par numéro:\nsudo ufw delete 3\n\n# Désactiver firewall:\nsudo ufw disable\n\n# Reset (supprimer toutes règles):\nsudo ufw reset\n\n# Logs:\nsudo ufw logging on\nsudo tail -f /var/log/ufw.log"
            },
            {
                "title": "fail2ban - Protection Brute-Force",
                "code": "# fail2ban = Ban IPs après X échecs login\n\n# Installer:\nsudo apt install fail2ban -y\n\n# Ne JAMAIS éditer /etc/fail2ban/jail.conf!\n# Créer /etc/fail2ban/jail.local:\nsudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local\nsudo nano /etc/fail2ban/jail.local\n\n# Configuration recommandée:\n[DEFAULT]\nbantime  = 3600        # 1h ban\nfindtime = 600         # Fenêtre 10min\nmaxretry = 5           # 5 échecs max\nignoreip = 127.0.0.1/8 192.168.1.0/24  # IPs ignorées\n\n[sshd]\nenabled = true\nport    = ssh\nlogpath = /var/log/auth.log\nmaxretry = 3           # SSH: 3 échecs seulement!\n\n# Redémarrer:\nsudo systemctl restart fail2ban\n\n# Status:\nsudo fail2ban-client status\nsudo fail2ban-client status sshd\n\n# Débanner IP:\nsudo fail2ban-client set sshd unbanip 1.2.3.4\n\n# Logs:\nsudo tail -f /var/log/fail2ban.log\n\n# Jails disponibles:\nls /etc/fail2ban/filter.d/\n# apache-auth, nginx-http-auth, postfix, etc."
            },
            {
                "title": "SSH - Durcissement",
                "code": "# Config SSH sécurisée: /etc/ssh/sshd_config\n\nsudo nano /etc/ssh/sshd_config\n\n# Changements recommandés:\nPort 2222                      # Changer port (évite scans auto)\nPermitRootLogin no             # JAMAIS login root direct!\nPasswordAuthentication no      # Clés SSH UNIQUEMENT\nPubkeyAuthentication yes\nPermitEmptyPasswords no\nX11Forwarding no               # Sauf si besoin\nMaxAuthTries 3\nMaxSessions 2\nClientAliveInterval 300\nClientAliveCountMax 2\nAllowUsers alice bob           # Whitelist users\n# Ou:\nDenyUsers root guest\n\n# Protocole 2 uniquement (défaut moderne):\nProtocol 2\n\n# Algorithmes forts uniquement:\nCiphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com\nMACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com\nKexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org\n\n# Appliquer changements:\nsudo systemctl restart sshd\n\n# Vérifier config AVANT redémarrer:\nsudo sshd -t\n# OK si aucun output\n\n# Tester connexion (nouveau terminal!):\nssh -p 2222 user@localhost\n\n# ⚠️ Gardez session root ouverte jusqu'à test réussi!"
            },
            {
                "title": "AppArmor / SELinux - Mandatory Access Control",
                "code": "# AppArmor (Ubuntu/Debian/SUSE):\n# Préinstallé Ubuntu, actif par défaut\n\n# Status:\nsudo aa-status\n# Affiche profiles chargés\n\n# Modes:\n# enforce: Bloque violations\n# complain: Logs uniquement (audit)\n# disabled: Inactif\n\n# Mettre profile en mode complain:\nsudo aa-complain /etc/apparmor.d/usr.bin.firefox\n\n# Retour enforce:\nsudo aa-enforce /etc/apparmor.d/usr.bin.firefox\n\n# Recharger profiles:\nsudo systemctl reload apparmor\n\n# Logs violations:\nsudo journalctl | grep -i apparmor\nsudo dmesg | grep -i apparmor\n\n# SELinux (Fedora/RHEL/CentOS):\n# Status:\ngetenforce\n# Enforcing, Permissive, ou Disabled\n\n# Changer mode temporaire:\nsudo setenforce 0  # Permissive\nsudo setenforce 1  # Enforcing\n\n# Permanent: /etc/selinux/config\nSELINUX=enforcing\n\n# Voir contextes fichiers:\nls -Z /var/www/html/\n\n# Restaurer contextes:\nsudo restorecon -Rv /var/www/html/\n\n# Logs:\nsudo ausearch -m avc -ts recent\nsudo tail -f /var/log/audit/audit.log | grep AVC\n\n# Générer policy depuis logs:\nsudo audit2allow -a\nsudo audit2allow -a -M mypolicy\nsudo semodule -i mypolicy.pp"
            },
            {
                "title": "Chiffrement Disque - LUKS",
                "code": "# LUKS = Linux Unified Key Setup (chiffrement disque)\n\n# Vérifier si partition chiffrée:\nlsblk -f\n# TYPE=\"crypto_LUKS\" si chiffré\n\n# Chiffrer partition VIDE:\nsudo cryptsetup luksFormat /dev/sdb1\n# ⚠️ EFFACE partition! Demande passphrase\n\n# Ouvrir partition chiffrée:\nsudo cryptsetup luksOpen /dev/sdb1 ma_partition\n# Demande passphrase, crée /dev/mapper/ma_partition\n\n# Formater partition déchiffrée:\nsudo mkfs.ext4 /dev/mapper/ma_partition\n\n# Monter:\nsudo mount /dev/mapper/ma_partition /mnt/secure\n\n# Utiliser normalement...\n\n# Démonter + fermer:\nsudo umount /mnt/secure\nsudo cryptsetup luksClose ma_partition\n\n# Montage auto (/etc/crypttab + /etc/fstab):\n# /etc/crypttab:\nma_partition UUID=abc-123-def /chemin/vers/keyfile luks\n\n# Keyfile (éviter saisie password boot):\nsudo dd if=/dev/urandom of=/root/keyfile bs=1024 count=4\nsudo chmod 600 /root/keyfile\nsudo cryptsetup luksAddKey /dev/sdb1 /root/keyfile\n\n# Changer passphrase:\nsudo cryptsetup luksChangeKey /dev/sdb1\n\n# Backup header LUKS (critique!):\nsudo cryptsetup luksHeaderBackup /dev/sdb1 --header-backup-file /root/luks-header-sdb1.img\n# Header corrompu = données perdues!"
            },
            {
                "title": "Audit Sécurité - Lynis",
                "code": "# Lynis = Audit sécurité automatisé\n\n# Installer:\nsudo apt install lynis -y\nsudo dnf install lynis -y\n\n# Lancer audit complet:\nsudo lynis audit system\n\n# Rapport généré: /var/log/lynis-report.dat\n\n# Sections auditées:\n# - Boot/services\n# - Kernel\n# - Logging\n# - Storage\n# - Filesystems\n# - USB devices\n# - Networking\n# - Firewall\n# - SSH config\n# - Comptes utilisateurs\n# - Authentication\n# - Malware scanners\n# - File integrity\n\n# Score sécurité:\n# Hardening index: 65/100 (exemple)\n\n# Suggestions affichées:\n# [SUGGESTION] Enable process accounting\n# [SUGGESTION] Install malware scanner\n\n# Voir report:\ncat /var/log/lynis-report.dat\n\n# Audit régulier (cron):\ncrontab -e\n# 0 3 * * 0 /usr/bin/lynis audit system >> /var/log/lynis-weekly.log"
            },
            {
                "title": "Antivirus - ClamAV",
                "code": "# ClamAV = Antivirus open-source Linux\n\n# Installer:\nsudo apt install clamav clamav-daemon -y\n\n# Mettre à jour signatures:\nsudo systemctl stop clamav-freshclam\nsudo freshclam\nsudo systemctl start clamav-freshclam\n\n# Scanner dossier:\nclamscan -r /home/user/\n# -r: Récursif\n\n# Scanner + supprimer infectés:\nclamscan -r --remove /home/user/Downloads/\n\n# Scanner + logs:\nclamscan -r -i /home/ -l /var/log/clamav-scan.log\n# -i: Afficher infectés uniquement\n\n# Scan système complet:\nsudo clamscan -r -i / --exclude-dir=/sys --exclude-dir=/proc --exclude-dir=/dev\n\n# Daemon temps réel (clamd):\nsudo systemctl start clamav-daemon\n\n# On-access scanning (nécessite clamav-unofficial-sigs):\nsudo apt install clamav-unofficial-sigs -y\n\n# Scan automatique (cron):\ncrontab -e\n# 0 2 * * * clamscan -r -i /home >> /var/log/clamav-daily.log\n\n# ⚠️ ClamAV détecte surtout malware Windows\n# Utile pour serveurs mail/fichiers partagés"
            },
            {
                "info": "💡 Sécurité = layers! Combinez: firewall + fail2ban + SSH keys + updates auto + AppArmor + backups. Une seule mesure ≠ suffisant."
            },
            {
                "warning": "⚠️ TESTEZ config SSH dans nouveau terminal AVANT fermer session admin! Config cassée = lockout permanent si accès physique impossible."
            },
            {
                "warning": "⚠️ LUKS header backup CRITIQUE! Header corrompu = données irrécupérables même avec passphrase. Sauvegardez header séparément!"
            }
        ]
    },

    "linux_performance": {
        "title": "⚡ Optimisation & Performance",
        "sections": [
            {
                "title": "Diagnostic Performance",
                "code": "# CPU:\ntop                   # Classique\nhtop                  # Meilleur (installer: apt install htop)\n# Tri: F6 (CPU%, MEM%, TIME)\n# Kill: F9\n# Tree view: F5\n\n# RAM:\nfree -h\n# Available = RAM réellement disponible (pas Free!)\n# Swap utilisé massivement = manque RAM\n\n# Disk I/O:\nsudo iotop           # apt install iotop\n# Affiche processus I/O disk\n\n# Network:\nsudo iftop           # apt install iftop\nsudo nethogs         # Par processus\n\n# Overview complet:\nvmstat 1             # Stats par seconde\n# r = processus waiting CPU (>CPU cores = bottleneck)\n# si/so = swap in/out (>0 constamment = problème RAM)\n# bi/bo = blocks in/out (I/O disk)\n\n# I/O wait:\niostat -x 1\n# %iowait élevé = disk lent\n\n# Température:\nsensors              # apt install lm-sensors\nsudo sensors-detect  # 1ère fois\n\n# GPU:\nnvidia-smi           # NVIDIA\nradeontop            # AMD (apt install radeontop)\nintel_gpu_top        # Intel"
            },
            {
                "title": "Swappiness - Gestion Swap",
                "code": "# Swappiness = Agressivité utilisation swap\n# 0-100: 0=éviter swap, 100=swap agressif\n# Défaut: 60 (trop élevé desktop!)\n\n# Voir swappiness actuel:\ncat /proc/sys/vm/swappiness\n# 60 (défaut)\n\n# Recommandé desktop (beaucoup RAM): 10\n# Recommandé serveur: 10-30\n# Recommandé laptop (peu RAM): 40-60\n\n# Changer temporaire:\nsudo sysctl vm.swappiness=10\n\n# Permanent:\nsudo nano /etc/sysctl.conf\n# Ajouter:\nvm.swappiness=10\n\n# Appliquer:\nsudo sysctl -p\n\n# Vérifier:\ncat /proc/sys/vm/swappiness\n# 10\n\n# Vider swap (si RAM disponible):\nsudo swapoff -a && sudo swapon -a\n# ⚠️ Nécessite RAM libre >= swap utilisé!\n\n# Désactiver swap complètement:\nsudo swapoff -a\n# Commenter ligne swap dans /etc/fstab\n\n# Réactiver:\nsudo swapon -a"
            },
            {
                "title": "I/O Scheduler - Performance Disque",
                "code": "# I/O Scheduler = Algorithme ordonnancement I/O\n\n# Schedulers disponibles:\n# - mq-deadline: Défaut, bon compromis\n# - kyber: Moderne, faible latence\n# - bfq: Budget Fair Queueing (desktop, interactivité)\n# - none: Direct dispatch (NVMe rapides)\n\n# Voir scheduler actuel:\ncat /sys/block/sda/queue/scheduler\n# [mq-deadline] kyber bfq none\n# [] = actif\n\n# Changer temporaire:\necho bfq | sudo tee /sys/block/sda/queue/scheduler\n\n# Permanent (udev rule):\nsudo nano /etc/udev/rules.d/60-scheduler.rules\n\n# SSD/NVMe (none ou kyber):\nACTION==\"add|change\", KERNEL==\"nvme[0-9]n[0-9]\", ATTR{queue/scheduler}=\"none\"\nACTION==\"add|change\", KERNEL==\"sd[a-z]\", ATTR{queue/rotational}==\"0\", ATTR{queue/scheduler}=\"kyber\"\n\n# HDD (mq-deadline ou bfq):\nACTION==\"add|change\", KERNEL==\"sd[a-z]\", ATTR{queue/rotational}==\"1\", ATTR{queue/scheduler}=\"bfq\"\n\n# Appliquer:\nsudo udevadm control --reload-rules\nsudo udevadm trigger\n\n# Recommandations:\n# - NVMe rapide: none\n# - SSD SATA: kyber ou mq-deadline\n# - HDD: bfq (desktop) ou mq-deadline (serveur)\n# - Desktop interactif: bfq\n# - Serveur DB: mq-deadline"
            },
            {
                "title": "CPU Governor - Gestion Fréquence",
                "code": "# CPU Governor = Gestion fréquence CPU (performance vs économie)\n\n# Governors:\n# - powersave: Fréquence mini (économie)\n# - performance: Fréquence maxi (perf)\n# - ondemand: Auto selon charge (équilibré)\n# - schedutil: Moderne, basé scheduler (défaut récent)\n# - conservative: Comme ondemand, transitions lentes\n\n# Voir governor actuel:\ncat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor\n\n# Ou:\ncpupower frequency-info\n# apt install linux-tools-common linux-tools-generic\n\n# Changer tous CPUs:\nsudo cpupower frequency-set -g performance\n\n# Performance max (gaming, rendu):\nsudo cpupower frequency-set -g performance\n\n# Économie (laptop batterie):\nsudo cpupower frequency-set -g powersave\n\n# Auto (défaut):\nsudo cpupower frequency-set -g schedutil\n\n# Permanent (systemd):\nsudo nano /etc/default/cpupower\n# governor='performance'\n\nsudo systemctl enable cpupower\nsudo systemctl start cpupower\n\n# Turbo Boost (Intel):\n# Activer:\necho 0 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo\n# Désactiver:\necho 1 | sudo tee /sys/devices/system/cpu/intel_pstate/no_turbo\n\n# AMD équivalent:\necho 0 | sudo tee /sys/devices/system/cpu/cpufreq/boost"
            },
            {
                "title": "Preload - Prédiction Chargement Apps",
                "code": "# Preload = Précharge apps fréquentes en RAM\n# Analyse usage, prédit apps à charger\n# Utile si >4GB RAM disponible\n\n# Installer:\nsudo apt install preload -y\n\n# Démarre auto, aucune config requise\n\n# Vérifier status:\nsudo systemctl status preload\n\n# Logs (voir apps analysées):\nsudo journalctl -u preload\n\n# Config avancée (optionnel):\nsudo nano /etc/preload.conf\n\n# Options:\nminsize = 2000000      # Taille min fichier (bytes)\nmemtotal = 256         # RAM min system (MB)\nmemfree = 50           # RAM libre garder (MB)\n\n# Redémarrer:\nsudo systemctl restart preload\n\n# ⚠️ Consomme RAM! Pas recommandé si <4GB RAM\n# Bénéfice: Apps démarrent ~20-50% plus vite\n\n# Alternative: systemd-readahead (obsolète, remplacé par systemd)\n# Moderne: systemd boot analysis\nsystemd-analyze blame"
            },
            {
                "title": "zram - Compression RAM",
                "code": "# zram = Swap compressé en RAM (pas sur disque!)\n# Utile: Laptop peu RAM, éviter swap disque lent\n\n# Installer:\nsudo apt install zram-config -y    # Ubuntu\nsudo dnf install zram -y           # Fedora\n\n# Auto-activé après install Ubuntu\n\n# Vérifier:\nzramctl\n# NAME       ALGORITHM DISKSIZE DATA COMPR TOTAL STREAMS MOUNTPOINT\n# /dev/zram0 lz4           2G   4K   74B   12K       4 [SWAP]\n\n# Status:\nsudo systemctl status zram-config\n\n# Manuel (Arch, etc.):\nsudo modprobe zram\necho lz4 | sudo tee /sys/block/zram0/comp_algorithm\necho 2G | sudo tee /sys/block/zram0/disksize\nsudo mkswap /dev/zram0\nsudo swapon -p 100 /dev/zram0\n# -p 100: Priorité max (préférer zram vs swap disque)\n\n# Permanent (systemd service):\nsudo nano /etc/systemd/system/zram.service\n\n[Unit]\nDescription=Swap with zram\nAfter=multi-user.target\n\n[Service]\nType=oneshot\nRemainAfterExit=true\nExecStartPre=/sbin/modprobe zram\nExecStart=/bin/sh -c 'echo lz4 > /sys/block/zram0/comp_algorithm'\nExecStart=/bin/sh -c 'echo 2G > /sys/block/zram0/disksize'\nExecStart=/sbin/mkswap /dev/zram0\nExecStart=/sbin/swapon -p 100 /dev/zram0\nExecStop=/sbin/swapoff /dev/zram0\n\n[Install]\nWantedBy=multi-user.target\n\nsudo systemctl enable zram\nsudo systemctl start zram\n\n# Ratio compression: ~2.5:1 (2GB zram ≈ 5GB données)\n# Performance: Bien meilleur que swap disque!"
            },
            {
                "title": "Nettoyage Système",
                "code": "# Nettoyer cache APT:\nsudo apt clean              # Supprime tous .deb téléchargés\nsudo apt autoclean          # Supprime .deb obsolètes\nsudo apt autoremove         # Supprime dépendances inutiles\n\n# Fedora:\nsudo dnf clean all\nsudo dnf autoremove\n\n# Arch:\nsudo pacman -Scc            # Nettoie cache (garde 3 versions)\nsudo pacman -Sc             # Nettoie packages non installés\npacman -Qtdq | sudo pacman -Rns -  # Orphelins\n\n# Journald (logs systemd):\n# Voir taille:\njournalctl --disk-usage\n\n# Garder 3 jours:\nsudo journalctl --vacuum-time=3d\n\n# Garder 500MB max:\nsudo journalctl --vacuum-size=500M\n\n# Config permanent:\nsudo nano /etc/systemd/journald.conf\nSystemMaxUse=500M\n\n# Thumbnails cache:\ndu -sh ~/.cache/thumbnails\nrm -rf ~/.cache/thumbnails/*\n\n# Trash:\ndu -sh ~/.local/share/Trash\nrm -rf ~/.local/share/Trash/*\n\n# Fichiers temporaires:\nsudo rm -rf /tmp/*\nsudo rm -rf /var/tmp/*\n\n# Trouver gros fichiers:\nsudo du -ah / | sort -rh | head -20\nncdu /                      # apt install ncdu (interactif)\n\n# Fichiers >1GB:\nsudo find / -type f -size +1G -exec ls -lh {} \\;\n\n# Vieux kernels (Ubuntu):\nsudo apt autoremove --purge"
            },
            {
                "title": "SSD - Optimisations",
                "code": "# TRIM - Libérer blocs effacés\n# Moderne: Auto-activé (fstab discard ou fstrim.timer)\n\n# Vérifier TRIM supporté:\nsudo hdparm -I /dev/sda | grep TRIM\n# Data Set Management TRIM supported\n\n# Méthode 1: fstrim manuel\nsudo fstrim -v /\n# /: 15.2 GiB trimmed\n\n# Méthode 2: fstrim.timer (recommandé)\nsudo systemctl status fstrim.timer\nsudo systemctl enable fstrim.timer\n# Lance fstrim hebdomadaire auto\n\n# Méthode 3: fstab discard (déconseillé - impact perf)\n# /etc/fstab:\n# UUID=xxx / ext4 defaults,noatime,discard 0 1\n# ⚠️ discard continu = ralentit écritures\n\n# noatime - Pas update access time:\n# /etc/fstab:\nUUID=xxx / ext4 defaults,noatime 0 1\n# Réduit écritures SSD, améliore perf\n\n# Scheduler (voir section I/O Scheduler):\necho none | sudo tee /sys/block/nvme0n1/queue/scheduler\n\n# Swappiness bas (si SSD):\nvm.swappiness=10\n\n# SMART monitoring:\nsudo apt install smartmontools -y\nsudo smartctl -a /dev/sda\n# Wear leveling count, reallocated sectors\n\n# ⚠️ Pas de defrag SSD! (inutile + use wear)"
            },
            {
                "title": "Benchmarks Performance",
                "code": "# CPU - sysbench:\nsudo apt install sysbench -y\nsysbench cpu --threads=4 --time=30 run\n# events per second = score\n\n# Disk - hdparm (lecture):\nsudo hdparm -Tt /dev/sda\n# Timing cached reads:   12000 MB/sec\n# Timing buffered disk reads: 450 MB/sec\n\n# Disk - dd (écriture):\nsync; dd if=/dev/zero of=~/testfile bs=1G count=1 oflag=direct; sync\n# 1+0 records in/out, 500 MB/s\nrm ~/testfile\n\n# Disk - fio (avancé):\nsudo apt install fio -y\nfio --name=randwrite --ioengine=libaio --iodepth=16 --rw=randwrite --bs=4k --direct=1 --size=1G --numjobs=4 --runtime=60 --group_reporting\n\n# RAM:\nsudo apt install sysbench -y\nsysbench memory --threads=4 run\n\n# GPU - glxgears:\nglxgears\n# FPS affiché\n\n# GPU - unigine-heaven:\n# Benchmark 3D complet (télécharger site Unigine)\n\n# Réseau - iperf3:\nsudo apt install iperf3 -y\n# Serveur:\niperf3 -s\n# Client:\niperf3 -c <ip_serveur>\n\n# Boot time:\nsystemd-analyze\n# Startup finished in 2.5s (kernel) + 8.3s (userspace) = 10.8s\n\nsystemd-analyze blame\n# Liste services par temps démarrage"
            },
            {
                "info": "💡 Performance = compromis! Performance max = consommation élevée. Laptop: Économie batterie > perf. Desktop/gaming: Perf > économie."
            },
            {
                "warning": "⚠️ SSD: JAMAIS defrag! Inutile (pas fragmentation) + use wear. TRIM hebdo suffisant (fstrim.timer). noatime recommandé."
            },
            {
                "warning": "⚠️ Governor performance = CPU 100% fréquence constante = chaleur + conso. Gaming uniquement, pas 24/7! Schedutil équilibré meilleur quotidien."
            }
        ]
    },

    "linux_wine": {
        "title": "🍷 Wine - Applications Windows sur Linux",
        "sections": [
            {
                "title": "Wine - Qu'est-ce que c'est?",
                "content": "Wine (Wine Is Not an Emulator) = Couche compatibilité exécutant apps Windows sur Linux. Traduit appels API Windows → Linux. Pas de virtualisation, performance native. Proton (Valve) = Wine + DXVK + améliorations gaming. Lutris = Frontend graphique Wine + gestionnaire jeux/apps. Wine Staging = Nouvelles features expérimentales. CrossOver = Version commerciale (support professionnel)."
            },
            {
                "title": "Installer Wine",
                "code": "# Ubuntu/Debian - Wine stable:\nsudo dpkg --add-architecture i386\nsudo mkdir -pm755 /etc/apt/keyrings\nsudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key\nsudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/$(lsb_release -cs)/winehq-$(lsb_release -cs).sources\nsudo apt update\nsudo apt install --install-recommends winehq-stable -y\n\n# Wine Staging (nouvelles features):\nsudo apt install --install-recommends winehq-staging -y\n\n# Fedora:\nsudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/$(rpm -E %fedora)/winehq.repo\nsudo dnf install winehq-stable -y\n\n# Arch:\nsudo pacman -S wine winetricks -y\n\n# Vérifier version:\nwine --version\n# wine-9.0\n\nwinetricks --version"
            },
            {
                "title": "Utiliser Wine - Basique",
                "code": "# Lancer .exe Windows:\nwine programme.exe\n\n# Installer .exe (installateur):\nwine setup.exe\n# Suit wizard installation Windows normal\n\n# Apps installées dans:\n~/.wine/drive_c/Program Files/\n~/.wine/drive_c/Program Files (x86)/\n\n# Lancer app installée:\nwine ~/.wine/drive_c/Program\\ Files/MonApp/app.exe\n\n# Créer raccourci:\nwine explorer /desktop=shell,1920x1080 programme.exe\n\n# Désinstaller app:\nwine uninstaller\n# Liste apps Windows installées\n\n# Tuer processus Wine bloqué:\nwineserver -k\n# Kill all\n\n# Configuration Wine:\nwinecfg\n# GUI config: Version Windows, Audio, Graphics, etc."
            },
            {
                "title": "Wine Prefix - Environnements Isolés",
                "code": "# Wine Prefix = Environnement Windows isolé\n# Défaut: ~/.wine\n# Chaque app peut avoir son prefix (éviter conflits)\n\n# Créer prefix 64-bit:\nWINEARCH=win64 WINEPREFIX=~/wine-prefixes/monapp wineboot\n\n# Créer prefix 32-bit (apps anciennes):\nWINEARCH=win32 WINEPREFIX=~/wine-prefixes/app32 wineboot\n\n# Lancer app dans prefix:\nWINEPREFIX=~/wine-prefixes/monapp wine programme.exe\n\n# Config prefix spécifique:\nWINEPREFIX=~/wine-prefixes/monapp winecfg\n\n# Structure prefix:\n~/wine-prefixes/monapp/\n├── drive_c/\n│   ├── Program Files/\n│   ├── users/\n│   └── windows/\n├── dosdevices/\n└── system.reg\n\n# Supprimer prefix:\nrm -rf ~/wine-prefixes/monapp\n\n# Avantages prefixes séparés:\n# - Isolation (DLL conflicts évités)\n# - Version Wine différente par app\n# - Désinstallation propre (rm -rf)"
            },
            {
                "title": "winetricks - Installer Dépendances",
                "code": "# winetricks = Installer DLL, fonts, runtime Windows\n\n# GUI:\nwinetricks\n\n# Installer .NET Framework:\nwinetricks dotnet48\n# Ou versions anciennes:\nwinetricks dotnet40 dotnet35\n\n# Visual C++ Runtime:\nwinetricks vcrun2019\nwinetricks vcrun2015 vcrun2013 vcrun2010\n\n# DirectX:\nwinetricks d3dx9 d3dx10 d3dx11_43\n\n# Fonts (polices):\nwinetricks corefonts\nwinetricks allfonts        # Toutes (lourd!)\n\n# DXVK (DirectX → Vulkan):\nwinetricks dxvk\n# Performance gaming++\n\n# VKD3D (DirectX 12 → Vulkan):\nwinetricks vkd3d\n\n# Autres runtime courants:\nwinetricks vcrun6           # Visual Basic 6\nwinetricks mfc42            # Microsoft Foundation Classes\nwinetricks msxml3 msxml6    # XML parsers\nwinetricks quartz           # DirectShow\n\n# Dans prefix spécifique:\nWINEPREFIX=~/wine-prefixes/monapp winetricks vcrun2019\n\n# Lister verbs disponibles:\nwinetricks list-all\n\n# Installer app populaire (script):\nwinetricks steam            # Steam\nwinetricks spotify          # Spotify\n# ⚠️ Versions Linux natives existent!"
            },
            {
                "title": "DXVK - DirectX → Vulkan",
                "code": "# DXVK = Traduit DirectX 9/10/11 → Vulkan\n# Performance gaming bien meilleure!\n\n# Installer (winetricks):\nwinetricks dxvk\n\n# Ou manuel (dernière version):\nwget https://github.com/doitsujin/dxvk/releases/latest\nunzip dxvk-*.tar.gz\ncd dxvk-*/\nWINEPREFIX=~/wine-prefixes/jeu ./setup_dxvk.sh install\n\n# Vérifier DXVK actif (logs):\nDXVK_HUD=fps wine jeu.exe\n# Affiche FPS overlay + version DXVK\n\n# HUD complet:\nDXVK_HUD=full wine jeu.exe\n# FPS, frametimes, drawcalls, etc.\n\n# Config DXVK (dxvk.conf):\n# ~/.wine/drive_c/dxvk.conf\nd3d9.maxFrameRate = 144\nd3d11.maxFrameRate = 144\ndxgi.maxFrameLatency = 1\n\n# Désactiver DXVK:\nWINEPREFIX=~/wine-prefixes/jeu ./setup_dxvk.sh uninstall\n\n# Ou variable:\nDXVK_DISABLE=1 wine jeu.exe\n\n# Logs debug:\nDXVK_LOG_LEVEL=info wine jeu.exe\n\n# ⚠️ Nécessite drivers Vulkan!\nvulkaninfo | grep deviceName"
            },
            {
                "title": "Gaming avec Wine",
                "code": "# Préférez Proton/Steam si possible!\n# Sinon Lutris (gère Wine automatiquement)\n\n# Variables environnement utiles:\n# Performance max:\nMESA_GL_VERSION_OVERRIDE=4.5 wine jeu.exe\n\n# Force Vulkan:\nDXVK_HUD=1 wine jeu.exe\n\n# Esync (sync events - performance):\nWINEESYNC=1 wine jeu.exe\n# Nécessite limites ulimit:\nulimit -n 524288\n\n# Fsync (meilleur que esync):\nWINEFSYNC=1 wine jeu.exe\n# Kernel 5.16+ requis\n\n# ACO compiler (AMD GPU):\nRADV_PERFTEST=aco wine jeu.exe\n\n# Virtual desktop (éviter bugs fullscreen):\nwine explorer /desktop=game,1920x1080 jeu.exe\n\n# Exemple combiné (AMD GPU, jeu DX11):\nDXVK_HUD=fps WINEFSYNC=1 RADV_PERFTEST=aco wine jeu.exe\n\n# Problèmes courants:\n# - Pas de son: winetricks sound=pulse\n# - Crash DX: winetricks dxvk\n# - Fonts manquantes: winetricks corefonts\n# - .NET erreur: winetricks dotnet48\n\n# Logs debug:\nWINEDEBUG=+all wine jeu.exe > wine.log 2>&1\n# ⚠️ Fichier énorme!\n\n# Logs modules spécifiques:\nWINEDEBUG=+d3d11,+dxgi wine jeu.exe"
            },
            {
                "title": "Applications Bureautique",
                "code": "# Microsoft Office:\n# ⚠️ Versions récentes problématiques\n# Office 2010/2013 fonctionnent mieux\n\n# Installer Office 2010:\nwinetricks msxml6 dotnet40 corefonts\n# Lancer setup.exe Office\n\n# Alternative: WPS Office (natif Linux!)\nsudo apt install wps-office -y\n\n# Adobe Photoshop:\n# CS6 fonctionne (versions récentes non)\nWINEARCH=win64 WINEPREFIX=~/wine-prefixes/photoshop wineboot\nWINEPREFIX=~/wine-prefixes/photoshop winetricks atmlib gdiplus msxml3 msxml6 vcrun2008 vcrun2010 vcrun2012 corefonts\n# Installer Photoshop_Set-Up.exe\n\n# Alternative: GIMP (natif!)\nsudo apt install gimp -y\n\n# Notepad++:\nwine notepadplusplus-installer.exe\n# Alternative: VSCode, Sublime, Gedit\n\n# 7-Zip:\nwine 7z-installer.exe\n# Alternative: p7zip (natif)\nsudo apt install p7zip-full -y\n\n# FileZilla, VLC, etc.:\n# Versions Linux natives existent!\nsudo apt install filezilla vlc"
            },
            {
                "title": "Debugging Wine",
                "code": "# Vérifier architecture:\nfile programme.exe\n# PE32+ = 64-bit (WINEPREFIX 64-bit)\n# PE32 = 32-bit (WINEPREFIX 32-bit)\n\n# Lister processus Wine:\nwinedbg --command \"info proc\"\n\n# Tuer tous Wine:\nwineserver -k\n\n# Logs verbeux:\nWINEDEBUG=+all wine app.exe 2>&1 | tee wine.log\n# Fichier gigantesque! Utiliser grep\n\n# Modules spécifiques:\nWINEDEBUG=+module,+relay wine app.exe\n\n# Registry Windows:\nwine regedit\n# HKEY_CURRENT_USER, etc.\n\n# Task Manager:\nwine taskmgr\n\n# Explorateur fichiers:\nwine explorer\n\n# CMD Windows:\nwine cmd\n\n# Désinstaller tout Wine (reset):\nrm -rf ~/.wine\nwineboot\n# Recrée prefix vierge\n\n# Problème fréquent: Mono installer\n# Si popup \"Install Mono?\": Oui\n# Ou:\nwinetricks mono"
            },
            {
                "info": "💡 Préférez versions Linux natives! Wine = dernier recours. Steam Proton meilleur pour jeux. Lutris gère Wine automatiquement."
            },
            {
                "warning": "⚠️ Wine ≠ 100% compatible! Apps récentes/complexes problématiques. Vérifier WineHQ AppDB avant: appdb.winehq.org"
            },
            {
                "warning": "⚠️ Malware Windows fonctionne sous Wine! Antivirus Linux + prudence. Pas exécuter .exe suspects. Wine = accès /home/!"
            }
        ]
    },

    "linux_docker": {
        "title": "🐳 Docker - Conteneurisation",
        "sections": [
            {
                "title": "Docker - Concepts de Base",
                "bullets": [
                    "Container: Processus isolé, léger (vs VM lourde)",
                    "• Partage kernel hôte, isolation filesystem/network/processus",
                    "• Démarre en secondes, utilise peu RAM",
                    "",
                    "Image: Template lecture seule (base container)",
                    "• Layers superposés (base → app → config)",
                    "• Réutilisables, partageables (Docker Hub)",
                    "",
                    "Dockerfile: Recette création image",
                    "• FROM, RUN, COPY, CMD, etc.",
                    "",
                    "Docker Hub: Registry images publiques",
                    "• Ubuntu, Nginx, MySQL, etc."
                ]
            },
            {
                "title": "Installer Docker",
                "code": "# Ubuntu/Debian - Méthode officielle:\nsudo apt update\nsudo apt install ca-certificates curl gnupg -y\nsudo install -m 0755 -d /etc/apt/keyrings\ncurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg\nsudo chmod a+r /etc/apt/keyrings/docker.gpg\n\necho \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null\n\nsudo apt update\nsudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y\n\n# Fedora:\nsudo dnf install dnf-plugins-core -y\nsudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo\nsudo dnf install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y\nsudo systemctl start docker\nsudo systemctl enable docker\n\n# Arch:\nsudo pacman -S docker docker-compose -y\nsudo systemctl start docker\nsudo systemctl enable docker\n\n# Ajouter user au groupe docker (éviter sudo):\nsudo usermod -aG docker $USER\n# RE-LOGIN requis!\n\n# Vérifier:\ndocker --version\ndocker run hello-world"
            },
            {
                "title": "Commandes Docker Essentielles",
                "code": "# Lister containers actifs:\ndocker ps\n\n# Tous containers (actifs + arrêtés):\ndocker ps -a\n\n# Lancer container:\ndocker run ubuntu\n# Télécharge image ubuntu, lance, arrête\n\n# Container interactif:\ndocker run -it ubuntu bash\n# -i: Interactive (stdin ouvert)\n# -t: TTY (terminal)\n# Sortir: exit ou Ctrl+D\n\n# Container détaché (background):\ndocker run -d nginx\n# -d: Detached\n# Retourne CONTAINER_ID\n\n# Nommer container:\ndocker run --name mon-nginx -d nginx\n\n# Arrêter container:\ndocker stop mon-nginx\n# Ou par ID:\ndocker stop abc123\n\n# Démarrer container arrêté:\ndocker start mon-nginx\n\n# Redémarrer:\ndocker restart mon-nginx\n\n# Supprimer container:\ndocker rm mon-nginx\n# ⚠️ Container doit être arrêté!\n# Force:\ndocker rm -f mon-nginx\n\n# Supprimer tous containers arrêtés:\ndocker container prune\n\n# Logs container:\ndocker logs mon-nginx\ndocker logs -f mon-nginx  # Follow (temps réel)\n\n# Exécuter commande dans container:\ndocker exec -it mon-nginx bash\n# Ouvre shell dans container actif"
            },
            {
                "title": "Images Docker",
                "code": "# Lister images locales:\ndocker images\n\n# Télécharger image:\ndocker pull ubuntu:22.04\n# Format: nom:tag\n# Tag = version (latest par défaut)\n\n# Chercher images Docker Hub:\ndocker search nginx\n\n# Supprimer image:\ndocker rmi ubuntu:22.04\n# ⚠️ Aucun container utilisant image!\n\n# Supprimer images non utilisées:\ndocker image prune\n\n# Inspecter image:\ndocker inspect nginx\n# JSON: layers, variables env, config\n\n# Historique layers:\ndocker history nginx\n# Affiche commandes création layers\n\n# Sauvegarder image (tar):\ndocker save nginx > nginx.tar\n\n# Charger image:\ndocker load < nginx.tar\n\n# Tag image:\ndocker tag nginx:latest mon-nginx:v1\n\n# Push Docker Hub (nécessite login):\ndocker login\ndocker push username/mon-nginx:v1"
            },
            {
                "title": "Ports & Volumes",
                "code": "# Mapper port (host:container):\ndocker run -d -p 8080:80 nginx\n# Accès: http://localhost:8080\n# Host port 8080 → Container port 80\n\n# Port aléatoire:\ndocker run -d -P nginx\n# -P: Publie tous ports EXPOSE\n\n# Voir ports:\ndocker port mon-nginx\n# 80/tcp -> 0.0.0.0:8080\n\n# Volume (persister données):\ndocker run -d -v /host/data:/container/data ubuntu\n# /host/data monté sur /container/data\n\n# Volume nommé:\ndocker volume create mon-volume\ndocker run -d -v mon-volume:/data ubuntu\n\n# Lister volumes:\ndocker volume ls\n\n# Inspecter volume:\ndocker volume inspect mon-volume\n# Localisation: /var/lib/docker/volumes/mon-volume/_data\n\n# Supprimer volume:\ndocker volume rm mon-volume\n\n# Supprimer volumes non utilisés:\ndocker volume prune\n\n# Bind mount (dossier hôte):\ndocker run -d -v /home/user/site:/usr/share/nginx/html nginx\n# Modifications hôte = visibles container temps réel"
            },
            {
                "title": "Dockerfile - Créer Images",
                "code": "# Dockerfile = Recette création image\n\n# Exemple Dockerfile:\ncat > Dockerfile <<'EOF'\n# Image de base\nFROM ubuntu:22.04\n\n# Metadata\nLABEL maintainer=\"you@example.com\"\n\n# Update + install packages\nRUN apt update && apt install -y \\\n    nginx \\\n    curl \\\n    && rm -rf /var/lib/apt/lists/*\n\n# Copier fichiers\nCOPY index.html /var/www/html/\n\n# Variables environnement\nENV APP_VERSION=1.0\n\n# Port exposé\nEXPOSE 80\n\n# Commande démarrage\nCMD [\"nginx\", \"-g\", \"daemon off;\"]\nEOF\n\n# Build image:\ndocker build -t mon-app:v1 .\n# -t: Tag\n# . : Dossier Dockerfile (contexte)\n\n# Build avec args:\ndocker build --build-arg VERSION=2.0 -t mon-app:v2 .\n\n# Dockerfile multi-stage (optimiser taille):\nFROM golang:1.21 AS builder\nWORKDIR /app\nCOPY . .\nRUN go build -o myapp\n\nFROM alpine:latest\nCOPY --from=builder /app/myapp /usr/local/bin/\nCMD [\"myapp\"]\n# Résultat: Image finale = alpine + binary (pas Go!)\n\n# Instructions Dockerfile:\n# FROM: Image base\n# RUN: Exécuter commande (build time)\n# CMD: Commande par défaut (runtime, écrasable)\n# ENTRYPOINT: Commande fixe (runtime)\n# COPY: Copier fichiers host → image\n# ADD: Comme COPY + extraction tar + URLs\n# ENV: Variable environnement\n# EXPOSE: Port documenté (pas publish!)\n# VOLUME: Point montage\n# WORKDIR: Dossier travail\n# USER: User exécution"
            },
            {
                "title": "Docker Compose - Multi-Containers",
                "code": "# docker-compose.yml = Orchestrer plusieurs containers\n\n# Exemple: WordPress + MySQL\ncat > docker-compose.yml <<'EOF'\nversion: '3.8'\n\nservices:\n  db:\n    image: mysql:8.0\n    volumes:\n      - db_data:/var/lib/mysql\n    environment:\n      MYSQL_ROOT_PASSWORD: rootpass\n      MYSQL_DATABASE: wordpress\n      MYSQL_USER: wpuser\n      MYSQL_PASSWORD: wppass\n    networks:\n      - wp-network\n\n  wordpress:\n    image: wordpress:latest\n    depends_on:\n      - db\n    ports:\n      - \"8080:80\"\n    environment:\n      WORDPRESS_DB_HOST: db\n      WORDPRESS_DB_USER: wpuser\n      WORDPRESS_DB_PASSWORD: wppass\n      WORDPRESS_DB_NAME: wordpress\n    volumes:\n      - wp_data:/var/www/html\n    networks:\n      - wp-network\n\nvolumes:\n  db_data:\n  wp_data:\n\nnetworks:\n  wp-network:\nEOF\n\n# Lancer stack:\ndocker compose up -d\n# -d: Detached\n\n# Voir logs:\ndocker compose logs -f\n\n# Arrêter stack:\ndocker compose down\n\n# Arrêter + supprimer volumes:\ndocker compose down -v\n\n# Rebuild images:\ndocker compose up -d --build\n\n# Scale service:\ndocker compose up -d --scale wordpress=3\n\n# Exec dans service:\ndocker compose exec wordpress bash"
            },
            {
                "title": "Gestion & Nettoyage",
                "code": "# Statistiques containers:\ndocker stats\n# CPU, RAM, I/O en temps réel\n\n# Espace disque Docker:\ndocker system df\n# Images, Containers, Volumes, Build Cache\n\n# Nettoyage complet:\ndocker system prune\n# Supprime:\n# - Containers arrêtés\n# - Networks non utilisés\n# - Images dangling\n# - Build cache\n\n# Nettoyage agressif:\ndocker system prune -a\n# + Images non utilisées par containers\n\n# Supprimer TOUT (⚠️):\ndocker system prune -a --volumes\n# Containers, Images, Volumes, Networks\n\n# Limiter ressources container:\ndocker run -d --memory=\"512m\" --cpus=\"1.5\" nginx\n# 512MB RAM max, 1.5 CPU cores\n\n# Redémarrage auto:\ndocker run -d --restart=unless-stopped nginx\n# Policies: no, on-failure, always, unless-stopped\n\n# Logs rotation:\ndocker run -d --log-opt max-size=10m --log-opt max-file=3 nginx\n\n# Inspecter container:\ndocker inspect mon-nginx\n# JSON complet: IP, volumes, env, etc."
            },
            {
                "info": "💡 Containers = éphémères! Données importantes dans volumes. Image = immuable, container = jetable. docker compose pour apps multi-services."
            },
            {
                "warning": "⚠️ Images publiques = potentiel malware! Utilisez images officielles (verified publisher). Scannez: docker scan image_name."
            },
            {
                "warning": "⚠️ Groupe docker = root-equivalent! User dans groupe docker peut escalate privilèges. Containers rootless si sécurité critique."
            }
        ]
    },

    "linux_scripts": {
        "title": "📜 Scripts Bash - Automatisation",
        "sections": [
            {
                "title": "Bash Scripting - Bases",
                "code": "#!/bin/bash\n# Shebang: Interpréteur à utiliser\n\n# Commentaire\n\n# Variables:\nNAME=\"Alice\"\nAGE=25\n\n# Utiliser variables:\necho \"Bonjour $NAME, vous avez $AGE ans\"\necho \"Bonjour ${NAME}, vous avez ${AGE} ans\"  # Syntaxe complète\n\n# Read-only:\nreadonly PI=3.14\n\n# Commandes:\nDATE=$(date)\nUSERS=$(who | wc -l)\n\n# Arithmétique:\nRESULT=$((5 + 3))\nRESULT=$((AGE * 2))\n\n# Arguments script:\n# $0 = nom script\n# $1, $2, ... = arguments\n# $# = nombre arguments\n# $@ = tous arguments\n# $? = code retour dernière commande\n\n#!/bin/bash\necho \"Script: $0\"\necho \"Premier arg: $1\"\necho \"Nombre args: $#\"\necho \"Tous args: $@\""
            },
            {
                "title": "Conditions if/elif/else",
                "code": "#!/bin/bash\n\n# if basique:\nif [ condition ]; then\n    echo \"Vrai\"\nfi\n\n# if/else:\nif [ condition ]; then\n    echo \"Vrai\"\nelse\n    echo \"Faux\"\nfi\n\n# if/elif/else:\nif [ condition1 ]; then\n    echo \"Condition 1\"\nelif [ condition2 ]; then\n    echo \"Condition 2\"\nelse\n    echo \"Autre\"\nfi\n\n# Comparaisons numériques:\n# -eq: égal\n# -ne: différent\n# -lt: inférieur\n# -le: inférieur ou égal\n# -gt: supérieur\n# -ge: supérieur ou égal\n\nif [ $AGE -ge 18 ]; then\n    echo \"Majeur\"\nfi\n\n# Comparaisons chaînes:\n# =: égal\n# !=: différent\n# -z: vide\n# -n: non vide\n\nif [ \"$NAME\" = \"Alice\" ]; then\n    echo \"Bonjour Alice\"\nfi\n\nif [ -z \"$VAR\" ]; then\n    echo \"Variable vide\"\nfi\n\n# Tests fichiers:\n# -f: fichier existe\n# -d: répertoire existe\n# -r: fichier lisible\n# -w: fichier modifiable\n# -x: fichier exécutable\n# -s: fichier non vide\n\nif [ -f \"/etc/passwd\" ]; then\n    echo \"Fichier existe\"\nfi\n\nif [ ! -d \"$DIR\" ]; then\n    mkdir \"$DIR\"\nfi\n\n# Opérateurs logiques:\n# &&: ET\n# ||: OU\n# !: NON\n\nif [ $AGE -ge 18 ] && [ \"$NAME\" = \"Alice\" ]; then\n    echo \"Alice majeure\"\nfi"
            },
            {
                "title": "Boucles for/while/until",
                "code": "#!/bin/bash\n\n# Boucle for - liste:\nfor NAME in Alice Bob Charlie; do\n    echo \"Bonjour $NAME\"\ndone\n\n# Boucle for - fichiers:\nfor FILE in *.txt; do\n    echo \"Fichier: $FILE\"\ndone\n\n# Boucle for - range:\nfor i in {1..10}; do\n    echo \"Nombre: $i\"\ndone\n\n# Boucle for - style C:\nfor ((i=0; i<10; i++)); do\n    echo \"Itération $i\"\ndone\n\n# Boucle while:\nCOUNT=0\nwhile [ $COUNT -lt 5 ]; do\n    echo \"Count: $COUNT\"\n    COUNT=$((COUNT + 1))\ndone\n\n# Lire fichier ligne par ligne:\nwhile IFS= read -r line; do\n    echo \"Ligne: $line\"\ndone < fichier.txt\n\n# Boucle until (inverse while):\nCOUNT=0\nuntil [ $COUNT -ge 5 ]; do\n    echo \"Count: $COUNT\"\n    COUNT=$((COUNT + 1))\ndone\n\n# break/continue:\nfor i in {1..10}; do\n    if [ $i -eq 5 ]; then\n        break  # Sortir boucle\n    fi\n    if [ $((i % 2)) -eq 0 ]; then\n        continue  # Itération suivante\n    fi\n    echo \"Impair: $i\"\ndone"
            },
            {
                "title": "Fonctions",
                "code": "#!/bin/bash\n\n# Définir fonction:\ngreet() {\n    echo \"Bonjour $1\"\n}\n\n# Appeler fonction:\ngreet \"Alice\"\n\n# Fonction avec return:\nadd() {\n    local result=$(($1 + $2))\n    echo $result\n}\n\nsum=$(add 5 3)\necho \"Somme: $sum\"\n\n# Variables locales:\nmyfunction() {\n    local LOCAL_VAR=\"Local\"\n    GLOBAL_VAR=\"Global\"\n    echo \"Dans fonction: $LOCAL_VAR\"\n}\n\nmyfunction\necho \"Hors fonction: $GLOBAL_VAR\"\n# LOCAL_VAR n'existe plus\n\n# Fonction avec validation:\nbackup_file() {\n    if [ $# -ne 1 ]; then\n        echo \"Usage: backup_file <fichier>\"\n        return 1\n    fi\n    \n    local file=$1\n    \n    if [ ! -f \"$file\" ]; then\n        echo \"Erreur: $file n'existe pas\"\n        return 1\n    fi\n    \n    cp \"$file\" \"${file}.bak\"\n    echo \"Backup créé: ${file}.bak\"\n    return 0\n}\n\nbackup_file \"document.txt\"\nif [ $? -eq 0 ]; then\n    echo \"Backup réussi\"\nfi"
            },
            {
                "title": "Arrays (Tableaux)",
                "code": "#!/bin/bash\n\n# Déclarer array:\nFRUITS=(\"Pomme\" \"Banane\" \"Orange\")\n\n# Accéder éléments:\necho \"${FRUITS[0]}\"  # Pomme\necho \"${FRUITS[1]}\"  # Banane\n\n# Tous éléments:\necho \"${FRUITS[@]}\"\necho \"${FRUITS[*]}\"\n\n# Nombre éléments:\necho \"${#FRUITS[@]}\"\n\n# Ajouter élément:\nFRUITS+=(\"Fraise\")\nFRUITS[4]=\"Cerise\"\n\n# Itérer array:\nfor fruit in \"${FRUITS[@]}\"; do\n    echo \"Fruit: $fruit\"\ndone\n\n# Array avec index:\nfor i in \"${!FRUITS[@]}\"; do\n    echo \"Index $i: ${FRUITS[$i]}\"\ndone\n\n# Slice array:\necho \"${FRUITS[@]:1:2}\"  # 2 éléments depuis index 1\n\n# Supprimer élément:\nunset FRUITS[1]\n\n# Array associatif (dictionnaire):\ndeclare -A USER\nUSER[name]=\"Alice\"\nUSER[age]=25\nUSER[city]=\"Paris\"\n\necho \"${USER[name]} a ${USER[age]} ans\"\n\n# Itérer array associatif:\nfor key in \"${!USER[@]}\"; do\n    echo \"$key = ${USER[$key]}\"\ndone"
            },
            {
                "title": "Gestion Erreurs & Debugging",
                "code": "#!/bin/bash\n\n# Exit on error:\nset -e\n# Script s'arrête si commande échoue\n\n# Exit on undefined variable:\nset -u\n# Erreur si variable non définie\n\n# Combiné (recommandé):\nset -euo pipefail\n# pipefail: Pipe échoue si commande échoue\n\n# Trap erreurs:\ntrap 'echo \"Erreur ligne $LINENO\"' ERR\n\n# Cleanup à la sortie:\ncleanup() {\n    echo \"Nettoyage...\"\n    rm -f /tmp/tempfile\n}\ntrap cleanup EXIT\n\n# Vérifier code retour:\nif command; then\n    echo \"Succès\"\nelse\n    echo \"Échec\"\nfi\n\n# Ou:\ncommand\nif [ $? -eq 0 ]; then\n    echo \"OK\"\nfi\n\n# Redirection erreurs:\ncommand 2>/dev/null  # Supprime stderr\ncommand > /dev/null 2>&1  # Supprime stdout + stderr\n\n# Debug mode:\nset -x  # Affiche commandes exécutées\ncommand1\ncommand2\nset +x  # Désactive debug\n\n# Ou lancer script:\nbash -x script.sh\n\n# Logging:\nlog() {\n    echo \"[$(date +'%Y-%m-%d %H:%M:%S')] $*\" | tee -a /var/log/script.log\n}\n\nlog \"Script démarré\"\nlog \"Traitement...\"\n\n# Assert:\nassert() {\n    if ! \"$@\"; then\n        echo \"Assertion failed: $*\" >&2\n        exit 1\n    fi\n}\n\nassert [ -f \"/etc/passwd\" ]"
            },
            {
                "title": "Exemple Script Complet",
                "code": "#!/bin/bash\n# Script backup automatique\n\nset -euo pipefail  # Strict mode\n\n# Config\nBACKUP_DIR=\"/backup\"\nSOURCE=\"/home/user/documents\"\nDATE=$(date +%Y%m%d)\nLOGFILE=\"/var/log/backup.log\"\nMAX_BACKUPS=7\n\n# Logging\nlog() {\n    echo \"[$(date +'%Y-%m-%d %H:%M:%S')] $*\" | tee -a \"$LOGFILE\"\n}\n\n# Cleanup\ncleanup() {\n    log \"Nettoyage temporaires...\"\n    # Supprimer fichiers temp si existent\n}\ntrap cleanup EXIT\n\n# Vérifications\nif [ ! -d \"$SOURCE\" ]; then\n    log \"ERREUR: Source $SOURCE n'existe pas\"\n    exit 1\nfi\n\nmkdir -p \"$BACKUP_DIR\"\n\n# Backup\nlog \"Début backup: $SOURCE\"\n\nBACKUP_FILE=\"$BACKUP_DIR/backup_$DATE.tar.gz\"\n\nif tar -czf \"$BACKUP_FILE\" -C \"$(dirname \"$SOURCE\")\" \"$(basename \"$SOURCE\")\"; then\n    SIZE=$(du -h \"$BACKUP_FILE\" | cut -f1)\n    log \"Backup réussi: $BACKUP_FILE ($SIZE)\"\nelse\n    log \"ERREUR backup!\"\n    exit 1\nfi\n\n# Rotation (garder derniers X backups)\nlog \"Rotation backups...\"\ncd \"$BACKUP_DIR\"\nls -t backup_*.tar.gz | tail -n +$((MAX_BACKUPS + 1)) | xargs -r rm -f\nlog \"$(ls -1 backup_*.tar.gz | wc -l) backups conservés\"\n\nlog \"Backup terminé avec succès\"\n\n# Utilisation:\n# chmod +x backup.sh\n# ./backup.sh\n# Ou cron: 0 2 * * * /path/to/backup.sh"
            },
            {
                "info": "💡 Toujours: set -euo pipefail en début script! Évite erreurs silencieuses. chmod +x script.sh pour rendre exécutable."
            },
            {
                "warning": "⚠️ Quotes critiques! \"$VAR\" vs $VAR: Avec guillemets évite word splitting. TOUJOURS quoter variables avec espaces possibles!"
            },
            {
                "warning": "⚠️ rm -rf $VAR/ SANS quotes = DANGER! $VAR vide → rm -rf / (destruction système). TOUJOURS: rm -rf \"${VAR}/\""
            }
        ]
    },

    "linux_cron": {
        "title": "⏰ Cron - Tâches Planifiées",
        "sections": [
            {
                "title": "Cron - Syntaxe de Base",
                "code": "# Format crontab:\n# Min  Hour  Day  Month  Weekday  Command\n#  0-59 0-23  1-31 1-12   0-7\n# (0 = Dimanche, 7 = Dimanche aussi)\n\n# Éditer crontab user:\ncrontab -e\n\n# Lister crontab:\ncrontab -l\n\n# Supprimer crontab:\ncrontab -r\n\n# Crontab autre user (root):\nsudo crontab -u alice -e\n\n# Exemples:\n# Tous les jours 2h30:\n30 2 * * * /path/to/script.sh\n\n# Toutes les heures:\n0 * * * * /path/to/script.sh\n\n# Toutes les 15 minutes:\n*/15 * * * * /path/to/script.sh\n\n# Lundi-Vendredi 9h:\n0 9 * * 1-5 /path/to/script.sh\n\n# 1er jour du mois:\n0 0 1 * * /path/to/script.sh\n\n# Dimanche minuit:\n0 0 * * 0 /path/to/script.sh\n\n# Au reboot:\n@reboot /path/to/script.sh\n\n# Raccourcis:\n@yearly   # 0 0 1 1 *\n@monthly  # 0 0 1 * *\n@weekly   # 0 0 * * 0\n@daily    # 0 0 * * *\n@hourly   # 0 * * * *\n@reboot   # Au démarrage"
            },
            {
                "title": "Crontab - Exemples Pratiques",
                "code": "# Backup quotidien 3h:\n0 3 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1\n\n# Nettoyage cache hebdomadaire (dimanche 4h):\n0 4 * * 0 find /tmp -type f -mtime +7 -delete\n\n# Check disk space toutes les 6h:\n0 */6 * * * df -h | mail -s \"Disk Space\" admin@example.com\n\n# Update packages (Ubuntu) quotidien 2h:\n0 2 * * * apt update && apt upgrade -y >> /var/log/updates.log 2>&1\n\n# Restart service toutes les 4h:\n0 */4 * * * systemctl restart myservice\n\n# Archive logs mensuels (1er du mois):\n0 1 1 * * /usr/local/bin/archive-logs.sh\n\n# Variables environnement:\nPATH=/usr/local/bin:/usr/bin:/bin\nSHELL=/bin/bash\nMAILTO=admin@example.com\n\n0 2 * * * /path/to/script.sh\n\n# Redirection output:\n# >> log: Append\n# > log: Overwrite\n# 2>&1: stderr → stdout\n# 2>log: stderr uniquement\n# >/dev/null 2>&1: Supprime tout output\n\n# Exemple complet:\nPATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\nMAILTO=root\n\n# Backup quotidien\n0 2 * * * /usr/local/bin/daily-backup.sh >> /var/log/backup.log 2>&1\n\n# Cleanup hebdo\n0 3 * * 0 /usr/local/bin/cleanup.sh\n\n# Monitoring toutes les 5 min\n*/5 * * * * /usr/local/bin/monitor.sh >/dev/null 2>&1"
            },
            {
                "title": "Systemd Timers - Alternative Moderne",
                "code": "# Systemd timer = Alternative cron, plus features\n\n# Créer service: /etc/systemd/system/backup.service\n[Unit]\nDescription=Daily Backup\n\n[Service]\nType=oneshot\nUser=backup\nExecStart=/usr/local/bin/backup.sh\nStandardOutput=journal\nStandardError=journal\n\n# Créer timer: /etc/systemd/system/backup.timer\n[Unit]\nDescription=Daily Backup Timer\n\n[Timer]\nOnCalendar=daily\nPersistent=true\n\n[Install]\nWantedBy=timers.target\n\n# Activer:\nsudo systemctl daemon-reload\nsudo systemctl enable backup.timer\nsudo systemctl start backup.timer\n\n# Vérifier:\nsystemctl list-timers\nsystemctl status backup.timer\n\n# OnCalendar syntaxe:\n# OnCalendar=hourly          # Toutes les heures\n# OnCalendar=daily           # Quotidien minuit\n# OnCalendar=weekly          # Hebdo dimanche minuit\n# OnCalendar=monthly         # Mensuel 1er minuit\n# OnCalendar=*-*-* 02:00:00  # Quotidien 2h\n# OnCalendar=Mon 09:00       # Lundi 9h\n# OnCalendar=*:0/15          # Toutes les 15 min\n\n# OnBootSec:\n# OnBootSec=10min            # 10 min après boot\n\n# OnUnitActiveSec:\n# OnUnitActiveSec=1h         # 1h après dernière exécution\n\n# Logs:\njournalctl -u backup.service\njournalctl -u backup.timer\n\n# Avantages systemd:\n# - Logs centralisés (journalctl)\n# - Dépendances services\n# - RandomizedDelaySec (jitter)\n# - Persistent (rattrape si PC éteint)"
            },
            {
                "title": "Anacron - Tâches Différées",
                "code": "# Anacron = Cron pour machines pas toujours allumées\n# Rattrape tâches manquées\n\n# Config: /etc/anacrontab\n\n# Format:\n# period  delay  job-id  command\n# period: jours entre exécutions\n# delay: minutes attendre après boot\n# job-id: nom unique\n# command: commande\n\n# Exemples:\n1    5    daily-backup    /usr/local/bin/backup.sh\n7    10   weekly-update   apt update && apt upgrade -y\n30   15   monthly-clean   /usr/local/bin/cleanup.sh\n\n# @daily, @weekly, @monthly:\n@daily   10  daily-job   /path/to/script.sh\n\n# Vérifier:\nanacron -T  # Test syntaxe\nanacron -n  # Lancer immédiatement (debug)\n\n# Logs:\n/var/log/syslog\ngrep anacron /var/log/syslog\n\n# Ubuntu/Debian:\n# Anacron lancé quotidien via cron.daily\n# /etc/cron.daily/\n# /etc/cron.weekly/\n# /etc/cron.monthly/\n\n# Placer script exécutable dans dossier:\nsudo cp backup.sh /etc/cron.daily/\nsudo chmod +x /etc/cron.daily/backup.sh\n# Exécuté quotidien automatiquement"
            },
            {
                "title": "at - Tâche Unique",
                "code": "# at = Exécuter commande à moment précis (1 fois)\n\n# Installer:\nsudo apt install at -y\nsudo systemctl start atd\nsudo systemctl enable atd\n\n# Planifier tâche:\necho \"backup.sh\" | at 14:30\n# Ou interactif:\nat 14:30\nat> /usr/local/bin/backup.sh\nat> <Ctrl+D>\n\n# Syntaxes temps:\nat now + 1 hour\nat now + 30 minutes\nat 2:30 PM\nat 14:30 tomorrow\nat 10:00 AM 01/15/2024\nat midnight\nat noon\n\n# Lister tâches:\natq\n# Ou:\nat -l\n\n# Supprimer tâche:\natrm 1  # Numéro job\n\n# Voir détails job:\nat -c 1\n\n# Exemples:\n# Dans 5 minutes:\necho \"systemctl restart nginx\" | at now + 5 minutes\n\n# Demain 3h:\necho \"/usr/local/bin/maintenance.sh\" | at 3:00 AM tomorrow\n\n# Batch (si load < seuil):\necho \"heavy-task.sh\" | batch\n# Exécute quand load system bas\n\n# Script multi-lignes:\nat 22:00 <<EOF\ncd /var/www\ntar -czf backup.tar.gz html/\nmv backup.tar.gz /backup/\nEOF"
            },
            {
                "title": "Debugging Cron Jobs",
                "code": "# Problèmes courants cron:\n\n# 1. PATH différent:\n# Cron PATH minimal!\n# Solution: PATH complet en début crontab\nPATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n\n# Ou chemin absolu commandes:\n0 2 * * * /usr/bin/python3 /home/user/script.py\n\n# 2. Variables environnement manquantes:\n# Solution: Sourcer profil ou définir variables\n0 2 * * * source ~/.bashrc && /path/to/script.sh\n\n# Ou dans crontab:\nSHELL=/bin/bash\nHOME=/home/user\nUSER=user\n\n# 3. Permissions:\n# Vérifier script exécutable:\nchmod +x script.sh\n\n# 4. Logs cron:\n# Debian/Ubuntu:\ngrep CRON /var/log/syslog\nsudo tail -f /var/log/syslog | grep CRON\n\n# Fedora/RHEL:\nsudo journalctl -u crond -f\n\n# 5. Rediriger output:\n# Toujours rediriger stdout/stderr!\n0 2 * * * /path/to/script.sh >> /var/log/script.log 2>&1\n\n# 6. Test manuel:\n# Lancer commande comme cron le ferait:\nenv -i /bin/bash -c \"cd /home/user && ./script.sh\"\n# env -i = Environnement vide\n\n# 7. Email notifications:\n# Cron envoie email si output\nMAILTO=admin@example.com\n0 2 * * * /path/to/script.sh\n\n# Désactiver emails:\nMAILTO=\"\"\n# Ou:\n0 2 * * * /path/to/script.sh >/dev/null 2>&1\n\n# 8. Vérifier syntaxe:\n# Chaque ligne doit être valide\n# Test:\ncrontab -l  # Si erreur syntaxe = affichée"
            },
            {
                "info": "💡 Systemd timers > cron pour nouvelles configs! Logs intégrés, dépendances, persistent. Cron reste simple pour tâches basiques."
            },
            {
                "warning": "⚠️ Cron PATH minimal! Toujours chemins absolus: /usr/bin/python3, pas python3. Ou déclarer PATH en début crontab."
            },
            {
                "warning": "⚠️ Scripts cron DOIVENT rediriger output! Sinon email envoyé à chaque run. >> log.txt 2>&1 ou >/dev/null 2>&1."
            }
        ]
    },

    "linux_logs": {
        "title": "📋 Gestion des Logs Système",
        "sections": [
            {
                "title": "Journalctl - Logs Systemd",
                "code": "# journalctl = Lecteur logs systemd (moderne)\n\n# Tous logs:\njournalctl\n# Spacebar: page suivante\n# q: quitter\n\n# Logs récents:\njournalctl -n 50        # 50 dernières lignes\njournalctl -n 100\n\n# Follow (temps réel):\njournalctl -f\n# Comme tail -f\n\n# Boot actuel:\njournalctl -b\n# Boot précédent:\njournalctl -b -1\n# Lister boots:\njournalctl --list-boots\n\n# Depuis date/heure:\njournalctl --since \"2024-01-01\"\njournalctl --since \"2024-01-01 10:00\"\njournalctl --since \"1 hour ago\"\njournalctl --since yesterday\njournalctl --since \"10 minutes ago\"\n\n# Jusqu'à date:\njournalctl --until \"2024-01-02\"\n\n# Période:\njournalctl --since \"2024-01-01\" --until \"2024-01-02\"\n\n# Service spécifique:\njournalctl -u nginx\njournalctl -u nginx.service\njournalctl -u ssh\n\n# Plusieurs services:\njournalctl -u nginx -u ssh\n\n# Follow service:\njournalctl -u nginx -f\n\n# Priorité (syslog levels):\n# 0: emerg, 1: alert, 2: crit, 3: err\n# 4: warning, 5: notice, 6: info, 7: debug\njournalctl -p err       # Erreurs uniquement\njournalctl -p warning   # Warning + err + crit...\n\n# Kernel messages:\njournalctl -k\n# Équivalent: dmesg\n\n# User spécifique:\njournalctl _UID=1000\n\n# Process ID:\njournalctl _PID=1234\n\n# Executable:\njournalctl /usr/bin/python3\n\n# Output formats:\njournalctl -o json-pretty   # JSON\njournalctl -o short         # Court (défaut)\njournalctl -o verbose       # Détaillé\n\n# Disk usage:\njournalctl --disk-usage\n\n# Rotation/nettoyage:\nsudo journalctl --vacuum-time=3d    # Garder 3 jours\nsudo journalctl --vacuum-size=500M  # Max 500MB"
            },
            {
                "title": "Logs Traditionnels (/var/log/)",
                "code": "# Principaux fichiers logs:\n\n# Messages système:\n/var/log/syslog         # Debian/Ubuntu\n/var/log/messages       # Fedora/RHEL\n\n# Authentication:\n/var/log/auth.log       # Debian/Ubuntu (SSH, sudo, login)\n/var/log/secure         # Fedora/RHEL\n\n# Kernel:\n/var/log/kern.log\ndmesg                   # Kernel ring buffer\n\n# Boot:\n/var/log/boot.log\n\n# Cron:\n/var/log/cron           # Fedora\ngrep CRON /var/log/syslog  # Ubuntu\n\n# Apache/Nginx:\n/var/log/apache2/access.log\n/var/log/apache2/error.log\n/var/log/nginx/access.log\n/var/log/nginx/error.log\n\n# Mail:\n/var/log/mail.log\n\n# MySQL:\n/var/log/mysql/error.log\n\n# Lire logs:\ntail -f /var/log/syslog        # Follow\ntail -n 100 /var/log/syslog    # 100 dernières lignes\nhead -n 50 /var/log/syslog     # 50 premières lignes\n\n# Rechercher dans logs:\ngrep \"error\" /var/log/syslog\ngrep -i \"failed\" /var/log/auth.log  # Case insensitive\ngrep \"Jan 3\" /var/log/syslog\n\n# Multiples fichiers:\ngrep \"error\" /var/log/*.log\n\n# Compter occurrences:\ngrep -c \"error\" /var/log/syslog\n\n# Context lignes:\ngrep -A 5 -B 5 \"error\" /var/log/syslog\n# -A 5: 5 lignes après\n# -B 5: 5 lignes avant"
            },
            {
                "title": "Logrotate - Rotation Automatique",
                "code": "# logrotate = Rotation automatique logs (éviter remplir disque)\n\n# Config globale: /etc/logrotate.conf\n# Configs apps: /etc/logrotate.d/\n\n# Exemple config:\nsudo nano /etc/logrotate.d/myapp\n\n/var/log/myapp/*.log {\n    daily              # Rotation quotidienne\n    rotate 7           # Garder 7 versions\n    compress           # Compresser anciens\n    delaycompress      # Compress N-1 (pas dernier)\n    missingok          # Pas erreur si fichier absent\n    notifempty         # Pas rotation si vide\n    create 0640 user group  # Permissions nouveau fichier\n    sharedscripts      # Scripts 1 fois pour tous fichiers\n    postrotate\n        systemctl reload myapp\n    endscript\n}\n\n# Fréquences:\n# daily, weekly, monthly, yearly\n\n# Taille:\nsize 100M          # Rotation si >100MB\nminsize 10M        # Minimum 10MB même si daily\n\n# Nombre versions:\nrotate 10          # Garder 10 anciens\nmaxage 30          # Supprimer >30j\n\n# Compression:\ncompress\nnocompress\ndelaycompress      # Compress N-1\ncompresscmd gzip\ncompressoptions -9\n\n# Scripts:\nprerotate\n    # Avant rotation\nendscript\n\npostrotate\n    # Après rotation\n    systemctl reload nginx\nendscript\n\n# Tester config:\nsudo logrotate -d /etc/logrotate.d/myapp\n# -d: Debug (dry-run)\n\n# Forcer rotation:\nsudo logrotate -f /etc/logrotate.conf\n\n# Exemple Nginx:\n/var/log/nginx/*.log {\n    daily\n    rotate 14\n    compress\n    delaycompress\n    notifempty\n    create 0640 www-data adm\n    sharedscripts\n    postrotate\n        [ -f /var/run/nginx.pid ] && kill -USR1 $(cat /var/run/nginx.pid)\n    endscript\n}"
            },
            {
                "title": "Logger - Écrire dans Syslog",
                "code": "# logger = Écrire messages dans syslog depuis scripts\n\n# Message simple:\nlogger \"Mon message de log\"\n\n# Avec tag:\nlogger -t mon_script \"Backup démarré\"\n\n# Priorité:\nlogger -p user.info \"Info message\"\nlogger -p user.warning \"Warning message\"\nlogger -p user.err \"Error message\"\nlogger -p user.crit \"Critical!\"\n\n# Facilities:\n# user, daemon, local0-local7, etc.\n\n# Depuis script:\n#!/bin/bash\nLOG_TAG=\"backup_script\"\n\nlogger -t $LOG_TAG \"Début backup\"\n\nif backup_command; then\n    logger -t $LOG_TAG -p user.info \"Backup réussi\"\nelse\n    logger -t $LOG_TAG -p user.err \"Backup échoué\"\nfi\n\n# Voir dans journalctl:\njournalctl -t backup_script\n\n# Ou syslog:\ngrep backup_script /var/log/syslog\n\n# Logger depuis fichier:\nlogger -f /path/to/file.log\n\n# Logger stdin:\necho \"Message\" | logger -t mon_tag\n\n# Exemple monitoring:\n#!/bin/bash\nDISK_USE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')\n\nif [ $DISK_USE -gt 90 ]; then\n    logger -t disk_monitor -p user.warning \"Disk usage: ${DISK_USE}%\"\nfi"
            },
            {
                "title": "Rsyslog - Configuration Avancée",
                "code": "# rsyslog = Daemon logs système (remplace syslog)\n\n# Config: /etc/rsyslog.conf\n# Configs supplémentaires: /etc/rsyslog.d/\n\n# Format règles:\n# facility.priority    action\n\n# Exemples règles:\n# Tout vers fichier:\n*.*                     /var/log/all.log\n\n# Erreurs kernel:\nkern.err                /var/log/kernel-errors.log\n\n# Auth vers fichier séparé:\nauth,authpriv.*         /var/log/auth.log\n\n# Cron:\ncron.*                  /var/log/cron.log\n\n# Mail:\nmail.*                  /var/log/mail.log\n\n# Tous sauf mail:\n*.*;mail.none           /var/log/messages\n\n# Priorités multiples:\nkern.warning;*.err      /var/log/important.log\n\n# Remote logging (envoyer vers serveur):\n*.* @@remote-server:514\n# @ = UDP, @@ = TCP\n\n# Recevoir logs distant:\n# Activer dans /etc/rsyslog.conf:\nmodule(load=\"imudp\")\ninput(type=\"imudp\" port=\"514\")\n\nmodule(load=\"imtcp\")\ninput(type=\"imtcp\" port=\"514\")\n\n# Templates (format custom):\ntemplate(name=\"CustomFormat\" type=\"string\"\n         string=\"%TIMESTAMP% %HOSTNAME% %syslogtag%%msg%\\n\")\n\n*.* /var/log/custom.log;CustomFormat\n\n# Redémarrer rsyslog:\nsudo systemctl restart rsyslog\n\n# Tester config:\nrsyslogd -N1\n\n# Debug:\nrsyslogd -d"
            },
            {
                "title": "Analyse Logs - Outils",
                "code": "# grep - Recherche basique:\ngrep \"error\" /var/log/syslog\ngrep -E \"error|fail|critical\" /var/log/syslog  # Regex\ngrep -v \"INFO\" /var/log/app.log  # Inverse (exclure)\n\n# awk - Extraction colonnes:\nawk '{print $1, $5}' /var/log/syslog  # Colonnes 1 et 5\nawk '/error/ {print $0}' /var/log/syslog  # Lignes avec \"error\"\n\n# sed - Remplacement:\nsed 's/ERROR/ERREUR/g' /var/log/app.log\n\n# cut - Découper:\ncut -d' ' -f1-3 /var/log/syslog  # 3 premiers champs\n\n# sort - Trier:\nsort /var/log/app.log\nsort -r /var/log/app.log  # Inverse\n\n# uniq - Unique (après sort!):\nsort /var/log/app.log | uniq\nsort /var/log/app.log | uniq -c  # Avec comptage\n\n# Exemple: Top 10 IPs (access.log):\nawk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10\n\n# Exemple: Erreurs par heure:\ngrep \"error\" /var/log/app.log | awk '{print $1, $2}' | cut -d: -f1 | sort | uniq -c\n\n# Multitail - Follow plusieurs logs:\nsudo apt install multitail -y\nmultitail /var/log/syslog /var/log/auth.log\n\n# lnav - Log navigator (viewer interactif):\nsudo apt install lnav -y\nlnav /var/log/syslog /var/log/auth.log\n# Chercher: /, Filtre: TAB, Quit: q\n\n# ccze - Coloriser logs:\nsudo apt install ccze -y\ntail -f /var/log/syslog | ccze -A\n\n# GoAccess - Analyse access.log (web UI):\nsudo apt install goaccess -y\ngoaccess /var/log/nginx/access.log -o report.html\n# Dashboard HTML généré"
            },
            {
                "info": "💡 journalctl -f = tail -f moderne! Système récent = journald (binaire), ancien = /var/log/ (texte). Les deux coexistent."
            },
            {
                "warning": "⚠️ Logs non rotatés = disque plein! Vérifier logrotate actif: systemctl status logrotate.timer. Configurer rotation pour apps custom."
            },
            {
                "warning": "⚠️ Logs sensibles (passwords, tokens) dans /var/log/! Restreindre permissions: chmod 600. Nettoyer régulièrement. RGPD applicable!"
            }
        ]
    },

    "linux_boot": {
        "title": "🚀 Processus de Boot & GRUB",
        "sections": [
            {
                "title": "Processus de Boot Linux",
                "bullets": [
                    "1. BIOS/UEFI: Charge bootloader (GRUB) depuis disque",
                    "2. GRUB: Menu démarrage, charge kernel + initramfs",
                    "3. Kernel: Init hardware, monte initramfs",
                    "4. Initramfs: Drivers essentiels, monte / (root)",
                    "5. Systemd (init): PID 1, démarre services",
                    "6. Login: getty/lightdm/gdm/sddm",
                    "",
                    "Temps boot:",
                    "• systemd-analyze: Affiche durée boot",
                    "• systemd-analyze blame: Services lents"
                ]
            },
            {
                "title": "GRUB - Configuration",
                "code": "# Fichier config: /etc/default/grub\n\nsudo nano /etc/default/grub\n\n# Options importantes:\nGRUB_DEFAULT=0              # Entrée par défaut (0=première)\nGRUB_TIMEOUT=5              # Délai menu (secondes)\nGRUB_TIMEOUT_STYLE=menu     # menu ou hidden\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash\"  # Params kernel\nGRUB_CMDLINE_LINUX=\"\"       # Params kernel (toujours)\nGRUB_GFXMODE=1920x1080      # Résolution GRUB\nGRUB_DISABLE_RECOVERY=false # Afficher mode recovery\n\n# Désactiver submenu:\nGRUB_DISABLE_SUBMENU=y\n\n# OS Prober (dual-boot Windows):\nGRUB_DISABLE_OS_PROBER=false  # true=désactive détection\n\n# Appliquer changements:\nsudo update-grub           # Debian/Ubuntu\n# Ou:\nsudo grub-mkconfig -o /boot/grub/grub.cfg  # Fedora/Arch\n\n# Vérifier entrées GRUB:\ngrep menuentry /boot/grub/grub.cfg\n\n# Sélectionner entrée par nom:\nGRUB_DEFAULT=\"Advanced options>Ubuntu, kernel 5.15\"\n\n# Toujours booter dernier kernel:\nGRUB_DEFAULT=saved\nGRUB_SAVEDEFAULT=true"
            },
            {
                "title": "GRUB - Édition au Boot",
                "code": "# Au menu GRUB:\n# Appuyer 'e' sur entrée pour éditer\n\n# Ligne commençant par 'linux':\nlinux /vmlinuz-5.15.0-generic root=UUID=abc-123 ro quiet splash\n\n# Modifications courantes:\n\n# Mode single user (recovery):\n# Ajouter à fin ligne linux:\nsingle\n# Ou:\nsystemd.unit=rescue.target\n\n# Mode emergency:\nsystemd.unit=emergency.target\n\n# Désactiver quiet/splash (voir boot messages):\n# Supprimer: quiet splash\n\n# Changer root password oublié:\n# Ajouter à fin ligne linux:\ninit=/bin/bash\n# Ctrl+X pour booter\n# Puis:\nmount -o remount,rw /\npasswd root\nexec /sbin/init\n\n# Boot verbose (debug):\n# Remplacer quiet par:\nsystemd.log_level=debug systemd.log_target=console\n\n# Désactiver GPU:\n# Ajouter:\nnomodeset\n# Ou (NVIDIA):\nnvidia.modeset=0\n\n# Après éditions: Ctrl+X pour booter\n# ⚠️ Changements temporaires! Pas sauvegardés."
            },
            {
                "title": "GRUB - Réinstallation",
                "code": "# Réinstaller GRUB (si cassé)\n\n# Boot sur live USB\n\n# 1. Identifier partitions:\nsudo fdisk -l\nlsblk\n# Trouver partition root (/) et EFI\n\n# 2. Monter partition root:\nsudo mount /dev/sda2 /mnt\n\n# 3. Si UEFI, monter EFI:\nsudo mount /dev/sda1 /mnt/boot/efi\n\n# 4. Chroot:\nsudo mount --bind /dev /mnt/dev\nsudo mount --bind /proc /mnt/proc\nsudo mount --bind /sys /mnt/sys\nsudo chroot /mnt\n\n# 5. Réinstaller GRUB:\n# BIOS:\ngrub-install /dev/sda\n# UEFI:\ngrub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ubuntu\n\n# 6. Regénérer config:\nupdate-grub\n# Ou:\ngrub-mkconfig -o /boot/grub/grub.cfg\n\n# 7. Sortir chroot + reboot:\nexit\nsudo umount /mnt/boot/efi\nsudo umount /mnt/dev\nsudo umount /mnt/proc\nsudo umount /mnt/sys\nsudo umount /mnt\nsudo reboot\n\n# Vérifier boot order (UEFI):\nefibootmgr -v\n\n# Changer ordre:\nsudo efibootmgr -o 0001,0000,0002"
            },
            {
                "title": "Kernel Parameters",
                "code": "# Params kernel permanents: /etc/default/grub\n\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash param1=value param2\"\n\n# Exemples params utiles:\n\n# nomodeset: Désactive KMS (problèmes GPU)\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash nomodeset\"\n\n# acpi=off: Désactive ACPI (problèmes hardware ancien)\nacpi=off\n\n# noapic: Désactive APIC\nnoapic\n\n# pci=nomsi: Désactive MSI (problèmes PCI)\npci=nomsi\n\n# i915.modeset=1: Force Intel GPU\ni915.modeset=1\n\n# nvidia-drm.modeset=1: NVIDIA modesetting\nnvidia-drm.modeset=1\n\n# amd_iommu=on: AMD IOMMU (virtualisation)\namd_iommu=on intel_iommu=on\n\n# mitigations=off: Désactive Spectre/Meltdown (perf++, sécurité--)\nmitigations=off\n\n# elevator=deadline: I/O scheduler\nelevator=deadline\n\n# Appliquer:\nsudo update-grub\nsudo reboot\n\n# Voir params kernel actuel:\ncat /proc/cmdline\n\n# Modifier temporaire (boot actuel):\n# Éditer GRUB au boot (voir section précédente)"
            },
            {
                "title": "Initramfs - Initial RAM Filesystem",
                "code": "# Initramfs = Filesystem temporaire au boot\n# Contient drivers essentiels pour monter /\n\n# Regénérer initramfs:\n# Ubuntu/Debian:\nsudo update-initramfs -u\n# -u: Update\n# -c: Create\n# -k all: Tous kernels\n\n# Kernel spécifique:\nsudo update-initramfs -u -k 5.15.0-generic\n\n# Fedora/RHEL:\nsudo dracut --force\n\n# Arch:\nsudo mkinitcpio -P  # Tous kernels\nsudo mkinitcpio -p linux  # Kernel linux\n\n# Localisation initramfs:\nls -lh /boot/initrd.img*      # Ubuntu\nls -lh /boot/initramfs*       # Fedora/Arch\n\n# Lister contenu initramfs:\nlsinitramfs /boot/initrd.img-5.15.0-generic\n\n# Ou extraire:\nmkdir /tmp/initramfs\ncd /tmp/initramfs\nunmkinitramfs /boot/initrd.img-5.15.0-generic .\n\n# Config initramfs (Ubuntu):\nsudo nano /etc/initramfs-tools/initramfs.conf\n\n# MODULES=most  # Inclure beaucoup modules\n# MODULES=dep   # Seulement dépendances (plus léger)\n# MODULES=list  # Liste custom\n\n# Hooks (scripts exécutés génération):\nls /etc/initramfs-tools/hooks/\n\n# Quand regénérer:\n# - Nouveau kernel installé (auto)\n# - Modif /etc/crypttab (LUKS)\n# - Modif /etc/mdadm/mdadm.conf (RAID)\n# - Ajout module custom"
            },
            {
                "title": "Systemd Analyze - Boot Performance",
                "code": "# Temps boot total:\nsystemd-analyze\n# Startup finished in 2.5s (kernel) + 8.3s (userspace) = 10.8s\n\n# Services par temps démarrage:\nsystemd-analyze blame\n# Liste services tri par durée\n\n# Chaîne critique (services bloquants):\nsystemd-analyze critical-chain\n# Affiche dépendances ralentissant boot\n\n# Service spécifique:\nsystemd-analyze critical-chain nginx.service\n\n# Graphique boot (SVG):\nsystemd-analyze plot > boot.svg\n# Ouvrir boot.svg dans navigateur\n\n# Vérifier config systemd:\nsystemd-analyze verify /etc/systemd/system/myservice.service\n\n# Security analysis:\nsystemd-analyze security nginx.service\n# Score sécurité + recommandations\n\n# Temps par target:\nsystemd-analyze blame | head -20\n\n# Optimisations boot:\n# 1. Désactiver services inutiles:\nsudo systemctl disable bluetooth.service\nsudo systemctl disable cups.service  # Imprimante\n\n# 2. Paralléliser (systemd fait déjà!)\n\n# 3. Mask services vraiment inutiles:\nsudo systemctl mask plymouth.service  # Boot splash\n\n# 4. Vérifier NetworkManager:\n# Si lent, changer timeout:\nsudo nano /etc/systemd/system/network-online.target.wants/NetworkManager-wait-online.service\n# TimeoutStartSec=2sec"
            },
            {
                "info": "💡 systemd-analyze blame = votre ami! Désactivez services inutiles (Bluetooth, cups si pas imprimante). Boot <10s possible SSD."
            },
            {
                "warning": "⚠️ GRUB: update-grub REQUIS après /etc/default/grub! Sinon changements ignorés. Backup config avant modif: cp /boot/grub/grub.cfg /boot/grub/grub.cfg.bak"
            },
            {
                "warning": "⚠️ Kernel params: mitigations=off = DANGER sécurité! Performance +5-10% mais vulnérable Spectre/Meltdown. NE PAS utiliser serveur public!"
            }
        ]
    },

    "linux_kernel": {
        "title": "🔧 Gestion du Kernel Linux",
        "sections": [
            {
                "title": "Kernel Linux - Concepts",
                "content": "Kernel = Cœur système Linux, interface hardware/software. Versions: 5.15, 6.1, 6.6 (Stable), 6.7-rc (Testing). LTS (Long Term Support) = 5.15, 6.1, 6.6 (support 2-6 ans). Mainline = Dernière version stable. Types: Stock (distribution), Lowlatency (audio/gaming), Realtime (industriel), Zen/Liquorix (desktop optimisé). Modules = Drivers chargeables (lsmod, modprobe)."
            },
            {
                "title": "Versions Kernel",
                "code": "# Version kernel actuel:\nuname -r\n# 5.15.0-91-generic\n\n# Détails complets:\nuname -a\n# Linux hostname 5.15.0-91-generic #101-Ubuntu SMP x86_64 GNU/Linux\n\n# Lister kernels installés:\n# Ubuntu/Debian:\ndpkg --list | grep linux-image\n\n# Fedora:\nsudo dnf list installed kernel*\n\n# Arch:\npacman -Q linux\n\n# Fichiers kernel:\nls -lh /boot/vmlinuz*     # Kernel binary\nls -lh /boot/initrd.img*  # Initramfs\nls -lh /boot/config*      # Config kernel\n\n# Modules kernel:\nls /lib/modules/\n# Dossier par version kernel\n\n# Config kernel actuel:\ncat /boot/config-$(uname -r)\n# Ou:\nzcat /proc/config.gz  # Si activé"
            },
            {
                "title": "Installer/Supprimer Kernels",
                "code": "# Ubuntu/Debian - Installer kernel:\nsudo apt update\nsudo apt install linux-image-generic  # Dernier stable\nsudo apt install linux-image-5.15.0-91-generic  # Version spécifique\n\n# Kernel lowlatency (gaming/audio):\nsudo apt install linux-lowlatency\n\n# Kernel HWE (Hardware Enablement - nouveau hardware):\nsudo apt install linux-generic-hwe-22.04\n\n# Fedora:\nsudo dnf install kernel\n# Garde anciens kernels auto\n\n# Arch:\nsudo pacman -S linux        # Stable\nsudo pacman -S linux-lts    # LTS\nsudo pacman -S linux-zen    # Optimisé desktop\n\n# Supprimer vieux kernels:\n# Ubuntu/Debian:\nsudo apt autoremove --purge\n# Supprime kernels obsolètes\n\n# Manuel:\nsudo apt remove linux-image-5.15.0-50-generic\nsudo apt remove linux-headers-5.15.0-50-generic\n\n# ⚠️ GARDEZ AU MOINS 2 KERNELS!\n# Si nouveau kernel problème = boot ancien\n\n# Vérifier GRUB après install:\nsudo update-grub\n\n# Reboot + choisir kernel dans GRUB Advanced Options"
            },
            {
                "title": "Modules Kernel",
                "code": "# Lister modules chargés:\nlsmod\n# Module, Size, Used by\n\n# Détails module:\nmodinfo nvidia\nmodinfo e1000e  # Driver Ethernet Intel\n\n# Charger module:\nsudo modprobe module_name\nsudo modprobe nvidia\n\n# Décharger module:\nsudo modprobe -r module_name\nsudo rmmod module_name  # Force\n\n# ⚠️ rmmod échoue si module utilisé!\n# Vérifier dépendances:\nlsmod | grep module_name\n\n# Charger module au boot:\nsudo nano /etc/modules-load.d/mymodule.conf\n# Ajouter:\nmodule_name\n\n# Blacklister module (empêcher chargement):\nsudo nano /etc/modprobe.d/blacklist.conf\n# Ajouter:\nblacklist module_name\n\n# Exemple blacklist Nouveau (GPU NVIDIA):\nblacklist nouveau\noptions nouveau modeset=0\n\n# Appliquer blacklist:\nsudo update-initramfs -u\nsudo reboot\n\n# Modules chargés au boot:\ndmesg | grep -i module\n\n# Localisation modules:\nls /lib/modules/$(uname -r)/kernel/drivers/\n# net/, gpu/, usb/, etc.\n\n# Dépendances modules:\nmodprobe --show-depends module_name\n\n# Paramètres module:\nsudo modprobe module_name param1=value param2=value\n\n# Permanent:\nsudo nano /etc/modprobe.d/module_name.conf\noptions module_name param1=value\n\n# Exemple NVIDIA:\noptions nvidia NVreg_UsePageAttributeTable=1"
            },
            {
                "title": "Compiler Kernel Custom",
                "code": "# ⚠️ Avancé! Généralement inutile.\n# Distributions fournissent kernels optimisés.\n\n# Dépendances build (Ubuntu):\nsudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev\n\n# Télécharger source:\nwget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.6.tar.xz\ntar -xf linux-6.6.tar.xz\ncd linux-6.6\n\n# Config kernel:\n# Copier config actuelle:\ncp /boot/config-$(uname -r) .config\n\n# Menuconfig (interface):\nmake menuconfig\n# Naviguer options, activer/désactiver modules\n\n# Ou config automatique:\nmake olddefconfig  # Défauts pour nouvelles options\n\n# Compiler:\nmake -j$(nproc)  # Utilise tous CPU cores\n# Durée: 30min-2h selon CPU\n\n# Installer modules:\nsudo make modules_install\n\n# Installer kernel:\nsudo make install\n# Copie vers /boot/, update initramfs + GRUB\n\n# Ou créer .deb (Ubuntu):\nmake -j$(nproc) bindeb-pkg\n# Crée .deb dans dossier parent\nsudo dpkg -i ../linux-image*.deb\n\n# Reboot + tester:\nsudo reboot\nuname -r  # Vérifier version\n\n# Si problème:\n# Boot ancien kernel (GRUB Advanced Options)\n# Supprimer kernel custom:\nsudo apt remove linux-image-6.6.0"
            },
            {
                "title": "Kernel Parameters Runtime",
                "code": "# sysctl = Modifier params kernel runtime\n\n# Lister tous params:\nsysctl -a\n\n# Param spécifique:\nsysctl vm.swappiness\n# vm.swappiness = 60\n\n# Modifier temporaire:\nsudo sysctl vm.swappiness=10\n\n# Permanent:\nsudo nano /etc/sysctl.conf\n# Ajouter:\nvm.swappiness=10\nnet.ipv4.ip_forward=1\n\n# Ou fichier dédié:\nsudo nano /etc/sysctl.d/99-custom.conf\nvm.swappiness=10\n\n# Appliquer sans reboot:\nsudo sysctl -p\n# Ou:\nsudo sysctl --system\n\n# Params utiles:\n\n# Swappiness (0-100):\nvm.swappiness=10\n\n# File handles max:\nfs.file-max=2097152\n\n# IP forwarding (routeur):\nnet.ipv4.ip_forward=1\nnet.ipv6.conf.all.forwarding=1\n\n# TCP tuning:\nnet.core.rmem_max=16777216\nnet.core.wmem_max=16777216\nnet.ipv4.tcp_rmem=4096 87380 16777216\nnet.ipv4.tcp_wmem=4096 65536 16777216\n\n# Désactiver IPv6:\nnet.ipv6.conf.all.disable_ipv6=1\nnet.ipv6.conf.default.disable_ipv6=1\n\n# SYN flood protection:\nnet.ipv4.tcp_syncookies=1\n\n# Kernel panic auto-reboot:\nkernel.panic=10  # Reboot après 10s\n\n# Core dumps:\nkernel.core_pattern=/tmp/core-%e-%p\n\n# Voir param runtime:\ncat /proc/sys/vm/swappiness\ncat /proc/sys/net/ipv4/ip_forward"
            },
            {
                "title": "Dmesg - Kernel Messages",
                "code": "# dmesg = Kernel ring buffer (messages boot/hardware)\n\n# Tous messages:\ndmesg\n\n# Derniers messages:\ndmesg | tail -50\n\n# Follow (temps réel):\nsudo dmesg -w\n# Comme tail -f\n\n# Human-readable timestamps:\ndmesg -T\n\n# Filtrer par niveau:\ndmesg --level=err,warn  # Erreurs + warnings\ndmesg --level=err       # Erreurs uniquement\n\n# Niveaux:\n# emerg, alert, crit, err, warn, notice, info, debug\n\n# Facility (subsystem):\ndmesg --facility=kern   # Kernel\ndmesg --facility=user   # Userspace\n\n# Chercher:\ndmesg | grep -i usb\ndmesg | grep -i error\ndmesg | grep -i nvidia\n\n# Clear buffer:\nsudo dmesg -C\n\n# Exemples diagnostics:\n\n# Problèmes USB:\ndmesg | grep -i usb\n\n# Erreurs disk:\ndmesg | grep -i \"ata\\|sda\\|nvme\"\n\n# GPU:\ndmesg | grep -i \"nvidia\\|amdgpu\\|i915\"\n\n# Réseau:\ndmesg | grep -i \"eth0\\|wlan\\|network\"\n\n# OOM (Out of Memory):\ndmesg | grep -i \"killed process\"\n\n# Hardware errors:\ndmesg | grep -i \"mce\\|hardware error\"\n\n# Sauvegarder logs:\ndmesg > ~/dmesg-$(date +%Y%m%d).log"
            },
            {
                "info": "💡 Kernel LTS (5.15, 6.1, 6.6) = Stabilité. Mainline = Nouvelles features. Desktop: LTS suffisant. Gaming récent: Mainline ou Zen."
            },
            {
                "warning": "⚠️ Gardez MINIMUM 2 kernels installés! Nouveau kernel bug = boot impossible. GRUB Advanced Options = sauveur."
            },
            {
                "warning": "⚠️ Compiler kernel custom = risqué! Distribution kernels déjà optimisés. Compilation ratée = system unboo table. Testez VM d'abord!"
            }
        ]
    },

    "linux_server": {
        "title": "🖥️ Administration Serveur Linux",
        "sections": [
            {
                "title": "Serveur Linux - Bonnes Pratiques",
                "bullets": [
                    "Sécurité FIRST:",
                    "• SSH clés uniquement (pas password)",
                    "• Firewall actif (ufw/iptables)",
                    "• fail2ban contre brute-force",
                    "• Updates automatiques sécurité",
                    "",
                    "Monitoring:",
                    "• Logs centralisés",
                    "• Alertes disk/RAM/CPU",
                    "• Uptime monitoring",
                    "",
                    "Backups:",
                    "• Automatisés quotidien",
                    "• Testés régulièrement",
                    "• Off-site (cloud/autre serveur)",
                    "",
                    "Documentation:",
                    "• Procédures écrites",
                    "• Runbooks incidents",
                    "• Contacts urgence"
                ]
            },
            {
                "title": "Monitoring Système",
                "code": "# htop - Monitoring interactif:\nsudo apt install htop -y\nhtop\n# F6: Tri, F9: Kill, F5: Tree, q: Quit\n\n# Disk usage:\ndf -h                    # Partitions\ndu -sh /*                # Dossiers racine\ndu -sh /var/* | sort -rh | head -10  # Top 10\n\n# Inodes (fichiers):\ndf -i\n# Inodes épuisés = cannot create file (même si espace!)\n\n# I/O disk:\nsudo iotop -o  # Seulement processus actifs I/O\n\n# Réseau:\nss -tuln               # Ports listening\nss -tulnp              # + PIDs\nss -s                  # Statistiques\n\n# Bandwidth:\nsudo apt install iftop -y\nsudo iftop -i eth0\n\n# Uptime + load:\nuptime\n# Load average: 1.5, 1.2, 1.0 (1min, 5min, 15min)\n# > CPU cores = surcharge\n\n# RAM:\nfree -h\n# Available = RAM réellement dispo\n\n# Processus:\nps auxf                # Tree\nps aux --sort=-%cpu | head -10  # Top CPU\nps aux --sort=-%mem | head -10  # Top RAM\n\n# Logs temps réel:\njournalctl -f\ntail -f /var/log/syslog\n\n# Check ports:\nsudo netstat -tulnp\n# Ou:\nsudo lsof -i -P -n | grep LISTEN"
            },
            {
                "title": "Nginx - Serveur Web",
                "code": "# Installer Nginx:\nsudo apt update\nsudo apt install nginx -y\n\n# Démarrer:\nsudo systemctl start nginx\nsudo systemctl enable nginx\n\n# Status:\nsudo systemctl status nginx\n\n# Tester config:\nsudo nginx -t\n\n# Recharger config (sans downtime):\nsudo systemctl reload nginx\n\n# Restart:\nsudo systemctl restart nginx\n\n# Config principale:\nsudo nano /etc/nginx/nginx.conf\n\n# Sites:\n/etc/nginx/sites-available/  # Configs disponibles\n/etc/nginx/sites-enabled/    # Configs actives (symlinks)\n\n# Créer site:\nsudo nano /etc/nginx/sites-available/monsite\n\nserver {\n    listen 80;\n    server_name exemple.com www.exemple.com;\n    \n    root /var/www/monsite;\n    index index.html index.php;\n    \n    location / {\n        try_files $uri $uri/ =404;\n    }\n    \n    # PHP-FPM:\n    location ~ \\.php$ {\n        include snippets/fastcgi-php.conf;\n        fastcgi_pass unix:/run/php/php8.1-fpm.sock;\n    }\n    \n    # Logs:\n    access_log /var/log/nginx/monsite-access.log;\n    error_log /var/log/nginx/monsite-error.log;\n}\n\n# Activer site:\nsudo ln -s /etc/nginx/sites-available/monsite /etc/nginx/sites-enabled/\nsudo nginx -t\nsudo systemctl reload nginx\n\n# Désactiver site:\nsudo rm /etc/nginx/sites-enabled/monsite\nsudo systemctl reload nginx\n\n# Logs:\ntail -f /var/log/nginx/access.log\ntail -f /var/log/nginx/error.log\n\n# HTTPS (Let's Encrypt):\nsudo apt install certbot python3-certbot-nginx -y\nsudo certbot --nginx -d exemple.com -d www.exemple.com\n# Suit wizard, renouvelle auto"
            },
            {
                "title": "MySQL/MariaDB - Base de Données",
                "code": "# Installer MariaDB:\nsudo apt install mariadb-server -y\n\n# Démarrer:\nsudo systemctl start mariadb\nsudo systemctl enable mariadb\n\n# Sécuriser installation:\nsudo mysql_secure_installation\n# Root password, remove anonymous, disable remote root, etc.\n\n# Login:\nsudo mysql\n# Ou:\nmysql -u root -p\n\n# Créer database:\nCREATE DATABASE wordpress;\n\n# Créer user:\nCREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'password';\n\n# Permissions:\nGRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost';\nFLUSH PRIVILEGES;\n\n# Lister databases:\nSHOW DATABASES;\n\n# Lister users:\nSELECT User, Host FROM mysql.user;\n\n# Sortir:\nEXIT;\n\n# Backup database:\nmysqldump -u root -p wordpress > wordpress-$(date +%Y%m%d).sql\n\n# Backup toutes databases:\nmysqldump -u root -p --all-databases > all-db-$(date +%Y%m%d).sql\n\n# Restaurer:\nmysql -u root -p wordpress < wordpress-backup.sql\n\n# Remote access (⚠️ sécurité!):\nsudo nano /etc/mysql/mariadb.conf.d/50-server.cnf\n# Commenter:\n# bind-address = 127.0.0.1\n\n# Créer user remote:\nCREATE USER 'remote'@'%' IDENTIFIED BY 'password';\nGRANT ALL PRIVILEGES ON *.* TO 'remote'@'%';\nFLUSH PRIVILEGES;\n\n# Firewall:\nsudo ufw allow 3306/tcp\n\nsudo systemctl restart mariadb\n\n# Logs:\nsudo tail -f /var/log/mysql/error.log\n\n# Performance:\nsudo mysqltuner\n# Recommandations config"
            },
            {
                "title": "SSH - Accès Distant Sécurisé",
                "code": "# Installer SSH server:\nsudo apt install openssh-server -y\n\n# Démarrer:\nsudo systemctl start ssh\nsudo systemctl enable ssh\n\n# Config:\nsudo nano /etc/ssh/sshd_config\n\n# Sécurité recommandée:\nPort 2222                      # Changer port\nPermitRootLogin no             # Bloquer root\nPasswordAuthentication no      # Clés SSH uniquement\nPubkeyAuthentication yes\nPermitEmptyPasswords no\nX11Forwarding no\nMaxAuthTries 3\nAllowUsers alice bob           # Whitelist\nClientAliveInterval 300\nClientAliveCountMax 2\n\n# Appliquer:\nsudo systemctl restart sshd\n\n# ⚠️ Tester AVANT fermer session!\nssh -p 2222 user@localhost\n\n# Générer clés SSH (client):\nssh-keygen -t ed25519 -C \"mon@email.com\"\n\n# Copier clé publique vers serveur:\nssh-copy-id -p 2222 user@serveur\n\n# Connexion:\nssh -p 2222 user@serveur\n\n# Config client (~/.ssh/config):\nHost monserveur\n    HostName 1.2.3.4\n    Port 2222\n    User alice\n    IdentityFile ~/.ssh/id_ed25519\n\n# Connexion simplifiée:\nssh monserveur\n\n# Tunneling SSH:\n# Local forward:\nssh -L 8080:localhost:80 user@serveur\n# localhost:8080 → serveur:80\n\n# Remote forward:\nssh -R 8080:localhost:80 user@serveur\n# serveur:8080 → localhost:80\n\n# SOCKS proxy:\nssh -D 1080 user@serveur\n\n# SCP (copie fichiers):\nscp fichier.txt user@serveur:/path/\nscp -r dossier/ user@serveur:/path/\n\n# SFTP:\nsftp user@serveur\n# put fichier.txt\n# get fichier.txt\n# exit\n\n# Logs SSH:\nsudo tail -f /var/log/auth.log"
            },
            {
                "title": "Systemd Services Custom",
                "code": "# Créer service systemd\n\n# Fichier: /etc/systemd/system/myapp.service\nsudo nano /etc/systemd/system/myapp.service\n\n[Unit]\nDescription=My Application\nAfter=network.target\nRequires=mariadb.service\n\n[Service]\nType=simple\nUser=myapp\nGroup=myapp\nWorkingDirectory=/opt/myapp\nExecStart=/usr/bin/python3 /opt/myapp/app.py\nRestart=on-failure\nRestartSec=10\n\n# Environment:\nEnvironment=\"ENV=production\"\nEnvironmentFile=/etc/myapp/env\n\n# Logs:\nStandardOutput=journal\nStandardError=journal\n\n# Security:\nPrivateTmp=true\nNoNewPrivileges=true\nProtectSystem=strict\nProtectHome=true\nReadWritePaths=/var/lib/myapp\n\n[Install]\nWantedBy=multi-user.target\n\n# Reload daemon:\nsudo systemctl daemon-reload\n\n# Activer:\nsudo systemctl enable myapp.service\n\n# Démarrer:\nsudo systemctl start myapp\n\n# Status:\nsudo systemctl status myapp\n\n# Logs:\njournalctl -u myapp -f\n\n# Restart:\nsudo systemctl restart myapp\n\n# Stop:\nsudo systemctl stop myapp\n\n# Désactiver:\nsudo systemctl disable myapp\n\n# Types service:\n# simple: Processus principal\n# forking: Daemon (fork)\n# oneshot: Tâche unique\n# notify: Notify systemd quand ready\n# dbus: D-Bus service"
            },
            {
                "title": "Automatisation - Ansible Basics",
                "code": "# Ansible = Automation multi-serveurs\n\n# Installer (contrôle machine):\nsudo apt install ansible -y\n\n# Inventory (liste serveurs):\nsudo nano /etc/ansible/hosts\n\n[webservers]\nweb1 ansible_host=192.168.1.10\nweb2 ansible_host=192.168.1.11\n\n[dbservers]\ndb1 ansible_host=192.168.1.20\n\n[all:vars]\nansible_user=admin\nansible_ssh_private_key_file=~/.ssh/id_ed25519\n\n# Test connexion:\nansible all -m ping\n\n# Commande ad-hoc:\nansible webservers -m shell -a \"uptime\"\nansible all -m apt -a \"name=htop state=present\" --become\n\n# Playbook (tasks.yml):\n---\n- name: Configure Web Servers\n  hosts: webservers\n  become: yes\n  tasks:\n    - name: Update apt cache\n      apt:\n        update_cache: yes\n    \n    - name: Install Nginx\n      apt:\n        name: nginx\n        state: present\n    \n    - name: Start Nginx\n      systemd:\n        name: nginx\n        state: started\n        enabled: yes\n    \n    - name: Copy config\n      copy:\n        src: nginx.conf\n        dest: /etc/nginx/nginx.conf\n      notify: Reload Nginx\n  \n  handlers:\n    - name: Reload Nginx\n      systemd:\n        name: nginx\n        state: reloaded\n\n# Exécuter playbook:\nansible-playbook tasks.yml\n\n# Dry-run:\nansible-playbook tasks.yml --check\n\n# Limiter hosts:\nansible-playbook tasks.yml --limit web1\n\n# Variables:\nansible-playbook tasks.yml -e \"version=1.2.3\""
            },
            {
                "info": "💡 Serveur = sécurité critique! SSH keys only, firewall, fail2ban, backups testés. Monitoring 24/7. Documentation à jour."
            },
            {
                "warning": "⚠️ JAMAIS PasswordAuthentication yes sur serveur public! Brute-force garanti. Clés SSH + fail2ban minimum. Port SSH non-standard aide."
            },
            {
                "warning": "⚠️ Backups database RÉGULIERS! mysqldump quotidien + off-site. Tester restauration 1× par mois. Backup non testé = pas de backup."
            }
        ]
    },

    "linux_desktop": {
        "title": "🖥️ Environnements de Bureau Linux",
        "sections": [
            {
                "title": "Environnements de Bureau - Vue d'Ensemble",
                "bullets": [
                    "Desktop Environment (DE): Interface graphique complète",
                    "• Gestionnaire fenêtres + panneau + apps intégrées",
                    "• GNOME, KDE Plasma, XFCE, Cinnamon, MATE, etc.",
                    "",
                    "Window Manager (WM): Gestion fenêtres seulement",
                    "• Plus léger, configurable, clavier-centric",
                    "• i3, Sway, Openbox, bspwm, awesome, etc.",
                    "",
                    "Display Server:",
                    "• X11 (Xorg): Standard historique, mature",
                    "• Wayland: Moderne, sécurisé, smooth (animations)"
                ]
            },
            {
                "title": "GNOME - Installation & Personnalisation",
                "code": "# Installer GNOME (Ubuntu/Debian):\nsudo apt install gnome-shell gnome-session gdm3 -y\n\n# Installer GNOME (Fedora):\nsudo dnf install @gnome-desktop\n\n# Extensions GNOME (indispensable!):\nsudo apt install gnome-shell-extensions chrome-gnome-shell -y\n# Puis: https://extensions.gnome.org/\n\n# Tweaks GNOME:\nsudo apt install gnome-tweaks -y\ngnome-tweaks\n\n# Extensions populaires:\n# • Dash to Dock: Dock macOS-like\n# • User Themes: Thèmes custom\n# • AppIndicator: Tray icons\n# • Clipboard Indicator: Historique presse-papier\n# • Vitals: Monitoring système dans barre"
            },
            {
                "title": "KDE Plasma - Installation & Config",
                "code": "# Installer KDE Plasma (Ubuntu/Kubuntu):\nsudo apt install kde-plasma-desktop plasma-nm plasma-pa -y\n\n# Installer KDE Plasma (Fedora):\nsudo dnf install @kde-desktop\n\n# SDDM (login manager KDE):\nsudo apt install sddm -y\nsudo systemctl enable sddm\n\n# Personnalisation KDE:\n# System Settings → Apparence → Thèmes globaux\n# Télécharger: store.kde.org\n\n# KDE Connect (sync Android/Linux):\nsudo apt install kdeconnect -y\n# Partage fichiers, notifs, clipboard, commande à distance"
            },
            {
                "title": "XFCE - Léger & Performant",
                "code": "# Installer XFCE (Ubuntu/Xubuntu):\nsudo apt install xfce4 xfce4-goodies -y\n\n# LightDM (login manager léger):\nsudo apt install lightdm lightdm-gtk-greeter -y\n\n# Personnalisation XFCE:\n# Apparence → Style & Icônes\n# Gestionnaire fenêtres → Thème\n\n# Whisker Menu (menu app amélioré):\nsudo apt install xfce4-whiskermenu-plugin -y\n# Panel → Ajouter élément → Whisker Menu\n\n# Plugins utiles:\nsudo apt install xfce4-pulseaudio-plugin xfce4-clipman-plugin -y"
            },
            {
                "title": "i3 Window Manager - Tiling Keyboard-Centric",
                "code": "# Installer i3 (Ubuntu/Debian):\nsudo apt install i3 i3status i3blocks dmenu rofi -y\n\n# Config i3: ~/.config/i3/config\nmkdir -p ~/.config/i3\ncp /etc/i3/config ~/.config/i3/config\n\n# Raccourcis essentiels (Mod = Win/Super):\n# Mod+Enter: Terminal\n# Mod+d: dmenu (lancer app)\n# Mod+Shift+q: Fermer fenêtre\n# Mod+1,2,3...: Changer workspace\n# Mod+Shift+1,2,3...: Déplacer vers workspace\n# Mod+f: Fullscreen\n# Mod+v/h: Split vertical/horizontal\n\n# Bar i3:\n# i3status: Léger, basique\n# i3blocks: Scriptable, modules custom\n# polybar: Ultra configurable (install séparé)\n\n# Installer polybar:\nsudo apt install polybar -y\nmkdir -p ~/.config/polybar\ncp /usr/share/doc/polybar/examples/config.ini ~/.config/polybar/config.ini"
            },
            {
                "title": "Changer Desktop Environment",
                "code": "# Lister DEs installés:\nls /usr/share/xsessions/\n\n# Changer DE au login:\n# Écran login → Icône engrenage/settings → Sélectionner DE\n\n# Définir DE par défaut (update-alternatives):\nsudo update-alternatives --config x-session-manager\n\n# Désinstaller DE (ex: GNOME):\nsudo apt remove gnome-shell gdm3 --autoremove -y\n\n# Supprimer configs utilisateur:\nrm -rf ~/.config/gnome-*\nrm -rf ~/.local/share/gnome-*"
            },
            {
                "title": "Wayland vs X11",
                "bullets": [
                    "Wayland (moderne):",
                    "• Meilleur sécurité (isolation apps)",
                    "• Animations smooth, fractional scaling",
                    "• Incompatibilités: apps X11 only, certains jeux, screen share",
                    "",
                    "X11 (legacy mais stable):",
                    "• Compatibilité maximale",
                    "• Screen share/recording fiable",
                    "• NVIDIA historiquement mieux supporté",
                    "",
                    "Basculer Wayland ↔ X11:",
                    "• GNOME: Écran login → Engrenage → 'GNOME' (Wayland) ou 'GNOME on Xorg'",
                    "• KDE: SDDM login → Session 'Plasma' (Wayland) ou 'Plasma (X11)'"
                ]
            },
            {
                "info": "💡 Débutants: GNOME (Ubuntu), KDE (Fedora), XFCE (PC anciens). Avancés: i3/Sway (productivité clavier max)."
            },
            {
                "warning": "⚠️ Plusieurs DEs installés = conflits possibles (settings, keybindings). Garder 1-2 DEs max. Backup configs avant changement DE majeur."
            }
        ]
    },

    "linux_virtualization": {
        "title": "💻 Virtualisation Linux - KVM & QEMU",
        "sections": [
            {
                "title": "Virtualisation - Technologies",
                "bullets": [
                    "Type 1 (Bare Metal): Hyperviseur direct sur hardware",
                    "• KVM (Kernel-based VM): Intégré kernel Linux",
                    "• Performances natives (CPU passthrough)",
                    "• Production servers",
                    "",
                    "Type 2 (Hosted): Hyperviseur sur OS hôte",
                    "• VirtualBox: Facile, GUI, cross-platform",
                    "• VMware Workstation: Pro, snapshots avancés",
                    "• QEMU: Émulation pure (plus lent), cross-architecture",
                    "",
                    "Conteneurs (alternative légère):",
                    "• Docker, LXC/LXD: Partage kernel, démarrage instant"
                ]
            },
            {
                "title": "KVM/QEMU - Installation",
                "code": "# Vérifier support virtualisation CPU:\ngrep -E 'vmx|svm' /proc/cpuinfo\n# vmx = Intel VT-x, svm = AMD-V\n# Si vide: Activer VT-x/AMD-V dans BIOS!\n\n# Ubuntu/Debian:\nsudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager -y\n\n# Fedora:\nsudo dnf install @virtualization\n\n# Arch:\nsudo pacman -S qemu libvirt virt-manager\n\n# Ajouter user au groupe libvirt:\nsudo usermod -aG libvirt $(whoami)\nsudo usermod -aG kvm $(whoami)\n# Déconnexion/reconnexion nécessaire!\n\n# Démarrer service libvirt:\nsudo systemctl enable --now libvirtd\n\n# Vérifier install:\nvirsh list --all\nsudo virt-host-validate"
            },
            {
                "title": "Virt-Manager - Créer VM (GUI)",
                "code": "# Lancer virt-manager:\nvirt-manager\n\n# Créer VM:\n# 1. Fichier → Nouvelle machine virtuelle\n# 2. ISO installation (ex: ubuntu-24.04.iso)\n# 3. RAM: 4096 MB (4GB min pour desktop)\n# 4. CPU: 2 cœurs (recommandé)\n# 5. Disque: 20-50 GB (qcow2 format)\n# 6. Réseau: NAT (par défaut) ou Bridge\n\n# Optimisations VM:\n# • CPU: Mode 'host-passthrough' (perf max)\n# • Disk: Bus VirtIO (I/O rapide)\n# • Network: VirtIO (vs e1000)\n# • Video: QXL ou VirtIO-GPU\n# • Installer qemu-guest-agent dans VM\n\n# Snapshots:\n# VM → Gérer snapshots\n# Utile avant updates/tests dangereux"
            },
            {
                "title": "virsh - CLI Management",
                "code": "# Lister VMs:\nvirsh list --all\n\n# Démarrer/Arrêter VM:\nvirsh start nom_vm\nvirsh shutdown nom_vm     # Propre (ACPI)\nvirsh destroy nom_vm      # Forcer arrêt\n\n# Auto-démarrage au boot:\nvirsh autostart nom_vm\nvirsh autostart --disable nom_vm\n\n# Infos VM:\nvirsh dominfo nom_vm\nvirsh vcpuinfo nom_vm     # CPU allocation\nvirsh domblklist nom_vm   # Disques\n\n# Cloner VM:\nvirt-clone --original vm1 --name vm2 --auto-clone\n\n# Supprimer VM:\nvirsh destroy nom_vm\nvirsh undefine nom_vm --remove-all-storage\n\n# Snapshot CLI:\nvirsh snapshot-create-as nom_vm snapshot1 \"Description\"\nvirsh snapshot-list nom_vm\nvirsh snapshot-revert nom_vm snapshot1\nvirsh snapshot-delete nom_vm snapshot1"
            },
            {
                "title": "Networking VMs",
                "bullets": [
                    "NAT (default):",
                    "• VM accède internet via hôte (SNAT)",
                    "• Isolée du LAN physique",
                    "• Port forwarding pour accès externe",
                    "",
                    "Bridge (bridged):",
                    "• VM = machine physique sur LAN",
                    "• IP propre (DHCP/static)",
                    "• Accessible par autres machines réseau",
                    "",
                    "Host-only:",
                    "• VM ↔ Hôte uniquement",
                    "• Pas internet",
                    "• Tests isolés"
                ]
            },
            {
                "title": "VirtualBox - Alternative",
                "code": "# Installer VirtualBox:\nsudo apt install virtualbox virtualbox-ext-pack -y\n\n# Ou télécharger .deb: https://www.virtualbox.org/\n\n# Créer VM (CLI):\nVBoxManage createvm --name \"MaVM\" --ostype Ubuntu_64 --register\nVBoxManage modifyvm \"MaVM\" --memory 4096 --cpus 2\nVBoxManage createhd --filename ~/VMs/MaVM.vdi --size 20480\nVBoxManage storagectl \"MaVM\" --name \"SATA\" --add sata\nVBoxManage storageattach \"MaVM\" --storagectl \"SATA\" --port 0 --type hdd --medium ~/VMs/MaVM.vdi\n\n# Lancer GUI:\nvirtualbox\n\n# Guest Additions (clipboard, shared folders):\n# Dans VM: Périphériques → Insérer image CD Guest Additions\n# Puis dans VM:\nsudo apt install build-essential dkms linux-headers-$(uname -r) -y\nsudo sh /media/cdrom/VBoxLinuxAdditions.run"
            },
            {
                "title": "GPU Passthrough (Gaming VM)",
                "code": "# Passthrough GPU physique à VM (performances natives!)\n# Prérequis:\n# • 2 GPUs (ou iGPU + dGPU)\n# • CPU/Mobo support IOMMU (Intel VT-d / AMD-Vi)\n# • BIOS: Activer VT-d/AMD-Vi\n\n# Activer IOMMU (GRUB):\nsudo nano /etc/default/grub\n# Intel:\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet intel_iommu=on iommu=pt\"\n# AMD:\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet amd_iommu=on iommu=pt\"\nsudo update-grub\nsudo reboot\n\n# Vérifier IOMMU:\nsudo dmesg | grep -i iommu\n\n# Isoler GPU (vfio-pci):\n# Identifier GPU PCI ID:\nlspci -nn | grep -i nvidia\n# Ex: 01:00.0 VGA ... [10de:1b81]\n\n# /etc/modprobe.d/vfio.conf:\noptions vfio-pci ids=10de:1b81,10de:10f0\n# Mettre tous IDs (GPU + Audio GPU)\n\nsudo update-initramfs -u\nsudo reboot\n\n# Guide complet: https://wiki.archlinux.org/title/PCI_passthrough"
            },
            {
                "info": "💡 KVM performances ≈ natives (98-99%). Gaming VM avec GPU passthrough = Windows gaming sur Linux host sans dual-boot!"
            },
            {
                "warning": "⚠️ GPU Passthrough = complexe! Backup système avant. Tester VMs basiques d'abord. Certains GPU/mobos incompatibles (reset bug)."
            }
        ]
    },

    "linux_development": {
        "title": "⚙️ Outils de Développement Linux",
        "sections": [
            {
                "title": "Git - Contrôle de Version",
                "code": "# Installer Git:\nsudo apt install git -y\n\n# Config initiale:\ngit config --global user.name \"Votre Nom\"\ngit config --global user.email \"email@example.com\"\n\n# Créer repo:\nmkdir mon_projet && cd mon_projet\ngit init\n\n# Workflow basique:\ngit add fichier.py               # Stager fichier\ngit add .                        # Stager tout\ngit commit -m \"Message commit\"   # Commit\ngit status                       # État repo\ngit log --oneline --graph        # Historique\n\n# Branches:\ngit branch feature1              # Créer branche\ngit checkout feature1            # Basculer\ngit checkout -b feature2         # Créer + basculer\ngit merge feature1               # Merger dans branche actuelle\ngit branch -d feature1           # Supprimer branche\n\n# Remote (GitHub, GitLab):\ngit remote add origin https://github.com/user/repo.git\ngit push -u origin main          # Push initial\ngit push                         # Push suivants\ngit pull                         # Récupérer changements\ngit clone https://github.com/user/repo.git  # Cloner repo"
            },
            {
                "title": "Compilateurs & Build Tools",
                "code": "# GCC (C/C++):\nsudo apt install build-essential -y\n# Inclut: gcc, g++, make\n\ngcc programme.c -o programme      # Compiler C\ng++ programme.cpp -o programme    # Compiler C++\n\n# Options utiles:\ngcc -Wall -Wextra -O2 -o prog prog.c\n# -Wall -Wextra: Warnings\n# -O2: Optimisation niveau 2\n# -g: Symbols debug (pour gdb)\n\n# CMake (build system moderne):\nsudo apt install cmake -y\n\nmkdir build && cd build\ncmake ..                          # Générer Makefile\nmake                              # Compiler\nsudo make install                 # Installer\n\n# Rust:\ncurl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh\nsource \"$HOME/.cargo/env\"\n\ncargo new mon_projet              # Nouveau projet\ncargo build                       # Compiler\ncargo run                         # Compiler + exécuter\ncargo build --release             # Build optimisé\n\n# Go:\nsudo apt install golang-go -y\ngo mod init mon_projet\ngo build                          # Compiler\ngo run main.go                    # Exécuter direct"
            },
            {
                "title": "Python - Environnements Virtuels",
                "code": "# Installer Python 3.12:\nsudo apt install python3.12 python3.12-venv python3-pip -y\n\n# Créer venv (recommandé!):\npython3 -m venv venv\nsource venv/bin/activate          # Activer\n# Prompt change: (venv) $\n\npip install requests flask numpy  # Installer packages\npip freeze > requirements.txt     # Sauvegarder dépendances\npip install -r requirements.txt   # Installer depuis fichier\n\ndeactivate                        # Désactiver venv\n\n# Poetry (gestionnaire moderne):\ncurl -sSL https://install.python-poetry.org | python3 -\n\npoetry new mon_projet\ncd mon_projet\npoetry add requests               # Ajouter dépendance\npoetry install                    # Installer deps\npoetry run python main.py         # Exécuter dans venv\n\n# pyenv (multiples versions Python):\ncurl https://pyenv.run | bash\npyenv install 3.12.0\npyenv global 3.12.0"
            },
            {
                "title": "IDEs & Éditeurs",
                "code": "# VS Code:\nsudo snap install code --classic\n# Extensions: Python, C/C++, GitLens, Docker\n\n# JetBrains IDEs (PyCharm, IntelliJ, WebStorm):\nsudo snap install pycharm-community --classic\nsudo snap install intellij-idea-community --classic\n\n# Neovim (terminal, ultra configurable):\nsudo apt install neovim -y\n# Config: ~/.config/nvim/init.vim\n# Plugins: vim-plug, packer.nvim\n\n# Emacs:\nsudo apt install emacs -y\n\n# Vim basique:\nsudo apt install vim -y\n\n# Geany (léger, GUI):\nsudo apt install geany -y"
            },
            {
                "title": "Debugging & Profiling",
                "code": "# GDB (C/C++ debugger):\nsudo apt install gdb -y\n\n# Compiler avec symbols debug:\ngcc -g programme.c -o programme\n\n# Lancer gdb:\ngdb ./programme\n# Commandes:\n# break main          # Breakpoint\n# run                 # Exécuter\n# next                # Ligne suivante\n# step                # Entrer fonction\n# print variable      # Afficher var\n# backtrace           # Stack trace\n# quit                # Quitter\n\n# Valgrind (memory leaks):\nsudo apt install valgrind -y\nvalgrind --leak-check=full ./programme\n\n# strace (system calls):\nstrace ./programme\nstrace -p 1234        # Attacher à PID\n\n# ltrace (library calls):\nsudo apt install ltrace -y\nltrace ./programme\n\n# perf (profiling CPU):\nsudo apt install linux-tools-generic -y\nsudo perf record ./programme\nsudo perf report\n\n# Python debugger (pdb):\npython3 -m pdb script.py\n# Ou dans code:\nimport pdb; pdb.set_trace()  # Breakpoint"
            },
            {
                "title": "Containers & CI/CD",
                "code": "# Docker (déjà couvert dans guide Docker)\n\n# Docker Compose (multi-containers):\nsudo apt install docker-compose -y\n\n# docker-compose.yml:\nversion: '3.8'\nservices:\n  web:\n    image: nginx\n    ports:\n      - \"80:80\"\n  db:\n    image: postgres\n    environment:\n      POSTGRES_PASSWORD: secret\n\ndocker-compose up -d              # Démarrer\ndocker-compose down               # Arrêter\ndocker-compose logs -f            # Logs\n\n# GitHub Actions (CI/CD):\n# .github/workflows/ci.yml:\nname: CI\non: [push, pull_request]\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - name: Run tests\n        run: |\n          python -m pytest\n\n# GitLab CI:\n# .gitlab-ci.yml:\ntest:\n  script:\n    - pytest tests/"
            },
            {
                "title": "Outils Système Développeur",
                "code": "# htop (monitoring avancé):\nsudo apt install htop -y\nhtop\n\n# tmux (terminal multiplexer):\nsudo apt install tmux -y\ntmux                              # Lancer\n# Ctrl+b puis c: Nouvelle fenêtre\n# Ctrl+b puis n/p: Fenêtre next/prev\n# Ctrl+b puis %: Split vertical\n# Ctrl+b puis \": Split horizontal\n# Ctrl+b puis d: Détacher session\ntmux attach                       # Réattacher\n\n# ripgrep (grep ultra-rapide):\nsudo apt install ripgrep -y\nrg \"pattern\" /chemin              # Recherche récursive\n\n# fzf (fuzzy finder):\nsudo apt install fzf -y\nhistory | fzf                     # Recherche historique\nfind . | fzf                      # Recherche fichiers\n\n# jq (parser JSON):\nsudo apt install jq -y\ncurl https://api.github.com/users/octocat | jq '.name'\n\n# httpie (curl user-friendly):\nsudo apt install httpie -y\nhttp GET https://httpbin.org/get\nhttp POST https://httpbin.org/post name=Alice age:=25"
            },
            {
                "info": "💡 Débutants: VS Code + Git + venv Python. Avancés: Neovim + tmux + Docker. Toujours utiliser Git, même projets persos!"
            },
            {
                "warning": "⚠️ JAMAIS commit secrets (API keys, passwords) dans Git! Utiliser .gitignore + .env files. Secrets leakés = permanents dans historique Git."
            }
        ]
    },

    "win11_install": {
        "title": "💿 Installation & Mise à Jour Windows 11",
        "sections": [
            {
                "title": "Installation Windows 11 - Prérequis",
                "bullets": [
                    "Configuration minimale:",
                    "• Processeur: 1 GHz, 2+ cœurs, 64-bit compatible",
                    "• RAM: 4 GB minimum (8 GB recommandé)",
                    "• Stockage: 64 GB minimum",
                    "• TPM: Version 2.0 (Trusted Platform Module)",
                    "• UEFI: Secure Boot capable",
                    "• Carte graphique: Compatible DirectX 12",
                    "",
                    "Vérifier compatibilité:",
                    "• Télécharger 'PC Health Check' depuis Microsoft",
                    "• Vérifier TPM: Win+R → tpm.msc",
                    "• Vérifier Secure Boot: msinfo32 → Mode BIOS"
                ]
            },
            {
                "title": "Créer Clé USB Bootable",
                "code": "# Méthode 1: Media Creation Tool (officiel)\n1. Télécharger depuis: https://www.microsoft.com/software-download/windows11\n2. Lancer MediaCreationToolW11.exe\n3. Accepter licence\n4. Choisir 'Créer un support d'installation'\n5. Langue: Français, Édition: Windows 11, Architecture: 64-bit\n6. Support: Disque mémoire flash USB (8 GB min)\n7. Sélectionner clé USB → Suivant\n\n# Méthode 2: Rufus (plus rapide, options avancées)\n1. Télécharger Rufus: https://rufus.ie/\n2. Télécharger ISO Windows 11\n3. Lancer Rufus:\n   - Périphérique: Votre clé USB\n   - Méthode démarrage: Disque ou ISO\n   - Sélectionner ISO Windows 11\n   - Schéma partition: GPT\n   - Système cible: UEFI\n4. Options Rufus pour contourner TPM/Secure Boot (si besoin):\n   ☑ Remove requirement for 4GB+ RAM\n   ☑ Remove requirement for Secure Boot\n   ☑ Remove requirement for TPM 2.0\n5. Démarrer\n\n# Installation:\n1. Insérer clé USB\n2. Redémarrer PC\n3. Appuyer F12/F2/DEL (selon PC) pour Boot Menu\n4. Sélectionner clé USB\n5. Suivre assistant installation"
            },
            {
                "title": "Windows Update - Gestion",
                "code": "# Vérifier mises à jour:\n- Paramètres → Windows Update → Rechercher mises à jour\n- Ou: Win+I → Windows Update\n\n# Forcer mise à jour immédiate:\nPowerShell (Admin):\nInstall-WindowsUpdate -AcceptAll -AutoReboot\n\n# Voir historique mises à jour:\nParamètres → Windows Update → Historique des mises à jour\n\n# Désinstaller mise à jour problématique:\nParamètres → Windows Update → Historique → Désinstaller\n\n# Pause updates (max 5 semaines):\nParamètres → Windows Update → Suspendre → Choisir durée\n\n# Options avancées:\nWindows Update → Options avancées\n☑ Recevoir mises à jour produits Microsoft\n☑ Me prévenir quand redémarrage nécessaire\n☐ Télécharger updates sur connexions limitées"
            },
            {
                "title": "Mise à Niveau 10 → 11",
                "bullets": [
                    "Via Windows Update (recommandé):",
                    "• Paramètres → Windows Update",
                    "• 'Mise à niveau vers Windows 11 disponible' apparaîtra si éligible",
                    "• Cliquer 'Télécharger et installer'",
                    "",
                    "Via Assistant Installation (si pas proposé):",
                    "• https://www.microsoft.com/software-download/windows11",
                    "• Télécharger 'Assistant Installation Windows 11'",
                    "• Lancer → Vérification compatibilité automatique",
                    "• Accepter → Installation démarre",
                    "",
                    "Données préservées:",
                    "• Fichiers personnels conservés",
                    "• Applications installées préservées",
                    "• Paramètres conservés",
                    "• MAIS: Sauvegarde recommandée avant upgrade!"
                ]
            },
            {
                "warning": "⚠️ TPM 2.0 requis! Si PC non compatible, considérer: 1) Rester Windows 10 (support jusqu'à 2025), 2) Contourner via Rufus (non recommandé - pas de updates sécurité futures), 3) Upgrade matériel."
            },
            {
                "info": "💡 Windows 11 Pro vs Home: Pro ajoute BitLocker (chiffrement), Remote Desktop, Hyper-V, gestion domaine entreprise. Pour particuliers, Home suffit."
            }
        ]
    },

    "win11_taskmanager": {
        "title": "⚙️ Gestionnaire de Tâches Avancé",
        "sections": [
            {
                "title": "Ouvrir Gestionnaire de Tâches",
                "code": "# Méthodes rapides:\nCtrl + Shift + Esc          # Direct (plus rapide)\nCtrl + Alt + Suppr → Gestionnaire de tâches\nClic droit Barre des tâches → Gestionnaire de tâches\nWin + X → Gestionnaire de tâches\n\n# Via Exécuter:\nWin + R → taskmgr → Entrée"
            },
            {
                "title": "Onglet Processus - Vue d'Ensemble",
                "bullets": [
                    "Colonnes importantes:",
                    "• Nom: Application ou processus",
                    "• CPU: Utilisation processeur (% cumulé tous cœurs)",
                    "• Mémoire: RAM utilisée (Mo/Go)",
                    "• Disque: Activité lecture/écriture",
                    "• Réseau: Bande passante utilisée",
                    "",
                    "Trier par colonne:",
                    "• Cliquer en-tête colonne pour trier",
                    "• Identifier rapidement processus problématiques",
                    "",
                    "Types de processus:",
                    "• Applications: Programmes ouverts",
                    "• Processus en arrière-plan: Services Windows",
                    "• Processus Windows: Système (explorer.exe, etc.)"
                ]
            },
            {
                "title": "Arrêter Processus Bloqué",
                "code": "# Gestionnaire de tâches:\n1. Onglet Processus\n2. Clic droit sur processus → Fin de tâche\n3. Si ne répond pas: Sélectionner → Fin de tâche (en bas)\n\n# PowerShell (si GUI bloquée):\nGet-Process | Where-Object {$_.ProcessName -like '*chrome*'} | Stop-Process -Force\n\n# Ou par PID:\nStop-Process -Id 1234 -Force\n\n# CMD (taskkill):\ntaskkill /IM chrome.exe /F\ntaskkill /PID 1234 /F\n\n# Tuer TOUS processus d'un programme:\ntaskkill /IM notepad.exe /F /T\n# /T = tue aussi processus enfants"
            },
            {
                "title": "Onglet Performances - Monitoring",
                "bullets": [
                    "CPU:",
                    "• Utilisation: % global et par cœur (clic droit → Graphique → Processeurs logiques)",
                    "• Vitesse: Fréquence actuelle vs Base",
                    "• Processus: Nombre total actifs",
                    "• Threads: Nombre total threads",
                    "",
                    "Mémoire (RAM):",
                    "• En cours d'utilisation: RAM occupée",
                    "• Disponible: RAM libre",
                    "• Validée: Mémoire virtuelle (RAM + Fichier d'échange)",
                    "• Mise en cache: Données préchargées",
                    "",
                    "Disque:",
                    "• Temps actif: % temps disque occupé (100% = saturé)",
                    "• Vitesse lecture/écriture: Mo/s",
                    "",
                    "Réseau:",
                    "• Débit envoi/réception: Mbps",
                    "• Adaptateurs: Ethernet, Wi-Fi, VPN"
                ]
            },
            {
                "title": "Onglet Démarrage - Optimiser Boot",
                "code": "# Gestionnaire de tâches → Onglet Démarrage\n\n# Désactiver programmes au démarrage:\n1. Clic droit programme → Désactiver\n2. Impact: Élevé/Moyen/Faible (désactiver 'Élevé' d'abord)\n\n# Programmes à généralement désactiver:\n- Adobe Creative Cloud\n- Spotify\n- Discord\n- Microsoft Teams\n- Skype\n- Applications gamers (Steam, Epic, etc.) si pas gaming régulier\n\n# Programmes à GARDER:\n- Antivirus\n- Drivers graphiques (NVIDIA, AMD)\n- Gestionnaire souris/clavier gaming\n- Logiciels cloud critiques (OneDrive si utilisé)\n\n# Via PowerShell (liste auto-démarrage):\nGet-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location, User\n\n# Désactiver via Registry (avancé):\nWin + R → regedit\nHKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\nSupprimer entrée non désirée"
            },
            {
                "title": "Onglet Détails - Informations Avancées",
                "bullets": [
                    "Colonnes utiles (clic droit en-tête → Sélectionner colonnes):",
                    "• PID: Process ID unique",
                    "• Nom d'utilisateur: Compte exécutant processus",
                    "• CPU: Utilisation processeur",
                    "• Mémoire: RAM utilisée",
                    "• Description: Nom complet application",
                    "",
                    "Définir priorité processus:",
                    "• Clic droit processus → Définir la priorité",
                    "• Temps réel (max) / Élevée / Supérieure à la normale / Normale / Inférieure",
                    "• ⚠️ Temps réel peut bloquer système!",
                    "",
                    "Affinité processeur:",
                    "• Clic droit → Définir l'affinité",
                    "• Choisir cœurs CPU dédiés au processus",
                    "• Utile pour: Vieux jeux, tests performances"
                ]
            },
            {
                "info": "💡 PC lent au démarrage? Onglet Démarrage → Désactiver programmes 'Impact élevé'. Peut réduire temps boot de 30-60 secondes!"
            },
            {
                "warning": "⚠️ NE PAS arrêter 'Processus Windows' (explorer.exe, dwm.exe, etc.) sauf dépannage! Peut rendre Windows instable. Si explorer.exe planté: Fichier → Exécuter → explorer.exe"
            }
        ]
    },

    "win11_personalization": {
        "title": "🎨 Personnalisation Windows 11",
        "sections": [
            {
                "title": "Thèmes et Couleurs",
                "code": "# Accès rapide:\nParamètres → Personnalisation\nOu: Clic droit Bureau → Personnaliser\n\n# Mode sombre/clair:\nPersonnalisation → Couleurs → Mode\n- Clair\n- Sombre (recommandé la nuit, réduit fatigue yeux)\n- Personnalisé (Apps sombre, Windows clair)\n\n# Couleur d'accentuation:\nPersonnalisation → Couleurs → Couleur d'accentuation\n☑ Afficher couleur accent sur surfaces suivantes:\n  ☑ Menu Démarrer, barre des tâches, centre notifications\n  ☑ Barres de titre et bordures fenêtres\n\n# Transparence:\nPersonnalisation → Couleurs\n☑ Effets de transparence (Aero Glass)\n\n# Télécharger thèmes:\nPersonnalisation → Thèmes → Parcourir thèmes\nMicrosoft Store → Thèmes gratuits/payants"
            },
            {
                "title": "Fond d'Écran et Écran de Verrouillage",
                "bullets": [
                    "Fond d'écran:",
                    "• Personnalisation → Arrière-plan",
                    "• Types: Image, Couleur unie, Diaporama",
                    "• Ajustement: Remplir, Ajuster, Étirer, Mosaïque, Centrer",
                    "• Clic droit image → Définir comme arrière-plan (rapide)",
                    "",
                    "Diaporama automatique:",
                    "• Arrière-plan → Diaporama",
                    "• Sélectionner dossier d'images",
                    "• Changer image: 1min / 10min / 30min / 1h / 1 jour",
                    "• Ordre aléatoire: Oui/Non",
                    "",
                    "Écran de verrouillage:",
                    "• Personnalisation → Écran de verrouillage",
                    "• Windows à la une: Photos Bing quotidiennes",
                    "• Image: Photo personnalisée",
                    "• Diaporama: Rotation images"
                ]
            },
            {
                "title": "Barre des Tâches - Configuration",
                "code": "# Paramètres barre des tâches:\nParamètres → Personnalisation → Barre des tâches\n\n# Position (Windows 11 22H2+):\nAlignment: Centré (défaut) ou Gauche (style Windows 10)\n\n# Icônes système:\nBarre des tâches → Icônes d'angle de barre des tâches\n☑ Wi-Fi\n☑ Volume\n☑ Batterie (ordinateurs portables)\n☑ Explorateur de fichiers\n☐ Widgets (désactiver si non utilisé)\n\n# Applications épinglées:\nClic droit app ouverte → Épingler à la barre des tâches\nDétacher: Clic droit → Détacher\n\n# Masquer automatiquement:\nBarre des tâches → Comportements\n☑ Masquer automatiquement la barre des tâches\n\n# Badges notifications:\nBarre des tâches → Comportements\n☑ Afficher badges sur apps barre des tâches"
            },
            {
                "title": "Menu Démarrer - Personnalisation",
                "bullets": [
                    "Épingler applications favorites:",
                    "• Rechercher app → Clic droit → Épingler au menu Démarrer",
                    "• Réorganiser: Glisser-déposer icônes",
                    "",
                    "Dossiers dans menu Démarrer:",
                    "• Paramètres → Personnalisation → Démarrer",
                    "• Dossiers: Documents, Téléchargements, Paramètres, etc.",
                    "• Activer ceux utilisés fréquemment",
                    "",
                    "Applications récentes:",
                    "• Démarrer → Paramètres",
                    "• Afficher applications récemment ajoutées: Oui/Non",
                    "• Afficher apps les + utilisées: Oui/Non",
                    "",
                    "Recommandations (publicités):",
                    "• Démarrer → Paramètres",
                    "• Afficher recommandations: Désactiver (retire publicités Microsoft)"
                ]
            },
            {
                "title": "Polices et Accessibilité",
                "code": "# Taille texte système:\nParamètres → Accessibilité → Taille du texte\nCurseur: 100% (défaut) à 225% (grandes polices)\n\n# Mise à l'échelle affichage:\nParamètres → Système → Affichage → Échelle\n100% (natif) / 125% / 150% / 175% / 200%\nRecommandé: Laisser automatique (Windows détecte)\n\n# Installer nouvelles polices:\n1. Télécharger fichier .ttf ou .otf\n2. Clic droit → Installer\n3. Ou: Copier dans C:\\Windows\\Fonts\n\n# Changer police système (avancé - Registry):\n⚠️ Sauvegarde recommandée!\nWin + R → regedit\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts\nModifier 'Segoe UI' → Autre police\n\n# ClearType (lissage polices):\nWin + R → cttune\nSuivre assistant optimisation"
            },
            {
                "info": "💡 Mode sombre + Réduction lumière bleue (Éclairage nocturne) = Meilleur sommeil! Paramètres → Système → Affichage → Éclairage nocturne."
            },
            {
                "warning": "⚠️ Scaling >150% peut rendre certaines vieilles apps floues. Si problème: Clic droit .exe → Propriétés → Compatibilité → Remplacer comportement mise à l'échelle."
            }
        ]
    },

    "win11_optimization": {
        "title": "⚡ Optimisation Performances Windows 11",
        "sections": [
            {
                "title": "Optimisations Visuelles - Boost Performances",
                "code": "# Ajuster effets visuels (gain 5-15% perfs):\nWin + R → sysdm.cpl\nOnglet 'Paramètres système avancés' → Performances → Paramètres\n\nOptions:\n○ Ajuster afin d'obtenir les meilleures performances (désactive tout)\n○ Personnalisé (recommandé):\n  ☐ Animer fenêtres lors réduction/agrandissement\n  ☐ Animations dans barre des tâches\n  ☐ Estomper/glisser menus\n  ☑ Lisser bords polices écran (garder!)\n  ☑ Afficher miniatures (garder!)\n  ☐ Transparence barre des tâches\n\n# Désactiver transparence (séparément):\nParamètres → Personnalisation → Couleurs\n☐ Effets de transparence"
            },
            {
                "title": "Mode Performances - Plans d'Alimentation",
                "code": "# Accès rapide:\nPanneau de configuration → Options d'alimentation\nOu: Win + X → Options d'alimentation\n\n# Modes disponibles:\n- Équilibré (recommandé): Balance perfs/économie\n- Économie d'énergie: Max batterie (laptops)\n- Hautes performances: Max CPU (PCs fixes)\n\n# Activer 'Performances maximales' (caché):\nPowerShell (Admin):\npowercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61\n\nPuis:\nPanneau de configuration → Options alimentation\nSélectionner 'Performances maximales'\n\n# Paramètres avancés alimentation:\nOptions alimentation → Modifier paramètres mode\n→ Modifier paramètres avancés\n\nOptimisations PC fixe:\n- Disque dur → Éteindre après: Jamais\n- État minimum processeur: 100%\n- État maximum processeur: 100%\n- Stratégie refroidissement: Active (ventilateurs à fond)\n\nOptimisations laptop (économie):\n- Luminosité écran: 50%\n- Suspension: Après 10-15 min inactivité\n- État processeur: 5% min, 80% max"
            },
            {
                "title": "Nettoyer Disque - Libérer Espace",
                "code": "# Nettoyage disque Windows:\nWin + R → cleanmgr\nSélectionner lecteur C: → OK\n\nCocher:\n☑ Fichiers Internet temporaires\n☑ Fichiers journaux mise à niveau Windows\n☑ Miniatures\n☑ Fichiers temporaires\n☑ Corbeille\n☑ Fichiers programmes téléchargés\n\n# Nettoyage avancé (fichiers système):\nNettoyer fichiers système (bouton)\n☑ Installations Windows précédentes (10-20 GB!)\n☑ Fichiers de mise à niveau Windows abandonnés\n\n# Storage Sense (automatique):\nParamètres → Système → Stockage\n☑ Storage Sense activé\nConfigurer:\n- Exécuter: Tous les mois / Chaque semaine / Quand espace faible\n- Supprimer fichiers temp: Après 1 jour\n- Vider corbeille: Après 30 jours\n\n# Analyser espace disque (WinDirStat):\nTélécharger: https://windirstat.net/\nAnalyse visuelle consommation espace"
            },
            {
                "title": "Désactiver Services Inutiles",
                "code": "# Gestionnaire services:\nWin + R → services.msc\n\nServices à désactiver (PC gaming/perfs):\n\n1. Windows Search (si pas utilisé)\n   Clic droit → Propriétés → Type démarrage: Désactivé\n   ⚠️ Désactive recherche fichiers rapide!\n\n2. Superfetch/SysMain (SSD seulement)\n   Inutile sur SSD, ralentit\n\n3. Windows Update (temporairement)\n   ⚠️ Réactiver régulièrement pour sécurité!\n\n4. Print Spooler (si pas imprimante)\n\n5. Fax (personne utilise!)\n\n6. Expérience utilisateur connecté et télémétrie\n   Données envoyées à Microsoft\n\n# Via PowerShell (ex: Désactiver Superfetch):\nStop-Service \"SysMain\" -Force\nSet-Service \"SysMain\" -StartupType Disabled\n\n# Réactiver:\nSet-Service \"SysMain\" -StartupType Automatic\nStart-Service \"SysMain\""
            },
            {
                "title": "Optimiser SSD - TRIM et Défragmentation",
                "code": "# Vérifier TRIM activé (SSD):\nPowerShell (Admin):\nfsutil behavior query DisableDeleteNotify\n\nRésultat attendu:\nNTFS DisableDeleteNotify = 0 (TRIM activé ✓)\n\nSi = 1 (désactivé), activer:\nfsutil behavior set DisableDeleteNotify 0\n\n# Planification optimisation (auto):\nWin + R → dfrgui\nSélectionner lecteur C: → Optimiser\n\n☑ Optimisation planifiée: Activée\nFréquence: Hebdomadaire (par défaut)\n\n⚠️ Windows gère automatiquement:\n- SSD: TRIM (pas défragmentation!)\n- HDD: Défragmentation classique\n\n# Défragmenter HDD manuellement:\ndfrgui → Sélectionner lecteur → Optimiser\nDurée: 30min - 2h selon taille/fragmentation\n\n# Via CMD (HDD seulement):\ndefrag C: /U /V\n# /U = Verbose, /V = Afficher progression"
            },
            {
                "title": "RAM - Vider Cache et Optimiser",
                "code": "# Vider mémoire cache (RAM):\nPowerShell (Admin):\n$ClearMemory = @\"\nusing System;\nusing System.Runtime.InteropServices;\npublic class MemoryManagement {\n    [DllImport(\"kernel32.dll\")]\n    public static extern bool SetProcessWorkingSetSize(IntPtr proc, int min, int max);\n    public static void FlushMemory() {\n        GC.Collect();\n        GC.WaitForPendingFinalizers();\n        SetProcessWorkingSetSize(System.Diagnostics.Process.GetCurrentProcess().Handle, -1, -1);\n    }\n}\n\"@\nAdd-Type $ClearMemory\n[MemoryManagement]::FlushMemory()\n\n# Désactiver fichier d'échange (si 16GB+ RAM):\nWin + R → sysdm.cpl\nAvancé → Performances → Paramètres → Avancé → Mémoire virtuelle\n○ Aucun fichier d'échange\n⚠️ Peut crasher apps gourmandes!\n\n# Fichier d'échange custom (recommandé):\n☑ Taille personnalisée\nTaille initiale: 1.5× RAM (ex: 24 GB si 16 GB RAM)\nTaille maximale: 2× RAM (ex: 32 GB si 16 GB RAM)"
            },
            {
                "info": "💡 PC portable? Désactiver 'Démarrage rapide' si bugs au boot: Panneau de config → Options alimentation → Choisir comportement boutons → Modifier paramètres indisponibles → Décocher 'Démarrage rapide'."
            },
            {
                "warning": "⚠️ NE PAS désactiver Windows Defender (sauf antivirus tiers installé). Pas de 'RAM cleaner' tiers - souvent malwares! Windows gère RAM automatiquement."
            }
        ]
    },

    "win11_disk_management": {
        "title": "💾 Gestion des Disques Windows",
        "sections": [
            {
                "title": "Gestionnaire de Disques - Interface",
                "code": "# Ouvrir gestionnaire disques:\nWin + X → Gestion des disques\nOu: Win + R → diskmgmt.msc\n\n# Interface:\n- Vue supérieure: Liste volumes (lettres lecteurs)\n- Vue inférieure: Représentation graphique partitions\n\n# Informations affichées:\n- Lettre lecteur: C:, D:, E:, etc.\n- Système fichiers: NTFS, FAT32, exFAT, ReFS\n- État: Sain, RAW (non formaté), Récupération\n- Capacité: Taille totale\n- Espace libre: Disponible\n- Type: Partition principale, Étendue, Logique"
            },
            {
                "title": "Créer Nouvelle Partition",
                "code": "# Étapes création partition:\n1. Clic droit espace non alloué → Nouveau volume simple\n2. Assistant:\n   - Taille: Spécifier en Mo (ex: 50000 Mo = 50 GB)\n   - Lettre lecteur: Choisir (D:, E:, etc.)\n   - Système fichiers:\n     * NTFS (recommandé Windows, >4GB fichiers)\n     * FAT32 (compatibilité max, fichiers <4GB)\n     * exFAT (clés USB modernes, >4GB fichiers)\n   - Nom volume: Label descriptif\n   - Formatage rapide: Cocher (plus rapide)\n3. Terminer\n\n# Si pas d'espace non alloué, réduire partition existante:\nClic droit partition (ex: C:) → Réduire le volume\nQuantité: Espace à libérer en Mo\n⚠️ Windows ne peut réduire que jusqu'aux fichiers immobiles!"
            },
            {
                "title": "Formater / Reformater Partition",
                "code": "# Formater partition:\nClic droit partition → Formater\n\nOptions:\n- Nom volume: Étiquette (ex: 'Données', 'Backup')\n- Système fichiers:\n  * NTFS: Windows, fichiers >4GB, permissions, chiffrement\n  * FAT32: Compatibilité universelle, fichiers <4GB\n  * exFAT: Clés USB/externes, fichiers >4GB, pas permissions\n- Taille unité allocation: Défaut (recommandé)\n- Formatage rapide: ☑ Cocher (efface table, pas données)\n                    ☐ Décocher (réécriture complète, lent, sécurisé)\n\n⚠️ FORMATAGE EFFACE TOUTES DONNÉES!\n\n# Formater via CMD (avancé):\nformat D: /FS:NTFS /Q /V:MonDisque\n# /FS: Système fichiers\n# /Q: Rapide\n# /V: Label volume"
            },
            {
                "title": "Changer Lettre de Lecteur",
                "code": "# Modifier lettre lecteur:\n1. Gestionnaire disques\n2. Clic droit partition → Modifier lettre/chemin d'accès\n3. Modifier → Sélectionner nouvelle lettre\n4. OK\n\n⚠️ Applications installées sur lecteur peuvent casser!\n⚠️ Ne PAS changer lettre C: (Windows)\n\n# Via DiskPart (CMD Admin):\ndiskpart\nlist volume\nselect volume 2     # Numéro volume à changer\nassign letter=E     # Nouvelle lettre\nexit\n\n# Supprimer lettre lecteur (monter dans dossier):\nModifier → Supprimer\nAjouter → Monter dans dossier NTFS vide\nExemple: C:\\Montages\\Disque2\\"
            },
            {
                "title": "Vérifier Santé Disque - CHKDSK",
                "code": "# Vérifier erreurs disque:\nClic droit lecteur (Explorateur) → Propriétés\nOutils → Vérification erreurs → Analyser\n\n# CHKDSK via CMD (Admin):\nchkdsk C: /F /R\n# /F: Corrige erreurs système fichiers\n# /R: Localise secteurs défectueux, récupère données\n# Redémarrage requis si C: en cours utilisation\n\n# CHKDSK scan complet (très long!):\nchkdsk C: /F /R /X\n# /X: Démonte volume d'abord\n\n# Voir résultat CHKDSK précédent:\nObservateur événements → Journaux Windows → Application\nFiltrer: Source = Chkdsk, ID événement = 26226\n\n# SMART status disque (PowerShell Admin):\nGet-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceID, Wear, Temperature\n\n# CrystalDiskInfo (GUI, recommandé):\nTélécharger: https://crystalmark.info/\nAffiche: Santé, température, heures utilisation, secteurs réalloués"
            },
            {
                "title": "Convertir MBR ↔ GPT",
                "code": "# MBR vs GPT:\nMBR (Master Boot Record):\n- Maximum 4 partitions primaires\n- Disques <2 TB\n- BIOS Legacy\n\nGPT (GUID Partition Table):\n- 128+ partitions\n- Disques >2 TB\n- UEFI (Windows 11 requis)\n- Plus fiable (backup table partitions)\n\n# Vérifier type partition:\nDiskPart:\nlist disk\n# Colonne 'Gpt': * = GPT, vide = MBR\n\n# Convertir MBR → GPT (sans perte données, Windows 10+):\nPowerShell (Admin):\nmbr2gpt /convert /disk:0 /allowFullOS\n# /disk:0 = Premier disque (vérifier numéro!)\n# ⚠️ Changer BIOS Legacy → UEFI après!\n\n# Convertir via DiskPart (EFFACE DONNÉES!):\ndiskpart\nlist disk\nselect disk 1       # Disk à convertir\nclean               # ⚠️ EFFACE TOUT!\nconvert gpt         # Ou: convert mbr\nexit"
            },
            {
                "info": "💡 SSD neuf non visible? Normal - doit être initialisé! Gestionnaire disques → Clic droit 'Disque inconnu' → Initialiser → GPT."
            },
            {
                "warning": "⚠️ NE JAMAIS formater partition 'Récupération' (300-500 MB) ou 'EFI' (100 MB)! Empêche boot Windows. Si supprimé par erreur, réinstallation Windows requise."
            }
        ]
    },

    "win11_backup": {
        "title": "💾 Sauvegardes Windows 11",
        "sections": [
            {
                "title": "Historique des Fichiers - Sauvegarde Continue",
                "code": "# Activer Historique fichiers:\nParamètres → Système → Stockage → Options avancées → Sauvegarde\nOu: Panneau config → Historique fichiers\n\n# Configuration:\n1. Connecter disque externe (USB, NAS)\n2. Sélectionner lecteur\n3. Activer\n\n# Dossiers sauvegardés automatiquement:\n- Bureau\n- Documents\n- Téléchargements\n- Images\n- Musique\n- Vidéos\n- OneDrive (si activé)\n\n# Fréquence sauvegarde:\nOptions avancées → Enregistrer copies fichiers\n- Toutes les 10 minutes (défaut, intensif)\n- Toutes les heures (recommandé)\n- Quotidiennement\n\n# Conserver versions:\n- Jusqu'à espace nécessaire (défaut)\n- 1 mois / 3 mois / 6 mois / 1 an / 2 ans / Toujours\n\n# Restaurer fichiers:\nHistorique fichiers → Restaurer fichiers personnels\nParcourir versions → Sélectionner → Restaurer"
            },
            {
                "title": "Sauvegarde Image Système Complète",
                "code": "# Créer image système (clone complet disque C:):\nPanneau config → Sauvegarde et restauration (Windows 7)\nCréer image système\n\n# Assistant:\n1. Destination:\n   - Disque dur externe (recommandé)\n   - DVD (multiples disques requis, obsolète)\n   - Emplacement réseau (NAS)\n\n2. Lecteurs à inclure:\n   ☑ C: (Windows) - obligatoire\n   ☑ Partitions système (EFI, Récupération) - automatique\n   ☐ D:, E: (données) - optionnel\n\n3. Démarrer sauvegarde\n   Durée: 30min - 2h (selon taille)\n\n4. Créer disque réparation système? → Oui (USB bootable)\n\n# Restaurer image système:\n1. Paramètres → Système → Récupération → Redémarrage avancé\n2. Dépannage → Options avancées → Récupération image système\n3. Sélectionner image → Suivant → Restaurer\n⚠️ EFFACE Windows actuel!\n\n# Via CMD (création image):\nwbadmin start backup -backupTarget:E: -include:C: -allCritical -quiet"
            },
            {
                "title": "OneDrive - Sauvegarde Cloud",
                "bullets": [
                    "Configuration OneDrive:",
                    "• Gratuit: 5 GB",
                    "• Microsoft 365: 1 TB",
                    "",
                    "Activer sauvegarde dossiers:",
                    "• Clic icône OneDrive (barre tâches) → Paramètres",
                    "• Sauvegarde → Gérer sauvegarde",
                    "• Sélectionner: Bureau, Documents, Images",
                    "• Démarrer sauvegarde",
                    "",
                    "Avantages:",
                    "• Accès fichiers depuis n'importe quel appareil",
                    "• Versions antérieures (30 jours)",
                    "• Protection ransomware (détection + restauration)",
                    "",
                    "Fichiers à la demande:",
                    "• Économise espace disque",
                    "• Fichiers cloud téléchargés seulement si ouverts",
                    "• Clic droit fichier → Libérer de l'espace"
                ]
            },
            {
                "title": "Point de Restauration - Sauvegarde Système",
                "code": "# Créer point restauration manuellement:\nWin + R → sysdm.cpl\nProtection système → Créer\nDescription: \"Avant mise à jour\" / \"Installation propre\"\n\n# Activer protection système (si désactivée):\nProtection système → Sélectionner C: → Configurer\n☑ Activer protection système\nUtilisation disque: 5-10% (5-10 GB typique)\n\n# Points restauration automatiques:\nCréés automatiquement avant:\n- Installations Windows Update\n- Installations drivers\n- Installations logiciels majeurs\n\n# Restaurer point restauration:\nParamètres → Système → Récupération → Récupération avancée\nOu: sysdm.cpl → Protection système → Restauration système\nChoisir point → Suivant → Terminer\n⚠️ Désinstalle apps/drivers installés après point!\n\n# Supprimer anciens points (libérer espace):\nWin + R → cleanmgr\nNettoyer fichiers système → Onglet 'Autres options'\nPoints restauration → Nettoyer (garde dernier point)"
            },
            {
                "title": "Outils Sauvegarde Tiers",
                "bullets": [
                    "Macrium Reflect (gratuit):",
                    "• Clonage disque complet",
                    "• Sauvegardes incrémentielles/différentielles",
                    "• Média récupération bootable",
                    "• https://www.macrium.com/reflectfree",
                    "",
                    "EaseUS Todo Backup (freemium):",
                    "• Interface simple",
                    "• Sauvegarde cloud (payant)",
                    "• https://www.easeus.com/backup-software/",
                    "",
                    "Veeam Agent (gratuit):",
                    "• Pro-grade gratuit",
                    "• Restauration fichier par fichier",
                    "• https://www.veeam.com/windows-endpoint-server-backup-free.html",
                    "",
                    "Stratégie 3-2-1:",
                    "• 3 copies données",
                    "• 2 supports différents (disque + cloud)",
                    "• 1 copie hors site (cloud, disque distant)"
                ]
            },
            {
                "info": "💡 Sauvegarde AVANT installations majeures (Windows updates, nouveaux drivers). Point restauration = 5 min, peut sauver des heures de réinstallation!"
            },
            {
                "warning": "⚠️ Historique fichiers ≠ Image système! Historique = fichiers perso. Image = Windows complet. Les DEUX recommandés pour protection totale."
            }
        ]
    },

    "win11_defender": {
        "title": "🛡️ Windows Defender & Sécurité",
        "sections": [
            {
                "title": "Windows Defender - Configuration",
                "code": "# Ouvrir Sécurité Windows:\nParamètres → Confidentialité et sécurité → Sécurité Windows\nOu: Win + I → Sécurité Windows\nOu: Rechercher 'Sécurité Windows'\n\n# Protection en temps réel:\nProtection antivirus → Gérer paramètres\n☑ Protection en temps réel (toujours activée!)\n☑ Protection cloud (détection menaces récentes)\n☑ Envoi échantillons automatique\n☑ Protection contre falsification (empêche malwares désactiver Defender)\n\n# Analyse rapide:\nProtection antivirus → Analyse rapide\nDurée: 5-15 min\nAnalyse: Fichiers système, mémoire, démarrage\n\n# Analyse complète:\nOptions analyse → Analyse complète\nDurée: 1-3h\nAnalyse: TOUS fichiers disque\n\n# Analyse personnalisée:\nOptions analyse → Personnalisée\nSélectionner dossiers spécifiques"
            },
            {
                "title": "Analyses Planifiées & Automatiques",
                "code": "# Planifier analyse (Planificateur tâches):\nWin + R → taskschd.msc\nBibliothèque Planificateur → Microsoft → Windows → Windows Defender\n\nTâches Defender:\n- Windows Defender Scheduled Scan (analyse hebdo)\n- Windows Defender Cache Maintenance\n- Windows Defender Cleanup\n- Windows Defender Verification\n\n# Modifier fréquence analyse:\nClic droit 'Scheduled Scan' → Propriétés\nDéclencheurs → Modifier\nFréquence: Quotidien / Hebdomadaire / Mensuel\nHeure: Choisir moment PC allumé (ex: 2h du matin)\n\n# Via PowerShell (analyse manuelle):\nStart-MpScan -ScanType QuickScan\nStart-MpScan -ScanType FullScan\n\n# Mettre à jour définitions virus:\nUpdate-MpSignature\n\n# Voir dernière analyse:\nGet-MpComputerStatus"
            },
            {
                "title": "Exclusions Defender (Faux Positifs)",
                "code": "# Ajouter exclusion fichier/dossier:\nSécurité Windows → Protection antivirus\nGérer paramètres → Exclusions → Ajouter exclusion\n\nTypes exclusions:\n- Fichier (ex: C:\\Games\\game.exe)\n- Dossier (ex: C:\\Dev\\MyProject)\n- Type fichier (ex: .bat, .ps1)\n- Processus (ex: python.exe)\n\n# Quand ajouter exclusions:\n- Outils développement (Visual Studio, Git)\n- Logiciels activation (cracks - ⚠️ risque!)\n- Jeux avec anti-cheat (Steam, Epic)\n- Machines virtuelles\n- Dossiers compilation (build/)\n\n# Via PowerShell (Admin):\n# Exclure dossier:\nAdd-MpPreference -ExclusionPath \"C:\\Dev\"\n\n# Exclure extension:\nAdd-MpPreference -ExclusionExtension \".py\"\n\n# Exclure processus:\nAdd-MpPreference -ExclusionProcess \"python.exe\"\n\n# Lister exclusions:\nGet-MpPreference | Select-Object -ExpandProperty ExclusionPath"
            },
            {
                "title": "Protection Ransomware - Accès Contrôlé",
                "code": "# Activer Accès contrôlé dossiers:\nSécurité Windows → Protection antivirus\nProtection contre ransomware → Gérer protection\n☑ Accès contrôlé aux dossiers: Activé\n\n# Dossiers protégés (par défaut):\n- Bureau\n- Documents\n- Images\n- Vidéos\n- Musique\n\n# Ajouter dossier protégé:\nDossiers protégés → Ajouter dossier protégé\nEx: C:\\Projets\\Important\n\n# Autoriser app à modifier dossiers protégés:\nAutoriser app via accès contrôlé dossiers\nAjouter app autorisée\nEx: C:\\Program Files\\Backup\\backup.exe\n\n⚠️ Seulement apps de confiance!\n\n# Fonctionnement:\n- Bloque apps non autorisées modifier dossiers protégés\n- Protège contre chiffrement ransomware\n- Notification si tentative bloquée"
            },
            {
                "title": "SmartScreen & Protection Web",
                "bullets": [
                    "SmartScreen Windows:",
                    "• Bloque apps non reconnues",
                    "• Vérification réputation fichiers téléchargés",
                    "• Protection phishing sites web",
                    "",
                    "Configuration:",
                    "• Sécurité Windows → Contrôle apps/navigateur",
                    "• Vérifier apps/fichiers: Activé (recommandé)",
                    "• SmartScreen Microsoft Edge: Activé",
                    "• Protection anti-hameçonnage: Activé",
                    "",
                    "Contourner SmartScreen (si fichier sûr):",
                    "• Téléchargement bloqué: Infos complémentaires → Exécuter",
                    "• ⚠️ Seulement si fichier de source fiable!",
                    "",
                    "Protection exploits:",
                    "• Contrôle apps → Paramètres protection exploits",
                    "• Atténuation exploits système activée",
                    "• Protège contre attaques mémoire (buffer overflow, etc.)"
                ]
            },
            {
                "title": "Quarantaine & Historique Menaces",
                "code": "# Voir menaces détectées:\nSécurité Windows → Protection antivirus\nMenaces actuelles\n\n# Quarantaine:\nHistorique protection → Voir historique complet\nMenaces en quarantaine\n\n# Restaurer fichier quarantaine (faux positif):\nSélectionner menace → Restaurer\n⚠️ Seulement si CERTAIN que faux positif!\n\n# Supprimer définitivement:\nSélectionner → Supprimer\n\n# Via PowerShell:\n# Lister menaces quarantaine:\nGet-MpThreat\n\n# Supprimer toutes menaces quarantaine:\nRemove-MpThreat\n\n# Voir dernières détections:\nGet-MpThreatDetection"
            },
            {
                "info": "💡 Defender = suffisant pour 95% utilisateurs! Gratuit, intégré, pas ralentissements. Antivirus tiers utile seulement si besoins spécifiques (entreprise, serveurs)."
            },
            {
                "warning": "⚠️ NE JAMAIS désactiver Protection falsification! Malwares ciblent cette option. Si vraiment besoin désactiver Defender (tests), réactiver immédiatement après."
            }
        ]
    },

    "win11_firewall": {
        "title": "🔥 Pare-feu Windows",
        "sections": [
            {
                "title": "Pare-feu Windows - Statut",
                "code": "# Ouvrir Pare-feu:\nParamètres → Confidentialité et sécurité → Sécurité Windows → Pare-feu\nOu: Panneau config → Système et sécurité → Pare-feu Windows Defender\nOu: Win + R → firewall.cpl\n\n# Vérifier statut:\nParamètres → Réseau et Internet → Paramètres réseau avancés\nPare-feu Windows Defender\n\n# 3 profils réseau:\n1. Réseau de domaine (entreprise - Active Directory)\n   ☑ Activé (géré admin)\n\n2. Réseau privé (maison, confiance)\n   ☑ Activé (recommandé)\n   Détection réseau: Activée\n   Partage fichiers: Autorisé\n\n3. Réseau public (Wi-Fi café, hôtel)\n   ☑ Activé (strict!)\n   Détection réseau: Désactivée\n   Partage fichiers: Bloqué\n   Connexions entrantes: Bloquées par défaut"
            },
            {
                "title": "Autoriser Application via Pare-feu",
                "code": "# Méthode GUI (simple):\n1. Pare-feu Windows → Autoriser app via pare-feu\n2. Modifier paramètres\n3. Chercher app dans liste\n   Si absente: Autoriser autre app → Parcourir\n4. Cocher:\n   ☑ Privé (réseau maison)\n   ☐ Public (généralement décocher)\n5. OK\n\n# Applications courantes à autoriser:\n- Navigateurs (Chrome, Firefox) - déjà autorisés\n- Clients torrent (qBittorrent, Transmission)\n- Serveurs locaux (XAMPP, Node.js)\n- Jeux multijoueur\n- Apps partage fichiers (Syncthing)\n- Bureau à distance (RDP, TeamViewer)\n\n# Via PowerShell (Admin):\n# Autoriser programme:\nNew-NetFirewallRule -DisplayName \"MonApp\" -Direction Inbound -Program \"C:\\Apps\\app.exe\" -Action Allow\n\n# Autoriser port:\nNew-NetFirewallRule -DisplayName \"Port 8080\" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow"
            },
            {
                "title": "Règles Pare-feu Avancées",
                "code": "# Pare-feu avancé:\nWin + R → wf.msc\n\n# Interface:\n- Règles entrantes (Inbound): Connexions vers PC\n- Règles sortantes (Outbound): Connexions depuis PC\n- Règles sécurité connexion: IPsec, VPN\n\n# Créer règle personnalisée:\nRègles entrantes → Nouvelle règle\n\n1. Type:\n   ○ Programme (recommandé)\n   ○ Port\n   ○ Prédéfinie (services Windows)\n   ○ Personnalisée (avancé)\n\n2. Programme:\n   ○ Tous programmes\n   ○ Chemin programme: C:\\Apps\\server.exe\n\n3. Action:\n   ○ Autoriser connexion\n   ○ Autoriser connexion si sécurisée (IPsec)\n   ○ Bloquer connexion\n\n4. Profil:\n   ☑ Domaine\n   ☑ Privé\n   ☐ Public (généralement décocher)\n\n5. Nom: \"Mon Serveur Web\"\n\n# Désactiver règle:\nClic droit règle → Désactiver\n(Plutôt que supprimer)"
            },
            {
                "title": "Bloquer Application / Port",
                "code": "# Bloquer application (empêcher accès Internet):\nwf.msc → Règles sortantes → Nouvelle règle\nType: Programme\nChemin: C:\\Program Files\\App\\app.exe\nAction: Bloquer connexion\nProfil: Tous\nNom: \"Bloquer App Internet\"\n\n# Bloquer port entrant (ex: Telnet 23):\nRègles entrantes → Nouvelle règle\nType: Port\nProtocole: TCP\nPort: 23\nAction: Bloquer\n\n# Bloquer plage ports:\nPorts: 4000-5000\n\n# Via PowerShell:\n# Bloquer app sortant:\nNew-NetFirewallRule -DisplayName \"Bloquer App\" -Direction Outbound -Program \"C:\\App.exe\" -Action Block\n\n# Bloquer port entrant:\nNew-NetFirewallRule -DisplayName \"Bloquer Port 23\" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block"
            },
            {
                "title": "Notifications Pare-feu",
                "bullets": [
                    "Popup 'Windows Defender a bloqué...':",
                    "• Apparaît quand app tente connexion bloquée",
                    "• Options: Autoriser / Annuler",
                    "",
                    "Désactiver notifications:",
                    "• Pare-feu → Activer/désactiver pare-feu",
                    "• Décocher: 'M'avertir quand pare-feu bloque app'",
                    "• ⚠️ Non recommandé - perd visibilité!",
                    "",
                    "Journal pare-feu (avancé):",
                    "• wf.msc → Pare-feu Windows → Propriétés",
                    "• Profil actif → Personnaliser journal",
                    "• Nom: %systemroot%\\system32\\LogFiles\\Firewall\\pfirewall.log",
                    "• Taille max: 4096 KB (4 MB)",
                    "• Enregistrer: Connexions supprimées / réussies",
                    "",
                    "Analyser journal:",
                    "• notepad C:\\Windows\\System32\\LogFiles\\Firewall\\pfirewall.log",
                    "• Colonnes: Date, Heure, Action (DROP/ALLOW), Protocole, Src-IP, Dst-IP, Port"
                ]
            },
            {
                "title": "Réinitialiser Pare-feu",
                "code": "# Restaurer paramètres par défaut:\nPare-feu Windows → Restaurer valeurs par défaut\n⚠️ Supprime TOUTES règles personnalisées!\n\n# Via PowerShell (Admin):\n(New-Object -ComObject HNetCfg.FwPolicy2).RestoreLocalFirewallDefaults()\n\n# Ou via netsh:\nnetsh advfirewall reset\n\n# Vérifier règles actives:\nGet-NetFirewallRule | Where-Object {$_.Enabled -eq 'True'} | Select-Object DisplayName, Direction, Action"
            },
            {
                "info": "💡 Serveur web/jeu local pas accessible? Vérifier pare-feu! Port 80 (HTTP), 443 (HTTPS), 3389 (RDP) souvent bloqués par défaut."
            },
            {
                "warning": "⚠️ NE JAMAIS désactiver pare-feu complètement! Si app bloquée, créer règle spécifique. Désactiver pare-feu = porte ouverte hackers."
            }
        ]
    },

    "win11_network": {
        "title": "🌐 Réseau et Partage Windows",
        "sections": [
            {
                "title": "Configuration Réseau - Profils",
                "code": "# Changer profil réseau (Public ↔ Privé):\nParamètres → Réseau et Internet\nSélectionner connexion active (Wi-Fi / Ethernet)\nProfil réseau:\n○ Public (recommandé Wi-Fi publics)\n  - Détection réseau désactivée\n  - Partage fichiers bloqué\n  - Pare-feu strict\n○ Privé (réseau maison)\n  - Détection réseau activée\n  - Partage fichiers autorisé\n  - Autres PCs visibles\n\n# Via PowerShell (Admin):\n# Lister réseaux:\nGet-NetConnectionProfile\n\n# Changer en Privé:\nSet-NetConnectionProfile -InterfaceAlias \"Wi-Fi\" -NetworkCategory Private\n\n# Changer en Public:\nSet-NetConnectionProfile -InterfaceAlias \"Ethernet\" -NetworkCategory Public"
            },
            {
                "title": "Partage de Fichiers - Configuration",
                "code": "# Activer partage fichiers:\nParamètres → Réseau et Internet → Paramètres réseau avancés\nParamètres de partage avancés\n\nProfil Privé:\n☑ Activer la détection de réseau\n☑ Activer découverte automatique\n☑ Activer partage fichiers et imprimantes\n☑ Autoriser Windows gérer connexions groupe résidentiel (obsolète Win11)\n\nToutes réseaux:\n☑ Activer partage pour permettre accès réseau\n☐ Désactiver partage protégé par mot passe (réseau confiance)\n☑ Activer partage protégé (réseau public)\n\n# Partager dossier:\n1. Clic droit dossier → Propriétés → Partage\n2. Partage avancé → ☑ Partager ce dossier\n3. Nom partage: (ex: \"Documents\")\n4. Autorisations:\n   - Contrôle total (lecture + écriture + suppression)\n   - Modifier (lecture + écriture)\n   - Lecture seule\n5. Appliquer → OK\n\n# Accéder partage depuis autre PC:\n\\\\NOM-PC\\NomPartage\nOu: \\\\192.168.1.10\\Documents"
            },
            {
                "title": "Réseau Local - Diagnostic",
                "code": "# Voir configuration IP:\nipconfig /all\n\nInfos importantes:\n- Adresse IPv4: 192.168.1.x (IP locale)\n- Masque sous-réseau: 255.255.255.0\n- Passerelle: 192.168.1.1 (routeur)\n- DNS: 8.8.8.8 (Google) ou DNS FAI\n\n# Renouveler IP (DHCP):\nipconfig /release\nipconfig /renew\n\n# Vider cache DNS:\nipconfig /flushdns\n\n# Tester connectivité:\nping 8.8.8.8           # Internet Google\nping 192.168.1.1       # Routeur\nping google.com        # DNS + Internet\n\n# Traceroute (chemin paquets):\ntracert google.com\n\n# Voir connexions actives:\nnetstat -ano\n# -a: Toutes connexions\n# -n: Adresses numériques\n# -o: PID processus\n\n# Connexions établies seulement:\nnetstat -ano | findstr ESTABLISHED"
            },
            {
                "title": "Wi-Fi - Gestion et Dépannage",
                "code": "# Oublier réseau Wi-Fi:\nParamètres → Réseau et Internet → Wi-Fi\nGérer réseaux connus → Sélectionner → Oublier\n\n# Se connecter réseau caché:\nWi-Fi → Afficher réseaux disponibles\nRéseau masqué → Se connecter manuellement\nSaisir SSID, Type sécurité, Mot passe\n\n# Priorité réseaux Wi-Fi:\nPowerShell (Admin):\nnetsh wlan show profiles\nnetsh wlan set profileorder name=\"MonWiFi\" interface=\"Wi-Fi\" priority=1\n# Priority: 1=premier, 2=deuxième, etc.\n\n# Désactiver Wi-Fi auto (économie batterie):\nParamètres → Réseau et Internet → Wi-Fi\n☐ Activer Wi-Fi\n\n# Voir mot de passe Wi-Fi enregistré:\nnetsh wlan show profile name=\"NomRéseau\" key=clear\n# Chercher ligne 'Contenu clé'\n\n# Dépannage Wi-Fi:\n1. Redémarrer adaptateur:\n   Paramètres → Réseau → Wi-Fi → Désactiver → Attendre 10s → Activer\n\n2. Réinitialiser réseau:\n   Paramètres → Réseau → Paramètres réseau avancés\n   Réinitialisation réseau\n   ⚠️ Oublie tous Wi-Fi!\n\n3. Mettre à jour driver:\n   Gestionnaire périph → Cartes réseau → Clic droit → MàJ driver"
            },
            {
                "title": "Ethernet - Configuration",
                "bullets": [
                    "Avantages Ethernet vs Wi-Fi:",
                    "• Latence: 1-5ms (vs 20-50ms Wi-Fi)",
                    "• Stabilité: Pas interférences",
                    "• Vitesse: 1 Gbps typique (vs 100-600 Mbps Wi-Fi)",
                    "• Sécurité: Pas interception sans accès physique",
                    "",
                    "Configuration IP statique (serveurs, imprimantes):",
                    "• Paramètres → Réseau → Ethernet → Propriétés",
                    "• Attribution IP: Manuel",
                    "• IPv4: Activé",
                    "• IP: 192.168.1.100 (choix libre 2-254)",
                    "• Masque: 255.255.255.0",
                    "• Passerelle: 192.168.1.1 (IP routeur)",
                    "• DNS primaire: 8.8.8.8 (Google)",
                    "• DNS secondaire: 1.1.1.1 (Cloudflare)",
                    "",
                    "Tester câble Ethernet:",
                    "• Gestionnaire tâches → Performances → Ethernet",
                    "• Vitesse liaison: 1 Gbps (bon), 100 Mbps (câble Cat5 vieux)",
                    "• Si 10 Mbps: Câble défectueux"
                ]
            },
            {
                "info": "💡 Partage fichiers lent (1-5 MB/s)? Vérifier: 1) Câble Ethernet Cat6+ (pas Cat5), 2) Switch/routeur Gigabit, 3) Disque destination pas saturé."
            },
            {
                "warning": "⚠️ Partage protégé par mot passe DÉSACTIVÉ = DANGER sur réseau non fiable! N'importe qui peut accéder fichiers. Activer sur réseau maison seulement."
            }
        ]
    },

    "win11_privacy": {
        "title": "🔒 Confidentialité Windows 11",
        "sections": [
            {
                "title": "Confidentialité - Paramètres Essentiels",
                "code": "# Accès paramètres confidentialité:\nParamètres → Confidentialité et sécurité\n\n# Autorisations Windows (recommandations):\n\n1. Général:\n   ☐ ID de publicité (désactiver - tracking pubs)\n   ☐ Sites web accès liste langues (désactiver)\n   ☐ Contenu suggéré Paramètres (désactiver - pubs Microsoft)\n   ☑ Afficher apps suggérées menu Démarrer (selon préférence)\n\n2. Voix:\n   ☐ Reconnaissance vocale en ligne (désactiver si pas Cortana)\n\n3. Diagnostics:\n   ○ Données diagnostic requises (minimum)\n   ☐ Expériences personnalisées (désactiver)\n   ☐ Supprimer données diagnostic (nettoyer)\n   ☐ Feedback (désactiver)\n\n4. Historique activités:\n   ☐ Enregistrer historique (désactiver)\n   Effacer → Effacer historique complet"
            },
            {
                "title": "Autorisations Applications",
                "bullets": [
                    "Localisation:",
                    "• Désactiver si pas navigation/météo",
                    "• Autoriser seulement: Cartes, Météo",
                    "",
                    "Caméra:",
                    "• Désactiver globalement",
                    "• Autoriser: Zoom, Teams, Discord (selon usage)",
                    "• ⚠️ Vérifier apps suspectes!",
                    "",
                    "Microphone:",
                    "• Désactiver globalement",
                    "• Autoriser: Apps visio, enregistrement",
                    "",
                    "Notifications:",
                    "• Désactiver apps non critiques",
                    "• Garder: Mail, Calendrier, Sécurité Windows",
                    "",
                    "Contacts / Calendrier / Appels téléphoniques:",
                    "• Désactiver si pas sync téléphone",
                    "",
                    "Compte et informations:",
                    "• Vérifier apps ayant accès compte Microsoft",
                    "• Supprimer apps inconnues",
                    "",
                    "Fichiers:",
                    "• Autoriser seulement apps confiance (OneDrive, backup)"
                ]
            },
            {
                "title": "Télémétrie - Minimiser Données Microsoft",
                "code": "# Désactiver télémétrie (Édition Pro/Entreprise):\nGestion stratégie groupe:\ngpedit.msc\n\nConfiguration ordinateur → Modèles admin\n→ Composants Windows → Collecte données\nAutoriser télémétrie:\n○ 0 - Sécurité (Entreprise only)\n○ 1 - De base (minimum)\n\n# Services télémétrie à désactiver:\nWin + R → services.msc\n\n1. Expériences utilisateur connecté et télémétrie\n   Clic droit → Propriétés → Désactivé\n\n2. Service de rapport d'erreurs Windows\n   Désactivé (optionnel - aide Microsoft corriger bugs)\n\n# Via PowerShell (Admin):\nDisable-ScheduledTask -TaskName \"Microsoft\\Windows\\Application Experience\\*\"\nDisable-ScheduledTask -TaskName \"Microsoft\\Windows\\Customer Experience Improvement Program\\*\"\n\n# Bloquer serveurs télémétrie (fichier hosts):\nnotepad C:\\Windows\\System32\\drivers\\etc\\hosts\n\nAjouter lignes:\n0.0.0.0 vortex.data.microsoft.com\n0.0.0.0 vortex-win.data.microsoft.com\n0.0.0.0 telecommand.telemetry.microsoft.com\n0.0.0.0 oca.telemetry.microsoft.com"
            },
            {
                "title": "Cortana - Désactivation",
                "code": "# Désactiver Cortana (Windows 11):\nParamètres → Applications → Applications installées\nChercher 'Cortana' → ... → Options avancées\nDésinstaller (si option dispo)\n\n# Ou désactiver:\nDémarrer → Cortana → Paramètres\n☐ Laisser Cortana répondre 'Hey Cortana'\n☐ Autoriser Cortana écran verrouillé\n\n# Via Registry (désactiver complètement):\nWin + R → regedit\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\nCréer DWORD (32-bit):\nNom: AllowCortana\nValeur: 0\n\nRedémarrer PC"
            },
            {
                "title": "OneDrive - Contrôle Sync Cloud",
                "bullets": [
                    "Désactiver sync OneDrive:",
                    "• Clic droit icône OneDrive (barre tâches)",
                    "• Paramètres → Compte → Dissocier ce PC",
                    "• Fichiers locaux conservés",
                    "",
                    "Désinstaller OneDrive complètement:",
                    "• Win + R → appwiz.cpl",
                    "• Microsoft OneDrive → Désinstaller",
                    "",
                    "Empêcher OneDrive démarrage:",
                    "• Gestionnaire tâches → Démarrage",
                    "• Microsoft OneDrive → Désactiver",
                    "",
                    "Via PowerShell (désinstaller):",
                    "• taskkill /f /im OneDrive.exe",
                    "• %SystemRoot%\\SysWOW64\\OneDriveSetup.exe /uninstall",
                    "",
                    "Réactiver si besoin:",
                    "• C:\\Program Files\\Microsoft OneDrive\\OneDrive.exe"
                ]
            },
            {
                "title": "Widgets & Actualités - Désactiver",
                "code": "# Désactiver Widgets (barre tâches):\nClic droit barre tâches → Paramètres\n☐ Widgets\n\n# Désactiver actualités (lock screen):\nParamètres → Personnalisation → Écran verrouillage\nÉtat écran verrouillage: Image (pas 'Windows à la une')\n\n# Via Registry:\nregedit\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Dsh\nCréer DWORD:\nNom: AllowNewsAndInterests\nValeur: 0"
            },
            {
                "info": "💡 Désactiver télémétrie ≠ casser Windows. Fonctionnalités essentielles intactes. Seulement données usage anonymes + suggestions publicitaires arrêtées."
            },
            {
                "warning": "⚠️ Modifications Registry = risque si erreur! Toujours sauvegarder Registry avant (Fichier → Exporter). Si problème: Mode sans échec + restaurer backup."
            }
        ]
    },

    # ==================== BATCH 3 - GUIDES WINDOWS 11 (11-15/15) ====================

    "win11_cmd": {
        "title": "💻 Command Prompt (CMD) - Commandes Essentielles",
        "sections": [
            {
                "title": "Ouvrir CMD (Invite de Commandes)",
                "code": "# Méthodes rapides:\nWin + R → cmd → Entrée           # Standard\nWin + R → cmd + Ctrl+Shift+Entrée  # Administrateur\n\n# Via menu Démarrer:\nMenu Démarrer → Taper 'cmd' → Clic droit → Exécuter en tant qu'administrateur\n\n# Via explorateur Windows:\nExplorateur → Dossier souhaité → Barre d'adresse → Taper 'cmd' + Entrée\n(Ouvre CMD directement dans ce dossier)"
            },
            {
                "title": "Commandes de Navigation",
                "code": "# Changer de dossier:\ncd C:\\Users\\VotreNom\\Documents    # Aller vers chemin absolu\ncd Documents                       # Aller vers sous-dossier\ncd ..                             # Remonter d'un niveau\ncd \\                              # Racine du disque actuel\n\n# Changer de disque:\nD:                                # Passer au disque D:\nE:                                # Passer au disque E:\n\n# Lister fichiers/dossiers:\ndir                               # Liste simple\ndir /a                            # Afficher fichiers cachés\ndir /o:n                          # Trier par nom\ndir /o:d                          # Trier par date\ndir /s                            # Liste récursive (sous-dossiers)"
            },
            {
                "title": "Gestion Fichiers & Dossiers",
                "code": "# Créer/supprimer dossiers:\nmkdir NouveauDossier              # Créer dossier\nmd \"Dossier avec espaces\"         # Guillemets si espaces\nrmdir /s /q DossierASupprimer     # Supprimer + contenu (/s) sans confirmation (/q)\n\n# Copier/déplacer fichiers:\ncopy fichier.txt D:\\Backup\\       # Copier fichier\ncopy *.txt D:\\Backup\\             # Copier tous .txt\nxcopy /e /i /y C:\\Source D:\\Dest  # Copier dossier complet (/e=sous-dossiers, /i=créer dest, /y=écraser)\nmove fichier.txt C:\\Autre\\        # Déplacer fichier\n\n# Supprimer fichiers:\ndel fichier.txt                   # Supprimer fichier\ndel /q *.log                      # Supprimer tous .log sans confirmation\nerase /f fichier.txt              # Force suppression (/f=fichiers protégés)"
            },
            {
                "title": "Informations Système",
                "code": "# Info système complète:\nsysteminfo                        # Info détaillées (OS, RAM, CPU, réseau, etc.)\nsysteminfo | findstr /C:\"Total Physical Memory\"  # Filtre RAM totale\n\n# Processus & Performances:\ntasklist                          # Liste tous processus actifs\ntasklist | findstr chrome         # Chercher processus Chrome\ntaskkill /IM chrome.exe /F        # Tuer processus par nom (/F=forcer)\ntaskkill /PID 1234 /F             # Tuer par ID processus\n\n# Disques & Partitions:\nwmic diskdrive get size,model,status  # Info disques physiques\nvol C:                            # Info volume (nom, serial)\nchkdsk C: /f                      # Vérifier/réparer erreurs disque"
            },
            {
                "title": "Réseau - Diagnostic & Config",
                "code": "# Configuration IP:\nipconfig                          # Adresses IP actuelles\nipconfig /all                     # Config réseau complète\nipconfig /release                 # Libérer IP DHCP\nipconfig /renew                   # Renouveler IP DHCP\nipconfig /flushdns                # Vider cache DNS\n\n# Tests réseau:\nping google.com                   # Tester connectivité Internet\nping 192.168.1.1                  # Tester passerelle locale\ntracert google.com                # Tracer route vers serveur\nnslookup google.com               # Résolution DNS\nnetstat -an                       # Connexions réseau actives\nnetstat -ano | findstr :80        # Chercher processus port 80"
            },
            {
                "title": "Dépannage & Maintenance",
                "code": "# SFC (System File Checker) - Réparer fichiers système:\nsfc /scannow                      # Scanner + réparer (admin requis)\n\n# DISM - Réparer image Windows:\nDISM /Online /Cleanup-Image /CheckHealth    # Vérifier santé\nDISM /Online /Cleanup-Image /RestoreHealth  # Réparer image Windows\n\n# Redémarrage/Arrêt:\nshutdown /s /t 0                  # Arrêter immédiatement\nshutdown /r /t 0                  # Redémarrer immédiatement\nshutdown /a                       # Annuler arrêt en cours\nshutdown /r /t 3600 /c \"Maintenance dans 1h\"  # Redémarrage différé avec message"
            },
            {
                "title": "Astuces Productivité CMD",
                "bullets": [
                    "🔼 Flèches Haut/Bas : Historique des commandes précédentes",
                    "📋 Clic droit dans CMD : Coller texte du presse-papiers",
                    "🎯 Tab : Autocomplétion chemins/fichiers (appuyer plusieurs fois pour cycler)",
                    "📂 Glisser-déposer dossier dans CMD : Insère chemin absolu automatiquement",
                    "🔁 cls : Effacer écran CMD",
                    "📝 help [commande] : Aide détaillée (ex: help dir)",
                    "📄 [commande] > output.txt : Sauvegarder résultat dans fichier",
                    "🔗 && : Enchaîner commandes (ex: cd Desktop && dir)"
                ]
            },
            {
                "info": "💡 Astuce Pro: Créer script .bat pour automatiser tâches répétitives! Ex: fichier 'backup.bat' avec xcopy /e /i /y C:\\Important D:\\Backup\\. Double-clic = backup automatique!"
            },
            {
                "warning": "⚠️ Commandes destructives (del, rmdir, format) = AUCUN undo! Toujours vérifier chemin AVANT valider. Utiliser /p pour confirmation interactive."
            }
        ]
    },

    "win11_powershell": {
        "title": "⚡ PowerShell - Scripts & Automatisation",
        "sections": [
            {
                "title": "PowerShell vs CMD",
                "bullets": [
                    "💪 PowerShell = CMD 2.0 : Plus puissant, moderne, orienté objets",
                    "📦 Cmdlets : Commandes format Verbe-Nom (Get-Process, Set-ExecutionPolicy)",
                    "🔗 Pipeline objets : Passer données complexes entre commandes",
                    "🌐 .NET Framework : Accès APIs Windows complètes",
                    "📜 Scripts .ps1 : Automatisation avancée, conditions, boucles, fonctions",
                    "🎨 Couleurs & formatage : Output lisible avec tables, grilles"
                ]
            },
            {
                "title": "Ouvrir PowerShell",
                "code": "# Méthodes:\nWin + X → Windows PowerShell (Admin)  # Menu rapide Win11\nWin + R → powershell → Entrée         # Standard\nWin + R → powershell + Ctrl+Shift+Entrée  # Administrateur\n\n# Via menu Démarrer:\nMenu → Taper 'PowerShell' → Clic droit → Exécuter en admin\n\n# Via explorateur:\nExplorateur → Dossier → Maj+Clic droit espace vide → 'Ouvrir PowerShell ici'"
            },
            {
                "title": "Commandes Essentielles (Cmdlets)",
                "code": "# Gestion fichiers/dossiers:\nGet-ChildItem                     # Liste fichiers (alias: ls, dir)\nGet-ChildItem -Recurse            # Liste récursive\nGet-ChildItem *.txt               # Filtrer .txt\nNew-Item -ItemType Directory -Name \"Test\"  # Créer dossier\nCopy-Item fichier.txt D:\\Backup\\  # Copier\nMove-Item fichier.txt C:\\Autre\\   # Déplacer\nRemove-Item fichier.txt           # Supprimer\n\n# Processus:\nGet-Process                       # Liste processus\nGet-Process | Where-Object {$_.CPU -gt 100}  # Processus CPU > 100\nStop-Process -Name chrome -Force  # Tuer Chrome\nStart-Process notepad.exe         # Lancer Notepad\n\n# Services Windows:\nGet-Service                       # Liste services\nGet-Service | Where-Object {$_.Status -eq 'Running'}  # Services actifs\nStop-Service -Name 'Spooler'      # Arrêter service Imprimante\nStart-Service -Name 'Spooler'     # Démarrer service\nRestart-Service -Name 'Spooler'   # Redémarrer service"
            },
            {
                "title": "Pipeline & Filtres",
                "code": "# Pipeline (|) = passer output d'une commande à une autre:\nGet-Process | Sort-Object CPU -Descending | Select-Object -First 10\n# → Top 10 processus par CPU\n\nGet-Service | Where-Object {$_.Status -eq 'Stopped'} | Select-Object Name, DisplayName\n# → Services arrêtés\n\nGet-ChildItem -Recurse *.log | Remove-Item\n# → Supprimer tous fichiers .log récursivement\n\n# Exportation:\nGet-Process | Export-Csv C:\\Temp\\processus.csv\nGet-Service | ConvertTo-Html | Out-File C:\\Temp\\services.html\nGet-EventLog -LogName System -Newest 50 | Export-Csv C:\\Temp\\events.csv"
            },
            {
                "title": "Scripts PowerShell (.ps1)",
                "code": "# Créer script backup.ps1:\n# ------------------------------\n# Backup automatique Documents\n$source = \"C:\\Users\\$env:USERNAME\\Documents\"\n$dest = \"D:\\Backups\\$(Get-Date -Format 'yyyy-MM-dd')\"\n\nif (!(Test-Path $dest)) {\n    New-Item -ItemType Directory -Path $dest\n}\n\nCopy-Item -Path $source -Destination $dest -Recurse -Force\nWrite-Host \"✅ Backup terminé : $dest\" -ForegroundColor Green\n# ------------------------------\n\n# Exécuter script:\n.\\backup.ps1                      # Dans dossier du script\nC:\\Scripts\\backup.ps1             # Chemin absolu"
            },
            {
                "title": "Politique d'Exécution Scripts",
                "code": "# Vérifier politique actuelle:\nGet-ExecutionPolicy\n\n# Politiques possibles:\n# - Restricted : Aucun script (défaut Windows)\n# - RemoteSigned : Scripts locaux OK, scripts téléchargés doivent être signés\n# - Unrestricted : Tous scripts OK (demande confirmation si téléchargé)\n\n# Activer scripts (ADMIN requis):\nSet-ExecutionPolicy RemoteSigned -Scope CurrentUser\n# OU pour session actuelle seulement:\nSet-ExecutionPolicy Bypass -Scope Process\n\n# Contourner UNE FOIS pour 1 script:\npowershell -ExecutionPolicy Bypass -File C:\\Scripts\\backup.ps1"
            },
            {
                "title": "Exemples Scripts Utiles",
                "code": "# 1. Nettoyage fichiers temporaires:\nRemove-Item -Path $env:TEMP\\* -Recurse -Force -ErrorAction SilentlyContinue\nWrite-Host \"Temp nettoyé!\"\n\n# 2. Info système rapide:\n$os = Get-CimInstance Win32_OperatingSystem\n$cpu = Get-CimInstance Win32_Processor\n$ram = [math]::Round($os.TotalVisibleMemorySize / 1MB, 2)\n\nWrite-Host \"OS: $($os.Caption)\"\nWrite-Host \"CPU: $($cpu.Name)\"\nWrite-Host \"RAM: $ram GB\"\n\n# 3. Chercher fichiers volumineux (>1 GB):\nGet-ChildItem C:\\ -Recurse -File -ErrorAction SilentlyContinue |\n    Where-Object {$_.Length -gt 1GB} |\n    Sort-Object Length -Descending |\n    Select-Object FullName, @{Name='Size (GB)'; Expression={[math]::Round($_.Length / 1GB, 2)}}\n\n# 4. Lister programmes installés:\nGet-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* |\n    Select-Object DisplayName, DisplayVersion, Publisher, InstallDate |\n    Where-Object {$_.DisplayName} |\n    Sort-Object DisplayName"
            },
            {
                "info": "💡 PowerShell ISE (Integrated Scripting Environment) = éditeur graphique pour écrire/tester scripts. Chercher 'PowerShell ISE' dans menu Démarrer. Pratique pour débutants!"
            },
            {
                "warning": "⚠️ Scripts téléchargés sur Internet = risque malware! TOUJOURS lire contenu script AVANT exécuter. Sites fiables: Microsoft Docs, GitHub vérifiés. Si doute, demander expert."
            }
        ]
    },

    "win11_registry": {
        "title": "📝 Registry Editor (Registre Windows)",
        "sections": [
            {
                "title": "Qu'est-ce que le Registre?",
                "bullets": [
                    "🗄️ Base de données centrale Windows : Config système, utilisateurs, apps, drivers",
                    "🔑 Structure hiérarchique : Clés (dossiers) → Valeurs (paramètres)",
                    "⚙️ 5 Ruches principales (HKEY) : HKLM, HKCU, HKCR, HKU, HKCC",
                    "💾 Stockage physique : Fichiers dans C:\\Windows\\System32\\config",
                    "🚨 Modifications directes = puissant MAIS dangereux (risque instabilité/boot)",
                    "💡 Usage courant : Tweaks avancés, dépannage, désactiver fonctions cachées"
                ]
            },
            {
                "title": "Ouvrir Registry Editor",
                "code": "# Méthode standard:\nWin + R → regedit → Entrée\n\n# Via menu Démarrer:\nMenu Démarrer → Taper 'regedit' → Clic droit → Exécuter en admin (optionnel)\n\n# Via CMD/PowerShell:\nregedit\nStart-Process regedit -Verb RunAs  # PowerShell en admin"
            },
            {
                "title": "Structure du Registre - 5 Ruches",
                "bullets": [
                    "📂 HKEY_LOCAL_MACHINE (HKLM) : Config système globale (tous utilisateurs)",
                    "• Exemple : HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run (programmes démarrage)",
                    "",
                    "👤 HKEY_CURRENT_USER (HKCU) : Config utilisateur actuel",
                    "• Exemple : HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer (paramètres Explorateur)",
                    "",
                    "🔗 HKEY_CLASSES_ROOT (HKCR) : Associations fichiers + COM objects",
                    "• Exemple : HKCR\\.txt → ouvre fichiers .txt avec quelle app",
                    "",
                    "👥 HKEY_USERS (HKU) : Profils tous utilisateurs (HKCU = sous-clé de HKU)",
                    "",
                    "⚙️ HKEY_CURRENT_CONFIG (HKCC) : Config matériel actuelle (profile hardware)"
                ]
            },
            {
                "title": "Types de Valeurs Registry",
                "bullets": [
                    "📝 REG_SZ : Chaîne texte (ex: 'C:\\Windows')",
                    "🔢 REG_DWORD : Nombre 32-bit (ex: 1 = activé, 0 = désactivé)",
                    "📊 REG_QWORD : Nombre 64-bit",
                    "📄 REG_MULTI_SZ : Chaînes multiples (liste)",
                    "🔗 REG_EXPAND_SZ : Chaîne avec variables (ex: '%SystemRoot%')",
                    "🗃️ REG_BINARY : Données binaires brutes"
                ]
            },
            {
                "title": "Opérations Basiques - Créer/Modifier/Supprimer",
                "code": "# Créer nouvelle clé:\n1. Clic droit sur clé parente → Nouveau → Clé\n2. Nommer la nouvelle clé\n\n# Créer nouvelle valeur:\n1. Clic droit dans panneau droit → Nouveau → DWORD (32-bit) / Chaîne / etc.\n2. Nommer la valeur\n3. Double-clic → Entrer données\n\n# Modifier valeur existante:\nDouble-clic sur valeur → Modifier données → OK\n\n# Supprimer clé/valeur:\nClic droit → Supprimer → Confirmer\n\n# Chercher clé/valeur:\nCtrl + F → Entrer terme recherché → Suivant"
            },
            {
                "title": "Sauvegarder & Restaurer Registry",
                "code": "# MÉTHODE 1 : Exporter clé spécifique (recommandé):\n1. Clic droit sur clé à sauvegarder → Exporter\n2. Choisir emplacement (ex: Bureau\\backup_registry.reg)\n3. Sauvegarder\n\n# Restaurer backup:\nDouble-clic fichier .reg → Oui → OK\nOU : Clic droit .reg → Fusionner\n\n# MÉTHODE 2 : Point de Restauration Système (recommandé avant modifs majeures):\nWin + R → rstrui → Créer point de restauration\nSi problème Registry → Restauration système restaure aussi Registry!\n\n# MÉTHODE 3 : Export complet (backup total):\nregedit → Fichier → Exporter → Plage export: Tout → Sauvegarder\n⚠️ Fichier volumineux (100-300 MB)!"
            },
            {
                "title": "Tweaks Registry Utiles",
                "code": "# 1. Désactiver Windows Defender (temporaire test):\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\nCréer DWORD: DisableAntiSpyware = 1\n(Redémarrer requis)\n\n# 2. Réduire durée menu boot (plus rapide):\nWin + R → msconfig → Onglet Démarrage → Délai: 3 secondes\nOU Registry:\nHKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\BootControl\nDWORD: Timeout = 3 (secondes)\n\n# 3. Désactiver publicités menu Démarrer:\nHKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\nDWORD: SystemPaneSuggestionsEnabled = 0\nDWORD: SubscribedContent-338388Enabled = 0\n\n# 4. Activer mode Dieu (God Mode):\n1. Créer dossier sur Bureau\n2. Renommer: GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}\n→ Dossier = accès direct à TOUS paramètres Windows!\n\n# 5. Désactiver télémétrie (privacy):\nHKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\nDWORD: AllowTelemetry = 0\n(Redémarrer requis)"
            },
            {
                "title": "Commandes Registry via CMD/PowerShell",
                "code": "# CMD - REG command:\nreg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion  # Lire clé\nreg add HKCU\\Software\\TestKey /v TestValue /t REG_SZ /d \"Texte\" /f  # Ajouter valeur\nreg delete HKCU\\Software\\TestKey /f  # Supprimer clé\n\n# PowerShell:\nGet-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\"  # Lire\nNew-ItemProperty -Path \"HKCU:\\Software\\TestKey\" -Name \"TestValue\" -Value \"Texte\" -PropertyType String  # Créer\nRemove-ItemProperty -Path \"HKCU:\\Software\\TestKey\" -Name \"TestValue\"  # Supprimer valeur\nRemove-Item -Path \"HKCU:\\Software\\TestKey\" -Recurse  # Supprimer clé\n\n# Importer fichier .reg via CMD:\nreg import C:\\Backup\\backup.reg"
            },
            {
                "info": "💡 Astuce: Ajouter clés fréquentes aux Favoris! Registry Editor → Clé → Favoris → Ajouter aux favoris. Accès rapide sans navigation!"
            },
            {
                "warning": "⚠️ DANGER: Modifications Registry incorrectes = Windows INUTILISABLE! TOUJOURS créer Point Restauration AVANT modifications. Si doute, NE PAS modifier. Tweaks Internet = vérifier source fiable (Microsoft, forums officiels)."
            }
        ]
    },

    "win11_troubleshooting": {
        "title": "🔧 Dépannage Avancé Windows 11",
        "sections": [
            {
                "title": "Options de Démarrage Avancées",
                "code": "# Accéder Options Démarrage Avancées:\n\n# MÉTHODE 1 : Depuis Windows (fonctionnel):\nParamètres → Système → Récupération → Redémarrage avancé → Redémarrer maintenant\n\n# MÉTHODE 2 : Écran connexion:\nMaintenir Shift + Clic 'Redémarrer' (bouton marche/arrêt)\n\n# MÉTHODE 3 : Windows ne démarre PAS:\n1. Allumer PC\n2. Dès logo Windows → Bouton Power 10 sec (forcer arrêt)\n3. Répéter 3 fois → Windows lance auto Réparation automatique\n\n# MÉTHODE 4 : Clé USB Windows 11:\nBoot sur USB → Réparer ordinateur → Dépannage"
            },
            {
                "title": "Mode Sans Échec (Safe Mode)",
                "code": "# Démarrer en Mode Sans Échec:\nOptions Démarrage Avancées → Dépannage → Options avancées → Paramètres de démarrage → Redémarrer\n→ Appuyer F4 (Mode sans échec)\n→ Appuyer F5 (Mode sans échec avec réseau)\n→ Appuyer F6 (Invite commandes mode sans échec)\n\n# OU via msconfig (depuis Windows):\nWin + R → msconfig → Onglet Démarrage → ☑ Démarrage sécurisé → Minimal → OK → Redémarrer\n\n# OU via CMD (admin):\nbcdedit /set {current} safeboot minimal  # Sans réseau\nbcdedit /set {current} safeboot network  # Avec réseau\n# Redémarrer PC\n# Désactiver après:\nbcdedit /deletevalue {current} safeboot"
            },
            {
                "title": "Réparation Fichiers Système (SFC & DISM)",
                "code": "# SFC (System File Checker) - Répare fichiers Windows corrompus:\n1. Ouvrir CMD en Administrateur\n2. sfc /scannow\n3. Attendre scan complet (10-30 min)\n\n# Si SFC échoue → DISM (répare l'image Windows):\nDISM /Online /Cleanup-Image /CheckHealth      # Vérif rapide\nDISM /Online /Cleanup-Image /ScanHealth       # Scan approfondi\nDISM /Online /Cleanup-Image /RestoreHealth    # Réparer (télécharge depuis Windows Update)\n\n# Séquence complète (recommandée):\nDISM /Online /Cleanup-Image /RestoreHealth\nsfc /scannow\n# Redémarrer PC"
            },
            {
                "title": "Restauration Système",
                "code": "# Créer Point de Restauration:\n1. Win + R → sysdm.cpl → Onglet Protection système\n2. Sélectionner disque C: → Configurer → Activer protection\n3. Créer → Nommer point → Créer\n\n# Restaurer depuis Point:\n1. Win + R → rstrui → Suivant\n2. Choisir point restauration (avant problème)\n3. Suivant → Terminer → Oui\n\n# Restaurer depuis Options Démarrage Avancées (si Windows plante):\nOptions Avancées → Restauration système → Choisir point → Restaurer"
            },
            {
                "title": "Réparer Démarrage Windows (Bootloader)",
                "code": "# Si Windows ne boot PAS → Réparer MBR/BCD:\n1. Boot sur clé USB Windows 11\n2. Réparer ordinateur → Dépannage → Invite commandes\n3. Exécuter commandes:\n\nbootrec /fixmbr         # Répare Master Boot Record\nbootrec /fixboot        # Répare secteur boot\nbootrec /scanos         # Scan installations Windows\nbootrec /rebuildbcd     # Reconstruit BCD (boot config)\n\n# Si UEFI (mode modern):\nbcdboot C:\\Windows /s C: /f UEFI\n\n# Redémarrer PC"
            },
            {
                "title": "Réinitialiser Windows 11 (Clean Install Partielle)",
                "code": "# Réinitialiser tout en gardant fichiers persos:\nParamètres → Système → Récupération → Réinitialiser ce PC → Démarrer\n\n# Options:\n→ Conserver mes fichiers : Garde Documents, Images, etc. Supprime apps/paramètres\n→ Tout supprimer : Clean install complète (comme neuf)\n\n# Téléchargement Cloud vs Local:\n→ Cloud : Télécharge dernière version Windows 11 (recommandé si connexion stable)\n→ Local : Utilise fichiers système actuels (plus rapide, offline)\n\n# ⏱️ Durée: 30-90 minutes selon options"
            },
            {
                "title": "Problèmes Courants & Solutions",
                "bullets": [
                    "❌ **Écran bleu (BSOD) fréquent**:",
                    "→ Noter code erreur (ex: DRIVER_IRQL_NOT_LESS_OR_EQUAL)",
                    "→ Mode Sans Échec → Désinstaller pilote récent (Gestionnaire périphériques)",
                    "→ Vérifier RAM (Windows Memory Diagnostic: Win+R → mdsched)",
                    "→ Mettre à jour BIOS + tous drivers (carte mère, GPU, chipset)",
                    "",
                    "🐌 **PC très lent après update Windows**:",
                    "→ Désinstaller update récent: Paramètres → Windows Update → Historique mises à jour → Désinstaller",
                    "→ Désactiver programmes démarrage (Gestionnaire tâches → Démarrage)",
                    "→ Nettoyage disque: cleanmgr → Cocher tout → OK",
                    "→ Défragmenter (HDD seulement): dfrgui",
                    "",
                    "🔇 **Pas de son**:",
                    "→ Clic droit icône son → Résoudre problèmes",
                    "→ Gestionnaire périphériques → Audio → Désinstaller pilote → Redémarrer (réinstalle auto)",
                    "→ Services → Windows Audio → Démarrer + Type démarrage Automatique",
                    "",
                    "🌐 **Pas de connexion Internet (Wi-Fi/Ethernet)**:",
                    "→ CMD (admin): ipconfig /release → ipconfig /renew → ipconfig /flushdns",
                    "→ Redémarrer routeur + PC",
                    "→ Réinitialiser réseau: Paramètres → Réseau → Réinitialisation réseau",
                    "→ Mettre à jour pilote carte réseau (Gestionnaire périphériques)",
                    "",
                    "💾 **Disque 100% constamment (Task Manager)**:",
                    "→ Désactiver Windows Search: services.msc → Windows Search → Arrêter + Désactiver",
                    "→ Désactiver SuperFetch: services.msc → SysMain → Arrêter + Désactiver",
                    "→ Vérifier malware (Windows Defender scan complet)",
                    "→ Vérifier erreurs disque: chkdsk C: /f /r (redémarrage requis)"
                ]
            },
            {
                "title": "Outils Diagnostics Avancés",
                "code": "# Event Viewer (journaux erreurs système):\nWin + R → eventvwr.msc\n→ Journaux Windows → Système / Application\n→ Filtrer par 'Erreur' et 'Avertissement'\n\n# Reliability Monitor (historique pannes):\nWin + R → perfmon /rel\n→ Graphique stabilité système sur 30 jours\n\n# Windows Memory Diagnostic (test RAM):\nWin + R → mdsched → Redémarrer et vérifier\n\n# Performance Monitor:\nWin + R → perfmon\n→ Surveiller CPU, RAM, Disque en temps réel\n\n# Resource Monitor (détails processus):\nGestionnaire tâches → Performance → Ouvrir Moniteur ressources\n→ Voir EXACT processus utilisant CPU/Disque/Réseau"
            },
            {
                "info": "💡 Créer Point Restauration AVANT toute modification importante (install drivers, tweaks Registry, updates majeures). Peut sauver des heures de dépannage!"
            },
            {
                "warning": "⚠️ Réinitialiser PC = dernier recours! Essayer d'abord: Mode Sans Échec, SFC/DISM, Restauration Système. Sauvegarder données AVANT réinitialisation (même si option 'Conserver fichiers')."
            }
        ]
    },

    "win11_performance": {
        "title": "📊 Surveillance Performances & Event Viewer",
        "sections": [
            {
                "title": "Gestionnaire de Tâches - Onglet Performances",
                "code": "# Ouvrir Gestionnaire Tâches:\nCtrl + Shift + Esc\n\n# Onglet Performances - Sections:\n📊 CPU : % utilisation, vitesse, threads, processus\n💾 Mémoire : RAM utilisée/totale, cache, pool paginé\n💿 Disque : % activité, vitesse lecture/écriture (MB/s)\n🌐 Wi-Fi/Ethernet : Débit envoi/réception (Mbps)\n🎮 GPU : % utilisation, mémoire dédiée (si carte graphique dédiée)\n\n# Clic 'Ouvrir Moniteur ressources' (bas) → Détails avancés"
            },
            {
                "title": "Moniteur de Ressources (Resource Monitor)",
                "code": "# Ouvrir Resource Monitor:\nGestionnaire Tâches → Performance → Ouvrir Moniteur ressources\nOU : Win + R → resmon\n\n# 5 Onglets détaillés:\n\n1️⃣ **Vue d'ensemble** : Résumé CPU, Disque, Réseau, Mémoire\n\n2️⃣ **CPU** :\n   - Processus : Voir EXACT thread utilisant CPU\n   - Services associés : Quel service Windows utilise CPU\n   - Handles : Fichiers/registres ouverts par processus\n\n3️⃣ **Mémoire** :\n   - Commit (MB) : Mémoire réservée par processus\n   - Working Set : RAM physique utilisée\n   - Shareable : Mémoire partageable entre processus\n\n4️⃣ **Disque** :\n   - Activité disque : Fichier EXACT lu/écrit en temps réel\n   - Processus → Fichier : Qui lit/écrit quel fichier\n   - Vitesse lecture/écriture par processus\n\n5️⃣ **Réseau** :\n   - Processus avec activité réseau : Qui télécharge/upload\n   - Adresses IP/Ports : Connexions actives par processus\n   - Débit envoi/réception par processus"
            },
            {
                "title": "Performance Monitor (perfmon)",
                "code": "# Ouvrir Performance Monitor:\nWin + R → perfmon\n\n# Ajouter compteurs personnalisés:\n1. Graphique → Clic droit → Ajouter compteurs\n2. Choisir catégorie (Processeur, Mémoire, Disque logique, etc.)\n3. Sélectionner compteurs souhaités:\n   • Processeur: % temps processeur, interruptions/s\n   • Mémoire: Pages/s, mémoire disponible (Mo)\n   • Disque logique: % temps disque, lectures/s, écritures/s\n4. Ajouter → OK\n\n# Surveiller en temps réel:\nGraphique ligne = évolution temps réel\nCtrl+H = Histogramme (barres)\nCtrl+R = Rapport (valeurs numériques)\n\n# Créer ensemble de collecteurs (logs longs):\nEnsembles Collecteurs Données → Défini par utilisateur → Nouveau\n→ Configurer compteurs → Durée/intervalle → Démarrer\n→ Enregistre logs .blg pour analyse ultérieure"
            },
            {
                "title": "Event Viewer (Observateur d'Événements)",
                "code": "# Ouvrir Event Viewer:\nWin + R → eventvwr.msc\nOU : Menu Démarrer → Outils Admin → Observateur événements\n\n# Structure:\n📂 Journaux Windows:\n   • Application : Erreurs logiciels (apps installées)\n   • Sécurité : Tentatives connexion, modifications sécurité\n   • Installation : Installations/mises à jour Windows\n   • Système : Erreurs drivers, services, boot\n\n📂 Journaux Applications et Services:\n   • Microsoft → Windows → Catégories spécifiques (Defender, PowerShell, etc.)\n\n# Niveaux événements:\n🔴 Erreur : Problème significatif (perte données, service crashé)\n⚠️ Avertissement : Problème potentiel (disque presque plein)\nℹ️ Informations : Événement normal (service démarré)\n✅ Audit succès : Action sécurité réussie (connexion user)\n❌ Audit échec : Action sécurité échouée (mauvais password)"
            },
            {
                "title": "Analyser Erreurs Event Viewer",
                "code": "# Filtrer erreurs critiques:\n1. Clic droit 'Système' → Filtrer journal actuel\n2. Cocher: Critique, Erreur, Avertissement\n3. OK → Voir seulement problèmes\n\n# Chercher erreur spécifique:\nCtrl + F → Entrer code erreur (ex: 'Erreur 41', 'WHEA-Logger')\n\n# Interpréter entrée événement:\n📌 Source : Composant ayant généré événement (ex: 'Disk', 'DistributedCOM')\n📌 ID événement : Code numérique unique (ex: 41 = arrêt inattendu)\n📌 Description : Détails événement\n\n# Erreurs courantes:\n• ID 41 (Kernel-Power) : Arrêt brutal PC (coupure courant, crash)\n• ID 10016 (DistributedCOM) : Permissions DCOM (souvent inoffensif)\n• ID 7000 (Service Control Manager) : Service n'a pas démarré\n• ID 1014 (DNS Client) : Échec résolution nom (DNS)\n\n# Recherche Google:\nCopier 'Source' + 'ID événement' + premiers mots description\nEx: \"Disk Event ID 11\" → Forums/docs Microsoft"
            },
            {
                "title": "Reliability Monitor (Moniteur Fiabilité)",
                "code": "# Ouvrir Reliability Monitor:\nWin + R → perfmon /rel\nOU : Panneau config → Sécurité et Maintenance → Maintenance → Afficher historique fiabilité\n\n# Graphique stabilité (Indice 1-10):\n📉 Ligne graphique : Stabilité système sur 30 derniers jours\n10 = Aucun crash, 1 = Crashes fréquents\n\n# Événements marqués:\n🔴 Cercle rouge X : Arrêt inattendu, crash app, erreur Windows\n⚠️ Triangle jaune : Avertissement (update, config modifiée)\nℹ️ Cercle bleu i : Info (install logiciel, update réussie)\n\n# Clic sur jour → Détails:\nVoir EXACT crash/erreur → Vérifier solution en ligne\n\n# Usage:\nPC instable récemment? → Reliability Monitor → Chercher pic d'erreurs\n→ Voir si lié à install récente / update Windows\n→ Désinstaller soft/update problématique"
            },
            {
                "title": "Baseline Performances (Référence)",
                "bullets": [
                    "✅ **CPU Usage Normal** :",
                    "• Idle (rien faire): 2-10%",
                    "• Navigation web: 10-30%",
                    "• Gaming/Montage vidéo: 50-100% (normal!)",
                    "• >80% constant (rien faire) = problème (malware, service bloqué)",
                    "",
                    "✅ **RAM Usage Normal** :",
                    "• Windows 11 idle: 4-6 GB (sur 16 GB total)",
                    "• 50-70% utilisé = normal (Windows précharge apps)",
                    "• >90% constant = ajouter RAM OU fermer apps",
                    "",
                    "✅ **Disque Usage Normal** :",
                    "• Idle: 0-10%",
                    "• Copy fichiers: 50-100% (temporaire)",
                    "• 100% constant (>5 min) = problème (Windows Search, malware, disque défaillant)",
                    "",
                    "✅ **Températures CPU** :",
                    "• Idle: 30-50°C",
                    "• Charge moyenne: 50-70°C",
                    "• Gaming/Rendering: 70-85°C (acceptable)",
                    "• >90°C = danger (throttling, réduire perf, nettoyer ventilateurs)",
                    "• Logiciels monitoring: HWiNFO, Core Temp, MSI Afterburner"
                ]
            },
            {
                "title": "Diagnostics Automatiques Windows",
                "code": "# Performance Troubleshooter:\nParamètres → Système → Résolution problèmes → Autres utilitaires résolution problèmes\n→ Lancer 'Performances et maintenance système'\n\n# Windows Memory Diagnostic (test RAM):\nWin + R → mdsched → Redémarrer et vérifier\n→ Test complet RAM (détecte barrettes défectueuses)\n\n# Disk Check (vérifier erreurs disque):\nExplorateur → Clic droit C: → Propriétés → Outils → Vérifier\nOU CMD (admin): chkdsk C: /f /r\n\n# System File Checker:\nCMD (admin): sfc /scannow\n\n# Network Diagnostics:\nParamètres → Réseau → État → Résolution problèmes réseau"
            },
            {
                "info": "💡 Event Viewer = mine d'or pour dépannage! Avant poster forum aide, toujours vérifier Event Viewer → Copier erreurs exactes. Experts peuvent diagnostiquer 10x plus vite avec Event IDs!"
            },
            {
                "warning": "⚠️ Disque 100% constant + lenteurs extrêmes = signe disque SSD/HDD mourant! Sauvegarder URGENCE données importantes. Vérifier santé disque: CrystalDiskInfo (gratuit). Remplacer si 'Caution' ou 'Bad'."
            }
        ]
    }

}
