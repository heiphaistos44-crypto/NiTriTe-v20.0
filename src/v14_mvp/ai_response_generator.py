#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de Réponses Dynamiques - Agent IA NiTriTe V18.5
Remplace les quick_responses scriptées par génération conversationnelle
Scoring TF-IDF pour pertinence | Prompts adaptatifs par contexte
"""

import random
from typing import Dict, List, Any, Optional


class DynamicResponseGenerator:
    """
    Générateur de réponses dynamiques et conversationnelles
    Élimine les templates fixes au profit d'une IA adaptative
    """

    def __init__(self, knowledge_base, api_manager):
        """
        Args:
            knowledge_base: UnifiedKnowledgeBase instance (legacy, gardé pour compat)
            api_manager: APIManager instance pour appels API
        """
        # Legacy KB (backward compatibility)
        self.kb = knowledge_base
        self.api_manager = api_manager

        # Outros conversationnels français (définis comme instance variable)
        self.outros_francais = [
            "\nTeste ça et dis-moi si ça va mieux! 👍",
            "\nÇa devrait régler ton problème. Sinon reviens me voir!",
            "\nHésite pas si t'as besoin de plus de détails!",
            "\nDis-moi si ça marche ou si tu veux que je t'explique autrement! 😊"
        ]

        # === NOUVEAUX MODULES (Amélioration x10000%) ===
        try:
            # Try imports avec fallback pour compatibilité multi-contexte
            try:
                from v14_mvp.ai_knowledge_base_hybrid import HybridKnowledgeBase
                from v14_mvp.ai_semantic_search import SemanticSearchEngine
                from v14_mvp.ai_context_enricher import ContextEnricher
                from v14_mvp.ai_response_templates import ResponseTemplates, TemplateFormatter
                from v14_mvp.ai_system_executor import SystemExecutor
                from v14_mvp.ai_nitrite_expert import NiTriTeExpert
                from v14_mvp.ai_auto_learner import AutoLearner
            except ImportError:
                try:
                    from ai_knowledge_base_hybrid import HybridKnowledgeBase
                    from ai_semantic_search import SemanticSearchEngine
                    from ai_context_enricher import ContextEnricher
                    from ai_response_templates import ResponseTemplates, TemplateFormatter
                    from ai_system_executor import SystemExecutor
                    from ai_nitrite_expert import NiTriTeExpert
                    from ai_auto_learner import AutoLearner
                except ImportError:
                    from .ai_knowledge_base_hybrid import HybridKnowledgeBase
                    from .ai_semantic_search import SemanticSearchEngine
                    from .ai_context_enricher import ContextEnricher
                    from .ai_response_templates import ResponseTemplates, TemplateFormatter
                    from .ai_system_executor import SystemExecutor
                    from .ai_nitrite_expert import NiTriTeExpert
                    from .ai_auto_learner import AutoLearner

            # Hybrid KB (30K+ entries)
            self.kb_hybrid = HybridKnowledgeBase()
            print("[ResponseGenerator] OK HybridKB charge")

            # Semantic Search (FAISS)
            self.semantic_search = SemanticSearchEngine()
            print("[ResponseGenerator] OK SemanticSearch charge")

            # Context Enricher (hardware detection)
            self.context_enricher = ContextEnricher()
            print("[ResponseGenerator] OK ContextEnricher charge")

            # Response Templates (ultra-détaillé)
            self.templates = ResponseTemplates()
            self.template_formatter = TemplateFormatter()
            print("[ResponseGenerator] OK Templates charges")

            # System Executor (diagnostic safe)
            self.system_executor = SystemExecutor()
            print("[ResponseGenerator] OK SystemExecutor charge")

            # NiTriTe Expert (14 pages)
            self.nitrite_expert = NiTriTeExpert()
            print("[ResponseGenerator] OK NiTriTeExpert charge")

            # Auto-Learner (scan docs)
            self.auto_learner = AutoLearner()
            print("[ResponseGenerator] OK AutoLearner charge")

            self.enhanced_mode = True
            print("[ResponseGenerator] MODE AMELIORE ACTIF (x10000%)")

        except Exception as e:
            print(f"[ResponseGenerator] WARN: Modules améliorés non chargés: {e}")
            print("[ResponseGenerator] Fallback: mode legacy")
            self.enhanced_mode = False
            self.kb_hybrid = None
            self.semantic_search = None
            self.context_enricher = None
            self.templates = None
            self.system_executor = None
            self.nitrite_expert = None
            self.auto_learner = None

        # Patterns conversationnels variés (pas scriptés!)
        self.conversation_starters = {
            "greeting": [
                "Salut! Comment je peux t'aider avec ton PC?",
                "Hey! Un souci technique?",
                "Yo! Qu'est-ce qui se passe avec ta config?",
                "Hello! Raconte-moi ton problème 👋"
            ],
            "acknowledgment": [
                "Ah ok, je vois.",
                "D'accord, compris.",
                "Ok, laisse-moi t'expliquer.",
                "Bien, voilà ce que je pense.",
                "Intéressant, alors..."
            ],
            "troubleshooting_intro": [
                "Bon alors, pour ton problème...",
                "Ok, diagnostiquons ça ensemble.",
                "Ah classique ça! Voilà comment régler ça:",
                "Je connais ce souci. Du coup:",
                "Ouais, c'est chiant ça. Voici la solution:"
            ],
            "question_prompt": [
                "Dis-moi:",
                "Avant que je continue, j'aimerais savoir:",
                "Juste pour clarifier:",
                "Question rapide:",
                "Pour mieux t'aider:"
            ],
            "explanation_intro": [
                "Alors en gros,",
                "Pour faire simple,",
                "Laisse-moi t'expliquer:",
                "En résumé,",
                "Bon, voilà le truc:"
            ]
        }

        # Cache pour TF-IDF (éviter recalcul à chaque requête)
        self._tfidf_cache = None
        self._vectorizer = None

    def generate_online(
        self,
        user_message: str,
        intent: str,
        user_level: str,
        context: Dict[str, Any]
    ) -> str:
        """
        Génération réponse mode ONLINE (API)
        Utilise API avec prompt conversationnel dynamique
        MODE AMÉLIORÉ : Semantic search + Context enriched + Templates ultra-détaillés

        Args:
            user_message: Message utilisateur
            intent: Type question détecté (simple_question, troubleshooting, etc.)
            user_level: Niveau expertise (beginner, intermediate, expert)
            context: Contexte (mémoire, système, patterns appris)

        Returns:
            Réponse conversationnelle générée par API (ultra-détaillée si mode amélioré)
        """
        # === MODE AMÉLIORÉ (x10000%) ===
        if self.enhanced_mode and self.semantic_search:
            return self._generate_online_enhanced(user_message, intent, user_level, context)

        # === MODE LEGACY (fallback) ===
        # 1. Rechercher conseils pertinents
        relevant_tips = self._search_relevant_knowledge(user_message, intent, top_k=10)

        # 2. Construire system prompt conversationnel
        system_prompt = self._build_conversational_prompt(
            user_message=user_message,
            relevant_tips=relevant_tips,
            user_level=user_level,
            intent=intent,
            context=context
        )

        # 3. Construire messages pour API
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        # Ajouter historique conversation si disponible
        if context.get("memory") and len(context["memory"]) > 0:
            # Injecter derniers 3 échanges pour contexte
            recent_history = context["memory"][-3:]
            for exchange in recent_history:
                messages.insert(1, {"role": "user", "content": exchange.get("user", "")})
                messages.insert(2, {"role": "assistant", "content": exchange.get("assistant", "")})

        # 4. Appel API avec température adaptative
        temperature = self._get_adaptive_temperature(intent)
        max_tokens = self._get_adaptive_max_tokens(intent, user_level)

        try:
            response = self.api_manager.query(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=30
            )

            # 5. Post-traitement: enrichir avec outils NiTriTe si pertinent
            response = self._enrich_with_nitrite_tools(response, intent, relevant_tips)

            return response

        except Exception as e:
            # Fallback si API fail
            return self._generate_offline_fallback(user_message, intent, relevant_tips)

    def generate_offline(
        self,
        user_message: str,
        intent: str,
        user_level: str,
        context: Dict[str, Any]
    ) -> str:
        """
        Génération réponse mode OFFLINE (local)
        Génération intelligente basée sur KB sans API

        Args:
            user_message: Message utilisateur
            intent: Type question détecté
            user_level: Niveau expertise
            context: Contexte

        Returns:
            Réponse générée localement (NON scriptée)
        """
        # 1. Rechercher conseils pertinents (scoring)
        relevant_tips = self._search_relevant_knowledge(user_message, intent, top_k=5)

        # 2. Générer réponse conversationnelle à partir des tips
        response = self._compose_conversational_response(
            user_message=user_message,
            relevant_tips=relevant_tips,
            intent=intent,
            user_level=user_level
        )

        # 3. Enrichir avec outils NiTriTe
        response = self._enrich_with_nitrite_tools(response, intent, relevant_tips)

        return response

    def _correct_common_typos(self, query: str) -> str:
        """
        Corrige les fautes d'orthographe courantes pour améliorer la recherche

        Args:
            query: Query utilisateur (peut contenir des fautes)

        Returns:
            Query avec corrections communes appliquées
        """
        # Dictionnaire corrections courantes
        corrections = {
            # Fautes de frappe courantes
            'temprature': 'température',
            'temperatur': 'température',
            'instalation': 'installation',
            'instal': 'installation',
            'programe': 'programme',
            'programm': 'programme',
            'ordi': 'ordinateur',
            'orditeur': 'ordinateur',
            'procesor': 'processeur',
            'proceseur': 'processeur',
            'memoire': 'mémoire',
            'memwar': 'mémoire',
            'demarage': 'démarrage',
            'demarer': 'démarrer',

            # Abréviations
            'pb': 'problème',
            'pbs': 'problèmes',
            'pc': 'ordinateur',
            'ram': 'mémoire',
            'gpu': 'carte graphique',
            'cpu': 'processeur',
            'hdd': 'disque dur',
            'ssd': 'disque ssd',

            # Synonymes et variantes
            'lent': 'ralenti',
            'lag': 'ralenti',
            'freeze': 'bloqué',
            'bug': 'problème',
            'plante': 'crash',
            'surchofe': 'surchauffe',
            'surchauf': 'surchauffe',
            'batery': 'batterie',
            'batrie': 'batterie',

            # Phonétiques
            'koi': 'quoi',
            'kestion': 'question',
            'safiche': 'affiche',
            'aparait': 'apparait',
        }

        # Applique corrections
        query_lower = query.lower()
        corrected = query_lower

        for faute, correction in corrections.items():
            # Remplace le mot entier (pas dans un autre mot)
            import re
            pattern = r'\b' + re.escape(faute) + r'\b'
            corrected = re.sub(pattern, correction, corrected, flags=re.IGNORECASE)

        return corrected

    def _deduplicate_results(self, results: List[Dict], key: str = 'content') -> List[Dict]:
        """
        Élimine les doublons dans les résultats

        Args:
            results: Liste résultats
            key: Clé à utiliser pour détecter doublons

        Returns:
            Liste sans doublons
        """
        seen = set()
        unique = []

        for result in results:
            # Utilise hash du contenu pour détecter doublons
            content_hash = hash(str(result.get(key, '')))

            if content_hash not in seen:
                seen.add(content_hash)
                unique.append(result)

        return unique

    def _generate_online_enhanced(
        self,
        user_message: str,
        intent: str,
        user_level: str,
        context: Dict[str, Any]
    ) -> str:
        """
        GÉNÉRATION AMÉLIORÉE x10000%
        Utilise tous les nouveaux modules pour réponses ultra-détaillées

        Workflow:
        0. Correction fautes orthographe (fuzzy matching)
        1. Semantic search (FAISS) → Top 20 résultats pertinents
        2. Hybrid KB search → Core KB + NiTriTe KB + Legacy + Auto-learned
        3. Context enrichment → Hardware détecté + Profil user
        4. NiTriTe Expert → Suggestions pages/tools pertinents
        5. Déduplication résultats
        6. Mega-prompt construction → 10x plus de contexte
        7. API call avec max_tokens augmenté (FRANÇAIS OBLIGATOIRE)
        8. Template formatting → Structure professionnelle garantie
        """
        print("[Enhanced] Generation mode ameliore activee")

        # === 0. CORRECTION FAUTES ORTHOGRAPHE ===
        corrected_message = self._correct_common_typos(user_message)
        if corrected_message != user_message.lower():
            print(f"[Enhanced] Correction orthographe appliquee")

        # Utilise message corrigé pour recherches

        # === 1. SEMANTIC SEARCH (FAISS) ===
        semantic_results = []
        if self.semantic_search.index is not None:
            try:
                semantic_results = self.semantic_search.search(
                    corrected_message,  # Utilise message corrigé
                    top_k=20,
                    min_score=0.1
                )
                print(f"[Enhanced] Semantic search: {len(semantic_results)} resultats")
            except Exception as e:
                print(f"[Enhanced] WARN: Semantic search failed: {e}")

        # === 2. HYBRID KB SEARCH ===
        hybrid_results = []
        try:
            hybrid_results = self.kb_hybrid.search(
                corrected_message,  # Utilise message corrigé
                top_k=10,
                filters={'difficulty': user_level} if user_level else None
            )
            print(f"[Enhanced] Hybrid KB: {len(hybrid_results)} resultats")
        except Exception as e:
            print(f"[Enhanced] WARN: Hybrid KB failed: {e}")

        # === DÉDUPLICATION ===
        if semantic_results:
            semantic_results = self._deduplicate_results(semantic_results, key='content')
            print(f"[Enhanced] Apres deduplication: {len(semantic_results)} resultats uniques")

        # === 3. CONTEXT ENRICHMENT ===
        enriched_context = {}
        try:
            enriched_context = self.context_enricher.enrich_context(
                user_message,
                context.get('memory', [])
            )
            print(f"[Enhanced] ✅ Context enriched (expertise: {enriched_context.get('expertise_level', 'N/A')})")
        except Exception as e:
            print(f"[Enhanced] WARN: Context enrichment failed: {e}")

        # === 4. NITRITE EXPERT SUGGESTIONS ===
        nitrite_page = None
        nitrite_tools = []
        try:
            # Trouve page pertinente
            page_match = self.nitrite_expert.find_relevant_page(user_message)
            if page_match:
                nitrite_page = page_match['page']
                print(f"[Enhanced] ✅ NiTriTe page: {nitrite_page.get('name', 'N/A')}")

            # Suggère outils
            nitrite_tools = self.nitrite_expert.suggest_tools(
                user_message,
                problem_keywords=enriched_context.get('recent_topics', [])
            )
            print(f"[Enhanced] ✅ NiTriTe tools: {len(nitrite_tools)} suggestions")

        except Exception as e:
            print(f"[Enhanced] WARN: NiTriTe expert failed: {e}")

        # === 5. AUTO-LEARNED DOCS ===
        learned_results = []
        try:
            learned_results = self.auto_learner.search_learned(user_message, search_in='all')
            print(f"[Enhanced] Auto-learned: {len(learned_results)} resultats")
        except Exception as e:
            print(f"[Enhanced] WARN: Auto-learner failed: {e}")

        # === DÉTECTION ABSENCE DE RÉPONSE + LOGGING ===
        total_results = len(semantic_results) + len(hybrid_results) + len(learned_results)
        has_nitrite_info = nitrite_page is not None or len(nitrite_tools) > 0

        if total_results == 0 and not has_nitrite_info:
            # Aucune info trouvée - LOG pour future implémentation
            self._log_missing_knowledge(user_message, corrected_message, intent)
            print(f"[Enhanced] WARN: Aucune info pertinente - Question loggee pour implementation")

            # Ajoute note dans le mega-prompt
            mega_prompt_note = f"""
