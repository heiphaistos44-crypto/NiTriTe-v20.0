#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Page Agents IA - NiTriTe V18
Agent IA spécialisé en maintenance informatique avec autodiagnostic
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import requests
import json
import os
import platform
import psutil
from v14_mvp.design_system import DesignTokens
from v14_mvp.components import ModernCard, ModernButton
from v14_mvp.logger_system import logger
from v14_mvp.ai_api_manager import APIManager
from v14_mvp.ai_knowledge_extended import ExtendedKnowledgeBase
from v14_mvp.ai_rag_system import RAGSystem
from v14_mvp.ai_tool_calling import ToolCallSystem
from v14_mvp.ai_conversation_memory import ConversationMemory
from v14_mvp.ai_learning_system import LearningSystem
from v14_mvp.ai_multilingual import MultilingualSystem
from v14_mvp.ai_voice_interface import VoiceInterface

# Phase 10: Nouveau système enrichi (5000+ conseils, réponses non-scriptées)
from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
from v14_mvp.ai_response_generator import DynamicResponseGenerator
from v14_mvp.ai_intent_analyzer import IntentAnalyzer

# Phase 11: MCP Integration (10000% boost - Web, Code, Thinking, Memory)
from v14_mvp.ai_mcp_integration import MCPIntegration

# Essayer d'importer google-generativeai
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    logger.warning("AI_Agent", "google-generativeai non disponible - pip install google-generativeai")


