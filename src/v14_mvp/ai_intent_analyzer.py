#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyseur d'Intent pour Agent IA - NiTriTe V20.0
Détection intelligente de l'intent utilisateur et niveau d'expertise
Remplace pattern matching basique if/elif
AMÉLIORATION V20.0: Fuzzy matching natif + Tolérance fautes d'orthographe
"""

import re
from typing import Dict, Optional, Tuple, List
from difflib import SequenceMatcher


class IntentAnalyzer:
    """
    Analyse intelligente des messages utilisateur
    - Détection type de question (intent)
    - Détection niveau expertise (beginner/intermediate/expert)
    - Fuzzy matching catégories
    """

    def __init__(self):
        """Initialise les patterns d'intent et keywords d'expertise"""

        # Dictionnaire de variantes orthographiques et synonymes ÉTENDU (500+)
        self.word_variants = {
            # ===== MATÉRIEL - CPU (50 variantes) =====
            "cpu": ["cpu", "processeur", "proc", "proco", "procesor"],
            "processeur": ["processeur", "cpu", "proc", "proco"],
            "procesor": "processeur", "proceseur": "processeur", "proco": "processeur",
            "proc": "processeur", "procs": "processeur",

            # Intel
            "i3": ["intel i3", "i3", "core i3"], "i5": ["intel i5", "i5", "core i5"],
            "i7": ["intel i7", "i7", "core i7"], "i9": ["intel i9", "i9", "core i9"],
            "intel": ["intel", "intel cpu"], "core": ["core", "intel core"],

            # AMD
            "ryzen": ["ryzen", "amd ryzen", "r5", "r7", "r9"],
            "r5": ["ryzen 5", "r5", "amd ryzen 5"], "r7": ["ryzen 7", "r7", "amd ryzen 7"],
            "r9": ["ryzen 9", "r9", "amd ryzen 9"], "amd": ["amd", "amd cpu"],
            "threadripper": ["threadripper", "tr", "amd threadripper"],

            # ===== MATÉRIEL - GPU (60 variantes) =====
            "gpu": ["gpu", "carte graphique", "cg", "carte graph", "cg", "graphique"],
            "carte graphique": ["carte graphique", "gpu", "cg", "carte graph"],
            "cart graphik": "carte graphique", "carte grafique": "carte graphique",
            "cart grafik": "carte graphique", "cg": "carte graphique",
            "carte graph": "carte graphique", "graphique": "carte graphique",

            # NVIDIA
            "rtx": ["nvidia rtx", "geforce rtx", "rtx"], "gtx": ["nvidia gtx", "geforce gtx", "gtx"],
            "nvidia": ["nvidia", "geforce"], "geforce": ["geforce", "nvidia"],
            "rtx 4090": ["rtx 4090", "4090"], "rtx 4080": ["rtx 4080", "4080"],
            "rtx 4070": ["rtx 4070", "4070"], "rtx 4060": ["rtx 4060", "4060"],
            "rtx 3090": ["rtx 3090", "3090"], "rtx 3080": ["rtx 3080", "3080"],
            "rtx 3070": ["rtx 3070", "3070"], "rtx 3060": ["rtx 3060", "3060"],

            # AMD GPU
            "rx": ["amd rx", "radeon rx", "rx"], "radeon": ["radeon", "amd radeon"],
            "rx 7900": ["rx 7900", "7900 xt", "7900 xtx"],
            "rx 7800": ["rx 7800", "7800 xt"], "rx 7700": ["rx 7700", "7700 xt"],
            "rx 6800": ["rx 6800", "6800 xt"], "rx 6700": ["rx 6700", "6700 xt"],

            # Mémoire GPU
            "vram": ["vram", "mémoire graphique", "mémoire gpu", "memoire gpu"],
            "memoire graphique": "mémoire graphique",

            # ===== MATÉRIEL - RAM (40 variantes) =====
            "ram": ["ram", "mémoire", "memoire", "barrette", "barrettes"],
            "mémoire": ["mémoire", "ram", "memoire"], "memoire": "mémoire",
            "memwar": "mémoire", "memwar vive": "mémoire vive",
            "barrette": ["barrette", "barrette ram", "ram"], "barrettes": ["barrettes", "ram"],

            # Types RAM
            "ddr4": ["ddr4", "ram ddr4", "ddr 4"], "ddr5": ["ddr5", "ram ddr5", "ddr 5"],
            "ddr3": ["ddr3", "ram ddr3", "ddr 3"],
            "dimm": ["dimm", "barrette dimm"], "sodimm": ["sodimm", "so-dimm", "portable ram"],

            # Capacités
            "8go": ["8gb", "8go", "8 gb", "8 go"], "16go": ["16gb", "16go", "16 gb", "16 go"],
            "32go": ["32gb", "32go", "32 gb", "32 go"], "64go": ["64gb", "64go", "64 gb", "64 go"],
            "gb": "go", "giga": "go",

            # ===== MATÉRIEL - STOCKAGE (45 variantes) =====
            "ssd": ["ssd", "disque ssd", "solid state"], "hdd": ["hdd", "disque dur", "hard drive"],
            "disque dur": ["disque dur", "hdd"], "disk dur": "disque dur", "diske dur": "disque dur",
            "nvme": ["nvme", "m.2", "pcie ssd", "m2"], "m2": "m.2", "m.2": ["m.2", "nvme", "m2"],
            "sata": ["sata", "ssd sata"], "pcie": ["pcie", "pci express", "pci-e"],

            # Capacités
            "500go": ["500gb", "500go", "500 gb"], "1to": ["1tb", "1to", "1 to", "1 tb"],
            "2to": ["2tb", "2to", "2 to", "2 tb"], "4to": ["4tb", "4to", "4 to"],
            "to": "tb", "tera": "tb",

            # ===== MATÉRIEL - PÉRIPHÉRIQUES (35 variantes) =====
            "souris": ["souris", "mouse", "souri"], "souri": "souris", "mouse": "souris",
            "clavier": ["clavier", "keyboard", "clavié"], "clavié": "clavier", "keyboard": "clavier",
            "écran": ["écran", "moniteur", "screen", "display"], "ecran": "écran",
            "moniteur": ["moniteur", "écran", "monitor"], "monitor": "moniteur",
            "casque": ["casque", "headset", "headphones"], "headset": "casque",
            "micro": ["micro", "microphone", "mic"], "microphone": ["microphone", "micro"],

            # ===== PROBLÈMES - CRASHES (50 variantes) =====
            "crash": ["crash", "plante", "freeze", "bug", "plantage"],
            "plante": ["plante", "crash", "freeze", "plantage"], "plantage": ["plantage", "crash"],
            "freeze": ["freeze", "bloqué", "gelé", "figé", "bloque"], "freze": "freeze",
            "bloqué": ["bloqué", "freeze", "bloque"], "bloque": "bloqué", "gelé": "freeze",
            "figé": "freeze", "fige": "freeze",

            "bug": ["bug", "erreur", "problème", "crash", "beug"], "beug": "bug",
            "bsod": ["bsod", "écran bleu", "blue screen", "ecran bleu"],
            "écran bleu": ["écran bleu", "bsod", "blue screen"], "ecran bleu": "écran bleu",
            "blue screen": "écran bleu", "bluescreen": "écran bleu",

            # ===== PROBLÈMES - PERFORMANCE (60 variantes) =====
            "lent": ["lent", "ralenti", "lag", "rame", "slow"], "ralenti": ["ralenti", "lent", "lag"],
            "lag": ["lag", "rame", "lent", "latence", "laggy"], "laggy": "lag",
            "rame": ["rame", "lag", "lent", "ralenti", "laggy"], "ram": ["rame", "lag"],

            "saccade": ["saccade", "freeze", "stutter", "micro-freeze", "saccades"],
            "saccades": "saccade", "stutter": ["stutter", "saccade", "micro-freeze"],
            "micro-freeze": ["micro-freeze", "saccade", "stutter"], "microfreeze": "micro-freeze",

            "fps": ["fps", "framerate", "images par seconde", "frame rate"],
            "framerate": "fps", "frame rate": "fps", "images": "fps",
            "fps bas": ["fps bas", "fps faible", "peu de fps"], "fps faible": "fps bas",

            # Latence
            "latence": ["latence", "ping", "lag", "délai"], "ping": ["ping", "latence", "ms"],
            "délai": "latence", "delai": "latence",

            # ===== PROBLÈMES - TEMPÉRATURE (40 variantes) =====
            "chauffe": ["chauffe", "surchauffe", "chaud", "température", "chaleur"],
            "surchauffe": ["surchauffe", "chauffe", "overheating", "overheat"],
            "surchofe": "surchauffe", "surchauf": "surchauffe", "sur chauffe": "surchauffe",
            "overheat": "surchauffe", "overheating": "surchauffe",

            "température": ["température", "temp", "chaleur", "heat"],
            "temperature": "température", "temperatur": "température", "temprature": "température",
            "temp": "température", "chaleur": ["chaleur", "température", "heat"],
            "chaud": ["chaud", "chauffe", "température", "hot"], "hot": "chaud",
            "brûlant": "chaud", "brulant": "chaud",

            # ===== PROBLÈMES - BRUIT (25 variantes) =====
            "bruyant": ["bruyant", "fort", "bruit", "loud", "bruy"], "bruy": "bruyant",
            "fort": ["fort", "bruyant", "bruit"], "bruit": ["bruit", "bruyant", "noise"],
            "loud": "bruyant", "noise": "bruit",

            "ventilo": ["ventilateur", "ventilo", "fan", "ventilos"],
            "ventilateur": ["ventilateur", "ventilo", "fan"], "ventilos": "ventilateur",
            "fan": "ventilateur", "fans": "ventilateur",
            "coil whine": ["coil whine", "sifflement", "bourdonnement"],

            # ===== ACTIONS - INSTALLATION (30 variantes) =====
            "installer": ["installer", "install", "installation", "installé"],
            "install": "installer", "installation": ["installation", "install", "installer"],
            "instalation": "installation", "instal": "installation", "instaler": "installer",
            "installé": "installer", "installe": "installer",

            "télécharger": ["télécharger", "download", "dl", "telecharger"],
            "telecharger": "télécharger", "download": "télécharger", "dl": "télécharger",

            # ===== ACTIONS - CONFIGURATION (35 variantes) =====
            "configurer": ["configurer", "configuration", "config", "setup", "parametrer"],
            "config": "configuration", "configuration": ["configuration", "config", "setup"],
            "setup": "configuration", "parametrer": "configurer", "paramètrer": "configurer",
            "paramètre": "configuration", "parametre": "configuration",
            "réglage": "configuration", "reglage": "configuration", "regler": "configurer",

            # ===== ACTIONS - OPTIMISATION (30 variantes) =====
            "optimiser": ["optimiser", "optimisation", "optim", "améliorer", "booster"],
            "optim": "optimisation", "optimisation": ["optimisation", "optim", "optimiser"],
            "améliorer": ["améliorer", "optimiser", "booster"], "ameliorer": "améliorer",
            "booster": ["booster", "optimiser", "améliorer"], "boost": "booster",
            "accélérer": ["accélérer", "optimiser", "rendre plus rapide"],
            "accelerer": "accélérer", "rapide": ["rapide", "rapide", "quick"],

            # ===== ACTIONS - NETTOYAGE (25 variantes) =====
            "nettoyer": ["nettoyer", "nettoyage", "clean", "cleanup", "cleaner"],
            "nettoyage": ["nettoyage", "cleanup", "clean"], "clean": "nettoyage",
            "cleanup": "nettoyage", "cleaner": "nettoyage",
            "supprimer": ["supprimer", "delete", "effacer"], "delete": "supprimer",
            "effacer": "supprimer", "vider": ["vider", "nettoyer", "cleanup"],

            # ===== ACTIONS - MISE À JOUR (30 variantes) =====
            "update": ["mettre à jour", "update", "upgrade", "maj"],
            "upgrade": ["mettre à jour", "upgrade", "update"], "maj": "mise à jour",
            "mise à jour": ["mise à jour", "update", "maj"], "mise a jour": "mise à jour",
            "mettre à jour": ["mettre à jour", "update", "maj"],
            "actualiser": "mettre à jour", "updater": "mettre à jour",

            # ===== TERMES TECHNIQUES - DRIVERS (25 variantes) =====
            "driver": ["driver", "pilote", "drivers", "pilotes"],
            "pilote": ["pilote", "driver"], "drivers": "driver", "pilotes": "pilote",
            "driveur": "driver", "driveurs": "driver",
            "driver graphique": ["driver graphique", "pilote gpu"],
            "driver audio": ["driver audio", "pilote audio"],

            # ===== TERMES TECHNIQUES - BIOS/UEFI (20 variantes) =====
            "bios": ["bios", "uefi", "firmware"], "uefi": ["uefi", "bios"],
            "firmware": ["firmware", "bios", "uefi"],
            "cmos": ["cmos", "bios battery"], "bootloader": ["bootloader", "boot"],

            # ===== TERMES TECHNIQUES - OVERCLOCKING (30 variantes) =====
            "overclock": ["overclock", "oc", "overclocking", "overclocker"],
            "oc": "overclock", "overclocking": "overclock", "overclocker": "overclock",
            "ovrclock": "overclock", "over clock": "overclock",

            "undervolt": ["undervolt", "undervolting", "sous-voltage"],
            "undervolting": "undervolt", "sous-voltage": "undervolt",

            # ===== TERMES TECHNIQUES - WINDOWS (35 variantes) =====
            "windows": ["windows", "win", "windows 10", "windows 11", "w10", "w11"],
            "win": "windows", "win10": "windows 10", "win11": "windows 11",
            "w10": "windows 10", "w11": "windows 11",
            "windows 10": ["windows 10", "win10", "w10"],
            "windows 11": ["windows 11", "win11", "w11"],

            "mise à jour windows": ["mise à jour windows", "windows update", "update windows"],
            "windows update": "mise à jour windows",

            # ===== PC & ORDINATEUR (20 variantes) =====
            "pc": ["pc", "ordinateur", "ordi", "machine", "computer"],
            "ordi": ["ordinateur", "pc", "ordi"], "ordinateur": ["ordinateur", "pc", "ordi"],
            "orditeur": "ordinateur", "ordinateure": "ordinateur",
            "machine": ["machine", "pc", "ordinateur"], "computer": "ordinateur",
            "setup": ["setup", "config pc", "configuration"],

            # ===== PROBLÈMES GÉNÉRAUX (25 variantes) =====
            "problème": ["problème", "pb", "souci", "soucis", "issue"],
            "probème": "problème", "probleme": "problème", "poblème": "problème",
            "pb": "problème", "soucis": "problème", "souci": "problème",
            "issue": "problème", "pblm": "problème",

            "erreur": ["erreur", "bug", "crash", "problème", "error"],
            "error": "erreur", "eror": "erreur", "ereur": "erreur",

            # ===== FONCTIONNEMENT (20 variantes) =====
            "marche": ["marche", "fonctionne", "works"], "fonctionne": ["fonctionne", "marche"],
            "marche pas": ["ne marche pas", "ne fonctionne pas", "marche pas", "fonctionne pas"],
            "ne marche pas": ["ne marche pas", "marche pas", "fonctionne pas"],
            "ne fonctionne pas": ["ne fonctionne pas", "marche pas"],
            "fonctionne pas": "ne fonctionne pas", "works": "fonctionne",

            # ===== QUESTIONS (25 variantes) =====
            "comment": ["comment", "coment", "commen", "comant"],
            "coment": "comment", "commen": "comment", "comant": "comment",
            "quoi": ["quoi", "koi", "kwa"], "koi": "quoi", "kwa": "quoi",
            "pourquoi": ["pourquoi", "pourkoi", "prkoi", "pk"],
            "pourkoi": "pourquoi", "prkoi": "pourquoi", "pk": "pourquoi",

            # ===== CHOIX & RECOMMANDATIONS (20 variantes) =====
            "meilleur": ["meilleur", "mieux", "best", "top"], "mieux": "meilleur",
            "best": "meilleur", "top": "meilleur",
            "choisir": ["choisir", "sélection", "sélectionner", "selection"],
            "selection": "sélection", "sélectionner": "choisir",
            "recommander": ["recommander", "recommandation", "conseil"],
            "conseil": "recommandation",
        }

        # Patterns pour chaque type d'intent
        self.intent_patterns = {
            "greeting": {
                "keywords": ["bonjour", "salut", "hello", "hey", "bonsoir", "coucou", "yo"],
                "patterns": [r"^(bonjour|salut|hey|hello|yo)", r"(ça va|comment ça va)"]
            },
            "thanks": {
                "keywords": ["merci", "super", "top", "génial", "parfait", "excellent", "cool"],
                "patterns": [r"merci", r"super", r"top", r"génial", r"parfait"]
            },
            "simple_question": {
                "keywords": ["c'est quoi", "qu'est-ce que", "qu'est ce que", "quelle est", "quel est", "definition"],
                "patterns": [r"c'est quoi", r"qu[''']est[\s-]?ce", r"quelle? est", r"définition"]
            },
            "comparison": {
                "keywords": ["vs", " ou ", "versus", "différence", "comparaison", "meilleur", "mieux"],
                "patterns": [r"\svs\s", r"\sou\s", r"différence entre", r"compara", r"meilleur"]
            },
            "troubleshooting": {
                "keywords": ["problème", "bug", "erreur", "ne marche pas", "marche pas", "crash", "bsod",
                           "freeze", "bloque", "plante", "redémarre", "écran bleu", "ne fonctionne pas",
                           "surchauffe", "chauffe", "chaud", "température", "chaleur", "brûlant"],
                "patterns": [r"problème", r"erreur", r"ne (marche|fonctionne) pas", r"crash", r"bsod",
                           r"freeze", r"bloque", r"plante", r"surchauffe", r"chauffe", r"température"]
            },
            "performance": {
                "keywords": ["lent", "ralenti", "rame", "fps", "lag", "saccade", "latence", "ping",
                           "performance", "optimiser", "accélérer", "rapide"],
                "patterns": [r"lent", r"ralenti", r"rame", r"\sfps\s", r"lag", r"saccade", r"latence"]
            },
            "recommendation": {
                "keywords": ["quel", "quelle", "meilleur", "recommande", "conseil", "acheter",
                           "choisir", "suggestion", "bon choix"],
                "patterns": [r"quel(le)?", r"meilleur", r"recommande", r"conseil", r"acheter", r"choisir"]
            },
            "how_to": {
                "keywords": ["comment", "tuto", "tutoriel", "guide", "installer", "configurer",
                           "faire", "procédure", "étapes"],
                "patterns": [r"comment", r"tuto", r"guide", r"installer", r"configurer"]
            }
        }

        # Keywords techniques pour détecter niveau expert
        self.expert_keywords = {
            # RAM & Memory
            "fclk", "infinity fabric", "xmp", "expo", "docp", "cl", "timings", "cas latency",
            "trcd", "trp", "tras", "gear mode", "command rate",

            # CPU
            "tctl", "tdie", "vrm", "llc", "load line", "vcore", "vdimm", "vccsa", "vccio",
            "pbo", "precision boost", "curve optimizer", "co", "ppt", "tdc", "edc",
            "avx", "avx2", "avx-512", "ipc", "cinebench", "aida64",

            # GPU
            "dlss", "frame generation", "ray tracing", "rt cores", "tensor cores",
            "nvenc", "cuda", "stream processors", "compute units", "vram",
            "memory bandwidth", "resizable bar", "sam", "smart access memory",

            # Storage
            "nvme", "pcie gen4", "pcie gen5", "dram cache", "slc cache", "tlc", "qlc",
            "tbw", "dwpd", "iops", "queue depth", "trim",

            # Motherboard
            "pcie bifurcation", "dimm.2", "vrm phases", "mosfet", "choke", "pwm controller",
            "bios flashback", "cmos", "uefi",

            # Software
            "registry", "regedit", "powershell", "cmd", "dism", "sfc",
            "kernel", "driver signature", "secure boot", "tpm", "bitlocker",
            "gpedit", "group policy", "services.msc", "msconfig",

            # Networking
            "qos", "upnp", "port forwarding", "nat", "dns", "dhcp", "ipv6",
            "tcp", "udp", "mtu", "mss", "bufferbloat",

            # Monitoring
            "hwinfo", "hwmonitor", "afterburner", "rivatuner", "rtss",
            "event viewer", "perfmon", "resource monitor"
        }

        # Catégories techniques (pour fuzzy matching)
        # Sera rempli dynamiquement depuis UnifiedKnowledgeBase
        self.technical_categories = []


    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """
        Calcule la distance de Levenshtein entre deux chaînes
        (nombre minimum d'opérations pour transformer s1 en s2)

        Args:
            s1: Première chaîne
            s2: Deuxième chaîne

        Returns:
            Distance de Levenshtein (int)
        """
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                # Coût insertion, deletion, substitution
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]


    def _similarity_ratio(self, s1: str, s2: str) -> float:
        """
        Calcule ratio de similarité entre deux chaînes (0.0 - 1.0)
        Utilise SequenceMatcher de difflib

        Args:
            s1: Première chaîne
            s2: Deuxième chaîne

        Returns:
            Ratio de similarité (0.0 = différent, 1.0 = identique)
        """
        return SequenceMatcher(None, s1.lower(), s2.lower()).ratio()


    def _fuzzy_match_word(self, word: str, target: str, threshold: float = 0.8) -> bool:
        """
        Vérifie si un mot matche une cible avec tolérance aux fautes

        Args:
            word: Mot à matcher
            target: Cible à comparer
            threshold: Seuil de similarité (0.0-1.0)

        Returns:
            True si match, False sinon
        """
        # Match exact
        if word.lower() == target.lower():
            return True

        # Fuzzy match avec ratio
        if self._similarity_ratio(word, target) >= threshold:
            return True

        # Distance Levenshtein (max 2 erreurs pour mots courts, 3 pour longs)
        max_distance = 2 if len(target) <= 6 else 3
        if self._levenshtein_distance(word.lower(), target.lower()) <= max_distance:
            return True

        return False


    def _expand_with_variants(self, user_message: str) -> str:
        """
        Expand le message avec variantes et synonymes pour améliorer matching

        Args:
            user_message: Message utilisateur original

        Returns:
            Message enrichi avec variantes
        """
        msg_lower = user_message.lower()
        expanded_parts = [msg_lower]

        # Ajouter variantes pour chaque mot trouvé
        words = msg_lower.split()

        for word in words:
            # Chercher dans dictionnaire de variantes
            if word in self.word_variants:
                variants = self.word_variants[word]

                # Si c'est une liste de variantes
                if isinstance(variants, list):
                    expanded_parts.extend(variants)
                # Si c'est une correction orthographique
                elif isinstance(variants, str):
                    expanded_parts.append(variants)

        return " ".join(expanded_parts)


    def set_categories(self, categories: List[str]):
        """
        Définit la liste des catégories pour fuzzy matching

        Args:
            categories: Liste des noms de catégories
        """
        self.technical_categories = categories


    def analyze(self, user_message: str) -> str:
        """
        Détecte le type de question (intent) avec fuzzy matching
        AMÉLIORATION V20.0: Tolère fautes d'orthographe et variantes

        Args:
            user_message: Message utilisateur

        Returns:
            Intent détecté parmi: greeting, thanks, simple_question, comparison,
            troubleshooting, performance, recommendation, how_to, general_question
        """
        msg_lower = user_message.lower()

        # Expand message avec variantes pour meilleur matching
        expanded_msg = self._expand_with_variants(user_message)

        # Scoring pour chaque intent
        scores = {}

        for intent, config in self.intent_patterns.items():
            score = 0

            # Score keywords avec fuzzy matching
            for keyword in config["keywords"]:
                # Match exact dans message original
                if keyword in msg_lower:
                    score += 2  # Match exact = bonus

                # Match exact dans message expanded
                elif keyword in expanded_msg:
                    score += 1.5

                # Fuzzy match pour tolérer fautes
                else:
                    words_in_msg = msg_lower.split()
                    for word in words_in_msg:
                        if self._fuzzy_match_word(word, keyword, threshold=0.85):
                            score += 1
                            break

            # Score patterns (regex) - toujours sur message original
            for pattern in config["patterns"]:
                if re.search(pattern, msg_lower, re.IGNORECASE):
                    score += 2  # Patterns comptent double

                # Essayer aussi sur expanded pour capturer variantes
                elif re.search(pattern, expanded_msg, re.IGNORECASE):
                    score += 1.5

            if score > 0:
                scores[intent] = score

        # Intent avec highest score
        if scores:
            best_intent = max(scores, key=scores.get)

            # Validation: certains intents ont priorité
            # Ex: troubleshooting prend le dessus si score >= 2
            if "troubleshooting" in scores and scores["troubleshooting"] >= 2:
                return "troubleshooting"

            # Performance prend dessus si FPS/lag mentionné
            if "performance" in scores and scores["performance"] >= 2:
                return "performance"

            return best_intent
        else:
            return "general_question"


    def detect_expertise(self, user_message: str, context: Optional[Dict] = None) -> str:
        """
        Détecte le niveau d'expertise utilisateur

        Args:
            user_message: Message utilisateur
            context: Contexte optionnel (historique, profil)

        Returns:
            Niveau: "beginner", "intermediate", "expert"
        """
        msg_lower = user_message.lower()

        # Compter keywords techniques experts
        expert_count = 0
        matched_keywords = []

        for keyword in self.expert_keywords:
            # Match exact ou avec bordures de mot
            pattern = r'\b' + re.escape(keyword) + r'\b'
            if re.search(pattern, msg_lower):
                expert_count += 1
                matched_keywords.append(keyword)

        # Vérifier historique context si fourni
        history_level = "beginner"
        if context:
            history_level = context.get("user_expertise_level", "beginner")

        # Patterns débutants
        beginner_patterns = [
            r"c'est quoi",
            r"je ne sais pas",
            r"je comprends pas",
            r"pour les nuls",
            r"simple",
            r"facile"
        ]

        beginner_count = sum(1 for p in beginner_patterns if re.search(p, msg_lower))

        # Décision niveau
        if expert_count >= 3:
            # 3+ keywords techniques = expert
            return "expert"
        elif expert_count >= 1 and beginner_count == 0:
            # 1-2 keywords techniques sans patterns débutants = intermediate
            return "intermediate"
        elif history_level == "expert" and expert_count >= 1:
            # Historique expert + au moins 1 keyword = expert
            return "expert"
        elif history_level == "intermediate" and expert_count >= 1:
            # Historique intermediate + keyword = intermediate
            return "intermediate"
        elif beginner_count >= 2:
            # Patterns débutants = beginner
            return "beginner"
        else:
            # Par défaut, utiliser historique ou beginner
            return history_level if context else "beginner"


    def fuzzy_match_category(self, user_query: str, threshold: float = 0.6) -> Optional[str]:
        """
        Match catégorie avec fuzzy matching natif (tolère typos)
        AMÉLIORATION V20.0: Utilise fuzzy matching natif sans dépendances

        Args:
            user_query: Requête utilisateur
            threshold: Score minimum (0.0-1.0) pour match

        Returns:
            Nom catégorie matchée ou None
        """
        if not self.technical_categories:
            return None

        query_lower = user_query.lower()
        best_match = None
        best_score = 0.0

        for category in self.technical_categories:
            cat_lower = category.lower()

            # Score 1: Match exact substring
            if cat_lower in query_lower or query_lower in cat_lower:
                return category  # Match parfait immédiat

            # Score 2: Similarity ratio global
            similarity = self._similarity_ratio(query_lower, cat_lower)

            # Score 3: Token-based matching (mots individuels)
            query_tokens = set(query_lower.replace("_", " ").split())
            cat_tokens = set(cat_lower.replace("_", " ").split())

            # Calculer ratio de tokens communs
            if len(cat_tokens) > 0:
                common_tokens = query_tokens & cat_tokens
                token_ratio = len(common_tokens) / len(cat_tokens)
            else:
                token_ratio = 0.0

            # Score 4: Fuzzy match sur chaque token
            fuzzy_token_matches = 0
            for q_token in query_tokens:
                for c_token in cat_tokens:
                    if self._fuzzy_match_word(q_token, c_token, threshold=0.8):
                        fuzzy_token_matches += 1
                        break

            fuzzy_token_ratio = fuzzy_token_matches / len(cat_tokens) if len(cat_tokens) > 0 else 0.0

            # Score final: moyenne pondérée
            final_score = (
                similarity * 0.3 +           # 30% similarité globale
                token_ratio * 0.4 +          # 40% tokens exacts communs
                fuzzy_token_ratio * 0.3      # 30% tokens fuzzy matchés
            )

            if final_score > best_score:
                best_score = final_score
                best_match = category

        # Retourner si score >= threshold
        if best_score >= threshold:
            return best_match

        return None


    def _fallback_category_match(self, user_query: str) -> Optional[str]:
        """
        Fallback matching si fuzzywuzzy indisponible
        Simple substring matching
        """
        query_lower = user_query.lower()

        # Match exact
        for category in self.technical_categories:
            if category.lower() in query_lower or query_lower in category.lower():
                return category

        # Match partiel (mots clés)
        query_words = set(query_lower.split())
        best_match = None
        best_score = 0

        for category in self.technical_categories:
            cat_words = set(category.lower().replace("_", " ").split())
            common = len(query_words & cat_words)

            if common > best_score:
                best_score = common
                best_match = category

        if best_score >= 2:  # Au moins 2 mots en commun
            return best_match

        return None


    def extract_keywords(self, user_message: str) -> List[str]:
        """
        Extrait keywords importants du message

        Args:
            user_message: Message utilisateur

        Returns:
            Liste de keywords extraits
        """
        # Mots vides à ignorer
        stopwords = {
            "le", "la", "les", "un", "une", "des", "de", "du", "mon", "ma", "mes",
            "ton", "ta", "tes", "son", "sa", "ses", "ce", "cette", "ces",
            "je", "tu", "il", "elle", "nous", "vous", "ils", "elles",
            "est", "sont", "a", "ont", "être", "avoir", "faire",
            "pour", "dans", "avec", "sur", "sous", "par", "sans",
            "que", "qui", "quoi", "comment", "pourquoi", "où", "quand"
        }

        # Tokenize
        words = re.findall(r'\b\w+\b', user_message.lower())

        # Filtrer stopwords et courts
        keywords = [w for w in words if w not in stopwords and len(w) >= 3]

        # Priorité aux keywords techniques
        technical_kw = [w for w in keywords if w in self.expert_keywords]
        other_kw = [w for w in keywords if w not in self.expert_keywords]

        # Technical d'abord, puis autres
        return technical_kw + other_kw[:10]  # Max 10 autres


    def detect_question_complexity(self, user_message: str, intent: str) -> str:
        """
        Détecte la complexité de la question

        Args:
            user_message: Message utilisateur
            intent: Intent détecté

        Returns:
            Complexité: "simple", "moderate", "complex"
        """
        msg_lower = user_message.lower()

        # Facteurs de complexité
        length = len(user_message)
        question_marks = user_message.count("?")
        conjunctions = sum(1 for c in [" et ", " ou ", " mais ", " donc "] if c in msg_lower)

        # Mots complexes
        complex_words = ["optimiser", "configuration", "performance", "diagnostic",
                        "troubleshooting", "comparaison", "analyse"]
        complex_count = sum(1 for w in complex_words if w in msg_lower)

        # Intent influence
        complex_intents = ["troubleshooting", "comparison", "recommendation"]
        simple_intents = ["greeting", "thanks", "simple_question"]

        # Scoring complexité
        complexity_score = 0

        if length > 100:
            complexity_score += 2
        elif length > 50:
            complexity_score += 1

        complexity_score += min(conjunctions, 3)  # Max +3
        complexity_score += complex_count

        if intent in complex_intents:
            complexity_score += 2
        elif intent in simple_intents:
            complexity_score -= 2

        # Décision
        if complexity_score >= 5:
            return "complex"
        elif complexity_score >= 2:
            return "moderate"
        else:
            return "simple"


    def suggest_clarification_questions(self, user_message: str, intent: str) -> List[str]:
        """
        Suggère questions de clarification si message vague

        Args:
            user_message: Message utilisateur
            intent: Intent détecté

        Returns:
            Liste de questions suggérées (vide si clair)
        """
        msg_lower = user_message.lower()
        questions = []

        # Troubleshooting vague
        if intent == "troubleshooting":
            if "pc" in msg_lower and len(user_message) < 30:
                questions.append("Depuis quand ça arrive?")
                questions.append("C'est sur un jeu précis ou aléatoire?")
                questions.append("T'as fait des changements récemment? (update, nouveau matériel)")

            if "lent" in msg_lower or "rame" in msg_lower:
                questions.append("C'est au démarrage, en jeu, ou tout le temps?")
                questions.append("Ça a commencé après quoi?")

        # Performance sans détails
        if intent == "performance":
            if "fps" in msg_lower and "jeu" not in msg_lower:
                questions.append("Sur quel jeu exactement?")
                questions.append("Quelles sont tes specs? (CPU, GPU, RAM)")

            if "lag" in msg_lower and "ping" not in msg_lower:
                questions.append("C'est du lag réseau (ping) ou FPS?")

        # Recommendation sans contexte
        if intent == "recommendation":
            if ("acheter" in msg_lower or "choisir" in msg_lower) and len(user_message) < 40:
                questions.append("Quel budget?")
                questions.append("C'est pour quoi? (gaming, travail, les deux)")

        return questions[:2]  # Max 2 questions


# Tests unitaires
if __name__ == "__main__":
    print("=" * 80)
    print("  TEST INTENT ANALYZER - NiTriTe V18.5")
    print("=" * 80)
    print()

    # Créer instance
    analyzer = IntentAnalyzer()

    # Test 1: Détection intent
    print("TEST 1: Détection Intent")
    print("-" * 80)

    test_messages = [
        ("Bonjour, j'ai besoin d'aide", "greeting"),
        ("Merci beaucoup!", "thanks"),
        ("C'est quoi la DDR5?", "simple_question"),
        ("RTX 4090 vs RX 7900 XTX", "comparison"),
        ("Mon PC crash avec un BSOD", "troubleshooting"),
        ("Mon jeu lag, j'ai des FPS bas", "performance"),
        ("Quel CPU choisir pour du gaming?", "recommendation"),
        ("Comment overclock ma RAM?", "how_to")
    ]

    for msg, expected in test_messages:
        detected = analyzer.analyze(msg)
        status = "✅" if detected == expected else "❌"
        print(f"{status} '{msg[:40]:<40}' → {detected:<20} (attendu: {expected})")

    # Test 2: Détection expertise
    print("\n" + "=" * 80)
    print("TEST 2: Détection Niveau Expertise")
    print("-" * 80)

    expertise_tests = [
        ("Mon PC est lent, comment faire?", "beginner"),
        ("Mes timings RAM sont CL16-18-18-38", "intermediate"),
        ("Curve Optimizer -30 sur tous les cores, PBO limits +200 PPT", "expert"),
        ("C'est quoi le XMP?", "beginner"),
        ("J'ai activé EXPO mais FCLK ne sync pas 1:1", "expert")
    ]

    for msg, expected_approx in expertise_tests:
        detected = analyzer.detect_expertise(msg)
        print(f"  '{msg[:50]:<50}' → {detected:<15} (attendu: ~{expected_approx})")

    # Test 3: Extraction keywords
    print("\n" + "=" * 80)
    print("TEST 3: Extraction Keywords")
    print("-" * 80)

    keyword_test = "Mon PC rame en jeu avec un i5-12400F et une RTX 3060"
    keywords = analyzer.extract_keywords(keyword_test)
    print(f"Message: '{keyword_test}'")
    print(f"Keywords: {keywords}")

    # Test 4: Complexité
    print("\n" + "=" * 80)
    print("TEST 4: Détection Complexité")
    print("-" * 80)

    complexity_tests = [
        "Salut!",
        "Mon PC est lent",
        "Mon PC rame en jeu, j'ai des saccades et les FPS chutent à 40 alors que j'ai une RTX 4070"
    ]

    for msg in complexity_tests:
        intent = analyzer.analyze(msg)
        complexity = analyzer.detect_question_complexity(msg, intent)
        print(f"  '{msg[:60]:<60}' → {complexity}")

    # Test 5: Fuzzy matching (fallback)
    print("\n" + "=" * 80)
    print("TEST 5: Fuzzy Category Matching (Fallback)")
    print("-" * 80)

    test_categories = [
        "cpu_intel_generations",
        "gpu_nvidia_rtx_40_series",
        "ram_ddr5_tuning",
        "windows_11_expert"
    ]

    analyzer.set_categories(test_categories)

    fuzzy_tests = [
        "intel cpu generations",
        "nvidia rtx 40",
        "ddr5 ram",
        "windows 11"
    ]

    for query in fuzzy_tests:
        matched = analyzer.fuzzy_match_category(query)
        print(f"  '{query:<30}' → {matched}")

    print("\n" + "=" * 80)
    print("  TESTS TERMINÉS!")
    print("=" * 80)