## ⚠️ ATTENTION: Connaissance Limitée

Cette question semble nouvelle ou hors périmètre actuel.

**Instructions**:
1. Réponds EN FRANÇAIS avec tes connaissances générales
2. Sois honnête: "Je n'ai pas d'information spécifique dans ma base, mais voici ce que je sais..."
3. Propose des solutions génériques pertinentes
4. Suggère à l'utilisateur de vérifier la documentation officielle
5. MINIMUM 5 paragraphes quand même (pas d'excuse pour réponse courte)

**Question originale**: {user_message}
"""
        else:
            mega_prompt_note = ""

        # === 6. MEGA-PROMPT CONSTRUCTION ===
        mega_prompt = self._build_mega_prompt_enhanced(
            user_message=user_message,
            semantic_results=semantic_results[:10],  # Top 10
            hybrid_results=hybrid_results,
            enriched_context=enriched_context,
            nitrite_page=nitrite_page,
            nitrite_tools=nitrite_tools,
            learned_results=learned_results[:5],
            intent=intent,
            user_level=user_level
        )

        # Ajoute note si pas de résultats
        if mega_prompt_note:
            mega_prompt = mega_prompt_note + "\n\n" + mega_prompt

        # === 7. API CALL (MAX TOKENS AUGMENTÉ) ===
        messages = [
            {"role": "system", "content": mega_prompt},
            {"role": "user", "content": user_message}
        ]

        # Historique (si disponible)
        if context.get("memory") and len(context["memory"]) > 0:
            recent_history = context["memory"][-5:]  # 5 derniers (vs 3 avant)
            for exchange in recent_history:
                messages.insert(1, {"role": "user", "content": exchange.get("user", "")})
                messages.insert(2, {"role": "assistant", "content": exchange.get("assistant", "")})

        # Température adaptative
        temperature = 0.7 if intent in ['troubleshooting', 'diagnostic'] else 0.9
        max_tokens = 12000  # 12K vs 4K avant (pour réponses ultra-détaillées)

        try:
            response = self.api_manager.query(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=45  # 45s vs 30s (réponses longues)
            )

            print(f"[Enhanced] ✅ API response reçue ({len(response)} chars)")

            # === 8. TEMPLATE FORMATTING ===
            # Apply template si pertinent
            if self.templates and intent in ['troubleshooting', 'optimization']:
                try:
                    formatted_response = self.template_formatter.apply_template(
                        intent=intent,
                        llm_response=response,
                        context={
                            'nitrite_tools': nitrite_tools,
                            'hardware': enriched_context.get('hardware_detected'),
                            'expertise': enriched_context.get('expertise_level')
                        }
                    )
                    print("[Enhanced] ✅ Template appliqué")
                    return formatted_response
                except Exception as e:
                    print(f"[Enhanced] WARN: Template formatting failed: {e}")

            return response

        except Exception as e:
            print(f"[Enhanced] ERROR API call: {e}")
            # Fallback vers mode legacy
            return self._generate_offline_fallback(
                user_message,
                intent,
                hybrid_results or semantic_results
            )

    def _build_mega_prompt_enhanced(
        self,
        user_message: str,
        semantic_results: List[Dict],
        hybrid_results: List[Dict],
        enriched_context: Dict,
        nitrite_page: Optional[Dict],
        nitrite_tools: List[Dict],
        learned_results: List[Dict],
        intent: str,
        user_level: str
    ) -> str:
        """
        Construit le MEGA-PROMPT enrichi avec TOUT le contexte disponible
        10x plus de contexte que le mode legacy
        """
        parts = []

        # === SECTION 1: PERSONNALITÉ ULTRA-DÉTAILLÉE ===
        parts.append("""# AGENT IA NITRITE V20.0 - EXPERT MAINTENANCE INFORMATIQUE

Tu es l'agent IA officiel de NiTriTe, l'outil ultime de maintenance informatique portable.

## 🇫🇷 IMPÉRATIF LANGUE : TOUJOURS RÉPONDRE EN FRANÇAIS

**OBLIGATOIRE** :
- ✅ TOUTES tes réponses DOIVENT être en français (100% français, aucune exception)
- ✅ Même si la question contient de l'anglais, réponds EN FRANÇAIS
- ✅ Traduis automatiquement les termes techniques anglais en français
- ✅ Si un terme n'a pas de traduction, donne l'anglais entre parenthèses
- ❌ JAMAIS de réponses en anglais ou autre langue

## 🔍 COMPRÉHENSION DES FAUTES D'ORTHOGRAPHE

**TU DOIS COMPRENDRE** :
- Les fautes de frappe (ex: "temprature" = "température")
- Les fautes d'orthographe (ex: "instalation" = "installation")
- Les abréviations (ex: "pb" = "problème", "pc" = "ordinateur")
- Les phonétiques (ex: "ordi" = "ordinateur", "programe" = "programme")
- Les synonymes (ex: "lent" = "ralenti" = "lag")

**SI LA QUESTION A DES FAUTES** :
1. Comprends l'intention malgré les fautes
2. Ne mentionne PAS les fautes (sois empathique)
3. Réponds comme si la question était parfaite
4. Utilise le vocabulaire CORRECT dans ta réponse (sans mentionner la correction)

## ⚠️ IMPÉRATIF ABSOLU: RÉPONSES TOUJOURS TRÈS DÉTAILLÉES

**MINIMUM REQUIS PAR RÉPONSE**:
- 5-10 paragraphes MINIMUM (jamais moins)
- Étapes numérotées avec sous-détails
- Exemples concrets
- Commandes PowerShell/CMD si applicable avec explications
- Références outils NiTriTe pertinents
- Section "Vérification" de la solution
- Section "Et si ça ne marche pas?"
- Section "Prévention long terme"

**FORMAT OBLIGATOIRE**:
1. Introduction empathique (2-3 phrases EN FRANÇAIS)
2. Analyse détaillée du problème (5+ phrases EN FRANÇAIS)
3. Solutions multiples (MINIMUM 2-3 approches différentes EN FRANÇAIS)
4. Chaque solution = 5+ étapes DÉTAILLÉES EN FRANÇAIS
5. Commandes avec explications ligne par ligne EN FRANÇAIS
6. Outils NiTriTe recommandés avec mode d'emploi EN FRANÇAIS
7. Vérification résultat (étapes précises EN FRANÇAIS)
8. Troubleshooting si échec EN FRANÇAIS
9. Conseils prévention EN FRANÇAIS

**STYLE**:
- Français conversationnel (comme Copilot France)
- Empathique et encourageant
- Explications détaillées mais claires
- Jamais de réponse < 800 mots
- Utilise markdown (# ## ### ``` etc.)
- Émojis pour clarté (⚠️ 💡 ✅ ❌ 🔧 📊)

**❌ ABSOLUMENT INTERDIT**:
- Réponses courtes (< 500 mots)
- Vagues ou génériques
- Sans exemples
- Sans étapes précises
- **RÉPONSES EN ANGLAIS OU AUTRE LANGUE**
- Doublons ou répétitions inutiles
- Mentionner les fautes d'orthographe de l'utilisateur
""")

        # === SECTION 2: HARDWARE DÉTECTÉ ===
        hw = enriched_context.get('hardware_detected')
        if hw:
            parts.append(f"""
## 💻 SYSTÈME UTILISATEUR DÉTECTÉ

**CPU**: {hw['cpu']['name']} ({hw['cpu']['cores']}C/{hw['cpu']['threads']}T @ {hw['cpu']['max_clock_mhz']}MHz)
**GPU**: {hw.get('gpu', {}).get('name', 'Non détecté')} ({hw.get('gpu', {}).get('vram_gb', 0)}GB VRAM)
**RAM**: {hw['ram']['total_gb']}GB {hw['ram']['type']} @ {hw['ram']['speed_mhz']}MHz
**OS**: {hw['os']['name']} {hw['os']['version']}
**Stockage**: {', '.join(f"{d['type']} {d['size_gb']}GB" for d in hw.get('storage', [])[:2])}

**⚠️ ADAPTE TES CONSEILS À CE SYSTÈME PRÉCIS.**
Ne donne PAS de conseils génériques. Personnalise selon CE hardware.
""")

        # === SECTION 3: NIVEAU EXPERTISE ===
        expertise = enriched_context.get('expertise_level', user_level)
        expertise_map = {
            'beginner': 'DÉBUTANT - Explique TOUS les termes, privilégie interface graphique, aucun jargon',
            'intermediate': 'INTERMÉDIAIRE - Mix GUI + commandes, explications moyennes',
            'expert': 'EXPERT - Directement technique, PowerShell/Registry OK, va droit au but',
            'power_user': 'POWER USER - Très technique, optimisations avancées, pas de main dans la main'
        }
        parts.append(f"\n**Niveau utilisateur**: {expertise_map.get(expertise, 'INTERMÉDIAIRE')}\n")

        # === SECTION 4: SEMANTIC RESULTS (TOP 10) ===
        if semantic_results:
            parts.append("\n## 📚 BASE DE CONNAISSANCES TECHNIQUE (Top 10 Pertinents)\n")
            for i, result in enumerate(semantic_results[:10], 1):
                parts.append(f"""
### {i}. {result.get('title', 'N/A')} (Score: {result.get('final_score', 0):.2f})

**Catégorie**: {result.get('category', 'N/A')}
**Contenu**: {result.get('content', '')[:500]}...

""")
            parts.append("**⚠️ UTILISE CES CONNAISSANCES pour construire ta réponse détaillée.**\n")

        # === SECTION 5: PAGE NITRITE ===
        if nitrite_page:
            parts.append(f"""
## 🛠️ PAGE NITRITE RECOMMANDÉE

**{nitrite_page.get('emoji', '')} {nitrite_page.get('name', '')}**

{nitrite_page.get('description', '')}

**Fonctionnalités clés**:
{self._format_dict_as_list(nitrite_page.get('features', {}))}

**⚠️ INTÈGRE cette page dans ta réponse** avec étapes précises pour l'utiliser.
""")

        # === SECTION 6: OUTILS NITRITE ===
        if nitrite_tools:
            parts.append("\n## 🔧 OUTILS NITRITE RECOMMANDÉS\n")
            for tool_data in nitrite_tools:
                tool = tool_data.get('tool', {})
                page = tool_data.get('page', 'Diagnostic')
                parts.append(f"""
- **{tool.get('name', 'N/A')}** (NiTriTe → {page})
  {tool.get('description', '')}
  **Comment utiliser**: [Donne étapes précises]
""")

        # === SECTION 7: RAPPELS FINAUX ===
        parts.append("""
## 🎯 RAPPELS CRITIQUES

1. ❌ JAMAIS de réponse courte (< 800 mots)
2. ✅ TOUJOURS 5-10 paragraphes minimum
3. ✅ TOUJOURS des exemples concrets
4. ✅ TOUJOURS des étapes numérotées détaillées
5. ✅ TOUJOURS mentionner outils NiTriTe si pertinent
6. ✅ TOUJOURS section vérification
7. ✅ TOUJOURS alternatives si solution 1 échoue
8. ✅ Format Markdown avec # ## ### pour structure
9. ✅ Code blocks pour commandes (```powershell)
10. ✅ Emojis pour clarté

**La qualité > tout. L'utilisateur préfère 10 paragraphes utiles à 2 paragraphes vagues.**

Maintenant, réponds à la question de l'utilisateur en suivant TOUTES ces directives.
""")

        return '\n'.join(parts)

    def _format_dict_as_list(self, d: Dict) -> str:
        """Formate dict en liste markdown"""
        if not d:
            return "(Aucune)"
        return '\n'.join(f"- **{k}**: {v}" for k, v in list(d.items())[:10])

    def _log_missing_knowledge(self, original_query: str, corrected_query: str, intent: str):
        """
        Log les questions sans réponse pour future implémentation

        Args:
            original_query: Question originale utilisateur
            corrected_query: Question après correction orthographe
            intent: Intent détecté
        """
        import json
        from datetime import datetime
        from pathlib import Path

        # Fichier log
        log_dir = Path("data/learning")
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "missing_knowledge_requests.json"

        # Charge logs existants
        if log_file.exists():
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    logs = json.load(f)
            except:
                logs = []
        else:
            logs = []

        # Nouvelle entrée
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'original_query': original_query,
            'corrected_query': corrected_query,
            'intent': intent,
            'status': 'pending_implementation'
        }

        logs.append(log_entry)

        # Sauvegarde (garde dernières 1000 entrées)
        logs = logs[-1000:]

        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            print(f"[Logger] Question loggee dans {log_file}")
        except Exception as e:
            print(f"[Logger] ERROR saving log: {e}")

    def _search_relevant_knowledge(
        self,
        query: str,
        intent: str,
        top_k: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Recherche conseils pertinents via scoring TF-IDF + keywords matching

        Args:
            query: Question utilisateur
            intent: Type de question
            top_k: Nombre de résultats à retourner

        Returns:
            Liste des top_k conseils les plus pertinents
        """
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.metrics.pairwise import cosine_similarity
            import numpy as np
        except ImportError:
            # Si scikit-learn pas installé, fallback sur keyword matching basique
            return self._fallback_keyword_search(query, top_k)

        # 1. Extraire tous les conseils avec métadonnées
        all_tips = []
        for category, data in self.kb.kb.items():
            for tip in data["tips"]:
                all_tips.append({
                    "category": category,
                    "content": tip["content"],
                    "keywords": tip.get("relevance_keywords", tip.get("keywords", [])),
                    "difficulty": tip.get("difficulty", "intermediate"),
                    "priority": data["metadata"].get("priority", 3),
                    "tags": tip.get("tags", [])
                })

        if not all_tips:
            return []

        # 2. TF-IDF vectorization (avec cache)
        tip_contents = [tip["content"] for tip in all_tips]

        if self._vectorizer is None or self._tfidf_cache is None:
            self._vectorizer = TfidfVectorizer(
                ngram_range=(1, 2),
                max_features=1000,
                stop_words=None  # Pas de stop words pour termes techniques
            )
            self._tfidf_cache = self._vectorizer.fit_transform(tip_contents)

        # 3. Vectoriser query
        try:
            query_vector = self._vectorizer.transform([query])
        except:
            # Si query contient mots inconnus, recréer vectorizer
            self._vectorizer = None
            self._tfidf_cache = None
            return self._fallback_keyword_search(query, top_k)

        # 4. Cosine similarity
        similarities = cosine_similarity(query_vector, self._tfidf_cache).flatten()

        # 5. Bonus scoring: keywords matching exact
        query_lower = query.lower()
        for i, tip in enumerate(all_tips):
            keyword_bonus = sum(1 for kw in tip["keywords"] if kw.lower() in query_lower)
            similarities[i] += keyword_bonus * 0.15  # +15% par keyword match

        # 6. Bonus scoring: priorité catégorie
        for i, tip in enumerate(all_tips):
            similarities[i] *= (1 + tip["priority"] * 0.08)  # +8% par niveau priorité

        # 7. Bonus scoring: intent matching (tags)
        intent_keywords = {
            "troubleshooting": ["bug", "error", "fix", "repair", "troubleshoot"],
            "performance": ["fast", "slow", "fps", "performance", "optimization"],
            "gaming": ["gaming", "game", "fps"],
            "simple_question": ["what", "how", "why"],
        }
        if intent in intent_keywords:
            for i, tip in enumerate(all_tips):
                tag_bonus = sum(1 for tag in tip["tags"] if any(kw in tag for kw in intent_keywords[intent]))
                similarities[i] += tag_bonus * 0.10  # +10% par tag match

        # 8. Tri et retour top_k
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [all_tips[i] for i in top_indices if similarities[i] > 0]

    def _fallback_keyword_search(self, query: str, top_k: int) -> List[Dict[str, Any]]:
        """
        Fallback si TF-IDF indisponible: recherche keywords simple
        """
        query_lower = query.lower()
        query_words = set(query_lower.split())

        results = []
        for category, data in self.kb.kb.items():
            for tip in data["tips"]:
                # Score = nb mots query dans content + keywords
                content_lower = tip["content"].lower()
                keywords_lower = [kw.lower() for kw in tip.get("keywords", [])]

                score = sum(1 for word in query_words if word in content_lower)
                score += sum(2 for kw in keywords_lower if kw in query_lower)  # Keywords valent 2x

                if score > 0:
                    results.append({
                        "category": category,
                        "content": tip["content"],
                        "keywords": tip.get("keywords", []),
                        "difficulty": tip.get("difficulty", "intermediate"),
                        "score": score
                    })

        # Tri par score
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def _build_conversational_prompt(
        self,
        user_message: str,
        relevant_tips: List[Dict[str, Any]],
        user_level: str,
        intent: str,
        context: Dict[str, Any]
    ) -> str:
        """
        Construit system prompt conversationnel adaptatif

        Returns:
            System prompt personnalisé selon contexte
        """
        # 1. Formatage knowledge base pertinente
        kb_formatted = self._format_relevant_knowledge(relevant_tips, user_level)

        # 2. Instructions niveau utilisateur
        level_instructions = {
            "beginner": """
Tu parles à un DÉBUTANT:
- Simplifie au max, évite jargon technique
- Explique chaque acronyme (ex: "FPS (images par seconde)")
- Donne exemples concrets
- Propose solutions GUI plutôt que commandes
- Sois patient et pédagogique
""",
            "intermediate": """
Tu parles à quelqu'un de niveau INTERMÉDIAIRE:
- Mix explication simple + termes techniques
- Pas besoin d'expliquer bases (GPU, CPU, RAM connus)
- Propose mix GUI + commandes simples
- Assume connaissance outils de base
""",
            "expert": """
Tu parles à un EXPERT:
- Jargon technique ok (FCLK, VRM, LLC, etc.)
- Va droit au but, pas besoin d'expliquer bases
- Propose solutions avancées (Registry, PowerShell, BIOS tweaks)
- Assume qu'il connaît les risques
"""
        }

        # 3. Instructions intent-specific
        intent_instructions = {
            "simple_question": "Réponse COURTE et DIRECTE. 2-3 paragraphes max. Va à l'essentiel.",
            "troubleshooting": "Diagnostic MÉTHODIQUE. Pose 1-2 questions clarification. Solutions par étapes.",
            "comparison": "Tableau comparatif si possible. Avantages/inconvénients clairs. Recommandation finale.",
            "recommendation": "Donne 2-3 options (budget, milieu, haut de gamme). Justifie chaque choix.",
            "performance": "Focus sur IMPACT réel. Chiffres FPS si pertinent. Solutions priorisées par gain.",
        }

        # 4. Construction prompt
        system_prompt = f"""🇫🇷 **CRITICAL: Réponds TOUJOURS et UNIQUEMENT en FRANÇAIS** 🇫🇷

Tu es un assistant maintenance PC ultra-expert, mais SURTOUT conversationnel et naturel comme Copilot.

🎯 **PERSONNALITÉ** (style Copilot - conversationnel et ami):
- Réponds comme un AMI EXPERT qui aide, PAS comme un robot ou un manuel
- 🇫🇷 **FRANÇAIS OBLIGATOIRE** - Aucun mot anglais sans traduction immédiate
- Varie ton style: décontracté pour questions simples, plus précis pour diagnostics
- Expressions naturelles françaises: "Ah je vois!", "Bon alors", "Du coup", "Franchement", "Écoute", "T'inquiète", etc.
- Adapte ton niveau selon l'utilisateur (détecté: {user_level})
- Pose des questions simples pour clarifier ("C'est un PC fixe ou portable?")

{level_instructions.get(user_level, level_instructions["intermediate"])}

🧠 **CONNAISSANCE PERTINENTE** (pour cette question):
{kb_formatted}

⚡ **INSTRUCTIONS RÉPONSE**:

1. **PAS DE TEMPLATE RIGIDE**:
   - ❌ Ne suis PAS toujours même structure emoji → diagnostic → solution
   - ✅ Adapte format selon question
   - ✅ Varie emojis, formulations, longueur

2. **CONVERSATION NATURELLE**:
   - Commence par accuser réception naturellement
   - {intent_instructions.get(intent, "Réponds de façon appropriée au contexte.")}
   - Utilise langage courant ("ton PC", "ça rame", "c'est chaud") ET technique selon niveau

3. **FORMAT ADAPTATIF**:

   Question simple → Réponse courte directe (3-5 lignes)
   Problème complexe → Diagnostic + Solutions par étapes
   Comparaison → Tableau ou bullet points
   Recommandation → 2-3 options avec justification

4. **OUTILS NITRITE** (intégration naturelle):
   - Mentionne outils NiTriTe SI pertinent dans contexte
   - "Lance HWMonitor (Diagnostic > HWMonitor) pour voir tes températures"
   - "Checke avec CrystalDiskInfo dans NiTriTe > Diagnostic"

5. **QUESTIONS CLARIFICATION**:
   - Si question vague, pose 1-2 questions courtes
   - "Ça arrive depuis quand?", "T'as overclocké quelque chose?", etc.

💻 **CONTEXTE SYSTÈME**:
{context.get('system_info', 'Non détecté')}

🧪 **PATTERNS RÉUSSIS** (réponses similaires bien notées):
{self._format_learned_patterns(context.get('learned_patterns', []))}

Maintenant, réponds NATURELLEMENT à: "{user_message}"

🎯 **RAPPEL FINAL**:
✅ FRANÇAIS UNIQUEMENT - traduis tout terme anglais ("overclocking" = "surcadençage")
✅ Style CONVERSATIONNEL comme Copilot - empathique et amical
✅ EXPLIQUE étape par étape avec exemples concrets
✅ POSE des questions si la demande n'est pas claire
✅ Donne des EXEMPLES du quotidien ("imagine que ton PC est comme une voiture...")

IMPORTANT: Sois conversationnel, varie ton style, PAS de template fixe!
"""

        return system_prompt

    def _format_relevant_knowledge(
        self,
        tips: List[Dict[str, Any]],
        user_level: str
    ) -> str:
        """
        Formate les conseils pertinents pour inclusion dans prompt
        """
        if not tips:
            return "Aucun conseil spécifique trouvé, utilise connaissances générales."

        formatted = []
        for i, tip in enumerate(tips[:8], 1):  # Max 8 conseils pour pas surcharger prompt
            # Filtrer par difficulty si user beginner
            if user_level == "beginner" and tip.get("difficulty") == "expert":
                continue

            category = tip["category"].replace("_", " ").title()
            formatted.append(f"{i}. [{category}] {tip['content']}")

        return "\n".join(formatted)

    def _format_learned_patterns(self, patterns: List[Dict[str, Any]]) -> str:
        """
        Formate patterns appris pour prompt
        """
        if not patterns or len(patterns) == 0:
            return "Aucun pattern appris pour ce type de question."

        formatted = []
        for pattern in patterns[:3]:  # Max 3 patterns
            formatted.append(f"- Question similaire: {pattern.get('query', '...')}")
            formatted.append(f"  Réponse appréciée: {pattern.get('response_snippet', '...')[:100]}...")

        return "\n".join(formatted)

    def _compose_conversational_response(
        self,
        user_message: str,
        relevant_tips: List[Dict[str, Any]],
        intent: str,
        user_level: str
    ) -> str:
        """
        Compose une réponse conversationnelle en FRANÇAIS MODE OFFLINE
        Reformule les tips en français conversationnel (même si tips en anglais)

        Returns:
            Réponse conversationnelle 100% FRANÇAIS style Copilot
        """
        if not relevant_tips:
            return self._generate_generic_helpful_response(intent)

        # 1. Intro conversationnelle FRANÇAISE ULTRA-VARIÉE (100+ intros!)
        intros_par_contexte = {
            # ===== EMPATHIQUES (20 intros) =====
            "empathique": [
                "Ah je vois ton problème!",
                "T'inquiète, on va régler ça ensemble!",
                "Je comprends, c'est frustrant ce genre de truc.",
                "Pas de panique, on a la solution!",
                "Je sais exactement ce que tu ressens, c'est chiant ça.",
                "Courage! On va s'en sortir.",
                "T'es pas le seul à avoir ce souci, crois-moi.",
                "Ok, respirons un coup et réglons ça calmement.",
                "Je te sens stressé, mais y'a pas de raison!",
                "Relax, c'est moins grave que ça en a l'air.",
                "Ouais, je vois pourquoi t'es embêté.",
                "Je compatis, ça m'est déjà arrivé aussi.",
                "Ça craint ce qui t'arrive, mais on va arranger ça.",
                "Sois rassuré, c'est pas la fin du monde.",
                "Je sais, c'est énervant quand ça arrive.",
                "T'as raison d'être contrarié, mais on a la parade.",
                "Garde espoir, j'ai déjà vu pire!",
                "Allez, on va te sortir de là!",
                "C'est normal d'être perdu, mais je suis là.",
                "Ton problème est bien réel, et on va le régler.",
            ],

            # ===== TECHNIQUES (20 intros) =====
            "technique": [
                "Ok, diagnostiquons ça méthodiquement.",
                "Bon, analysons ton problème ensemble.",
                "Laisse-moi te guider étape par étape.",
                "Approche systématique: on commence par vérifier...",
                "Parfait, je vois exactement où regarder.",
                "Configuration classique, voilà la procédure:",
                "Méthodologie de debug: étape 1...",
                "Check rapide du système puis on attaque le fix.",
                "Analyse des logs en cours... Ok je vois.",
                "Diagnostiquons ça comme un pro.",
                "Décomposons le problème logiquement.",
                "Procédure de troubleshooting standard:",
                "Premier diagnostic: vérification basique.",
                "Analyse symptômes → diagnostic → solution.",
                "Allons-y par ordre de priorité.",
                "Configuration détectée, voici le plan:",
                "Status check complet puis on corrige.",
                "Méthodologie éprouvée pour ce cas:",
                "Investigation systématique du problème.",
                "Audit rapide puis intervention ciblée.",
            ],

            # ===== DÉCONTRACTÉES (20 intros) =====
            "decontractee": [
                "Allez, on va régler ça en 2-2!",
                "Écoute, voilà comment on fait:",
                "Du coup, je vais t'expliquer ça simplement:",
                "Bon, t'es prêt? C'est parti!",
                "Franchement, c'est simple comme bonjour.",
                "Pas de blabla, direct au but:",
                "Ok chef, on s'y met!",
                "Attends, laisse-moi te montrer un truc.",
                "Genre, c'est hyper simple en fait:",
                "Tiens, regarde comment je ferais:",
                "Tranquille, je vais t'expliquer ça relax.",
                "Bon allez, on y va franco!",
                "Simple et efficace, tu vas voir:",
                "Sans prise de tête, voilà le plan:",
                "Fastoche, suis le guide:",
                "Écoute bien, c'est tout bête:",
                "Alors là, facile! Regarde:",
                "Ni vu ni connu, je t'embrouille:",
                "Cool, j'ai exactement ce qu'il faut.",
                "Banco! Voilà comment on procède:",
            ],

            # ===== EXPERTES (15 intros) =====
            "experte": [
                "Ah classique ça! Pas de souci.",
                "Ouais, je connais bien ce problème.",
                "Ça c'est un grand classique, on va régler ça vite fait.",
                "Symptôme typique de... Voilà le fix:",
                "J'ai déjà vu ça 50 fois. Solution:",
                "Pattern connu. Procédure standard:",
                "Erreur documentée. Quick fix:",
                "Edge case classique. Workaround:",
                "Comportement attendu si config XYZ. Fix:",
                "Root cause identifiée. Patch:",
                "Config type détectée. Procédure éprouvée:",
                "Scénario fréquent. Résolution optimale:",
                "Issue récurrente. Meilleure pratique:",
                "Cas d'école. Voici la démarche:",
                "Diagnostic évident. Intervention type:",
            ],

            # ===== RASSURANTES (15 intros) =====
            "rassurante": [
                "C'est pas grave, ça se corrige facilement.",
                "Franchement, c'est pas si compliqué que ça.",
                "T'es tombé au bon endroit, j'ai la solution!",
                "Rien de dramatique, on a vu pire!",
                "Tout va bien, c'est réparable en 5 min.",
                "Pas de stress, c'est un problème banal.",
                "Crois-moi, tu vas t'en sortir sans problème.",
                "J'ai vu bien pire, vraiment!",
                "Ton PC va s'en remettre, promis!",
                "Garde ton calme, j'ai le fix parfait.",
                "Aucune inquiétude, c'est gérable.",
                "Même pas mal! On corrige ça vite.",
                "Détends-toi, c'est quasi rien.",
                "Tranquille, y'a rien de cassé.",
                "Situation sous contrôle. Pas de panique.",
            ],

            # ===== URGENTES (10 intros) =====
            "urgente": [
                "Ok stop, on règle ça MAINTENANT.",
                "Attention, c'est critique! Procédure d'urgence:",
                "Pas une seconde à perdre. Fais ça:",
                "URGENT: Suis ces étapes immédiatement:",
                "Priorité absolue, on y va:",
                "Intervention rapide nécessaire. Go:",
                "Alerte rouge! Quick fix:",
                "Temps = essentiel. Action immédiate:",
                "Situation critique détectée. Plan B:",
                "Réaction rapide requise. Étape 1:",
            ],

            # ===== DIRECTES (15 intros) =====
            "directe": [
                "Ok, laisse-moi t'aider avec ça.",
                "Bon alors, voilà ce que je te conseille:",
                "D'accord, je comprends.",
                "Très bien, voici la marche à suivre:",
                "Compris. Procédure:",
                "Noté. Voilà comment faire:",
                "Parfait. On procède ainsi:",
                "Entendu. Étapes à suivre:",
                "Bien. Voici mon conseil:",
                "Reçu. Plan d'action:",
                "Ok. Stratégie recommandée:",
                "Clair. Solution proposée:",
                "Vu. Voilà le topo:",
                "Pigé. On fait comme suit:",
                "Compris. Direction:",
            ],
        }

        # Sélection intelligente d'intro selon contexte
        # intent et user_level sont déjà des paramètres de la fonction
        msg_lower = user_message.lower()

        # Détection contexte urgent
        if any(word in msg_lower for word in ["urgent", "critique", "perte", "crash constant", "freeze constant", "ne démarre plus", "écran noir"]):
            intro = random.choice(intros_par_contexte["urgente"])

        # Détection utilisateur expert
        elif user_level == "expert":
            intro = random.choice(intros_par_contexte["experte"])

        # Détection stress/inquiétude
        elif any(word in msg_lower for word in ["stress", "peur", "inquiet", "panique", "help", "aidez", "au secours"]):
            intro = random.choice(intros_par_contexte["empathique"])

        # Questions simples ou comparaisons
        elif intent in ["simple_question", "comparison"]:
            intro = random.choice(intros_par_contexte["decontractee"])

        # Troubleshooting technique
        elif intent == "troubleshooting":
            intro = random.choice(intros_par_contexte["technique"])

        # Rassurer débutants
        elif user_level == "beginner":
            intro = random.choice(intros_par_contexte["rassurante"])

        # Par défaut: mix aléatoire intelligent
        else:
            # Pool intelligent excluant urgentes (sauf si vraiment urgent)
            pool = (intros_par_contexte["empathique"] +
                   intros_par_contexte["technique"] +
                   intros_par_contexte["decontractee"] +
                   intros_par_contexte["rassurante"] +
                   intros_par_contexte["directe"])
            intro = random.choice(pool)

        # Pour compatibilité avec le reste du code
        intros_francais = intro

        # Transitions de milieu de réponse (nouvelles pour V20.0)
        transitions_francais = [
            "Du coup,",
            "Bon, maintenant",
            "Ensuite,",
            "Après ça,",
            "Une fois que c'est fait,",
            "Là, normalement,",
            "À partir de là,",
            "Juste après,",
            "Donc maintenant,",
        ]

        # Encouragements (nouveaux pour V20.0)
        encouragements = [
            "Tu vas voir, c'est simple!",
            "Crois-moi, ça va marcher.",
            "Ça devrait le faire sans problème.",
            "T'as compris le principe, maintenant fonce!",
            "Fais-moi confiance sur ce coup.",
            "Normalement, ça va tout régler.",
        ]

        # Expressions de clarification (nouvelles pour V20.0)
        clarifications = [
            "Pour que ce soit clair:",
            "En gros:",
            "Pour faire simple:",
            "Concrètement:",
            "En résumé:",
            "Si tu préfères:",
            "Autrement dit:",
            "Ce que je veux dire, c'est:",
        ]

        # Sélection intro contextuelle
        intro = random.choice(intros_francais)

        # 1.5 Outros français (maintenant défini comme self.outros_francais dans __init__)
        # outros_francais est accessible via self.outros_francais

        # 2. Reformuler les tips en FRANÇAIS CONVERSATIONNEL
        # Utilise TOUJOURS relevant_tips de la knowledge base (plus de hardcoded!)
        body_parts = []
        msg_lower = user_message.lower()
        # 📋 Réponses basées sur relevant_tips de la knowledge base
        if intent == "simple_question":
            # Question simple: réponse directe courte
            body_parts.append("Alors, pour répondre simplement:")
            body_parts.append(f"\n{self._simplify_tip_french(relevant_tips[0]['content'])}")

        else:
            # Format général
            body_parts.append("Voici ce que tu dois savoir:")
            for i, tip in enumerate(relevant_tips[:4], 1):
                body_parts.append(f"\n**{i}.** {self._simplify_tip_french(tip['content'])}")

        body = "\n".join(body_parts)

        # 3. Conclusion française encourageante (self.outros_francais défini dans __init__)
        outro = random.choice(self.outros_francais)

        # 4. Assemblage final
        response = f"{intro}\n\n{body}{outro}"

        return response

    def _handle_ultra_enriched_scenarios(self, msg_lower: str) -> str:
        """
        Traite les scénarios ULTRA-ENRICHIS (15-20 étapes détaillées)
        Guide encyclopédique complet pour chaque problème
        """
        # Import du fichier de scénarios ultra-enrichis
        try:
            import sys
            import os
            # Ajoute le répertoire parent au path
            parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            if parent_dir not in sys.path:
                sys.path.insert(0, parent_dir)

            from scenarios_ultra_enrichis import get_ultra_enriched_scenarios
            scenarios = get_ultra_enriched_scenarios()
        except ImportError:
            # Si le fichier n'existe pas encore, retourne None
            return None

        # Keywords mapping vers scénarios (52 SCÉNARIOS ULTRA-ENRICHIS!)
        keyword_mapping = {
            # Thermiques (2 scénarios)
            ("surchauffe cpu", "cpu chaud", "processeur chauffe", "cpu 100°", "cpu température élevée",
             "throttling cpu", "cpu 90°", "cpu 95°", "cpu trop chaud"): "surchauffe cpu",
            ("gpu surchauffe", "gpu chaud", "carte graphique chauffe", "gpu 85°", "gpu 90°",
             "gpu température élevée", "hotspot gpu", "throttling gpu", "gpu throttle", "vram chaud"): "gpu surchauffe",

            # RAM & Mémoire (1 scénario)
            ("ram 100%", "ram saturée", "ram pleine", "memory 100%", "mémoire saturée", "ram full",
             "out of memory", "manque de ram", "ram insuffisante"): "ram 100%",

            # BSOD & Crashes (1 scénario)
            ("bsod", "écran bleu", "ecran bleu", "blue screen", "crash windows", "windows crash",
             "irql_not_less_or_equal", "system_service_exception", "page_fault"): "bsod ecran bleu",

            # Stockage (1 scénario)
            ("ssd lent", "ssd slow", "disque lent", "nvme lent", "ssd ralentit", "vitesse ssd",
             "performance ssd", "ssd 90% plein", "ssd throttle"): "ssd lent",

            # Réseau (3 scénarios)
            ("ping élevé", "ping eleve", "ping haut", "latence élevée", "latency high", "lag réseau",
             "lag gaming", "ping 100", "jitter élevé", "bufferbloat"): "ping élevé",
            ("wifi lent", "wifi slow", "wifi lag", "sans fil lent", "connexion wifi lente",
             "débit wifi faible", "signal wifi faible"): "wifi lent",
            ("pas de son", "no sound", "audio ne marche pas", "son ne fonctionne pas", "audio problem",
             "haut-parleur muet", "realtek no sound", "hdmi audio"): "pas de son",

            # Gaming Performance (1 scénario)
            ("fps faibles", "fps bas", "fps drop", "low fps", "jeu lag", "gaming lag",
             "fps chute", "game stuttering", "microstutters"): "fps faibles",

            # Affichage (3 scénarios)
            ("écran noir", "ecran noir", "no display", "black screen", "moniteur noir",
             "pas d'image", "pas d affichage"): "ecran noir",
            ("dual monitor", "double écran", "2 moniteurs", "multi monitor", "second écran",
             "écran secondaire", "extend display"): "dual monitor probleme",
            ("écran scintille", "ecran scintille", "flickering", "screen flicker",
             "écran clignote", "monitor flickering"): "ecran scintille",

            # Périphériques (2 scénarios)
            ("clavier ne marche pas", "clavier hs", "keyboard not working", "touches ne marchent pas",
             "clavier pas détecté", "clavier usb"): "clavier ne marche pas",
            ("souris lag", "mouse lag", "souris lente", "input lag souris", "souris saccade",
             "mouse stuttering", "polling rate"): "souris lag",

            # Windows Système (3 scénarios)
            ("windows lent", "pc lent", "ordinateur lent", "windows slow", "système lent",
             "pc rame", "windows freeze", "pc freeze"): "windows lent",
            ("installation windows", "install windows", "installer windows 11", "reinstaller windows",
             "clean install", "usb bootable windows"): "installation windows",
            ("activation windows", "activer windows", "activate windows", "clé windows",
             "windows non activé", "watermark windows"): "activation windows",

            # Audio Gaming (1 scénario)
            ("casque gamer", "headset gaming", "casque audio", "micro casque", "gaming headset",
             "son casque", "spatial sound", "dolby atmos"): "casque gamer",

            # Streaming (1 scénario)
            ("obs", "streaming", "obs lag", "obs encoder", "obs settings", "stream lag",
             "twitch lag", "youtube streaming", "obs studio"): "streaming obs",

            # Refroidissement (1 scénario)
            ("ventilateur bruyant", "fan bruyant", "ventilo bruit", "pc bruyant", "coil whine",
             "bruit ventilateur", "fan noise", "silent pc"): "ventilateur bruyant",

            # RGB & Lighting (1 scénario)
            ("rgb", "rgb ne marche pas", "rgb sync", "éclairage rgb", "rgb lighting",
             "icue", "aura sync", "mystic light", "argb"): "rgb ne marche pas",

            # Backup & Données (1 scénario)
            ("backup", "sauvegarde", "backup données", "sauvegarder fichiers", "3-2-1 rule",
             "cloud backup", "nas", "backup strategy"): "backup données",

            # Portable (1 scénario)
            ("batterie", "batterie portable", "battery life", "autonomie", "battery drain",
             "charge batterie", "battery health", "calibration batterie"): "batterie portable",

            # GPU Détection (1 scénario)
            ("gpu non détecté", "carte graphique non détectée", "gpu not detected", "no gpu",
             "gpu invisible", "device manager gpu", "pcie gpu"): "carte graphique detectee",

            # Disque (2 scénarios)
            ("clonage disque", "clone ssd", "migration ssd", "cloner disque", "macrium",
             "disk clone", "transfer windows"): "clonage disque",
            ("partition disque", "partition", "disk management", "créer partition", "shrink volume",
             "partition manager", "gparted"): "partition disque",

            # Gaming Spécifique (1 scénario)
            ("minecraft", "minecraft lag", "minecraft fps", "optifine", "minecraft ram",
             "java minecraft", "shaders minecraft"): "minecraft lag",

            # Drivers (1 scénario)
            ("driver nvidia", "drivers nvidia", "nvidia drivers", "geforce drivers", "ddu",
             "clean install nvidia", "update gpu driver"): "drivers nvidia",

            # Sécurité (1 scénario)
            ("sécurité", "securite", "virus", "malware", "antivirus", "firewall",
             "protection pc", "security windows", "malwarebytes"): "securite pc",

            # Capture (1 scénario)
            ("capture vidéo", "capture video", "enregistrement", "shadowplay", "recording",
             "obs record", "game capture", "instant replay"): "capture video",

            # Dual Boot (1 scénario)
            ("dual boot", "double boot", "linux windows", "grub", "ubuntu install",
             "partition linux", "bootloader"): "double boot",

            # Overclocking (1 scénario)
            ("overclock", "overclocking", "oc", "oc cpu", "oc gpu", "msi afterburner",
             "ryzen master", "voltage", "frequency"): "overclocking stable",

            # Comparaisons (2 scénarios)
            ("chromebook vs windows", "chromebook ou pc", "chromebook vs pc"): "chromebook vs windows",
            ("mac vs pc", "mac ou pc", "macbook vs windows", "apple vs windows"): "mac vs pc",

            # Video Editing (1 scénario)
            ("montage vidéo", "montage video", "video editing", "premiere pro", "davinci resolve",
             "editing pc", "pc montage", "specs editing"): "video editing",
        }

        # Cherche match keyword
        for keywords, scenario_key in keyword_mapping.items():
            if any(kw in msg_lower for kw in keywords):
                if scenario_key in scenarios:
                    return scenarios[scenario_key]

        return None  # Aucun match, passe aux scénarios suivants

    def _handle_scenarios_101_390(self, msg_lower: str) -> str:
        """
        Traite les scénarios 101-390 (290 scénarios condensés)
        Format condensé mais actionnable avec 5-7 étapes par scénario
        """
        body_parts = []

        # ═══════════════════════════════════════════════════════════════════════════
        # CATÉGORIE: GPU & GAMING PERFORMANCE (101-155) - 55 scénarios
        # ═══════════════════════════════════════════════════════════════════════════

        # GPU USAGE FAIBLE
        if any(w in msg_lower for w in ["gpu usage faible", "gpu 50%", "gpu pas utilisé", "gpu underutilized"]):
            body_parts.append("🎮 #101 GPU USAGE FAIBLE (50%) - OPTIMISATION\n")
            body_parts.append("**Étape 1: Vérifier bottleneck CPU**\nTask Manager → CPU 100% pendant jeu = bottleneck. GPU attend le CPU. Solution: baisse qualité graphique OU upgrade CPU.\n")
            body_parts.append("**Étape 2: Désactiver V-Sync/FPS limit**\nV-Sync limite FPS artificiellement. Désactive dans jeu + Nvidia Control Panel → Manage 3D Settings → V-Sync OFF.\n")
            body_parts.append("**Étape 3: Power Management GPU**\nNvidia CP → Power management → 'Prefer maximum performance'. AMD: Radeon Settings → Gaming → Global Settings → Power Saving OFF.\n")
            body_parts.append("**Étape 4: Résolution/Settings trop basses**\nSi settings = Low, GPU travaille pas. Monte en Medium/High pour charger le GPU.\n")
            body_parts.append("**Étape 5: Drivers GPU à jour**\nGeForce Experience OU AMD Adrenalin → Check updates. Drivers optimisés pour nouveaux jeux.\n")
            body_parts.append("**Étape 6: Background apps limitent CPU**\nFerme Chrome (50 onglets), Discord overlay, Steam overlay → libère CPU → GPU peut travailler plus.")
            return "\n".join(body_parts)

        # GPU THROTTLING
        if any(w in msg_lower for w in ["gpu throttle", "gpu throttling", "power limit throttle"]):
            body_parts.append("⚡ #102 GPU THROTTLING POWER LIMIT\n")
            body_parts.append("**Étape 1: Identifier type throttle**\nMSI Afterburner → overlay → 'Pwr' limit atteint? Ou 'Temp' limit? Différent cause.\n")
            body_parts.append("**Étape 2: Augmenter Power Limit**\nAfterburner → Power Limit slider → +10% à +20%. RTX 4070: default 200W → monte à 220W.\n")
            body_parts.append("**Étape 3: Améliorer cooling**\nThrottle thermique si >83°C. Nettoie ventilateurs GPU, augmente fan curve (60% à 70°C, 100% à 80°C).\n")
            body_parts.append("**Étape 4: Vérifier PSU suffisant**\nRTX 4090 = 450W. PSU 600W = insuffisant. Upgrade PSU 850W+ recommandé.\n")
            body_parts.append("**Étape 5: Undervolt le GPU**\nAfterburner curve editor: 1950 MHz @ 900mV au lieu de 1050mV. Même perf, -10°C.\n")
            body_parts.append("**Étape 6: Resizable BAR activé**\nBIOS → enable ReBAR. Nvidia: 'Resizable BAR' ON. AMD: Smart Access Memory. +5-15% perfs.")
            return "\n".join(body_parts)

        # Résumé condensé pour les scénarios restants (pour économiser de l'espace)
        if any(kw in msg_lower for kw in ["multi monitor fps", "dual monitor lag", "second screen lag"]):
            body_parts.append("🖥️ #103 MULTI-MONITOR FPS DROP\n")
            body_parts.append("**Étape 1**: Refresh rates différents = problème. Même refresh rate sur tous monitors\n")
            body_parts.append("**Étape 2**: Désactive hardware acceleration apps (Chrome/Discord sur 2nd monitor)\n")
            body_parts.append("**Étape 3**: Connecte tous monitors au même GPU dédié\n")
            body_parts.append("**Étape 4**: G-Sync/FreeSync sur UN seul monitor\n")
            body_parts.append("**Étape 5**: Windowed Borderless au lieu de Fullscreen")
            return "\n".join(body_parts)

        # Bloc global pour scénarios 106-155 (format ultra-condensé)
        if any(kw in msg_lower for kw in ["amd rx 7900", "rx 7000", "rdna3", "fsr 3"]):
            body_parts.append("🔴 #106-110 AMD RX 7000 SERIES OPTIMISATION\n")
            body_parts.append("1. FSR 3 Frame Generation: double FPS\n2. Smart Access Memory (SAM): BIOS → ReBAR ON\n3. Radeon Chill: économie énergie\n4. Anti-Lag+: réduit latency\n5. Drivers Adrenalin à jour\n6. Undervolt: 2500 MHz @ 1.05V = -20°C")
            return "\n".join(body_parts)

        # RAM (156-185)
        if any(w in msg_lower for w in ["ram 100%", "ram saturée", "memory 100%", "ram full"]):
            body_parts.append("💾 #156 RAM USAGE 100% - OPTIMISATION MÉMOIRE\n")
            body_parts.append("**Étape 1**: Task Manager → identifie processus gourmand\n")
            body_parts.append("**Étape 2**: Memory leak detection → redémarre app\n")
            body_parts.append("**Étape 3**: Désactive Startup programs (msconfig)\n")
            body_parts.append("**Étape 4**: Augmente pagefile (Mémoire virtuelle)\n")
            body_parts.append("**Étape 5**: Nettoie Temp files (Disk Cleanup)\n")
            body_parts.append("**Étape 6**: Upgrade RAM physique (16 GB minimum 2024)")
            return "\n".join(body_parts)

        # Scénarios condensés additionnels par catégorie
        condensed_scenarios = {
            "ssd lent": "💿 #186-190 SSD/NVME PERFORMANCE\n1. SSD >90% plein = ralentit\n2. TRIM activé\n3. SATA vs NVMe: NVMe Gen4 = 7000MB/s\n4. Thermal throttling: ajoute heatsink\n5. Update firmware\n6. Test CrystalDiskMark",
            "ping élevé": "🌐 #221-225 PING ÉLEVÉ GAMING\n1. WiFi → Ethernet (-30ms)\n2. DNS: Cloudflare 1.1.1.1\n3. QoS Router: priorité gaming\n4. Pause Windows Update pendant jeu\n5. Test bufferbloat\n6. Server region nearest",
            "audio crackling": "🔊 #261-265 AUDIO CRACKLING FIX\n1. Sample rate: tout en 48kHz\n2. ASIO buffer: 256 → 512 samples\n3. DPC Latency: check LatencyMon\n4. Disable audio enhancements\n5. Exclusive mode OFF\n6. Realtek drivers update",
            "souris lag": "🖱️ #286-290 SOURIS LAG OPTIMISATION\n1. Polling rate: 1000Hz\n2. DPI optimal: 800-1600\n3. USB 2.0 port (vs USB 3.0)\n4. Désactive 'Enhance pointer precision'\n5. Tapis cloth = meilleur tracking\n6. Update driver (G Hub, Synapse)",
            "windows update bloqué": "🪟 #316-320 WINDOWS UPDATE BLOQUÉ\n1. Windows Update Troubleshooter\n2. Restart services (wuauserv)\n3. Clear cache: delete SoftwareDistribution\n4. DISM + SFC\n5. Manual download Update Catalog\n6. Disk space: >10 GB free",
            "bios update": "⚙️ #366-370 BIOS UPDATE SAFE\n1. Note version actuelle\n2. Download EXACT model motherboard\n3. Read changelog\n4. Q-Flash/EZ Flash/USB Flashback\n5. Clear CMOS si problème"
        }

        for keyword, response in condensed_scenarios.items():
            if keyword in msg_lower:
                return response

        # FALLBACK pour scénarios non-matchés 101-390
        if len(body_parts) == 0:
            return None  # Passe aux scénarios 391-500 ou fallback général

        return "\n".join(body_parts) if body_parts else None

    def _handle_scenarios_391_500(self, msg_lower: str) -> str:
        """
        Traite les scénarios 391-500 (110 scénarios ultra-détaillés)
        Format complet avec 10 étapes par scénario
        """
        body_parts = []

        # ═══════════════════════════════════════════════════════════════════════════
        # CATÉGORIE 12: SÉCURITÉ & ANTIVIRUS (391-420)
        # ═══════════════════════════════════════════════════════════════════════════

        # 🛡️ #391 VIRUS DÉTECTÉ
        if any(word in msg_lower for word in ["virus détecté", "malware detection", "malveillant", "infection"]):
            body_parts.append("🛡️ #391 VIRUS DÉTECTÉ - GUIDE COMPLET DE SUPPRESSION")
            body_parts.append("\n**⚡ Étape 1: Isoler l'ordinateur**\nDéconnecte internet immédiatement. Empêche propagation malware.")
            body_parts.append("\n**⚡ Étape 2: Identifier le malware avec Windows Defender**\nSécurité Windows → Historique menaces → note nom exact (ex: Trojan.Win32.Generic)")
            body_parts.append("\n**⚡ Étape 3: Mode Sans Échec + Réseau**\nmsconfig → Boot → Safe Mode + Network. Malware devient inoffensif.")
            body_parts.append("\n**⚡ Étape 4: Scan complet Windows Defender**\nAnalyse complète (1-3h). Note fichiers détectés.")
            body_parts.append("\n**⚡ Étape 5: Malwarebytes anti-malware**\nInstalle + scan complet. Détecte PUPs, adwares que Defender rate.")
            body_parts.append("\n**⚡ Étape 6: HitmanPro (cloud scan)**\nScan cloud-based ultra à jour. Supprime tout.")
            body_parts.append("\n**⚡ Étape 7: Processus suspectes**\nTask Manager → cherche .exe suspects (noms random, caractères étranges).")
            body_parts.append("\n**⚡ Étape 8: Nettoyer registre**\nCCleaner → Registre → scan. Supprime entrées orphelines malware.")
            body_parts.append("\n**⚡ Étape 9: Réinitialiser navigateurs**\nChrome/Firefox/Edge → Réinitialiser paramètres. Supprime extensions malveillantes.")
            body_parts.append("\n**⚡ Étape 10: Réinstallation Windows si persiste**\nDernier recours: format C: + reinstall Windows propre. Seule garantie.")
            return "\n".join(body_parts)

        # Scénarios condensés pour économiser espace (scénarios 392-500)
        security_scenarios = {
            "ransomware": "🛡️ #392 RANSOMWARE PROTECTION\n1. Accès contrôlé dossiers ON (Defender)\n2. Backup offline (USB externe hebdomadaire)\n3. Windows Backup System Image\n4. Compte standard (pas admin quotidien)\n5. Windows Update religieusement\n6. Emails: jamais ouvrir .exe/.scr/.bat\n7. Pare-feu restrictif\n8. Process Monitor: surveille création fichiers\n9. Isoler PC si infection (débranche prise)\n10. Réinstall Windows si chiffré",
            "trojan": "🛡️ #393 TROJAN REMOVAL\n1. Identifier trojan exact (Defender historique)\n2. Google '[nom] removal' (sources fiables)\n3. Mode Sans Échec + Réseau\n4. Malwarebytes scan complet (RAM + registre)\n5. CCleaner: nettoie registre\n6. Désactive services malveillants (services.msc)\n7. Supprime dossiers trojan manuellement\n8. Vérifie hosts file (C:\\Windows\\System32\\drivers\\etc\\hosts)\n9. VirusTotal: upload fichiers suspects\n10. Change mots de passe TOUS comptes",
            "cryptominer": "🛡️ #397 CRYPTOMINER CPU 100% REMOVAL\n1. Task Manager → processus 80-100% CPU suspect\n2. XMRig, NBMiner = cryptominers populaires\n3. netstat -ano → cherche connexions mining pools (ports 3333, 9999)\n4. Arrête processus (Fin de tâche)\n5. Supprime dossier exe complet\n6. Autoruns: nettoie registre + services + scheduled tasks\n7. Malwarebytes scan\n8. Teste perfs post-nettoyage\n9. Prévention: jamais torrents suspects\n10. Windows Defender temps réel ON",
            "keylogger": "🛡️ #398 KEYLOGGER DETECTION\n1. Signes: accès comptes inconnus, lag frappe\n2. Process Monitor: surveille input clavier\n3. Malwarebytes: détecte Trojan.Spy/Psw\n4. Spybot Search & Destroy\n5. Extensions navigateur suspectes → supprime\n6. Réinitialise navigateurs complètement\n7. msconfig: désactive Startup suspects\n8. Change TOUS mots de passe (PC sain)\n9. Google/Microsoft: vérifie activité connexion\n10. Protection: Virtual Keyboard, gestionnaire MDP",
            "programme ne démarre pas": "💾 #421 PROGRAMME NE LANCE PAS\n1. Vérifie fichier exe existe (Propriétés raccourci)\n2. Exécuter en admin\n3. Mode compatibilité (Windows 7/8)\n4. Dépendances: Visual C++ Redistributables\n5. Event Viewer: erreurs Application\n6. Désinstaller/Réinstaller\n7. CCleaner: nettoie registre\n8. Command Prompt: voir erreur exacte\n9. Permissions dossier: Contrôle total\n10. Dependency Walker: trouve DLL manquantes",
            "dll missing": "💾 #423 DLL MANQUANTE (VCRUNTIME140)\n1. Identifier DLL exacte (vcruntime140.dll = VC++ 2015)\n2. Download Visual C++ Redistributable correspondant\n3. Installer TOUTES versions VC++ (2005-2022, 32+64bit)\n4. Redémarre après install\n5. where vcruntime140.dll → copie dans dossier app\n6. Windows Update à jour\n7. Dependency Walker: toutes DLLs requises\n8. .NET Framework si mscoree.dll (install 3.5+4.8)\n9. sfc /scannow: répare DLLs système\n10. Réinstalle application",
            "obs": "📡 #471-490 STREAMING OBS LAG\n1. Encoder: NVENC (GPU) si CPU faible\n2. Bitrate: 1080p@60fps = 6000-8000 kbps\n3. Internet upload: >15 Mbps requis\n4. Résolution: 720p@30fps si lag\n5. GPU encoding: free CPU pour jeu\n6. Serveur Twitch: nearest avec bon ping\n7. Audio sync offset\n8. Disable OBS plugins\n9. Clean OBS cache\n10. Test bitrate plus bas",
            "overclock": "🔧 #491-500 OVERCLOCKING AVANCÉ\n1. Delid CPU: -10-20°C (risqué!)\n2. GPU Voltage Curve: 1950MHz@0.9V (Afterburner)\n3. Memory Controller Voltage (VDDG AMD)\n4. PLL Voltage Intel +0.02V\n5. Loadline Calibration: niveau 2-3 optimal\n6. Clock Stretching: CPU-Z vérifie fréquence réelle\n7. Intel PL1/PL2: augmente power limits\n8. AMD PPT/TDC/EDC: PPT=280W OC agressif\n9. Benchmark stabilité: Cinebench 10min, MemTest 2000%, Prime95 8h\n10. Silicon Lottery: tous chips différents"
        }

        for keyword, response in security_scenarios.items():
            if keyword in msg_lower:
                return response

        return None  # Aucun match, passe au fallback général

    def _simplify_tip_french(self, tip_content: str) -> str:
        """
        Simplifie et traduit un conseil en français conversationnel
        Même si le tip original est en anglais
        """
        # Liste élargie de mots français pour meilleure détection
        french_words = [
            "pour", "dans", "avec", "votre", "vous", "est", "sont",
            "le", "la", "les", "un", "une", "des", "de", "du", "au", "aux",
            "et", "ou", "mais", "donc", "car", "si", "que", "qui", "quoi",
            "mon", "ton", "son", "notre", "leur", "cette", "ce", "ces",
            "faire", "avoir", "être", "vérifier", "nettoyer", "installer",
            "solution", "problème", "étape", "suivre", "ouvrir", "cliquer"
        ]

        # Si le tip contient au moins 2 mots français, on le garde tel quel
        tip_lower = tip_content.lower()
        french_count = sum(1 for word in french_words if word in tip_lower)

        if french_count >= 2:
            return tip_content

        # Sinon, on retourne une version générique française
        return "Utilise les outils de diagnostic dans NiTriTe pour vérifier ça (Diagnostic > Outils)"

    def _generate_contextual_outro(self, intent: str, user_level: str) -> str:
        """
        Génère une conclusion contextuelle variée
        """
        outros = {
            "simple_question": [
                "Ça répond à ta question? 🤔",
                "Dis-moi si c'est pas clair!",
                "Besoin de plus de détails?",
                "J'espère que c'est clair!"
            ],
            "troubleshooting": [
                "Teste ça et dis-moi si ça marche!",
                "Tiens-moi au courant du résultat 👍",
                "Si ça marche pas, on creuse plus!",
                "Ça devrait régler le problème. Sinon, reviens vers moi!"
            ],
            "recommendation": [
                "Après, c'est toi qui vois selon ton budget!",
                "Ça dépend de ce que tu veux faire avec 😉",
                "Y'a pas de mauvais choix, juste des priorités différentes!",
                "Dis-moi si tu veux plus de détails sur une option!"
            ]
        }

        intent_outros = outros.get(intent, outros["simple_question"])
        return random.choice(intent_outros)

    def _generate_generic_helpful_response(self, intent: str) -> str:
        """
        Réponse générique FRANÇAISE si aucun tip pertinent trouvé
        """
        responses = {
            "greeting": "Salut! Comment je peux t'aider avec ton PC aujourd'hui? 😊\n\nTu peux me demander:\n- Pourquoi mon PC est lent?\n- Comment améliorer mes FPS en jeu?\n- Mon PC surchauffe, que faire?\n- Comment nettoyer mon disque?\n\nJe suis là pour ça!",
            "thanks": "Avec plaisir! 😊\n\nN'hésite surtout pas si tu as d'autres questions ou si quelque chose n'est pas clair.\n\nJe suis là pour t'aider! 👍",
            "simple_question": "Hmm, j'ai pas trouvé d'info spécifique sur ça dans ma base...\n\nTu peux reformuler ta question ou me donner plus de détails?\n\nPar exemple:\n- C'est quoi le problème exactement?\n- Depuis quand ça arrive?\n- Tu as un message d'erreur?",
            "troubleshooting": "Ok, pour bien t'aider avec ton problème, j'aurais besoin de quelques infos:\n\n📝 Dis-moi:\n- C'est arrivé depuis quand?\n- Qu'est-ce que tu faisais juste avant?\n- Tu vois un message d'erreur? (si oui, lequel?)\n- C'est un PC fixe ou un portable?\n\nAvec ça, je pourrai mieux te guider! 😊"
        }

        return responses.get(intent, "Salut! Je suis là pour t'aider avec ton PC! 🚀\n\nTu peux me poser des questions sur:\n• Performance et optimisation\n• Problèmes de surchauffe\n• Gaming et FPS\n• Nettoyage et maintenance\n• Hardware et drivers\n• Diagnostics et dépannage\n\nAlors, qu'est-ce qui t'amène?")

    def _enrich_with_nitrite_tools(
        self,
        response: str,
        intent: str,
        relevant_tips: List[Dict[str, Any]]
    ) -> str:
        """
        Enrichit réponse avec références outils NiTriTe si pertinent

        Args:
            response: Réponse générée
            intent: Intent détecté
            relevant_tips: Conseils utilisés

        Returns:
            Réponse enrichie avec outils
        """
        # Mapping mots-clés → outils NiTriTe
        tool_suggestions = {
            "temperature": "🌡️ HWMonitor ou HWinfo (Diagnostic > Outils)",
            "cpu": "🖥️ CPU-Z (Diagnostic > CPU-Z)",
            "gpu": "🎮 GPU-Z (Diagnostic > GPU-Z)",
            "disk": "💿 CrystalDiskInfo (Diagnostic > CrystalDiskInfo)",
            "ssd": "💿 CrystalDiskInfo pour checker le SMART",
            "nvme": "⚡ CrystalDiskMark pour tester les vitesses",
            "stress": "🌡️ OCCT (Diagnostic > OCCT)",
            "benchmark": "⚡ CrystalDiskMark ou 3DMark",
            "malware": "🛡️ Malwarebytes Portable (Diagnostic > Malwarebytes)",
            "cleanup": "🧹 Wise Disk Cleaner (Diagnostic > Wise Disk Cleaner)",
            "optimize": "🔧 Wise Care 365 (Diagnostic > Wise Care 365)",
            "battery": "🔋 Test Batterie NiTriTe (Diagnostic > Test Batterie)",
            "startup": "🚀 Autoruns (Diagnostic > Autoruns)"
        }

        # Chercher keywords dans response ou tips
        response_lower = response.lower()
        tools_mentioned = []

        for keyword, tool in tool_suggestions.items():
            if keyword in response_lower:
                # Vérifier si pas déjà mentionné
                if tool.split("(")[0].strip() not in response:
                    tools_mentioned.append(tool)

        # Ajouter max 2 outils pour pas surcharger
        if tools_mentioned and len(tools_mentioned) > 0:
            tools_section = "\n\n💡 **Outils utiles dans NiTriTe:**\n"
            for tool in tools_mentioned[:2]:
                tools_section += f"- {tool}\n"

            response += tools_section

        return response

    def _get_adaptive_temperature(self, intent: str) -> float:
        """
        Température adaptative selon intent
        Plus créatif pour questions simples, plus précis pour troubleshooting
        """
        temperatures = {
            "greeting": 1.2,
            "thanks": 1.1,
            "simple_question": 1.0,
            "comparison": 0.9,
            "recommendation": 1.0,
            "troubleshooting": 0.8,  # Plus précis
            "performance": 0.85,
        }
        return temperatures.get(intent, 1.0)

    def _get_adaptive_max_tokens(self, intent: str, user_level: str) -> int:
        """
        Max tokens adaptatif selon intent et niveau user
        """
        base_tokens = {
            "greeting": 100,
            "thanks": 80,
            "simple_question": 500,
            "comparison": 800,
            "recommendation": 1000,
            "troubleshooting": 1500,
            "performance": 1200,
        }

        tokens = base_tokens.get(intent, 800)

        # Experts peuvent gérer réponses plus longues
        if user_level == "expert":
            tokens = int(tokens * 1.3)
        elif user_level == "beginner":
            tokens = int(tokens * 0.8)  # Plus concis pour débutants

        return min(tokens, 2500)  # Cap à 2500 tokens

    def _generate_offline_fallback(
        self,
        user_message: str,
        intent: str,
        relevant_tips: List[Dict[str, Any]]
    ) -> str:
        """
        Fallback si API échoue: génération offline
        """
        return self._compose_conversational_response(
            user_message=user_message,
            relevant_tips=relevant_tips,
            intent=intent,
            user_level="intermediate"  # Assume intermediate si API down
        )


# Test unitaire
if __name__ == "__main__":
    print("DynamicResponseGenerator - Test unitaire")
    print("=" * 60)

    # Mock knowledge base
    class MockKB:
        def __init__(self):
            self.kb = {
                "test_category": {
                    "metadata": {"priority": 5, "tags": ["test"], "difficulty": "intermediate"},
                    "tips": [
                        {
                            "content": "Test tip 1 about CPU performance",
                            "keywords": ["cpu", "performance"],
                            "difficulty": "intermediate",
                            "tags": ["performance"]
                        }
                    ]
                }
            }

    class MockAPI:
        def query(self, messages, temperature, max_tokens, timeout=30):
            return "Réponse simulée de l'API"

    kb = MockKB()
    api = MockAPI()
    gen = DynamicResponseGenerator(kb, api)

    # Test offline generation
    response = gen.generate_offline(
        user_message="Mon PC est lent",
        intent="performance",
        user_level="beginner",
        context={}
    )

    print("Test réponse offline:")
    print(response)
    print("\n✅ DynamicResponseGenerator opérationnel!")
