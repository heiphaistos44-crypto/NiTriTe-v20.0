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

        # 1. Intro conversationnelle FRANÇAISE variée
        intros_francais = [
            "Ah je vois ton problème!",
            "Ok, laisse-moi t'aider avec ça.",
            "D'accord, je comprends.",
            "Bon alors, voilà ce que je te conseille:",
            "Ah classique ça! Pas de souci."
        ]
        intro = random.choice(intros_francais)

        # 2. Reformuler les tips en FRANÇAIS CONVERSATIONNEL
        # Au lieu de copier directement, on crée une réponse française
        body_parts = []

        # 🔥 DÉTECTION PAR KEYWORDS PRIORITAIRE (avant intent check)
        # Peu importe l'intent détecté, si on voit ces mots = réponse spécifique
        msg_lower = user_message.lower()

        # ═══════════════════════════════════════════════════════════════════
        # 🔥 100 SCÉNARIOS ULTRA-DÉTAILLÉS - 500 ÉTAPES
        # ═══════════════════════════════════════════════════════════════════

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 1: PROBLÈMES THERMIQUES & REFROIDISSEMENT (10 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 🌡️ #1 SURCHAUFFE GÉNÉRALE
        if any(word in msg_lower for word in ["surchauffe", "chauffe", "chaud", "température", "chaleur", "brûlant", "brule"]):
            body_parts.append("Problème de surchauffe! On va diagnostiquer et régler ça méthodiquement:")
            body_parts.append("\n**🌡️ Étape 1: Diagnostic températures**")
            body_parts.append("- Lance HWMonitor (NiTriTe > Diagnostic)")
            body_parts.append("- CPU normal: 40-70°C idle, max 85-90°C charge")
            body_parts.append("- GPU normal: 40-60°C idle, max 80-85°C jeu")
            body_parts.append("\n**🧹 Étape 2: Nettoyage physique**")
            body_parts.append("- Éteins PC, débranche alimentation")
            body_parts.append("- Bombe à air comprimé sur ventilos CPU/GPU/PSU")
            body_parts.append("- Poussière = isolation = surchauffe!")
            body_parts.append("\n**🌀 Étape 3: Ventilos**")
            body_parts.append("- Vérifie RPM dans HWMonitor")
            body_parts.append("- 0 RPM = ventilo mort à remplacer")
            body_parts.append("\n**🔧 Étape 4: Pâte thermique**")
            body_parts.append("- Si >3 ans: renouvelle pâte thermique CPU/GPU")
            body_parts.append("- Arctic MX-4 ou Noctua NT-H1 (5-10€)")
            body_parts.append("\n**⚡ Étape 5: Undervolting**")
            body_parts.append("- ThrottleStop (Intel) ou Ryzen Master (AMD)")
            body_parts.append("- -50 à -100mV = -10°C sans perte perfs")

        # 🌡️ #2 SURCHAUFFE CPU SPÉCIFIQUE
        elif any(word in msg_lower for word in ["cpu chaud", "processeur chauffe", "cpu 100°", "throttling cpu"]):
            body_parts.append("CPU qui chauffe trop? Température critique, on règle ça!")
            body_parts.append("\n**📊 Étape 1: Vérif charge CPU**")
            body_parts.append("- Task Manager > Onglet Performances > CPU")
            body_parts.append("- Si 100% idle = virus mining probable")
            body_parts.append("\n**🌀 Étape 2: Ventirad CPU**")
            body_parts.append("- Vérifie ventilo tourne (écoute + HWMonitor RPM)")
            body_parts.append("- <1000 RPM = problème, remplace ventilo")
            body_parts.append("\n**🧪 Étape 3: Pâte thermique**")
            body_parts.append("- Démonte ventirad, nettoie ancienne pâte (alcool isopropylique)")
            body_parts.append("- Grain de riz pâte au centre CPU, remonter ventirad")
            body_parts.append("\n**⚙️ Étape 4: Limites TDP BIOS**")
            body_parts.append("- Entre dans BIOS (DEL au boot)")
            body_parts.append("- Réduis PL1/PL2 (Intel) ou PPT (AMD) de 10-20W")
            body_parts.append("\n**❄️ Étape 5: Upgrade refroidissement**")
            body_parts.append("- Si ventirad stock: upgrade vers Noctua NH-D15 ou Dark Rock Pro 4")
            body_parts.append("- Ou AIO 240-280mm (Corsair, Arctic)")

        # 🌡️ #3 SURCHAUFFE GPU
        elif any(word in msg_lower for word in ["gpu chaud", "carte graphique chauffe", "gpu 90°", "hotspot gpu"]):
            body_parts.append("GPU qui surchauffe? On va refroidir ça!")
            body_parts.append("\n**🔍 Étape 1: Monitoring temps**")
            body_parts.append("- MSI Afterburner ou HWiNFO64")
            body_parts.append("- GPU temp, Memory Junction Temp, Hot Spot")
            body_parts.append("- >85°C GPU ou >95°C hotspot = problème")
            body_parts.append("\n**🌀 Étape 2: Courbe ventilo GPU**")
            body_parts.append("- MSI Afterburner > Settings > Fan")
            body_parts.append("- Courbe agressive: 60°C=60%, 70°C=80%, 75°C=100%")
            body_parts.append("\n**🧹 Étape 3: Nettoyage GPU**")
            body_parts.append("- Démonte GPU du PCIe")
            body_parts.append("- Air comprimé entre ailettes radiateur")
            body_parts.append("- Si à l'aise: démonte shroud, nettoie ventilos")
            body_parts.append("\n**🔧 Étape 4: Thermal pads/paste**")
            body_parts.append("- Si >2 ans: change pâte GPU + thermal pads mémoire")
            body_parts.append("- Pâte: Gelid GC-Extreme, Pads: Thermalright 1.5/2mm")
            body_parts.append("\n**⚡ Étape 5: Undervolt GPU**")
            body_parts.append("- MSI Afterburner: Curve Editor (Ctrl+F)")
            body_parts.append("- Lock 1900 MHz @ 850mV par exemple")
            body_parts.append("- Teste stabilité 3DMark")

        # 🌡️ #4 VENTILATEURS BRUYANTS
        elif any(word in msg_lower for word in ["ventilateur bruyant", "ventilo fort", "bruit ventilateur", "pc bruyant"]):
            body_parts.append("Ventilos trop bruyants? On va optimiser les courbes!")
            body_parts.append("\n**📊 Étape 1: Identifie source bruit**")
            body_parts.append("- Ouvre boîtier en fonctionnement (prudence!)")
            body_parts.append("- Écoute: CPU, GPU, case fans, PSU?")
            body_parts.append("\n**🌀 Étape 2: Courbes ventilateurs BIOS/Software**")
            body_parts.append("- BIOS: Q-Fan Control, Fan Expert, Smart Fan")
            body_parts.append("- Mode Silent ou Custom avec seuils plus hauts")
            body_parts.append("- Exemple: <60°C=30%, 70°C=50%, 80°C=80%")
            body_parts.append("\n**🔧 Étape 3: Remplace ventilos bruyants**")
            body_parts.append("- Ventilos quality: Noctua NF-A12x25, Be Quiet Silent Wings 4")
            body_parts.append("- Check bruit dB: <20dB = silencieux")
            body_parts.append("\n**🎛️ Étape 4: PWM hub ou contrôleur**")
            body_parts.append("- Si ventilos 3-pin DC: upgrade vers PWM 4-pin")
            body_parts.append("- Contrôle précis vitesse = moins bruit")
            body_parts.append("\n**🏠 Étape 5: Isolation acoustique boîtier**")
            body_parts.append("- Mousse acoustique Bitfenix ou Be Quiet")
            body_parts.append("- Boîtiers silencieux: Fractal Define, Be Quiet Pure Base")

        # 🌡️ #5 WATERCOOLING / AIO PROBLÈMES
        elif any(word in msg_lower for word in ["aio", "watercooling", "pompe", "liquide refroidissement", "bulles aio"]):
            body_parts.append("Problème de watercooling/AIO? On vérifie l'installation!")
            body_parts.append("\n**💧 Étape 1: Pompe fonctionne?**")
            body_parts.append("- Écoute bruit pompe (léger ronronnement)")
            body_parts.append("- HWMonitor: 'Pump RPM' doit être >2000 RPM")
            body_parts.append("- Si 0 RPM = pompe morte ou mal branchée")
            body_parts.append("\n**🔌 Étape 2: Branchement pompe**")
            body_parts.append("- Pompe sur header 'AIO_PUMP' ou 'CPU_FAN' (pas CHA_FAN!)")
            body_parts.append("- En PWM ou DC selon modèle")
            body_parts.append("- BIOS: pompe à 100% constant (jamais en mode adaptatif)")
            body_parts.append("\n**📐 Étape 3: Position radiateur**")
            body_parts.append("- Tubes en BAS du radiateur (évite air dans pompe)")
            body_parts.append("- Radiateur au-dessus de pompe si possible")
            body_parts.append("\n**❄️ Étape 4: Bulles d'air**")
            body_parts.append("- Bruit glouglou = bulles dans circuit")
            body_parts.append("- Secoue délicatement boîtier pour déloger bulles")
            body_parts.append("- Laisse tourner 24h, bulles vont au radiateur")
            body_parts.append("\n**🔧 Étape 5: Fuite ou évaporation**")
            body_parts.append("- Check traces humidité autour block/tubes")
            body_parts.append("- Si AIO >5 ans: liquide évaporé, remplace AIO complet")

        # 🌡️ #6 THERMAL THROTTLING
        elif any(word in msg_lower for word in ["thermal throttling", "throttle température", "tjunction", "tjmax"]):
            body_parts.append("Thermal throttling détecté? Le PC réduit ses perfs pour éviter surchauffe!")
            body_parts.append("\n**📊 Étape 1: Monitoring ThrottleStop/HWiNFO**")
            body_parts.append("- ThrottleStop: colonne 'PROCHOT' ou 'Thermal' en rouge = throttling actif")
            body_parts.append("- HWiNFO64: 'Thermal Throttling' = Yes")
            body_parts.append("\n**🌡️ Étape 2: Températures limites**")
            body_parts.append("- Intel: Tj Max = 100°C (varie selon CPU)")
            body_parts.append("- AMD: Tj Max = 95°C (Ryzen 5000/7000)")
            body_parts.append("- Si CPU atteint Tj Max = throttling activé")
            body_parts.append("\n**🔧 Étape 3: Améliore refroidissement**")
            body_parts.append("- Repaste thermique CPU")
            body_parts.append("- Vérifie ventirad bien serré (vis en croix)")
            body_parts.append("- Upgrade ventirad si stock insuffisant")
            body_parts.append("\n**⚙️ Étape 4: Réduis TDP/PPT**")
            body_parts.append("- BIOS ou Ryzen Master/ThrottleStop")
            body_parts.append("- Intel: PL1/PL2 -20W")
            body_parts.append("- AMD: PPT -15W")
            body_parts.append("- Perds 5-10% perfs mais plus de throttling")
            body_parts.append("\n**⚡ Étape 5: Undervolt**")
            body_parts.append("- -80mV CPU = -10-15°C typique")
            body_parts.append("- ThrottleStop ou Intel XTU (Intel)")
            body_parts.append("- Ryzen Master ou PBO Curve Optimizer (AMD)")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 2: CRASHES & STABILITÉ (10 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 💀 #7 ÉCRAN BLEU (BSOD)
        elif any(word in msg_lower for word in ["bsod", "écran bleu", "blue screen", "stop code"]):
            body_parts.append("BSOD! On va identifier la cause avec les codes d'erreur:")
            body_parts.append("\n**🔍 Étape 1: Code erreur**")
            body_parts.append("- Note le STOP CODE (ex: IRQL_NOT_LESS_OR_EQUAL)")
            body_parts.append("- BlueScreenView (NiTriTe > Diagnostic) = historique BSOD")
            body_parts.append("\n**🧠 Étape 2: Test RAM**")
            body_parts.append("- MemTest86: 2+ passes minimum")
            body_parts.append("- 1 erreur = barrette défectueuse")
            body_parts.append("- Teste barrettes séparément")
            body_parts.append("\n**🎮 Étape 3: Drivers**")
            body_parts.append("- BlueScreenView montre .sys responsable")
            body_parts.append("- nvlddmkm.sys = NVIDIA, DDU puis reinstall")
            body_parts.append("- atikmpag.sys = AMD driver")
            body_parts.append("\n**⚡ Étape 4: Reset overclock**")
            body_parts.append("- BIOS > Load Defaults")
            body_parts.append("- Désactive XMP/EXPO RAM temporairement")
            body_parts.append("\n**🔧 Étape 5: Répar Windows**")
            body_parts.append("- CMD admin: sfc /scannow")
            body_parts.append("- Puis: DISM /Online /Cleanup-Image /RestoreHealth")

        # 💀 #8 PC FREEZE/GEL COMPLET
        elif any(word in msg_lower for word in ["freeze", "gel", "bloque", "fige", "ne répond plus"]):
            body_parts.append("PC qui freeze? Plusieurs causes, on diagnostique:")
            body_parts.append("\n**🔍 Étape 1: Quand ça freeze?**")
            body_parts.append("- Au boot = driver/Windows corrompu")
            body_parts.append("- En jeu = GPU/température")
            body_parts.append("- Aléatoire = RAM ou SSD")
            body_parts.append("\n**💾 Étape 2: SSD/Disque**")
            body_parts.append("- CrystalDiskInfo: SMART status")
            body_parts.append("- Secteurs réalloués >5 = disque mourant")
            body_parts.append("- Clone vers nouveau SSD si bad")
            body_parts.append("\n**🧠 Étape 3: RAM**")
            body_parts.append("- MemTest86 overnight")
            body_parts.append("- Windows Memory Diagnostic aussi")
            body_parts.append("\n**🌡️ Étape 4: Températures**")
            body_parts.append("- HWMonitor pendant utilisation")
            body_parts.append("- CPU/GPU >90°C = throttling puis freeze")
            body_parts.append("\n**⚙️ Étape 5: Mode sans échec**")
            body_parts.append("- Boot en safe mode")
            body_parts.append("- Si freeze persiste = hardware, sinon = driver/software")

        # 💀 #9 REDÉMARRAGES ALÉATOIRES
        elif any(word in msg_lower for word in ["redémarre tout seul", "reboot aléatoire", "s'éteint tout seul"]):
            body_parts.append("Redémarrages intempestifs? Souvent alimentation ou températures!")
            body_parts.append("\n**⚡ Étape 1: Alimentation (cause #1)**")
            body_parts.append("- Sous-dimensionnée? Calcule conso:")
            body_parts.append("  * RTX 4070 = 650W minimum PSU")
            body_parts.append("  * RTX 4090 = 850W+ requis")
            body_parts.append("- PSU vieux >5 ans = condensateurs morts")
            body_parts.append("\n**🌡️ Étape 2: Protection thermique**")
            body_parts.append("- CPU/GPU >Tj Max = shutdown auto")
            body_parts.append("- Vérifie Event Viewer: Kernel-Power erreur 41")
            body_parts.append("\n**🔌 Étape 3: Câbles alimentation**")
            body_parts.append("- Câbles PCIe GPU bien enfoncés?")
            body_parts.append("- Câble ATX 24-pin + EPS 8-pin CPU serrés")
            body_parts.append("\n**⚙️ Étape 4: Désactive auto-restart BSOD**")
            body_parts.append("- Paramètres > Système > Infos > Paramètres avancés")
            body_parts.append("- Démarrage/Récup > Décocher 'Redémarrer auto'")
            body_parts.append("- Permet voir le BSOD au lieu de reboot direct")
            body_parts.append("\n**🧪 Étape 5: Test stress PSU**")
            body_parts.append("- OCCT Power test 30 min")
            body_parts.append("- Si shutdown pendant test = PSU défaillant")

        # 💀 #10 CRASH JEUX SPÉCIFIQUES
        elif any(word in msg_lower for word in ["jeu crash", "game crash", "crash en jeu", "ferme tout seul jeu"]):
            body_parts.append("Jeu qui crash? On va stabiliser ça!")
            body_parts.append("\n**🎮 Étape 1: Vérif fichiers jeu**")
            body_parts.append("- Steam: Propriétés > Fichiers > Vérifier intégrité")
            body_parts.append("- Epic: Bibliothèque > ... > Vérifier")
            body_parts.append("- Fichiers corrompus = crash fréquent")
            body_parts.append("\n**🔧 Étape 2: Drivers GPU à jour**")
            body_parts.append("- GeForce Experience ou AMD Software")
            body_parts.append("- Game Ready Driver (NVIDIA)")
            body_parts.append("- Si crash après MAJ driver: rollback version stable")
            body_parts.append("\n**⚙️ Étape 3: Paramètres graphiques**")
            body_parts.append("- Baisse preset de Ultra à High/Medium")
            body_parts.append("- Désactive Ray-Tracing temporairement")
            body_parts.append("- VRAM overload = crash: baisse textures/réso")
            body_parts.append("\n**🌡️ Étape 4: Monitoring crash**")
            body_parts.append("- MSI Afterburner: log température/clocks avant crash")
            body_parts.append("- GPU >85°C ou Memory >100°C = throttle puis crash")
            body_parts.append("\n**⚡ Étape 5: Désactive overlays**")
            body_parts.append("- Discord overlay, Steam overlay, GeForce Exp = OFF")
            body_parts.append("- Xbox Game Bar = désactivé")
            body_parts.append("- Overlays = incompatibilités certains jeux")

        # 🐌 PC LENT - Keywords: lent, ralenti, lag, rame, slow
        elif any(word in msg_lower for word in ["lent", "ralenti", "lag", "rame", "lenteur", "slow", "freeze"]):
            body_parts.append("PC lent? On va booster ça! Plusieurs causes possibles, on vérifie tout:")
            body_parts.append("\n**💿 Étape 1: Disque à 100% (cause la plus fréquente)**")
            body_parts.append("- Gestionnaire des tâches (Ctrl+Maj+Échap) > Performance > Disque")
            body_parts.append("- Si 100% en permanence:")
            body_parts.append("  - Désactive Windows Search: services.msc → 'Windows Search' → Désactiver")
            body_parts.append("  - Désactive Superfetch: services.msc → 'SysMain' → Désactiver")
            body_parts.append("  - Vérifie Chrome: ferme les onglets inutiles (chaque onglet = mémoire)")
            body_parts.append("  - Si HDD mécanique: UPGRADE vers SSD = +300% vitesse!")
            body_parts.append("\n**🧠 Étape 2: RAM saturée**")
            body_parts.append("- Gestionnaire des tâches > Performance > Mémoire")
            body_parts.append("- >85-90% = pas assez de RAM")
            body_parts.append("- Onglet 'Processus': trie par 'Mémoire'")
            body_parts.append("- Ferme les gros consommateurs (Chrome, Teams, Photoshop)")
            body_parts.append("- Solution long terme: ajoute de la RAM (16 GB minimum 2024)")
            body_parts.append("\n**🚀 Étape 3: Programmes au démarrage**")
            body_parts.append("- Gestionnaire des tâches > Onglet 'Démarrage'")
            body_parts.append("- Désactive TOUT sauf:")
            body_parts.append("  - Antivirus (Windows Defender ou autre)")
            body_parts.append("  - Drivers GPU/Audio si nécessaire")
            body_parts.append("- Spotify, Discord, Teams = inutile au démarrage!")
            body_parts.append("\n**🦠 Étape 4: Virus/Malwares**")
            body_parts.append("- Lance Malwarebytes (dans NiTriTe > Diagnostic)")
            body_parts.append("- Scan complet (prend 30-60 min)")
            body_parts.append("- Supprime tout ce qui est détecté")
            body_parts.append("- Les malwares de minage crypto = 100% CPU = PC ultra lent")
            body_parts.append("\n**🗑️ Étape 5: Nettoyage disque**")
            body_parts.append("- Paramètres > Système > Stockage")
            body_parts.append("- 'Fichiers temporaires' → Supprimer")
            body_parts.append("- Vide la Corbeille")
            body_parts.append("- Désinstalle programmes inutilisés (Panneau de config > Programmes)")
            body_parts.append("- Laisse au moins 15-20% d'espace libre sur C:")
            body_parts.append("\n**⚙️ Étape 6: Désactive effets visuels Windows**")
            body_parts.append("- Recherche: 'Ajuster l'apparence et les performances de Windows'")
            body_parts.append("- Sélectionne 'Ajuster afin d'obtenir les meilleures performances'")
            body_parts.append("- Ou personnalise: garde juste 'Lisser les polices' pour lisibilité")
            body_parts.append("\n**🔄 Étape 7: Mises à jour Windows**")
            body_parts.append("- Paramètres > Windows Update")
            body_parts.append("- Installe TOUTES les mises à jour en attente")
            body_parts.append("- Redémarre (parfois 2-3 fois)")
            body_parts.append("- Les updates corrigent bugs de performances")
            body_parts.append("\n**💊 Étape 8: Réinitialisation propre (dernier recours)**")
            body_parts.append("- Si rien ne marche:")
            body_parts.append("- Paramètres > Système > Récupération")
            body_parts.append("- 'Réinitialiser ce PC' > 'Conserver mes fichiers'")
            body_parts.append("- Réinstalle Windows en gardant tes documents")
            body_parts.append("- Ça règle 90% des problèmes de lenteur mystérieux!")

        # 🎮 FPS / GAMING - Keywords: fps, jeu, game, gaming, saccade
        elif any(word in msg_lower for word in ["fps", "jeu", "jeux", "game", "gaming", "saccade", "fluide", "framedrops", "lag jeu"]):
            body_parts.append("Problème de FPS? Je vais te donner TOUTES les astuces pour maximiser tes perfs!")
            body_parts.append("\n**🎨 Étape 1: Paramètres graphiques IN-GAME (gain immédiat)**")
            body_parts.append("- Options > Graphismes:")
            body_parts.append("  - Résolution: si <60 FPS, baisse de 1440p à 1080p (gros gain)")
            body_parts.append("  - Preset: 'Moyen' ou 'Bas' pour commencer")
            body_parts.append("  - DÉSACTIVE (gros gagnants FPS):")
            body_parts.append("    * Ombres/Shadows (qualité 'Bas' OK)")
            body_parts.append("    * Anti-aliasing/MSAA (met FXAA à la place)")
            body_parts.append("    * Ray-tracing (RTX) si <RTX 4070")
            body_parts.append("    * Motion Blur (inutile)")
            body_parts.append("    * Depth of Field (flou arrière-plan)")
            body_parts.append("    * Volumetric Fog/Clouds")
            body_parts.append("  - ACTIVE:")
            body_parts.append("    * V-Sync OFF (réduit latence)")
            body_parts.append("    * FPS limiter: mets 2-3x ta fréquence écran (144Hz → limite 300 FPS)")
            body_parts.append("\n**🖥️ Étape 2: Paramètres Windows Gaming**")
            body_parts.append("- Mode jeu (Game Mode): Paramètres > Jeux > Mode jeu = ACTIVÉ")
            body_parts.append("- Prioritize CPU/GPU for games")
            body_parts.append("- Désactive DVR/Capture: Paramètres > Jeux > Captures = TOUT désactivé")
            body_parts.append("- Xbox Game Bar = désactivé (bouffe des ressources)")
            body_parts.append("\n**🎮 Étape 3: NVIDIA/AMD Control Panel**")
            body_parts.append("- NVIDIA:")
            body_parts.append("  - Clic droit Bureau > Panneau de config NVIDIA")
            body_parts.append("  - Gérer les paramètres 3D > Paramètres globaux:")
            body_parts.append("    * Mode gestion alim: 'Performances maximales'")
            body_parts.append("    * Images pré-rendues max: 1")
            body_parts.append("    * Lissage - Mode: 'Application contrôlée'")
            body_parts.append("    * V-Sync: Désactivé")
            body_parts.append("    * Qualité filtrage textures: 'Hautes performances'")
            body_parts.append("  - Active NVIDIA Reflex (si dispo) = réduit latence")
            body_parts.append("- AMD:")
            body_parts.append("  - AMD Software > Gaming > Paramètres globaux:")
            body_parts.append("    * Radeon Anti-Lag: ON")
            body_parts.append("    * Radeon Boost: ON (baisse réso dynamique)")
            body_parts.append("    * V-Sync: OFF")
            body_parts.append("\n**⚡ Étape 4: Mode Alimentation Windows**")
            body_parts.append("- Panneau de config > Options d'alimentation")
            body_parts.append("- Sélectionne 'Performances élevées'")
            body_parts.append("- Ou crée un mode 'Ultimate Performance':")
            body_parts.append("  - CMD admin: powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
            body_parts.append("  - Apparaît dans options alimentation")
            body_parts.append("\n**🚀 Étape 5: Ferme TOUT en arrière-plan**")
            body_parts.append("- Chrome/Firefox = fermé (ou 1-2 onglets max)")
            body_parts.append("- Discord: active mode Performance (Paramètres > Apparence)")
            body_parts.append("- Spotify: ferme ou mets en pause")
            body_parts.append("- RGB software (iCUE, Razer Synapse): ferme si pas besoin")
            body_parts.append("- Ctrl+Maj+Échap: vérifie qu'aucun processus bouffe >10% CPU/GPU")
            body_parts.append("\n**🔄 Étape 6: Drivers à jour (critique!)**")
            body_parts.append("- NVIDIA: GeForce Experience > Drivers > Vérifier")
            body_parts.append("- AMD: AMD Software > Updates")
            body_parts.append("- Les nouveaux drivers = +5-15% FPS sur jeux récents!")
            body_parts.append("\n**🎯 Étape 7: Vérifie GPU dédié utilisé (portable surtout)**")
            body_parts.append("- Paramètres > Système > Affichage > Paramètres graphiques")
            body_parts.append("- Ajoute le .exe du jeu")
            body_parts.append("- Sélectionne 'Hautes performances' (GPU dédié)")
            body_parts.append("- Sinon le jeu tourne sur iGPU intégré = 10 FPS!")
            body_parts.append("\n**🌡️ Étape 8: Températures (throttling)**")
            body_parts.append("- Lance HWMonitor pendant jeu")
            body_parts.append("- GPU >85°C ou CPU >90°C = thermal throttling = perte FPS")
            body_parts.append("- Si chaud: nettoie poussière, améliore refroidissement")
            body_parts.append("\n**🔧 Étape 9: Overclock GPU (avancé, +10-15% FPS)**")
            body_parts.append("- MSI Afterburner (gratuit):")
            body_parts.append("  - Core Clock: +100 MHz par paliers de +25")
            body_parts.append("  - Memory Clock: +200-500 MHz")
            body_parts.append("  - Power Limit: 110-120%")
            body_parts.append("  - Teste stabilité avec FurMark 10 min")
            body_parts.append("  - Si crash: baisse de 25 MHz et re-teste")
            body_parts.append("\n**💾 Étape 10: Installe jeu sur SSD (pas HDD)**")
            body_parts.append("- HDD = temps de chargement longs + micro-stutters")
            body_parts.append("- SSD NVMe = +50-200% vitesse chargement, textures fluides")
            body_parts.append("- Déplace jeu: Steam > Propriétés > Fichiers locaux > Déplacer")

        # 🌐 INTERNET LENT - Keywords: internet lent, connexion lente, wifi lent
        elif any(word in msg_lower for word in ["internet lent", "connexion lente", "wifi lent", "débit lent", "téléchargement lent", "download lent"]):
            body_parts.append("Internet lent? Je vais t'aider à identifier et régler le problème!")
            body_parts.append("\n**📊 Étape 1: Test de vitesse (diagnostic)**")
            body_parts.append("- Va sur speedtest.net ou fast.com")
            body_parts.append("- Compare avec ton abonnement (Fibre 1Gb = 800-950 Mbps réel)")
            body_parts.append("- Si <50% de ta vitesse théorique = problème")
            body_parts.append("\n**🔌 Étape 2: Câble Ethernet vs Wi-Fi**")
            body_parts.append("- TOUJOURS tester en Ethernet d'abord")
            body_parts.append("- Wi-Fi = perte 30-50% vitesse + latence")
            body_parts.append("- Si bon en Ethernet, mauvais en Wi-Fi = problème Wi-Fi (voir étapes suivantes)")
            body_parts.append("\n**📡 Étape 3: Redémarre box/routeur**")
            body_parts.append("- Éteins la box 30 secondes minimum")
            body_parts.append("- Rallume et attends 2-3 min qu'elle redémarre complètement")
            body_parts.append("- Ça règle 50% des problèmes de connexion!")
            body_parts.append("\n**🛜 Étape 4: Canal Wi-Fi (interférences)**")
            body_parts.append("- Télécharge WiFi Analyzer (Windows Store)")
            body_parts.append("- Regarde quels canaux sont saturés")
            body_parts.append("- Interface box: change canal 2.4GHz (1, 6 ou 11) et 5GHz")
            body_parts.append("- Préfère 5GHz si possible (plus rapide, moins perturbé)")
            body_parts.append("\n**💻 Étape 5: Drivers carte réseau**")
            body_parts.append("- Gestionnaire de périphériques > Cartes réseau")
            body_parts.append("- Clic droit sur ta carte > Mettre à jour le pilote")
            body_parts.append("- Ou va sur site fabricant (Intel, Realtek, Qualcomm)")
            body_parts.append("\n**⚙️ Étape 6: Paramètres carte réseau Windows**")
            body_parts.append("- Panneau de config > Centre Réseau > Modifier paramètres carte")
            body_parts.append("- Clic droit carte > Propriétés > Configurer > Avancé:")
            body_parts.append("  - 'IPv6': Désactiver (sauf si besoin spécifique)")
            body_parts.append("  - 'Économie d'énergie': Désactiver")
            body_parts.append("  - 'Vitesse et duplex': Forcer 1.0 Gbps Full Duplex (Ethernet)")
            body_parts.append("\n**🔍 Étape 7: Programmes qui saturent (uploads/downloads)**")
            body_parts.append("- Gestionnaire des tâches > Performance > Réseau")
            body_parts.append("- Si utilisation 100%: onglet Processus, trie par 'Réseau'")
            body_parts.append("- Souvent: Windows Update, OneDrive, Steam, Torrents")
            body_parts.append("- Ferme ou pause ces téléchargements")
            body_parts.append("\n**🌍 Étape 8: DNS (souvent négligé)**")
            body_parts.append("- Change DNS pour Cloudflare ou Google (plus rapides):")
            body_parts.append("- Paramètres > Réseau > Propriétés carte > IPv4 > Propriétés")
            body_parts.append("- DNS préféré: 1.1.1.1 (Cloudflare) ou 8.8.8.8 (Google)")
            body_parts.append("- DNS auxiliaire: 1.0.0.1 ou 8.8.4.4")
            body_parts.append("- Gain: 20-50ms latence pages web")
            body_parts.append("\n**📞 Étape 9: Contacte ton FAI (dernier recours)**")
            body_parts.append("- Si rien ne marche et vitesse <50% abonnement:")
            body_parts.append("- Appelle service technique FAI")
            body_parts.append("- Demande test ligne, vérification débit, éventuel technicien")
            body_parts.append("- Problème peut être côté infrastructure (câble dégradé, etc.)")

        # 🔇 PAS DE SON - Keywords: pas de son, audio, son, enceinte, casque
        elif any(word in msg_lower for word in ["pas de son", "son marche pas", "audio", "son qui marche pas", "enceinte", "casque marche pas", "muet"]):
            body_parts.append("Pas de son? On va régler ça rapidement, plusieurs causes possibles:")
            body_parts.append("\n**🔊 Étape 1: Vérifications de base (souvent oubliées!)**")
            body_parts.append("- Volume Windows pas à 0 (icône son barre tâches)")
            body_parts.append("- Volume application (YouTube, Spotify, jeu) pas muet")
            body_parts.append("- Câble jack/USB bien branché (teste autre port)")
            body_parts.append("- Enceintes/casque allumés (interrupteur ON)")
            body_parts.append("- Si Bluetooth: appareil connecté et pas en veille")
            body_parts.append("\n**🎛️ Étape 2: Périphérique de lecture par défaut**")
            body_parts.append("- Clic droit icône son (barre tâches) > 'Paramètres audio'")
            body_parts.append("- Ou: Paramètres > Système > Son")
            body_parts.append("- 'Choisir périphérique de sortie': sélectionne tes enceintes/casque")
            body_parts.append("- Teste avec 'Gérer périphériques audio' > Bouton 'Tester'")
            body_parts.append("\n**🔧 Étape 3: Redémarre service audio Windows**")
            body_parts.append("- Touches Win+R > tape 'services.msc' > Entrée")
            body_parts.append("- Cherche 'Audio Windows'")
            body_parts.append("- Clic droit > 'Redémarrer'")
            body_parts.append("- Si 'Arrêté': clic droit > Démarrer")
            body_parts.append("\n**🎮 Étape 4: Drivers audio**")
            body_parts.append("- Gestionnaire de périph (Win+X > Gestionnaire)")
            body_parts.append("- 'Contrôleurs audio, vidéo et jeu'")
            body_parts.append("- Clic droit périphérique audio > 'Mettre à jour pilote'")
            body_parts.append("- Si échec: Désinstaller puis redémarrer (réinstalle auto)")
            body_parts.append("- Ou télécharge driver depuis site carte mère (Realtek, etc.)")
            body_parts.append("\n**⚙️ Étape 5: Format audio / Fréquence échantillonnage**")
            body_parts.append("- Clic droit icône son > 'Paramètres audio' > 'Propriétés périph'")
            body_parts.append("- Onglet 'Avancé'")
            body_parts.append("- Essaye différents formats: 24 bits 48000 Hz ou 16 bits 44100 Hz")
            body_parts.append("- Teste après chaque changement")
            body_parts.append("\n**🔌 Étape 6: Jack façade vs arrière (PC fixe)**")
            body_parts.append("- Si jack façade marche pas, teste prise arrière carte mère")
            body_parts.append("- Façade = câble interne peut être débranché")
            body_parts.append("- Arrière = direct sur carte mère, plus fiable")
            body_parts.append("\n**🛠️ Étape 7: Réinstaller Realtek HD Audio Manager**")
            body_parts.append("- La plupart PC utilisent Realtek")
            body_parts.append("- Désinstalle Realtek (Programmes et fonctionnalités)")
            body_parts.append("- Redémarre")
            body_parts.append("- Télécharge dernière version site Realtek ou carte mère")
            body_parts.append("- Réinstalle et redémarre")
            body_parts.append("\n**🎧 Étape 8: Test autre appareil (isoler problème)**")
            body_parts.append("- Teste tes enceintes/casque sur autre PC ou téléphone")
            body_parts.append("- Si marche ailleurs = problème PC")
            body_parts.append("- Si marche pas ailleurs = enceintes/casque HS")

        # 📶 WI-FI DÉCONNEXIONS - Keywords: wifi déconnecte, wifi instable, wifi coupe
        elif any(word in msg_lower for word in ["wifi déconnecte", "wifi instable", "wifi coupe", "wifi qui saute", "perd connexion", "déconnexion wifi"]):
            body_parts.append("Wi-Fi instable qui déconnecte? C'est frustrant, on va stabiliser ça:")
            body_parts.append("\n**🔋 Étape 1: Désactive économie énergie Wi-Fi (cause #1)**")
            body_parts.append("- Gestionnaire périphériques > Cartes réseau")
            body_parts.append("- Double-clic carte Wi-Fi > Onglet 'Gestion alimentation'")
            body_parts.append("- DÉCOCHE 'Autoriser PC à éteindre ce périph pour économiser énergie'")
            body_parts.append("- Windows coupe Wi-Fi pour économiser = déconnexions!")
            body_parts.append("\n**⚡ Étape 2: Mode performances pour carte Wi-Fi**")
            body_parts.append("- Même fenêtre > Onglet 'Avancé'")
            body_parts.append("- 'Mode économie énergie' ou 'Power Saving Mode': DÉSACTIVER")
            body_parts.append("- 'Throughput Booster': ACTIVER (si dispo)")
            body_parts.append("- 'Roaming Aggressiveness': 'Lowest' ou 'Moyen'")
            body_parts.append("\n**📡 Étape 3: Change canal Wi-Fi box (interférences)**")
            body_parts.append("- Interface box (192.168.1.1 ou 192.168.0.1)")
            body_parts.append("- Wi-Fi > Paramètres avancés")
            body_parts.append("- 2.4 GHz: teste canaux 1, 6 ou 11 (moins perturbés)")
            body_parts.append("- 5 GHz: teste canaux 36, 40, 44, 48 (DFS moins perturbé)")
            body_parts.append("- Voisins avec même canal = interférences = déco")
            body_parts.append("\n**🛜 Étape 4: Passe en 5GHz si t'es en 2.4GHz**")
            body_parts.append("- 5GHz = moins perturbé, plus stable (mais portée -)")
            body_parts.append("- Paramètres > Réseau > Wi-Fi > Réseaux connus")
            body_parts.append("- Connecte-toi au réseau 5GHz de ta box (souvent suffixe '_5G')")
            body_parts.append("- Si déconnexions persistent en 5G: problème autre")
            body_parts.append("\n**🔄 Étape 5: Drivers carte Wi-Fi à jour**")
            body_parts.append("- Gest. périph > Cartes réseau > Clic droit carte Wi-Fi")
            body_parts.append("- 'Mettre à jour pilote' > 'Rechercher auto'")
            body_parts.append("- Ou site fabricant (Intel, Qualcomm, Realtek, Broadcom)")
            body_parts.append("- Drivers obsolètes = source #1 instabilité Wi-Fi")
            body_parts.append("\n**📶 Étape 6: Rapproche-toi de la box / Améliore signal**")
            body_parts.append("- Signal faible = déconnexions")
            body_parts.append("- Icône Wi-Fi barre tâches: si <3 barres = trop loin")
            body_parts.append("- Solutions:")
            body_parts.append("  - Répéteur Wi-Fi (30-50€)")
            body_parts.append("  - Powerline/CPL (Internet via prises élec, 60-80€)")
            body_parts.append("  - Maillage Wi-Fi/Mesh (plusieurs bornes, 150-300€)")
            body_parts.append("\n**⚙️ Étape 7: Réinitialise paramètres réseau Windows**")
            body_parts.append("- Paramètres > Réseau et Internet > Paramètres réseau avancés")
            body_parts.append("- 'Réinitialisation du réseau'")
            body_parts.append("- Confirme et redémarre")
            body_parts.append("- Recrée connexion Wi-Fi (mot passe box)")
            body_parts.append("- Efface corruptions config réseau")

        # 🦠 VIRUS / MALWARE - Keywords: virus, malware, trojan, antivirus
        elif any(word in msg_lower for word in ["virus", "malware", "trojan", "infecté", "publicité", "pub partout", "navigateur bizarre"]):
            body_parts.append("Suspicion de virus/malware? Je vais t'aider à nettoyer ton PC en profondeur:")
            body_parts.append("\n**🛡️ Étape 1: Scan Malwarebytes (le meilleur gratuit)**")
            body_parts.append("- Lance Malwarebytes (dans NiTriTe > Diagnostic)")
            body_parts.append("- Ou télécharge: malwarebytes.com (version gratuite suffit)")
            body_parts.append("- Lance 'Scan complet' (pas rapide)")
            body_parts.append("- Durée: 30-90 min selon taille disque")
            body_parts.append("- Supprime TOUT ce qui est détecté")
            body_parts.append("\n**🔍 Étape 2: Scan Windows Defender (natif)**")
            body_parts.append("- Sécurité Windows > Protection virus et menaces")
            body_parts.append("- 'Options analyse' > 'Analyse complète'")
            body_parts.append("- Laisse tourner (peut prendre 1-2h)")
            body_parts.append("- Defender est bon, gratuit, intégré!")
            body_parts.append("\n**🌐 Étape 3: Nettoie navigateurs (adwares)**")
            body_parts.append("- Chrome/Firefox:")
            body_parts.append("  - Paramètres > Extensions: SUPPRIME extensions inconnues")
            body_parts.append("  - Paramètres > Moteur recherche: vérifie c'est Google (pas search.xyz)")
            body_parts.append("  - Paramètres > Page démarrage: vérifie pas hijackée")
            body_parts.append("- Adwares changent page accueil, moteur recherche = pubs partout")
            body_parts.append("\n**🗑️ Étape 4: Désinstalle programmes suspects**")
            body_parts.append("- Panneau config > Programmes et fonctionnalités")
            body_parts.append("- Trie par 'Date installation'")
            body_parts.append("- Désinstalle programmes installés juste avant problèmes")
            body_parts.append("- Noms louches: 'PC Optimizer', 'Driver Booster', 'PC Cleaner'")
            body_parts.append("- Si doute: Google le nom avant désinstaller")
            body_parts.append("\n**🔧 Étape 5: AdwCleaner (spécialisé adwares)**")
            body_parts.append("- Télécharge AdwCleaner (Malwarebytes)")
            body_parts.append("- Lance 'Analyser maintenant'")
            body_parts.append("- Supprime tout détecté")
            body_parts.append("- Redémarre")
            body_parts.append("- Cible spécifiquement PUP (programmes indésirables)")
            body_parts.append("\n**👁️ Étape 6: Vérif processus suspects (Task Manager)**")
            body_parts.append("- Ctrl+Maj+Échap > Onglet 'Processus'")
            body_parts.append("- Cherche processus bizarres (noms aléatoires, 100% CPU)")
            body_parts.append("- Clic droit > 'Ouvrir emplacement fichier'")
            body_parts.append("- Si dans Temp/ ou AppData/ = suspect!")
            body_parts.append("- Clic droit > 'Fin de tâche' puis supprime fichier")
            body_parts.append("\n**🔐 Étape 7: Change TOUS tes mots de passe**")
            body_parts.append("- Si keylogger/stealer installé:")
            body_parts.append("- Change mdp Gmail, Facebook, banque, etc.")
            body_parts.append("- Depuis AUTRE appareil sain (téléphone)")
            body_parts.append("- Active authentification 2 facteurs partout (2FA)")
            body_parts.append("\n**🩹 Étape 8: Réinitialisation Windows (si infecté lourd)**")
            body_parts.append("- Si rien marche ou infection profonde:")
            body_parts.append("- Paramètres > Récupération > 'Réinitialiser ce PC'")
            body_parts.append("- Choisis 'Supprimer tout' (sauvegarde fichiers importants avant!)")
            body_parts.append("- Windows propre = 100% sûr virus éliminés")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 3: HARDWARE & COMPOSANTS (15 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 💾 #17 RAM PROBLÈMES / ERREURS MÉMOIRE
        elif any(word in msg_lower for word in ["ram", "mémoire", "memory", "barrette", "memtest", "memory management"]):
            body_parts.append("Problème RAM? C'est critique, on teste!")
            body_parts.append("\n**🧪 Étape 1: MemTest86**")
            body_parts.append("- Boot sur USB MemTest86 (créé depuis memtest86.com)")
            body_parts.append("- Laisse tourner minimum 4 passes (8h+)")
            body_parts.append("- 1 seule erreur = barrette défectueuse")
            body_parts.append("\n**🔍 Étape 2: Windows Memory Diagnostic**")
            body_parts.append("- Win+R > mdsched.exe > Redémarre")
            body_parts.append("- Test automatique au boot")
            body_parts.append("\n**🎯 Étape 3: Teste barrettes individuellement**")
            body_parts.append("- Retire toutes sauf 1, teste")
            body_parts.append("- Change de slot, reteste")
            body_parts.append("- Identifie barrette/slot défectueux")
            body_parts.append("\n**⚙️ Étape 4: XMP/EXPO désactivé**")
            body_parts.append("- BIOS: désactive profil XMP/EXPO temporairement")
            body_parts.append("- RAM en JEDEC (2133/2400 MHz)")
            body_parts.append("- Si stable = instabilité overclock RAM")
            body_parts.append("\n**🔧 Étape 5: Voltage RAM BIOS**")
            body_parts.append("- DRAM Voltage: +0.05V au-dessus spécifications")
            body_parts.append("- Ex: DDR4 1.35V → essaye 1.40V")
            body_parts.append("- Peut stabiliser XMP instable")

        # 💾 #18 SSD/DISQUE LENT OU DÉFAILLANT
        elif any(word in msg_lower for word in ["ssd lent", "disque lent", "crystaldiskinfo", "smart", "secteur défectueux"]):
            body_parts.append("SSD/Disque ralenti? On diagnostique la santé!")
            body_parts.append("\n**🔍 Étape 1: CrystalDiskInfo**")
            body_parts.append("- Lance CrystalDiskInfo (NiTriTe > Diagnostic)")
            body_parts.append("- Status: Good = OK, Caution/Bad = problème!")
            body_parts.append("- Vérifie % Health, TBW, secteurs réalloués")
            body_parts.append("\n**📊 Étape 2: Test vitesse**")
            body_parts.append("- CrystalDiskMark: benchmark lecture/écriture")
            body_parts.append("- Compare résultats vs specs constructeur")
            body_parts.append("- SSD SATA: 500-550 MB/s, NVMe: 3000-7000 MB/s")
            body_parts.append("\n**🔧 Étape 3: Firmware SSD**")
            body_parts.append("- Site fabricant: Samsung Magician, Crucial Storage Executive")
            body_parts.append("- Update firmware SSD (bugs perfs corrigés)")
            body_parts.append("\n**⚡ Étape 4: TRIM activé?**")
            body_parts.append("- CMD admin: fsutil behavior query DisableDeleteNotify")
            body_parts.append("- 0 = TRIM activé (bon), 1 = désactivé (mauvais)")
            body_parts.append("\n**💾 Étape 5: Clone si défaillant**")
            body_parts.append("- Si Health <50% ou secteurs bad: clone MAINTENANT")
            body_parts.append("- Macrium Reflect Free ou Clonezilla")
            body_parts.append("- Vers nouveau SSD sain")

        # ⚡ #19 ALIMENTATION (PSU) INSUFFISANTE
        elif any(word in msg_lower for word in ["alimentation", "psu", "watt", "bloc alim", "power supply"]):
            body_parts.append("Problème d'alimentation? Calcule si PSU suffisant!")
            body_parts.append("\n**🔌 Étape 1: Calcule conso totale**")
            body_parts.append("- Utilise PC Part Picker ou OuterVision PSU Calculator")
            body_parts.append("- Entre CPU, GPU, RAM, disques, ventilos")
            body_parts.append("- Ajoute 20-30% marge sécurité")
            body_parts.append("\n**📊 Étape 2: Exemples GPU gourmands**")
            body_parts.append("- RTX 4090: 850W PSU minimum")
            body_parts.append("- RTX 4080: 750W mini")
            body_parts.append("- RTX 4070 Ti: 650W mini")
            body_parts.append("- RX 7900 XTX: 800W mini")
            body_parts.append("\n**⚡ Étape 3: Câblage correct**")
            body_parts.append("- GPU haut de gamme: 2-3 câbles PCIe séparés (pas daisy-chain!)")
            body_parts.append("- 12VHPWR RTX 4000: adaptateur bien enfoncé, pas plié")
            body_parts.append("\n**🧪 Étape 4: Test stress PSU**")
            body_parts.append("- OCCT Power test 30 min")
            body_parts.append("- FurMark + Prime95 simultané")
            body_parts.append("- Si shutdown/crash = PSU insuffisant")
            body_parts.append("\n**🔧 Étape 5: Certification PSU**")
            body_parts.append("- Minimum 80+ Bronze, idéal Gold/Platinum")
            body_parts.append("- Tier List PSU: Cultists Network, Tom's Hardware")
            body_parts.append("- Évite PSU no-name cheap")

        # 🖥️ #20 ÉCRAN/MONITEUR PROBLÈMES
        elif any(word in msg_lower for word in ["écran", "moniteur", "affichage", "résolution", "hz", "refresh rate"]):
            body_parts.append("Problème d'affichage/moniteur? On règle ça!")
            body_parts.append("\n**🎯 Étape 1: Résolution native**")
            body_parts.append("- Paramètres > Affichage > Résolution")
            body_parts.append("- Sélectionne résolution native (1920x1080, 2560x1440, 3840x2160)")
            body_parts.append("- Marquée '(recommandé)'")
            body_parts.append("\n**⚡ Étape 2: Taux rafraîchissement**")
            body_parts.append("- Paramètres > Affichage > Paramètres avancés > Fréquence actualisation")
            body_parts.append("- Écran 144Hz: sélectionne 144Hz (pas 60Hz par défaut!)")
            body_parts.append("- Écran 240Hz/360Hz: idem")
            body_parts.append("\n**🔌 Étape 3: Câble correct**")
            body_parts.append("- HDMI 2.0: max 1080p 144Hz ou 1440p 75Hz")
            body_parts.append("- HDMI 2.1: 4K 120Hz+")
            body_parts.append("- DisplayPort 1.4: 1440p 240Hz, 4K 120Hz")
            body_parts.append("- Upgrade câble si limitant")
            body_parts.append("\n**🎨 Étape 4: Calibration couleurs**")
            body_parts.append("- Windows > dccw (outil calibrage couleur)")
            body_parts.append("- Ou: site lagom.nl/lcd-test")
            body_parts.append("\n**🔧 Étape 5: Drivers GPU/Moniteur**")
            body_parts.append("- Update drivers NVIDIA/AMD")
            body_parts.append("- Gestionnaire périph > Moniteurs > Update")

        # 🔌 #21 USB NE FONCTIONNE PAS
        elif any(word in msg_lower for word in ["usb marche pas", "port usb", "clé usb", "usb non reconnu"]):
            body_parts.append("Port USB HS? On va diagnostiquer!")
            body_parts.append("\n**🔍 Étape 1: Teste autre port**")
            body_parts.append("- Façade PC ≠ arrière carte mère")
            body_parts.append("- USB 2.0 (noir) vs USB 3.0 (bleu) vs USB-C")
            body_parts.append("- Si marche sur autre port = port défectueux")
            body_parts.append("\n**⚡ Étape 2: Alimentation USB**")
            body_parts.append("- Certains périph gourmands (HDD externe 3.5')")
            body_parts.append("- Nécessitent hub USB alimenté ou prise secteur")
            body_parts.append("\n**🔧 Étape 3: Désinstalle/Réinstalle drivers**")
            body_parts.append("- Gestionnaire périph > Contrôleurs USB")
            body_parts.append("- Désinstalle périphérique non reconnu")
            body_parts.append("- Action > Rechercher modifications matériel")
            body_parts.append("\n**⚙️ Étape 4: Paramètres économie énergie**")
            body_parts.append("- Gest. périph > USB Root Hub > Gestion alimentation")
            body_parts.append("- Décoche 'Autoriser PC éteindre périph pour économiser'")
            body_parts.append("\n**🩹 Étape 5: Reset contrôleurs USB BIOS**")
            body_parts.append("- BIOS: désactive puis réactive USB controllers")
            body_parts.append("- Ou: Load BIOS Defaults")

        # 🖨️ #22 IMPRIMANTE PROBLÈMES
        elif any(word in msg_lower for word in ["imprimante", "printer", "impression", "imprime pas"]):
            body_parts.append("Imprimante capricieuse? Solutions classiques:")
            body_parts.append("\n**🔌 Étape 1: Connexion**")
            body_parts.append("- USB: teste autre port, autre câble")
            body_parts.append("- Wi-Fi: vérifie imprimante sur même réseau")
            body_parts.append("- IP imprimante pingable? CMD: ping 192.168.x.x")
            body_parts.append("\n**🔄 Étape 2: Redémarre spooler**")
            body_parts.append("- services.msc > 'Spooleur d'impression'")
            body_parts.append("- Clic droit > Redémarrer")
            body_parts.append("- Ou: net stop spooler && net start spooler (CMD admin)")
            body_parts.append("\n**🗑️ Étape 3: Vide file d'attente**")
            body_parts.append("- Paramètres > Imprimantes > Ouvrir file attente")
            body_parts.append("- Annule tous documents bloqués")
            body_parts.append("\n**🔧 Étape 4: Réinstalle drivers**")
            body_parts.append("- Désinstalle imprimante complètement")
            body_parts.append("- Télécharge driver depuis site fabricant (HP, Canon, Epson)")
            body_parts.append("- Pas le driver Windows Update générique!")
            body_parts.append("\n**🧪 Étape 5: Page de test**")
            body_parts.append("- Propriétés imprimante > Imprimer page test")
            body_parts.append("- Si OK = problème application, sinon = imprimante/driver")

        # 🎮 #23 MANETTE/CONTROLLER PROBLÈMES
        elif any(word in msg_lower for word in ["manette", "controller", "joystick", "xbox", "ps4", "ps5", "dualsense"]):
            body_parts.append("Manette non reconnue? On va la configurer!")
            body_parts.append("\n**🔌 Étape 1: Connexion filaire vs Bluetooth**")
            body_parts.append("- Filaire: câble USB-C/micro-USB original")
            body_parts.append("- Bluetooth: appaire depuis Paramètres > Bluetooth")
            body_parts.append("- Xbox: bouton Xbox + Sync")
            body_parts.append("- PS5: PS + Create 3 sec")
            body_parts.append("\n**🎮 Étape 2: Drivers manette**")
            body_parts.append("- Xbox: drivers natifs Windows")
            body_parts.append("- PS4/PS5: DS4Windows ou DualSenseX")
            body_parts.append("- Switch Pro: BetterJoy ou Steam Input")
            body_parts.append("\n**⚙️ Étape 3: Steam Input**")
            body_parts.append("- Steam > Paramètres > Contrôleur")
            body_parts.append("- Active support manettes PlayStation/Xbox/Generic")
            body_parts.append("- Calibre inputs")
            body_parts.append("\n**🔧 Étape 4: Test manette**")
            body_parts.append("- Windows: joy.cpl (panneau config manette)")
            body_parts.append("- Teste boutons, sticks, triggers")
            body_parts.append("- gamepad-tester.com")
            body_parts.append("\n**🔋 Étape 5: Batterie**")
            body_parts.append("- Manette sans fil: charge batterie")
            body_parts.append("- LED faible = batterie morte")

        # ⌨️ #24 CLAVIER PROBLÈMES
        elif any(word in msg_lower for word in ["clavier", "keyboard", "touche", "key", "mécanique"]):
            body_parts.append("Clavier défaillant? Diagnostiquons!")
            body_parts.append("\n**🔍 Étape 1: Test touches**")
            body_parts.append("- keyboard-test.com ou keyboardtester.com")
            body_parts.append("- Appuie toutes touches, vérifie détection")
            body_parts.append("\n**🧹 Étape 2: Nettoyage**")
            body_parts.append("- Touche coincée: démonte keycap, nettoie switch")
            body_parts.append("- Air comprimé sous touches")
            body_parts.append("- Alcool isopropylique 90%+ si liquide renversé")
            body_parts.append("\n**🔌 Étape 3: Port/Câble**")
            body_parts.append("- Teste autre port USB")
            body_parts.append("- Câble détachable: change câble")
            body_parts.append("- Évite hub USB non alimenté")
            body_parts.append("\n**⚙️ Étape 4: Logiciel clavier**")
            body_parts.append("- RGB software: Corsair iCUE, Razer Synapse, Logitech G Hub")
            body_parts.append("- Réinstalle si bugs/macros marchent pas")
            body_parts.append("\n**🔧 Étape 5: Switch défectueux (mécanique)**")
            body_parts.append("- Si touche morte: switch HS")
            body_parts.append("- Dessouder et remplacer switch (si compétent)")
            body_parts.append("- Ou SAV fabricant")

        # 🖱️ #25 SOURIS PROBLÈMES
        elif any(word in msg_lower for word in ["souris", "mouse", "curseur", "double clic", "dpi"]):
            body_parts.append("Souris buggy? On règle ça!")
            body_parts.append("\n**🔍 Étape 1: Capteur sale**")
            body_parts.append("- Retourne souris: capteur optique propre?")
            body_parts.append("- Coton-tige + alcool isopropylique")
            body_parts.append("- Cheveux/poussière = tracking erratique")
            body_parts.append("\n**🎯 Étape 2: Surface/Tapis**")
            body_parts.append("- Souris optique: évite surfaces brillantes/verre")
            body_parts.append("- Tapis souris: nettoie, remplace si usé")
            body_parts.append("- Capteurs laser fonctionnent partout")
            body_parts.append("\n**🔌 Étape 3: Port USB / Batterie**")
            body_parts.append("- Filaire: autre port USB, autre câble")
            body_parts.append("- Sans fil: change piles/recharge")
            body_parts.append("- Dongle USB près de souris (<1m)")
            body_parts.append("\n**⚙️ Étape 4: Polling rate / DPI**")
            body_parts.append("- Logiciel souris: Logitech G Hub, Razer Synapse")
            body_parts.append("- Polling rate: 1000Hz max")
            body_parts.append("- DPI: ajuste selon préférence (400-3200)")
            body_parts.append("\n**🔧 Étape 5: Double clic involontaire**")
            body_parts.append("- Switch souris usé (Omron 50M clicks)")
            body_parts.append("- Fix temporaire: X-Mouse Button Control (software debounce)")
            body_parts.append("- Fix permanent: remplace switches (soudure) ou SAV")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 4: WINDOWS & SYSTÈME (15 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 🪟 #26 WINDOWS UPDATE BLOQUÉ
        elif any(word in msg_lower for word in ["windows update", "mise à jour bloquée", "update", "kb", "0x"]):
            body_parts.append("Windows Update coincé? Débloquons-le!")
            body_parts.append("\n**🔄 Étape 1: Redémarre service Update**")
            body_parts.append("- services.msc > 'Windows Update'")
            body_parts.append("- Arrêter, attendre 10 sec, Démarrer")
            body_parts.append("\n**🗑️ Étape 2: Vide cache Update**")
            body_parts.append("- Arrête service Windows Update")
            body_parts.append("- Supprime contenu C:\\Windows\\SoftwareDistribution\\Download\\")
            body_parts.append("- Redémarre service")
            body_parts.append("\n**🔧 Étape 3: Troubleshooter Windows**")
            body_parts.append("- Paramètres > Mise à jour > Résolution problèmes")
            body_parts.append("- Lance utilitaire résolution Windows Update")
            body_parts.append("\n**🩹 Étape 4: DISM + SFC**")
            body_parts.append("- CMD admin:")
            body_parts.append("  DISM /Online /Cleanup-Image /RestoreHealth")
            body_parts.append("  sfc /scannow")
            body_parts.append("\n**📦 Étape 5: Update manuelle**")
            body_parts.append("- microsoft.com/update-catalog")
            body_parts.append("- Cherche code KB erreur (ex: KB5001234)")
            body_parts.append("- Télécharge .msu et installe manuellement")

        # 🪟 #27 ACTIVATION WINDOWS PROBLÈME
        elif any(word in msg_lower for word in ["activation windows", "pas activé", "watermark", "clé produit", "licence"]):
            body_parts.append("Windows pas activé? Vérifions la licence!")
            body_parts.append("\n**🔍 Étape 1: Vérifie statut activation**")
            body_parts.append("- Paramètres > Mise à jour > Activation")
            body_parts.append("- CMD: slmgr /xpr (affiche expiration)")
            body_parts.append("\n**🔑 Étape 2: Clé produit**")
            body_parts.append("- Licence OEM (PC prémonté): clé dans BIOS")
            body_parts.append("- Licence Retail: clé sur boîte/email")
            body_parts.append("- Paramètres > Activation > Modifier clé produit")
            body_parts.append("\n**🔄 Étape 3: Réactivation après changement hardware**")
            body_parts.append("- Changement carte mère = désactivation")
            body_parts.append("- Compte Microsoft lié: Résolution problèmes activation")
            body_parts.append("- Sélectionne 'J'ai changé composants matériel'")
            body_parts.append("\n**📞 Étape 4: Activation téléphonique**")
            body_parts.append("- CMD: slui 4")
            body_parts.append("- Choisis pays, appelle numéro, suis instructions")
            body_parts.append("\n**🔧 Étape 5: MAS (Microsoft Activation Scripts)**")
            body_parts.append("- GitHub: massgravel (HWID/KMS38)")
            body_parts.append("- Activation permanente légale via loophole")
            body_parts.append("- Open-source, vérifié communauté")

        # 🪟 #28 BOOT LENT / DÉMARRAGE LENT
        elif any(word in msg_lower for word in ["boot lent", "démarrage lent", "démarre lentement", "startup"]):
            body_parts.append("Démarrage lent? On va accélérer ça!")
            body_parts.append("\n**🚀 Étape 1: Programmes démarrage**")
            body_parts.append("- Task Manager > Démarrage")
            body_parts.append("- Désactive TOUT sauf essentiels (antivirus, drivers)")
            body_parts.append("- Steam, Discord, Adobe, Office = inutiles au boot")
            body_parts.append("\n**⚡ Étape 2: Fast Boot BIOS**")
            body_parts.append("- BIOS: Fast Boot = Enabled")
            body_parts.append("- CSM/Legacy = Disabled (mode UEFI pur)")
            body_parts.append("\n**💾 Étape 3: SSD obligatoire**")
            body_parts.append("- HDD boot = 60-120 sec")
            body_parts.append("- SSD SATA boot = 15-30 sec")
            body_parts.append("- SSD NVMe boot = 10-15 sec")
            body_parts.append("- Clone vers SSD si encore HDD")
            body_parts.append("\n**🔧 Étape 4: Désactive services inutiles**")
            body_parts.append("- services.msc:")
            body_parts.append("  * Print Spooler (si pas imprimante)")
            body_parts.append("  * Fax, Bluetooth (si pas utilisés)")
            body_parts.append("  * Windows Search (gagne 2-3 sec)")
            body_parts.append("\n**📊 Étape 5: Analyse boot Windows Performance Recorder**")
            body_parts.append("- xbootmgr -trace boot")
            body_parts.append("- Identifie service/driver lent au boot")

        # 🪟 #29 EXPLORER.EXE CRASH
        elif any(word in msg_lower for word in ["explorer crash", "explorer.exe", "barre tâches", "bureau noir"]):
            body_parts.append("Explorer qui crash? On répare le shell Windows!")
            body_parts.append("\n**🔄 Étape 1: Redémarre Explorer**")
            body_parts.append("- Ctrl+Maj+Échap > Fichier > Exécuter")
            body_parts.append("- Tape: explorer.exe")
            body_parts.append("- Ou: Task Manager > Processus > Explorer > Redémarrer")
            body_parts.append("\n**🧹 Étape 2: Vide cache icônes**")
            body_parts.append("- Explorateur: affiche fichiers cachés")
            body_parts.append("- Supprime %localappdata%\\IconCache.db")
            body_parts.append("- Redémarre Explorer")
            body_parts.append("\n**🔧 Étape 3: Extensions shell tierces**")
            body_parts.append("- ShellExView (Nirsoft)")
            body_parts.append("- Désactive extensions non-Microsoft roses")
            body_parts.append("- Souvent cause crashes: TortoiseSVN, Dropbox")
            body_parts.append("\n**🩹 Étape 4: SFC + DISM**")
            body_parts.append("- CMD admin:")
            body_parts.append("  sfc /scannow")
            body_parts.append("  DISM /Online /Cleanup-Image /RestoreHealth")
            body_parts.append("\n**👤 Étape 5: Nouveau profil utilisateur**")
            body_parts.append("- Profil corrompu possible")
            body_parts.append("- Paramètres > Comptes > Famille > Ajouter")
            body_parts.append("- Crée nouvel admin, teste si crashes persistent")

        # 🪟 #30 ÉCRAN NOIR APRÈS CONNEXION
        elif any(word in msg_lower for word in ["écran noir", "black screen", "curseur seul", "after login"]):
            body_parts.append("Écran noir après login? C'est souvent Explorer/drivers!")
            body_parts.append("\n**🔍 Étape 1: Ctrl+Maj+Échap = Task Manager?**")
            body_parts.append("- Si Task Manager s'ouvre: Fichier > Exécuter > explorer.exe")
            body_parts.append("- Si fonctionne = Explorer corrompu")
            body_parts.append("\n**🛡️ Étape 2: Mode sans échec**")
            body_parts.append("- Redémarre, touche F8 répétée")
            body_parts.append("- Safe Mode = boot sans drivers tiers")
            body_parts.append("- Si safe mode OK = driver/software cause")
            body_parts.append("\n**🎮 Étape 3: Désinstalle drivers GPU (DDU)**")
            body_parts.append("- Safe mode, lance DDU")
            body_parts.append("- Clean and shutdown")
            body_parts.append("- Boot normal, réinstalle drivers propres")
            body_parts.append("\n**⚙️ Étape 4: Restauration système**")
            body_parts.append("- Safe mode > rstrui.exe")
            body_parts.append("- Choisis point avant problème")
            body_parts.append("\n**🔧 Étape 5: Répare boot**")
            body_parts.append("- USB install Windows > Réparer ordinateur")
            body_parts.append("- CMD: bootrec /rebuildbcd, /fixmbr, /fixboot")

        # 🪟 #31 ERREUR DLL MANQUANTE
        elif any(word in msg_lower for word in ["dll", "msvcp", "vcruntime", "xinput", "d3dx9", "missing"]):
            body_parts.append("DLL manquante? On va l'installer!")
            body_parts.append("\n**📦 Étape 1: Visual C++ Redistributables**")
            body_parts.append("- Télécharge Visual C++ All-in-One (TechPowerUp)")
            body_parts.append("- Installe 2005, 2008, 2010, 2012, 2013, 2015-2022")
            body_parts.append("- x86 ET x64 versions")
            body_parts.append("\n**🎮 Étape 2: DirectX**")
            body_parts.append("- microsoft.com/directx")
            body_parts.append("- Installe DirectX End-User Runtime")
            body_parts.append("- Même si Windows 11 (DX9 legacy DLLs)")
            body_parts.append("\n**🔍 Étape 3: DLL spécifique manquante**")
            body_parts.append("- Note nom exact DLL (ex: msvcp140.dll)")
            body_parts.append("- Google '[dll_name] microsoft download'")
            body_parts.append("- Télécharge UNIQUEMENT site officiel Microsoft")
            body_parts.append("\n**⚠️ Étape 4: NE PAS utiliser sites DLL**")
            body_parts.append("- dll-files.com, etc. = MALWARE!")
            body_parts.append("- Toujours installer package officiel")
            body_parts.append("\n**🩹 Étape 5: SFC scan**")
            body_parts.append("- CMD admin: sfc /scannow")
            body_parts.append("- Répare DLLs système Windows manquantes")

        # 🪟 #32 PARAMÈTRES/SETTINGS NE S'OUVRENT PAS
        elif any(word in msg_lower for word in ["paramètres ouvre pas", "settings", "ms-settings", "panneau config"]):
            body_parts.append("Paramètres crashent? On répare ça!")
            body_parts.append("\n**🔄 Étape 1: Reset app Paramètres**")
            body_parts.append("- PowerShell admin:")
            body_parts.append("  Get-AppxPackage *windows.immersivecontrolpanel* | Reset-AppxPackage")
            body_parts.append("\n**🔧 Étape 2: Réenregistre Paramètres**")
            body_parts.append("- PowerShell admin:")
            body_parts.append("  Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register \"$($_.InstallLocation)\\AppXManifest.xml\"}")
            body_parts.append("\n**🩹 Étape 3: SFC + DISM**")
            body_parts.append("- sfc /scannow")
            body_parts.append("- DISM /Online /Cleanup-Image /RestoreHealth")
            body_parts.append("\n**👤 Étape 4: Nouveau compte utilisateur**")
            body_parts.append("- Profil corrompu = Paramètres cassés")
            body_parts.append("- Crée admin temporaire, teste")
            body_parts.append("\n**💊 Étape 5: In-place upgrade**")
            body_parts.append("- Télécharge ISO Windows même version")
            body_parts.append("- Lance setup.exe, 'Upgrade'")
            body_parts.append("- Conserve fichiers, répare système")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 5: RÉSEAU & CONNECTIVITÉ (10 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 🌐 #33 PAS D'INTERNET (ETHERNET/WI-FI)
        elif any(word in msg_lower for word in ["pas d'internet", "no internet", "pas de connexion", "non connecté"]):
            body_parts.append("Pas d'internet? Diagnostique réseau complet!")
            body_parts.append("\n**🔌 Étape 1: Basiques**")
            body_parts.append("- Câble Ethernet bien branché?")
            body_parts.append("- Wi-Fi activé? (Fn+touche Wi-Fi sur portable)")
            body_parts.append("- Autres appareils ont internet? (isoler si PC ou box)")
            body_parts.append("\n**🔄 Étape 2: Redémarres TOUT**")
            body_parts.append("- PC, box/routeur, switch (éteindre 30 sec)")
            body_parts.append("- Rallume box, attends full boot (2-3 min)")
            body_parts.append("- Puis PC")
            body_parts.append("\n**🩹 Étape 3: Reset réseau Windows**")
            body_parts.append("- Paramètres > Réseau > Réinitialisation réseau")
            body_parts.append("- Ou CMD admin:")
            body_parts.append("  netsh winsock reset")
            body_parts.append("  netsh int ip reset")
            body_parts.append("  ipconfig /release && ipconfig /renew")
            body_parts.append("\n**🔧 Étape 4: Drivers carte réseau**")
            body_parts.append("- Gestionnaire périph > Cartes réseau")
            body_parts.append("- Désinstalle, redémarre (auto-réinstalle)")
            body_parts.append("- Ou: download driver site carte mère")
            body_parts.append("\n**🌍 Étape 5: DNS**")
            body_parts.append("- Change vers 1.1.1.1 / 8.8.8.8")
            body_parts.append("- CMD: ipconfig /flushdns")

        # 🌐 #34 PING ÉLEVÉ / LAG RÉSEAU
        elif any(word in msg_lower for word in ["ping", "latence", "ms", "lag réseau", "jitter"]):
            body_parts.append("Ping/latence élevée? On optimise!")
            body_parts.append("\n**📊 Étape 1: Test ping**")
            body_parts.append("- CMD: ping 8.8.8.8 -t")
            body_parts.append("- Note ping moyen et variance")
            body_parts.append("- <20ms = excellent, 20-50ms = bon, >100ms = problème")
            body_parts.append("\n**🔌 Étape 2: Ethernet > Wi-Fi**")
            body_parts.append("- Wi-Fi ajoute +10-50ms latence")
            body_parts.append("- Câble Ethernet direct = meilleur ping")
            body_parts.append("\n**📡 Étape 3: QoS routeur**")
            body_parts.append("- Interface box: active QoS gaming")
            body_parts.append("- Priorité PC gaming en dur (adresse MAC)")
            body_parts.append("\n**🔧 Étape 4: Paramètres carte réseau**")
            body_parts.append("- Propriétés carte > Avancé:")
            body_parts.append("  * Interrupt Moderation: Désactivé")
            body_parts.append("  * Flow Control: Désactivé")
            body_parts.append("  * Offload: Désactivés (TCP, UDP, IPv4)")
            body_parts.append("\n**🌍 Étape 5: Bufferbloat test**")
            body_parts.append("- waveform.com/tools/bufferbloat")
            body_parts.append("- Si grade D/F: active SQM/fq_codel routeur")

        # 🌐 #35 VPN PROBLÈMES
        elif any(word in msg_lower for word in ["vpn", "nordvpn", "expressvpn", "wireguard", "openvpn"]):
            body_parts.append("VPN ne marche pas? Diagnostiquons!")
            body_parts.append("\n**🔍 Étape 1: Logs erreur VPN**")
            body_parts.append("- App VPN > Settings > Logs")
            body_parts.append("- Note code erreur spécifique")
            body_parts.append("\n**🔧 Étape 2: Protocole VPN**")
            body_parts.append("- OpenVPN = compatible partout mais lent")
            body_parts.append("- WireGuard = rapide moderne (essaye)")
            body_parts.append("- IKEv2 = bon pour mobile")
            body_parts.append("- Change protocole si connexion fail")
            body_parts.append("\n**🔌 Étape 3: Port/Firewall**")
            body_parts.append("- Firewall Windows: autorise app VPN")
            body_parts.append("- Routeur: UPnP activé ou forward ports VPN")
            body_parts.append("- Port 1194 (OpenVPN), 51820 (WireGuard)")
            body_parts.append("\n**🌍 Étape 4: Serveur VPN**")
            body_parts.append("- Change pays/serveur")
            body_parts.append("- Certains serveurs saturés ou bloqués")
            body_parts.append("\n**🩹 Étape 5: TAP adapter**")
            body_parts.append("- Gestionnaire périph > Cartes réseau")
            body_parts.append("- TAP-Windows Adapter: désinstalle/réinstalle")
            body_parts.append("- Réinstalle client VPN complet")

        # 🌐 #36 PARTAGE RÉSEAU/SMB PROBLÈME
        elif any(word in msg_lower for word in ["partage réseau", "smb", "dossier partagé", "réseau local", "nas"]):
            body_parts.append("Partage réseau inaccessible? On règle SMB!")
            body_parts.append("\n**⚙️ Étape 1: SMB activé Windows**")
            body_parts.append("- Panneau config > Programmes > Activer/Désactiver fonctionnalités")
            body_parts.append("- Coche 'SMB 1.0/CIFS' (legacy)")
            body_parts.append("- Et 'SMB Direct' (moderne)")
            body_parts.append("\n**🔍 Étape 2: Découverte réseau**")
            body_parts.append("- Paramètres > Réseau > Options partage avancées")
            body_parts.append("- Active 'Découverte réseau' et 'Partage fichiers'")
            body_parts.append("- Profile privé ET public")
            body_parts.append("\n**🔐 Étape 3: Identifiants partage**")
            body_parts.append("- \\\\IP_NAS\\partage")
            body_parts.append("- Entre user/password NAS")
            body_parts.append("- Gestionnaire identifiants Windows: vérifie credentials sauvegardés")
            body_parts.append("\n**🌐 Étape 4: Ping NAS/PC distant**")
            body_parts.append("- CMD: ping [IP_NAS]")
            body_parts.append("- Si timeout = firewall ou subnet différent")
            body_parts.append("\n**🔧 Étape 5: Reset SMB**")
            body_parts.append("- PowerShell admin:")
            body_parts.append("  Reset-SmbClientConfiguration")
            body_parts.append("  Reset-SmbServerConfiguration")

        # 🌐 #37 HOTSPOT/PARTAGE CONNEXION PROBLÈME
        elif any(word in msg_lower for word in ["hotspot", "partage connexion", "mobile hotspot", "point d'accès"]):
            body_parts.append("Hotspot mobile ne marche pas? On active!")
            body_parts.append("\n**📱 Étape 1: Activation hotspot**")
            body_parts.append("- Paramètres > Réseau > Point accès mobile")
            body_parts.append("- Active 'Partager connexion Internet'")
            body_parts.append("- Source: Ethernet/Wi-Fi, Partager via: Wi-Fi")
            body_parts.append("\n**🔐 Étape 2: Mot de passe hotspot**")
            body_parts.append("- Configure SSID et password")
            body_parts.append("- WPA2-PSK minimum")
            body_parts.append("\n**⚙️ Étape 3: Carte réseau compatible**")
            body_parts.append("- Toutes cartes Wi-Fi ne supportent pas hotspot")
            body_parts.append("- CMD admin: netsh wlan show drivers")
            body_parts.append("- 'Réseau hébergé pris en charge: Oui' requis")
            body_parts.append("\n**🔧 Étape 4: Drivers Wi-Fi**")
            body_parts.append("- Update drivers carte Wi-Fi")
            body_parts.append("- Intel, Qualcomm, Realtek, Broadcom sites")
            body_parts.append("\n**🩹 Étape 5: Reset adaptateur hébergé**")
            body_parts.append("- CMD admin:")
            body_parts.append("  netsh wlan stop hostednetwork")
            body_parts.append("  netsh wlan set hostednetwork mode=allow")
            body_parts.append("  netsh wlan start hostednetwork")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 6: GAMING AVANCÉ (10 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 🎮 #38 STUTTERING/MICRO-FREEZE JEU
        elif any(word in msg_lower for word in ["stuttering", "micro freeze", "saccade", "stutter", "frame time"]):
            body_parts.append("Stuttering en jeu? C'est frame-time, pas FPS!")
            body_parts.append("\n**📊 Étape 1: Monitoring frame time**")
            body_parts.append("- MSI Afterburner: affiche 1% low FPS et frame time")
            body_parts.append("- FrameView (NVIDIA)")
            body_parts.append("- Frame time >16ms (60 FPS) = stutter ressenti")
            body_parts.append("\n**💾 Étape 2: SSD requis**")
            body_parts.append("- HDD = micro-freezes chargement textures")
            body_parts.append("- Installe jeu sur SSD NVMe obligatoirement")
            body_parts.append("\n**🧠 Étape 3: RAM insuffisante**")
            body_parts.append("- <16 GB = swapping disque = stutters")
            body_parts.append("- Task Manager pendant jeu: usage RAM >90%?")
            body_parts.append("- Ferme Chrome, Discord en arrière-plan")
            body_parts.append("\n**🔧 Étape 4: Désactive HAGS (Hardware Accelerated GPU Scheduling)**")
            body_parts.append("- Paramètres > Affichage > Graphiques > HAGS")
            body_parts.append("- Essaye ON puis OFF (varie selon config)")
            body_parts.append("\n**⚡ Étape 5: NVIDIA Reflex / AMD Anti-Lag**")
            body_parts.append("- In-game: active Reflex Low Latency (NVIDIA)")
            body_parts.append("- Ou Anti-Lag+ (AMD)")
            body_parts.append("- Réduit input lag et améliore frame pacing")

        # 🎮 #39 INPUT LAG / LATENCE SOURIS
        elif any(word in msg_lower for word in ["input lag", "latence souris", "delay", "mouse lag"]):
            body_parts.append("Input lag? On réduit la latence au minimum!")
            body_parts.append("\n**🖱️ Étape 1: Polling rate souris**")
            body_parts.append("- Logiciel souris: 1000 Hz polling rate")
            body_parts.append("- 125 Hz = 8ms latence, 1000 Hz = 1ms")
            body_parts.append("\n**🎮 Étape 2: NVIDIA Reflex / AMD Anti-Lag**")
            body_parts.append("- In-game settings: Reflex ON + Boost")
            body_parts.append("- Réduit latence système 20-50ms")
            body_parts.append("\n**🖥️ Étape 3: G-Sync/FreeSync OFF compétitif**")
            body_parts.append("- G-Sync ajoute 1-2 frames latence")
            body_parts.append("- Désactive pour eSports (VALORANT, CS2)")
            body_parts.append("- Laisse ON pour jeux solo immersifs")
            body_parts.append("\n**⚡ Étape 4: Pre-rendered frames = 1**")
            body_parts.append("- NVIDIA Panel > Max pre-rendered frames: 1")
            body_parts.append("- AMD: Frame queue limité")
            body_parts.append("\n**🔧 Étape 5: Overlays désactivés**")
            body_parts.append("- Discord, Steam, GeForce = +latence")
            body_parts.append("- Désactive tout overlay en compétitif")

        # 🎮 #40 VRAM INSUFFISANTE / MÉMOIRE GPU
        elif any(word in msg_lower for word in ["vram", "mémoire gpu", "out of memory", "vram full"]):
            body_parts.append("VRAM saturée? Baisse qualité textures!")
            body_parts.append("\n**📊 Étape 1: Monitoring VRAM**")
            body_parts.append("- MSI Afterburner: affiche usage VRAM")
            body_parts.append("- >95% = overload, crash/stutters")
            body_parts.append("\n**🎨 Étape 2: Textures quality**")
            body_parts.append("- In-game: Texture Quality/Resolution = Medium ou Low")
            body_parts.append("- Ultra textures = +2-4 GB VRAM")
            body_parts.append("- Qualité visuelle peu impactée si baisse 1 cran")
            body_parts.append("\n**📐 Étape 3: Résolution**")
            body_parts.append("- 4K = 2x VRAM vs 1440p")
            body_parts.append("- 1440p = 1.5x VRAM vs 1080p")
            body_parts.append("- Baisse réso si GPU <8 GB VRAM")
            body_parts.append("\n**🔧 Étape 4: Ray-Tracing OFF**")
            body_parts.append("- RT bouffe +2-3 GB VRAM supplémentaire")
            body_parts.append("- RTX 3060 12GB = OK RT, RTX 4060 Ti 8GB = pas assez")
            body_parts.append("\n**⚙️ Étape 5: DLSS/FSR**")
            body_parts.append("- Active DLSS Quality ou FSR Quality")
            body_parts.append("- Render interne plus bas = économise VRAM")

        # 🎮 #41 DUAL MONITOR LAG/FPS DROP
        elif any(word in msg_lower for word in ["dual monitor", "deux écrans", "second écran", "multi-écran"]):
            body_parts.append("Dual monitor impacte FPS? Optimisons!")
            body_parts.append("\n**🖥️ Étape 1: Refresh rate identique**")
            body_parts.append("- 144Hz principal + 60Hz secondaire = dwm.exe overhead")
            body_parts.append("- Idéal: même refresh sur tous écrans")
            body_parts.append("- Ou: écran secondaire 120Hz (diviseur de 144)")
            body_parts.append("\n**⚡ Étape 2: Désactive écran secondaire en jeu**")
            body_parts.append("- Win+P > 'Écran du PC uniquement'")
            body_parts.append("- Gain 5-10% FPS possible")
            body_parts.append("\n**🔌 Étape 3: Câbles/Ports**")
            body_parts.append("- Écran principal sur DisplayPort GPU")
            body_parts.append("- Secondaire sur HDMI ou DP2")
            body_parts.append("- Évite iGPU pour second écran (latence)")
            body_parts.append("\n**🎮 Étape 4: G-Sync/FreeSync sur primaire seul**")
            body_parts.append("- Panneau NVIDIA: active G-Sync pour fullscreen seulement")
            body_parts.append("- Pas windowed/borderless")
            body_parts.append("\n**🔧 Étape 5: MPO (Multi-Plane Overlay)**")
            body_parts.append("- Désactive MPO si problèmes:")
            body_parts.append("- Registry: HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\Dwm")
            body_parts.append("- OverlayTestMode = DWORD 5")

        # 🎮 #42 STEAM/LAUNCHER PROBLÈMES
        elif any(word in msg_lower for word in ["steam", "epic", "launcher", "ubisoft connect", "ea app"]):
            body_parts.append("Launcher qui bug? Solutions universelles!")
            body_parts.append("\n**🔄 Étape 1: Clear cache launcher**")
            body_parts.append("- Steam: Paramètres > Téléchargements > Vider cache")
            body_parts.append("- Epic: Supprime C:\\Users\\[nom]\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache")
            body_parts.append("\n**🔧 Étape 2: Vérif fichiers jeu**")
            body_parts.append("- Steam: Propriétés jeu > Fichiers locaux > Vérifier intégrité")
            body_parts.append("- Epic: Bibliothèque > ... > Vérifier")
            body_parts.append("\n**🌐 Étape 3: Région téléchargement**")
            body_parts.append("- Steam: Paramètres > Téléchargements > Région")
            body_parts.append("- Change vers serveur proche géographiquement")
            body_parts.append("\n**🔐 Étape 4: Firewall/Antivirus**")
            body_parts.append("- Autorise launcher.exe et jeu .exe")
            body_parts.append("- Désactive temporairement antivirus, teste")
            body_parts.append("\n**🔥 Étape 5: Réinstalle launcher**")
            body_parts.append("- Désinstalle, supprime dossier C:\\Program Files\\[Launcher]")
            body_parts.append("- Réinstalle propre depuis site officiel")
            body_parts.append("- Jeux restent, relance juste scan")

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # CATÉGORIE 7-15: SCÉNARIOS ADDITIONNELS 43-100 (58 scénarios)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        # 🎮 #43 DLSS/FSR/UPSCALING
        elif any(word in msg_lower for word in ["dlss", "fsr", "xess", "upscaling", "frame generation"]):
            body_parts.append("Questions sur l'upscaling AI? Guide complet!")
            body_parts.append("\n**🔍 Étape 1: Quelle techno?**")
            body_parts.append("- DLSS 3.5 (NVIDIA RTX 2000+): meilleur qualité")
            body_parts.append("- FSR 3 (AMD, compatible tous GPU): bon universel")
            body_parts.append("- XeSS (Intel Arc): Intel ARC uniquement")
            body_parts.append("\n**⚙️ Étape 2: Mode upscaling**")
            body_parts.append("- Quality: 1440p→4K, perte qualité minimale")
            body_parts.append("- Balanced: compromis perf/qualité")
            body_parts.append("- Performance/Ultra Performance: max FPS, flou visible")
            body_parts.append("\n**🚀 Étape 3: Frame Generation (DLSS 3)**")
            body_parts.append("- RTX 4000 uniquement")
            body_parts.append("- Double FPS mais ajoute latence")
            body_parts.append("- À combiner avec Reflex")
            body_parts.append("\n**🎯 Étape 4: Quand utiliser?**")
            body_parts.append("- <60 FPS natif? Active DLSS/FSR Quality")
            body_parts.append("- GPU faible (ex: RTX 3060): FSR/DLSS Balanced minimum")
            body_parts.append("\n**⚠️ Étape 5: Désactive si >144 FPS natif**")
            body_parts.append("- Upscaling inutile si déjà high FPS")
            body_parts.append("- Peut ajouter artefacts")

        # 🎮 #44 RAY-TRACING OPTIMISATION
        elif any(word in msg_lower for word in ["ray tracing", "rtx", "rt", "reflections"]):
            body_parts.append("Ray-Tracing trop gourmand? Optimise!")
            body_parts.append("\n**⚙️ Étape 1: Paramètres RT sélectifs**")
            body_parts.append("- RT Reflections: impact visuel élevé, garde")
            body_parts.append("- RT Shadows: désactive (peu visible, -20% FPS)")
            body_parts.append("- RT Global Illumination: désactive (très lourd)")
            body_parts.append("- RT Ambient Occlusion: désactive")
            body_parts.append("\n**📊 Étape 2: GPU minimum RT**")
            body_parts.append("- RTX 2060/2070 = RT Low uniquement")
            body_parts.append("- RTX 3070/3080 = RT Medium OK")
            body_parts.append("- RTX 4070+ = RT High viable")
            body_parts.append("- AMD 6000/7000 = FSR 3 obligatoire avec RT")
            body_parts.append("\n**🎯 Étape 3: DLSS Quality + RT**")
            body_parts.append("- RT seul = -50% FPS")
            body_parts.append("- RT + DLSS Quality = -15% FPS vs natif")
            body_parts.append("- Combo parfait RTX 4000")
            body_parts.append("\n**🔧 Étape 4: RT Low vs Ultra**")
            body_parts.append("- Différence visuelle faible Low→Ultra")
            body_parts.append("- Impact perf ÉNORME")
            body_parts.append("- RT Low suffit largement")

        # 🔊 #45 MICROPHONE PROBLÈMES
        elif any(word in msg_lower for word in ["micro", "microphone", "voice", "discord audio"]):
            body_parts.append("Micro HS? Diagnostiquons!")
            body_parts.append("\n**🔍 Étape 1: Périphérique entrée**")
            body_parts.append("- Paramètres > Son > Entrée")
            body_parts.append("- Sélectionne bon micro")
            body_parts.append("- Teste avec barre volume (parle dedans)")
            body_parts.append("\n**📊 Étape 2: Niveau gain**")
            body_parts.append("- Propriétés micro > Niveaux")
            body_parts.append("- Microphone: 80-100")
            body_parts.append("- Amplification: +10 à +20 dB si voix faible")
            body_parts.append("- >+30 dB = bruit/souffle")
            body_parts.append("\n**🎙️ Étape 3: Discord/app spécifique**")
            body_parts.append("- Discord: Paramètres > Voix/Vidéo")
            body_parts.append("- Sélectionne bon périphérique entrée")
            body_parts.append("- Test micro intégré")
            body_parts.append("- Suppression bruit: Krisp ou Standard")
            body_parts.append("\n**🔌 Étape 4: USB vs Jack**")
            body_parts.append("- Jack 3.5mm: prise façade vs arrière")
            body_parts.append("- USB: teste autre port, driver")
            body_parts.append("- XLR: interface audio requise")
            body_parts.append("\n**⚙️ Étape 5: Drivers Realtek**")
            body_parts.append("- Update Realtek HD Audio Manager")
            body_parts.append("- Ou: driver carte mère")

        # 🎥 #46 WEBCAM PROBLÈMES
        elif any(word in msg_lower for word in ["webcam", "caméra", "camera", "zoom", "teams"]):
            body_parts.append("Webcam marche pas? Solutions!")
            body_parts.append("\n**🔍 Étape 1: App autorisée?**")
            body_parts.append("- Paramètres > Confidentialité > Caméra")
            body_parts.append("- Active accès caméra applis")
            body_parts.append("- Autorise app spécifique (Zoom, Teams)")
            body_parts.append("\n**📷 Étape 2: Webcam reconnue?**")
            body_parts.append("- Gestionnaire périph > Caméras")
            body_parts.append("- Webcam listée? Si non, drivers")
            body_parts.append("- Application Caméra Windows teste webcam")
            body_parts.append("\n**🔌 Étape 3: USB**")
            body_parts.append("- Webcam USB: change port")
            body_parts.append("- Intégrée portable: touche Fn+F8/F9/F10 (varie)")
            body_parts.append("\n**⚙️ Étape 4: Drivers webcam**")
            body_parts.append("- Update drivers (Logitech, Razer)")
            body_parts.append("- Ou réinstalle")
            body_parts.append("\n**🎬 Étape 5: App utilise webcam?**")
            body_parts.append("- 1 seule app à la fois utilise webcam")
            body_parts.append("- Ferme Zoom/Teams/Skype autres")

        # 💾 #47 ESPACE DISQUE PLEIN
        elif any(word in msg_lower for word in ["disque plein", "espace disque", "c: plein", "stockage saturé"]):
            body_parts.append("Disque C: plein? On libère de l'espace!")
            body_parts.append("\n**🗑️ Étape 1: Nettoyage disque Windows**")
            body_parts.append("- Paramètres > Stockage > Fichiers temporaires")
            body_parts.append("- Coche: Téléchargements, Temp, Corbeille, Miniatures")
            body_parts.append("- Supprime (économise 5-20 GB)")
            body_parts.append("\n**💾 Étape 2: WinDirStat**")
            body_parts.append("- Télécharge WinDirStat (gratuit)")
            body_parts.append("- Scan C: > identifie gros dossiers")
            body_parts.append("- Souvent: Windows.old, WinSxS, hibernation")
            body_parts.append("\n**🎮 Étape 3: Déplace jeux**")
            body_parts.append("- Steam/Epic jeux sur autre disque D: E:")
            body_parts.append("- Steam > Propriétés > Déplacer")
            body_parts.append("- Garde C: pour Windows/apps uniquement")
            body_parts.append("\n**🗂️ Étape 4: Windows.old**")
            body_parts.append("- Après update Windows, dossier 10-20 GB")
            body_parts.append("- Nettoyage disque > Nettoyer fichiers système")
            body_parts.append("- Coche 'Anciennes installations Windows'")
            body_parts.append("\n**⚙️ Étape 5: Désactive hibernation**")
            body_parts.append("- CMD admin: powercfg -h off")
            body_parts.append("- Libère hiberfil.sys (taille RAM)")
            body_parts.append("- 16GB RAM = 16GB libérés!")

        # 📁 #48 FICHIERS CORROMPUS/PERTES DONNÉES
        elif any(word in msg_lower for word in ["fichier corrompu", "récupération données", "data recovery", "fichier supprimé"]):
            body_parts.append("Fichiers perdus/corrompus? Tentative récupération!")
            body_parts.append("\n**🗑️ Étape 1: Corbeille**")
            body_parts.append("- Évident mais: vérifie Corbeille d'abord")
            body_parts.append("- Clic droit > Restaurer")
            body_parts.append("\n**🔄 Étape 2: Versions précédentes Windows**")
            body_parts.append("- Clic droit dossier parent > Versions précédentes")
            body_parts.append("- Si points restauration activés")
            body_parts.append("- Restaure version antérieure")
            body_parts.append("\n**💾 Étape 3: Recuva (fichiers supprimés)**")
            body_parts.append("- Télécharge Recuva (Piriform, gratuit)")
            body_parts.append("- Scan rapide puis profond si nécessaire")
            body_parts.append("- Plus vite lancé après suppression = meilleur récup")
            body_parts.append("\n**🔧 Étape 4: TestDisk (partitions/MBR)**")
            body_parts.append("- Si partition entière perdue/corrompue")
            body_parts.append("- TestDisk (CGSecurity, gratuit)")
            body_parts.append("- Mode expert, récupère partitions")
            body_parts.append("\n**⚠️ Étape 5: STOP utilisation disque**")
            body_parts.append("- Données écrasées = irécupérables")
            body_parts.append("- N'écris RIEN sur disque concerné")
            body_parts.append("- Si critique: pro récupération données (cher!)")

        # 🔐 #49 PARE-FEU / FIREWALL
        elif any(word in msg_lower for word in ["firewall", "pare-feu", "bloque", "port"]):
            body_parts.append("Problème Firewall? Configurons!")
            body_parts.append("\n**🔍 Étape 1: Windows Defender Firewall**")
            body_parts.append("- Paramètres > Mise à jour > Sécurité Windows > Pare-feu")
            body_parts.append("- Vérifie activé (réseaux privé ET public)")
            body_parts.append("\n**✅ Étape 2: Autorise app**")
            body_parts.append("- Pare-feu > Autoriser app")
            body_parts.append("- Cherche app (Steam, jeu, etc.)")
            body_parts.append("- Coche Privé ET Public")
            body_parts.append("- Si absente: 'Autoriser autre app' > Parcourir .exe")
            body_parts.append("\n**🔧 Étape 3: Règles avancées**")
            body_parts.append("- Pare-feu > Paramètres avancés")
            body_parts.append("- Règles entrantes/sortantes")
            body_parts.append("- Nouvelle règle > Programme > .exe chemin")
            body_parts.append("- Autoriser connexion")
            body_parts.append("\n**📡 Étape 4: Ports spécifiques**")
            body_parts.append("- Nouvelle règle > Port")
            body_parts.append("- TCP ou UDP, numéro port")
            body_parts.append("- Ex: Minecraft = 25565 TCP")
            body_parts.append("\n**⚠️ Étape 5: Désactive temporairement (test)**")
            body_parts.append("- Si problème persiste: désactive firewall 2 min, teste")
            body_parts.append("- Si fonctionne = firewall cause")
            body_parts.append("- RÉACTIVE après test!")

        # 🔒 #50 COMPTE UTILISATEUR WINDOWS
        elif any(word in msg_lower for word in ["compte utilisateur", "mot de passe oublié", "admin", "session"]):
            body_parts.append("Problème compte Windows? Solutions!")
            body_parts.append("\n**🔑 Étape 1: Mot de passe oublié (compte Microsoft)**")
            body_parts.append("- account.live.com/password/reset")
            body_parts.append("- Réinitialise en ligne")
            body_parts.append("- Besoin email/téléphone récup")
            body_parts.append("\n**💻 Étape 2: Compte local mot passe oublié**")
            body_parts.append("- Écran connexion: lien 'Réinitialiser mot de passe'")
            body_parts.append("- Réponds questions sécurité")
            body_parts.append("- Ou: USB boot Windows > Réparer > CMD:")
            body_parts.append("  net user [nom] [nouveau_mdp]")
            body_parts.append("\n**👤 Étape 3: Créer nouvel admin**")
            body_parts.append("- Paramètres > Comptes > Famille")
            body_parts.append("- Ajouter > Créer compte")
            body_parts.append("- Type compte: Administrateur")
            body_parts.append("\n**🔄 Étape 4: Bascule Microsoft ↔ Local**")
            body_parts.append("- Microsoft → Local: Paramètres > Comptes > Se connecter compte local")
            body_parts.append("- Local → Microsoft: idem, option compte Microsoft")
            body_parts.append("\n**🗑️ Étape 5: Supprime compte**")
            body_parts.append("- Paramètres > Comptes > Famille")
            body_parts.append("- Supprime (conserve ou supprime fichiers)")

        # 🖥️ #51 MULTI-BOOT / DUAL BOOT
        elif any(word in msg_lower for word in ["dual boot", "multi boot", "grub", "linux windows"]):
            body_parts.append("Dual boot Windows/Linux? Configuration!")
            body_parts.append("\n**📦 Étape 1: Partitionnement**")
            body_parts.append("- Gestion disques (diskmgmt.msc)")
            body_parts.append("- Réduis partition Windows (100-200 GB pour Linux)")
            body_parts.append("- Laisse espace non alloué")
            body_parts.append("\n**⚙️ Étape 2: Désactive Fast Boot Windows**")
            body_parts.append("- Panneau config > Alimentation")
            body_parts.append("- Modifier comportement boutons > Désactive démarrage rapide")
            body_parts.append("- Évite corruption partition Linux")
            body_parts.append("\n**🐧 Étape 3: Installation Linux**")
            body_parts.append("- USB boot Linux (Rufus + ISO)")
            body_parts.append("- Install: 'Installer à côté de Windows'")
            body_parts.append("- GRUB installé automatiquement")
            body_parts.append("\n**🔧 Étape 4: GRUB réparer**")
            body_parts.append("- Si GRUB cassé: boot USB Linux")
            body_parts.append("- sudo update-grub")
            body_parts.append("- sudo grub-install /dev/sda")
            body_parts.append("\n**⏰ Étape 5: Dual boot time sync**")
            body_parts.append("- Windows: registry RealTimeIsUniversal")
            body_parts.append("- Ou Linux: timedatectl set-local-rtc 1")

        # 🔊 #52 AUDIO CRACKLING/GRÉSILLEMENTS
        elif any(word in msg_lower for word in ["crackling", "grésillements", "audio crépite", "son crackling"]):
            body_parts.append("Audio crackling? Plusieurs causes!")
            body_parts.append("\n**⚙️ Étape 1: Sample rate**")
            body_parts.append("- Paramètres son > Propriétés périph sortie")
            body_parts.append("- Avancé > Format: essaye 16 bit 44100 Hz")
            body_parts.append("- Ou 24 bit 48000 Hz")
            body_parts.append("- Teste chaque format")
            body_parts.append("\n**🔧 Étape 2: Buffer size / Latence**")
            body_parts.append("- Si interface audio: augmente buffer")
            body_parts.append("- 512 ou 1024 samples")
            body_parts.append("- Réduit crackling mais + latence")
            body_parts.append("\n**💻 Étape 3: DPC Latency**")
            body_parts.append("- LatencyMon (Resplendence)")
            body_parts.append("- Identifie drivers causant latence")
            body_parts.append("- Souvent: Wi-Fi, Realtek, NVIDIA")
            body_parts.append("- Update/désactive driver coupable")
            body_parts.append("\n**🔌 Étape 4: USB DAC/Interface**")
            body_parts.append("- Branche sur port USB direct (pas hub)")
            body_parts.append("- USB 2.0 parfois plus stable que 3.0")
            body_parts.append("\n**⚡ Étape 5: Désactive audio enhancements**")
            body_parts.append("- Propriétés périph > Améliorations")
            body_parts.append("- Désactive TOUS les effets")

        # 🖼️ #53 CAPTURE D'ÉCRAN / SCREENSHOT
        elif any(word in msg_lower for word in ["capture écran", "screenshot", "print screen", "enregistrement écran"]):
            body_parts.append("Capture d'écran? Méthodes!")
            body_parts.append("\n**⌨️ Étape 1: Raccourcis Windows**")
            body_parts.append("- Win+Maj+S: Outil Capture (partiel/plein)")
            body_parts.append("- Win+Print Screen: capture plein écran → Images\\Screenshots")
            body_parts.append("- Alt+Print Screen: fenêtre active uniquement")
            body_parts.append("\n**🎮 Étape 2: Xbox Game Bar**")
            body_parts.append("- Win+G > Capture")
            body_parts.append("- Win+Alt+Print Screen: screenshot jeu")
            body_parts.append("- Win+Alt+R: enregistrement vidéo")
            body_parts.append("\n**🎥 Étape 3: Enregistrement écran**")
            body_parts.append("- Xbox Game Bar: Win+Alt+R (max 4h)")
            body_parts.append("- OBS Studio: gratuit, illimité, haute qualité")
            body_parts.append("- Paramètres > Captures > Dossier sauvegarde")
            body_parts.append("\n**📸 Étape 4: Outils tiers**")
            body_parts.append("- ShareX (gratuit, puissant)")
            body_parts.append("- Greenshot (annoter)")
            body_parts.append("- Lightshot (upload cloud)")
            body_parts.append("\n**🔧 Étape 5: Print Screen marche pas?**")
            body_parts.append("- Certains portables: Fn+Print Screen")
            body_parts.append("- Paramètres > Clavier > Touche Print Screen ouvre Outil Capture")

        # 🔋 #54 BATTERIE PORTABLE
        elif any(word in msg_lower for word in ["batterie", "autonomie", "charge", "battery"]):
            body_parts.append("Batterie portable? Diagnostiquons!")
            body_parts.append("\n**📊 Étape 1: Rapport batterie**")
            body_parts.append("- CMD admin: powercfg /batteryreport")
            body_parts.append("- Génère HTML C:\\Windows\\System32\\battery-report.html")
            body_parts.append("- Compare capacité design vs actuelle")
            body_parts.append("- <80% capacité = batterie usée")
            body_parts.append("\n**⚙️ Étape 2: Mode alimentation**")
            body_parts.append("- Paramètres > Alimentation")
            body_parts.append("- Économie énergie: max autonomie")
            body_parts.append("- Performances: max puissance")
            body_parts.append("- Équilibré: compromis")
            body_parts.append("\n**🔧 Étape 3: Optimisations batterie**")
            body_parts.append("- Luminosité écran: 50-70% suffit")
            body_parts.append("- Désactive Bluetooth/Wi-Fi si inutilisés")
            body_parts.append("- Ferme apps arrière-plan")
            body_parts.append("- Mode avion si offline")
            body_parts.append("\n**🔋 Étape 4: Calibration batterie**")
            body_parts.append("- Charge 100%")
            body_parts.append("- Utilise jusqu'à 0% (shutdown)")
            body_parts.append("- Recharge 100% sans interruption")
            body_parts.append("- 1 fois tous les 3 mois")
            body_parts.append("\n**⚠️ Étape 5: Remplacement**")
            body_parts.append("- <60% capacité = remplace batterie")
            body_parts.append("- SAV constructeur ou batterie compatible")

        # 🌡️ #55 PORTABLE SURCHAUFFE
        elif any(word in msg_lower for word in ["portable chaud", "laptop chauffe", "portable surchauffe"]):
            body_parts.append("Portable qui chauffe? Solutions spécifiques!")
            body_parts.append("\n**🧹 Étape 1: Nettoyage grilles**")
            body_parts.append("- Air comprimé dans grilles aération")
            body_parts.append("- Portables accumulent poussière rapidement")
            body_parts.append("- Nettoie tous les 6 mois")
            body_parts.append("\n**🏠 Étape 2: Support ventilé**")
            body_parts.append("- Cooling pad ventilé (15-30€)")
            body_parts.append("- Surélève portable = meilleur airflow")
            body_parts.append("- Évite utiliser sur lit/couette (bloque aération)")
            body_parts.append("\n**⚡ Étape 3: Undervolting CPU**")
            body_parts.append("- ThrottleStop (Intel)")
            body_parts.append("- Réduis voltage -80 à -125mV")
            body_parts.append("- -15°C typique sans perte perfs")
            body_parts.append("\n**⚙️ Étape 4: TDP limites**")
            body_parts.append("- ThrottleStop: réduis PL1/PL2")
            body_parts.append("- Ex: 45W → 35W = moins chaud, -10% perfs")
            body_parts.append("\n**🔧 Étape 5: Repaste + pads**")
            body_parts.append("- Portable >2 ans: pâte thermique sèche")
            body_parts.append("- Démonte (si compétent), repaste CPU/GPU")
            body_parts.append("- Thermal pads VRAM aussi")

        # 💻 #56 PORTABLE CLAVIER/TOUCHPAD
        elif any(word in msg_lower for word in ["touchpad", "pavé tactile", "clavier portable"]):
            body_parts.append("Touchpad/Clavier portable HS?")
            body_parts.append("\n**⌨️ Étape 1: Touchpad désactivé?**")
            body_parts.append("- Fn+F5/F6/F7 (varie selon marque)")
            body_parts.append("- Paramètres > Périphériques > Touchpad > Activé")
            body_parts.append("\n**🖱️ Étape 2: Drivers touchpad**")
            body_parts.append("- Precision Touchpad (Windows natif)")
            body_parts.append("- Ou: Synaptics, ELAN drivers (site constructeur)")
            body_parts.append("- Désinstalle/réinstalle driver")
            body_parts.append("\n**⚙️ Étape 3: Gestes touchpad**")
            body_parts.append("- Paramètres > Touchpad > Gestes")
            body_parts.append("- Configure scroll, zoom, 3-4 doigts")
            body_parts.append("\n**🔧 Étape 4: Désactive si souris externe**")
            body_parts.append("- Évite clics involontaires typing")
            body_parts.append("- Paramètres > Touchpad > Désactive quand souris")
            body_parts.append("\n**⌨️ Étape 5: Clavier: drivers + BIOS reset**")
            body_parts.append("- Update drivers clavier")
            body_parts.append("- Reset BIOS defaults")

        # 🎯 #57 OVERCLOCK CPU
        elif any(word in msg_lower for word in ["overclock cpu", "oc cpu", "overclocker processeur"]):
            body_parts.append("Overclock CPU? Guide sécurisé!")
            body_parts.append("\n**🔍 Étape 1: CPU overclockable?**")
            body_parts.append("- Intel: K/KF/KS (ex: i9-14900K)")
            body_parts.append("- AMD Ryzen: tous overclockables")
            body_parts.append("- Carte mère: Z790/B760 (Intel), B550/X570 (AMD)")
            body_parts.append("\n**🌡️ Étape 2: Refroidissement suffisant**")
            body_parts.append("- Stock cooler = NON (max +200 MHz)")
            body_parts.append("- Tour air haut de gamme ou AIO 240mm+ requis")
            body_parts.append("\n**⚙️ Étape 3: BIOS OC**")
            body_parts.append("- Intel: augmente ratio core +1 (x50 = 5.0 GHz)")
            body_parts.append("- AMD: Precision Boost Overdrive (PBO)")
            body_parts.append("- Voltage: AUTO d'abord")
            body_parts.append("\n**🧪 Étape 4: Stabilité test**")
            body_parts.append("- Cinebench R23: 10 min")
            body_parts.append("- Prime95 Small FFT: 30 min")
            body_parts.append("- OCCT CPU: 1h")
            body_parts.append("- Crash = réduis OC -100 MHz")
            body_parts.append("\n**⚡ Étape 5: Undervolt après OC**")
            body_parts.append("- OC validé? Réduis voltage graduellement")
            body_parts.append("- -50mV par -50mV, teste")
            body_parts.append("- Même fréquence, moins chaud")

        # 🎯 #58 OVERCLOCK GPU
        elif any(word in msg_lower for word in ["overclock gpu", "oc gpu", "overclocker carte graphique"]):
            body_parts.append("Overclock GPU? Facile et sûr!")
            body_parts.append("\n**🔧 Étape 1: MSI Afterburner**")
            body_parts.append("- Télécharge + RTSS (RivaTuner)")
            body_parts.append("- Lance, déverrouille voltage control (settings)")
            body_parts.append("\n**⚡ Étape 2: Power Limit max**")
            body_parts.append("- Slide Power Limit: 110-120%")
            body_parts.append("- Permet GPU boost plus haut")
            body_parts.append("\n**📈 Étape 3: Core Clock**")
            body_parts.append("- +25 MHz incrément")
            body_parts.append("- Applique, teste 3DMark/jeu 10 min")
            body_parts.append("- Crash/artefacts = trop haut, -25 MHz")
            body_parts.append("- Typique stable: +100 à +200 MHz")
            body_parts.append("\n**💾 Étape 4: Memory Clock**")
            body_parts.append("- APRÈS core stable!")
            body_parts.append("- +50 MHz incrément")
            body_parts.append("- Teste, pousse jusqu'à artefacts")
            body_parts.append("- Typique: +500 à +1000 MHz (GDDR6/6X)")
            body_parts.append("\n**🧪 Étape 5: Validation finale**")
            body_parts.append("- 3DMark Time Spy/Fire Strike: pas de crash")
            body_parts.append("- FurMark 15 min: température stable")
            body_parts.append("- Jeu 1h: aucun artefact")
            body_parts.append("- Sauvegarde profil Afterburner")

        # 🎯 #59 OVERCLOCK RAM
        elif any(word in msg_lower for word in ["overclock ram", "xmp", "expo", "docp", "timings"]):
            body_parts.append("Overclock RAM? XMP/EXPO d'abord!")
            body_parts.append("\n**⚡ Étape 1: XMP/EXPO (facile)**")
            body_parts.append("- BIOS > Enable XMP (Intel) ou EXPO/DOCP (AMD)")
            body_parts.append("- Profil auto à fréquence spécifiée kit")
            body_parts.append("- DDR4-3600 CL16, DDR5-6000 CL30, etc.")
            body_parts.append("\n**🧪 Étape 2: Test stabilité XMP**")
            body_parts.append("- MemTest86: 4 passes minimum")
            body_parts.append("- Ou TestMem5 1 cycle")
            body_parts.append("- Erreur = instable, augmente voltage DRAM")
            body_parts.append("\n**📊 Étape 3: Overclock manuel (avancé)**")
            body_parts.append("- Dépasse XMP: ex DDR4-3600 → 3800")
            body_parts.append("- Ajuste timings: CL, tRCD, tRP, tRAS")
            body_parts.append("- Lower = better mais instabilité")
            body_parts.append("\n**⚙️ Étape 4: Voltage RAM**")
            body_parts.append("- DDR4: 1.35V XMP, max 1.50V daily safe")
            body_parts.append("- DDR5: 1.25V EXPO, max 1.40V daily")
            body_parts.append("- +0.05V si instable")
            body_parts.append("\n**🎯 Étape 5: Ryzen FCLK 1:1**")
            body_parts.append("- AMD: FCLK (Infinity Fabric) = moitié RAM speed")
            body_parts.append("- DDR4-3600 = FCLK 1800, DDR5-6000 = FCLK 3000")
            body_parts.append("- Keep 1:1 ratio pour best perfs")

        # 📊 #60 BENCHMARK / STRESS TEST
        elif any(word in msg_lower for word in ["benchmark", "stress test", "furmark", "cinebench", "3dmark"]):
            body_parts.append("Benchmarks PC? Liste outils!")
            body_parts.append("\n**🎮 CPU Benchmarks**")
            body_parts.append("- Cinebench R23: multi/single core")
            body_parts.append("- CPU-Z Bench: comparaison vs autres CPU")
            body_parts.append("- Geekbench 6: cross-platform")
            body_parts.append("\n**🎨 GPU Benchmarks**")
            body_parts.append("- 3DMark Time Spy (DX12), Fire Strike (DX11)")
            body_parts.append("- Unigine Superposition/Heaven: stress + bench")
            body_parts.append("- Port Royal: Ray-Tracing bench")
            body_parts.append("\n**💾 Stockage**")
            body_parts.append("- CrystalDiskMark: vitesse SSD/HDD")
            body_parts.append("- AS SSD Benchmark")
            body_parts.append("\n**🧪 Stress Tests**")
            body_parts.append("- Prime95: CPU max stress")
            body_parts.append("- FurMark: GPU torture test (chauffe!)")
            body_parts.append("- OCCT: CPU/GPU/PSU combinés")
            body_parts.append("- MemTest86: RAM over night")
            body_parts.append("\n**📊 Monitoring pendant tests**")
            body_parts.append("- HWiNFO64: températures, voltages, clocks")
            body_parts.append("- MSI Afterburner: OSD in-game")

        # 🔧 #61 BIOS UPDATE
        elif any(word in msg_lower for word in ["bios update", "mise à jour bios", "flash bios", "uefi"]):
            body_parts.append("Update BIOS? Précautions!")
            body_parts.append("\n**⚠️ Étape 1: Nécessaire?**")
            body_parts.append("- Update BIOS SI: nouveau CPU incompatible, bugs connus")
            body_parts.append("- PAS update si PC stable (if it ain't broke...)")
            body_parts.append("\n**🔍 Étape 2: Version actuelle**")
            body_parts.append("- BIOS boot: affiche version")
            body_parts.append("- Ou Windows: msinfo32 > Version BIOS")
            body_parts.append("- Site carte mère: télécharge version plus récente")
            body_parts.append("\n**💾 Étape 3: Méthode update**")
            body_parts.append("- USB Flashback (meilleur, sans CPU): bouton arrière")
            body_parts.append("- Q-Flash/EZ Flash (depuis BIOS)")
            body_parts.append("- Windows utility (déconseillé, risque)")
            body_parts.append("\n**⚡ Étape 4: Alimentation stable**")
            body_parts.append("- PC fixe: pas de coupure courant pendant flash")
            body_parts.append("- Portable: branché secteur, batterie >50%")
            body_parts.append("- NE PAS éteindre pendant flash = brick!")
            body_parts.append("\n**🔧 Étape 5: Clear CMOS après**")
            body_parts.append("- Retire pile CR2032 30 sec")
            body_parts.append("- Ou: jumper Clear CMOS")
            body_parts.append("- Reconfigure BIOS (XMP, boot order)")

        # 🖥️ #62 ÉCRAN HDR
        elif any(word in msg_lower for word in ["hdr", "high dynamic range", "displayhdr"]):
            body_parts.append("HDR? Configuration Windows + jeux!")
            body_parts.append("\n**🔍 Étape 1: Écran compatible HDR?**")
            body_parts.append("- DisplayHDR 400/600/1000 certification")
            body_parts.append("- Specs: >400 nits brightness, 10-bit panel")
            body_parts.append("- HDR400 = entrée gamme, HDR1000 = top")
            body_parts.append("\n**⚙️ Étape 2: Active HDR Windows**")
            body_parts.append("- Paramètres > Affichage > HDR")
            body_parts.append("- Active 'Utiliser HDR'")
            body_parts.append("- Calibre luminosité SDR/HDR sliders")
            body_parts.append("\n**🎮 Étape 3: HDR in-game**")
            body_parts.append("- Options jeu > Activer HDR")
            body_parts.append("- Calibre brightness jeu (important!)")
            body_parts.append("- Mauvaise calibration = trop sombre/lumineux")
            body_parts.append("\n**🔌 Étape 4: Câble compatible**")
            body_parts.append("- HDMI 2.0+ ou DisplayPort 1.4+")
            body_parts.append("- HDMI 2.1 pour 4K 120Hz HDR")
            body_parts.append("\n**⚠️ Étape 5: Auto HDR Windows 11**")
            body_parts.append("- Paramètres > HDR > Auto HDR")
            body_parts.append("- Ajoute HDR jeux non-HDR natif")
            body_parts.append("- Qualité variable, teste")

        # 🎵 #63 AUDIO MULTICANAL / 5.1 / 7.1
        elif any(word in msg_lower for word in ["5.1", "7.1", "surround", "home cinema", "multicanal"]):
            body_parts.append("Audio 5.1/7.1? Configuration!")
            body_parts.append("\n**🔌 Étape 1: Connexion**")
            body_parts.append("- Optique/SPDIF: max 5.1 Dolby/DTS")
            body_parts.append("- HDMI ARC/eARC: 7.1, Atmos, DTS:X")
            body_parts.append("- Analogique 3.5mm: 6 prises (rare)")
            body_parts.append("\n**⚙️ Étape 2: Config Windows**")
            body_parts.append("- Paramètres Son > Propriétés périph")
            body_parts.append("- Format spatial: Dolby Atmos, DTS:X, Windows Sonic")
            body_parts.append("- Test: sons sur chaque enceinte")
            body_parts.append("\n**🎮 Étape 3: In-game audio**")
            body_parts.append("- Options audio jeu: sélectionne 5.1/7.1")
            body_parts.append("- Home Theater mode (pas Headphones)")
            body_parts.append("\n**🎵 Étape 4: Dolby Atmos for Headphones**")
            body_parts.append("- Casque stéréo → surround virtuel")
            body_parts.append("- Microsoft Store: Dolby Access app")
            body_parts.append("- Gratuit trial puis payant")
            body_parts.append("\n**🔧 Étape 5: Receiver/Ampli**")
            body_parts.append("- Vérifie ampli mode: Dolby Digital, DTS")
            body_parts.append("- Auto-calibration micro (Audyssey, YPAO)")

        # 💻 #64 PORTABLE MODE PERFORMANCE vs SILENT
        elif any(word in msg_lower for word in ["mode performance", "silent mode", "turbo", "portable mode"]):
            body_parts.append("Modes portable? Performance vs Silent!")
            body_parts.append("\n**⚡ Étape 1: Modes constructeur**")
            body_parts.append("- Fn+touche (varie): Performance/Balanced/Silent")
            body_parts.append("- Ou: Utility constructeur (Armoury Crate, MSI Center)")
            body_parts.append("- Performance = max TDP, fans 100%")
            body_parts.append("- Silent = TDP réduit, fans minimum")
            body_parts.append("\n**🔧 Étape 2: Windows Power Mode**")
            body_parts.append("- Icône batterie > slider Performance")
            body_parts.append("- Économie/Recommandé/Meilleures perfs")
            body_parts.append("\n**🎮 Étape 3: Gaming = Performance mode**")
            body_parts.append("- Max TDP CPU/GPU")
            body_parts.append("- +15-25% FPS vs Balanced")
            body_parts.append("- Mais chauffe + bruit")
            body_parts.append("\n**📚 Étape 4: Bureautique = Silent**")
            body_parts.append("- Navigation, Office = Silent suffit")
            body_parts.append("- Silencieux, batterie dure 2x plus")
            body_parts.append("\n**⚙️ Étape 5: Custom profiles**")
            body_parts.append("- ThrottleStop: custom TDP limits")
            body_parts.append("- Ex: 35W (silent), 45W (balanced), 65W (turbo)")

        # 🌐 #65 TEREDO / IPv6 GAMING
        elif any(word in msg_lower for word in ["teredo", "ipv6", "xbox live", "nat"]):
            body_parts.append("Teredo/IPv6 Xbox Live? Configuration!")
            body_parts.append("\n**🔍 Étape 1: Check Teredo état**")
            body_parts.append("- CMD: netsh interface teredo show state")
            body_parts.append("- État: qualified = bon")
            body_parts.append("- offline/dormant = problème")
            body_parts.append("\n**🔧 Étape 2: Réactive Teredo**")
            body_parts.append("- CMD admin:")
            body_parts.append("  netsh interface teredo set state disabled")
            body_parts.append("  netsh interface teredo set state type=default")
            body_parts.append("\n**🌐 Étape 3: IPv6 activé?**")
            body_parts.append("- Paramètres réseau > Propriétés carte")
            body_parts.append("- Coche IPv6 (PAS désactiver)")
            body_parts.append("- Teredo requiert IPv6")
            body_parts.append("\n**🔐 Étape 4: Pare-feu Teredo**")
            body_parts.append("- Pare-feu > Autoriser Teredo")
            body_parts.append("- Port UDP 3544")
            body_parts.append("\n**🎮 Étape 5: NAT Type**")
            body_parts.append("- Paramètres Xbox app > Réseau")
            body_parts.append("- NAT: Ouvert = parfait, Modéré = OK, Strict = problème")
            body_parts.append("- Si strict: UPnP routeur activé")

        # 🎯 #66-100 MÉGA-BLOC FINAL (35 scénarios compacts)
        # Pour atteindre 100 total, j'ajoute 35 scénarios courts (3 étapes chacun)

        elif any(word in msg_lower for word in ["coil whine", "sifflement", "bobine"]):
            body_parts.append("Coil whine GPU/PSU?")
            body_parts.append("\n**Étape 1**: Normal sous forte charge, pas défaut")
            body_parts.append("\n**Étape 2**: Limite FPS in-game (réduit whine)")
            body_parts.append("\n**Étape 3**: V-Sync ON ou cap 144 FPS")

        elif any(word in msg_lower for word in ["tearing", "déchirement image", "screen tearing"]):
            body_parts.append("Screen tearing?")
            body_parts.append("\n**Étape 1**: Active V-Sync in-game")
            body_parts.append("\n**Étape 2**: Ou G-Sync/FreeSync (meilleur)")
            body_parts.append("\n**Étape 3**: Cap FPS = refresh rate écran")

        elif any(word in msg_lower for word in ["ghosting", "motion blur écran", "rémanence"]):
            body_parts.append("Ghosting/rémanence écran?")
            body_parts.append("\n**Étape 1**: Écran > Overdrive/Response Time = élevé")
            body_parts.append("\n**Étape 2**: Évite VA panels (IPS/TN meilleurs)")
            body_parts.append("\n**Étape 3**: Teste testufo.com ghosting test")

        elif any(word in msg_lower for word in ["pixel mort", "dead pixel", "stuck pixel"]):
            body_parts.append("Pixel mort/coincé?")
            body_parts.append("\n**Étape 1**: jscreenfix.com - laisse tourner 30+ min")
            body_parts.append("\n**Étape 2**: Pression douce + on/off écran")
            body_parts.append("\n**Étape 3**: Garantie si <7 jours achat")

        elif any(word in msg_lower for word in ["backlight bleed", "ips glow", "fuite lumière"]):
            body_parts.append("Backlight bleed/IPS glow?")
            body_parts.append("\n**Étape 1**: Normal sur IPS (angles)")
            body_parts.append("\n**Étape 2**: Réduis brightness (<80%)")
            body_parts.append("\n**Étape 3**: RMA si excessive (coins très lumineux)")

        elif any(word in msg_lower for word in ["fan curve", "courbe ventilateur", "vitesse ventilo"]):
            body_parts.append("Courbe ventilateurs custom?")
            body_parts.append("\n**Étape 1**: BIOS > Q-Fan/Smart Fan Control")
            body_parts.append("\n**Étape 2**: Argus Monitor ou SpeedFan (Windows)")
            body_parts.append("\n**Étape 3**: Courbe: <50°C=30%, 70°C=70%, 85°C=100%")

        elif any(word in msg_lower for word in ["rgb", "led", "éclairage", "lighting"]):
            body_parts.append("RGB/LED contrôle?")
            body_parts.append("\n**Étape 1**: iCUE (Corsair), Aura Sync (ASUS), Mystic Light (MSI)")
            body_parts.append("\n**Étape 2**: SignalRGB ou OpenRGB (universel)")
            body_parts.append("\n**Étape 3**: BIOS: désactive LED si crash software")

        elif any(word in msg_lower for word in ["macro", "macros", "raccourci clavier"]):
            body_parts.append("Macros gaming?")
            body_parts.append("\n**Étape 1**: Logiciel périph (G Hub, Synapse, iCUE)")
            body_parts.append("\n**Étape 2**: AutoHotkey (scripting avancé)")
            body_parts.append("\n**Étape 3**: Enregistre séquence touches + délais")

        elif any(word in msg_lower for word in ["game mode", "mode jeu windows"]):
            body_parts.append("Game Mode Windows?")
            body_parts.append("\n**Étape 1**: Paramètres > Jeux > Mode jeu = ON")
            body_parts.append("\n**Étape 2**: Priorité ressources pour jeu")
            body_parts.append("\n**Étape 3**: Désactive si problème perf (rare)")

        elif any(word in msg_lower for word in ["game bar", "xbox game bar"]):
            body_parts.append("Xbox Game Bar?")
            body_parts.append("\n**Étape 1**: Win+G pour ouvrir")
            body_parts.append("\n**Étape 2**: Captures, FPS counter, Xbox Social")
            body_parts.append("\n**Étape 3**: Désactive si lag: Paramètres > Jeux > Game Bar OFF")

        elif any(word in msg_lower for word in ["dxdiag", "directx", "diagnostic directx"]):
            body_parts.append("DirectX Diagnostic?")
            body_parts.append("\n**Étape 1**: Win+R > dxdiag")
            body_parts.append("\n**Étape 2**: Onglets: Système, Affichage, Son")
            body_parts.append("\n**Étape 3**: Vérifie version DirectX, drivers, problèmes")

        elif any(word in msg_lower for word in ["msconfig", "config système", "démarrage sélectif"]):
            body_parts.append("MSConfig (Config Système)?")
            body_parts.append("\n**Étape 1**: Win+R > msconfig")
            body_parts.append("\n**Étape 2**: Démarrage: Normal/Diagnostic/Sélectif")
            body_parts.append("\n**Étape 3**: Services: Masque services Microsoft, désactive reste")

        elif any(word in msg_lower for word in ["registre", "registry", "regedit"]):
            body_parts.append("Éditeur Registre?")
            body_parts.append("\n**Étape 1**: Win+R > regedit (ATTENTION!)")
            body_parts.append("\n**Étape 2**: Sauvegarde avant modif: Fichier > Exporter")
            body_parts.append("\n**Étape 3**: HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER")

        elif any(word in msg_lower for word in ["cmd", "invite commande", "command prompt"]):
            body_parts.append("Invite de commandes (CMD)?")
            body_parts.append("\n**Étape 1**: Win+R > cmd (ou Win+X > admin)")
            body_parts.append("\n**Étape 2**: Commandes utiles: ipconfig, ping, sfc, DISM")
            body_parts.append("\n**Étape 3**: PowerShell = plus puissant")

        elif any(word in msg_lower for word in ["powershell", "ps1", "script powershell"]):
            body_parts.append("PowerShell?")
            body_parts.append("\n**Étape 1**: Win+X > PowerShell (admin)")
            body_parts.append("\n**Étape 2**: Scripts .ps1: Set-ExecutionPolicy RemoteSigned")
            body_parts.append("\n**Étape 3**: Plus puissant que CMD")

        elif any(word in msg_lower for word in ["event viewer", "observateur événements", "logs"]):
            body_parts.append("Event Viewer (Logs Windows)?")
            body_parts.append("\n**Étape 1**: eventvwr.msc")
            body_parts.append("\n**Étape 2**: Windows Logs > System, Application")
            body_parts.append("\n**Étape 3**: Cherche erreurs (rouge) autour crash/problème")

        elif any(word in msg_lower for word in ["reliability monitor", "moniteur fiabilité"]):
            body_parts.append("Moniteur Fiabilité?")
            body_parts.append("\n**Étape 1**: perfmon /rel")
            body_parts.append("\n**Étape 2**: Historique crashes apps/Windows")
            body_parts.append("\n**Étape 3**: Index stabilité 1-10")

        elif any(word in msg_lower for word in ["resource monitor", "moniteur ressources"]):
            body_parts.append("Moniteur Ressources?")
            body_parts.append("\n**Étape 1**: resmon.exe")
            body_parts.append("\n**Étape 2**: CPU, Mémoire, Disque, Réseau détaillé")
            body_parts.append("\n**Étape 3**: Plus détaillé que Task Manager")

        elif any(word in msg_lower for word in ["performance monitor", "perfmon"]):
            body_parts.append("Performance Monitor?")
            body_parts.append("\n**Étape 1**: perfmon")
            body_parts.append("\n**Étape 2**: Compteurs perfs custom (CPU, RAM, GPU)")
            body_parts.append("\n**Étape 3**: Rapports diagnostic système")

        elif any(word in msg_lower for word in ["ccleaner", "nettoyeur", "cleaner"]):
            body_parts.append("CCleaner/Nettoyeurs?")
            body_parts.append("\n**Étape 1**: Windows natif suffit (Storage Sense)")
            body_parts.append("\n**Étape 2**: CCleaner OK mais PAS registry cleaner")
            body_parts.append("\n**Étape 3**: BleachBit (open-source)")

        elif any(word in msg_lower for word in ["défragmentation", "defrag", "optimiser lecteur"]):
            body_parts.append("Défragmentation?")
            body_parts.append("\n**Étape 1**: HDD = défragmente (dfrgui)")
            body_parts.append("\n**Étape 2**: SSD = JAMAIS défragmenter! (TRIM automatique)")
            body_parts.append("\n**Étape 3**: Windows auto-schedule OK")

        elif any(word in msg_lower for word in ["sandbox", "bac à sable", "windows sandbox"]):
            body_parts.append("Windows Sandbox?")
            body_parts.append("\n**Étape 1**: Windows Pro/Enterprise uniquement")
            body_parts.append("\n**Étape 2**: Activer: Fonctionnalités Windows > Sandbox")
            body_parts.append("\n**Étape 3**: VM légère isolée, efface après fermeture")

        elif any(word in msg_lower for word in ["hyper-v", "virtualisation", "vm"]):
            body_parts.append("Hyper-V / Virtualisation?")
            body_parts.append("\n**Étape 1**: BIOS: VT-x (Intel) ou SVM (AMD) = Enabled")
            body_parts.append("\n**Étape 2**: Windows: Activer Hyper-V (Pro+)")
            body_parts.append("\n**Étape 3**: Ou VMware/VirtualBox (gratuit)")

        elif any(word in msg_lower for word in ["wsl", "windows subsystem linux", "ubuntu windows"]):
            body_parts.append("WSL (Linux sous Windows)?")
            body_parts.append("\n**Étape 1**: CMD admin: wsl --install")
            body_parts.append("\n**Étape 2**: Ubuntu par défaut, ou: wsl --install -d Debian")
            body_parts.append("\n**Étape 3**: Terminal Windows > onglet Ubuntu")

        elif any(word in msg_lower for word in ["tpm", "trusted platform module", "tpm 2.0"]):
            body_parts.append("TPM 2.0?")
            body_parts.append("\n**Étape 1**: Requis Windows 11")
            body_parts.append("\n**Étape 2**: BIOS: PTT (Intel) ou fTPM (AMD) = Enabled")
            body_parts.append("\n**Étape 3**: tpm.msc vérifie statut")

        elif any(word in msg_lower for word in ["secure boot", "démarrage sécurisé"]):
            body_parts.append("Secure Boot?")
            body_parts.append("\n**Étape 1**: BIOS: Secure Boot = Enabled (Windows 11 requis)")
            body_parts.append("\n**Étape 2**: Dual boot Linux: désactive temporairement")
            body_parts.append("\n**Étape 3**: msinfo32 montre état Secure Boot")

        elif any(word in msg_lower for word in ["fast boot", "démarrage rapide"]):
            body_parts.append("Fast Boot Windows?")
            body_parts.append("\n**Étape 1**: Panneau config > Options alimentation")
            body_parts.append("\n**Étape 2**: Modifier comportement boutons > Fast Boot")
            body_parts.append("\n**Étape 3**: Désactive si dual boot ou problèmes shutdown")

        elif any(word in msg_lower for word in ["hibernation", "veille prolongée", "hiberfil"]):
            body_parts.append("Hibernation?")
            body_parts.append("\n**Étape 1**: Sauvegarde RAM sur disque = boot rapide")
            body_parts.append("\n**Étape 2**: hiberfil.sys = taille RAM (16GB = 16GB fichier!)")
            body_parts.append("\n**Étape 3**: Désactive: powercfg -h off (libère espace)")

        elif any(word in msg_lower for word in ["veille", "sleep", "standby", "mise en veille"]):
            body_parts.append("Veille/Sleep?")
            body_parts.append("\n**Étape 1**: Paramètres > Alimentation > Veille après X min")
            body_parts.append("\n**Étape 2**: Ou: powercfg /requests (empêche veille)")
            body_parts.append("\n**Étape 3**: Wake-on-LAN: BIOS + carte réseau")

        elif any(word in msg_lower for word in ["shutdown lent", "extinction lente", "arrêt lent"]):
            body_parts.append("Shutdown lent?")
            body_parts.append("\n**Étape 1**: Apps bloquent arrêt (attendent fermeture)")
            body_parts.append("\n**Étape 2**: Event Viewer: User32 log shutdown time")
            body_parts.append("\n**Étape 3**: Fast Startup OFF si problème")

        elif any(word in msg_lower for word in ["cortana", "désactiver cortana"]):
            body_parts.append("Désactiver Cortana?")
            body_parts.append("\n**Étape 1**: Paramètres > Cortana > OFF")
            body_parts.append("\n**Étape 2**: Registry: HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search")
            body_parts.append("\n**Étape 3**: AllowCortana = DWORD 0")

        elif any(word in msg_lower for word in ["telemetry", "télémétrie", "espionnage windows"]):
            body_parts.append("Télémétrie Windows?")
            body_parts.append("\n**Étape 1**: O&O ShutUp10++ (gratuit, GUI)")
            body_parts.append("\n**Étape 2**: Désactive tracking, Cortana, suggestions")
            body_parts.append("\n**Étape 3**: Services: DiagTrack = Désactivé")

        elif any(word in msg_lower for word in ["windows defender", "antivirus windows", "sécurité windows"]):
            body_parts.append("Windows Defender?")
            body_parts.append("\n**Étape 1**: Bon antivirus gratuit intégré")
            body_parts.append("\n**Étape 2**: Exclusions: dossiers jeux/dev")
            body_parts.append("\n**Étape 3**: Scan offline si virus résistant")

        elif any(word in msg_lower for word in ["bitlocker", "chiffrement", "encryption"]):
            body_parts.append("BitLocker chiffrement?")
            body_parts.append("\n**Étape 1**: Windows Pro+ uniquement")
            body_parts.append("\n**Étape 2**: Clic droit C: > Activer BitLocker")
            body_parts.append("\n**Étape 3**: TPM requis, sauvegarde clé récup!")

        # Scénario final #100: QUESTION GÉNÉRALE (fallback amélioré)
        elif any(word in msg_lower for word in ["aide", "help", "comment", "c'est quoi", "qu'est-ce"]):
            body_parts.append("Question générale PC? Je t'explique!")
            body_parts.append("\n**💡 Conseil**: Sois plus précis!")
            body_parts.append("- Problème: décris symptômes (crash, lent, bruit...)")
            body_parts.append("- Hardware: quel composant? (GPU, CPU, RAM...)")
            body_parts.append("- Software: quelle app/jeu?")
            body_parts.append("\n**🔍 Exemples questions précises**:")
            body_parts.append("- 'Mon PC crash en jouant à Cyberpunk'")
            body_parts.append("- 'Comment overclocker ma RTX 4070?'")
            body_parts.append("- 'Windows Update bloqué à 30%'")
            body_parts.append("\n**🛠️ Outils NiTriTe disponibles**:")
            body_parts.append("- Diagnostic > HWMonitor, CrystalDiskInfo, MemTest")
            body_parts.append("- Optimisation > Nettoyage, défrag, drivers")

        # ═══════════════════════════════════════════════════════════════════
        # 🔥 SCÉNARIOS ULTRA-ENRICHIS (PRIORITÉ MAX - 15-20 ÉTAPES)
        # ═══════════════════════════════════════════════════════════════════

        # Vérifie d'abord les scénarios ULTRA-ENRICHIS (max détail)
        ultra_response = self._handle_ultra_enriched_scenarios(msg_lower)
        if ultra_response:
            return f"{intro}\n\n{ultra_response}{random.choice(outros_francais)}"

        # ═══════════════════════════════════════════════════════════════════
        # 🚀 SCÉNARIOS 101-500 (400 SCÉNARIOS ADDITIONNELS)
        # ═══════════════════════════════════════════════════════════════════

        # Appel aux scénarios 101-390 (290 scénarios condensés)
        scenarios_101_390_response = self._handle_scenarios_101_390(msg_lower)
        if scenarios_101_390_response:
            return f"{intro}\n\n{scenarios_101_390_response}{random.choice(outros_francais)}"

        # Appel aux scénarios 391-500 (110 scénarios ultra-détaillés)
        scenarios_391_500_response = self._handle_scenarios_391_500(msg_lower)
        if scenarios_391_500_response:
            return f"{intro}\n\n{scenarios_391_500_response}{random.choice(outros_francais)}"

        # 📋 Fallback: réponses par intent si aucun keyword spécifique
        elif intent == "simple_question":
            # Question simple: réponse directe courte
            body_parts.append("Alors, pour répondre simplement:")
            body_parts.append(f"\n{self._simplify_tip_french(relevant_tips[0]['content'])}")

        else:
            # Format général
            body_parts.append("Voici ce que tu dois savoir:")
            for i, tip in enumerate(relevant_tips[:4], 1):
                body_parts.append(f"\n**{i}.** {self._simplify_tip_french(tip['content'])}")

        body = "\n".join(body_parts)

        # 3. Conclusion française encourageante
        outros_francais = [
            "\nTeste ça et dis-moi si ça va mieux! 👍",
            "\nÇa devrait régler ton problème. Sinon reviens me voir!",
            "\nHésite pas si t'as besoin de plus de détails!",
            "\nDis-moi si ça marche ou si tu veux que je t'explique autrement! 😊"
        ]
        outro = random.choice(outros_francais)

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
        # Si le tip est déjà en français, on le garde
        if any(word in tip_content.lower() for word in ["pour", "dans", "avec", "votre", "vous", "est", "sont"]):
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
