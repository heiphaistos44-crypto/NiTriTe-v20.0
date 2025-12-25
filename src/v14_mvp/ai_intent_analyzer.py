#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyseur d'Intent pour Agent IA - NiTriTe V18.5
Détection intelligente de l'intent utilisateur et niveau d'expertise
Remplace pattern matching basique if/elif
"""

import re
from typing import Dict, Optional, Tuple, List


class IntentAnalyzer:
    """
    Analyse intelligente des messages utilisateur
    - Détection type de question (intent)
    - Détection niveau expertise (beginner/intermediate/expert)
    - Fuzzy matching catégories
    """

    def __init__(self):
        """Initialise les patterns d'intent et keywords d'expertise"""

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


    def set_categories(self, categories: List[str]):
        """
        Définit la liste des catégories pour fuzzy matching

        Args:
            categories: Liste des noms de catégories
        """
        self.technical_categories = categories


    def analyze(self, user_message: str) -> str:
        """
        Détecte le type de question (intent)

        Args:
            user_message: Message utilisateur

        Returns:
            Intent détecté parmi: greeting, thanks, simple_question, comparison,
            troubleshooting, performance, recommendation, how_to, general_question
        """
        msg_lower = user_message.lower()

        # Scoring pour chaque intent
        scores = {}

        for intent, config in self.intent_patterns.items():
            score = 0

            # Score keywords
            for keyword in config["keywords"]:
                if keyword in msg_lower:
                    score += 1

            # Score patterns (regex)
            for pattern in config["patterns"]:
                if re.search(pattern, msg_lower, re.IGNORECASE):
                    score += 2  # Patterns comptent double

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


    def fuzzy_match_category(self, user_query: str, threshold: int = 60) -> Optional[str]:
        """
        Match catégorie avec fuzzy matching (tolère typos)

        Args:
            user_query: Requête utilisateur
            threshold: Score minimum (0-100) pour match

        Returns:
            Nom catégorie matchée ou None
        """
        if not self.technical_categories:
            return None

        try:
            from fuzzywuzzy import fuzz, process

            # Fuzzy matching sur noms catégories
            best_match = process.extractOne(
                user_query,
                self.technical_categories,
                scorer=fuzz.token_sort_ratio
            )

            if best_match and best_match[1] >= threshold:
                return best_match[0]
            else:
                return None

        except ImportError:
            # Fallback si fuzzywuzzy pas installé
            return self._fallback_category_match(user_query)


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