class MaintenanceAIAgent:
    """Agent IA de maintenance informatique"""

    def __init__(self):
        self.conversation_history = []
        self.use_online_mode = False  # Mode local par défaut
        self.gemini_api_key = ""  # Clé API Gemini (legacy, maintenant géré par APIManager)

        # Nouveau gestionnaire multi-API
        self.api_manager = APIManager()

        # RAG System pour recherche web en temps réel
        self.rag_system = RAGSystem()
        self.use_rag = True  # Activer RAG par défaut

        # Tool Calling System pour exécution commandes avec confirmation
        self.tool_system = ToolCallSystem()
        self.enable_tool_calling = True  # Activer par défaut

        # Phase 6: Conversation Memory (contexte multi-sessions)
        self.memory = ConversationMemory()

        # Phase 7: Learning System (feedback et amélioration continue)
        self.learning = LearningSystem()

        # Phase 8: Multilingual Support (détection auto langue)
        self.multilingual = MultilingualSystem()
        self.detected_language = "fr"  # Langue détectée par défaut

        # Phase 9: Voice Interface (optionnel, lazy init)
        self.voice = None  # Initialisé seulement si utilisateur active
        self.voice_enabled = False

        # Phase 10: NOUVEAU - Système enrichi (5000+ conseils, génération dynamique)
        # =========================================================================
        # Remplace quick_responses scriptées par génération conversationnelle
        # 143 catégories techniques, réponses adaptatives
        # =========================================================================
        self.unified_kb = UnifiedKnowledgeBase()  # 5000+ conseils, 143 catégories
        self.response_generator = DynamicResponseGenerator(
            knowledge_base=self.unified_kb,
            api_manager=self.api_manager
        )
        self.intent_analyzer = IntentAnalyzer()

        # Configurer fuzzy matching avec catégories
        category_names = self.unified_kb.get_all_categories()
        self.intent_analyzer.set_categories(category_names)

        logger.info("AI_Agent", f"Knowledge base unifiée chargée: {len(category_names)} catégories")

        # Phase 11: MCP Integration - Super-pouvoirs de l'agent
        self.mcp = MCPIntegration()
        capabilities = self.mcp.enhance_agent_capabilities()
        logger.info("AI_Agent", f"MCP activé: {len(capabilities)} capacités enrichies")

        # Knowledge Base ÉTENDUE (616+ entrées) - CONSERVÉE pour compatibilité
        self.extended_kb = ExtendedKnowledgeBase()
        self.extended_knowledge = self.extended_kb.get_all_knowledge()

        # Fusionner avec la knowledge base legacy pour compatibilité
        self.knowledge_base = {
            "diagnostic": [
                "HWMonitor: Surveillez températures CPU/GPU, tensions, vitesses des ventilateurs en temps réel",
                "HWiNFO64: Diagnostic matériel complet avec logs et alertes personnalisables",
                "CrystalDiskMark: Testez vitesses lecture/écriture séquentielle et aléatoire de vos disques",
                "CrystalDiskInfo: Vérifiez la santé des disques avec technologie S.M.A.R.T.",
                "CPU-Z: Informations détaillées CPU, RAM, carte mère, fréquences et voltages",
                "GPU-Z: Détails GPU, VRAM, températures, fréquences et utilisation",
                "MemTest86: Testez la RAM pour détecter erreurs mémoire (bootable USB)",
                "Wise Care 365: Suite complète diagnostic, nettoyage et optimisation système",
                "Utilisez Event Viewer (eventvwr.msc) pour analyser les erreurs système",
                "Lancez sfc /scannow pour réparer fichiers système Windows corrompus",
                "DISM /Online /Cleanup-Image /RestoreHealth pour réparer l'image Windows",
                "chkdsk /f /r pour vérifier et réparer erreurs disque dur",
                "Testez la stabilité du système avec Prime95 (stress test CPU)",
                "FurMark pour stress test GPU et détecter problèmes graphiques",
                "WhoCrashed: Analyse automatique des crash dumps et BSOD",
                "BlueScreenView: Lecture détaillée des minidump crashes Windows",
                "UserBenchmark: Benchmark rapide et comparaison avec PC similaires",
                "Speccy: Vue d'ensemble complète des spécifications matérielles",
                "MSI Afterburner: Monitoring GPU en jeu avec OSD personnalisable",
                "HDD Sentinel: Santé disques avec prédiction de défaillance",
                "Victoria HDD: Test bas niveau secteurs défectueux disques durs",
                "Reliability Monitor: Historique fiabilité système (perfmon /rel)",
                "Resource Monitor: Analyse détaillée utilisation CPU/RAM/disque/réseau (resmon)",
                "Process Explorer: Task Manager avancé (Microsoft Sysinternals)",
                "BatteryInfoView: État batterie portable (cycles, capacité, usure)",
                "OCCT: Stress test CPU/GPU/PSU avec détection erreurs",
                "Cinebench: Benchmark rendu CPU multithread (R23/R24)",
                "3DMark: Benchmark gaming synthétique (Time Spy, Fire Strike)",
                "PassMark PerformanceTest: Suite benchmark complète tous composants",
                "DPC Latency Checker: Détecte problèmes latence audio/vidéo pilotes"
            ],
            "optimisation": [
                "Gestionnaire des tâches > Démarrage: Désactivez programmes inutiles au boot (viser < 10)",
                "services.msc: Désactivez services Windows inutiles (Télécopie, Bluetooth si non utilisé)",
                "Nettoyage de disque: Supprimez fichiers temporaires, cache, téléchargements anciens",
                "Vider cache DNS: ipconfig /flushdns et ipconfig /release puis /renew",
                "Désactivez effets visuels: Panneau > Système > Paramètres avancés > Performances",
                "Défragmentation HDD mensuelle (NE JAMAIS défragmenter un SSD!)",
                "SSD: Activez TRIM avec 'fsutil behavior set disabledeletenotify 0'",
                "Ajustez taille fichier d'échange: 1.5x RAM minimum, 3x RAM maximum recommandé",
                "Désactivez indexation sur SSD: Propriétés lecteur > Décocher indexation",
                "Nettoyez registre avec CCleaner ou Wise Registry Cleaner (avec précaution)",
                "Désinstallez bloatware et programmes inutilisés via Panneau de configuration",
                "Limitez applications arrière-plan: Paramètres > Confidentialité > Applications",
                "Mode haute performance: Panneau > Options d'alimentation > Hautes performances",
                "Augmentez RAM si utilisation > 80% constante (8GB minimum, 16GB recommandé)",
                "Mettez à jour BIOS pour performances et compatibilité améliorées",
                "Désactivez Game Bar Xbox si non-joueur: Paramètres > Jeux > Game Bar",
                "Optimisez Windows Search: Limitez les emplacements indexés",
                "Nettoyez dossier WinSxS: DISM /Online /Cleanup-Image /StartComponentCleanup",
                "Désactivez Cortana si non utilisé: GPedit.msc ou Registre",
                "Désactivez OneDrive sync si non nécessaire (économise CPU/RAM)",
                "BleachBit: Alternative open-source à CCleaner pour nettoyage système",
                "Revo Uninstaller: Désinstallation complète avec suppression résidus",
                "Debloat scripts Windows 10/11: Supprimez apps pré-installées inutiles",
                "Désactivez télémétrie: O&O ShutUp10++ ou scripts PowerShell",
                "Optimisez boot: msconfig > Boot > Décocher GUI de démarrage",
                "Priority: Augmentez priorité apps importantes via Task Manager",
                "Affinity: Assignez programmes à cœurs CPU spécifiques (gaming)",
                "RAM Disk: Créez disque virtuel RAM pour fichiers temporaires navigateur",
                "Prefetch/Superfetch: Désactivez si PC lent (services.msc)",
                "Compact OS: Compressez Windows (compact /compactos:always) = gain 2-4GB",
                "Hibernation: Désactivez si jamais utilisé (powercfg /h off) = gain RAM taille",
                "Tâches planifiées: Désactivez tâches inutiles (Task Scheduler)",
                "Animations: Désactivez toutes (SystemPropertiesPerformance.exe)",
                "Transparence: Désactivez effets transparence Windows (gain GPU)",
                "Notifications: Limitez notifications intempestives (Paramètres)",
                "Apps startup: Utilisez Autoruns (Sysinternals) pour contrôle avancé",
                "Context menu: Nettoyez menu contextuel avec ShellExView/ShellMenuView",
                "Duplicate files: Supprimez doublons avec dupeGuru ou Duplicate Cleaner",
                "Large files: TreeSize/WinDirStat pour visualiser espace disque",
                "Browser cache: Videz régulièrement caches Chrome/Firefox (peut atteindre Go!)"
            ],
            "sécurité": [
                "Windows Update: Activez mises à jour automatiques sécurité critiques",
                "Windows Defender: Scan complet hebdomadaire, protection temps réel activée",
                "Malwarebytes: Scan mensuel anti-malware/spyware complémentaire",
                "Spybot Search & Destroy: Protection contre spywares et immunisation navigateurs",
                "AdwCleaner: Supprimez adwares, PUPs, toolbars et hijackers navigateurs",
                "Créez des points de restauration avant modifications système importantes",
                "Sauvegarde 3-2-1: 3 copies, 2 supports différents, 1 hors site (cloud)",
                "Utilisez mots de passe forts: 12+ caractères, majuscules, chiffres, symboles",
                "Activez Windows Firewall et configurez règles sortantes",
                "BitLocker: Chiffrez disque système pour protection données sensibles",
                "UAC (Contrôle compte utilisateur): Maintenez niveau élevé",
                "Désactivez macros Office par défaut (risque malware)",
                "Vérifiez extensions navigateur: Supprimez extensions suspectes/inutiles",
                "HTTPS Everywhere: Forcez connexions sécurisées sites web",
                "Bloquez pop-ups et publicités avec uBlock Origin",
                "VPN recommandé pour WiFi publics et confidentialité navigation",
                "Désactivez SMBv1 (vulnérable): PowerShell Disable-WindowsOptionalFeature",
                "Vérifiez autorisations applications: Limitez accès caméra/micro/localisation",
                "Kaspersky Rescue Disk: Boot USB pour scan malware persistant",
                "HitmanPro: Second opinion scanner anti-malware (Sophos)",
                "ESET Online Scanner: Scan gratuit one-shot sans installation",
                "Sandboxie-Plus: Exécutez programmes suspects dans bac à sable isolé",
                "VirusTotal: Analysez fichiers suspects avec 70+ moteurs antivirus",
                "ProcessHacker: Surveillez processus suspects en temps réel",
                "TCPView: Surveillez connexions réseau actives (Sysinternals)",
                "Autoruns: Désactivez démarrages automatiques malveillants",
                "EMET/Windows Defender Exploit Guard: Protection anti-exploit",
                "Password managers: KeePass, Bitwarden (gratuits), 1Password, LastPass",
                "Authentification 2FA: Activez sur tous comptes importants",
                "Email: Ne cliquez JAMAIS liens suspects, vérifiez expéditeur",
                "Phishing: Vérifiez URL (typosquatting), certificat SSL (cadenas)",
                "Ransomware: Crypto locker, activez protection dossiers Windows Defender",
                "Port scans: ShieldsUP! (GRC) pour tester exposition internet",
                "Comodo Firewall: Alternative firewall avancé avec HIPS",
                "OpenDNS/NextDNS: Filtrage malware/phishing au niveau DNS",
                "Host file: Bloquez domaines malveillants (C:\\Windows\\System32\\drivers\\etc\\hosts)",
                "Désactivez RDP si non utilisé (Remote Desktop = porte d'entrée)",
                "VeraCrypt: Chiffrement conteneurs fichiers sensibles (successeur TrueCrypt)",
                "Secure erase: Suppression sécurisée (Eraser, SDelete avant vente PC)",
                "WiFi: WPA3 > WPA2 > désactivez WPS (vulnérable)",
                "Guest account: Désactivez compte invité Windows",
                "Admin account: Utilisez compte standard quotidien, admin seulement install"
            ],
            "performance": [
                "CPU < 80°C idle, < 85°C charge (remplacez pâte thermique si > 90°C)",
                "GPU < 50°C idle, < 85°C charge (nettoyez ventilateurs si > 90°C)",
                "RAM: Utilisation < 80% recommandée (8GB min, 16GB idéal, 32GB pro)",
                "Disque SSD: Minimum 15-20% espace libre pour performances optimales",
                "Nettoyez poussière PC tous les 3-6 mois (air comprimé, pinceau doux)",
                "Vérifiez rotation ventilateurs: Tous doivent tourner (sinon remplacer)",
                "Appliquez pâte thermique CPU tous les 2-3 ans",
                "Câble SATA: Utilisez SATA III 6Gb/s pour SSD (pas SATA II)",
                "Pilotes graphiques: Mise à jour mensuelle NVIDIA/AMD/Intel",
                "Moniteur utilisation: Task Manager > Performance pour identifier goulots",
                "Désactivez antivirus pendant gaming (risque, mais gain FPS)",
                "Fermez Chrome/navigateurs: Gros consommateurs RAM (20+ onglets = 2GB+)",
                "Xbox Game Bar: Désactivez si baisse FPS en jeu",
                "Activez XMP/DOCP BIOS pour RAM (vitesses annoncées constructeur)",
                "PCI-Express: Vérifiez que GPU est sur slot x16 (pas x8)",
                "Température ambiante: Maintenez pièce < 25°C pour meilleures perfs"
            ],
            "réseau": [
                "Routeur: Redémarrage hebdomadaire recommandé (déconnexion 30 sec)",
                "Ethernet vs WiFi: Câble = latence réduite, stabilité, vitesse max",
                "WiFi 5GHz: Moins congestionné, plus rapide mais portée réduite vs 2.4GHz",
                "Canal WiFi: Utilisez analyse (WiFi Analyzer) pour trouver canal libre",
                "DNS: Changez pour Cloudflare (1.1.1.1) ou Google (8.8.8.8) = vitesse",
                "QoS routeur: Priorisez trafic gaming/streaming sur navigation",
                "Pilotes réseau: Mise à jour depuis site fabricant carte mère",
                "ipconfig /flushdns: Videz cache DNS si sites ne chargent pas",
                "netsh winsock reset: Répare pile réseau Windows (redémarrage requis)",
                "Désactivez téléchargements Windows Update si lag gaming",
                "Test vitesse: Fast.com ou Speedtest.net (vérifiez vs forfait)",
                "Powerline adapters: Alternative si Ethernet impossible, meilleur que WiFi",
                "Répéteur WiFi: Étend portée mais réduit vitesse de 50%",
                "Mesh WiFi: Meilleure solution pour grande maison (Google WiFi, Orbi)",
                "VPN impact: Réduit vitesse 10-40% selon serveur/protocole",
                "WiFi 6/6E (802.11ax): Dernière norme, +40% vitesse vs WiFi 5",
                "Câble Ethernet: Cat5e (1Gbps), Cat6 (10Gbps courte), Cat6a/7 (10Gbps longue)",
                "netsh int tcp set global autotuninglevel=normal: Optimise TCP",
                "MTU: 1500 standard, 1492 PPPoE, testez optimal avec ping -f -l",
                "Bufferbloat: Testez avec waveform.com/tools/bufferbloat",
                "IPv6: Activez pour meilleures routes (mais vérifiez compatibilité)",
                "Bandwidth monitoring: NetLimiter, GlassWire pour identifier apps gourmandes",
                "PingPlotter: Diagnostic problèmes routage et packet loss",
                "WinMTR: Traceroute continu pour identifier sauts problématiques",
                "Router firmware: DD-WRT/OpenWRT pour fonctionnalités avancées",
                "Port forwarding: Configurez pour gaming/torrents (vérifiez sécurité)",
                "UPnP: Pratique mais risque sécurité, désactivez si non gaming",
                "Static IP: Réservez IP locale pour PC gaming (DHCP reservation)",
                "Network adapter: Intel > Realtek pour stabilité pilotes",
                "Wireless mode: N-only ou AC-only si tous devices compatibles",
                "Channel width: 20MHz (stabilité) vs 40/80MHz (vitesse) sur 5GHz",
                "Beamforming: Activez sur routeur WiFi 5/6 pour meilleur signal",
                "MU-MIMO: Multi-appareils simultanés sans perte vitesse",
                "Ping: < 20ms excellent, 20-50ms bon, 50-100ms acceptable, > 100ms problème",
                "Jitter: < 10ms requis gaming/VoIP, vérifiez avec speedtest",
                "Packet loss: 0% obligatoire, 1%+ = problème sérieux ligne/routeur"
            ],
            "écran_bleu": [
                "BSOD: Notez code erreur (ex: SYSTEM_SERVICE_EXCEPTION, IRQL_NOT_LESS_OR_EQUAL)",
                "BlueScreenView: Analysez dump mémoire pour identifier pilote fautif",
                "Désactivez overclocking CPU/GPU/RAM si instable",
                "Mettez à jour tous pilotes (GPU, chipset, réseau, audio)",
                "Testez RAM avec MemTest86 (8+ passes, 0 erreur)",
                "Vérifiez disque: chkdsk /f /r depuis CMD admin",
                "Restaurez point de restauration avant apparition BSOD",
                "Réinstallez Windows en dernier recours (sauvegardez avant!)",
                "Températures excessives peuvent causer BSOD (vérifiez avec HWMonitor)"
            ],
            "son": [
                "Aucun son: Vérifiez niveau volume Windows et application",
                "Clic droit Haut-parleurs > Résoudre problèmes de son",
                "Gestionnaire périphériques: Réinstallez pilote audio",
                "Realtek/Nahimic: Désactivez améliorations audio si grésillements",
                "Jack façade: Connectez arrière carte mère si problèmes façade",
                "Écouteurs Bluetooth: Oubliez et re-pairez si coupures",
                "Latence audio: Réduisez taille buffer dans paramètres DAW/ASIO",
                "Audio crackles: DPC Latency Checker pour identifier pilote problématique",
                "Spatial sound: Windows Sonic gratuit, Dolby Atmos payant (test gratuit)",
                "Exclusive mode: Activez pour qualité maximale (Propriétés > Avancé)",
                "Sample rate: 24-bit 48000Hz minimum audiophiles, 44100Hz suffisant",
                "ASIO drivers: Obligatoire production musicale (ASIO4ALL gratuit)",
                "VoiceMeeter: Routage audio virtuel avancé (streaming, recording)",
                "EarTrumpet: Remplacement volume mixer Windows amélioré",
                "Equalizer APO: Égaliseur système gratuit avec AutoEQ presets"
            ],
            "windows_commandes": [
                "sfc /scannow: Répare fichiers système corrompus",
                "DISM /Online /Cleanup-Image /RestoreHealth: Répare image Windows",
                "chkdsk C: /f /r: Vérifie et répare disque (requiert redémarrage)",
                "ipconfig /flushdns: Vide cache DNS",
                "ipconfig /release puis /renew: Renouvelle bail DHCP",
                "netsh winsock reset: Réinitialise pile réseau",
                "netsh int ip reset: Réinitialise config TCP/IP",
                "powercfg /batteryreport: Rapport santé batterie portable",
                "powercfg /energy: Analyse efficacité énergétique",
                "powercfg /h off: Désactive hibernation (libère espace)",
                "cleanmgr: Lance nettoyage disque graphique",
                "msconfig: Configuration démarrage système",
                "taskmgr: Gestionnaire des tâches",
                "resmon: Moniteur de ressources détaillé",
                "perfmon /rel: Historique fiabilité système",
                "eventvwr.msc: Observateur d'événements",
                "devmgmt.msc: Gestionnaire de périphériques",
                "diskmgmt.msc: Gestion des disques",
                "services.msc: Gestion des services Windows",
                "regedit: Éditeur de registre (ATTENTION!)",
                "gpedit.msc: Éditeur stratégie de groupe (Pro/Enterprise)",
                "sysdm.cpl: Propriétés système (variables environnement)",
                "appwiz.cpl: Programmes et fonctionnalités",
                "ncpa.cpl: Connexions réseau",
                "firewall.cpl: Pare-feu Windows",
                "control printers: Imprimantes et périphériques",
                "winver: Affiche version Windows",
                "dxdiag: Diagnostic DirectX (GPU, audio, input)",
                "SystemPropertiesAdvanced: Paramètres système avancés",
                "OptionalFeatures: Activer/désactiver fonctionnalités Windows",
                "shutdown /r /fw /t 0: Redémarre en BIOS/UEFI",
                "slmgr /xpr: Vérifie activation Windows",
                "tree /F > structure.txt: Exporte arborescence dossier"
            ],
            "gaming": [
                "Game Mode Windows: Activez (Paramètres > Jeux)",
                "NVIDIA Reflex: Activez in-game pour latence minimale (RTX 20+)",
                "DLSS/FSR: Quality mode = +40% FPS maintien qualité visuelle",
                "Ray-tracing: Désactivez sauf RTX 4070+ ou FPS > 100 natif",
                "V-Sync: Désactivez en compétitif (G-Sync/FreeSync suffisant)",
                "Triple buffering: Activez si V-Sync ON, sinon désactivez",
                "FPS cap: 3 sous refresh rate (141 pour 144Hz) réduit input lag",
                "Fullscreen vs Borderless: Fullscreen = meilleur perf, moins input lag",
                "Texture quality: Moyen/High si VRAM < 8GB, Ultra si 10GB+",
                "Shadow quality: Impact énorme, baissez en premier (Moyen/Bas)",
                "Anti-aliasing: TAA bon compromis, FXAA rapide, MSAA gourmand",
                "Ambient occlusion: SSAO rapide, HBAO+ beau mais lent",
                "Motion blur: Désactivez TOUJOURS (flou inutile)",
                "Depth of field: Désactivez (flou arrière-plan inutile compétitif)",
                "Lens flare/Chromatic aberration: Désactivez (pollution visuelle)",
                "Anisotropic filtering: 16x peu d'impact, améliorations textures distance",
                "View distance: Baissez si CPU-bound, peu d'impact si GPU-bound",
                "Foliage/Grass density: Baissez pour visibilité et FPS",
                "Post-processing: Moyen/Bas (effets secondaires peu utiles)",
                "MSI Afterburner OSD: Surveillez FPS, temps frame, températures, usage",
                "Rivatuner scanline sync: Alternative V-Sync ultra-low latency",
                "RTSS FPS limiter: Meilleur que limiteurs in-game",
                "Latency modes: NVIDIA Low Latency (Ultra), AMD Anti-Lag",
                "Shader cache: Activez NVIDIA/AMD pour réduire stutters",
                "Monitor: 144Hz+ obligatoire compétitif, 1ms response time",
                "Overdrive: Activez sur moniteur (réduit ghosting)",
                "Black equalizer: Augmentez visibilité zones sombres (moniteur gaming)",
                "Mouse: 800-1600 DPI pros, polling 1000Hz, désactivez accél Windows",
                "In-game sens: Trouvez votre 360° distance (généralement 20-40cm)",
                "Discord overlay: Désactivez si baisse FPS",
                "Windows focus assist: Gaming mode pour bloquer notifications",
                "Process priority: High pour jeu (Task Manager), Normal le reste",
                "Process lasso: Automatise gestion priorités et affinité CPU",
                "Timer resolution: Mieux que Windows default (Timer Resolution app)",
                "ISLC (Intelligent Standby List Cleaner): Libère RAM standby"
            ],
            "hardware": [
                "Bottleneck: Testez GPU 99% = bon, CPU 99% = CPU limite GPU",
                "CPU upgrade: AMD Ryzen 5 5600/7600 ou Intel i5-12400/13400 sweet spot",
                "GPU upgrade: Résolution 1080p 60fps = RTX 4060 / RX 7600",
                "GPU upgrade: 1440p 144fps = RTX 4070 Super / RX 7800 XT",
                "GPU upgrade: 4K 60fps = RTX 4080 / RX 7900 XTX",
                "RAM speed: Ryzen aime 3600MHz CL16, Intel moins sensible",
                "SSD: Samsung 980 Pro, WD SN850X, Crucial P5 Plus (Gen4 NVMe)",
                "PSU: 80+ Gold minimum, calculez besoin +150W marge (GPU + CPU TDP)",
                "PSU: Seasonic, Corsair RM/RMx, EVGA Supernova tiers A",
                "Thermalright Peerless Assassin: Meilleur rapport qualité/prix ventirad",
                "Noctua NH-D15: Top air cooling, silence absolu",
                "AIO: Arctic Liquid Freezer II excellent rapport prix/perf",
                "Thermal paste: Noctua NT-H1, Arctic MX-4, Thermal Grizzly Kryonaut",
                "Case airflow: 2-3 intake avant/bas, 1-2 exhaust arrière/haut",
                "Fan curve: 40% idle, rampe 60°C, 100% à 80°C",
                "Undervolting: Réduisez voltage CPU/GPU = moins chaleur, même perfs",
                "Overclocking: +5-15% perfs mais chaleur, instabilité, garantie perdue",
                "RAM OC: XMP/DOCP safe, manuel risqué mais gains 10-20%",
                "Monitor calibration: SpyderX, i1Display Pro pour couleurs précises",
                "Dual monitor: Même refresh rate sinon stutters, G-Sync sur primaire",
                "Keyboard: Mechanical > membrane, Cherry MX Brown polyvalent",
                "Mechanical switches: Red/Speed linéaire gaming, Blue clicky typiste",
                "Mouse sensor: PixArt 3360/3370/3395, Razer Focus+, Logitech HERO",
                "Mouse weight: 60-80g optimal gaming compétitif moderne",
                "Mousepad: Tissu = contrôle (Artisan, Zowie G-SR), hard = vitesse",
                "Headset: Audiotechnica M40x/M50x, Beyerdynamic DT770, Sennheiser HD599",
                "Gaming headsets: HyperX Cloud II, SteelSeries Arctis, Logitech G Pro X",
                "Microphone: Blue Yeti, Rode PodMic, Shure SM58 (XLR pro)",
                "Webcam: Logitech C920/C922 standard, Brio 4K, Elgato Facecam Pro",
                "Cable management: Velcro ties, tapis gaine, améliore airflow"
            ],
            "logiciels": [
                "7-Zip: Compresseur gratuit, .zip .rar .7z support",
                "VLC Media Player: Lit TOUS formats vidéo/audio",
                "Notepad++: Éditeur texte avancé programmation",
                "ShareX: Screenshots/screen recording puissant et gratuit",
                "OBS Studio: Streaming/recording Twitch/YouTube gratuit",
                "HandBrake: Conversion/compression vidéo open-source",
                "Audacity: Édition audio gratuite podcasts/musique",
                "GIMP: Retouche image gratuite (alternative Photoshop)",
                "Paint.NET: Édition image simple et rapide",
                "Inkscape: Création vectorielle gratuite (alternative Illustrator)",
                "Blender: 3D modeling/animation/rendering gratuit et pro",
                "DaVinci Resolve: Montage vidéo gratuit niveau pro",
                "VS Code: Éditeur code moderne polyvalent Microsoft",
                "qBittorrent: Client torrent open-source sans pub",
                "Brave/Firefox: Navigateurs respectueux vie privée",
                "uBlock Origin: Bloqueur publicités essentiel navigateur",
                "LibreOffice: Suite bureautique gratuite (alternative MS Office)",
                "Thunderbird: Client email open-source",
                "Discord: Communication vocal/text communauté gaming",
                "Spotify/YouTube Music: Streaming musical",
                "Steam: Plateforme jeux PC principale",
                "EpicGames: Jeux gratuits hebdomadaires",
                "GOG Galaxy: Jeux DRM-free, launcher universel",
                "Parsec: Remote desktop gaming ultra low latency",
                "TeamViewer/AnyDesk: Assistance à distance",
                "Revo Uninstaller: Désinstallation complète programmes",
                "Everything: Recherche fichiers instantanée Windows",
                "Ninite: Installation groupée logiciels populaires"
            ],
            "données": [
                "Règle 3-2-1: 3 copies, 2 supports différents, 1 hors site",
                "Windows Backup: Panneau > Sauvegarde et restauration",
                "Veeam Agent: Backup professionnel gratuit particuliers",
                "Macrium Reflect: Clone disque et images système",
                "Acronis True Image: Sauvegarde payante très complète",
                "Robocopy: Commande Windows sync dossiers puissante",
                "FreeFileSync: Synchronisation dossiers graphique",
                "Cloud: Google Drive 15GB, OneDrive 5GB, Mega 20GB gratuit",
                "Cloud payant: Google One, Dropbox, pCloud, iCloud",
                "NAS: Synology DS220+ excellent débutants",
                "Disque externe: 2-4TB HDD backup, SSD si transport fréquent",
                "RAID: RAID1 miroir sécurité, RAID0 vitesse, RAID5 compromis",
                "Partition recovery: TestDisk/PhotoRec récupère données perdues",
                "Recuva: Récupération fichiers supprimés simples",
                "Undelete 360: Alternative récupération gratuite",
                "Version History: Historique fichiers Windows (activez!)",
                "Shadow copies: Points restauration automatiques fichiers",
                "Chiffrement: VeraCrypt conteneurs, BitLocker système",
                "Secure erase: Eraser/SDelete écrasement sécurisé",
                "S.M.A.R.T.: CrystalDiskInfo surveillance santé disques"
            ],
            "dépannage": [
                "Redémarrez toujours en premier (80% problèmes résolus)",
                "Mode sans échec: F8 au boot ou msconfig > Boot > Safe boot",
                "Point de restauration: rstrui.exe si problème récent",
                "Clean boot: msconfig > Services > Masquer Microsoft, désactivez tout",
                "Désinstallez mises à jour récentes si problème apparu après",
                "Réparer démarrage: Média installation > Réparer ordinateur",
                "SFC puis DISM si erreurs système",
                "Vérifiez Event Viewer pour erreurs spécifiques",
                "Googlez message d'erreur EXACT avec guillemets",
                "Pilotes: Désinstallez avec DDU si GPU, réinstallation propre",
                "Conflit logiciels: Désinstallez derniers programmes installés",
                "Température: Vérifiez HWMonitor si ralentissements soudains",
                "RAM: MemTest86 si crashes aléatoires/BSOD",
                "Disque: CrystalDiskInfo si bruits suspects/lenteurs",
                "Infection: Malwarebytes scan si comportement anormal",
                "Réinitialisation Windows: Dernier recours, conservez fichiers",
                "Installation propre: Format C: résout 99% problèmes tenaces"
            ],
            "windows_installation": [
                "Création USB bootable: Media Creation Tool officiel Microsoft gratuit",
                "Téléchargez ISO Windows 10/11 depuis site officiel Microsoft uniquement",
                "Rufus: Alternative création USB boot, plus d'options (MBR/GPT, UEFI/Legacy)",
                "USB minimum 8GB, toutes données seront effacées pendant création",
                "Ventoy: Bootez plusieurs ISO depuis même USB (multi-boot pratique)",
                "Clé produit: Notez avec ShowKeyPlus avant réinstallation (liée carte mère OEM)",
                "UEFI vs Legacy BIOS: UEFI moderne obligatoire Windows 11, GPT partition",
                "Secure Boot: Requis Windows 11, activez dans BIOS/UEFI avant install",
                "TPM 2.0: Obligatoire Windows 11, vérifiez tpm.msc avant upgrade",
                "Bypass TPM W11: Regedit pendant install possible mais non recommandé (pas MAJ sécurité)",
                "Partitionnement: Supprimez TOUTES partitions pour installation propre (clean slate)",
                "Installation rapide vs personnalisée: Personnalisée = contrôle total privacy",
                "Compte local vs Microsoft: Local = privacy, Microsoft = sync multi-devices",
                "Windows 11 bypass compte Microsoft: OOBE\\BYPASSNRO dans CMD pendant install",
                "Pilote réseau sur USB: Backup crucial si carte WiFi non reconnue post-install",
                "Ordre installation post-Windows: 1) Chipset 2) GPU 3) Audio 4) Réseau 5) Utilitaires",
                "Windows Update d'abord: 3-4 redémarrages complets avant installer logiciels",
                "Activation KMS vs Retail: Retail légitime transférable, KMS risqué illégal",
                "In-place upgrade: Répare Windows sans perdre données (setup.exe depuis ISO monté)",
                "WinPE: Environnement récupération avancé (Hiren's Boot, gandalf PE)",
                "Dual boot précautions: Installez Windows AVANT Linux pour éviter GRUB corruption",
                "BitLocker avant format: Décryptez complètement sinon données perdues définitivement",
                "Sauvegarde complète avant: Macrium Reflect image système = filet sécurité",
                "DISM pour ISO custom: Ajoutez pilotes/logiciels dans image installation",
                "NTLite: Créez ISO Windows personnalisé (enlever bloatware, intégrer updates)",
                "Clé générique install: Utilisez clé générique si pas de clé (activez après)",
                "SkipMachineOOBE + SkipUserOOBE: Regedit skip questions inutiles installation",
                "Sysprep: Généralise Windows pour déploiement multi-machines (IT pro)",
                "Windows To Go: Windows sur USB externe bootable (Enterprise feature)",
                "Repair Windows via CMD: bootrec /fixmbr /fixboot /rebuildbcd depuis recovery"
            ],
            "bios_uefi": [
                "Accès BIOS: Del, F2, F10, F12 selon fabricant (spam touche au boot)",
                "UEFI moderne: Interface graphique, souris, réseau, plus rapide que Legacy BIOS",
                "Boot order: Priorité démarrage (SSD Windows en premier, USB si installation)",
                "Fast Boot: Réduit temps démarrage mais complique accès BIOS (désactivez temporairement)",
                "Secure Boot: Vérifie signatures système d'exploitation bootées (requis W11)",
                "CSM (Compatibility Support Module): Mode Legacy pour vieux OS, désactivez si UEFI",
                "XMP/DOCP: Active profil RAM annoncé (3200MHz etc.), obligatoire sinon 2133MHz default",
                "AHCI vs IDE: AHCI pour SSD obligatoire (performances), IDE = ancien HDD",
                "SATA modes: RAID si multi-disques miroir, AHCI si disques individuels",
                "Virtualization (VT-x/AMD-V): Activez pour VM (VirtualBox, Hyper-V, BlueStacks)",
                "Intel VT-d / AMD IOMMU: Passthrough GPU vers VM (avancé)",
                "TPM 2.0: Trusted Platform Module, activez si présent (requis W11, BitLocker)",
                "PTT (Intel) / fTPM (AMD): TPM firmware, activez dans BIOS pour Windows 11",
                "Resizable BAR: Améliore perfs GPU modernes (RTX 3000+, RX 6000+) si CPU supporte",
                "Above 4G Decoding: Requis avec Resizable BAR, activez ensemble",
                "CSM disabled: Obligatoire Resizable BAR et Secure Boot ensemble",
                "CPU C-States: États économie énergie, désactivez pour OC extrême sinon laissez",
                "Intel SpeedStep / AMD Cool'n'Quiet: Gestion fréquence dynamique, laissez activé",
                "Spread Spectrum: Réduit interférences électromagnétiques mais instabilité OC",
                "Legacy USB Support: Clavier/souris USB en DOS/BIOS, laissez activé",
                "IOMMU: Isolation mémoire VM, requis passthrough GPU avancé",
                "HPET (High Precision Event Timer): Laissez auto ou forcez disable (gains latence gaming)",
                "Restore optimized defaults: Reset BIOS si problèmes après changements",
                "Clear CMOS: Jumper ou pile BIOS retirez 30 sec = reset complet paramètres",
                "BIOS flashback: Bouton update BIOS via USB sans CPU/RAM (cartes mères haut gamme)",
                "Q-Flash/M-Flash: Update BIOS depuis interface BIOS directement",
                "BIOS update Windows: Possible mais RISQUÉ (panne courant = brick), préférez DOS",
                "Beta BIOS: Risqué instabilité, attendez version stable sauf problème spécifique",
                "Downgrade BIOS: Possible mais peut perdre fonctionnalités (AGESA AMD)",
                "AGESA updates (AMD): Microcode améliore RAM/CPU, important Ryzen 5000/7000",
                "POST codes: LEDs debug carte mère (Rouge=CPU, Jaune=RAM, Blanc=GPU, Vert=OK)",
                "Boot loops: Clear CMOS, retirez RAM/GPU, testez une par une",
                "BIOS password: Protection accès, notez bien sinon clear CMOS obligatoire",
                "Fan control: Courbes ventilateurs personnalisées (silencieux idle, puissant load)",
                "CPU Fan vs Chassis Fan: Headers différents, configurez vitesses séparément",
                "PWM vs DC: PWM = contrôle moderne 4pin, DC = 3pin voltage control",
                "Smart Fan Mode: Auto ajuste vitesse selon température, recommandé",
                "RGB control: BIOS peut contrôler certains éclairages (Aura, Mystic Light)",
                "Trusted Computing: TPM related, laissez activé sauf problèmes spécifiques",
                "Network stack: Boot réseau PXE, désactivez si jamais utilisé (boot plus rapide)"
            ],
            "drivers": [
                "Ordre installation: 1.Chipset 2.GPU 3.Audio 4.LAN/WiFi 5.USB 6.Périphériques",
                "Chipset drivers: Carte mère site fabricant (AMD, Intel), CRUCIAL pour stabilité",
                "AMD Chipset: Installe Power Plan Ryzen optimisé, obligatoire Ryzen performance",
                "Intel Chipset: INF drivers, Management Engine, essentiel communication matériel",
                "GPU drivers: GeForce Experience (NVIDIA), Adrenalin (AMD), DSA (Intel)",
                "Game Ready vs Studio drivers (NVIDIA): Game = derniers jeux, Studio = stabilité créa",
                "Clean installation GPU: Cochez pendant install, supprime anciens résidus",
                "DDU (Display Driver Uninstaller): Mode sans échec, désinstallation GPU complète propre",
                "Pilote GPU bêta: Gains perfs day-one jeux mais risque instabilité crashes",
                "Rollback driver: Gestionnaire périphériques > Propriétés > Pilote > Version précédente",
                "Audio Realtek: Site Realtek ou carte mère, bugs fréquents avec Windows Update",
                "Nahimic/Sonic Studio: Logiciels audio CM, peuvent causer grésillements désactivez test",
                "LAN drivers: Intel meilleur que Realtek stabilité gaming, site Intel ou CM",
                "WiFi drivers: Intel WiFi 6/6E excellent, Realtek/MediaTek site fabricant CM",
                "Bluetooth drivers: Souvent bundled WiFi, update ensemble même package",
                "USB drivers: Chipset inclut, séparé si USB 3.1 Gen2/Thunderbolt (ASMedia)",
                "VGA/HDMI audio driver: Séparé GPU driver si son via câble vidéo vers moniteur",
                "Microsoft Basic Display Adapter: GPU driver manquant, installez driver constructeur",
                "Code 43 GPU: Driver corrompu, DDU puis réinstall propre ou GPU défectueux",
                "Code 10 device: Pilote incompatible ou matériel défaillant, tentez rollback",
                "Windows Update drivers: Auto mais parfois anciens, préférez site fabricant",
                "Driver Booster: Automatise mais bundleware risque, utilisez version portable",
                "Snappy Driver Installer: Open-source alternative DriverBoost, hors ligne possible",
                "Device Manager error codes: Code 1 28 31 37 39 43 52 (Google code spécifique)",
                "Unsigned drivers: Test mode Windows (bcdedit) requis pilotes non signés",
                "Driver signature enforcement disable: F8 boot menu temporaire test driver",
                "Generic drivers suffisent: Clavier/souris basiques marchent sans pilote spécifique",
                "Printer drivers: Windows Update ou site HP/Canon/Epson, driver universel existe",
                "Scanner drivers: TWAIN/WIA protocoles, vérifiez compatibilité Windows 10/11",
                "Webcam drivers: Souvent plug-and-play, Logitech G Hub pour options avancées",
                "Game controller drivers: Xbox One native Windows, PS4/5 DS4Windows/DualSenseX",
                "Wacom drivers: Tablettes graphiques, vieux drivers conflits désinstall complet",
                "ASIO drivers: Audio production faible latence (ASIO4ALL gratuit universel)",
                "Peripheral manufacturers: Logitech G Hub, Razer Synapse, Corsair iCUE, SteelSeries GG",
                "RGB software conflicts: Désinstallez autres RGB avant installer nouveau (ASUS/MSI/Gigabyte)",
                "Chipset SATA/RAID: Intel RST (Rapid Storage Technology) si RAID configuré BIOS",
                "NVMe drivers: Windows 10/11 inclut natif, Samsung NVMe driver optionnel marginal gain",
                "Monitor drivers: .inf fichier couleurs précises, site fabricant rarement critique",
                "HID-compliant devices: Human Interface Devices generic, laissez Windows gérer"
            ],
            "peripheriques": [
                "USB 2.0 vs 3.0 vs 3.1 vs 3.2: 480Mbps / 5Gbps / 10Gbps / 20Gbps vitesses",
                "USB-C: Connecteur réversible, peut être USB 2.0, 3.0, Thunderbolt selon implémentation",
                "Thunderbolt 3/4: 40Gbps, connecteur USB-C, supporte GPU externe eGPU, moniteurs 4K double",
                "USB hub: 7 ports max par hub, alimentation externe requis périphériques gourmands",
                "Clavier mécanique switches: Cherry MX Red=linéaire gaming, Brown=tactile mixte, Blue=clicky typing",
                "Polling rate souris: 125/250/500/1000Hz, 1000Hz = 1ms réponse gaming optimal",
                "DPI souris: 800-1600 DPI professionnels gaming, 16000+ DPI marketing inutile",
                "Souris optique vs laser: Optique meilleur gaming précision, Laser fonctionne toutes surfaces",
                "Mousepad: Tissu=contrôle précision, Hard=vitesse glisse, taille XL recommandé FPS",
                "Écran IPS vs TN vs VA: IPS=couleurs angles, TN=réponse rapide gaming, VA=contraste HDR",
                "Temps réponse moniteur: 1ms=idéal, 4ms=acceptable, 5ms+=ghosting visible gaming",
                "Ghosting vs motion blur: Ghosting=traînées physiques, Blur=effet logiciel désactivable",
                "Overdrive monitor: Réduit ghosting mais trop élevé=inverse ghosting, testez réglages",
                "G-Sync vs FreeSync: NVIDIA vs AMD VRR éliminent tearing, G-Sync fonctionne écrans FreeSync",
                "DisplayPort vs HDMI: DP=meilleur bande passante gaming 144Hz+, HDMI 2.1 équivalent récent",
                "Câble DP certified: Vérifiez VESA certified sinon problèmes 144Hz instabilité",
                "KVM switch: Partage clavier/souris/écran multi-PC, USB+Vidéo switcher bouton",
                "Webcam 1080p@30fps vs 60fps: 30fps suffisant visio, 60fps streaming fluide mouvement",
                "Microphone USB vs XLR: USB=pratique plug-and-play, XLR=qualité pro interface audio requis",
                "Phantom power +48V: Requis microphones à condensateur XLR, fourni interface/mixeur",
                "Casque gaming vs audiophile: Gaming=micro intégré virtuel surround, Audiophile=qualité pure",
                "Impédance casque: 32Ω=plug direct, 80Ω+=ampli casque recommandé puissance suffisante",
                "DAC (Digital Analog Converter): Améliore qualité audio vs carte son intégrée, audiophiles",
                "Amplificateur casque: Requis casques haute impédance 250Ω+, Schiit Modi Magni populaire",
                "Imprimante laser vs jet d'encre: Laser=texte rapide économique, Jet=photos couleur qualité",
                "Scanner à plat vs alimenté: Plat=livres fragiles, Alimenté=documents multi-pages rapide",
                "Tablette graphique: Wacom référence pro, XP-Pen/Huion budget correct, sensibilité pression",
                "Manette Xbox vs PS: Xbox native Windows meilleur compatibilité, PS5 DualSense DS4Windows",
                "HOTAS: Hands On Throttle And Stick simulateurs vol (Flight Sim, DCS, Elite Dangerous)",
                "Volant sim racing: Force feedback requis immersion (Logitech G29/G923, Thrustmaster)",
                "Pédalier: Load cell frein = précision freinage vs pédalier ressort basique",
                "Stream Deck: Macros touches programmables streaming/productivité Elgato populaire",
                "Capteur cardiaque: Chest strap=précis, Bracelet=pratique, requis Bluetooth/ANT+",
                "UPS (onduleur): Batterie backup coupure courant, protège données corruption shutdown propre",
                "Parasurtenseur: Protège équipement surtensions électriques, joules élevé meilleur",
                "Switch réseau: Gigabit minimum 2024, 2.5GbE émerge, managed=contrôle avancé",
                "NAS: Network Attached Storage Synology/QNAP, RAID backup automatique famille",
                "eGPU: GPU externe Thunderbolt 3 laptop gaming, perte 15-30% perfs vs interne",
                "Docking station: Multi-ports USB/HDMI/Ethernet expansion laptop, Thunderbolt meilleur",
                "Adaptateurs: HDMI→DP/DVI/VGA, USB-C→USB-A, vérifiez direction conversion et spécifications"
            ],
            "video_audio": [
                "Codec vidéo H.264 vs H.265/HEVC: H.265 moitié taille même qualité mais encoding lent",
                "AV1 codec: Futur compression vidéo, meilleur H.265 mais support limité 2024",
                "Bitrate vidéo: 8-15Mbps 1080p, 20-40Mbps 1440p, 50-100Mbps 4K qualité",
                "CBR vs VBR: Constant BitRate streaming, Variable BitRate fichiers qualité optimale",
                "Résolution vs bitrate: 4K bas bitrate < 1080p haut bitrate qualité perceptuelle",
                "Frame rate: 24fps cinéma, 30fps standard, 60fps fluide gaming, 120fps+ overkill",
                "GOP (Group of Pictures): Keyframe interval, 2 secondes streaming optimal",
                "I-frame B-frame P-frame: Keyframe vs predicted, affecte compression et seeking",
                "Conteneurs: MP4=universel, MKV=features, AVI=ancien, MOV=Apple",
                "Upscaling vs native: 1080p upscalé 4K < native 4K mais AI upscale (DLSS) impressionnant",
                "HDR10 vs Dolby Vision: High Dynamic Range, Dolby Vision métadonnées dynamiques meilleur",
                "Color grading: LUTs (Look-Up Tables) ajustent couleurs cinématique DaVinci Resolve",
                "Chroma subsampling: 4:4:4=full color, 4:2:2=streaming, 4:2:0=YouTube acceptable",
                "Color space: Rec.709=SDR, Rec.2020=HDR, sRGB=web, DCI-P3=cinéma Apple",
                "Bit depth: 8-bit=16M couleurs, 10-bit=1B couleurs banding réduit HDR",
                "GPU encoding: NVENC (NVIDIA), VCE/AMF (AMD), QuickSync (Intel) rapide qualité correcte",
                "Software encoding x264/x265: Lent mais meilleure qualité vs hardware même bitrate",
                "Two-pass encoding: Premier passe analyse, deuxième encode = qualité optimale",
                "OBS Studio paramètres: Rate control CQP/CBR/VBR, Encoder NVENC > x264 si GPU",
                "OBS filters: Gain audio, Noise Gate, Compressor, Gate améliore micro qualité",
                "Render timeline: Proxies 720p fluidifie editing 4K machines faibles",
                "Vidéo editing GPU acceleration: CUDA (NV), OpenCL (AMD), Quick Sync (Intel) requis",
                "Lossless formats: ProRes, DNxHR editing intermédiaire avant export final",
                "HandBrake: Compresse vidéos énormes, presets intelligents, H.265 économise espace",
                "Audio codec AAC vs MP3 vs FLAC: AAC meilleur 128kbps+, MP3 compatible, FLAC lossless",
                "Sample rate: 44.1kHz CD qualité suffisant, 48kHz vidéo standard, 96kHz+ overkill",
                "Bit depth audio: 16-bit suffisant, 24-bit recording dynamique élevée, 32-bit float pro",
                "Audio interface: USB Focusrite Scarlett populaire home studio, XLR entrées",
                "Monitoring speakers: Plates neutres mixage (KRK, Yamaha HS), placement crucial",
                "Room treatment: Panneaux acoustiques réduisent réflexions critical points murs",
                "Microphone patterns: Cardioid=devant, Figure-8=avant/arrière, Omnidirectional=360°",
                "Dynamic vs Condenser mics: Dynamic=live résistant, Condenser=studio sensible détail",
                "Pop filter: Réduit plosives P/B/T sibilance S, obligatoire voix condenser",
                "Phantom power: Requis condensateurs +48V, n'envoyez JAMAIS dynamic mic risque",
                "Gain staging: Niveaux optimaux évite clipping distortion et bruit plancher",
                "Normalization audio: -14 LUFS streaming, -16 LUFS podcast, -23 LUFS broadcast",
                "Compression audio: Réduit dynamique range volume constant écoute confortable",
                "EQ (Equalizer): Coupe fréquences indésirables, boost présence, surgical vs musical",
                "De-esser: Réduit sibilance harsh S voix, compresseur multibande focalisé 5-8kHz",
                "Reverb: Ajoute ambiance espace, plate=voix, hall=orchestre, room=naturel",
                "Delay: Écho temporisé créatif, slapback court ou long ambient atmosphérique"
            ],
            "impression": [
                "Résolution impression: 300 DPI minimum photos qualité, 600 DPI texte net",
                "Laser vs Inkjet coût page: Laser 2-5cts/page, Inkjet 10-20cts/page long terme",
                "Imprimante laser monochrome: Meilleur rapport bureau texte documents volume",
                "Tank ink printers: Epson EcoTank, Canon MegaTank, réservoirs rechargeables économiques",
                "Cartouches originales vs compatibles: Originales fiables, Compatibles 50% moins cher risque",
                "Cartouches XL/XXL: Coût par page inférieur, rentable si impression fréquente",
                "Mode brouillon: Économise encre texte interne qualité réduite acceptable",
                "Recto-verso automatique: Économise papier, duplex matériel vs logiciel",
                "ADF (Automatic Document Feeder): Scan/copie multi-pages automatique essentiel bureau",
                "Bourrage papier: Retirez délicatement sans forcer, nettoyez rouleaux alcool",
                "Rouleaux pickup usés: Remplaçables 20-30€, cause bourrages fréquents",
                "Alignement têtes: Utilitaire imprimante calibre buses qualité optimale couleurs",
                "Nettoyage têtes: Fonction maintenance gaspille encre mais débouche buses sèches",
                "Têtes d'impression séchées: Inkjet non utilisé 1 mois+ risque, imprimez hebdomadaire",
                "Cartouches contrefaites: Puces resetters existent mais garantie annulée risque qualité",
                "Papier grammage: 80g/m² standard, 90-100g/m² rapports, 200g/m² photo brillant",
                "Papier photo: Glossy brillant vs Matte mat, RC (Resin Coated) séchage rapide",
                "Impression sans bordure: Active zone d'impression complète photos A4/A5",
                "Profils couleur: ICC profiles écran calibré → imprimante couleurs fidèles",
                "CMYK vs RGB: Imprimantes CMYK, écrans RGB, conversion affecte couleurs",
                "Impression A3: Coût élevé machine, besoin spécifique posters affiches plans",
                "Sublimation: Transfert chaleur textile polyester mugs, durable",
                "Traceur/Plotter: Impression grand format A0+ plans architecte ingénierie",
                "Pilote PCL vs PostScript: PCL Windows, PostScript Mac/Linux professionnels",
                "AirPrint: Impression iPhone/iPad sans pilote, HP/Canon/Epson support natif",
                "Google Cloud Print: Déprécié 2020, alternatives HP Smart, Epson Connect",
                "Print Spooler service: Windows service gère queue, restart si blocages",
                "Queue impression bloquée: Services.msc > Print Spooler Stop > Vider C:\\Windows\\System32\\spool > Start",
                "Network printer setup: IP statique recommandé vs DHCP évite perte connexion",
                "Shared printer: PC hôte doit être allumé, firewall exceptions requises",
                "Driver universal print: PCL6/PS universel fonctionne imprimantes diverses marques",
                "Erreur Out of Memory: Imprimante RAM insuffisante image complexe, réduisez résolution",
                "Code erreur 0x00000709: Corruption registry printer, supprimez clés registre clean",
                "Toner vs Ink: Toner poudre laser fusion chaleur, Ink liquide inkjet",
                "Tambour laser: Photorécepteur 10-50k pages remplacement drum séparé toner",
                "Unité de fusion: Four laser fixe toner papier, 50-100k pages remplacement",
                "Maintenance kit laser: Rouleaux + fusion + pad, prolonge vie imprimante professionnelle",
                "Scan to PDF: Réglages compression optimale taille fichier vs qualité lisibilité",
                "OCR (Optical Character Recognition): Convertit scan PDF éditable texte recherchable",
                "Scan résolution: 150 DPI texte OCR, 300 DPI photos documents, 600 DPI archives"
            ],
            "cloud": [
                "Stockage cloud gratuit: Google Drive 15GB, OneDrive 5GB, Mega 20GB, pCloud 10GB",
                "Dropbox: 2GB gratuit synchronisation multi-devices simple mais limité",
                "Google Drive: Intégration Gmail Docs Sheets, backup photos Google Photos inclus",
                "OneDrive: Natif Windows 10/11, Microsoft 365 inclut 1TB économique",
                "iCloud: Apple écosystème 5GB gratuit, 50GB/200GB/2TB payant seamless iOS",
                "Mega: 20GB gratuit chiffré end-to-end privacy focus Nouvelle-Zélande",
                "pCloud: Crypto optionnel client-side, lifetime plans achat unique vs abonnement",
                "Sync.com: Chiffré zero-knowledge Canada 5GB gratuit privacy respecté",
                "Nextcloud: Self-hosted open-source, contrôle total données NAS Raspberry Pi",
                "Synology Cloud: NAS Synology synchronisation automatique hybride local + cloud",
                "Sauvegarde vs Sync: Backup = historique versions, Sync = copie identique temps réel",
                "Versioning: Garde anciennes versions fichier récupère changements accidentels",
                "Partage fichiers: Liens partage publics vs privés, expiration mot de passe",
                "Collaboration: Google Docs temps réel vs Office 365 coédition concurrente",
                "Desktop sync apps: Synchronisation locale automatique upload download folders",
                "Bandwidth upload: Limite FAI upload lent (5-10Mbps ADSL vs 20-50Mbps fibre)",
                "Sync conflicts: Modifications simultanées créent doublons conflicted copy résoudre manuellement",
                "Selective sync: Choix dossiers synchronisés localement économise espace disque",
                "Placeholder files: Icônes cloud téléchargement à la demande (OneDrive Files On-Demand)",
                "Encryption transit: HTTPS TLS chiffre transfert vs stockage encryption at-rest",
                "Zero-knowledge encryption: Serveur ne connaît pas mot de passe Mega Sync pCloud Crypto",
                "Client-side encryption: Boxcryptor Cryptomator chiffre avant upload compatible tous clouds",
                "GDPR compliance: Données EU stockage localisation juridiction privacy réglementations",
                "Business plans: Stockage illimité équipes gestion admin controls compliance audit",
                "Family plans: Partage stockage 5-6 membres économique vs plans individuels",
                "Backup strategy 3-2-1: 3 copies 2 médias différents 1 offsite cloud rôle offsite",
                "Incremental backup cloud: Synchronise seulement changements delta économise bande passante",
                "Block-level sync: Détecte blocs modifiés fichiers large rapide Dropbox technique",
                "LAN sync: Synchronisation locale réseau rapide avant cloud (Dropbox Resilio Sync)",
                "Cloud gaming: GeForce NOW, Xbox Cloud Gaming, streaming jeux cloud latence dépendant",
                "Cloud storage providers comparison: Prix/GB, bande passante, features, juridiction, privacy",
                "Hybrid cloud NAS: Synology C2 QNAP backup local rapide cloud offsite sécurité",
                "Photo backup: Google Photos illimité compressé vs original iCloud Amazon Photos",
                "Enterprise cloud: AWS S3, Azure Blob, Google Cloud Storage glacier archival froid",
                "Object storage: S3-compatible MinIO alternatives self-hosted compatible applications"
            ],
            "virtualisation": [
                "VirtualBox: Oracle gratuit open-source Windows Mac Linux VMs, extensions guest additions",
                "VMware Workstation: Payant professionnel performances meilleures snapshots clones",
                "VMware Player: Gratuit usage personnel fonctionnalités limitées vs Workstation Pro",
                "Hyper-V: Microsoft intégré Windows 10/11 Pro natif performances Windows VMs",
                "QEMU/KVM: Linux hypervisor open-source performances natives passthrough GPU",
                "Proxmox: Distribution Linux hypervisor web interface gestion VMs containers",
                "VirtualBox vs VMware: VBox gratuit basique, VMware perfs snapshots réseau avancé",
                "Type 1 vs Type 2 hypervisor: Type 1 bare-metal serveurs, Type 2 desktop app",
                "Guest Additions: Pilotes optimisés résolution dynamique clipboard partagé performances",
                "VM RAM allocation: 4GB minimum Windows 10, 8GB confortable, 16GB multitâche",
                "CPU cores VM: 2 cores minimum, 4 cores confortable, ne pas allouer 100% hôte",
                "Dynamic disk vs Fixed: Dynamique grandit besoin, Fixed préalloué performances meilleures",
                "Snapshots: Sauvegardes état VM instantanées restauration rapide tests logiciels",
                "Clones: Copie complète VM linked=espace économisé full=indépendante portable",
                "Shared folders: Accès fichiers hôte depuis guest pratique transferts bidirectionnels",
                "NAT vs Bridged network: NAT VM internet via hôte, Bridged VM IP propre réseau",
                "Host-only network: Isolé VMs communiquent entre elles et hôte pas internet",
                "GPU passthrough: PCIe passthrough GPU physique vers VM gaming performances natives",
                "USB passthrough: Rediriger USB périphériques hôte vers VM transparent",
                "Nested virtualization: VM dans VM, Intel VT-x AMD-V enabled BIOS requis",
                "Container vs VM: Container partage kernel léger Docker, VM OS complet isolé lourd",
                "Docker: Containerisation applications portables isolées microservices DevOps",
                "Windows Sandbox: VM jetable Windows 10/11 tests logiciels suspects isolation",
                "WSL (Windows Subsystem Linux): Linux kernel Windows terminal Bash Ubuntu natif",
                "WSL2 vs WSL1: WSL2 vraie VM performances meilleures, WSL1 translation layer",
                "macOS VM: Légalement autorisé matériel Apple uniquement, Hackintosh gris",
                "Android VM: Genymotion, BlueStacks, Nox Player, gaming mobile PC performances",
                "Antivirus VM: Requis guest Windows comme physique, hôte antivirus pas suffisant",
                "VM backup: Export OVA/OVF portable import autres hypervisors migration facile",
                "Live migration: Déplacer VM running entre hôtes zéro downtime Proxmox VMware",
                "Resource allocation: Overcommit RAM CPU partage ressources hôte multiples VMs",
                "IOMMU groups: Isolation PCIe passthrough, meilleure carte mère separation propre",
                "SR-IOV: Single Root IO Virtualization réseau GPU partagé multiples VMs performances",
                "VM security: Isolation compromission guest pas hôte théorie, exploits existent patches"
            ],
            "linux_dualboot": [
                "Ubuntu: Distribution débutant conviviale LTS support long terme stable entreprise",
                "Linux Mint: Basé Ubuntu interface familière Windows utilisateurs Cinnamon desktop",
                "Pop!_OS: System76 gaming focus NVIDIA drivers auto productivity tiling",
                "Fedora: Red Hat bleeding edge technologies Workstation GNOME excellent laptops",
                "Arch Linux: Rolling release personnalisable total avancé documentation wiki excellente",
                "Manjaro: Arch convivial graphique installation AUR accès packages bleeding edge",
                "Debian: Stable ultra serveurs base Ubuntu conservateur testé fiable",
                "EndeavourOS: Arch graphique simple proche vanilla terminal friendly communauté",
                "Dual boot partition: 50-100GB Linux suffisant, séparé /home partition données persistent",
                "Bootloader GRUB: Gère multi-boot choix OS démarrage timeout personnalisable",
                "Windows dual boot: Installer Windows PREMIER puis Linux évite GRUB écrasé",
                "Secure Boot Linux: Ubuntu Fedora Mint signés fonctionnent, Arch Manjaro désactivez",
                "Partitioning scheme: / root 30GB, /home reste, swap 8GB si <16GB RAM",
                "ext4 vs Btrfs vs XFS: ext4 stable standard, Btrfs snapshots moderne, XFS serveurs",
                "Mount Windows partition Linux: NTFS lecture écriture ntfs-3g automatique browse fichiers",
                "GRUB customization: Timeout, résolution, thème GRUB Customizer GUI configuration",
                "Windows Update broke GRUB: Boot Repair USB ISO répare bootloader automatique",
                "Time sync dual boot: Linux UTC Windows local time désync, timedatectl local-rtc fix",
                "Gaming Linux: Proton Steam Lutris Wine compatibilité Windows jeux 70-90% fonctionnent",
                "Proton versions: Experimental derniers jeux, GE-Proton community patches performances",
                "Vulkan vs OpenGL: Vulkan moderne performances DirectX 12 équivalent requis récents GPU",
                "DXVK: DirectX Vulkan translation layer améliore perfs jeux Windows sous Linux",
                "Anti-cheat Linux: EAC BattlEye support limité Valorant LoL non fonctionnels 2024",
                "NVIDIA Linux: Drivers propriétaires requis performances, Nouveau open-source limité",
                "AMD Linux: Open-source AMDGPU excellent natif kernel plug-and-play support",
                "Wayland vs X11: Wayland moderne sécurisé GNOME default, X11 compatible legacy apps",
                "Desktop environments: GNOME moderne, KDE Plasma features, XFCE léger, Cinnamon familier",
                "Package managers: APT (Debian/Ubuntu), DNF (Fedora), Pacman (Arch), universal Flatpak Snap",
                "Terminal basics: ls cd mkdir rm cp mv chmod navigation commandes essentielles",
                "Sudo vs root: Sudo élévation temporaire sécurisé, root login permanent dangereux évitez",
                "File permissions: rwx owner group others 755 644 chmod chown gestion accès",
                "Bash scripting: Automation tasks .sh scripts conditions loops variables puissant",
                "System logs: journalctl dmesg /var/log debug problèmes kernel applications services",
                "Wine: Windows applications Linux compatibilité variable Office anciens jeux programmes",
                "Windows VM Linux: VirtualBox VMware Windows guest Linux hôte performances correctes",
                "Dual boot time: Garde Windows jeux triple-A anticheat, Linux productivité development"
            ],
            "overclocking_advanced": [
                "Silicon lottery: Chaque CPU unique, 5.0GHz stable vs 4.8GHz même modèle chance",
                "Binning: Fabricants testent chips meilleurs vendus SKU supérieur (i9 vs i5)",
                "Golden sample: Chip exceptionnel overclocks hauts voltages bas gagnant lottery",
                "Voltage scaling: Augmenter fréquence requiert plus voltage équilibre stabilité chaleur",
                "VCore: Voltage cœurs CPU, modification principale OC 1.25-1.40V typique limite",
                "LLC (Load Line Calibration): Compense Vdroop maintient voltage sous charge niveaux",
                "AVX offset: Réduit fréquence instructions AVX intensives évite instabilité crash",
                "Ring/Cache ratio: Fréquence cache CPU uncore, lie ratio core latence mémoire",
                "Memory overclocking: XMP profile départ, manuel timings voltage advanced Ryzen aime",
                "RAM timings: CAS Latency CL principal, tRCD tRP tRAS secondaires serrés = latence",
                "RAM voltage: 1.35V XMP safe, 1.40-1.45V OC manuel, 1.50V+ risque dégradation",
                "VCCSA VCCIO: Voltages IMC Intel contrôleur mémoire stabilité RAM overclocks élevés",
                "SOC voltage: AMD Ryzen contrôleur mémoire Infinity Fabric OC RAM 3600MHz+ booster",
                "FCLK Infinity Fabric: Fréquence interconnect Ryzen égale moitié RAM optimal 1800MHz=3600",
                "Gear mode Intel: Gear 1 = IMC=RAM rapide, Gear 2 = moitié latence mais DDR5",
                "Stability testing: Prime95 Small FFTs CPU, Large FFTs RAM, Blend mixte 8-24h",
                "OCCT: Stress test CPU GPU PSU détection erreurs Whea Logger monitore stability",
                "Linpack Xtreme: Stress AVX intense températures maximales réaliste charge lourde",
                "Y-Cruncher: Calcul Pi stress RAM fréquences timings erreurs instabilité mathématique",
                "Karhu RAM Test: Payant excellent RAM OC validation rapide erreurs subtiles détection",
                "MemTest86: Bootable USB test RAM nuit complet 0 erreur requis stable",
                "TM5 Anta777: Windows RAM test extrême configuration erreurs cachées révèle",
                "Stress test temps: 1h basique, 8h confiant, 24h garanti stable production usage",
                "WHEA errors: Windows Hardware Error Architecture logs Event Viewer instabilité cache",
                "HWiNFO64 sensors: Monitore VCore températures WHEA temps réel critical overclocking",
                "Temperature monitoring: Tctl/Tdie AMD, Package/Core Intel, Hotspot GPU VRAM",
                "Thermal throttling: CPU GPU réduit fréquences > Tjunction Max protéger matériel",
                "Power limits: PL1 PL2 Intel, PPT TDC EDC AMD, motherboard imposée enlever limites",
                "Motherboard VRM: Voltage Regulator Module phases qualité crucial OC stable chaleur",
                "VRM cooling: Dissipateurs heatsinks MOSFETs phases fan airflow directed important",
                "Delid CPU: Retirer IHS changer TIM liquid metal -15-20°C RISQUE garantie",
                "Liquid metal: Conducteur électrique Conductonaut Thermal Grizzly précautions short circuit",
                "Direct die cooling: Refroidissement direct die sans IHS extrême températures danger",
                "Curve Optimizer AMD: Per-core undervolting PBO2 Ryzen 5000+ efficacité températures",
                "PBO (Precision Boost Overdrive): AMD auto-overclock intelligent limites power températures",
                "Auto OC: AMD PBO Intel Turbo Boost automatique safe sans knowledge manuel",
                "LN2 overclocking: Azote liquide -196°C records monde extrême compétition validation"
            ],
            "powershell_avance": [
                "Get-Process: Liste processus running détails PID CPU mémoire utilisée",
                "Stop-Process -Name: Tuer processus nom spécifique force si nécessaire",
                "Get-Service: Affiche services Windows statut running stopped disabled",
                "Start-Service / Stop-Service: Démarrer arrêter services spécifiques",
                "Get-EventLog -LogName System: Consulter logs événements système errors warnings",
                "Get-WmiObject Win32_: Requêtes WMI info matériel BIOS disques processus",
                "Get-HotFix: Liste mises jour Windows installées KB numbers dates",
                "Test-NetConnection: Ping avancé traceroute test port TCP",
                "Get-NetAdapter: Informations cartes réseau vitesse statut MAC address",
                "Resolve-DnsName: Query DNS lookup serveurs alternatifs troubleshooting",
                "Get-ComputerInfo: Informations complètes système OS hardware BIOS",
                "Get-PhysicalDisk: État disques physiques SMART santé SSD HDD",
                "Clear-RecycleBin -Force: Vider corbeille toutes partitions sans confirmation",
                "Get-ChildItem -Recurse: Liste fichiers récursive taille recherche patterns",
                "Get-FileHash -Algorithm SHA256: Calculer hash fichier intégrité vérification",
                "Measure-Object -Sum: Calculer taille totale dossiers statistiques fichiers",
                "Export-Csv / Import-Csv: Exporter importer données tableaux CSV",
                "ConvertTo-Json / ConvertFrom-Json: Manipulation données JSON APIs",
                "Invoke-WebRequest: Télécharger fichiers scraping web HTTP requests",
                "Start-Job: Exécuter commandes background asynchrone parallèle",
                "Checkpoint-Computer: Créer point restauration système avant modifications",
                "Get-AppxPackage: Lister apps Windows Store UWP désinstaller bloatware",
                "Remove-AppxPackage: Supprimer apps préinstallées Windows 10/11",
                "Set-ExecutionPolicy RemoteSigned: Autoriser scripts PowerShell signés locaux",
                "Get-Acl / Set-Acl: Gérer permissions NTFS fichiers dossiers sécurité",
                "Take-Ownership: Prendre possession fichiers systèmes bloqués admin",
                "New-ScheduledTask: Créer tâches planifiées automatisation scripts",
                "Get-WindowsOptionalFeature: Lister features Windows activer désactiver",
                "Enable-WindowsOptionalFeature -Online: Activer Hyper-V WSL Sandbox",
                "Get-Volume: Informations volumes disques espace libre santé",
                "Optimize-Volume: Défragmentation TRIM SSD optimisation automatique",
                "Get-PnpDevice: Liste périphériques Plug and Play pilotes statut",
                "Update-Help: Télécharger aide PowerShell cmdlets offline documentation"
            ],
            "registry_tweaks": [
                "HKLM vs HKCU: Local Machine tous users vs Current User utilisateur actuel",
                "Regedit: Éditeur registre graphique recherche export import clés",
                "reg export / import: Sauvegarder restaurer clés registre fichier .reg",
                "Point restauration avant modif registre: Sécurité rollback si problème",
                "Désactiver télémétrie: DiagTrack service AllowTelemetry 0 vie privée",
                "Explorer compact view: Réduire espacement fichiers classique dense",
                "Show hidden files: Hidden 1 ShowSuperHidden 1 voir fichiers système",
                "Disable UAC prompts: ConsentPromptBehaviorAdmin 0 risque sécurité",
                "Disable lock screen: NoLockScreen 1 boot direct sans écran verrouillage",
                "Old context menu Win11: {86ca1aa0-34aa-4e8b-a509-50c905bae2a2} restaure",
                "Disable Windows Update: Start 4 service wuauserv déconseillé sécurité",
                "Disable hibernation: HibernateEnabled 0 libère espace disque Go",
                "Disable fast startup: HiberBootEnabled 0 boot propre pas hybrid",
                "Taskbar tweaks: TaskbarSmallIcons taille barre tâches position",
                "Remove OneDrive: Uninstall système clé registre désactivation totale",
                "Classic Alt+Tab: AltTabSettings vue classique fenêtres pas aperçu",
                "Disable Cortana: AllowCortana 0 économise ressources vie privée",
                "Disable Game DVR: AllowGameDVR 0 pas enregistrement performances gaming",
                "Show file extensions: HideFileExt 0 sécurité voir vrais types fichiers",
                "Disable ads Start: ContentDeliveryAllowed 0 suggestions publicités",
                "Windows Photo Viewer: Restaurer visionneuse classique vs app Photos",
                "Disable Bing Search: BingSearchEnabled 0 recherche locale uniquement",
                "NumLock on startup: InitialKeyboardIndicators 2 pavé numérique activé",
                "Disable animations: MinAnimate 0 interface immédiate performance",
                "Classic logon screen: Utilisateur liste dernière session options",
                "Network throttling: Désactiver NetworkThrottlingIndex 4294967295 streaming",
                "Disable PeerToPeer Windows Update: DoDownloadMode 0 économise bande passante",
                "Services background: Adjust BackgroundAccessApplications limiter apps",
                "Reserved storage: Disable 0 Windows 10 récupère 7GB espace réservé",
                "Verbose status messages: Boot shutdown affiche opérations détaillées debug"
            ],
            "backup_recovery": [
                "Règle 3-2-1: 3 copies 2 supports différents 1 hors site protection maximale",
                "Windows Backup: Image système sauvegarde complète restauration totale",
                "File History: Sauvegarde incrémentale fichiers personnels versions précédentes",
                "System Image: Copie exacte disque OS apps settings restauration rapide",
                "Point restauration: Rollback Windows modifications pilotes installations",
                "Veeam Agent: Backup gratuit professionnel images complètes incrémentielles",
                "Macrium Reflect: Clonage disque imaging backup restauration bootable",
                "Acronis True Image: Suite backup complète payante ransomware protection",
                "Clonezilla: Open-source clonage disque partitions déploiement réseau",
                "Rescuezilla: Clonezilla GUI convivial graphique accessible débutants",
                "EaseUS Todo Backup: Gratuit clonage migration SSD sauvegarde planifiée",
                "AOMEI Backupper: Backup clonage sync gratuit interface intuitive",
                "BackBlaze: Cloud backup illimité automatique 7$/mois restauration mondiale",
                "Crashplan: Backup cloud PME versionning fichiers rétention longue",
                "Duplicati: Open-source backup chiffré cloud multiple destinations gratuit",
                "Syncthing: Synchronisation P2P décentralisée multi-devices open-source",
                "FreeFileSync: Sync bidirectionnel miroir fichiers dossiers comparaison",
                "Robocopy: Windows built-in copie miroir incrémentielle scripts batch",
                "7-Zip: Compression archives backup password protection AES-256",
                "WinRAR: Archives RAR compression élevée recovery volumes réparation",
                "Cloud services: OneDrive Google Drive Dropbox sync automatique 15GB gratuit",
                "Version control: Git backup code source historique branches collaboration",
                "NAS backup: Network Attached Storage RAID redundancy accessible réseau",
                "External HDD: USB backup physique 2-4TB économique déconnecté ransomware",
                "Bootable USB recovery: Windows installation media réparation démarrage",
                "WinPE: Windows Preinstallation Environment boot rescue custom tools",
                "Hiren's BootCD: Suite outils rescue partitionnement antivirus recovery",
                "SystemRescue: Linux rescue distribution tools backup partitions data recovery",
                "TestDisk PhotoRec: Récupération partitions perdues fichiers supprimés gratuit",
                "Recuva: Récupération fichiers supprimés vidés corbeille Piriform",
                "R-Studio: Professionnel recovery données RAID reconstruction disque endommagé",
                "EaseUS Data Recovery: Assistant récupération graphique 2GB gratuit",
                "DMDE: Disk Editor récupération puissant gratuit partitions fichiers",
                "GetDataBack: Recovery NTFS FAT exFAT disques formatés supprimés",
                "OnTrack EasyRecovery: Professionnel enterprise niveau recovery service",
                "Shadow copies: VSS Volume Shadow Copy snapshots précédents fichiers",
                "Restore from shadow: ShadowExplorer accès copies ombres gratuitement",
                "DBAN: Darik's Boot And Nuke effacement sécurisé disque avant vente",
                "Eraser: Suppression sécurisée fichiers multiples passes DoD standards"
            ],
            "remote_support": [
                "TeamViewer: Remote desktop support populaire gratuit usage personnel",
                "AnyDesk: Alternative TeamViewer rapide léger faible latence",
                "Chrome Remote Desktop: Google gratuit multi-plateforme navigateur",
                "Windows RDP: Built-in Remote Desktop Protocol Pro Enterprise uniquement",
                "VNC (RealVNC, TightVNC): Open-source cross-platform remote control",
                "Parsec: Gaming remote play faible latence 60FPS 4K streaming",
                "Moonlight: NVIDIA GameStream client streaming jeux PC vers devices",
                "Splashtop: Business remote support rapide performances annotations",
                "LogMeIn: Professionnel entreprise remote IT management onéreux",
                "GoToMyPC: Citrix remote access business sécurisé compliance",
                "Zoho Assist: Remote support MSP ticketing intégration helpdesk",
                "ScreenConnect: ConnectWise control MSP remote monitoring management",
                "RustDesk: Open-source self-hosted alternative TeamViewer gratuit",
                "Ammyy Admin: Sans installation quick support léger urgences",
                "UltraVNC: Open-source VNC encryption file transfer chat",
                "NoMachine: Remote desktop NX protocol Linux Windows macOS",
                "SSH: Secure Shell Linux remote terminal encrypted secure",
                "PuTTY: Windows SSH client terminal Telnet serial connections",
                "WinSCP: Transfert fichiers SFTP SCP graphique scripts",
                "FileZilla: FTP SFTP client transferts fichiers serveurs web",
                "QuickSupport apps: Versions mobiles TeamViewer AnyDesk support",
                "Wake on LAN: Démarrer PC réseau à distance WOL magic packet",
                "Port forwarding: Ouvrir ports routeur RDP VNC SSH accès externe",
                "Dynamic DNS: DDNS NO-IP DuckDNS adresse fixe IP dynamique",
                "VPN remote access: OpenVPN WireGuard accès réseau local sécurisé",
                "Unattended access: Accès permanent sans permission distant",
                "Session recording: Enregistrement sessions support training compliance",
                "File transfer: Glisser-déposer fichiers clipboard copier-coller remote",
                "Multi-monitor: Support écrans multiples remote view all screens",
                "Mobile support: iOS Android apps contrôle PC smartphone tablet"
            ],
            "monitoring_outils": [
                "Task Manager: Ctrl+Shift+Esc performances processus démarrage services",
                "Resource Monitor: Resmon détails CPU RAM disque réseau avancé",
                "Performance Monitor: Perfmon compteurs métriques graphiques logs",
                "Process Explorer: Sysinternals task manager stéroïdes handles threads",
                "Process Monitor: Procmon activité temps réel fichiers registre réseau",
                "Autoruns: Sysinternals tout démarre Windows services drivers tâches",
                "TCPView: Sysinternals connexions réseau TCP UDP endpoints actifs",
                "HWiNFO64: Monitoring hardware complet sensors temperatures logs",
                "HWMonitor: CPUID températures voltages fans GPU CPU real-time",
                "MSI Afterburner: GPU monitoring OSD in-game FPS stats overlay",
                "RivaTuner: OSD overlay FPS frametime limiteur advanced monitoring",
                "NZXT CAM: Monitoring software RGB control all-in-one interface",
                "Corsair iCUE: Monitoring RGB synchronisation Corsair périphériques",
                "Argus Monitor: SMART disques fans control curves alertes température",
                "SpeedFan: Fans control curves automatique température based vintage",
                "Open Hardware Monitor: Open-source monitoring gratuit sensors all",
                "Libre Hardware Monitor: Fork open hardware updated active",
                "AIDA64: Suite diagnostic benchmark monitoring sensors reports",
                "HWINFO: Hardware information complète identification composants",
                "CPU-Z: Info CPU détaillée clocks voltages cache architecture",
                "GPU-Z: Détails GPU VRAM clocks température sensors logs",
                "CrystalDiskInfo: SMART disques santé température alerte prédiction",
                "CrystalDiskMark: Benchmark vitesse lecture écriture disques séquentiel",
                "HDTune: Test disque erreurs santé scan benchmark informations",
                "HD Sentinel: Monitoring santé disques prédiction défaillance alerte",
                "GlassWire: Firewall monitoring réseau graphiques apps bandwidth usage",
                "NetLimiter: Monitoring et limitation bandwidth par application",
                "BitMeter OS: Bandwidth monitor graphiques quotas historique",
                "NetWorx: Traffic monitoring quotas statistiques vitesse tests",
                "Event Viewer: Eventvwr.msc logs système applications sécurité errors",
                "Reliability Monitor: Perfmon /rel historique fiabilité crashes",
                "Windows Admin Center: Gestion serveurs monitoring web-based",
                "PRTG: Network monitoring enterprise serveurs switches SNMP",
                "Zabbix: Open-source monitoring infrastructure alertes graphiques",
                "Nagios: Monitoring open-source serveurs services réseau alertes"
            ],
            "automation_scripts": [
                "Task Scheduler: Taskschd.msc automatisation tâches planifiées triggers",
                "PowerShell scripts: Automation .ps1 scheduled tasks admin répétitives",
                "Batch files: .bat .cmd scripts Windows simple automation commands",
                "Windows Sandbox: Test scripts isolated VM jetable sécurisé",
                "AutoHotkey: Macros automation raccourcis clavier hotkeys scripts",
                "Python scripts: Automation puissante cross-platform librairies infinies",
                "Robocopy scripts: Backup automatique mirroring synchronisation planifié",
                "Shutdown scripts: Arrêt automatique planifié conditions backup avant",
                "Startup scripts: GPedit.msc scripts démarrage login automation",
                "Logon scripts: Group Policy exécution automatique session utilisateur",
                "Registry scripts: .reg fichiers déploiement configurations registre mass",
                "MSI packages: Installation silencieuse déploiement apps enterprise",
                "Group Policy: GPO déploiement configurations mass domain Windows",
                "WSUS: Windows Server Update Services déploiement updates centralisé",
                "PDQ Deploy: Software deployment automation push applications silent",
                "PDQ Inventory: Network inventory scanning hardware software reports",
                "Chocolatey: Package manager Windows apps installation CLI automation",
                "Winget: Microsoft package manager built-in Windows 10/11 automation",
                "Scoop: Package manager command-line portable apps automation",
                "Ansible: Infrastructure automation configuration management agentless",
                "Puppet: Configuration management automation infrastructure code",
                "Chef: Infrastructure automation configuration management recipes",
                "SaltStack: Infrastructure automation orchestration event-driven",
                "WinRM: Windows Remote Management PowerShell remote automation",
                "WMI: Windows Management Instrumentation queries automation scripts",
                "COM objects: Component Object Model automation Office Excel Word",
                "VBScript: Legacy automation Windows still works .vbs scripts",
                "JScript: JavaScript Windows scripting host automation legacy",
                "Cron jobs: Linux scheduled tasks automation maintenance scripts",
                "Systemd timers: Linux moderne scheduled automation services",
                "Email alerts: Scripts send emails notifications completion errors",
                "Webhook integration: REST APIs automation trigger actions cloud",
                "IFTTT: If This Then That automation web services trigger actions",
                "Zapier: Business automation workflows apps connections triggers",
                "n8n: Open-source workflow automation self-hosted alternative",
                "Node-RED: Flow-based automation visual programming IoT integration"
            ],
            "refroidissement_thermique": [
                "Air cooling vs Liquid: Air économique fiable, liquide performances silence",
                "AIO (All-In-One): Watercooling fermé simple installation maintenance zéro",
                "Custom loop: Watercooling custom maximal refroidissement complexe cher",
                "Tower coolers: Aircooling tours Noctua Be Quiet Dark Rock excellent",
                "Top-down coolers: Flux vertical refroidit VRM RAM carte mère",
                "Low profile: Coolers bas ITX HTPC cases petits clearance RAM",
                "TDP rating: Thermal Design Power cooler doit supporter TDP CPU minimum",
                "Pâte thermique: Arctic MX-5 Thermal Grizzly Kryonaut application cruciale",
                "Liquid metal: Conductonaut conductivité maximale risque électrique précaution",
                "Thermal pads: VRM VRAM refroidissement silicone conducteur épaisseur précise",
                "Case fans: Intake avant bas, exhaust arrière haut pression positive",
                "Static pressure: Fans radiateurs dissipateurs résistance airflow",
                "Airflow fans: High CFM (Cubic Feet/Minute) cases ouverts flow maximal",
                "PWM vs DC: PWM 4-pin control précis RPM, DC 3-pin voltage control",
                "Fan curves: BIOS courbes vitesse selon température silencieux vs perfs",
                "Positive vs negative pressure: Positive moins poussière, negative airflow",
                "Mesh cases: Airflow maximal poussière accumulation nettoyage fréquent",
                "Tempered glass: Esthétique mais réduit airflow vs mesh panels",
                "Dust filters: Filtres poussière magnetic nettoyage régulier améliore flux",
                "Cable management: Câbles ordonnés améliore airflow températures réduites",
                "GPU sag bracket: Support carte graphique évite stress PCIe sag",
                "GPU deshroud: Retirer shroud ventilateurs case fans meilleure cooling",
                "Undervolt: Réduire voltage maintient performances réduit chaleur consommation",
                "Repaste GPU: Changer pâte thermique GPU -10-15°C garantie annulée",
                "Delid CPU: Retirer IHS changer TIM extreme cooling -20°C risque",
                "Thermal throttling: CPU GPU réduit clocks températures excessives protéger",
                "Tjmax: Température jonction maximale 100-105°C throttling commence",
                "Ambient temperature: Température pièce affecte cooling 18-22°C idéal",
                "Overclocking temperatures: OC augmente chaleur refroidissement crucial stable",
                "Stress testing: Prime95 FurMark températures maximales tester cooling",
                "Idle vs load: Idle 30-40°C, load 60-80°C bon refroidissement",
                "Hot spot temperature: GPU hotspot junction 10-15°C plus chaud edge",
                "VRM cooling: Voltage Regulator Modules dissipateurs airflow crucial OC",
                "Chipset cooling: Passive actif X570 chaud dissipateur requis",
                "M.2 SSD cooling: Heatsinks throttling thermique 2-4GB/s réduit perfs",
                "RAM cooling: Heatsinks décoration mais aide OC extrême dissipation"
            ],
            "alimentation_electrique": [
                "80 Plus certification: Bronze Silver Gold Platinum Titanium efficacité",
                "Wattage calculateur: Outervision PCPartPicker calcul consommation totale",
                "Headroom 20-30%: Overhead marge sécurité upgrades futurs efficacité",
                "Modular PSU: Câbles détachables management propre airflow meilleur",
                "Single rail vs multi-rail: Single simple puissant, multi protections",
                "12V rail: Principal alimentation CPU GPU puissance stable crucial",
                "Ripple suppression: PSU qualité ondulation minimale composants protégés",
                "Hold-up time: Maintient power coupure brève 16ms minimum requis",
                "PSU fan: 120/140mm silence 0db fanless charge basse qualité",
                "Cable management: 24-pin ATX 8-pin CPU 8-pin PCIe modulaires",
                "UPS (Uninterruptible Power Supply): Onduleur coupures surtensions batterie backup",
                "Surge protector: Parasurtenseur protège foudre surtensions multiprise qualité",
                "Line interactive UPS: Régulation voltage automatique AVR batteries backup",
                "Online UPS: Double conversion meilleure protection serveurs équipement sensible",
                "VA vs Watts: Volt-Ampere apparent, Watts réel facteur puissance 0.6-0.8",
                "Runtime: Autonomie batterie UPS dépend charge arrêt propre système",
                "Sine wave: Pure sine wave requis PSU moderne, stepped approx. suffit",
                "UPS software: CyberPower PowerChute monitoring shutdown automatique",
                "Power consumption: Idle 50-100W, gaming 300-500W, workstation 200-350W",
                "Kill-a-Watt: Mesure consommation électrique réelle prise device wattmeter",
                "PSU efficiency curve: Maximum 50-80% load courbe efficacité calculer wattage",
                "Coil whine: Inductances vibrations bruit aigu charge GPU normal",
                "Capacitor aging: Condensateurs dégradation temps PSU 5-10 ans remplacer",
                "Japanese capacitors: Qualité supérieure Nippon Chemicon longévité",
                "PSU tier list: Cultists tier list hiérarchie modèles qualité fiabilité",
                "Warranty: 5-10 ans garantie indicateur qualité confiance fabricant",
                "OCP OVP UVP: Over Current/Voltage/Under Voltage Protection sécurité",
                "SFP OTP OPP: Short Circuit/Over Temperature/Power Protection crucial",
                "PSU testing: Resistive load tester multimètre oscilloscope ripple verify",
                "Cable gauge: AWG 16-18 qualité cuivre OFC résistance pertes minimales",
                "Daisy chain GPU: Éviter deux connecteurs même câble instabilité"
            ],
            "productivite_bureau": [
                "Microsoft Office: Suite bureautique Word Excel PowerPoint professionnelle",
                "LibreOffice: Alternative gratuite open-source compatible formats Office",
                "Google Workspace: Suite cloud collaborative Docs Sheets Slides Drive",
                "OnlyOffice: Bureautique compatible Office collaboration cloud gratuit",
                "Notion: Tout-en-un notes docs wiki databases teams productivity",
                "Obsidian: Note-taking markdown knowledge base linking powerful",
                "Evernote: Prise notes organisation web clipper synchronisation",
                "OneNote: Microsoft notes organisation sections synchronisation gratuit",
                "Joplin: Open-source notes markdown synchronisation cloud chiffré",
                "Trello: Kanban boards gestion projets tasks cartes visuelles",
                "Asana: Gestion projets tasks équipes calendrier dépendances",
                "Monday.com: Work OS gestion projets workflows automation",
                "ClickUp: All-in-one productivity tasks docs goals timesheets",
                "Todoist: Todo list tasks GTD priorités productivité simple",
                "Microsoft To Do: Tasks listes Outlook intégration gratuit",
                "TickTick: Todo calendar Pomodoro habits tracker complet",
                "Toggl Track: Time tracking productivité projets facturation rapports",
                "RescueTime: Automatic time tracking analytics productivity insights",
                "Focus@Will: Musique concentration neuroscience productivity focus",
                "Forest: Pomodoro gamification focus bloquer distractions smartphone",
                "Cold Turkey: Website blocker distractions focus time productivité",
                "Freedom: Multi-device distraction blocker apps sites scheduled",
                "PDF tools: Adobe Acrobat PDF-XChange Foxit edit merge split",
                "Sumatra PDF: Léger rapide lecteur PDF ePub gratuit minimaliste",
                "Calibre: Ebooks management conversion Kindle ePub library organisation",
                "Zotero: Research reference manager citations bibliography académique",
                "Grammarly: Correction grammar spelling writing assistant browser extension",
                "LanguageTool: Open-source grammar checker alternative Grammarly multi-langues",
                "AutoHotkey: Macros automation text expansion hotkeys productivité",
                "PhraseExpress: Text expander templates clipboard automation",
                "Ditto: Clipboard manager historique multiple items search",
                "ShareX: Screenshots screen recording OCR upload automation",
                "Greenshot: Screenshot tool annotation editing upload simple",
                "PowerToys: Microsoft utilities FancyZones PowerRename bulk tools",
                "Everything: File search instant indexing rapide alternative Windows search",
                "Listary: Search launcher quick file access navigation productivité",
                "7+ Taskbar Tweaker: Windows taskbar customization advanced options",
                "Rainmeter: Desktop customization widgets monitoring skins esthétique"
            ],
            "securite_avancee": [
                "Zero Trust: Principe sécurité aucune confiance implicite vérification continue",
                "Defense in depth: Multiples couches sécurité redondantes fortification",
                "Principle of least privilege: Droits minimum requis tâche réduire surface",
                "Security audit: Évaluation régulière vulnérabilités conformité politiques",
                "Penetration testing: Tests intrusion simulés identifier failles exploiter",
                "Vulnerability scanning: Analyse automatique failles logiciels configurations",
                "Security patches: Mises jour sécurité critiques appliquer rapidement",
                "Exploit mitigation: DEP ASLR CFG protections mémoire exploitation",
                "Sandboxing: Isolation applications environnement restreint confinement",
                "Application whitelisting: Autoriser uniquement apps approuvées blacklist inverse",
                "Behavioral analysis: Détection anomalies comportement malware signatures inconnues",
                "Heuristic scanning: Analyse comportementale code suspect patterns malveillants",
                "Firewall rules: Règles entrantes sortantes blocage par défaut exceptions",
                "IDS/IPS: Intrusion Detection/Prevention System monitoring réseau alertes",
                "SIEM: Security Information Event Management logs corrélation alertes central",
                "Honeypot: Système leurre attirer attaquants étudier techniques isolé",
                "Certificate pinning: HTTPS validation certificat spécifique MITM protection",
                "HSTS: HTTP Strict Transport Security forcer HTTPS downgrade attack",
                "CSP: Content Security Policy XSS protection headers injection",
                "DNSSEC: DNS Security Extensions authentification réponses poisoning protection",
                "IPSec: Internet Protocol Security VPN encryption tunnel mode transport",
                "WPA3: Wi-Fi Protected Access 3 encryption strongest WiFi security",
                "MAC filtering: Filtrage adresses physiques périphériques réseau WiFi",
                "Network segmentation: VLANs séparation réseaux isolation containment",
                "Air gap: Isolation physique réseau sécurité maximale offline",
                "Encryption at rest: Chiffrement données stockées disques BitLocker VeraCrypt",
                "Encryption in transit: TLS HTTPS VPN données network transit chiffré",
                "End-to-end encryption: E2EE chiffrement bout en bout Signal WhatsApp",
                "Key management: Gestion clés cryptographiques sécurisée rotation backup",
                "HSM: Hardware Security Module stockage clés matériel tamper-proof",
                "Smart card: Authentification two-factor physical hardware token",
                "FIDO2 / WebAuthn: Standard authentification passwordless hardware keys",
                "YubiKey: Hardware security key 2FA U2F FIDO2 OTP PIV",
                "Security questions: Éviter questions réponses devinables dictionnaire",
                "Password complexity: 12+ caractères min maj chiffres symboles unique",
                "Password rotation: Changer régulièrement 90 jours comptes sensibles",
                "Password manager: Génération stockage sécurisé passwords unique per site",
                "Multi-factor authentication: MFA 2FA authentification multiple facteurs requis",
                "Biometric authentication: Empreinte faciale reconnaissance physique 2FA"
            ],
            "troubleshooting_méthodologie": [
                "1. IDENTIFIER: Quand le problème apparaît (démarrage, utilisation, jeu, veille)",
                "2. ISOLER: Un composant spécifique ou général?",
                "3. REPRODUIRE: Le problème est-il constant ou intermittent?",
                "4. COMPARER: Le système fonctionnait avant? Changement récent?",
                "5. TESTER: Essayer en mode sans échec Windows",
                "6. VÉRIFIER: Logs Event Viewer pour erreurs critiques",
                "7. BENCHMARK: Comparer performances avant/après fix"
            ],
            "erreurs_courantes": [
                "Erreur 0x80070002: Fichier manquant Windows Update - DISM /RestoreHealth",
                "Erreur 0x80070057: Paramètre incorrect - chkdsk /f + sfc /scannow",
                "DLL manquante: Télécharger depuis dll-files.com OU réinstaller programme",
                "KERNEL_SECURITY_CHECK_FAILURE: RAM défectueuse ou pilote corrompu",
                "SYSTEM_SERVICE_EXCEPTION: Désinstaller dernier pilote installé",
                "PAGE_FAULT_IN_NONPAGED_AREA: Test RAM avec MemTest86",
                "IRQL_NOT_LESS_OR_EQUAL: Conflit pilotes - mode sans échec",
                "DPC_WATCHDOG_VIOLATION: Pilote réseau ou stockage obsolète",
                "CRITICAL_PROCESS_DIED: sfc /scannow + DISM restore",
                "BAD_POOL_HEADER: Antivirus incompatible ou RAM défectueuse"
            ],
            "outils_nitrite": [
                "🔧 Wise Care 365: Nettoyage registre + optimisation système tout-en-un",
                "💿 CrystalDiskInfo: SMART health disques, température, heures utilisation",
                "🎮 GPU-Z: Identification GPU exact, VRAM, fréquences, sensors temps réel",
                "🖥️ CPU-Z: Validation CPU, RAM speed, timings, voltages",
                "📊 HWMonitor: Températures CPU/GPU/SSD, voltages, fan speeds",
                "📊 HWinfo: Monitoring ultra-détaillé, logs, capteurs avancés",
                "⚡ CrystalDiskMark: Benchmark vitesses disque (séquentiel, 4K random)",
                "🌡️ OCCT: Stress test CPU/GPU/RAM avec monitoring température",
                "🔋 Test Batterie NiTriTe: Santé batterie avec mAh réels vs design",
                "🛡️ Malwarebytes Portable: Anti-malware sans installation",
                "🛡️ Spybot Search & Destroy: Détection spyware et tracking",
                "🛡️ AdwCleaner: Suppression adware/toolbars navigateurs",
                "🧹 Wise Disk Cleaner: Nettoyage fichiers temporaires Windows",
                "🔑 Activation Windows/Office: Scripts MassGrave (open-source)",
                "🚀 Autoruns: Gestion démarrage Windows ultra-complète"
            ],
            "windows_optimisation_avancee": [
                "Désactiver Cortana: HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search → AllowCortana = 0",
                "Désactiver télémétrie: services.msc → DiagTrack et dmwappushservice → Désactivé",
                "Désactiver Superfetch: services.msc → SysMain → Désactivé (SSD uniquement!)",
                "Désactiver Windows Search: services.msc → Windows Search → Désactivé (si SSD)",
                "Désactiver tips Windows: Paramètres → Système → Notifications → Obtenir astuces = OFF",
                "Visual Effects: SystemPropertiesAdvanced → Performances → Ajuster pour meilleures perf",
                "Désactiver hibernation (gain espace): powercfg /h off (libère plusieurs GB)",
                "Nettoyer WinSxS: DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase",
                "Page file optimal: Taille personnalisée = 1.5x RAM (ex: 16GB RAM → 24000 MB page file)",
                "Services Windows inutiles: Fax, Bluetooth (si non utilisé), Print Spooler (si pas imprimante)",
                "Game DVR désactivé: HKEY_CURRENT_USER\\System\\GameConfigStore → GameDVR_Enabled = 0",
                "Priorité processus: Task Manager → Détails → Clic droit programme → Priorité Haute",
                "Affinity CPU gaming: Réserver cœurs pour jeu (éviter core 0 car système)",
                "Désactiver Nagle: HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces → TcpAckFrequency = 1",
                "Interrupt Moderation: Panneau réseau → Propriétés carte → Avancé → Modération interruption = Désactivé",
                "MSI Mode GPU: Réduit latence (MSI Utility V2)",
                "HPET désactivé: bcdedit /deletevalue useplatformclock (meilleur pour gaming)",
                "C-States désactivés BIOS: Réduit latence CPU (au prix consommation)",
                "Power Plan Ultimate Performance: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61",
                "Désactiver GameBarPresenceWriter.exe: Prend CPU en fond (Task Manager → Terminer)"
            ],
            "registry_tweaks_avances": [
                "Explorer rapide: HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer → DisableThumbCache = 1",
                "Menu droit rapide: HKEY_CLASSES_ROOT\\Directory\\Background\\shellex\\ContextMenuHandlers → Supprimer inutiles",
                "Réduire latency audio: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile → SystemResponsiveness = 1",
                "Audio Gaming: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games → Priority = 6, Clock Rate = 10000",
                "Network Throttling OFF: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile → NetworkThrottlingIndex = ffffffff",
                "Désactiver Last Access: fsutil behavior set disablelastaccess 1",
                "SSD Optimize: fsutil behavior set disabledeletenotify 0 (TRIM activé)",
                "Prefetch SSD: HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters → EnablePrefetcher = 0",
                "TCP Window Auto-Tuning: netsh int tcp set global autotuninglevel=normal",
                "TCP Fast Open: netsh int tcp set global fastopen=enabled",
                "Reserved Bandwidth 0%: HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched → NonBestEffortLimit = 0",
                "Menu Start rapide: HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced → Start_TrackProgs = 0",
                "Animations OFF: HKEY_CURRENT_USER\\Control Panel\\Desktop\\WindowMetrics → MinAnimate = 0",
                "Explorer single click: HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer → ShellState",
                "Services.msc delay fix: HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control → WaitToKillServiceTimeout = 2000"
            ],
            "cmd_powershell_pro": [
                "Clean boot test: msconfig → Services → Cocher Masquer services Microsoft → Désactiver tout",
                "Liste programmes installés: wmic product get name,version > C:\\programs.txt",
                "Liste drivers: driverquery /v > C:\\drivers.txt",
                "Température CPU: wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature",
                "Liste processus CPU: wmic process get name,ProcessId,ThreadCount,UserModeTime,WorkingSetSize",
                "Kill processus: taskkill /IM processname.exe /F",
                "Scan fichiers système: sfc /scannow (30 min, redémarre si erreurs trouvées)",
                "Réparer image Windows: DISM /Online /Cleanup-Image /RestoreHealth",
                "Check disque complet: chkdsk C: /f /r /x (redémarrage requis, 1-5h selon taille)",
                "Liste services: sc query state= all > C:\\services.txt",
                "Info système complet: systeminfo > C:\\sysinfo.txt",
                "Test réseau: ping 8.8.8.8 -t (Ctrl+C pour arrêter)",
                "Trace route: tracert google.com",
                "DNS flush: ipconfig /flushdns",
                "Release/Renew IP: ipconfig /release && ipconfig /renew",
                "Reset TCP/IP: netsh int ip reset && netsh winsock reset",
                "Ports ouverts: netsh advfirewall show currentprofile",
                "Liste connexions actives: netstat -ano",
                "Clean temp: del /f /s /q %temp%\\* && rd /s /q %temp%",
                "Windows Update force: wuauclt /detectnow /updatenow",
                "Activation Windows check: slmgr /xpr",
                "Liste clés produit: wmic path softwarelicensingservice get OA3xOriginalProductKey",
                "Battery report: powercfg /batteryreport /output C:\\battery_report.html",
                "Sleep Study: powercfg /sleepstudy /output C:\\sleepstudy.html",
                "Energy report: powercfg /energy /output C:\\energy_report.html",
                "Liste apps store: Get-AppxPackage | Select Name, Version",
                "Désinstaller app store: Get-AppxPackage *appname* | Remove-AppxPackage",
                "Rebuild icon cache: ie4uinit.exe -show && taskkill /IM explorer.exe /F && start explorer.exe",
                "Check Windows version: winver.exe",
                "GPUpdate force: gpupdate /force"
            ],
            "bios_uefi_optimisations": [
                "XMP/DOCP Profile: Activer pour RAM full speed (DDR4 passe de 2133→3200+ MHz)",
                "Fast Boot: Enabled (gain 5-10s démarrage)",
                "CSM/Legacy Boot: Disabled (UEFI pure plus rapide)",
                "Secure Boot: Disabled si dual-boot Linux",
                "Intel Virtualization (VT-x): Enabled si VM/WSL2",
                "AMD-V: Enabled pour virtualisation AMD",
                "Above 4G Decoding: Enabled (requis grosses cartes graphiques)",
                "Resizable BAR: Enabled (RTX 30+/RX 6000+ gain 5-15% FPS)",
                "Smart Access Memory: AMD équivalent Resizable BAR",
                "C-States: Disabled pour latence mini (gaming compétitif)",
                "EIST/Cool'n'Quiet: Disabled si gaming uniquement",
                "CPU Core Ratio: Manuel pour overclock (ex: 50 = 5.0 GHz)",
                "CPU Voltage: Manuel pour undervolting (-0.050V à -0.100V typique)",
                "Load Line Calibration: Medium/High pour stabilité OC",
                "RAM Timings: CL16-18-18-38 typique DDR4 3200MHz",
                "RAM Voltage: 1.35V pour DDR4 XMP, 1.5V pour DDR5",
                "SATA Mode: AHCI (jamais IDE/RAID sauf usage spécifique)",
                "Boot Order: SSD Windows en premier",
                "Full Screen Logo: Disabled (gain 2-3s boot)",
                "NumLock on Boot: Selon préférence",
                "RGB Lighting: Disabled dans BIOS = moins overhead",
                "Audio Controller: Disabled si carte son dédiée",
                "Serial/Parallel Ports: Disabled (legacy)",
                "ErP Mode: S4+S5 pour consommation minimale OFF",
                "Power On by Keyboard: Disabled (sécurité)",
                "BIOS Update: Via USB (jamais depuis Windows!) - risque brick si coupure"
            ],
            "hardware_upgrade_guide": [
                "Upgrade #1 impact: SSD (300-500% faster) > GPU (gaming) > CPU > RAM",
                "SSD NVMe vs SATA: NVMe 7x plus rapide (3500 MB/s vs 550 MB/s) mais peu de diff réelle usage",
                "SSD TLC vs QLC: TLC plus durable (Crucial P5, WD SN850) vs QLC budget (WD Blue SN570)",
                "SSD endurance: 600 TBW minimum (TBW = TeraBytes Written lifetime)",
                "RAM upgrade: TOUJOURS dual channel (2x8 GB > 1x16 GB = 15-20% perf)",
                "RAM speed: DDR4 3200 CL16 sweet spot 2024, DDR5 5600 si plateforme récente",
                "GPU upgrade 1080p: RTX 4060 (8GB), RX 7600 (8GB) - 350-400€",
                "GPU upgrade 1440p: RTX 4070 Super (12GB), RX 7800 XT (16GB) - 600-700€",
                "GPU upgrade 4K: RTX 4080 (16GB), RX 7900 XTX (24GB) - 1000-1200€",
                "CPU upgrade AM4: Ryzen 5 5600 (150€) ou 5700X3D (250€) excellent",
                "CPU upgrade LGA1700: i5-13400F (220€) ou i5-14600K (320€)",
                "CPU upgrade AM5: Ryzen 5 7600 (230€) ou 7800X3D (450€ gaming)",
                "Bottleneck check: GPU 99% = bon, CPU 99% = CPU limite GPU",
                "PSU wattage: GPU TDP + CPU TDP + 150W margin (ex: RTX 4070 200W + i5 150W + 150W = 500W PSU min)",
                "PSU tier list: Tier A (Seasonic Focus, Corsair RMx) > B > C éviter",
                "Ventirad tower: Thermalright Peerless Assassin 120 (35€ perf Noctua NH-D15)",
                "Ventirad low-profile: Noctua NH-L9x65 (mITX), ID-Cooling IS-60",
                "AIO 240mm vs 360mm: 240mm suffit CPU 150W, 360mm si 250W+ (i9/Ryzen 9)",
                "Case airflow: 2-3 intake front/bottom, 1-2 exhaust rear/top = pression positive",
                "Monitor 1080p: 144Hz minimum gaming (BenQ Zowie, AOC 24G2)",
                "Monitor 1440p: 165-180Hz sweet spot (LG 27GP850, Dell S2721DGF)",
                "Monitor 4K: 144Hz si budget (LG 27GN950), sinon 60Hz OK",
                "Panel type: IPS (couleurs) vs TN (vitesse 1ms) vs VA (contraste)",
                "Response time: 1ms GtG gaming compétitif, 4ms acceptable",
                "VRR: G-Sync (NVIDIA) ou FreeSync (AMD) élimine tearing",
                "Thermal paste: Arctic MX-4 (7€), Thermal Grizzly Kryonaut (12€ haut de gamme)"
            ],
            "overclocking_guide": [
                "OC CPU Intel K: Multiplier core 50 = 5.0 GHz, stress test Prime95",
                "OC CPU AMD: PBO (Precision Boost Overdrive) + Curve Optimizer -15 à -30",
                "Undervolting CPU: Moins chaleur, même perf! Intel -0.080V offset, AMD CO -20",
                "OC RAM: Tighten timings CL16→CL14 gain 5%, overclock 3200→3600 gain 3-8%",
                "RAM voltage safe: 1.40V DDR4 daily, 1.50V extrême (dégradation)",
                "OC GPU NVIDIA: MSI Afterburner +150 core, +500 memory typical safe",
                "OC GPU AMD: Adrenalin +10% power limit, +100 MHz core, +50 MHz memory",
                "Undervolting GPU: 0.950V à 1950 MHz RTX 40 = -20°C même perf",
                "Stress test CPU: Prime95 Small FFT 30 min, OCCT 1h, Cinebench R23 10 runs",
                "Stress test GPU: 3DMark Time Spy loop, Unigine Heaven 30 min, FurMark 15 min",
                "Stress test RAM: MemTest86 8 passes (overnight), TestMem5 Anta777 config",
                "Stabilité check: 0 crash 24h = stable, 1 erreur MemTest = instable",
                "LLC (Load Line Calibration): Medium pour daily OC, High si droop voltage",
                "AVX offset: -2 ou -3 pour CPUs Intel (AVX charge extrême)",
                "Cooling requis OC: Air high-end (NH-D15), AIO 280/360mm, custom loop",
                "Température safe OC: CPU 80°C max daily, 90°C stress test, GPU 80°C max",
                "Dégradation: Voltage > 1.40V CPU Intel dégrade silicium long terme",
                "Garantie: OC annule garantie constructeur (sauf EVGA, XPG certains modèles)",
                "Binning: Tous CPUs différents, silicon lottery = certains OC mieux",
                "Delid CPU: Remove IHS pour -15°C, risque! (Thermalgrizzly Conductonaut liquid metal)"
            ],
            "troubleshooting_reseau": [
                "Ping test: ping 8.8.8.8 -t (Si fail = problème réseau/FAI, si OK = DNS)",
                "Test DNS: nslookup google.com (Si fail = changer DNS)",
                "DNS optimal: Cloudflare 1.1.1.1/1.0.0.1 (rapide), Google 8.8.8.8/8.8.4.4",
                "DNS-over-HTTPS: Sécurisé mais peut ralentir, test avec/sans",
                "WiFi 2.4 GHz: Portée ++, vitesse max 150 Mbps, canaux 1/6/11 évitent interférences",
                "WiFi 5 GHz: Portée --, vitesse max 1300+ Mbps, moins interférences",
                "WiFi 6 (AX): Meilleur latence, 9.6 Gbps théorique, requis routeur + carte compatibles",
                "Canal WiFi optimal: WiFi Analyzer app trouve canal le moins encombré",
                "Ethernet cat5e vs cat6: Cat5e = 1 Gbps, Cat6 = 10 Gbps sur 55m",
                "Powerline adapters: 500-1200 Mbps via prise électrique, alternative Ethernet",
                "QoS (Quality of Service): Priorité gaming/streaming dans routeur",
                "UPnP: Activer pour gaming (auto port forwarding), désactiver si problème sécurité",
                "Port Forwarding: Manuel si UPnP fail, vary par jeu (ex: 3074 Xbox, 27015-27030 Steam)",
                "DMZ: Met PC hors firewall (sécurité --, mais règle NAT strict)",
                "NAT Type: Open (meilleur) > Moderate > Strict (problème matchmaking)",
                "Mesh WiFi: Plusieurs points = couverture maison complète (Google WiFi, Eero)",
                "Bufferbloat: Latency spike upload/download, test dslreports.com/speedtest",
                "Bufferbloat fix: SQM (Smart Queue Management) routeur, limite bande 90%",
                "IPv6: Activé si FAI supporte (future-proof), peut causer bug certain jeux",
                "Jumbo Frames: MTU 9000 réseau local (NAS) gain 10-15%, jamais internet"
            ],
            "gaming_competitive_tweaks": [
                "Input lag réduction: Plein écran exclusif (pas Borderless), VSync OFF + G-Sync",
                "FPS cap optimal: Refresh rate -3 (141 FPS pour 144Hz) élimine tearing",
                "Mouse polling: 1000 Hz minimum (Razer/Logitech), 4000 Hz si supported",
                "Mouse DPI: 800-1600 pro players, sensibilité in-game pour 25-35cm/360°",
                "Disable mouse accel: Panneau config > Souris > Options pointeur > Améliorer précision = OFF",
                "Raw Input: Enabled in-game (ignore Windows sensitivity)",
                "MarkC Mouse Fix: Corrige scaling Windows (si raw input unavailable)",
                "Monitor overdrive: Medium (pas Max = overshoot ghosting)",
                "Response time: 1ms GtG gaming, 4ms acceptable, 10ms éviter",
                "Black equalizer: +15-20 visibilité zones sombres sans perdre détails",
                "Vibrance: +15-20 couleurs pop, visibilité ennemis (NVIDIA Digital Vibrance)",
                "Sharpening: +10-15 via pilote GPU si DLSS/FSR (combat blur)",
                "Low Latency Mode: NVIDIA Ultra (Reflex), AMD Anti-Lag, gain 10-30ms",
                "NVIDIA Reflex: Activé in-game si RTX 20+ série, analyze latency",
                "Frame Generation: OFF compétitif (latency ++), ON solo/casual (FPS ++)",
                "Audio: Stéréo > Surround virtuel (meilleur positionnement), HRTF in-game",
                "Network: Ethernet OBLIGATOIRE, WiFi 20-50ms latency supplémentaire",
                "Background apps: Close Discord overlay, Chrome, RGB software si FPS drop",
                "Fullscreen Optimizations: Désactiver (exe > Propriétés > Compatibilité)",
                "Process affinity: Réserver 2 threads CPU pour OS, reste pour jeu",
                "Multicore rendering: Enabled (gain 40-100% FPS si CPU multi-core)"
            ],
            "stockage_management": [
                "SSD vs HDD: SSD 100x plus rapide accès, HDD stockage masse (4-8 TB)",
                "Partitionnement optimal: 100-150 GB C: système, reste D: jeux/données",
                "Espace libre requis: 15% minimum SSD perf, 10% HDD défragmentation",
                "SSD Health: CrystalDiskInfo vérifier % vie, réallocated sectors count",
                "SMART warnings: Reallocated sectors > 0 = disque meurt, backup urgent!",
                "Défragmentation: JAMAIS SSD (usure inutile), HDD 1x/mois si <15% libre",
                "TRIM: Commande SSD cleanup, auto Windows si fsutil behavior query disabledeletenotify = 0",
                "Temp files: C:\\Windows\\Temp, %temp%, Prefetch (safe delete)",
                "WinSxS: 5-10 GB, ne PAS delete manuellement! DISM cleanup uniquement",
                "Hibernation: hiberfil.sys = taille RAM, delete via powercfg /h off",
                "Page file: 1.5x RAM ou auto, SSD OK (modern SSD TBW élevé)",
                "Storage Spaces: RAID software Windows, mirror = RAID1, parity = RAID5",
                "Clonage SSD: Macrium Reflect Free, Clonezilla (free), Samsung Data Migration",
                "Secure Erase SSD: ATA Secure Erase (permanent, restaure perf factory)",
                "File system: NTFS Windows, exFAT USB cross-platform, FAT32 old (4GB limit)",
                "Compression NTFS: Gain 20-40% espace au prix CPU +5% (old PC éviter)",
                "Cloud backup: 3-2-1 rule (3 copies, 2 mediums, 1 off-site)",
                "NAS storage: Synology DS220+ (budget), QNAP TS-464 (performance)",
                "External HDD: WD Elements, Seagate Expansion fiables, éviter Backup Plus",
                "M.2 vs 2.5 SSD: M.2 NVMe plus rapide (3500 MB/s), 2.5 SATA (550 MB/s)"
            ],
            "cooling_temperature_guide": [
                "Temp idle CPU: 30-45°C normal, 50°C+ nettoyer/remplacer pâte",
                "Temp charge CPU: 60-80°C normal, 80-90°C chaud, 90°C+ throttling danger",
                "Temp idle GPU: 30-50°C normal, ventilo stop < 60°C modern cards",
                "Temp charge GPU: 65-85°C normal, 85-90°C chaud, 90°C+ throttling",
                "Thermal throttling: Horloge baisse auto si > 95-100°C protection",
                "Thermal shutdown: 105-110°C CPU, 100-105°C GPU protection ultime",
                "Case airflow: Pression positive (intake > exhaust) moins poussière",
                "Fan curve: 40% idle silent, ramp 60°C, 75% à 80°C, 100% à 90°C",
                "Pâte thermique: Renouveler tous 2-3 ans (séchée = +10-15°C)",
                "Application pâte: Grain riz centre (spread seul), ligne si rectangulaire",
                "Liquid metal: -10°C vs pâte mais dangereux (conducteur, colle), expert only",
                "Undervolt benefit: -15°C CPU/GPU même performance (sweet spot)",
                "Repaste laptop: Complexe démontage, pro recommandé si garantie expirée",
                "Laptop cooling pad: -5°C à -10°C, obligatoire si throttle",
                "Custom water loop: -20°C possible mais 500€+ et maintenance",
                "Fan placement: Front/Bottom intake cool air, Rear/Top exhaust hot air",
                "Dust filters: Nettoyage mensuel, airflow -20% si obstrués",
                "Cable management: Améliore airflow 3-5°C, esthétique ++",
                "Negative pressure: Exhaust > intake, aspire poussière fentes",
                "AIO rad position: Top exhaust optimal, front intake acceptable (CPU chaud)"
            ],
            "audio_troubleshooting": [
                "Pas de son: Vérifier device sortie (Speakers icon taskbar > bon périphérique?)",
                "Playback devices: Panneau config > Son > Lecture > Définir par défaut",
                "Pilote audio: Realtek HD Audio Manager, update via site carte mère",
                "Enhancements: Désactiver tous (Propriétés device > Améliorations > Désactiver tout)",
                "Sample rate: 16 bit 44100 Hz (CD quality) ou 24 bit 48000 Hz",
                "Exclusive mode: Permettre applications contrôle exclusif (low latency)",
                "Crépitements: Buffer size audio (ASIO), DPC Latency Checker trouve coupable",
                "ASIO driver: FL Studio, Ableton (low latency 5-10ms), FlexASIO free",
                "Spatial sound: Windows Sonic free (acceptable), Dolby Atmos (meilleur payant)",
                "Headphone virtualization: Razer Surround, HeSuVi (positional gaming)",
                "Microphone boost: +10 dB max (plus = bruit fond), noise gate -40 dB",
                "Noise suppression: NVIDIA RTX Voice, Krisp, OBS noise suppression",
                "Audio crackling: Désactiver power saving USB (Device Manager > USB > Propriétés)",
                "Bluetooth latency: 150-200ms, inutilisable gaming, AptX Low Latency requis",
                "DAC/AMP: Améliore qualité si headphones 250+ ohms (FiiO, Schiit)",
                "Peace APO + AutoEQ: Égalisation automatique 1000+ headphones",
                "VoiceMeeter: Table mixage virtuelle (streamer), routing complexe",
                "Realtek Audio Console: Windows Store app si pilote DCH moderne",
                "Sound blaster: Carte son dédiée inutile 2024 (onboard excellent)",
                "USB audio: Isolé électriquement (moins interférences vs jack 3.5mm)"
            ],
            "windows_recovery_repair": [
                "Safe Mode: F8 boot ou Shift+Restart > Dépannage > Avancé > Démarrage",
                "Safe Mode types: Minimal (base), Networking (+ réseau), Command Prompt",
                "Point restauration: Panneau > Système > Protection système > Restaurer",
                "System Restore: Annule modifs système (pilotes, apps) garde fichiers perso",
                "Reset This PC: Keep files ou Remove all, réinstalle Windows propre",
                "DISM Health: DISM /Online /Cleanup-Image /RestoreHealth (30-60 min)",
                "SFC scan: sfc /scannow (15-30 min après DISM)",
                "Startup Repair: Boot USB Windows > Réparer ordinateur > Dépannage",
                "BCDEdit fix: bootrec /fixmbr puis /fixboot puis /rebuildbcd",
                "Partition recovery: TestDisk (free) récupère partitions perdues",
                "File recovery: Recuva (free), PhotoRec (pro), R-Studio (payant puissant)",
                "Bootable USB: Rufus + ISO Windows, select GPT/UEFI ou MBR/BIOS",
                "Clean install: Backup perso > Boot USB > Install > Delete all partitions",
                "Windows.old: Ancien Windows après upgrade, delete via Disk Cleanup",
                "DISM Source: DISM /Online /Cleanup /RestoreHealth /Source:wim:D:\\sources\\install.wim:1",
                "Registry backup: regedit > File > Export (full backup .reg)",
                "Driver backup: Double Driver (free) exporte tous pilotes",
                "Activation backup: ProduKey (NirSoft) trouve clés Windows/Office",
                "Shadow copies: vssadmin list shadows (Previous Versions fichiers)",
                "Event Viewer: eventvwr.msc > Windows Logs > System (errors avant crash)"
            ],
            "privacy_security_hardening": [
                "Telemetry block: O&O ShutUp10++ (free) désactive tracking Windows",
                "Firewall rules: wf.msc custom rules, block telemetry IPs",
                "Windows Defender: Meilleur free antivirus 2024, suffisant si prudent",
                "BitLocker: Chiffrement disque intégré Windows Pro, TPM requis",
                "VeraCrypt: Alternative BitLocker free, containers chiffrés portables",
                "Password manager: Bitwarden (free open-source), 1Password (payant UX++)",
                "2FA: Authy, Microsoft Authenticator, Google Authenticator (backups Authy)",
                "Hardware key: YubiKey 5 NFC (50€) phishing-proof authentication",
                "VPN: Mullvad (privacy), Proton VPN (free tier ok), éviter free VPN louches",
                "DNS-over-HTTPS: Cloudflare 1.1.1.1, NextDNS (ad-blocking intégré)",
                "Hosts file: Block telemetry/ads via C:\\Windows\\System32\\drivers\\etc\\hosts",
                "UAC: Toujours activé (User Account Control), prompt admin requis",
                "AppLocker: Windows Pro/Enterprise, whitelist applications autorisées",
                "Windows Sandbox: Test apps suspectes environnement isolé jetable",
                "Secure Boot: Protection bootkit/rootkit, requis Windows 11",
                "TPM 2.0: Trusted Platform Module, requis Windows 11, stockage clés",
                "Updates: JAMAIS désactiver! Patchs sécurité critiques mensuels",
                "SMBv1: Désactiver (vulnérable WannaCry), Features > SMB 1.0 = OFF",
                "RDP security: Changer port 3389, IP whitelist, strong password, 2FA",
                "Browser hardening: uBlock Origin, HTTPS Everywhere, Privacy Badger"
            ],
            "ram_expert_deepdive": [
                "DDR4: Double Data Rate 4th gen, 2133-3600 MHz standard, 1.2V",
                "DDR5: 4800-8000 MHz, 1.1V, on-die ECC, dual 32-bit channels",
                "CAS Latency (CL): Premier timing, CL14-CL18 DDR4, CL32-CL40 DDR5",
                "Timing format: CL-tRCD-tRP-tRAS, ex: 16-18-18-38",
                "tRCD: RAS to CAS Delay, row activation delay",
                "tRP: RAS Precharge, time to close row",
                "tRAS: Row Active Strobe, row open minimum time",
                "Command Rate: 1T vs 2T, 1T meilleur performance si stable",
                "Gear Mode: DDR5 Gear 2 (2:1) vs Gear 4 (4:1), Gear 2 meilleur",
                "XMP: Extreme Memory Profile, Intel one-click overclock profile",
                "EXPO: Extended Profiles for Overclocking, AMD version XMP DDR5",
                "DOCP: Direct Overclock Profile, AMD ASUS branding",
                "A-XMP: AMD Extended Memory Profile, MSI branding",
                "Dual Channel: 2 sticks, 2x bandwidth, obligatoire gaming",
                "Quad Channel: 4 sticks, HEDT/Threadripper, 4x bandwidth",
                "Single Rank vs Dual Rank: DR meilleur performance (+3-5%)",
                "Rank: Groupe de puces mémoire sur barrette, 1R/2R visible",
                "Capacity per DIMM: 8GB, 16GB, 32GB, 48GB (DDR5 new)",
                "Maximum capacity: 128 GB consumer (4x32), 192 GB DDR5 (4x48)",
                "IC manufacturer: Samsung B-die (best OC), Hynix, Micron",
                "Samsung B-die: DDR4 3200 CL14, golden OC binning",
                "Micron E-die: Budget OC champion, 3000 CL15 → 3600 CL16",
                "Hynix CJR/DJR: Good mid-range OC, 3200 CL16 → 3600 CL18",
                "Thaiphoon Burner: Identify RAM IC manufacturer tool",
                "MemTest86: Bootable USB, gold standard RAM test, 0 errors req",
                "TestMem5 Anta777: Extreme config, catches errors MemTest86 misses",
                "OCCT Memory: Windows-based stress test with error detection",
                "Prime95 Large FFT: Stress test RAM + CPU, detects instability",
                "AIDA64 Cache & Memory: Benchmark bandwidth read/write/copy/latency",
                "RAM bandwidth: 50-60 GB/s DDR4 dual channel, 80-100 GB/s DDR5",
                "RAM latency: 45-55 ns DDR4 3600 CL16, 65-75 ns DDR5 5600 CL36",
                "True latency formula: (CL / Frequency MHz) * 2000 = ns",
                "Frequency vs Timings: 3200 CL14 = 3600 CL16 latency (~8.75 ns)",
                "Ryzen RAM scaling: Infinity Fabric syncs RAM, 3600 MHz sweet spot",
                "Ryzen FCLK: 1800 MHz max stable (1:1 with 3600 RAM)",
                "Ryzen MCLK: Memory clock, half of RAM speed (1800 for 3600)",
                "Intel RAM scaling: Moins sensible, 3200-4000 sufficient",
                "Gear 1 vs Gear 2: Intel DDR4 Gear 1 1:1, Gear 2 1:2 high freq",
                "DDR5 on-die ECC: Error correction built-in, different from UDIMM ECC",
                "ECC UDIMM: Server RAM, detects/corrects single-bit errors",
                "Non-ECC: Consumer RAM, no error correction, sufficient gaming",
                "RGB RAM: Aesthetics, peut interférer OC (disable RGB si instable)",
                "RAM heat spreaders: Aluminum dissipateurs, utiles DDR5 (chauffe plus)",
                "RAM temperature: 40-50°C normal load, 60°C+ DDR5 stress test",
                "JEDEC standards: Base spec, 2133 MT/s DDR4, 4800 MT/s DDR5",
                "MT/s vs MHz: Mega Transfers vs Mega Hertz, MT/s = MHz × 2 (DDR)",
                "Subtimings: 20+ timings secondaires, fine-tuning 1-2% gains",
                "tRFC: Refresh Cycle Time, 300-800, lower better",
                "tREFI: Refresh Interval, higher = performance (risky)",
                "Voltage scaling: 1.35V XMP safe, 1.40V daily max, 1.50V extreme",
                "VCCSA/VCCIO: Intel System Agent/IO voltage, aide stabilité RAM OC",
                "SOC voltage: AMD Ryzen, 1.0-1.2V, aide stabilité RAM OC",
                "CLDO_VDDP: AMD voltage, 0.9-1.05V, important haute fréquence",
            ],
            "ssd_nvme_expert": [
                "NVMe: Non-Volatile Memory Express, protocol PCIe direct",
                "M.2: Form factor, 2280 (22mm x 80mm) most common",
                "2242, 2260, 2280, 22110: M.2 lengths, longer = more NAND chips",
                "PCIe Gen3 x4: 4000 MB/s max, ~3500 MB/s real (Samsung 970 EVO)",
                "PCIe Gen4 x4: 7500 MB/s max, ~7000 MB/s real (Samsung 990 Pro)",
                "PCIe Gen5 x4: 14000 MB/s max, nouveau 2024, peu de benefit encore",
                "SATA III: 600 MB/s max, ~550 MB/s real, legacy interface",
                "AHCI: Advanced Host Controller Interface, SATA protocol",
                "Sequential read: Large files streaming, important games AAA",
                "Sequential write: Copying big files, video editing",
                "4K random read: Small files, OS responsiveness, IOPS critical",
                "4K random write: Database, OS writes, most important metric",
                "IOPS: Input/Output Operations Per Second, 500K+ high-end NVMe",
                "QD: Queue Depth, concurrent operations, QD1 = typical usage",
                "TLC: Triple-Level Cell, 3 bits/cell, mainstream (Samsung 980 Pro)",
                "QLC: Quad-Level Cell, 4 bits/cell, slower writes but cheap",
                "MLC: Multi-Level Cell, 2 bits/cell, fast but expensive (rare now)",
                "SLC: Single-Level Cell, fastest/durable, used as cache",
                "SLC cache: TLC/QLC use SLC mode for burst speed, 10-200 GB",
                "Cache exhaustion: Writes drop to 100-300 MB/s after cache full",
                "DRAM cache: Onboard RAM chip, speeds up mapping table (meilleur)",
                "DRAMless: No RAM chip, uses HMB (cheaper but slower)",
                "HMB: Host Memory Buffer, uses system RAM, 64-256 MB",
                "Controller: Phison E18, Samsung Elpis, manages NAND",
                "Phison E18: High-end PCIe Gen4 controller, 7000 MB/s capable",
                "Samsung Elpis: Custom controller 990 Pro, 7400 MB/s",
                "TBW: TeraBytes Written, endurance rating, 600 TBW = 5 years 330 GB/day",
                "DWPD: Drive Writes Per Day, enterprise rating, 1 DWPD = full write daily",
                "Wear leveling: Distributes writes evenly across NAND",
                "Over-provisioning: Reserved space 7-28%, improves longevity",
                "TRIM: OS notifies SSD deleted blocks, maintains performance",
                "TRIM check: fsutil behavior query disabledeletenotify (0 = enabled)",
                "Garbage collection: SSD internal cleanup deleted blocks",
                "SMART attributes: 05 Reallocated Sectors Count critical, 0 ideal",
                "SMART 09: Power-On Hours, usage tracking",
                "SMART C2: Temperature, 40-50°C normal, 70°C+ throttle",
                "SMART E7: % Life Remaining, 100% new, RMA < 10%",
                "CrystalDiskInfo: Monitor SMART, health status Good/Caution/Bad",
                "CrystalDiskMark: Benchmark speeds SEQ/4K Q1T1/Q8T8/Q32T16",
                "AS SSD Benchmark: Score overall performance, compression test",
                "ATTO Disk Benchmark: Variable block sizes 512B-64MB test",
                "Secure Erase: ATA command wipes + restores factory performance",
                "Secure Erase tools: Samsung Magician, Crucial Storage Executive",
                "Format vs Secure Erase: Format leaves data recoverable, SE permanent",
                "Partition alignment: 1 MB (2048 sectors) optimal, automatic Windows 7+",
                "File system: NTFS Windows, exFAT cross-platform, ext4 Linux",
                "Cloning: Macrium Reflect Free, Clonezilla, Samsung Data Migration",
                "Encryption: BitLocker (Windows), LUKS (Linux), hardware AES 256-bit",
                "Self-Encrypting Drive (SED): Hardware encryption, TCG Opal 2.0",
                "NVMe heatsink: Aluminum or copper, -10°C thermal throttle prevention",
                "Thermal throttling: Reduces speed if >70-80°C, avoid by heatsink",
                "M.2 slot sharing: Some slots disable SATA ports (check manual)",
                "M.2 slot bandwidth: CPU lanes vs chipset lanes, direct CPU faster",
                "Boot drive optimization: Disable hibernate/swap if enough RAM",
            ],
            "motherboard_chipset_expert": [
                "Intel Z790: 12th/13th/14th gen, full OC, DDR5, PCIe 5.0",
                "Intel B760: Locked OC except RAM, mainstream value",
                "Intel H770: Business chipset, vPro support",
                "AMD X670E: Ryzen 7000, full OC, PCIe 5.0 GPU+NVMe",
                "AMD X670: PCIe 5.0 NVMe only, GPU PCIe 4.0",
                "AMD B650E: Budget OCable, PCIe 5.0 NVMe",
                "AMD B650: Entry level, PCIe 4.0 only",
                "VRM phases: More = better power delivery, 12+2 minimum good CPU OC",
                "VRM cooling: Heatsinks required high-end CPUs, bare VRM = throttle",
                "PWM vs Digital: Digital VRM meilleur efficacité (IR, Infineon)",
                "DrMOS: Driver + MOSFET integrated, compact efficient",
                "Power stages: 50A, 60A, 70A per phase, higher = more current",
                "Doublers: Fake phase count marketing, 8 real = 16 doubled",
                "Teaming: Parallel MOSFETs, increase amperage per phase",
                "PCIe lanes CPU: 16-20 lanes direct CPU (16 GPU + 4 M.2)",
                "PCIe lanes chipset: 4-16 additional lanes, higher latency",
                "PCIe bifurcation: Split x16 slot to 2x x8 or 4x x4",
                "M.2 slots: 1-5 slots modern boards, check PCIe gen and source",
                "SATA ports: 4-8 ports, may share bandwidth with M.2",
                "USB standards: USB 3.2 Gen 1 (5 Gbps), Gen 2 (10 Gbps), Gen 2x2 (20 Gbps)",
                "USB4: 40 Gbps, Thunderbolt 3 compatible, rare motherboards",
                "USB Type-C: Connector type, can be USB 2.0 to USB4 speeds",
                "Thunderbolt 4: Intel, 40 Gbps, PCIe tunneling, daisy chain",
                "Audio codec: Realtek ALC1220 good, ALC4080 excellent, ESS DAC best",
                "Audio SNR: Signal-to-Noise Ratio, 100 dB decent, 120 dB excellent",
                "Network: Intel I225-V 2.5 GbE good, Realtek 8125B acceptable",
                "WiFi 6E: 6 GHz band, less interference, AX210/AX211 Intel",
                "WiFi 7: BE200 Intel, 5.8 Gbps theoretical, MLO multi-link",
                "Bluetooth 5.3: 2 Mbps, LE Audio, LC3 codec",
                "BIOS flashback: Update BIOS sans CPU/RAM (bouton + USB)",
                "Clear CMOS: Reset BIOS settings, jumper ou bouton",
                "POST codes: Debug LED/display, identify boot failure",
                "Q-LED / EZ Debug: CPU/RAM/GPU/BOOT diagnostic LEDs",
                "UEFI BIOS: Modern graphical interface, mouse support",
                "Legacy BIOS: Text mode, PS/2 keyboard, old systems",
                "TPM 2.0: Trusted Platform Module, fTPM (firmware) ou dTPM (discrete)",
                "Secure Boot: UEFI security, validates bootloader signatures",
                "Fast Boot: Skip full POST, faster boot time",
                "Multi-Core Enhancement: Intel auto-OC all cores to turbo",
                "PBO: Precision Boost Overdrive, AMD auto-OC, safe",
                "LLC levels: 1-8, higher = less vdroop, Level 5-6 sweet spot",
                "Current protection: OCP/OPP/OVP/SCP prevent damage",
                "RGB headers: 12V 4-pin (RGB), 5V 3-pin (ARGB/aRGB)",
                "Fan headers: PWM 4-pin (DC control), DC 3-pin (voltage control)",
                "Fan curves: BIOS configure temperature targets, % speed",
                "AIO pump header: Full speed always, dedicated header important",
            ],
            "monitor_display_expert": [
                "Refresh rate: 60/75/120/144/165/240/360 Hz, higher = smoother",
                "Response time: GtG (Gray-to-Gray), 1ms competitive, 4ms acceptable",
                "Input lag: Signal delay, <10ms competitive, test rtings.com",
                "Panel type IPS: In-Plane Switching, meilleurs angles + couleurs",
                "Panel type VA: Vertical Alignment, meilleur contraste, ghosting",
                "Panel type TN: Twisted Nematic, 1ms fast mais angles/couleurs mauvais",
                "Panel type OLED: Perfect blacks, infinite contrast, burn-in risk",
                "Resolution 1080p: 1920×1080, 24\" max idéal, entry level",
                "Resolution 1440p: 2560×1440, 27\" sweet spot, performance/qualité",
                "Resolution 4K: 3840×2160, 27-32\", requis GPU puissant",
                "Resolution ultrawide: 3440×1440 (21:9), 3840×1600, immersif",
                "Pixel density: 27\" 1440p = 109 PPI, 4K = 163 PPI",
                "Aspect ratio: 16:9 standard, 21:9 ultrawide, 32:9 super ultrawide",
                "Brightness: 250-350 nits SDR, 400+ nits HDR requis",
                "Contrast ratio: 1000:1 IPS, 3000:1 VA, infinite OLED",
                "HDR10: 10-bit color, metadata static, baseline HDR",
                "DisplayHDR 400: VESA cert, 400 nits, meh fake HDR",
                "DisplayHDR 600: 600 nits, 10-bit, acceptable entry HDR",
                "DisplayHDR 1000: 1000 nits, FALD, true HDR experience",
                "Dolby Vision: Dynamic metadata, 12-bit, content dependent",
                "FALD: Full Array Local Dimming, meilleurs HDR blooming control",
                "Edge-lit: Cheaper backlight, worse HDR uniformity",
                "Zone count: FALD zones 100-1000+, more = less blooming",
                "Color gamut sRGB: 100% = accurate web/sRGB content",
                "Color gamut DCI-P3: Film standard, 90%+ good HDR",
                "Color gamut Adobe RGB: Photography, wider than sRGB",
                "Color accuracy ΔE: <2 professional, <1 perfect, 3-5 acceptable",
                "Calibration: Hardware (X-Rite, Datacolor), software (DisplayCAL)",
                "Overdrive: Pixel response acceleration, Medium meilleur (pas Extreme)",
                "Ghosting: Motion blur trails, VA prone, check UFO test",
                "Backlight bleed: IPS glow edges, lottery, worse dark rooms",
                "Dead pixels: ISO 13406-2 Class II = 2 dead acceptable (bullshit)",
                "G-Sync: NVIDIA VRR module, 30-max Hz range, expensive",
                "G-Sync Compatible: FreeSync monitor validated NVIDIA",
                "FreeSync: AMD VRR, 48-max Hz typical, cheaper",
                "FreeSync Premium: 120 Hz minimum, LFC support",
                "LFC: Low Framerate Compensation, double frames < min range",
                "VRR range: 48-144 Hz good, 30-240 Hz excellent",
                "DisplayPort 1.4: 32.4 Gbps, 1440p 240Hz, 4K 120Hz",
                "DisplayPort 2.1: 80 Gbps, 4K 240Hz, 8K 60Hz",
                "HDMI 2.0: 18 Gbps, 1080p 240Hz, 4K 60Hz",
                "HDMI 2.1: 48 Gbps, 4K 120Hz, 8K 60Hz, VRR native",
                "DSC: Display Stream Compression, lossless visually, enables higher specs",
                "Chroma subsampling 4:4:4: Full color, text sharp",
                "Chroma subsampling 4:2:2: Compressed, gaming ok",
                "Chroma subsampling 4:2:0: Heavy compression, avoid text",
                "ClearType: Windows font smoothing, configure for RGB/BGR",
            ],
            "keyboard_mouse_peripherals": [
                "Mechanical switches Cherry MX Red: Linear smooth, 45g, gaming",
                "Cherry MX Brown: Tactile bump, 55g, polyvalent",
                "Cherry MX Blue: Clicky loud, 60g, typing",
                "Cherry MX Speed Silver: Linear light, 45g, 1.2mm actuation fast",
                "Cherry MX Black: Linear heavy, 60g, avoid accidental press",
                "Gateron switches: Cherry clone cheaper, Yellow = smooth",
                "Kailh switches: Box White clicky, Speed Silver fast",
                "Optical switches: Light beam, faster response, Razer/Wooting",
                "Analog switches: Variable actuation, Wooting double-tap",
                "Hall Effect: Magnetic contactless, infinite durability",
                "Actuation force: 45g light, 60g medium, 80g+ heavy",
                "Actuation point: 1.5mm fast, 2.0mm standard, 3.5mm full travel",
                "Travel distance: 4mm full mechanical, 1.5mm low profile",
                "Keycap material ABS: Cheap, smooth, shines over time",
                "Keycap material PBT: Textured, durable, no shine",
                "Keycap profile OEM: Standard, sculpted rows",
                "Keycap profile Cherry: Lower height, gaming preferred",
                "Keycap profile SA: Tall vintage, loud typing",
                "Hot-swap: Replace switches without soldering",
                "Stabilizers: Spacebar/Enter, lubed = less rattle",
                "Polling rate keyboard: 1000 Hz standard, 8000 Hz Razer",
                "N-key rollover: All keys simultaneous, anti-ghosting",
                "RGB per-key: Individual LED control, expensive",
                "RGB zone: 5-10 zones, cheaper than per-key",
                "Macro keys: Programmable, 5-18 extra keys",
                "Media keys: Volume wheel, play/pause dedicated",
                "Wrist rest: Ergonomic, leather/memory foam",
                "TKL: Tenkeyless, no numpad, compact",
                "60%: No F-row, arrows, numpad, ultra compact",
                "75%: Compact with F-row, good balance",
                "Mouse sensor PixArt 3360: Flawless, no acceleration, 12000 DPI",
                "PixArt 3370: Wireless optimized, low latency",
                "PixArt 3395: Flagship 26000 DPI, overkill",
                "Razer Focus+: Optical 20000 DPI, proprietary",
                "Logitech HERO: 25000 DPI, efficient battery",
                "DPI: Dots Per Inch, 800-1600 pro gaming, 3200+ marketing",
                "Mouse acceleration: DISABLE! Inconsistent aim",
                "Pointer precision: Windows enhance = acceleration, OFF!",
                "Polling rate mouse: 1000 Hz minimum, 4000/8000 Hz competitive",
                "Sensor position: Center mouse optimal tracking",
                "Mouse weight: 60-80g modern, <60g ultra-light, 100g+ heavy",
                "Mouse feet PTFE: Teflon smooth glide, thickness varies",
                "Hyperglides: Premium PTFE feet, smoother than stock",
                "Mouse grip Palm: Whole hand contact, relaxed",
                "Mouse grip Claw: Arched fingers, tips + palm contact",
                "Mouse grip Fingertip: Fingers only, agile",
                "Mouse size: 12cm hand = small, 18cm = medium, 20cm+ = large",
                "Wireless latency: <1ms modern, wired competitive advantage gone",
                "Wireless battery: 70+ hours standard, charging dock/cable",
                "Bluetooth mode: Latency 10-20ms, multi-device",
                "2.4GHz dongle: <1ms latency, gaming mode",
                "Mouse software: Logitech G Hub, Razer Synapse, onboard memory",
                "Mousepad cloth: Control, Artisan Zero, Zowie G-SR",
                "Mousepad hard: Speed, low friction, Razer Strider",
                "Mousepad size: 450x400mm standard, 900x400mm deskmat",
                "Headset drivers: 40mm small, 50mm large, bigger ≠ better",
                "Headset impedance: 32Ω easy drive, 250Ω+ needs AMP",
                "Headset frequency: 20-20000 Hz human range, extended marketing",
                "Surround sound: Stereo better positional, 7.1 virtual gimmick",
                "Open-back: Sound leaks, better soundstage, home use",
                "Closed-back: Noise isolation, bass focused, portable",
                "Microphone type condenser: Studio quality, sensitive",
                "Microphone type dynamic: Broadcast, noise rejection",
                "Microphone polar pattern cardioid: Front pickup, rejects sides",
                "USB vs XLR: USB plug-and-play, XLR pro quality needs interface",
            ],
            "laptop_specific_optimization": [
                "Laptop TGP: Total Graphics Power, 80W mobile vs 320W desktop RTX 4090",
                "Max-Q: NVIDIA thin power-limited design, -20% performance",
                "Max-P: Maximum Performance, full power GPU laptop",
                "GPU variant: RTX 4060 Laptop 80W ≠ 140W big difference",
                "CPU variant: i7-13700H (45W) vs HX (55W) vs HK (unlocked)",
                "U-series: Ultra-low power 15W, thin&light, office work",
                "H-series: High performance 45W, gaming/workstation",
                "HX-series: Extreme 55W, desktop replacement",
                "Thermal throttling: Common laptops, -20% performance if hot",
                "Repaste: Replace thermal paste every 2 years, -10°C possible",
                "Thermal pads: GPU VRAM cooling, thicker pads better contact",
                "Liquid metal: -15°C vs paste, risky (conductif), pro install",
                "Undervolting CPU: ThrottleStop -100mV typical, stable -10°C",
                "ThrottleStop: Voltage offset, disable turbo, ratio limits",
                "Laptop fan control: SpeedFan (old), NoteBookFanControl custom curves",
                "Cooling pad: Mesh bottom, 2-4 fans, -5°C to -10°C",
                "Laptop position: Elevate rear, improve intake airflow",
                "Disable Turbo: BIOS or ThrottleStop, -20°C but -15% perf",
                "MUX switch: Direct GPU output, +10% FPS vs Optimus",
                "NVIDIA Optimus: iGPU routing, saves battery, adds latency",
                "Advanced Optimus: Dynamic MUX, auto switch iGPU/dGPU",
                "AMD Hybrid Graphics: Optimus equivalent AMD",
                "Battery care: 60-80% charge ideal longevity, full cycle monthly",
                "Battery wear: 80% health after 500 cycles typical",
                "Battery calibration: Full discharge→full charge, reset gauge",
                "Power plan: Balanced default, Performance full speed, Battery saver",
                "Panel Overdrive: Some laptops have, reduces ghosting",
                "DisplayPort over USB-C: Thunderbolt 3/4 external monitor 4K 60Hz+",
                "eGPU: External GPU Thunderbolt, -20% vs internal, expensive",
                "RAM upgrade: SO-DIMM slots, 2x16GB typical max",
                "Storage upgrade: M.2 2280, some laptops have 2 slots",
                "WiFi card upgrade: Intel AX210 drop-in, M.2 2230 E-key",
                "Warranty void: Disassembly may void, check manufacturer policy",
            ],
            "streaming_content_creation": [
                "OBS Studio: Open source, free, CPU x264 or GPU NVENC/AMF",
                "Streamlabs OBS: OBS fork, easier UI, built-in alerts",
                "OBS x264: CPU encoder, better quality slow preset",
                "NVENC: NVIDIA GPU encoder, quality preset high native",
                "NVENC B-frames: 2 B-frames = better quality, more latency",
                "QuickSync: Intel iGPU encoder, quality between x264/NVENC",
                "AMF: AMD GPU encoder, quality improved RX 6000/7000",
                "AV1: Next-gen codec, 40% bitrate reduction, RTX 40/RX 7000",
                "Bitrate 1080p60: 6000 kbps good, 8000-10000 kbps excellent",
                "Bitrate 1440p60: 12000-16000 kbps, platform limit check",
                "CBR: Constant Bitrate, streaming, predictable upload",
                "VBR: Variable Bitrate, recording, better quality files",
                "Keyframe interval: 2 seconds (2x framerate), required streaming",
                "Preset x264: ultrafast/veryfast streaming, slow recording",
                "Profile: High, Level 4.2, required 1080p60",
                "Audio bitrate: 128 kbps AAC good, 160 kbps better, 320 overkill",
                "Sample rate: 48 kHz streaming standard, 44.1 kHz music",
                "Dual PC streaming: Gaming PC + stream PC, 0 performance loss",
                "Capture card: Elgato 4K60 Pro, AverMedia Live Gamer 4K",
                "NDI: Network Device Interface, stream over LAN to 2nd PC",
                "Audio interface: Focusrite Scarlett 2i2, XLR mics",
                "Microphone: Shure SM7B (needs Cloudlifter), Rode PodMic",
                "USB microphone: Blue Yeti, Elgato Wave 3, Rode NT-USB",
                "Noise gate: Cuts mic when quiet, -40 dB threshold",
                "Noise suppression: NVIDIA RTX Voice, Krisp, OBS plugin",
                "Compressor: Even out loud/quiet, -12 dB threshold, 3:1 ratio",
                "EQ: Equalization, boost 100-200 Hz bass, cut 3-5 kHz harsh",
                "De-esser: Reduce 's' sibilance, 5-10 kHz",
                "Webcam: Logitech C920/C922 budget, Brio 4K, Elgato Facecam",
                "DSLR camera: Sony Alpha, Canon EOS, HDMI capture",
                "Green screen: Chroma key, even lighting critical, Elgato collapsible",
                "Lighting: 3-point setup, key light front, fill side, back rim",
                "Key light: 2700-5500K temperature, softbox diffused",
                "Ring light: Frontal soft light, reduces shadows face",
                "Stream deck: Elgato 15/32 keys, macros scene switch",
                "Alerts: StreamElements, StreamLabs, custom sounds/images",
                "Overlays: Nerd or Die, Own3d, custom Photoshop/Figma",
                "Chat bot: Nightbot, StreamElements, mod commands",
                "TTS: Text-to-Speech donations, CJK character support",
            ],
            "virtualization_containers": [
                "Hypervisor Type-1: Bare metal, ESXi, Hyper-V Server, Proxmox",
                "Hypervisor Type-2: Hosted, VMware Workstation, VirtualBox",
                "Hyper-V: Windows built-in, Pro/Enterprise, enable Windows Features",
                "WSL2: Linux kernel Windows, better than VM performance",
                "VirtualBox: Free cross-platform, USB pass-through, snapshots",
                "VMware Workstation: Paid, best performance, Pro features",
                "VMware Workstation Player: Free personal use, limited features",
                "Nested virtualization: VM inside VM, AMD-V/VT-x required",
                "CPU passthrough: Dedicate cores to VM, pinning affinity",
                "GPU passthrough: VFIO IOMMU, gaming VM Linux host",
                "vTPM: Virtual TPM 2.0, Windows 11 VM requirement",
                "VM disk types: Fixed size faster, dynamic grows",
                "Snapshot: Save VM state, rollback, chain performance impact",
                "Linked clone: Shares base disk, saves space",
                "Full clone: Independent VM, portable",
                "Network modes: NAT (internet), Bridged (LAN IP), Host-only (isolated)",
                "Shared folders: Host↔Guest file sharing, slower than native",
                "USB passthrough: Devices to VM, exclusive access",
                "Docker: Containerization, lightweight vs VM",
                "Docker Desktop: Windows/Mac GUI, WSL2 backend",
                "Container: Isolated process, shares kernel, seconds start",
                "Image: Container template, layered filesystem",
                "Dockerfile: Build script, FROM/RUN/COPY/CMD",
                "Docker Compose: Multi-container YAML, orchestration",
                "Kubernetes: Container orchestration, production scaling",
                "Proxmox: Open-source hypervisor, KVM + LXC containers",
                "ESXi: VMware enterprise, vCenter management",
                "Hyper-V Server: Free standalone, no Windows license",
                "Memory ballooning: Dynamic RAM allocation VMs",
                "CPU reservation: Guaranteed MHz minimum VM",
                "Storage thin provisioning: Allocate space on-demand",
            ],
            "linux_windows_dual_boot": [
                "Dual boot: Separate partitions, GRUB bootloader choice",
                "Install order: Windows first, Linux second (GRUB detects Windows)",
                "UEFI vs Legacy: UEFI modern, Secure Boot disable for Linux",
                "Partition scheme: EFI (500MB), Windows (C:), Linux / (50GB+), swap (RAM size), /home (rest)",
                "Ubuntu: Beginner-friendly, LTS support 5 years, 22.04/24.04",
                "Linux Mint: Windows-like, Cinnamon DE, based Ubuntu",
                "Pop!_OS: Gaming focus, NVIDIA drivers included, System76",
                "Fedora: Cutting-edge, 6-month releases, GNOME default",
                "Arch Linux: DIY install, rolling release, AUR packages",
                "Manjaro: Arch user-friendly, graphical installer",
                "EXT4: Linux filesystem, journaling, reliable",
                "BTRFS: Copy-on-write, snapshots, Fedora default",
                "NTFS: Windows, Linux can read/write (ntfs-3g)",
                "Shared partition: exFAT or NTFS for files both OS",
                "GRUB timeout: 5-10 seconds, edit /etc/default/grub",
                "GRUB themes: Customize bootloader, install Vimix/Poly-dark",
                "Windows boot repair: Boot Linux USB, Boot-Repair tool",
                "Time sync: Windows uses local time, Linux UTC, fix registry",
                "Windows fast startup: Disable, corrupts NTFS for Linux",
                "Swap file vs partition: Partition traditional, file flexible",
                "Hibernation: Swap size = RAM + 10% for hibernation",
                "Wine: Run Windows apps on Linux, compatibility layer",
                "Proton: Steam Windows games on Linux, Valve development",
                "Lutris: Game launcher, installers GOG/Epic/Battle.net",
                "GPU drivers: NVIDIA proprietary, AMD open-source Mesa",
                "Desktop Environment: GNOME (heavy), KDE (customizable), XFCE (light)",
                "Window Manager: i3 (tiling), Openbox (floating), minimal",
                "Package manager: apt (Debian/Ubuntu), dnf (Fedora), pacman (Arch)",
                "Flatpak: Universal packages, sandboxed, Flathub repository",
                "Snap: Ubuntu packages, containerized, slower startup",
                "AppImage: Portable executables, no install required",
            ]
        }

        # =============================================================================
        # DÉSACTIVÉ: quick_responses (177 réponses scriptées hardcodées)
        # Remplacé par DynamicResponseGenerator pour génération conversationnelle
        # Code conservé pour référence mais NON UTILISÉ
        # =============================================================================
        self.quick_responses_DEPRECATED_DO_NOT_USE = {
            "bonjour": " Bonjour ! Je suis votre assistant IA de maintenance informatique. Comment puis-je vous aider aujourd'hui ?",
            "salut": " Salut ! Que puis-je faire pour vous aider avec votre ordinateur ?",
            "hello": " Hello! How can I help you today? (Je peux répondre en français aussi!)",
            "aide": " **Je peux vous aider avec:**\n\n **Diagnostic**: Analyser problèmes matériels (CPU, RAM, disque, températures)\n **Optimisation**: Améliorer performances et vitesse système\n **Sécurité**: Protéger contre virus, malwares, ransomwares\n **Réseau**: Résoudre problèmes WiFi, Ethernet, connexion lente\n **Stockage**: Gérer disques, SSD, HDD, espace libre\n **Refroidissement**: Surveiller températures, ventilateurs\n **Écrans bleus**: Diagnostiquer BSOD et crashes\n **Audio**: Réparer problèmes de son\n **Performances gaming**: Optimiser FPS et latence\n\n**Posez-moi une question ou tapez un mot-clé!**",
            "merci": " De rien ! N'hésitez pas si vous avez d'autres questions. Bonne maintenance !",
            "problème": " **Décrivez votre problème en détail**\n\nType de problème:\n•  **Lenteur** générale ou au démarrage?\n•  **Surchauffe** CPU/GPU?\n•  **Écran bleu** (BSOD)?\n•  **Internet** lent ou déconnecté?\n•  **Pas de son** ou grésillements?\n•  **Disque** plein ou lent?\n•  **Jeux** qui lag ou freezent?\n•  **Arrêts** inattendus?\n\nDonnez-moi des détails et je vous guiderai !",

            "lenteur": " **Diagnostic Lenteur Système**\n\n**1. Vérification immédiate** (Ctrl+Shift+Esc)\n   • CPU > 90% constant? = Processus à tuer ou malware\n   • RAM > 85%? = Ajoutez RAM ou fermez apps\n   • Disque 100%? = Désactivez superfetch ou disque défaillant\n\n**2. Démarrage lent**\n   • Task Manager > Démarrage: Désactivez tout sauf antivirus\n   • Visez < 10 programmes au boot\n\n**3. Navigation lente**\n   • Nettoyage disque: supprimez fichiers temp\n   • Wise Care 365: nettoyage complet\n   • Vérifiez espace libre > 15%\n\n**4. Toujours lent après?**\n   • SSD upgrade = amélioration 300-500%\n   • +8GB RAM si < 16GB total\n\n**Voulez-vous des étapes détaillées?**",

            "surchauffe": " **Guide Surchauffe Complète**\n\n**Températures NORMALES:**\n• CPU idle: 30-45°C, charge: 60-80°C ( > 85°C)\n• GPU idle: 30-50°C, charge: 60-85°C ( > 90°C)\n\n**Diagnostic (HWMonitor):**\n1. Lancez HWMonitor depuis page Diagnostic\n2. Notez températures max CPU/GPU\n\n**Solutions par température:**\n **70-80°C**: Normal sous charge intense\n **80-90°C**: Nettoyage urgent requis\n **> 90°C**: DANGER - Arrêtez PC immédiatement\n\n**Actions correctrices:**\n1. **Nettoyage** (air comprimé, pas d'aspirateur!)\n   • Ventilateurs CPU/GPU\n   • Grilles aération boîtier\n   • Radiateurs\n\n2. **Vérifications**\n   • Tous ventilateurs tournent?\n   • Flux d'air: entrée avant, sortie arrière/haut\n   • Câbles ne bloquent pas flux?\n\n3. **Pâte thermique**\n   • Si > 2 ans: remplacez (Artic MX-4, Thermal Grizzly)\n   • Application: grain riz au centre CPU\n\n4. **Upgrades**\n   • Ventirad aftermarket (Hyper 212, Noctua NH-D15)\n   • Ventilateurs boîtier additionnels\n   • Amélioration flux d'air\n\n**Laptop surchauffe?**\n• Support ventilé obligatoire\n• Ne posez JAMAIS sur lit/tissu\n• Undervolt CPU avec ThrottleStop (-100mV)\n\n**Toujours trop chaud? = RMA ou réparation pro**",

            "virus": " **Protection Anti-Malware Complète**\n\n**SCAN IMMÉDIAT:**\n1. **Malwarebytes** (Page Diagnostic)\n   • Scan threat: 15-30 min\n   • Supprimez tout ce qui est détecté\n\n2. **AdwCleaner** (Page Diagnostic)\n   • Supprime adwares, toolbars, PUPs\n   • Scan rapide: 5 min\n\n3. **Spybot Search & Destroy**\n   • Anti-spyware complémentaire\n   • Immunisation navigateurs\n\n**Windows Defender:**\n• Paramètres > Sécurité Windows\n• Protection temps réel: ACTIVÉE\n• Scan complet hebdomadaire\n\n**PRÉVENTION:**\n Mises à jour Windows automatiques\n uBlock Origin (bloqueur pub navigateur)\n Pas de logiciels piratés\n Vérifier extensions navigateur suspectes\n Sauvegardes régulières (règle 3-2-1)\n\n**Signes d'infection:**\n• Pop-ups intempestifs\n• Page d'accueil modifiée\n• Ralentissements soudains\n• Processus inconnus (Task Manager)\n• Programmes qui s'installent seuls\n\n**Infection sévère?**\n→ Format + réinstallation Windows propre",

            "internet": " **Diagnostic Réseau Complet**\n\n**Test rapide:**\n1. Fonctionne sur autres appareils?\n   • Oui = Problème PC\n   • Non = Problème routeur/FAI\n\n**Si problème PC:**\n```cmd\nipconfig /release\nipconfig /renew\nipconfig /flushdns\nnetsh winsock reset\n```\n*Redémarrez après ces commandes*\n\n**Si problème routeur:**\n1. Déconnectez routeur 30 sec\n2. Reconnectez\n3. Attendez 2 min\n4. Testez\n\n**WiFi lent?**\n• 5GHz > 2.4GHz (si proche routeur)\n• Canal optimal: 1, 6 ou 11 (2.4GHz)\n• WiFi Analyzer pour trouver canal libre\n• Obstacles: murs épais réduisent signal\n\n**Ethernet vs WiFi:**\n• Ethernet = toujours mieux (latence, stabilité)\n• Powerline = alternative si Ethernet impossible\n\n**Optimisations:**\n• DNS Cloudflare: 1.1.1.1 / 1.0.0.1\n• DNS Google: 8.8.8.8 / 8.8.4.4\n• QoS routeur: priorisez gaming/streaming\n• Désactivez Windows Update download (temporaire)\n\n**Test vitesse:**\n• Fast.com (Netflix)\n• Speedtest.net (Ookla)\n• Comparez avec forfait FAI\n\n**Débit < 50% forfait?**\n→ Contactez FAI (problème ligne)",

            "écran bleu": " **Diagnostic BSOD (Blue Screen Of Death)**\n\n**1. NOTEZ LE CODE ERREUR!**\nExemples courants:\n• `SYSTEM_SERVICE_EXCEPTION` = Pilote fautif\n• `IRQL_NOT_LESS_OR_EQUAL` = Pilote/RAM\n• `PAGE_FAULT_IN_NONPAGED_AREA` = RAM défaillante\n• `DRIVER_IRQL_NOT_LESS_OR_EQUAL` = Pilote réseau\n• `MEMORY_MANAGEMENT` = RAM/fichier échange\n• `CRITICAL_PROCESS_DIED` = Système corrompu\n\n**2. Outil d'analyse**\n• BlueScreenView: Lit dumps mémoire\n• Identifie pilote/fichier fautif\n• Téléchargez NirSoft BlueScreenView\n\n**3. Solutions par cause:**\n\n**Pilotes:**\n• Mettez à jour GPU, chipset, réseau, audio\n• Site fabricant carte mère/GPU\n• Driver Booster (avec précaution)\n\n**RAM:**\n• MemTest86: bootable USB\n• 8+ passes, 0 erreur accepté\n• Testez 1 barrette à la fois\n• RAM défectueuse = RMA\n\n**Overclocking:**\n• Désactivez OC CPU/GPU/RAM\n• Retour fréquences stock BIOS\n• Testez stabilité\n\n**Disque:**\n```cmd\nchkdsk C: /f /r\n```\n*Redémarrage nécessaire*\n\n**Système:**\n```cmd\nsfc /scannow\nDISM /Online /Cleanup-Image /RestoreHealth\n```\n\n**4. En dernier recours:**\n• Point de restauration Windows\n• Réinstallation Windows propre\n• Sauvegardez AVANT!\n\n**BSOD sous charge = surchauffe possible**\n→ Vérifiez températures avec HWMonitor",

            "ram": " **Diagnostic Mémoire RAM**\n\n**Utilisation actuelle:**\n• Task Manager > Performance > Mémoire\n• < 50%: Excellent\n• 50-80%: Normal\n• > 80%: Ajoutez RAM!\n\n**Quantité recommandée 2024:**\n• Navigation: 8GB minimum\n• Gaming 1080p: 16GB\n• Gaming 1440p/4K: 32GB\n• Workstation (CAO, montage): 32-64GB\n\n**Test RAM (erreurs?):**\n1. Windows Memory Diagnostic\n2. MemTest86 (plus fiable)\n   • 8+ passes\n   • 0 erreur = OK\n   • 1+ erreur = RAM défectueuse\n\n**Optimisation RAM:**\n• Fermez programmes inutiles\n• Chrome = gouffre RAM (20 onglets = 2GB)\n• Désactivez démarrage automatique apps\n\n**Upgrade RAM:**\n• Même vitesse (MHz)\n• Même latence (CL)\n• Dual channel obligatoire (2x8GB > 1x16GB)\n• DDR4 3200MHz CL16 = sweet spot 2024\n• Activez XMP/DOCP dans BIOS!\n\n**Barrettes en panne?**\n• Testez une par une\n• Slots différents\n• RMA si défectueuse",

            "fps": " **Optimisation FPS Gaming**\n\n**Diagnostic basique:**\n1. FPS actuels vs attendus?\n2. Jeu spécifique ou tous?\n3. Baisse soudaine ou toujours?\n\n**Gains FPS immédiats:**\n\n**In-Game (50+ FPS):**\n• Baissez résolution (1440p→1080p)\n• Ombres: Moyen/Bas\n• Anti-aliasing: TAA ou désactivé\n• Ray-tracing: Désactivé (sauf RTX 4070+)\n• DLSS/FSR: Quality mode (gain 40%)\n\n**Windows (20+ FPS):**\n• Mode performances: Panneau > Alimentation\n• Game Mode: Activé (Paramètres > Jeux)\n• Game Bar: Désactivé si lag\n• Plein écran > Fenêtré\n\n**GPU (30+ FPS):**\n• Pilotes: Dernière version\n• NVIDIA: GeForce Experience > Game Ready\n• AMD: Adrenalin Edition\n• MSI Afterburner: OC léger (+10% FPS)\n\n**Monitoring:**\n• MSI Afterburner + RivaTuner\n• GPU 99% = Normal (bon!)\n• CPU 99% = Bottleneck (upgrade CPU)\n• Températures > 85°C = Throttling\n\n**Upgrades rentables:**\n1. GPU (impact +200%)\n2. RAM 16GB→32GB (+15%)\n3. CPU si > 5 ans (+40%)\n4. SSD (temps chargement)\n\n**Stuttering/freezes?**\n• Vérifiez température\n• Fermez Chrome/Discord\n• Scan malware\n\n**Compétitif (144+ FPS)?**\n• G-Sync/FreeSync activé\n• Taux rafraîchissement écran: 144Hz+\n• Latence réseau: Ethernet obligatoire",

            # Plus de salutations et réponses conversationnelles
            "bonsoir": " Bonsoir ! Comment puis-je vous aider ce soir avec votre PC ?",
            "hey": " Hey ! Je suis là pour vous aider. Quel est votre problème ?",
            "coucou": " Coucou ! Que puis-je faire pour vous aujourd'hui ?",
            "ça va": " Ça va très bien, merci ! Et votre PC, il va bien ? Des problèmes à résoudre ?",
            "comment vas-tu": " Je vais bien ! Prêt à résoudre tous vos problèmes informatiques. Comment puis-je vous aider ?",

            # Remerciements variés
            "merci beaucoup": " Avec plaisir ! C'est un plaisir de vous aider. Revenez quand vous voulez !",
            "super": " Content que ça vous aide ! N'hésitez pas pour d'autres questions !",
            "parfait": " Parfait ! Si vous avez besoin d'autre chose, je suis là !",
            "génial": " Génial ! Ravi d'avoir pu vous aider !",
            "top": " Top ! Si d'autres questions, n'hésitez pas !",

            # Questions communes
            "pc lent": " **PC lent?** Plusieurs causes possibles:\n\n1. **Vérif immédiate**: Ctrl+Shift+Esc\n   • Disque 100%? = Problème disque\n   • RAM > 90%? = Pas assez RAM\n   • CPU 100%? = Processus problématique\n\n2. **Solutions rapides:**\n   • Désactivez programmes démarrage\n   • Nettoyage disque (Wise Care 365)\n   • Scan antivirus (Malwarebytes)\n   • Vérifiez température (HWMonitor)\n\n3. **Upgrade si nécessaire:**\n   • SSD = +400% vitesse\n   • +8GB RAM\n\nTapez 'lenteur' pour guide complet!",

            "crash": " **PC qui crash?** Plusieurs types:\n\n**Écran bleu (BSOD):**\n• Notez le code d'erreur\n• BlueScreenView pour analyse\n• Tapez 'écran bleu' pour détails\n\n**Freeze/freeze:**\n• Température trop élevée?\n• RAM défectueuse? (MemTest86)\n• Pilotes obsolètes?\n\n**Arrêt brutal:**\n• Alimentation insuffisante?\n• Surchauffe critique?\n• Défaut matériel?\n\n**Crash jeux seulement:**\n• Pilotes GPU à jour?\n• Overclocking instable?\n• Température GPU?\n\nDonnez-moi plus de détails!",

            "freeze": " **PC qui freeze?**\n\n**Freezes courts (micro-stutters):**\n• Disque 100%: Superfetch/Windows Search\n• Pilotes obsolètes\n• Températures élevées\n\n**Freezes longs (30s+):**\n• HDD défaillant (CrystalDiskInfo)\n• RAM défectueuse (MemTest86)\n• Malware (Malwarebytes scan)\n\n**Freeze complet (reboot obligatoire):**\n• Surchauffe CPU/GPU\n• Overclocking instable\n• Alimentation défaillante\n• Pilote graphique corrompu\n\n**Actions immédiates:**\n1. HWMonitor: vérifiez températures\n2. Task Manager: processus anormal?\n3. Event Viewer: erreurs système?\n4. DDU + réinstall pilote GPU\n\nQuel type de freeze exactement?",

            "démarrage lent": " **Démarrage lent?**\n\n**Temps normal:**\n• SSD: 10-30 secondes\n• HDD: 30-120 secondes\n\n**Optimisations:**\n1. **Task Manager > Démarrage**\n   • Désactivez TOUT sauf antivirus\n   • Visez < 5 programmes activés\n\n2. **Fast Startup**\n   • Panneau > Options alimentation\n   • Paramètres avancés > Fast Startup\n\n3. **Services inutiles**\n   • services.msc\n   • Désactivez: Print Spooler si pas imprimante\n   • Télécopie, Bluetooth si non utilisé\n\n4. **BIOS**\n   • Désactivez boot logos\n   • Fast Boot: Enabled\n\n**Solution radicale:**\n→ Upgrade SSD = démarrage < 15 secondes!\n\nTemps de boot actuel?",

            "bruit": " **PC fait du bruit?**\n\n**Type de bruit:**\n\n**1. Ventilateur bruyant**\n• Normal sous charge\n• Anormal au repos = nettoyage requis\n• Aigu/vibration = roulement usé\n• **Solution**: Nettoyage ou remplacement ventilo\n\n**2. Coil whine (sifflement aigu)**\n• Provient GPU ou PSU\n• Normal mais désagréable\n• Pire sous charge\n• **Solution**: Limitez FPS ou changez PSU\n\n**3. Clics/grattements**\n•  DISQUE DUR EN PANNE!\n• Sauvegardez IMMÉDIATEMENT\n• Remplacez disque URGENT\n\n**4. Bourdonnement grave**\n• Alimentation (PSU)\n• Peut indiquer défaillance proche\n• Surveillez stabilité système\n\n**Quel type de bruit exactement?**",

            "batterie": " **Problème batterie laptop?**\n\n**Diagnostic:**\n```cmd\npowercfg /batteryreport\n```\nRapport dans C:\\Windows\\system32\\battery-report.html\n\n**Usure normale:**\n• 0-20% après 1 an: Excellent\n• 20-40% après 2 ans: Normal\n• 40-60% après 3 ans: Attendu\n• > 60%: Remplacement recommandé\n\n**Améliorer autonomie:**\n1. Mode économie d'énergie\n2. Luminosité 50%\n3. Désactivez RGB/Bluetooth inutile\n4. Fermez apps arrière-plan\n5. Undervolting CPU (ThrottleStop)\n\n**Calibration batterie:**\n1. Charge 100%\n2. Décharge complète 0%\n3. Recharge 100% sans interruption\n\n**Remplacement:**\n• Batterie 80€-200€ selon modèle\n• Possible vous-même si batterie externe\n\n**Tient combien de temps actuellement?**",

            "mise à jour": " **Problème mise à jour Windows?**\n\n**Erreur installation:**\n1. Windows Update Troubleshooter\n2. ```cmd\nnet stop wuauserv\nnet stop bits\nrd /s /q C:\\Windows\\SoftwareDistribution\nnet start wuauserv\nnet start bits\n```\n3. Relancez Windows Update\n\n**Mise à jour bloquée:**\n• Espace insuffisant? (20GB requis)\n• Désactivez temporairement antivirus\n• Update Assistant (Microsoft site)\n\n**Annuler mise à jour:**\n• Paramètres > Mise à jour > Historique\n• Désinstaller mises à jour\n\n**Empêcher mises à jour auto:**\n• gpedit.msc (Pro seulement)\n• Ou désactivez Windows Update (services.msc)\n\n**Pilotes GPU:**\n• NVIDIA: GeForce Experience\n• AMD: Adrenalin Software\n• Intel: Driver Support Assistant\n\nQuel type de mise à jour?",

            "jeu lag": " **Jeu qui lag?**\n\n**Diagnostic:**\n1. FPS bas OU latence haute?\n2. Jeu spécifique ou tous?\n3. Lag depuis toujours ou récent?\n\n**FPS bas (< 60):**\n• Baissez paramètres graphiques\n• Pilotes GPU à jour\n• MSI Afterburner: vérifiez usage GPU/CPU\n• Température > 85°C = throttling\n→ Tapez 'fps' pour guide complet\n\n**Latence/Ping élevé:**\n• Ethernet vs WiFi\n• Fermez téléchargements\n• QoS routeur\n• Serveur jeu proche géographiquement\n→ Tapez 'internet' pour diagnostic réseau\n\n**Stuttering (micro-lags):**\n• Fermez Chrome/Discord\n• Scan malware\n• Température\n• Shader cache activé\n\n**Config PC?** (CPU/GPU/RAM)",

            "windows 10": "🪟 **Windows 10**\n\nVersion actuelle support jusqu'en octobre 2025.\n\n**Optimisations W10:**\n• Désactivez Cortana\n• Limitez télémétrie (O&O ShutUp10++)\n• Game Mode activé\n• Débloat scripts\n\n**Upgrade Windows 11?**\nPROS:\n• Meilleures perfs gaming (10-15%)\n• DirectStorage\n• Auto HDR\n\nCONS:\n• Requiert TPM 2.0\n• Menu démarrer controversé\n• Barre des tâches moins flexible\n\nGardez W10 si:\n• CPU pré-2018\n• Pas TPM 2.0\n• Vous aimez l'interface\n\nQuelle question spécifique?",

            "windows 11": "🪟 **Windows 11**\n\n**Avantages:**\n• +10-15% FPS gaming\n• DirectStorage (chargements rapides)\n• Auto HDR\n• Interface moderne\n\n**Inconvénients:**\n• Requiert TPM 2.0 + CPU récent\n• Menu démarrer controversé\n• Barre tâches moins flexible\n• Android apps (mais limité)\n\n**Bypass restrictions TPM:**\n• Possible mais non recommandé\n• Pas de mises à jour sécurité garanties\n\n**Optimisations W11:**\n• Désactivez widgets\n• Limitez télémétrie\n• StartAllBack pour menu classique\n• ExplorerPatcher pour taskbar classique\n\n**Retour W10 possible 10 jours après upgrade**\n\nVous avez quel CPU?",

            "ssd": " **Question SSD?**\n\n**Upgrade HDD→SSD:**\n• +300-500% vitesse!\n• Boot 10-15 secondes\n• Jeux chargent 3-5x plus vite\n• Prix: 50€ (500GB) à 100€ (1TB)\n\n**Meilleurs SSD 2024:**\n• Samsung 980 Pro (Gen4)\n• WD Black SN850X\n• Crucial P5 Plus\n• Kingston KC3000\n\n**Installation:**\n1. Clone avec Macrium Reflect\n2. Ou install Windows propre\n3. IMPORTANT: Activez AHCI BIOS!\n\n**Optimisations SSD:**\n• TRIM activé (auto sur W10/11)\n• Ne JAMAIS défragmenter\n• 15-20% espace libre minimum\n• Désactivez indexation\n\n**Santé SSD:**\n• CrystalDiskInfo\n• Surveillez TBW (usure)\n\n**NVMe vs SATA:**\n• NVMe: 3500 MB/s (Gen4)\n• SATA: 550 MB/s max\n• Gaming: différence minime\n• Productivité: NVMe meilleur\n\nVotre question exacte?",

            "pilote": " **Problème pilote?**\n\n**Mise à jour pilotes:**\n\n**GPU (IMPORTANT!):**\n• NVIDIA: GeForce Experience\n• AMD: Adrenalin Software\n• Intel: Intel Driver Assistant\n• Fréquence: Mensuelle\n\n**Chipset:**\n• Site fabricant carte mère\n• AMD: AMD Chipset Drivers\n• Intel: Intel Chipset Device Software\n\n**Réseau:**\n• Gestionnaire périphériques\n• Ou site fabricant CM\n• Intel > Realtek (stabilité)\n\n**Audio:**\n• Realtek Audio Drivers\n• Site fabricant CM\n\n**Désinstallation propre GPU:**\n1. Téléchargez DDU (Display Driver Uninstaller)\n2. Mode sans échec\n3. DDU > Clean and restart\n4. Réinstallez pilote frais\n\n**Rollback pilote:**\n• Gestionnaire périphériques\n• Propriétés > Pilote\n• Restaurer pilote précédent\n\n**Quel périphérique?**",

            "formatage": " **Formatage Windows**\n\n** AVANT DE FORMATER:**\n1. **SAUVEGARDEZ TOUT!**\n   • Documents (Desktop, Documents, Pictures)\n   • Favoris navigateur\n   • Sauvegardes jeux (Steam Cloud?)\n   • Licences logiciels\n\n2. **Notez:**\n   • Clé Windows (ShowKeyPlus)\n   • Mots de passe\n   • Pilotes réseau (backup sur USB)\n\n**Méthodes:**\n\n**1. Réinitialisation Windows:**\n• Paramètres > Récupération\n• Conserver fichiers OU suppression totale\n• Réinstalle Windows, garde pilotes\n\n**2. Installation propre (recommandé):**\n• Créez USB boot (Media Creation Tool)\n• Bootez sur USB\n• Supprimez toutes partitions\n• Installation propre = PC neuf!\n\n**Après installation:**\n1. Windows Update\n2. Pilotes GPU/chipset/réseau\n3. Ninite pour logiciels essentiels\n4. Activez Windows\n\n**Durée: 1-2 heures**\n\nVous voulez formater pourquoi?",

            "installer": " **Installer un logiciel/jeu?**\n\n**Bonnes pratiques:**\n\n**1. Source fiable uniquement:**\n Site officiel éditeur\n Microsoft Store\n Steam/Epic/GOG\n Ninite (pack logiciels)\n Sites tiers/torrents = risque malware\n\n**2. Installation:**\n• Lisez options (refusez toolbars!)\n• Installation personnalisée\n• Décochez sponsors\n• Choisissez dossier (C: si SSD)\n\n**3. Après installation:**\n• Vérifiez démarrage auto (Task Manager)\n• Configurez logiciel\n• Raccourcis utiles?\n\n**Problèmes courants:**\n\n**\"Erreur 0x... installation\":**\n• Droits admin\n• Désactivez antivirus temporairement\n• Microsoft Visual C++ Redistributables\n• .NET Framework\n\n**\"Application ne se lance pas\":**\n• Pilotes GPU à jour?\n• DirectX à jour?\n• Compatibility mode?\n\n**Quel logiciel voulez-vous installer?**",

            # ========== 1000+ RÉPONSES RAPIDES SUPPLÉMENTAIRES ==========

            # Problèmes d'écran
            "écran noir": " **Écran noir?**\n\n**Au démarrage:**\n1. Mode sans échec (F8)\n2. DDU + réinstall pilote GPU\n3. Testez autre câble/port\n4. RAM mal insérée?\n\n**En jeu:**\n• Overclocking instable\n• Alimentation insuffisante\n• Température GPU > 90°C\n• Pilote GPU crash\n\n**Après mise à jour:**\n• Rollback pilote GPU\n• Point de restauration\n\nDétails du problème?",

            "écran bleu windows": " Tapez 'écran bleu' pour le guide complet BSOD!",
            "bsod": " Tapez 'écran bleu' pour le guide complet!",

            "pas d'image": " **Pas d'image?**\n\n**Vérifications:**\n1. Câble bien branché GPU (pas carte mère!)\n2. Monitor allumé + bon input (HDMI/DP)\n3. GPU bien inséré slot PCIe\n4. Connecteur alim GPU branché (6+2pin)\n5. Testez autre câble/port\n\n**LED debug carte mère?**\n• Blanc/Jaune = GPU\n• Rouge = CPU\n• Jaune = RAM\n\n**Beeps au démarrage?**\nCode erreur important!",

            "écran qui scintille": " **Scintillement écran?**\n\n**Causes:**\n• Refresh rate incorrect (60Hz vs 144Hz)\n• Câble défectueux (HDMI/DP)\n• Pilote GPU obsolète\n• Overclock moniteur instable\n• G-Sync/FreeSync mal configuré\n\n**Solutions:**\n1. Paramètres > Système > Affichage > Paramètres avancés\n2. Vérifiez refresh rate natif\n3. Testez autre câble\n4. DDU + pilote GPU frais\n5. Désactivez G-Sync temporairement",

            "2 écrans": " **Configuration dual monitor?**\n\n**Setup optimal:**\n1. Branchez les 2 sur GPU (pas carte mère!)\n2. Même refresh rate (sinon stutters)\n3. Windows + P > Étendre\n4. Clic droit bureau > Paramètres affichage\n5. Arrangez position physique\n\n**Gaming dual screen:**\n• Jeu sur moniteur principal\n• G-Sync sur primaire uniquement\n• Discord/YouTube sur secondaire\n\n**Problème?** Décrivez!",

            # Problèmes souris/clavier
            "souris qui lag": " **Souris qui lag?**\n\n**Gaming:**\n• Polling rate: 1000Hz\n• DPI: 800-1600 (pas 16000!)\n• Désactivez accélération Windows\n• Surface mousepad propre\n• Port USB 3.0 direct (pas hub)\n\n**Tous usages:**\n• DPC Latency Checker: pilote problème?\n• Enhanced Pointer Precision: OFF\n• Testez autre port USB\n• Driver souris officiel\n\n**Sans fil:**\n• Batterie faible?\n• Interférences WiFi 2.4GHz\n• Dongle trop loin",

            "clavier ne fonctionne pas": "⌨ **Clavier HS?**\n\n**USB:**\n1. Testez autre port\n2. Gestionnaire périph: réinstall\n3. Débranchez 30s puis rebranchez\n4. Mode sans échec = OK? Driver!\n\n**Sans fil:**\n• Batterie/piles\n• Re-pair Bluetooth\n• Dongle bien branché\n\n**Mécanique:**\n• Switch défectueux?\n• Liquide renversé? Nettoyage alcool isopropylique\n\n**Spécifiques touches?**\nSwitch à remplacer (hot-swap?)",

            "touches collent": "⌨ **Touches qui collent?**\n\n**Nettoyage:**\n1. Débranchez clavier\n2. Retirez keycaps (outil)\n3. Alcool isopropylique 99%\n4. Cotton-tige entre switches\n5. Air comprimé\n6. Séchage 30min\n\n**Liquide renversé?**\n• Débranchez IMMÉDIAT\n• Retournez clavier\n• Démontez si possible\n• Nettoyage alcool complet\n• Séchage 48h\n\n**Switches défectueux?**\n→ Remplacement (hot-swap = facile)",

            # Imprimante
            "imprimante": " **Problème imprimante?**\n\n**Ne se connecte pas:**\n• WiFi: même réseau que PC?\n• USB: testez autre port/câble\n• Services > Print Spooler > Redémarrer\n\n**N'imprime pas:**\n1. File d'attente: Annulez tout\n2. Redémarrez imprimante\n3. Pilote: réinstallez depuis site fabricant\n4. Testez page de test\n\n**Bourrage papier:**\n• Retirez délicatement\n• Nettoyez rouleaux\n• Papier correct (grammage)?\n\n**Qualité mauvaise:**\n• Nettoyage têtes (utilitaire)\n• Cartouches vides?\n• Paramètres qualité: Élevée\n\nMarque/modèle?",

            # WiFi/Bluetooth
            "pas de wifi": " **WiFi ne marche pas?**\n\n**Windows:**\n1. Avion mode: OFF\n2. WiFi activé (touche Fn + F...)\n3. Gestionnaire périph: Carte réseau activée\n4. Pilote WiFi: réinstallez\n\n**Routeur:**\n• Redémarrez (30sec débranché)\n• Autres appareils OK? = PC\n• SSID visible?\n• Bon mot de passe?\n\n**Laptop:**\n• Switch physique WiFi?\n• BIOS: WiFi enabled\n\n**Commandes:**\n```\nnetsh wlan show drivers\nnetsh wlan connect name=\"VotreSSID\"\n```",

            "bluetooth ne marche pas": " **Bluetooth HS?**\n\n**Activation:**\n1. Paramètres > Bluetooth: ON\n2. Mode avion: OFF\n3. Services: Bluetooth Support Service = Démarré\n4. Gestionnaire périph: Bluetooth activé\n\n**Pairing:**\n• Device en mode pairing (LED clignote)\n• Windows: + Ajouter Bluetooth\n• PIN si demandé (0000/1234 souvent)\n• Proche du PC (<5m)\n\n**Problèmes courants:**\n• Oubliez et re-pairez\n• Pilote Bluetooth: mise à jour\n• Interference USB 3.0?\n• Redémarrez PC + device\n\n**Toujours HS?**\nDongle Bluetooth USB externe (10€)",

            # Audio avancé
            "casque ne marche pas": " **Casque ne fonctionne pas?**\n\n**Jack 3.5mm:**\n1. Branché à fond?\n2. Bon port (casque = rose, micro = vert)\n3. Clic droit son > Périph lecture > Casque par défaut\n4. Testez façade ET arrière\n\n**USB:**\n• Autre port\n• Pilote: réinstall\n• Volume Windows + app\n\n**Bluetooth:**\n• Re-pair\n• Batterie?\n• Mode casque vs speaker\n\n**Dans jeu uniquement?**\n• Paramètres audio in-game\n• Discord overlay conflit?\n\n**Son faible?**\nVolume mixer: 100% partout",

            "micro ne marche pas": " **Micro HS?**\n\n**Test rapide:**\n1. Paramètres > Son > Entrée\n2. Parlez: barre bouge?\n3. Testez enregistreur vocal\n\n**Paramètres:**\n• Périphérique entrée par défaut\n• Volume micro: 80-100%\n• Boost micro: +10-20dB\n• Privacy: Micro autorisé apps\n\n**Discord/Teamspeak:**\n• Bon device sélectionné\n• Sensitivity ajustée\n• Noise suppression: test OFF\n\n**USB:**\n• Pilote: réinstall\n• Autre port USB\n\n**XLR (pro):**\n• Phantom +48V activé?\n• Gain préamp suffisant?",

            # Moniteur
            "moniteur 144hz": " **Moniteur 144Hz?**\n\n**Activation 144Hz:**\n1. Clic droit bureau > Paramètres affichage\n2. Paramètres avancés\n3. Taux rafraîchissement: 144Hz\n4. Si absent: mauvais câble!\n\n**Câbles compatibles:**\n DisplayPort 1.2+ (recommandé)\n HDMI 2.0+ (1080p 144Hz)\n DVI-D Dual Link (1080p 144Hz)\n HDMI 1.4 = 60Hz MAX\n VGA = poubelle\n\n**Vérification:**\n• testufo.com/frameskipping\n• Doit être FLUIDE\n\n**G-Sync/FreeSync:**\nActivez dans paramètres GPU (NVIDIA/AMD)",

            "g-sync": " **G-Sync/FreeSync?**\n\n**G-Sync (NVIDIA):**\n1. Moniteur compatible G-Sync\n2. DisplayPort (pas HDMI!)\n3. NVIDIA Control Panel\n4. Setup G-Sync\n5. Enable G-Sync\n6. Windowed + fullscreen\n\n**FreeSync (AMD):**\n1. Moniteur FreeSync\n2. AMD Settings\n3. Display\n4. AMD FreeSync: ON\n\n**Optimal setup:**\n• V-Sync: OFF (in-game)\n• G-Sync: ON\n• FPS cap: 3 below max (141 pour 144Hz)\n• Low Latency: Ultra (NVIDIA)\n\n**Test:**\nPendulum demo NVIDIA",

            # Overclocking
            "overclock cpu": " **Overclock CPU?**\n\n **RISQUES:**\n• Chaleur élevée\n• Instabilité système\n• Garantie annulée\n• Dégradation long terme\n\n**Prérequis:**\n• Ventirad aftermarket (Noctua, AIO)\n• Carte mère Z (Intel) / B/X (AMD)\n• PSU qualité suffisant\n• Monitoring (HWInfo)\n\n**Débutant:**\n1. BIOS > CPU Core Ratio\n2. +100-200MHz\n3. Voltage AUTO\n4. Test Prime95 10min\n5. Températures < 85°C\n6. Si stable: continuez\n\n**Avancé:**\n• Voltage manuel (1.25-1.35V)\n• LLC (Load Line Calibration)\n• AVX offset\n• Cache ratio\n\n**CPU?** (Ryzen/Intel?)",

            "overclock gpu": " **Overclock GPU?**\n\n**MSI Afterburner (gratuit):**\n1. Core Clock: +50MHz\n2. Memory: +100MHz\n3. Apply\n4. Test jeu/3DMark\n5. Stable? +50/+100 encore\n6. Crash? Reculez -25MHz\n\n**Optimal:**\n• Core: +100-200MHz typical\n• Memory: +400-800MHz (GDDR6)\n• Power Limit: +10-20%\n• Temp Limit: 83-85°C\n• Fan curve: Custom (aggressive)\n\n**Test stabilité:**\n• FurMark 10min (pas trop long!)\n• Heaven Benchmark 20min\n• Vos jeux 2h+\n\n**Gains:**\n+5-15% FPS gratuits!\n\n**GPU?** (RTX/RX?)",

            "undervolt": " **Undervolting CPU/GPU?**\n\n**Avantages:**\n Moins chaleur (10-20°C)\n Moins bruit\n Performances = identiques\n Consommation réduite\n Sans risque (stable ou crash)\n\n**CPU (Intel):**\n• ThrottleStop\n• Voltage offset: -100mV départ\n• Test stability\n• Montez si crash\n\n**CPU (AMD Ryzen):**\n• Ryzen Master\n• Curve Optimizer\n• -10 à -30 all cores\n\n**GPU:**\n• MSI Afterburner\n• Curve voltage (Ctrl+F)\n• Aplatir courbe\n• 900mV @ fréquence boost\n\n**Laptop = ESSENTIEL!**\n-20°C facile\n\nCPU/GPU?",

            # Streaming
            "obs": " **OBS Studio setup?**\n\n**Configuration optimale:**\n\n**Sortie > Streaming:**\n• Bitrate: 6000 (Twitch) / 8000 (YouTube)\n• Encoder: NVENC (GPU) ou x264 (CPU)\n• Preset: Quality (NVENC) / Medium (x264)\n• Profile: High\n• Keyframe: 2s\n\n**Vidéo:**\n• Base: 1920x1080\n• Output: 1920x1080 (ou 1280x720 si lag)\n• FPS: 60\n\n**Audio:**\n• Bitrate: 160kbps\n• Desktop + Micro séparés\n\n**Lag stream?**\n• Baissez résolution 720p\n• Preset: Performance\n• Bitrate: 3000-4000\n\n**Besoin aide setup complète?**",

            "streaming": " **Streaming Twitch/YouTube?**\n\n**Logiciels:**\n• OBS Studio (gratuit, pro)\n• Streamlabs OBS (débutant)\n• XSplit (payant, facile)\n\n**Requis PC:**\n• Upload: 10+ Mbps\n• GPU: GTX 1650+ (NVENC)\n• CPU: 6+ cores si x264\n• RAM: 16GB minimum\n• Dual monitor recommandé\n\n**Setup basique:**\n1. Compte Twitch/YT\n2. Stream key\n3. OBS: Paramètres stream\n4. Scènes: Jeu + Webcam\n5. Overlay (StreamElements)\n6. Chat (chatbot)\n\n**Tapez 'obs' pour config détaillée!**",

            # Carte graphique spécifique
            "rtx 4090": " **RTX 4090 - BÊTE ABSOLUE**\n\n**Specs:**\n• 24GB GDDR6X\n• 16384 CUDA cores\n• 450W TDP (!!)\n\n**Requis:**\n• PSU: 1000W+ (80+ Gold)\n• Câble: 3x 8pin ou 1x 12VHPWR\n• Boîtier: 350mm+ clearance\n• Airflow: ESSENTIEL\n\n**Performances:**\n• 4K 120+ FPS Ultra\n• 1440p 200+ FPS\n• Ray-tracing native fluide\n• DLSS 3 = magic\n\n**Problèmes courants:**\n• Câble 12VHPWR: vérifiez connexion!\n• Sag GPU: Support bracket\n• Températures: Normal 70-80°C\n• Coil whine: Cap FPS aide\n\n**Vous avez une 4090?**",

            "rtx 4070": " **RTX 4070 - Sweet Spot 2024**\n\n**Specs:**\n• 12GB GDDR6X\n• 5888 CUDA cores  \n• 200W TDP\n\n**Requis:**\n• PSU: 650W+\n• Câble: 1x 8pin\n\n**Performances:**\n• 1440p 144+ FPS High\n• 1080p 200+ FPS Ultra\n• DLSS 3: +60% FPS\n• Ray-tracing: Activable\n\n**vs 4070 Ti:**\n• 4070 Ti: +15% perfs\n• 4070 Ti: +150€\n• 4070: Meilleur rapport qualité/prix\n\n**Optimal pour:**\n• Gaming 1440p compétitif\n• Content creation\n• Budget raisonnable\n\nVous hésitez?",

            "rx 7900 xtx": " **RX 7900 XTX - Monstre AMD**\n\n**Specs:**\n• 24GB GDDR6\n• 6144 Stream processors\n• 355W TDP\n\n**Requis:**\n• PSU: 850W+\n• Câbles: 2x 8pin\n\n**Performances:**\n• 4K 80-100 FPS Ultra\n• 1440p 165+ FPS\n• Rasterization: Égale 4080\n• Ray-tracing: Moins bon NVIDIA\n\n**vs RTX 4080:**\n• Raster: XTX = 4080\n• RT: 4080 +30%\n• DLSS vs FSR: DLSS gagne\n• Prix: XTX -200€\n\n**Choix AMD si:**\n• Budget optimisé\n• Pas RT priority\n• VRAM 24GB utile (AI, 3D)\n\n**Vous avez XTX?**",

            # Processeurs
            "ryzen 5 7600": " **Ryzen 5 7600 - Gaming King Budget**\n\n**Specs:**\n• 6 cores / 12 threads\n• Base 3.8GHz, Boost 5.1GHz\n• AM5 (DDR5)\n• 65W TDP\n\n**Gaming:**\n• 1080p: RTX 4070 = 0 bottleneck\n• 1440p: Parfait\n• 4K: GPU-bound anyway\n\n**Requis:**\n• Carte mère: B650\n• RAM: DDR5 6000MHz CL30\n• Ventirad: Wraith suffisant (ou upgrade)\n\n**vs Alternatives:**\n• i5-13400F: Similaire, moins cher\n• 7600X: +200MHz, +30€, pas worth\n• 7700: Créa OK, gaming +5%\n\n**Meilleur CPU gaming <200€**\n\nVous hésitez?",

            "intel i5 13400f": " **i5-13400F - Best Value 2024**\n\n**Specs:**\n• 10 cores (6P+4E) / 16 threads\n• Turbo 4.6GHz\n• LGA1700 (DDR4/DDR5)\n• 65W base, 148W turbo\n• PAS de iGPU (F = GPU requis!)\n\n**Gaming:**\n• 1080p 144+fps: Parfait\n• Paire RTX 4060-4070\n• 0 bottleneck 1440p+\n\n**Requis:**\n• CM: B660/B760 suffisant\n• RAM: DDR4 3200MHz OK (économise!)\n• Ventirad: Tour aftermarket (stock faible)\n\n**vs 13600K:**\n• 13600K: +20% perfs\n• 13600K: +100€ + Z690 +50€\n• 13400F: Meilleur €/FPS\n\n**Top choix budget gaming**",

            # RAM
            "ddr4 vs ddr5": " **DDR4 vs DDR5 - Lequel choisir?**\n\n**DDR4:**\n Moins cher (100€ 32GB)\n Compatible vieux CPU\n 3200-3600MHz suffisant gaming\n Latence meilleure\n Pas futur-proof\n\n**DDR5:**\n Futur-proof (AM5, LGA1700)\n 6000-7200MHz\n Créa/productivité +10-15%\n Requis Ryzen 7000/Intel 13th+\n Cher (150€+ 32GB)\n Latence élevée\n\n**Gaming 2024:**\n• DDR4: Assez! 1-3% différence\n• DDR5: Si nouveau build AM5/1700\n\n**Recommendation:**\n• Budget? DDR4 3200 CL16\n• Nouveau? DDR5 6000 CL30\n• Intel 12th? DDR4 (B660)\n• Ryzen 7000? DDR5 obligé\n\nVotre CPU?",

            "combien de ram": " **Quantité RAM nécessaire?**\n\n**2024:**\n• 8GB: Minimum absolu (limite!)\n• 16GB: Standard gaming/bureautique \n• 32GB: Gaming + multitâche/stream \n• 64GB: Workstation/3D/vidéo pro\n• 128GB+: Serveurs/virtualisation\n\n**Détails usage:**\n\n**Gaming:**\n• Compétitif pur: 16GB OK\n• AAA moderne: 16GB requis\n• Jeu + Discord + Chrome: 32GB!\n• Jeu + Stream: 32GB minimum\n\n**Créa:**\n• Photo (Photoshop): 16GB\n• Vidéo (Premiere): 32GB\n• 3D (Blender): 32-64GB\n• After Effects: 64GB\n\n**Actuel RAM?** Ctrl+Shift+Esc",

            # Refroidissement
            "refroidissement liquide": " **Watercooling AIO?**\n\n**Types:**\n\n**120mm (1 fan):**\n Pire que ventirad tour\n Évitez\n\n**240mm (2 fans):**\n CPUs 65-105W\n Compact\n ~80€\n\n**280mm (2x140mm):**\n CPUs 125-150W\n Sweet spot perfs/prix\n\n**360mm (3x140mm):**\n CPUs 150W+\n i9/Ryzen 9 overclock\n Cher (150€+)\n\n**Top AIO 2024:**\n• Arctic Liquid Freezer II (best €/perf)\n• Corsair iCUE Elite\n• NZXT Kraken\n• Lian Li Galahad\n\n**vs Air:**\n• AIO: Look, clearance RAM\n• Air: Fiable, silent, moins cher\n• Perfs 240mm = NH-D15\n\nCPU?",

            "pate thermique": " **Pâte thermique?**\n\n**Quand changer:**\n• Tous les 2-3 ans\n• Si températures anormales\n• Après démontage ventirad\n• Pâte sèche visible\n\n**Top pâtes 2024:**\n\n**Budget:**\n• Arctic MX-4 (5€) \n• Noctua NT-H1 (8€)\n\n**Enthusiast:**\n• Thermal Grizzly Kryonaut (12€)\n• Noctua NT-H2 (10€)\n\n**Extreme:**\n• Thermal Grizzly Conductonaut (liquide métal)\n Conducteur = DANGER court-circuit\n Experts only!\n\n**Application:**\n1. Nettoyez IHS (alcool 99%)\n2. Grain de riz au centre\n3. Serrez ventirad\n4. Pression répartit\n\n**PAS:**\n Trop = pire\n Croix/X = myth\n Étaler = air bubbles\n\n-5-10°C possible!",

            # Stockage
            "cloner disque": " **Cloner HDD vers SSD?**\n\n**Logiciels gratuits:**\n\n**Macrium Reflect** (recommandé):\n1. Téléchargez gratuit\n2. Branchez nouveau SSD\n3. Create backup > Clone disk\n4. Source: HDD | Dest: SSD\n5. Attendez (30min-2h)\n6. Redémarrez\n7. BIOS: Boot priority SSD\n8. Formatez HDD ancien\n\n**Alternatives:**\n• Samsung Data Migration (SSDs Samsung)\n• Clonezilla (avancé, gratuit)\n• EaseUS Todo (freemium)\n\n**Espace insuffisant?**\n→ Installation propre Windows (meilleur)\n\n**Après clonage:**\n• TRIM activé (auto W10/11)\n• Désindexation SSD\n• HDD = stockage data\n\nBesoin aide?",

            "partition": " **Gérer partitions?**\n\n**Windows natif:**\n1. Win+X > Gestion disques\n2. Clic droit partition\n3. Options: Réduire, Étendre, Formater\n\n**Cas d'usage:**\n\n**Créer partition data:**\n• C: = System (100-150GB)\n• D: = Games/Data (reste)\n• Sépare system et données\n\n**Fusionner partitions:**\n1. Sauvegardez données!\n2. Supprimez partition droite\n3. Étendez partition gauche\n\n**Logiciels avancés:**\n• MiniTool Partition Wizard\n• EaseUS Partition Master\n• GParted (Linux live USB)\n\n** Partition = perte données!**\nSauvegardez AVANT!\n\nQue voulez-vous faire?",

            "disque externe": " **Disque externe?**\n\n**Usage:**\n\n**Backup:**\n• HDD 2-4TB suffisant\n• Pas besoin vitesse\n• 50-80€\n• Marques: WD, Seagate\n\n**Transport données:**\n• SSD externe 500GB-1TB\n• Rapide, résistant\n• 80-150€\n• Samsung T7, SanDisk Extreme\n\n**Gaming (PS5/Xbox):**\n• SSD NVMe externe\n• USB 3.2 Gen 2 minimum\n• Temps chargement!\n\n**Format:**\n• Windows: NTFS\n• Mac+Win: exFAT\n• Linux: ext4\n\n**Vitesse:**\n• USB 3.0: 100-150 MB/s\n• USB 3.1: 400-500 MB/s\n• Thunderbolt 3: 3000 MB/s\n\n**Usage?**",

            # Alimentation
            "psu": " **Alimentation (PSU)?**\n\n**Calcul wattage:**\n• GPU TDP + CPU TDP + 150W\n• Ex: RTX 4070 (200W) + i5 (150W) + 150W = 500W\n• Prenez +100W marge = **650W**\n\n**Certifications:**\n• 80+ Bronze: Budget\n• 80+ Gold: Recommandé \n• 80+ Platinum: Enthusiast\n• 80+ Titanium: Overkill\n\n**Tier List 2024:**\n\n**Tier A (excellent):**\n• Corsair RM/RMx/RMe\n• Seasonic Focus GX\n• EVGA SuperNOVA G6\n\n**Tier B (bon):**\n• Corsair CV/CX\n• Be Quiet! Pure Power\n• Cooler Master MWE Gold\n\n**À ÉVITER:**\n No-name brands\n < 80+ Bronze\n \"Gaming\" marketing\n\n**Config?** (CPU/GPU)",

            "modulaire": " **PSU Modulaire?**\n\n**Types:**\n\n**Non-modulaire:**\n• Tous câbles fixes\n• Moins cher\n Cable management difficile\n Encombré\n\n**Semi-modulaire:**\n• 24pin + CPU fixes\n• PCIe/SATA détachables\n Prix OK\n Assez flexible\n\n**Full modulaire:**\n• Tout détachable\n Clean build\n Airflow optimal\n +20-30€\n\n**Recommendation:**\n• Budget? Non-modulaire OK\n• Build propre? Semi minimum\n• Perfectionniste? Full\n\n**Cable extensions:**\n→ Esthétique (Cablemod, 30-50€)",

            # Boîtier
            "boitier": " **Choisir boîtier?**\n\n**Formats:**\n\n**Mini-ITX:**\n• Très compact (< 20L)\n• 1x GPU, 1x SSD\n Airflow limité\n Cher\n\n**Micro-ATX:**\n• Compact (30-40L)\n• 2x GPU, 2x SSD\n Bon compromis\n\n**ATX (Mid-Tower):**\n• Standard (50-70L)\n• 3x GPU, 4+ SSD\n Meilleur airflow \n Plus simple build\n\n**Full Tower:**\n• Énorme (80L+)\n• Multi-GPU, custom loop\n Trop pour 99% users\n\n**Critères importants:**\n1. Airflow (mesh front!)\n2. Clearance ventirad/GPU\n3. Cable management\n4. Filtres poussière\n5. USB-C front?\n\n**Top 2024:**\n• Fractal Torrent (airflow king)\n• Lian Li O11 Dynamic\n• NZXT H7\n• Be Quiet! Pure Base 500DX\n\nBudget?",

            # Windows spécifique
            "activation windows": " **Activer Windows?**\n\n**Légal:**\n\n**1. Licence OEM:**\n• Liée à carte mère\n• Pas transférable\n• Pas de support Microsoft\n• 10-20€ (revendeurs)\n\n**2. Licence Retail:**\n• Transférable\n• Support Microsoft\n• 100-150€ officiel\n\n**3. Licence Education:**\n• Si étudiant/prof\n• Gratuit via école\n• Vérifiez éligibilité\n\n**Vérifier activation:**\n```\nslmgr /xpr\n```\n\n** Je ne peux pas recommander:**\n• KMS tools\n• Cracks\n• Keys volées\n= Risques malware + illégal\n\n**Désactivé = Watermark + limite perso**\nPas bloquant fonctionnel\n\nVous avez licence?",

            "réinstaller windows": " **Réinstaller Windows propre?**\n\n** SAUVEGARDEZ D'ABORD!**\n• Documents, Images, Vidéos\n• Favoris navigateur (export)\n• Sauvegardes jeux\n• Licences logiciels\n• Clé Windows (ShowKeyPlus)\n\n**Méthode:**\n\n**1. USB bootable (8GB+):**\n• Media Creation Tool Microsoft\n• Télécharge ISO Windows 10/11\n• Créé USB boot automatique\n\n**2. Installation:**\n1. Branchez USB\n2. Redémarrez\n3. F12/Del > Boot menu\n4. Sélectionnez USB\n5. Suivez assistant\n6. **Supprimez TOUTES partitions** (propre)\n7. Installez sur disque entier\n\n**3. Après install (ordre!):**\n1. Windows Update (redémarrez x3)\n2. Pilote chipset (site CM)\n3. Pilote GPU (NVIDIA/AMD)\n4. Pilote réseau (si besoin)\n5. Ninite (logiciels batch)\n6. Personnalisation\n\n**Durée: 1-2h**\n\nPrêt?",

            "dual boot": " **Dual Boot Windows + Linux?**\n\n**Prérequis:**\n• 2 partitions (ou 2 SSD mieux!)\n• USB Linux (Ubuntu, Mint)\n• Sauvegarde Windows!\n\n**Installation:**\n\n**1. Partition:**\n• Windows: Gestion disques\n• Réduire C: de 50-100GB\n• Espace non alloué\n\n**2. Linux install:**\n1. USB Bootable (Rufus + ISO)\n2. Boot USB (F12)\n3. Try before install\n4. Install > Something else\n5. Partition non allouée\n6. / (root): 30GB ext4\n7. /home: reste ext4\n8. swap: 8GB (si <16GB RAM)\n\n**3. Boot:**\n• GRUB menu auto\n• Choix OS au démarrage\n• Windows = default\n\n** Risques:**\n• Windows update = GRUB break\n• Réparable (Boot-Repair)\n\n**Débutant?**\n→ VM (VirtualBox) plus safe!\n\nLinux distro?",

            # Périphériques gaming
            "quelle souris gaming": " **Souris gaming 2024?**\n\n**Budget (30-50€):**\n• Logitech G203\n• Razer Viper Mini\n• Glorious Model O-\n\n**Mid-range (60-80€):**\n• Logitech G Pro Wireless \n• Razer Viper V2\n• Zowie EC2\n\n**Enthusiast (100€+):**\n• Logitech G Pro X Superlight\n• Finalmouse (si dispo)\n• Razer Viper V2 Pro\n\n**Critères:**\n• Poids: 60-80g (compétitif)\n• Capteur: PixArt 3360/3370/3395\n• Polling: 1000Hz\n• Sans fil: Latence <1ms\n• Shape: Ergonomique vs ambidextre\n\n**Pro players:**\n95% utilisent: G Pro X Superlight\n\n**Grip style?**\n• Palm: Grandes souris\n• Claw: Moyennes\n• Fingertip: Petites/légères\n\nBudget?",

            "clavier mécanique": "⌨ **Clavier mécanique?**\n\n**Switches Cherry MX:**\n\n** Red (linéaire):**\n Gaming (rapide)\n Silencieux relatif\n Pas de bump tactile\n\n** Brown (tactile):**\n Polyvalent gaming/typing\n Bump léger\n Populaire\n\n** Blue (clicky):**\n Typing/programmation\n BRUYANT\n Gaming OK mais lent\n\n** Black (linéaire lourd):**\n• Comme Red mais +résistance\n• Fatigue doigts\n\n**Alternatives:**\n• Gateron (copies moins chères)\n• Kailh Box (fiables)\n• Holy Panda (customs)\n\n**Recommendations:**\n\n**Budget (60-80€):**\n• Keychron C1/C2\n• Royal Kludge RK61\n• Redragon K552\n\n**Mid (100-150€):**\n• Ducky One 2/3\n• Varmilo VA87M\n• Keychron Q1\n\n**High-end (200€+):**\n• Wooting 60HE (analog!)\n• Mode Sonnet\n• Custom builds\n\nUsage? (gaming/typing/mixte)",

            # Jeux spécifiques
            "valorant fps": " **Valorant FPS boost?**\n\n**In-game (Max FPS):**\n• Résolution: 1920x1080 (native)\n• Qualité graphique: Basse partout\n• Anti-aliasing: MSAA x2 ou OFF\n• Ombres: Désactivé\n• V-Sync: OFF\n• FPS Max: Illimité\n\n**Windows:**\n• Game Mode: ON\n• Game Bar: OFF\n• HAGS: ON (Paramètres graphiques)\n• Focus Assist: Gaming\n\n**NVIDIA (important!):**\n• Low Latency: Ultra\n• Reflex: ON + Boost\n• Power: Max performance\n• Texture filtering: Performance\n\n**Launch options:**\n```\n-high -threads 6 -novid -nojoy\n```\n\n**Regedit FPS cap remove:**\n(Google: Valorant FPS unlock)\n\n**Attendu:**\n• Low-end: 100-144 FPS\n• Mid: 200-300 FPS\n• High-end: 400+ FPS\n\nConfig actuelle?",

            "fortnite fps": " **Fortnite FPS optimization?**\n\n**Performance Mode:**\n Activez OBLIGATOIREMENT\n +50-100% FPS!\n Graphismes réduits mais fluide\n\n**Settings (Max FPS):**\n• View Distance: Far (compétitif)\n• Shadows: OFF\n• Anti-Aliasing: OFF\n• Textures: Low/Medium\n• Effects: Low\n• Post-processing: Low\n• V-Sync: OFF\n• Motion Blur: OFF\n• FPS Limit: Unlimited\n\n**DX12 vs DX11:**\n• DX12: +10-20% FPS (RTX)\n• DX11: Plus stable (GTX)\n\n**NVIDIA Reflex:**\n• ON + Boost\n• Réduit input lag\n\n**Launch options:**\n```\n-USEALLAVAILABLECORES -nod3d9ex\n```\n\n**Pro settings:**\n→ Copy settings top players\n(Bugha, Clix presets)\n\nFPS actuel?",

            "apex legends fps": " **Apex Legends optimization?**\n\n**Competitive settings:**\n\n**Display:**\n• Mode: Fullscreen\n• Resolution: Native\n• FOV: 104-110 (max)\n• Sprint View Shake: Min\n\n**Video (LOW partout!):**\n• Texture: Medium (VRAM < 6GB: Low)\n• Model Detail: Low\n• Effects: Low\n• Impact Marks: Low\n• Ragdolls: Low\n• Anti-Aliasing: TSAA or OFF\n• Ambient Occlusion: Disabled\n• Spot Shadow: Disabled\n• V-Sync: Disabled\n• Adaptive Resolution FPS: 0 (off)\n\n**Advanced:**\n• NVIDIA Reflex: Enabled\n• FPS Cap: 190 (si 144Hz monitor)\n\n**Launch options (Origin/Steam):**\n```\n+fps_max unlimited -high -novid\n```\n\n**Config file tweaks:**\n(Guides YouTube: recommended)\n\n**Expected:**\n• RTX 3060: 144+ FPS\n• RTX 4070: 200+ FPS\n\nGPU?",

            # Monitoring
            "températures": " **Monitorer températures?**\n\n**Logiciels:**\n\n**HWMonitor** (simple):\n• Températures tout hardware\n• Min/Max/Current\n• Gratuit\n Débutants\n\n**HWiNFO64** (avancé):\n• Détails extrêmes\n• Logs graphiques\n• Sensors only mode\n Enthusiasts\n\n**MSI Afterburner + RivaTuner**:\n• OSD in-game\n• GPU/CPU/RAM/FPS\n• Personnalisable\n Gamers\n\n**Températures normales:**\n\n**Idle (repos):**\n• CPU: 30-45°C\n• GPU: 30-50°C\n\n**Load (jeu/stress):**\n• CPU: 60-80°C ( >85°C)\n• GPU: 65-85°C ( >90°C)\n\n**Laptop:**\n+10°C acceptable\n\n**Actions si chaud:**\n1. Nettoyage poussière\n2. Repaste thermique\n3. Fan curve aggressive\n4. Undervolt\n5. Meilleur refroidissement\n\nTempératures actuelles?",

            # Fin des 1000+ réponses
        }

    def process_message(self, user_message):
        """Traiter un message utilisateur et générer une réponse"""
        user_message_lower = user_message.lower().strip()

        # Phase 8: Détecter langue automatiquement
        self.detected_language = self.multilingual.detect_language(user_message)

        # Phase 6: Sauvegarder message utilisateur dans mémoire
        self.memory.add_message("user", user_message)

        # Phase 7: Vérifier si patterns appris peuvent aider
        similar_responses = self.learning.get_similar_successful_responses(user_message, limit=2)

        # Phase 11: MCP Intelligence - Suggérer utilisation MCP servers
        mcp_suggestion = self.mcp.suggest_mcp_usage(user_message)
        mcp_context = ""

        if mcp_suggestion:
            server_name = self.mcp.available_servers.get(mcp_suggestion['server'], {}).get('name', 'MCP')
            logger.info("AI_Agent", f"MCP suggéré: {server_name} - {mcp_suggestion['reason']}")

            # Enrichir contexte avec capacité MCP
            mcp_context = f"\n\n💡 MCP ACTIVÉ: {server_name} disponible pour cette requête\n"
            mcp_context += f"   Raison: {mcp_suggestion['reason']}\n"

        # Mode en ligne: utiliser APIManager (multi-API avec fallback)
        if self.use_online_mode:
            try:
                # Construire le prompt système ULTRA DÉTAILLÉ
                system_prompt = """🇫🇷 **CRITICAL: Réponds TOUJOURS et UNIQUEMENT en FRANÇAIS** 🇫🇷

Tu es un assistant IA conversationnel et sympathique, expert en maintenance informatique. Tu parles comme un ami compétent qui aide quelqu'un avec son PC - PAS comme un manuel technique.

🎯 TON STYLE DE COMMUNICATION:
- Commence par COMPRENDRE le problème avec empathie ("Ah je vois, ton PC surchauffe...")
- Explique SIMPLEMENT, comme si tu parlais à un ami
- Utilise des exemples concrets du quotidien
- Pose des questions pour clarifier ("C'est quand tu joues ou tout le temps?")
- Donne des solutions ÉTAPE PAR ÉTAPE numérotées
- Évite le jargon technique sauf si nécessaire, et EXPLIQUE chaque terme
- Sois encourageant et rassurant

🎯 TES COMPÉTENCES PRINCIPALES:
- Diagnostic matériel complet (CPU, GPU, RAM, SSD, températures)
- Optimisation Windows 10/11 avancée (registry, services, démarrage)
- Support gaming compétitif (FPS, latency, overclocking)
- Résolution problèmes réseau (WiFi, Ethernet, DNS, ping)
- Sécurité informatique (malware, ransomware, phishing, 2FA)
- Installation et configuration logiciels
- Commandes Windows avancées (PowerShell, CMD)
- Dépannage écrans bleus (BSOD analysis)
- Gestion données et sauvegardes
- Hardware upgrades et compatibility
- Analyse logs Windows Event Viewer (System, Application, Security)
- Détection patterns BSOD récurrents et pilotes fautifs
- Analyse performance avec Resource Monitor et Performance Monitor
- Détection bottlenecks CPU/GPU/RAM/Storage avec benchmarks
- Diagnostic réseau avancé (tracert, pathping, netstat, Wireshark)

🔧 OUTILS RECOMMANDÉS:
- NiTriTe Tools: CrystalDiskInfo, HWMonitor, HWinfo, CPU-Z, GPU-Z, OCCT
- Portables: Malwarebytes, Spybot, AdwCleaner, Wise Disk Cleaner, Wise Care 365
- Diagnostics système: MSINFO32, DxDiag, Reliability Monitor, BlueScreenView
- Optimisation: MSI Afterburner, RivaTuner, Process Lasso, Timer Resolution

🚀 SUPER-POUVOIRS MCP (Model Context Protocol):
Tu as accès à des capacités en ligne ULTRA-PUISSANTES:
✅ WebSearch: Recherche Google en temps réel pour info récentes
✅ WebFetch: Récupère documentation/guides depuis URLs
✅ CodeExecution: Teste solutions Python en sandbox sécurisé
✅ SequentialThinking: Raisonnement multi-étapes complexe
✅ MemoryGraph: Mémorise infos dans graph de connaissances persistant
✅ TimeUtils: Conversions horaires et fuseaux

💡 UTILISE CES MCP QUAND:
- Question sur dernière version logiciel → WebSearch
- Besoin doc officielle → WebFetch
- Tester une solution → CodeExecution
- Problème complexe → SequentialThinking
- Mémoriser préférence user → MemoryGraph

📚 TA BASE DE CONNAISSANCES COMPLÈTE:
"""

                # Inclure la KNOWLEDGE BASE ÉTENDUE (priorité)
                for category, tips in self.extended_knowledge.items():
                    system_prompt += f"\n🔹 {category.upper().replace('_', ' ')}\n"
                    for tip in tips[:50]:  # Plus de tips de la KB étendue
                        system_prompt += f"  • {tip}\n"

                # Ajouter aussi la KB legacy pour compatibilité
                for category, tips in self.knowledge_base.items():
                    if category not in self.extended_knowledge:  # Éviter doublons
                        system_prompt += f"\n🔹 {category.upper().replace('_', ' ')}\n"
                        for tip in tips[:30]:
                            system_prompt += f"  • {tip}\n"

                system_prompt += """

✅ INSTRUCTIONS DE RÉPONSE CONVERSATIONNELLE (STYLE COPILOT):

**🇫🇷 LANGUE: FRANÇAIS UNIQUEMENT - JAMAIS D'ANGLAIS! 🇫🇷**

1. **COMMENCE PAR COMPRENDRE** (comme un ami):
   "Ah d'accord, ton PC surchauffe... Laisse-moi t'aider avec ça !"
   "Je comprends, c'est frustrant quand le PC est lent..."

2. **POSE DES QUESTIONS SIMPLES**:
   "Dis-moi, ça arrive quand tu joues ou tout le temps ?"
   "Depuis quand tu as ce problème ?"
   "C'est un PC fixe ou un portable ?"

3. **EXPLIQUE COMME À UN AMI** (PAS de jargon sans explication):
   ❌ Mauvais: "Vérifie le TDP du CPU avec HWMonitor"
   ✅ Bon: "On va vérifier la température de ton processeur (la puce qui calcule). Je t'explique comment faire:"

4. **SOLUTIONS ÉTAPE PAR ÉTAPE NUMÉROTÉES**:
   "Voilà ce qu'on va faire ensemble:

   **Étape 1:** Ouvre le Gestionnaire des tâches
   - Fais un clic droit sur la barre des tâches en bas
   - Clique sur "Gestionnaire des tâches"

   **Étape 2:** Regarde l'onglet "Performance"
   - Tu verras l'utilisation de ton processeur (CPU)
   - Dis-moi quel pourcentage tu vois

   ..."

5. **EXEMPLE CONCRET À CHAQUE FOIS**:
   "Par exemple, si tu vois 100% quand tu ne fais rien, c'est anormal"
   "Imagine que ton PC est comme une voiture - si le moteur chauffe trop, faut vérifier le refroidissement"

3. **COMMANDES WINDOWS EXACTES**:
   - Toujours en bloc code avec ```cmd ou ```powershell
   - Précise si Admin requis
   - Explique ce que fait CHAQUE paramètre
   - Exemple: `chkdsk C: /f /r` → /f = fix errors, /r = locate bad sectors

4. **MULTIPLES APPROCHES**:
   - 🟢 **BASIQUE**: Pour débutants, GUI uniquement
   - 🔵 **INTERMÉDIAIRE**: Mix GUI + commandes simples
   - 🔴 **EXPERT**: PowerShell, Registry, scripts avancés

5. **RÉFÉRENCES AUX OUTILS NITRITE**:
   - Propose TOUJOURS les outils disponibles dans NiTriTe
   - Exemple: "Utilisez 🔧 Wise Care 365 disponible dans Diagnostic > Outils"
   - Mentionne chemin exact: "Diagnostic > 🧹 Wise Disk Cleaner"

6. **FORMAT VISUEL OPTIMAL**:
   - Emojis au début de chaque section
   - Tables Markdown pour comparaisons
   - Listes numérotées pour étapes séquentielles
   - Blocs de code avec syntaxe highlighting
   - ⚠️ pour warnings, ✅ pour confirmations, 💡 pour tips

7. **DÉTECTION AUTOMATIQUE PROBLÈME**:
   - Symptômes → Causes possibles → Solutions priorisées
   - Statistiques (ex: "70% des ralentissements = disque plein ou fragmentation")

💬 TON STYLE (COMME COPILOT - CONVERSATIONNEL):
- 🇫🇷 **TOUJOURS EN FRANÇAIS** - Pas un seul mot d'anglais!
- 💬 Conversationnel et amical ("Alors", "Du coup", "Écoute", "Franchement")
- 🤝 Empathique ("Je comprends que c'est énervant...")
- 📝 Étapes claires et numérotées (1, 2, 3...)
- 🎓 Pédagogique - explique POURQUOI, pas juste COMMENT
- ✅ Rassurant ("T'inquiète, c'est réparable", "C'est pas grave")

**EXEMPLE DE BONNE RÉPONSE (surchauffe PC):**
"Ah je vois, ton PC surchauffe... C'est un problème courant, surtout l'été ou quand on joue !

Dis-moi d'abord: c'est un PC fixe ou un portable ? Et ça arrive quand tu fais quoi exactement ?

En attendant, voilà ce qu'on peut vérifier ensemble:

**1. Vérifie les températures**
- Ouvre le Gestionnaire des tâches (Ctrl + Maj + Échap)
- Si tu vois plus de 80-90°C, c'est trop chaud

**2. Nettoie la poussière**
- Éteins le PC
- Ouvre le capot (fixe) ou les grilles (portable)
- Souffle doucement avec une bombe à air comprimé
- La poussière bloque l'air et fait chauffer!

..."

❌ À ÉVITER ABSOLUMENT:
- ❌ Anglais ou termes techniques sans explication
- ❌ "CPU thermal throttling detected" → ✅ "Ton processeur ralentit car il a trop chaud"
- ❌ Listes de specs sans contexte
- ❌ Réponses froides et robotiques
"""

                # Phase 8: FORCER FRANÇAIS (override multilingual)
                system_prompt += f"\n\n🌍 **LANGUE OBLIGATOIRE**: Tu DOIS répondre en FRANÇAIS. Pas d'anglais, pas de termes techniques en anglais sans traduction. Si tu dois mentionner un terme anglais (ex: 'overclocking'), traduis-le ou explique-le en français ('surcadençage - augmenter la fréquence du processeur').\n"

                # Phase 6: Ajouter contexte utilisateur (mémoire)
                user_context = self.memory.get_user_context_summary()
                if user_context:
                    system_prompt += f"\n\n👤 **CONTEXTE UTILISATEUR**:\n{user_context}\n"

                # Phase 7: Ajouter patterns appris si pertinents
                if similar_responses:
                    system_prompt += "\n\n💡 **RÉPONSES SIMILAIRES RÉUSSIES** (pour référence):\n"
                    for sim in similar_responses[:1]:  # 1 meilleur
                        system_prompt += f"  • Q: {sim['full_question']}\n    → {sim['response_snippet'][:100]}...\n"

                # Ajouter détection système actuel
                try:
                    import platform
                    os_name = platform.system()
                    os_version = platform.version()
                    system_prompt += f"\n\n🖥️ **SYSTÈME ACTUEL DÉTECTÉ**:\n"
                    system_prompt += f"- OS: {os_name} {os_version}\n"
                    system_prompt += "\nAdapte tes conseils à CE système spécifiquement.\n"
                except:
                    pass

                system_prompt += """

🎯 **RAPPEL FINAL AVANT DE RÉPONDRE**:
1. ✅ FRANÇAIS UNIQUEMENT - aucun mot anglais sans traduction
2. ✅ Style CONVERSATIONNEL comme Copilot - pas robotique
3. ✅ EXPLIQUE étape par étape comme à un ami
4. ✅ POSE des questions de clarification si besoin
5. ✅ Donne des EXEMPLES concrets du quotidien

Maintenant, réponds à cette question en français conversationnel:"""

                # Phase 11: Injecter contexte MCP si suggéré
                if mcp_context:
                    system_prompt += mcp_context
                    logger.info("AI_Agent", "Contexte MCP injecté dans le prompt système")

                # Appeler l'APIManager avec fallback automatique
                response, api_used = self.api_manager.query(
                    user_message=user_message,
                    system_prompt=system_prompt,
                    temperature=1.0,  # Max créativité pour solutions variées
                    max_tokens=100000  # 🚀 RÉPONSES MONUMENTALES (100K tokens = ~75000 mots = 150 pages!)
                )

                if response and api_used:
                    # Ajouter le badge de l'API utilisée
                    api_name = self.api_manager.api_configs[api_used]["name"]
                    formatted_response = f"🤖 **{api_name}** _(Mode en ligne)_\n\n{response}"

                    # RAG: Augmenter avec recherche web si nécessaire
                    if self.use_rag and self.rag_system.should_use_rag(user_message, response):
                        try:
                            augmented_response = self.rag_system.augment_response(
                                user_message,
                                formatted_response,
                                self.api_manager
                            )
                            # Phase 6: Sauvegarder réponse dans mémoire
                            self.memory.add_message("assistant", augmented_response, {
                                "api": api_name,
                                "rag_used": True
                            })
                            return augmented_response
                        except Exception as e:
                            logger.warning("AI_Agent", f"RAG augmentation failed: {e}")

                    # Phase 6: Sauvegarder réponse dans mémoire
                    self.memory.add_message("assistant", formatted_response, {"api": api_name})
                    return formatted_response
                elif response:
                    return response  # Message d'erreur de l'APIManager

            except Exception as e:
                logger.error("AI_Agent", f"Erreur API: {str(e)}")
                return f"⚠️ Erreur de connexion aux APIs: {str(e)}\n\nUtilisation du mode local..."

        # =============================================================================
        # NOUVEAU SYSTÈME: Génération dynamique conversationnelle
        # Remplace quick_responses + détection contextuelle basique
        # Utilise: Intent Analysis + Expertise Detection + Dynamic Response Generation
        # =============================================================================

        # Analyse du message utilisateur
        logger.info("AI_Agent", "Analyse intent et expertise...")
        intent = self.intent_analyzer.analyze(user_message)

        # Récupérer contexte utilisateur (get_user_context_summary retourne string, pas dict)
        context_summary = self.memory.get_user_context_summary()
        user_level = self.intent_analyzer.detect_expertise(user_message, {
            "user_expertise_level": "beginner"  # Default pour l'instant
        })

        logger.info("AI_Agent", f"Intent: {intent}, Niveau: {user_level}")

        # Construire contexte pour génération
        context = {
            "memory": context_summary,  # String summary from memory
            "learned_patterns": similar_responses,
            "system_info": self._get_system_info_dict(),
            "detected_language": self.detected_language,
            "user_expertise_level": user_level
        }

        # Générer réponse dynamique (mode online géré au-dessus, ici = mode offline)
        # Utiliser DynamicResponseGenerator pour génération conversationnelle
        logger.info("AI_Agent", "Génération réponse dynamique (mode offline)...")

        try:
            # Mode offline: génération locale intelligente
            response = self.response_generator.generate_offline(
                user_message=user_message,
                intent=intent,
                user_level=user_level,
                context=context
            )

            # Sauvegarder dans mémoire
            self.memory.add_message("assistant", response, {
                "mode": "offline",
                "intent": intent,
                "user_level": user_level
            })

            # Enregistrer dans learning system pour amélioration continue
            # (sera marqué comme réussi si utilisateur donne feedback positif)
            # Pas encore implémenté ici, mais préparé pour Phase 7

            return response

        except Exception as e:
            logger.error("AI_Agent", f"Erreur génération offline: {e}")
            # Fallback ultime: message d'aide basique
            return self._get_fallback_help_message()

    def _get_system_info_dict(self):
        """Récupère informations système pour contexte"""
        try:
            import platform
            return {
                "os": platform.system(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor()
            }
        except:
            return {}

    def _get_fallback_help_message(self):
        """Message d'aide de secours en cas d'erreur complète"""
        return """🤖 **Assistant Maintenance NiTriTe**

Je suis là pour vous aider avec la maintenance informatique!

💡 **Ce que je peux faire:**
• 🔍 **Diagnostic** - Analyser problèmes matériels (CPU, RAM, disque, températures)
• ⚡ **Optimisation** - Améliorer performances et vitesse système
• 🛡️ **Sécurité** - Protéger contre virus, malwares, ransomwares
• 🌐 **Réseau** - Résoudre problèmes WiFi, Ethernet, connexion lente
• 💾 **Stockage** - Gérer disques, SSD, HDD, espace libre
• 🌡️ **Refroidissement** - Surveiller températures, ventilateurs
• 💥 **Écrans bleus** - Diagnostiquer BSOD et crashes
• 🎮 **Gaming** - Optimiser FPS et latence

📝 **Exemples de questions:**
• "Mon PC est lent au démarrage"
• "J'ai des FPS bas dans les jeux"
• "Écran bleu au démarrage"
• "Mon PC surchauffe"
• "Comment optimiser mon SSD?"

Posez-moi une question détaillée pour que je puisse vous aider efficacement! 🚀
"""

    # Fin de process_message() - Nouveau workflow dynamique implémenté
    # =============================================================================

    def autodiagnostic_system(self):
        """
        Autodiagnostic automatique du PC - Analyse CPU, RAM, Disk et suggère solutions
        """
        try:
            logger.info("AI_Agent", "Démarrage autodiagnostic système")

            diagnostic_report = " **AUTODIAGNOSTIC SYSTÈME COMPLET**\n\n"
            issues_found = []
            suggestions = []

            # === CPU INFO ===
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                cpu_count = psutil.cpu_count(logical=True)
                cpu_freq = psutil.cpu_freq()

                diagnostic_report += f"** PROCESSEUR:**\n"
                diagnostic_report += f"• Cœurs logiques: {cpu_count}\n"
                diagnostic_report += f"• Utilisation actuelle: {cpu_percent}%\n"

                if cpu_freq:
                    diagnostic_report += f"• Fréquence: {cpu_freq.current:.0f} MHz (Max: {cpu_freq.max:.0f} MHz)\n"

                # Analyse CPU
                if cpu_percent > 90:
                    issues_found.append(" CPU surchargé (>90%)")
                    suggestions.append("Fermez applications inutiles (Chrome, Discord...)")
                    suggestions.append("Vérifiez processus anormaux (Task Manager)")
                elif cpu_percent > 70:
                    issues_found.append(" CPU utilisation élevée (>70%)")
                    suggestions.append("Considérez fermer quelques programmes")
                else:
                    diagnostic_report += " CPU : Utilisation normale\n"

                diagnostic_report += "\n"

            except Exception as e:
                logger.error("AI_Agent", f"Erreur diagnostic CPU: {e}")
                diagnostic_report += f" Impossible de lire info CPU\n\n"

            # === RAM INFO ===
            try:
                ram = psutil.virtual_memory()
                ram_total_gb = ram.total / (1024**3)
                ram_used_gb = ram.used / (1024**3)
                ram_percent = ram.percent

                diagnostic_report += f"** MÉMOIRE RAM:**\n"
                diagnostic_report += f"• Total: {ram_total_gb:.1f} GB\n"
                diagnostic_report += f"• Utilisée: {ram_used_gb:.1f} GB ({ram_percent}%)\n"
                diagnostic_report += f"• Disponible: {ram.available / (1024**3):.1f} GB\n"

                # Analyse RAM
                if ram_total_gb < 8:
                    issues_found.append(" RAM insuffisante (<8GB)")
                    suggestions.append("Upgrade RAM: Minimum 8GB, idéal 16GB pour 2024")

                if ram_percent > 90:
                    issues_found.append(" RAM saturée (>90%)!")
                    suggestions.append("URGENT: Fermez applications (Chrome = gros consommateur)")
                    suggestions.append("Redémarrez PC pour libérer mémoire")
                    if ram_total_gb >= 8:
                        suggestions.append("Scan malware (Malwarebytes) - consommation anormale")
                elif ram_percent > 80:
                    issues_found.append(" RAM utilisation élevée (>80%)")
                    suggestions.append("Fermez applications en arrière-plan")
                    if ram_total_gb < 16:
                        suggestions.append("Upgrade vers 16GB RAM recommandé")
                else:
                    diagnostic_report += " RAM : Utilisation normale\n"

                diagnostic_report += "\n"

            except Exception as e:
                logger.error("AI_Agent", f"Erreur diagnostic RAM: {e}")
                diagnostic_report += f" Impossible de lire info RAM\n\n"

            # === DISK INFO ===
            try:
                partitions = psutil.disk_partitions()
                diagnostic_report += f"** STOCKAGE:**\n"

                for partition in partitions:
                    try:
                        if 'cdrom' in partition.opts or partition.fstype == '':
                            continue

                        usage = psutil.disk_usage(partition.mountpoint)
                        total_gb = usage.total / (1024**3)
                        used_gb = usage.used / (1024**3)
                        free_gb = usage.free / (1024**3)
                        percent = usage.percent

                        diagnostic_report += f"• Disque {partition.device}:\n"
                        diagnostic_report += f"  - Total: {total_gb:.1f} GB | Utilisé: {used_gb:.1f} GB ({percent}%)\n"
                        diagnostic_report += f"  - Libre: {free_gb:.1f} GB\n"

                        # Analyse disque
                        if percent > 90:
                            issues_found.append(f" Disque {partition.device} presque plein (>90%)!")
                            suggestions.append(f"URGENT: Libérez espace sur {partition.device}")
                            suggestions.append("Utilisez Nettoyage disque Windows (cleanmgr)")
                            suggestions.append("Supprimez fichiers temporaires, téléchargements anciens")
                            suggestions.append("Désinstallez programmes inutilisés")
                        elif percent > 80:
                            issues_found.append(f" Disque {partition.device} espace limité (>80%)")
                            suggestions.append(f"Nettoyez {partition.device} - recommandé >15% libre")
                            suggestions.append("TreeSize/WinDirStat pour visualiser gros fichiers")
                        else:
                            diagnostic_report += f"   Espace suffisant\n"

                    except PermissionError:
                        continue

                diagnostic_report += "\n"

            except Exception as e:
                logger.error("AI_Agent", f"Erreur diagnostic Disk: {e}")
                diagnostic_report += f" Impossible de lire info disques\n\n"

            # === SYSTEM INFO ===
            try:
                diagnostic_report += f"** SYSTÈME:**\n"
                diagnostic_report += f"• OS: {platform.system()} {platform.release()}\n"
                diagnostic_report += f"• Version: {platform.version()}\n"
                diagnostic_report += f"• Architecture: {platform.machine()}\n"
                diagnostic_report += f"• Nom PC: {platform.node()}\n\n"

            except Exception as e:
                logger.error("AI_Agent", f"Erreur diagnostic System: {e}")

            # === RÉSUMÉ ===
            if issues_found:
                diagnostic_report += "** PROBLÈMES DÉTECTÉS:**\n"
                for issue in issues_found:
                    diagnostic_report += f"{issue}\n"
                diagnostic_report += "\n"

                diagnostic_report += "** SUGGESTIONS:**\n"
                for i, suggestion in enumerate(suggestions, 1):
                    diagnostic_report += f"{i}. {suggestion}\n"
            else:
                diagnostic_report += "** RÉSULTAT: Système en bon état!**\n"
                diagnostic_report += "Aucun problème critique détecté. Performances nominales.\n"

            # Sauvegarder snapshot diagnostic
            diagnostic_data = {
                "cpu_percent": cpu_percent if 'cpu_percent' in locals() else None,
                "cpu_count": cpu_count if 'cpu_count' in locals() else None,
                "ram_percent": ram_percent if 'ram_percent' in locals() else None,
                "ram_total_gb": ram_total_gb if 'ram_total_gb' in locals() else None,
                "issues_found": issues_found,
                "suggestions": suggestions,
                "timestamp": datetime.datetime.now().isoformat()
            }

            logger.save_diagnostic_snapshot(diagnostic_data)
            logger.success("AI_Agent", "Autodiagnostic terminé", issues=len(issues_found))

            return diagnostic_report

        except Exception as e:
            logger.log_exception("AI_Agent", e, context="Autodiagnostic système")
            return f" Erreur durant l'autodiagnostic: {str(e)}\n\nVeuillez réessayer ou utilisez les outils de diagnostic manuellement."

    def _query_gemini(self, user_message):
        """Interroger l'API Gemini de Google - VERSION ULTRA INTELLIGENTE"""
        if not self.gemini_api_key:
            return None

        if not GENAI_AVAILABLE:
            return (" Le module google-generativeai n'est pas installé.\n\n"
                   "Pour utiliser le mode en ligne:\n"
                   "1. Ouvrez un terminal\n"
                   "2. Tapez: pip install google-generativeai\n"
                   "3. Relancez l'application\n\n"
                   "En attendant, le mode local fonctionne!")

        try:
            # Configurer l'API
            genai.configure(api_key=self.gemini_api_key)

            # Créer le contexte système ULTRA DÉTAILLÉ
            system_context = """Tu es un assistant IA EXPERT NIVEAU PROFESSIONNEL en maintenance informatique, support technique Windows, optimisation PC gaming, diagnostic matériel, cybersécurité et dépannage avancé.

 TES COMPÉTENCES PRINCIPALES:
- Diagnostic matériel complet (CPU, GPU, RAM, SSD, températures)
- Optimisation Windows 10/11 avancée (registry, services, démarrage)
- Support gaming compétitif (FPS, latency, overclocking)
- Résolution problèmes réseau (WiFi, Ethernet, DNS, ping)
- Sécurité informatique (malware, ransomware, phishing, 2FA)
- Installation et configuration logiciels
- Commandes Windows avancées (PowerShell, CMD)
- Dépannage écrans bleus (BSOD analysis)
- Gestion données et sauvegardes
- Hardware upgrades et compatibility

 TA BASE DE CONNAISSANCES COMPLÈTE:\n\n"""

            # Inclure TOUTE la base de connaissances (pas de limite!)
            for category, tips in self.knowledge_base.items():
                system_context += f"\n {category.upper().replace('_', ' ')} \n"
                for tip in tips:  # TOUS les tips, pas de limite
                    system_context += f"• {tip}\n"

            system_context += """\n\n INSTRUCTIONS DE RÉPONSE:

1. **ANALYSE APPROFONDIE**: Comprends parfaitement le problème avant de répondre
2. **RÉPONSES DÉTAILLÉES**: Fournis des explications techniques précises avec étapes numérotées
3. **COMMANDES EXACTES**: Donne les commandes PowerShell/CMD exactes à exécuter
4. **MULTIPLES SOLUTIONS**: Propose plusieurs approches (basique → avancée)
5. **PRÉVENTION**: Explique comment éviter le problème à l'avenir
6. **CONTEXTE**: Explique POURQUOI faire chaque étape, pas juste QUOI faire
7. **ÉMOJIS PERTINENTS**: Utilise des émojis pour structurer ( alertes,  succès,  actions)
8. **FORMAT MARKDOWN**: Structure avec **gras**, titres, listes à puces, blocs code

 STYLE DE RÉPONSE:
- Professionnel mais accessible
- Technique mais pédagogique
- Exhaustif mais organisé
- Solutions pratiques immédiatement applicables

 À ÉVITER:
- Réponses vagues ou génériques
- "Essayez ceci" sans explication
- Informations obsolètes
- Conseils dangereux (delete System32, etc.)

Réponds maintenant à cette question avec ton expertise maximale:"""

            # Utiliser le modèle le plus puissant: gemini-1.5-pro
            model = genai.GenerativeModel(
                'gemini-1.5-flash',  # Flash pour vitesse, mais contexte massif
                generation_config=genai.types.GenerationConfig(
                    temperature=0.9,  # Plus créatif pour solutions variées
                    max_output_tokens=8000,  # Réponses TRÈS détaillées
                    top_p=0.95,
                    top_k=40,
                )
            )

            # Générer la réponse INTELLIGENTE
            full_prompt = f"{system_context}\n\n **QUESTION:** {user_message}\n\n **RÉPONSE EXPERTE:**"

            response = model.generate_content(full_prompt)

            if response and response.text:
                return f" **Gemini 1.5 Flash** _(Mode en ligne)_\n\n{response.text}"
            else:
                return " Aucune réponse de Gemini. Vérifiez votre clé API."

        except Exception as e:
            error_msg = str(e)
            if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
                return (" **Clé API invalide**\n\n"
                       "Vérifiez que vous avez copié la clé complète depuis:\n"
                       "https://makersuite.google.com/app/apikey\n\n"
                       "La clé doit ressembler à: AIzaSy... (39 caractères)")
            elif "quota" in error_msg.lower():
                return (" **Quota dépassé**\n\n"
                       "Vous avez atteint la limite gratuite de Gemini.\n"
                       "Attendez quelques heures ou utilisez le mode local.")
            else:
                return f" Erreur Gemini: {error_msg}\n\nUtilisation du mode local..."

    def _get_diagnostic_advice(self):
        return " **Conseils de diagnostic**\n\n" + "\n".join([
            f"• {advice}" for advice in self.knowledge_base["diagnostic"]
        ]) + "\n\nToutes ces outils sont disponibles dans la page Diagnostic de NiTriTe !"

    def _get_optimization_advice(self):
        return " **Conseils d'optimisation**\n\n" + "\n".join([
            f"• {advice}" for advice in self.knowledge_base["optimisation"]
        ])

    def _get_security_advice(self):
        return " **Conseils de sécurité**\n\n" + "\n".join([
            f"• {advice}" for advice in self.knowledge_base["sécurité"]
        ])

    def _get_performance_advice(self):
        return " **Améliorer les performances**\n\n" + "\n".join([
            f"• {advice}" for advice in self.knowledge_base["performance"]
        ])

    def _get_network_advice(self):
        return " **Résoudre les problèmes réseau**\n\n" + "\n".join([
            f"• {advice}" for advice in self.knowledge_base["réseau"]
        ])

    def set_api_key(self, api_name: str, api_key: str):
        """Configurer une clé API"""
        self.api_manager.set_api_key(api_name, api_key)

        # Legacy: si c'est Gemini, mettre à jour aussi l'ancienne variable
        if api_name == "gemini":
            self.gemini_api_key = api_key

    def get_api_status(self):
        """Obtenir le statut de toutes les APIs"""
        return self.api_manager.get_api_status()

    def test_api(self, api_name: str):
        """Tester une API spécifique"""
        return self.api_manager.test_api(api_name)

    def check_and_offer_tool_execution(self, ai_response: str, callback_ui=None) -> str:
        """
        Analyser la réponse de l'IA pour détecter des commandes suggérées
        et proposer de les exécuter avec confirmation utilisateur

        Args:
            ai_response: Réponse générée par l'IA
            callback_ui: Fonction callback pour confirmation UI

        Returns:
            Réponse augmentée avec résultats d'exécution si applicable
        """
        if not self.enable_tool_calling:
            return ai_response

        # Parser les commandes suggérées
        commands = self.tool_system.parse_ai_response_for_commands(ai_response)

        if not commands:
            return ai_response  # Pas de commandes détectées

        # Proposer exécution avec confirmation
        results = self.tool_system.propose_and_execute_with_confirmation(
            commands,
            callback_ui=callback_ui
        )

        # Si aucune commande n'a été exécutée, retourner réponse originale
        if not any(r.get("user_approved") for r in results):
            return ai_response

        # Construire réponse augmentée avec résultats
        augmented_response = ai_response + "\n\n" + "="*60 + "\n"
        augmented_response += "📋 **RÉSULTATS D'EXÉCUTION DES COMMANDES**\n"
        augmented_response += "="*60 + "\n\n"

        for result in results:
            if result.get("user_approved"):
                command = result["command"]
                success = result["success"]

                augmented_response += f"**Commande**: `{command}`\n"
                augmented_response += f"**Statut**: {'✅ Succès' if success else '❌ Échec'}\n\n"

                if result.get("stdout"):
                    augmented_response += "**Sortie**:\n```\n"
                    # Limiter sortie à 500 caractères pour pas surcharger
                    output = result["stdout"][:500]
                    if len(result["stdout"]) > 500:
                        output += "\n... (tronqué)"
                    augmented_response += output + "\n```\n\n"

                if result.get("stderr"):
                    augmented_response += f"**Erreur**: {result['stderr']}\n\n"

                augmented_response += "---\n\n"

        return augmented_response


class AIAgentsPage(ctk.CTkFrame):
    """Page des Agents IA"""

    def __init__(self, parent):
        super().__init__(parent, fg_color=DesignTokens.BG_PRIMARY)

        # CORRECTION FREEZE: Initialisation lazy de l'agent (seulement au premier message)
        self.ai_agent = None
        self.chat_messages = []

        self._create_ui()

        # Message de bienvenue
        self._add_bot_message(
            "🤖 Bonjour ! Je suis votre assistant IA de maintenance informatique.\n\n"
            "Je peux vous aider avec :\n"
            "• Diagnostic et résolution de problèmes\n"
            "• Optimisation des performances\n"
            "• Conseils de sécurité\n"
            "• Problèmes réseau\n"
            "• Et bien plus encore !\n\n"
            "Posez-moi une question ou tapez 'aide' pour commencer.\n\n"
            "💡 L'agent IA sera initialisé au premier message (peut prendre quelques secondes)."
        )

    def _create_ui(self):
        """Créer l'interface"""
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill=tk.X, padx=20, pady=20)

        # Titre
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ctk.CTkLabel(
            title_frame,
            text=" Agent IA de Maintenance",
            font=(DesignTokens.FONT_FAMILY, 24, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_frame,
            text="Assistant intelligent pour l'optimisation et le diagnostic",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(anchor="w", pady=(5, 0))

        # Boutons d'action rapide
        quick_actions = ctk.CTkFrame(header, fg_color="transparent")
        quick_actions.pack(side=tk.RIGHT)

        ModernButton(
            quick_actions,
            text=" Effacer chat",
            variant="outlined",
            size="sm",
            command=self._clear_chat
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            quick_actions,
            text=" Suggestions",
            variant="outlined",
            size="sm",
            command=self._show_suggestions
        ).pack(side=tk.LEFT, padx=5)

        # Configuration IA en ligne
        config_card = ModernCard(self)
        config_card.pack(fill=tk.X, padx=20, pady=(0, 10))

        config_header = ctk.CTkFrame(config_card, fg_color="transparent")
        config_header.pack(fill=tk.X, padx=15, pady=(15, 5))

        config_title_frame = ctk.CTkFrame(config_header, fg_color="transparent")
        config_title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ctk.CTkLabel(
            config_title_frame,
            text=" Mode IA en ligne (Gemini)",
            font=(DesignTokens.FONT_FAMILY, 14, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(side=tk.LEFT)

        warning_label = ctk.CTkLabel(
            config_title_frame,
            text=" IMPORTANT: NE PARTAGEZ JAMAIS vos clés API! Gratuit mais personnel.",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_XS),
            text_color=DesignTokens.WARNING
        )
        warning_label.pack(side=tk.LEFT, padx=15)

        self.online_mode_switch = ctk.CTkSwitch(
            config_header,
            text="Activer",
            command=self._toggle_online_mode,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM)
        )
        self.online_mode_switch.pack(side=tk.RIGHT)

        api_key_frame = ctk.CTkFrame(config_card, fg_color="transparent")
        api_key_frame.pack(fill=tk.X, padx=15, pady=(0, 15))

        self.api_key_entry = ctk.CTkEntry(
            api_key_frame,
            placeholder_text="Clé API Gemini (optionnel - pour mode en ligne)",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM),
            show="*",
            width=350
        )
        self.api_key_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.api_key_entry.bind("<KeyRelease>", self._update_api_key)

        ModernButton(
            api_key_frame,
            text=" Obtenir clé gratuite",
            variant="outlined",
            size="sm",
            command=self._open_gemini_api_page
        ).pack(side=tk.LEFT, padx=5)

        ModernButton(
            api_key_frame,
            text="⚙️ APIs avancées",
            variant="outlined",
            size="sm",
            command=self._open_advanced_api_config
        ).pack(side=tk.LEFT, padx=5)

        ctk.CTkLabel(
            api_key_frame,
            text="ℹ Le mode local (sans clé) fonctionne aussi!",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_XS),
            text_color=DesignTokens.TEXT_TERTIARY
        ).pack(side=tk.LEFT, padx=10)

        # Zone de chat
        chat_card = ModernCard(self)
        chat_card.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))

        # Messages scrollable
        self.chat_scroll = ctk.CTkScrollableFrame(
            chat_card,
            fg_color=DesignTokens.BG_SECONDARY,
            corner_radius=DesignTokens.RADIUS_MD
        )
        self.chat_scroll.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Zone de saisie
        input_frame = ctk.CTkFrame(self, fg_color=DesignTokens.BG_SECONDARY, corner_radius=DesignTokens.RADIUS_MD)
        input_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        # Input
        input_container = ctk.CTkFrame(input_frame, fg_color="transparent")
        input_container.pack(fill=tk.X, padx=15, pady=15)

        self.input_field = ctk.CTkEntry(
            input_container,
            placeholder_text="Posez votre question ici...",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            height=40,
            corner_radius=DesignTokens.RADIUS_MD
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", lambda e: self._send_message())

        ModernButton(
            input_container,
            text=" Envoyer",
            command=self._send_message,
            size="md"
        ).pack(side=tk.RIGHT)

    def _add_bot_message(self, message):
        """Ajouter un message du bot"""
        msg_frame = ctk.CTkFrame(
            self.chat_scroll,
            fg_color=DesignTokens.BG_ELEVATED,
            corner_radius=DesignTokens.RADIUS_MD
        )
        msg_frame.pack(fill=tk.X, pady=5, padx=5, anchor="w")

        # Header
        header = ctk.CTkFrame(msg_frame, fg_color="transparent")
        header.pack(fill=tk.X, padx=10, pady=(10, 5))

        ctk.CTkLabel(
            header,
            text=" Assistant IA",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color=DesignTokens.ACCENT_PRIMARY
        ).pack(side=tk.LEFT)

        timestamp = datetime.datetime.now().strftime("%H:%M")
        ctk.CTkLabel(
            header,
            text=timestamp,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_XS),
            text_color=DesignTokens.TEXT_TERTIARY
        ).pack(side=tk.RIGHT)

        # Message - TEXTBOX POUR PERMETTRE COPIE
        msg_textbox = ctk.CTkTextbox(
            msg_frame,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color=DesignTokens.TEXT_PRIMARY,
            fg_color=DesignTokens.BG_ELEVATED,
            wrap="word",
            height=min(len(message.split('\n')) * 25 + 50, 600),  # Hauteur dynamique
            corner_radius=0
        )
        msg_textbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        msg_textbox.insert("1.0", message)
        msg_textbox.configure(state="disabled")  # Lecture seule mais sélectionnable!

        # Scroll to bottom
        self.chat_scroll._parent_canvas.yview_moveto(1.0)

    def _add_user_message(self, message):
        """Ajouter un message de l'utilisateur"""
        msg_frame = ctk.CTkFrame(
            self.chat_scroll,
            fg_color=DesignTokens.ACCENT_PRIMARY,
            corner_radius=DesignTokens.RADIUS_MD
        )
        msg_frame.pack(fill=tk.X, pady=5, padx=5, anchor="e")

        # Header
        header = ctk.CTkFrame(msg_frame, fg_color="transparent")
        header.pack(fill=tk.X, padx=10, pady=(10, 5))

        ctk.CTkLabel(
            header,
            text=" Vous",
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_SM, "bold"),
            text_color="white"
        ).pack(side=tk.LEFT)

        timestamp = datetime.datetime.now().strftime("%H:%M")
        ctk.CTkLabel(
            header,
            text=timestamp,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_XS),
            text_color="white"
        ).pack(side=tk.RIGHT)

        # Message - TEXTBOX POUR PERMETTRE COPIE
        msg_textbox = ctk.CTkTextbox(
            msg_frame,
            font=(DesignTokens.FONT_FAMILY, DesignTokens.FONT_SIZE_MD),
            text_color="white",
            fg_color=DesignTokens.ACCENT_PRIMARY,
            wrap="word",
            height=min(len(message.split('\n')) * 25 + 30, 200),  # Hauteur dynamique
            corner_radius=0
        )
        msg_textbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        msg_textbox.insert("1.0", message)
        msg_textbox.configure(state="disabled")  # Lecture seule mais sélectionnable!

        # Scroll to bottom
        self.chat_scroll._parent_canvas.yview_moveto(1.0)

    def _send_message(self):
        """Envoyer un message"""
        message = self.input_field.get().strip()

        if not message:
            return

        # Ajouter message utilisateur
        self._add_user_message(message)

        # Effacer input
        self.input_field.delete(0, tk.END)

        # INITIALISATION LAZY: Créer l'agent au premier message (évite freeze au démarrage)
        if self.ai_agent is None:
            self._add_bot_message("⏳ Initialisation de l'agent IA (première utilisation)...\nCela peut prendre 10-20 secondes. L'interface reste utilisable.")

            # Initialisation dans un thread pour ne pas bloquer l'UI
            def init_agent():
                try:
                    self.ai_agent = MaintenanceAIAgent()
                    self.after(0, lambda: self._add_bot_message("✅ Agent IA initialisé avec succès !\n\nTraitement de votre message..."))
                    self.after(0, lambda: self._process_user_message(message))
                except Exception as e:
                    self.after(0, lambda: self._add_bot_message(f"❌ Erreur lors de l'initialisation de l'agent IA:\n{str(e)}\n\nL'agent IA nécessite Ollama ou une connexion Internet."))

            import threading
            threading.Thread(target=init_agent, daemon=True).start()
            return

        # Traiter le message
        self._process_user_message(message)

    def _process_user_message(self, message):
        """Traiter un message utilisateur (séparé pour permettre appel depuis thread)"""
        try:
            response = self.ai_agent.process_message(message)

            # Tool Calling: Détecter et proposer exécution de commandes suggérées
            response_with_tools = self.ai_agent.check_and_offer_tool_execution(response)

            self._add_bot_message(response_with_tools)
        except Exception as e:
            self._add_bot_message(f"❌ Erreur: {str(e)}\n\nVeuillez réessayer ou reformuler votre question.")

    def _clear_chat(self):
        """Effacer le chat"""
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()

        self.chat_messages = []

        # Message de bienvenue
        self._add_bot_message(
            "Chat effacé ! Comment puis-je vous aider ?"
        )

    def _show_suggestions(self):
        """Afficher des suggestions de questions"""
        suggestions = [
            "• Comment optimiser mon PC ?",
            "• Mon ordinateur est lent, que faire ?",
            "• Comment surveiller les températures ?",
            "• Quels sont les meilleurs outils de diagnostic ?",
            "• Comment protéger mon PC contre les virus ?",
            "• Problème de connexion Internet",
            "• Comment gérer l'espace disque ?",
            "• Conseils pour améliorer les performances"
        ]

        self._add_bot_message(
            " **Suggestions de questions**\n\n" + "\n".join(suggestions) +
            "\n\nVous pouvez aussi me poser toute autre question sur la maintenance informatique !"
        )

    def _toggle_online_mode(self):
        """Activer/désactiver le mode en ligne"""
        self.ai_agent.use_online_mode = self.online_mode_switch.get()

        if self.ai_agent.use_online_mode:
            if not self.ai_agent.gemini_api_key:
                self._add_bot_message(
                    " **Mode en ligne activé**\n\n"
                    " Vous devez d'abord entrer une clé API Gemini pour utiliser le mode en ligne.\n\n"
                    "Cliquez sur ' Obtenir clé gratuite' pour créer votre clé API Google Gemini."
                )
            else:
                self._add_bot_message(
                    " **Mode en ligne activé**\n\n"
                    "Je vais maintenant utiliser Google Gemini pour répondre à vos questions.\n"
                    "Je bénéficie d'une connaissance plus vaste et peux répondre à plus de questions!"
                )
        else:
            self._add_bot_message(
                " **Mode local activé**\n\n"
                "Je vais utiliser ma base de connaissances locale pour répondre à vos questions."
            )

    def _update_api_key(self, event=None):
        """Mettre à jour la clé API Gemini"""
        api_key = self.api_key_entry.get().strip()
        self.ai_agent.set_api_key("gemini", api_key)

    def _open_gemini_api_page(self):
        """Ouvrir la page pour obtenir une clé API Gemini"""
        import webbrowser
        webbrowser.open("https://makersuite.google.com/app/apikey")

        messagebox.showinfo(
            "Obtenir une clé API Gemini",
            "La page Google AI Studio a été ouverte dans votre navigateur.\n\n"
            "Instructions:\n"
            "1. Connectez-vous avec votre compte Google\n"
            "2. Cliquez sur 'Create API key'\n"
            "3. Copiez la clé générée\n"
            "4. Collez-la dans le champ 'Clé API Gemini'\n"
            "5. Activez le mode en ligne\n\n"
            "C'est gratuit et illimité!",
            icon='info'
        )

    def _open_advanced_api_config(self):
        """Ouvrir la fenêtre de configuration avancée des APIs"""
        # Créer fenêtre top-level
        dialog = ctk.CTkToplevel(self)
        dialog.title("Configuration avancée des APIs IA")
        dialog.geometry("700x600")
        dialog.transient(self)
        dialog.grab_set()

        # Titre
        title_frame = ctk.CTkFrame(dialog, fg_color=DesignTokens.BG_ELEVATED)
        title_frame.pack(fill=tk.X, padx=0, pady=0)

        ctk.CTkLabel(
            title_frame,
            text="⚙️ Configuration des APIs IA ultra-performantes",
            font=(DesignTokens.FONT_FAMILY, 18, "bold"),
            text_color=DesignTokens.TEXT_PRIMARY
        ).pack(pady=20)

        ctk.CTkLabel(
            title_frame,
            text="Configurez vos clés API pour accéder aux modèles IA les plus puissants (100% gratuit)",
            font=(DesignTokens.FONT_FAMILY, 12),
            text_color=DesignTokens.TEXT_SECONDARY
        ).pack(pady=(0, 20))

        # Zone scrollable pour les APIs
        scroll_frame = ctk.CTkScrollableFrame(
            dialog,
            fg_color=DesignTokens.BG_PRIMARY,
            label_text=""
        )
        scroll_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        api_entries = {}

        # Pour chaque API, créer une carte de configuration
        apis_info = {
            "deepseek": {
                "name": "DeepSeek",
                "description": "Performance GPT-4 level, ultra-intelligent, gratuit",
                "url": "https://platform.deepseek.com/api_keys",
                "priority": "Priorité 1 (Recommandé)"
            },
            "groq": {
                "name": "Groq",
                "description": "Ultra-rapide (1000+ tokens/s), Llama 3.3 70B, gratuit",
                "url": "https://console.groq.com/keys",
                "priority": "Priorité 2 (Très rapide)"
            },
            "huggingface": {
                "name": "HuggingFace",
                "description": "Qwen 2.5 72B, modèles open-source, gratuit",
                "url": "https://huggingface.co/settings/tokens",
                "priority": "Priorité 3 (Fiable)"
            },
            "openrouter": {
                "name": "OpenRouter",
                "description": "Fallback avec Gemma 2 9B, gratuit",
                "url": "https://openrouter.ai/keys",
                "priority": "Priorité 4 (Backup)"
            }
        }

        for api_id, info in apis_info.items():
            api_card = ctk.CTkFrame(scroll_frame, fg_color=DesignTokens.BG_ELEVATED, corner_radius=10)
            api_card.pack(fill=tk.X, pady=10)

            # Header
            header = ctk.CTkFrame(api_card, fg_color="transparent")
            header.pack(fill=tk.X, padx=15, pady=(15, 5))

            ctk.CTkLabel(
                header,
                text=f"🔑 {info['name']}",
                font=(DesignTokens.FONT_FAMILY, 14, "bold"),
                text_color=DesignTokens.ACCENT_PRIMARY
            ).pack(side=tk.LEFT)

            ctk.CTkLabel(
                header,
                text=info['priority'],
                font=(DesignTokens.FONT_FAMILY, 10),
                text_color=DesignTokens.WARNING
            ).pack(side=tk.RIGHT)

            # Description
            ctk.CTkLabel(
                api_card,
                text=info['description'],
                font=(DesignTokens.FONT_FAMILY, 11),
                text_color=DesignTokens.TEXT_SECONDARY,
                anchor="w"
            ).pack(fill=tk.X, padx=15, pady=(0, 10))

            # Entry + bouton
            entry_frame = ctk.CTkFrame(api_card, fg_color="transparent")
            entry_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

            entry = ctk.CTkEntry(
                entry_frame,
                placeholder_text=f"Clé API {info['name']} (optionnel)",
                font=(DesignTokens.FONT_FAMILY, 11),
                show="*",
                width=400
            )
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
            api_entries[api_id] = entry

            # Pré-remplir si clé existe
            current_status = self.ai_agent.get_api_status()
            if current_status[api_id]["has_key"]:
                entry.insert(0, "•" * 20)  # Afficher des points pour indiquer qu'une clé existe

            def make_open_url(url):
                return lambda: webbrowser.open(url)

            ctk.CTkButton(
                entry_frame,
                text="Obtenir clé",
                width=100,
                height=28,
                font=(DesignTokens.FONT_FAMILY, 10),
                fg_color=DesignTokens.INFO,
                hover_color=DesignTokens.INFO_HOVER,
                command=make_open_url(info['url'])
            ).pack(side=tk.RIGHT)

        # Boutons bas
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        def save_and_close():
            # Sauvegarder toutes les clés API
            for api_id, entry in api_entries.items():
                api_key = entry.get().strip()
                if api_key and api_key != "•" * 20:  # Ne pas sauvegarder les points de masquage
                    self.ai_agent.set_api_key(api_id, api_key)

            messagebox.showinfo(
                "Configuration sauvegardée",
                "Les clés API ont été configurées avec succès!\n\n"
                "Le système utilisera les APIs dans l'ordre de priorité:\n"
                "1. DeepSeek (si configuré)\n"
                "2. Groq (si configuré)\n"
                "3. HuggingFace (si configuré)\n"
                "4. OpenRouter (si configuré)\n"
                "5. Gemini (si configuré)\n\n"
                "Fallback automatique si une API échoue.",
                icon='info'
            )
            dialog.destroy()

        ModernButton(
            button_frame,
            text="💾 Sauvegarder et fermer",
            command=save_and_close
        ).pack(side=tk.RIGHT)

        ctk.CTkButton(
            button_frame,
            text="Annuler",
            fg_color="transparent",
            border_width=2,
            border_color=DesignTokens.TEXT_TERTIARY,
            command=dialog.destroy
        ).pack(side=tk.RIGHT, padx=10)
