#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hybrid Knowledge Base Manager - NiTriTe V20.0
Gestionnaire unifié de bases de connaissances multiples
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Import legacy KB pour backward compat
try:
    from .ai_knowledge_unified import UnifiedKnowledgeBase
    LEGACY_KB_AVAILABLE = True
except ImportError:
    try:
        from ai_knowledge_unified import UnifiedKnowledgeBase
        LEGACY_KB_AVAILABLE = True
    except ImportError:
        try:
            from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
            LEGACY_KB_AVAILABLE = True
        except ImportError:
            LEGACY_KB_AVAILABLE = False


class HybridKnowledgeBase:
    """
    Gestionnaire hybride combinant:
    - Core KB (30K+ entrées techniques)
    - NiTriTe Expert KB (documentation app)
    - Legacy KB (5K tips existants)
    - Auto-learned docs (markdown/json scannés)
    """

    def __init__(self, data_dir="data/knowledge"):
        self.data_dir = Path(data_dir)

        # Chemins fichiers
        self.core_kb_path = self.data_dir / "core_kb.json"
        self.nitrite_kb_path = self.data_dir / "nitrite_expert_kb.json"
        self.auto_learned_path = self.data_dir / "auto_learned" / "index.json"

        # Chargement bases
        self.core_kb = self.load_core_kb()
        self.nitrite_kb = self.load_nitrite_kb()
        self.legacy_kb = self.load_legacy_kb()
        self.auto_learned = self.load_auto_learned()

        # Stats
        self.stats = self._compute_stats()

        print(f"[HybridKB] Chargé: {self.stats['total_entries']} entrées totales")
        print(f"  - Core KB: {self.stats['core_entries']} entrées")
        print(f"  - NiTriTe KB: {self.stats['nitrite_entries']} pages")
        print(f"  - Legacy KB: {self.stats['legacy_entries']} tips")
        print(f"  - Auto-learned: {self.stats['learned_entries']} docs")

    def load_core_kb(self) -> Dict:
        """Charge la base technique core (CPU, GPU, RAM, etc.)"""
        if not self.core_kb_path.exists():
            print(f"[HybridKB] WARN: Core KB non trouvé: {self.core_kb_path}")
            return {"entries": [], "stats": {"total_entries": 0}}

        try:
            with open(self.core_kb_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"[HybridKB] Core KB chargé: {len(data.get('entries', []))} entrées")
            return data
        except Exception as e:
            print(f"[HybridKB] ERROR loading Core KB: {e}")
            return {"entries": [], "stats": {"total_entries": 0}}

    def load_nitrite_kb(self) -> Dict:
        """Charge la base NiTriTe Expert (14 pages app)"""
        if not self.nitrite_kb_path.exists():
            print(f"[HybridKB] WARN: NiTriTe KB non trouvé: {self.nitrite_kb_path}")
            return {"pages": {}, "workflows": [], "query_mapping": {}}

        try:
            with open(self.nitrite_kb_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"[HybridKB] NiTriTe KB chargé: {len(data.get('pages', {}))} pages")
            return data
        except Exception as e:
            print(f"[HybridKB] ERROR loading NiTriTe KB: {e}")
            return {"pages": {}, "workflows": [], "query_mapping": {}}

    def load_legacy_kb(self):
        """Charge la base legacy (ai_knowledge_unified.py)"""
        if not LEGACY_KB_AVAILABLE:
            print("[HybridKB] Legacy KB non disponible (ai_knowledge_unified)")
            return None

        try:
            legacy = UnifiedKnowledgeBase()
            print(f"[HybridKB] Legacy KB chargé: {len(legacy.kb)} catégories")
            return legacy
        except Exception as e:
            print(f"[HybridKB] ERROR loading Legacy KB: {e}")
            return None

    def load_auto_learned(self) -> Dict:
        """Charge l'index des docs auto-appris"""
        if not self.auto_learned_path.exists():
            return {"markdown": [], "json": []}

        try:
            with open(self.auto_learned_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"[HybridKB] Auto-learned chargé: {len(data.get('markdown', []))} docs")
            return data
        except Exception as e:
            print(f"[HybridKB] ERROR loading auto-learned: {e}")
            return {"markdown": [], "json": []}

    def _compute_stats(self) -> Dict:
        """Calcule statistiques globales"""
        return {
            'total_entries': (
                len(self.core_kb.get('entries', [])) +
                len(self.nitrite_kb.get('pages', {})) +
                (len(self.legacy_kb.knowledge_base) if self.legacy_kb else 0) +
                len(self.auto_learned.get('markdown', []))
            ),
            'core_entries': len(self.core_kb.get('entries', [])),
            'nitrite_entries': len(self.nitrite_kb.get('pages', {})),
            'legacy_entries': len(self.legacy_kb.knowledge_base) if self.legacy_kb else 0,
            'learned_entries': len(self.auto_learned.get('markdown', []))
        }

    def search(self, query: str, top_k: int = 10, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Recherche hybride avec scoring pondéré

        Args:
            query: Query utilisateur
            top_k: Nombre de résultats à retourner
            filters: Filtres optionnels (difficulty, category, etc.)

        Returns:
            Liste de résultats scorés et triés
        """
        results = []

        # 1. Core KB (poids 40%)
        core_results = self._search_core(query, top_k * 2)
        for res in core_results:
            results.append({
                'source': 'core_kb',
                'weight': 0.4,
                'score': res['score'],
                'content': res
            })

        # 2. NiTriTe KB (poids 35% si keywords NiTriTe détectés)
        if self._is_nitrite_query(query):
            nitrite_results = self._search_nitrite(query, top_k * 2)
            for res in nitrite_results:
                results.append({
                    'source': 'nitrite_kb',
                    'weight': 0.35,
                    'score': res['score'],
                    'content': res
                })
        else:
            # Poids réduit si pas explicitement NiTriTe
            nitrite_results = self._search_nitrite(query, top_k)
            for res in nitrite_results:
                results.append({
                    'source': 'nitrite_kb',
                    'weight': 0.15,
                    'score': res['score'],
                    'content': res
                })

        # 3. Legacy KB (poids 15%)
        if self.legacy_kb:
            legacy_results = self._search_legacy(query, top_k)
            for res in legacy_results:
                results.append({
                    'source': 'legacy_kb',
                    'weight': 0.15,
                    'score': res.get('score', 0.5),
                    'content': res
                })

        # 4. Auto-learned (poids 10%)
        learned_results = self._search_auto_learned(query, top_k)
        for res in learned_results:
            results.append({
                'source': 'auto_learned',
                'weight': 0.1,
                'score': res['score'],
                'content': res
            })

        # 5. Scoring final
        scored_results = self._score_and_rank(results, query, filters)

        return scored_results[:top_k]

    def _search_core(self, query: str, top_k: int) -> List[Dict]:
        """Recherche TF-IDF dans Core KB"""
        entries = self.core_kb.get('entries', [])
        if not entries:
            return []

        # Extraction textes
        texts = [
            f"{e.get('title', '')} {e.get('content', '')} {' '.join(e.get('keywords', []))}"
            for e in entries
        ]

        # TF-IDF
        try:
            vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000, stop_words=None)
            tfidf_matrix = vectorizer.fit_transform(texts)
            query_vec = vectorizer.transform([query])
            similarities = cosine_similarity(query_vec, tfidf_matrix)[0]

            # Top K indices
            top_indices = similarities.argsort()[-top_k:][::-1]

            results = []
            for idx in top_indices:
                if similarities[idx] > 0.01:  # Seuil minimum
                    entry = entries[idx].copy()
                    entry['score'] = float(similarities[idx])

                    # Bonus keywords match
                    query_lower = query.lower()
                    keywords = entry.get('keywords', [])
                    keyword_matches = sum(1 for kw in keywords if kw.lower() in query_lower)
                    entry['score'] += keyword_matches * 0.15

                    results.append(entry)

            return results
        except Exception as e:
            print(f"[HybridKB] ERROR in _search_core: {e}")
            return []

    def _search_nitrite(self, query: str, top_k: int) -> List[Dict]:
        """Recherche dans NiTriTe KB (pages + workflows)"""
        results = []
        query_lower = query.lower()

        # 1. Query mapping direct
        query_mapping = self.nitrite_kb.get('query_mapping', {})
        for keyword, page_ids in query_mapping.items():
            if keyword in query_lower:
                # Keyword match trouvé
                if isinstance(page_ids, str):
                    page_ids = [page_ids]

                for page_id in page_ids:
                    page = self.nitrite_kb.get('pages', {}).get(page_id)
                    if page:
                        results.append({
                            'type': 'page',
                            'page_id': page_id,
                            'page': page,
                            'score': 0.9,  # Score élevé pour match direct
                            'match_type': 'query_mapping'
                        })

        # 2. Recherche dans descriptions pages
        pages = self.nitrite_kb.get('pages', {})
        for page_id, page_data in pages.items():
            description = page_data.get('description', '').lower()
            name = page_data.get('name', '').lower()

            if query_lower in description or query_lower in name:
                results.append({
                    'type': 'page',
                    'page_id': page_id,
                    'page': page_data,
                    'score': 0.7,
                    'match_type': 'description_match'
                })

        # 3. Recherche dans workflows
        workflows = self.nitrite_kb.get('workflows', [])
        for workflow in workflows:
            wf_name = workflow.get('name', '').lower()
            wf_desc = workflow.get('description', '').lower()
            typical_queries = workflow.get('typical_queries', [])

            score = 0.0
            if any(q in query_lower for q in typical_queries):
                score = 0.85
            elif query_lower in wf_name or query_lower in wf_desc:
                score = 0.65

            if score > 0:
                results.append({
                    'type': 'workflow',
                    'workflow': workflow,
                    'score': score,
                    'match_type': 'workflow_match'
                })

        # Trier et limiter
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

    def _search_legacy(self, query: str, top_k: int) -> List[Dict]:
        """Recherche dans Legacy KB"""
        if not self.legacy_kb:
            return []

        try:
            # Utilise la méthode existante de UnifiedKnowledgeBase
            # Note: search_tips n'existe pas encore, donc fallback simple
            results = []
            query_lower = query.lower()

            for category, cat_data in self.legacy_kb.knowledge_base.items():
                tips = cat_data.get('tips', [])
                for tip in tips:
                    content = tip.get('content', '').lower()
                    keywords = tip.get('keywords', [])

                    # Simple keyword matching
                    score = 0.0
                    if query_lower in content:
                        score += 0.5

                    keyword_matches = sum(1 for kw in keywords if kw.lower() in query_lower)
                    score += keyword_matches * 0.2

                    if score > 0:
                        results.append({
                            'category': category,
                            'tip': tip,
                            'score': score
                        })

            results.sort(key=lambda x: x['score'], reverse=True)
            return results[:top_k]

        except Exception as e:
            print(f"[HybridKB] ERROR in _search_legacy: {e}")
            return []

    def _search_auto_learned(self, query: str, top_k: int) -> List[Dict]:
        """Recherche dans docs auto-apprises"""
        results = []
        query_lower = query.lower()

        # Recherche dans markdown
        markdown_docs = self.auto_learned.get('markdown', [])
        for doc in markdown_docs:
            title = doc.get('title', '').lower()
            sections = doc.get('sections', [])

            score = 0.0
            if query_lower in title:
                score += 0.6

            for section in sections:
                section_content = ' '.join(section.get('content', [])).lower()
                if query_lower in section_content:
                    score += 0.3
                    break

            if score > 0:
                results.append({
                    'type': 'markdown',
                    'doc': doc,
                    'score': score
                })

        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]

    def _is_nitrite_query(self, query: str) -> bool:
        """Détecte si query concerne NiTriTe spécifiquement"""
        nitrite_keywords = [
            'nitrite', 'page', 'installer', 'télécharger', 'app', 'application',
            'driver', 'update', 'diagnostic', 'optimisation', 'terminal', 'pack'
        ]
        query_lower = query.lower()
        return any(kw in query_lower for kw in nitrite_keywords)

    def _score_and_rank(self, results: List[Dict], query: str, filters: Optional[Dict]) -> List[Dict]:
        """Scoring final pondéré et ranking"""
        final_results = []

        for res in results:
            # Score final = score * weight
            final_score = res['score'] * res['weight']

            # Application filtres
            if filters:
                if 'difficulty' in filters:
                    content = res.get('content', {})
                    if isinstance(content, dict):
                        content_diff = content.get('difficulty', 'intermediate')
                        if content_diff != filters['difficulty']:
                            final_score *= 0.5  # Pénalité si pas le bon niveau

            final_results.append({
                'source': res['source'],
                'score': final_score,
                'content': res['content']
            })

        # Tri par score final
        final_results.sort(key=lambda x: x['score'], reverse=True)

        return final_results

    def get_nitrite_page(self, page_id: str) -> Optional[Dict]:
        """Récupère une page NiTriTe par ID"""
        return self.nitrite_kb.get('pages', {}).get(page_id)

    def get_workflow(self, workflow_id: str) -> Optional[Dict]:
        """Récupère un workflow par ID"""
        workflows = self.nitrite_kb.get('workflows', [])
        for wf in workflows:
            if wf.get('id') == workflow_id:
                return wf
        return None

    def suggest_nitrite_tools(self, query: str, problem_keywords: List[str]) -> List[Dict]:
        """Suggère outils NiTriTe pertinents selon problème"""
        suggestions = []

        # Mapping problèmes → outils diagnostic
        problem_tool_map = {
            'lenteur': ['HWMonitor', 'CrystalDiskInfo', 'CrystalDiskMark'],
            'température': ['HWMonitor'],
            'batterie': ['Battery Test'],
            'disque': ['CrystalDiskInfo', 'CrystalDiskMark'],
            'ram': ['CPU-Z'],
            'cpu': ['CPU-Z', 'HWMonitor', 'OCCT'],
            'gpu': ['GPU-Z', 'HWMonitor', 'FurMark'],
            'crash': ['OCCT', 'MemTest86']
        }

        diag_page = self.get_nitrite_page('diagnostic')
        if not diag_page:
            return []

        tools = diag_page.get('tools', [])

        # Matching keywords
        for problem in problem_keywords:
            tool_names = problem_tool_map.get(problem.lower(), [])
            for tool_name in tool_names:
                for tool in tools:
                    if tool.get('name') == tool_name:
                        suggestions.append({
                            'problem': problem,
                            'tool': tool,
                            'page': 'diagnostic'
                        })

        # Déduplication
        unique_tools = []
        seen_names = set()
        for s in suggestions:
            tool_name = s['tool'].get('name')
            if tool_name not in seen_names:
                unique_tools.append(s)
                seen_names.add(tool_name)

        return unique_tools


# Test rapide
if __name__ == "__main__":
    print("=== Test HybridKnowledgeBase ===\n")

    kb = HybridKnowledgeBase()

    print("\n=== Test recherche: 'température cpu' ===")
    results = kb.search("température cpu", top_k=5)
    for i, res in enumerate(results, 1):
        print(f"\n{i}. Source: {res['source']} | Score: {res['score']:.3f}")
        if res['source'] == 'core_kb':
            print(f"   Titre: {res['content'].get('title', 'N/A')[:80]}")
        elif res['source'] == 'nitrite_kb':
            if res['content'].get('type') == 'page':
                print(f"   Page: {res['content']['page'].get('name', 'N/A')}")

    print("\n=== Test recherche NiTriTe: 'installer chrome' ===")
    results = kb.search("installer chrome", top_k=3)
    for i, res in enumerate(results, 1):
        print(f"\n{i}. Source: {res['source']} | Score: {res['score']:.3f}")
        if res['source'] == 'nitrite_kb' and res['content'].get('type') == 'page':
            page = res['content']['page']
            print(f"   Page: {page.get('emoji')} {page.get('name')}")
            print(f"   Description: {page.get('description', '')[:100]}")

    print("\n=== Test suggestions outils ===")
    suggestions = kb.suggest_nitrite_tools("pc lent", ['lenteur', 'température'])
    for sugg in suggestions:
        tool = sugg['tool']
        print(f"- {tool.get('name')}: {tool.get('description', '')[:80]}")
