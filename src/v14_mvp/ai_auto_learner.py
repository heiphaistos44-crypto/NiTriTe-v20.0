#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-Learner - NiTriTe V20.0
Scanner automatique de documentation pour enrichissement KB continu
"""

import os
import json
import hashlib
import re
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class AutoLearner:
    """
    Scanner automatique de documentation
    - Parse .md files (README, CORRECTIONS, docs/)
    - Index .json databases (programs, portables, custom_packs)
    - Mise à jour incrémentale (hash-based change detection)
    - Recherche dans docs apprises
    """

    def __init__(self, root_dir=".", index_dir="data/knowledge/auto_learned"):
        self.root_dir = Path(root_dir)
        self.index_dir = Path(index_dir)
        self.index_dir.mkdir(parents=True, exist_ok=True)

        # Chemins index
        self.markdown_index_path = self.index_dir / "markdown_index.json"
        self.json_index_path = self.index_dir / "json_index.json"
        self.updates_log_path = self.index_dir / "updates.log"

        # Chargement index
        self.markdown_index = self.load_index(self.markdown_index_path)
        self.json_index = self.load_index(self.json_index_path)

        print(f"[AutoLearner] Initialisé: {len(self.markdown_index.get('files', []))} .md, "
              f"{len(self.json_index.get('files', []))} .json indexés")

    def load_index(self, index_path: Path) -> Dict:
        """Charge index depuis disque"""
        if not index_path.exists():
            return {
                'version': '1.0.0',
                'files': [],
                'last_scan': None,
                'total_entries': 0
            }

        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[AutoLearner] ERROR loading index {index_path}: {e}")
            return {'version': '1.0.0', 'files': [], 'last_scan': None, 'total_entries': 0}

    def save_index(self, index_data: Dict, index_path: Path):
        """Sauvegarde index"""
        try:
            with open(index_path, 'w', encoding='utf-8') as f:
                json.dump(index_data, f, indent=2, ensure_ascii=False)
            print(f"[AutoLearner] Index sauvegardé: {index_path}")
        except Exception as e:
            print(f"[AutoLearner] ERROR saving index: {e}")

    def scan_all(self, force_rescan: bool = False) -> Dict:
        """
        Scan complet de toute la documentation

        Args:
            force_rescan: Forcer re-scan même si hash identique

        Returns:
            Dict avec statistiques scan
        """
        print("[AutoLearner] Scan complet de la documentation...")

        stats = {
            'markdown_files_scanned': 0,
            'markdown_new': 0,
            'markdown_updated': 0,
            'json_files_scanned': 0,
            'json_new': 0,
            'json_updated': 0,
            'scan_duration_seconds': 0,
            'scan_timestamp': datetime.now().isoformat()
        }

        start_time = datetime.now()

        # Scan markdown
        md_stats = self.scan_markdown_files(force_rescan=force_rescan)
        stats.update(md_stats)

        # Scan JSON databases
        json_stats = self.scan_json_databases(force_rescan=force_rescan)
        stats.update(json_stats)

        # Durée
        stats['scan_duration_seconds'] = (datetime.now() - start_time).total_seconds()

        # Log
        self._log_scan(stats)

        # Update last_scan
        self.markdown_index['last_scan'] = stats['scan_timestamp']
        self.json_index['last_scan'] = stats['scan_timestamp']

        # Save
        self.save_index(self.markdown_index, self.markdown_index_path)
        self.save_index(self.json_index, self.json_index_path)

        print(f"[AutoLearner] Scan termine en {stats['scan_duration_seconds']:.1f}s")
        print(f"  Markdown: {stats['markdown_new']} nouveaux, {stats['markdown_updated']} mis a jour")
        print(f"  JSON: {stats['json_new']} nouveaux, {stats['json_updated']} mis a jour")

        return stats

    def scan_markdown_files(self, force_rescan: bool = False) -> Dict:
        """
        Scan tous les .md du projet

        Returns:
            Dict avec stats
        """
        stats = {
            'markdown_files_scanned': 0,
            'markdown_new': 0,
            'markdown_updated': 0
        }

        # Patterns à exclure
        exclude_patterns = [
            'venv/', 'node_modules/', '.git/', '__pycache__/',
            'temp/', 'cache/', 'downloads/'
        ]

        # Trouve tous .md
        for md_path in self.root_dir.rglob("*.md"):
            # Skip exclusions
            if any(excl in str(md_path) for excl in exclude_patterns):
                continue

            stats['markdown_files_scanned'] += 1

            # Parse fichier
            file_data = self._parse_markdown_file(md_path, force_rescan=force_rescan)

            if file_data:
                # Nouveau ou mis à jour ?
                existing = self._find_file_in_index(str(md_path), self.markdown_index)

                if existing is None:
                    # Nouveau
                    self.markdown_index['files'].append(file_data)
                    stats['markdown_new'] += 1
                elif existing['hash'] != file_data['hash']:
                    # Mis à jour
                    self._update_file_in_index(str(md_path), file_data, self.markdown_index)
                    stats['markdown_updated'] += 1

        # Update total
        self.markdown_index['total_entries'] = len(self.markdown_index['files'])

        return stats

    def scan_json_databases(self, force_rescan: bool = False) -> Dict:
        """
        Scan fichiers JSON importants (programs, portables, custom_packs, etc.)

        Returns:
            Dict avec stats
        """
        stats = {
            'json_files_scanned': 0,
            'json_new': 0,
            'json_updated': 0
        }

        # JSON importants à indexer
        important_json = [
            'data/programs.json',
            'data/portable_apps.json',
            'data/custom_packs.json',
            'data/nitrite_config.json',
            'src/v14_mvp/storage/api_keys_encrypted.json'
        ]

        for json_path_str in important_json:
            json_path = self.root_dir / json_path_str

            if not json_path.exists():
                continue

            stats['json_files_scanned'] += 1

            # Parse JSON
            file_data = self._parse_json_file(json_path, force_rescan=force_rescan)

            if file_data:
                existing = self._find_file_in_index(str(json_path), self.json_index)

                if existing is None:
                    self.json_index['files'].append(file_data)
                    stats['json_new'] += 1
                elif existing['hash'] != file_data['hash']:
                    self._update_file_in_index(str(json_path), file_data, self.json_index)
                    stats['json_updated'] += 1

        # Update total
        self.json_index['total_entries'] = len(self.json_index['files'])

        return stats

    def _parse_markdown_file(self, md_path: Path, force_rescan: bool = False) -> Optional[Dict]:
        """
        Parse fichier Markdown en sections

        Returns:
            Dict avec path, hash, title, sections, keywords
        """
        try:
            content = md_path.read_text(encoding='utf-8')
            content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()

            # Skip si déjà indexé avec même hash
            if not force_rescan:
                existing = self._find_file_in_index(str(md_path), self.markdown_index)
                if existing and existing['hash'] == content_hash:
                    return None  # Pas de changement

            # Extraction titre
            title = self._extract_markdown_title(content)

            # Extraction sections
            sections = self._parse_markdown_sections(content)

            # Extraction keywords
            keywords = self._extract_markdown_keywords(content, title)

            return {
                'path': str(md_path),
                'hash': content_hash,
                'title': title,
                'sections_count': len(sections),
                'sections': sections[:20],  # Limite 20 sections pour taille
                'keywords': keywords[:50],  # Top 50 keywords
                'file_size_kb': md_path.stat().st_size / 1024,
                'indexed_at': datetime.now().isoformat()
            }

        except Exception as e:
            print(f"[AutoLearner] ERROR parsing {md_path}: {e}")
            return None

    def _parse_json_file(self, json_path: Path, force_rescan: bool = False) -> Optional[Dict]:
        """
        Parse fichier JSON (structure + metadata)

        Returns:
            Dict avec path, hash, type, entries_count, structure
        """
        try:
            content = json_path.read_text(encoding='utf-8')
            content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()

            # Skip si déjà indexé
            if not force_rescan:
                existing = self._find_file_in_index(str(json_path), self.json_index)
                if existing and existing['hash'] == content_hash:
                    return None

            data = json.loads(content)

            # Détection type
            db_type = self._detect_json_type(json_path.name, data)

            # Comptage entries
            entries_count = self._count_json_entries(data, db_type)

            # Analyse structure
            structure = self._analyze_json_structure(data)

            # Extraction sample entries (pour recherche)
            sample_entries = self._extract_json_sample(data, db_type)

            return {
                'path': str(json_path),
                'hash': content_hash,
                'type': db_type,
                'entries_count': entries_count,
                'structure': structure,
                'sample_entries': sample_entries[:10],  # 10 exemples
                'file_size_kb': json_path.stat().st_size / 1024,
                'indexed_at': datetime.now().isoformat()
            }

        except Exception as e:
            print(f"[AutoLearner] ERROR parsing {json_path}: {e}")
            return None

    # === Parsing Helpers ===

    def _extract_markdown_title(self, content: str) -> str:
        """Extrait titre du markdown (premier # ou nom fichier)"""
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled"

    def _parse_markdown_sections(self, content: str) -> List[Dict]:
        """Parse markdown en sections (## headers)"""
        sections = []
        current_section = None
        current_content = []

        for line in content.split('\n'):
            # Détection headers
            if line.startswith('# ') or line.startswith('## ') or line.startswith('### '):
                # Sauvegarde section précédente
                if current_section:
                    sections.append({
                        'title': current_section,
                        'content': '\n'.join(current_content[:100])  # Limite contenu
                    })

                # Nouvelle section
                level = line.count('#', 0, 3)
                current_section = line.lstrip('#').strip()
                current_content = []
            else:
                if current_section:
                    current_content.append(line)

        # Dernière section
        if current_section:
            sections.append({
                'title': current_section,
                'content': '\n'.join(current_content[:100])
            })

        return sections

    def _extract_markdown_keywords(self, content: str, title: str) -> List[str]:
        """Extrait keywords du markdown"""
        # Combine title + content
        text = f"{title} {content}".lower()

        # Remove markdown syntax
        text = re.sub(r'[#*`\[\]()]', ' ', text)

        # Split words
        words = re.findall(r'\b\w{4,}\b', text)  # Mots 4+ chars

        # Compte fréquence
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Trie par fréquence
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

        # Top keywords
        keywords = [w[0] for w in sorted_words[:50]]

        return keywords

    def _detect_json_type(self, filename: str, data: Dict) -> str:
        """Détecte type de base JSON"""
        type_map = {
            'programs.json': 'applications_catalog',
            'portable_apps.json': 'portable_catalog',
            'custom_packs.json': 'installation_packs',
            'nitrite_config.json': 'app_configuration',
            'api_keys': 'api_configuration',
            'core_kb.json': 'knowledge_base',
            'nitrite_expert_kb.json': 'expert_knowledge'
        }

        for key, val in type_map.items():
            if key in filename:
                return val

        # Détection par structure
        if 'categories' in data and isinstance(data.get('categories'), dict):
            return 'categorized_catalog'
        elif 'entries' in data and isinstance(data.get('entries'), list):
            return 'knowledge_base'

        return 'unknown'

    def _count_json_entries(self, data: Dict, db_type: str) -> int:
        """Compte entries dans JSON selon type"""
        if db_type == 'applications_catalog':
            # programs.json : categories -> apps
            count = 0
            for category_data in data.get('categories', {}).values():
                count += len(category_data.get('apps', []))
            return count

        elif db_type in ['portable_catalog', 'installation_packs']:
            # Listes directes
            return len(data.get('portables', []) or data.get('packs', []))

        elif db_type == 'knowledge_base':
            return len(data.get('entries', []))

        return 0

    def _analyze_json_structure(self, data: Dict) -> Dict:
        """Analyse structure JSON (keys, types)"""
        structure = {
            'top_level_keys': list(data.keys()),
            'data_types': {}
        }

        for key, value in data.items():
            structure['data_types'][key] = type(value).__name__

        return structure

    def _extract_json_sample(self, data: Dict, db_type: str) -> List[Dict]:
        """Extrait sample entries pour indexation"""
        samples = []

        if db_type == 'applications_catalog':
            # Prend 2 apps par catégorie
            for category, category_data in list(data.get('categories', {}).items())[:5]:
                apps = category_data.get('apps', [])[:2]
                for app in apps:
                    samples.append({
                        'category': category,
                        'name': app.get('name', ''),
                        'description': app.get('description', '')[:100]
                    })

        elif db_type == 'knowledge_base':
            # Prend 10 premières entries
            entries = data.get('entries', [])[:10]
            for entry in entries:
                samples.append({
                    'title': entry.get('title', ''),
                    'category': entry.get('category', ''),
                    'keywords': entry.get('keywords', [])[:5]
                })

        return samples

    # === Index Management ===

    def _find_file_in_index(self, file_path: str, index: Dict) -> Optional[Dict]:
        """Trouve fichier dans index"""
        for file_data in index.get('files', []):
            if file_data['path'] == file_path:
                return file_data
        return None

    def _update_file_in_index(self, file_path: str, new_data: Dict, index: Dict):
        """Met à jour fichier dans index"""
        for i, file_data in enumerate(index['files']):
            if file_data['path'] == file_path:
                index['files'][i] = new_data
                return

    def _log_scan(self, stats: Dict):
        """Log résultats scan"""
        try:
            log_entry = f"[{stats['scan_timestamp']}] Scan: {stats['markdown_new']} MD new, " \
                       f"{stats['json_new']} JSON new, {stats['scan_duration_seconds']:.1f}s\n"

            with open(self.updates_log_path, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"[AutoLearner] ERROR logging: {e}")

    # === Recherche ===

    def search_learned(self, query: str, search_in: str = 'all') -> List[Dict]:
        """
        Recherche dans documentation apprise

        Args:
            query: Query utilisateur
            search_in: 'all', 'markdown', 'json'

        Returns:
            Liste résultats [{type, file, section/entry, relevance}]
        """
        query_lower = query.lower()
        results = []

        # Recherche markdown
        if search_in in ['all', 'markdown']:
            for md_file in self.markdown_index.get('files', []):
                # Check title
                if query_lower in md_file.get('title', '').lower():
                    results.append({
                        'type': 'markdown',
                        'file': md_file['path'],
                        'title': md_file['title'],
                        'match_location': 'title',
                        'relevance': 0.9
                    })

                # Check keywords
                keywords = md_file.get('keywords', [])
                if any(query_lower in kw for kw in keywords):
                    results.append({
                        'type': 'markdown',
                        'file': md_file['path'],
                        'title': md_file['title'],
                        'match_location': 'keywords',
                        'relevance': 0.7
                    })

                # Check sections
                for section in md_file.get('sections', []):
                    if query_lower in section['title'].lower() or query_lower in section['content'].lower():
                        results.append({
                            'type': 'markdown',
                            'file': md_file['path'],
                            'section': section['title'],
                            'content_preview': section['content'][:200],
                            'match_location': 'section_content',
                            'relevance': 0.6
                        })

        # Recherche JSON
        if search_in in ['all', 'json']:
            for json_file in self.json_index.get('files', []):
                # Check sample entries
                for sample in json_file.get('sample_entries', []):
                    sample_text = json.dumps(sample, ensure_ascii=False).lower()
                    if query_lower in sample_text:
                        results.append({
                            'type': 'json',
                            'file': json_file['path'],
                            'db_type': json_file['type'],
                            'entry': sample,
                            'match_location': 'entry_data',
                            'relevance': 0.5
                        })

        # Tri par relevance
        results.sort(key=lambda r: r['relevance'], reverse=True)

        return results[:20]  # Top 20

    def get_stats(self) -> Dict:
        """Statistiques auto-learner"""
        return {
            'markdown_files': len(self.markdown_index.get('files', [])),
            'json_files': len(self.json_index.get('files', [])),
            'last_scan_markdown': self.markdown_index.get('last_scan'),
            'last_scan_json': self.json_index.get('last_scan'),
            'total_sections': sum(f.get('sections_count', 0) for f in self.markdown_index.get('files', [])),
            'total_json_entries': sum(f.get('entries_count', 0) for f in self.json_index.get('files', []))
        }


# Test
if __name__ == "__main__":
    print("=== Test AutoLearner ===\n")

    learner = AutoLearner(root_dir="../../")  # Depuis src/v14_mvp/

    # Test scan
    print("Scan documentation...\n")
    stats = learner.scan_all()

    print(f"\n✅ Résultats:")
    for key, val in stats.items():
        print(f"  {key}: {val}")

    # Stats
    print("\n=== Statistiques ===")
    stats = learner.get_stats()
    for key, val in stats.items():
        print(f"  {key}: {val}")

    # Test recherche
    print("\n=== Test recherche: 'installation' ===")
    results = learner.search_learned("installation", search_in='all')

    for i, res in enumerate(results[:5], 1):
        print(f"\n{i}. [{res['type']}] {res.get('file', 'N/A')}")
        print(f"   Match: {res['match_location']}, Relevance: {res['relevance']}")
        if 'section' in res:
            print(f"   Section: {res['section']}")
