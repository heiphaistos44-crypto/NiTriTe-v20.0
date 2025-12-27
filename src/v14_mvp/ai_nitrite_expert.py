#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NiTriTe Expert - NiTriTe V20.0
Expert système pour recommandations NiTriTe (pages, workflows, outils)
"""

import json
from pathlib import Path
from typing import List, Dict, Optional


class NiTriTeExpert:
    """
    Expert NiTriTe connaissant parfaitement les 14 pages, workflows, et outils
    Suggère pages/outils pertinents selon query utilisateur
    """

    def __init__(self, kb_path="data/knowledge/nitrite_expert_kb.json"):
        self.kb_path = Path(kb_path)
        self.kb = self.load_kb()

        # Cache recherches fréquentes
        self._page_cache = {}

        print(f"[NiTriTeExpert] Chargé: {len(self.kb.get('pages', {}))} pages, "
              f"{len(self.kb.get('workflows', []))} workflows")

    def load_kb(self) -> Dict:
        """Charge base de connaissances NiTriTe"""
        if not self.kb_path.exists():
            print(f"[NiTriTeExpert] WARN: KB non trouvé: {self.kb_path}")
            return {"pages": {}, "workflows": [], "query_mapping": {}}

        try:
            with open(self.kb_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[NiTriTeExpert] ERROR loading KB: {e}")
            return {"pages": {}, "workflows": [], "query_mapping": {}}

    def find_relevant_page(self, query: str) -> Optional[Dict]:
        """
        Trouve la page NiTriTe la plus pertinente pour une query

        Args:
            query: Query utilisateur

        Returns:
            Dict avec page_id et page_data, ou None
        """
        query_lower = query.lower()

        # 1. Query mapping direct (le plus fiable)
        query_mapping = self.kb.get('query_mapping', {})
        for keyword, page_ids in query_mapping.items():
            if keyword in query_lower:
                # Match trouvé !
                if isinstance(page_ids, str):
                    page_ids = [page_ids]

                # Prend la première page suggérée
                page_id = page_ids[0]
                page_data = self.get_page(page_id)

                if page_data:
                    return {
                        'page_id': page_id,
                        'page': page_data,
                        'confidence': 0.95,
                        'match_type': 'keyword_direct'
                    }

        # 2. Recherche dans noms/descriptions pages
        pages = self.kb.get('pages', {})
        best_match = None
        best_score = 0.0

        for page_id, page_data in pages.items():
            score = 0.0
            name = page_data.get('name', '').lower()
            description = page_data.get('description', '').lower()

            # Score par présence dans nom
            if query_lower in name:
                score += 0.8

            # Score par présence dans description
            if query_lower in description:
                score += 0.5

            # Score par nombre mots communs
            query_words = set(query_lower.split())
            desc_words = set(description.split())
            common = len(query_words & desc_words)
            score += common * 0.1

            if score > best_score:
                best_score = score
                best_match = {
                    'page_id': page_id,
                    'page': page_data,
                    'confidence': min(score, 0.9),
                    'match_type': 'description_match'
                }

        return best_match if best_score > 0.3 else None

    def get_page(self, page_id: str) -> Optional[Dict]:
        """Récupère page par ID"""
        return self.kb.get('pages', {}).get(page_id)

    def suggest_tools(self, query: str, problem_keywords: List[str] = None) -> List[Dict]:
        """
        Suggère outils NiTriTe pertinents

        Args:
            query: Query utilisateur
            problem_keywords: Keywords problème détectés (ex: ['lenteur', 'température'])

        Returns:
            Liste d'outils avec page source
        """
        if problem_keywords is None:
            problem_keywords = self._extract_problem_keywords(query)

        suggestions = []

        # Mapping problèmes → outils diagnostic
        problem_tool_map = {
            'lent': ['HWMonitor', 'CrystalDiskInfo', 'CrystalDiskMark'],
            'lenteur': ['HWMonitor', 'CrystalDiskInfo', 'CrystalDiskMark'],
            'température': ['HWMonitor'],
            'chaleur': ['HWMonitor'],
            'chauffe': ['HWMonitor'],
            'batterie': ['Battery Test'],
            'disque': ['CrystalDiskInfo', 'CrystalDiskMark'],
            'ssd': ['CrystalDiskInfo', 'CrystalDiskMark'],
            'hdd': ['CrystalDiskInfo'],
            'ram': ['CPU-Z'],
            'mémoire': ['CPU-Z'],
            'cpu': ['CPU-Z', 'HWMonitor', 'OCCT'],
            'processeur': ['CPU-Z', 'HWMonitor'],
            'gpu': ['GPU-Z', 'HWMonitor'],
            'carte graphique': ['GPU-Z'],
            'crash': ['OCCT'],
            'freeze': ['OCCT'],
            'instable': ['OCCT']
        }

        # Récupération outils page diagnostic
        diag_page = self.get_page('diagnostic')
        if not diag_page:
            return []

        tools = diag_page.get('tools', [])

        # Matching keywords → tools
        suggested_names = set()
        for keyword in problem_keywords:
            tool_names = problem_tool_map.get(keyword.lower(), [])
            for tool_name in tool_names:
                if tool_name not in suggested_names:
                    # Trouve l'outil complet
                    for tool in tools:
                        if tool.get('name') == tool_name:
                            suggestions.append({
                                'problem': keyword,
                                'tool': tool,
                                'page': 'diagnostic',
                                'page_emoji': '🔍'
                            })
                            suggested_names.add(tool_name)
                            break

        return suggestions

    def _extract_problem_keywords(self, query: str) -> List[str]:
        """Extrait keywords problème de la query"""
        keywords = []
        query_lower = query.lower()

        problem_patterns = {
            'lent': ['lent', 'ralenti', 'lag', 'freeze', 'rame'],
            'température': ['chauffe', 'température', 'chaleur', 'surchauffe', 'throttling'],
            'batterie': ['batterie', 'autonomie'],
            'disque': ['disque', 'ssd', 'hdd', 'stockage'],
            'ram': ['ram', 'mémoire'],
            'cpu': ['cpu', 'processeur'],
            'gpu': ['gpu', 'carte graphique', 'nvidia', 'amd'],
            'crash': ['crash', 'plantage', 'bsod', 'écran bleu']
        }

        for category, patterns in problem_patterns.items():
            if any(p in query_lower for p in patterns):
                keywords.append(category)

        return keywords if keywords else ['général']

    def find_workflow(self, goal: str) -> Optional[Dict]:
        """
        Trouve workflow approprié pour un objectif

        Args:
            goal: Objectif utilisateur (ex: "fresh install", "optimiser gaming")

        Returns:
            Workflow dict ou None
        """
        workflows = self.kb.get('workflows', [])
        goal_lower = goal.lower()

        for wf in workflows:
            # Check typical queries
            typical_queries = wf.get('typical_queries', [])
            if any(q in goal_lower for q in typical_queries):
                return wf

            # Check nom/description
            name = wf.get('name', '').lower()
            description = wf.get('description', '').lower()

            if goal_lower in name or goal_lower in description:
                return wf

        return None

    def generate_guide(self, page_id: str = None, workflow_id: str = None,
                      custom_goal: str = None) -> str:
        """
        Génère guide NiTriTe détaillé

        Args:
            page_id: ID page à documenter
            workflow_id: ID workflow à documenter
            custom_goal: Objectif personnalisé

        Returns:
            Guide formaté Markdown
        """
        if page_id:
            page = self.get_page(page_id)
            if not page:
                return f"❌ Page '{page_id}' non trouvée"

            guide = f"# {page.get('emoji', '')} {page.get('name', 'Page')}\n\n"
            guide += f"{page.get('description', '')}\n\n"

            # Features
            features = page.get('features', {})
            if features:
                guide += "## Fonctionnalités\n\n"
                for fname, fdesc in features.items():
                    guide += f"- **{fname}** : {fdesc}\n"
                guide += "\n"

            # Common tasks
            common_tasks = page.get('common_tasks', [])
            if common_tasks:
                guide += "## Tâches Courantes\n\n"
                for task in common_tasks:
                    guide += f"### {task.get('task', 'Task')}\n\n"
                    guide += "**Étapes** :\n"
                    for i, step in enumerate(task.get('steps', []), 1):
                        guide += f"{i}. {step}\n"
                    guide += f"\n⏱️ Durée : {task.get('duration', 'Variable')}\n\n"

            return guide

        elif workflow_id:
            workflows = self.kb.get('workflows', [])
            workflow = None
            for wf in workflows:
                if wf.get('id') == workflow_id:
                    workflow = wf
                    break

            if not workflow:
                return f"❌ Workflow '{workflow_id}' non trouvé"

            guide = f"# {workflow.get('name', 'Workflow')}\n\n"
            guide += f"{workflow.get('description', '')}\n\n"
            guide += f"⏱️ **Durée** : {workflow.get('duration', 'Variable')}\n"
            guide += f"📊 **Difficulté** : {workflow.get('difficulty', 'Moyenne')}\n\n"

            guide += "## Étapes\n\n"
            for step_data in workflow.get('steps', []):
                step_num = step_data.get('step', '?')
                page = step_data.get('page', '')
                action = step_data.get('action', '')
                why = step_data.get('why', '')

                guide += f"### Étape {step_num} : {action}\n\n"
                guide += f"📍 **Page** : {page}\n\n"
                if why:
                    guide += f"**Pourquoi** : {why}\n\n"

            return guide

        else:
            return "❌ Spécifiez page_id ou workflow_id"

    def get_stats(self) -> Dict:
        """Statistiques NiTriTe KB"""
        return {
            'total_pages': len(self.kb.get('pages', {})),
            'total_workflows': len(self.kb.get('workflows', [])),
            'total_apps': self.kb.get('stats', {}).get('total_apps', 0),
            'total_portables': self.kb.get('stats', {}).get('total_portables', 0),
            'total_scripts': self.kb.get('stats', {}).get('total_scripts', 0),
            'query_mappings': len(self.kb.get('query_mapping', {}))
        }


# Test
if __name__ == "__main__":
    print("=== Test NiTriTeExpert ===\n")

    expert = NiTriTeExpert()

    # Stats
    stats = expert.get_stats()
    print("Stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # Test recherche page
    print("\n=== Test: 'installer chrome' ===")
    result = expert.find_relevant_page("installer chrome")
    if result:
        page = result['page']
        print(f"Page trouvée: {page.get('emoji')} {page.get('name')}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Match type: {result['match_type']}")

    # Test suggestions outils
    print("\n=== Test: suggestions pour 'pc lent température' ===")
    tools = expert.suggest_tools("mon pc est lent et chauffe", ['lent', 'température'])
    for tool_data in tools:
        tool = tool_data['tool']
        print(f"- {tool.get('name')}: {tool.get('description', '')[:60]}...")

    # Test guide
    print("\n=== Test: guide page Applications ===")
    guide = expert.generate_guide(page_id='applications')
    print(guide[:300] + "...")
