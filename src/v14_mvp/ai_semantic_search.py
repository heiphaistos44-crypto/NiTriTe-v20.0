#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Semantic Search Engine - NiTriTe V20.0
Moteur de recherche sémantique avec embeddings et FAISS
"""

import os
import json
import pickle
import hashlib
from pathlib import Path
from typing import List, Dict, Optional
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    import faiss
    SEMANTIC_SEARCH_AVAILABLE = True
except ImportError:
    print("[SemanticSearch] WARN: sentence-transformers ou faiss non installé")
    SEMANTIC_SEARCH_AVAILABLE = False


class SemanticSearchEngine:
    """
    Moteur de recherche sémantique utilisant:
    - sentence-transformers/all-MiniLM-L6-v2 (~80MB, excellent qualité)
    - FAISS pour recherche vectorielle ultra-rapide
    """

    def __init__(self, embeddings_dir="data/knowledge/embeddings"):
        if not SEMANTIC_SEARCH_AVAILABLE:
            raise ImportError("sentence-transformers et faiss-cpu requis. pip install sentence-transformers faiss-cpu")

        self.embeddings_dir = Path(embeddings_dir)
        self.embeddings_dir.mkdir(parents=True, exist_ok=True)

        # Chemins
        self.index_path = self.embeddings_dir / "core_kb.faiss"
        self.metadata_path = self.embeddings_dir / "core_kb.pkl"
        self.model_cache_dir = self.embeddings_dir / "model_cache"
        self.model_cache_dir.mkdir(exist_ok=True)

        # Modèle sentence-transformers
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        print(f"[SemanticSearch] Chargement modèle {self.model_name}...")

        try:
            self.model = SentenceTransformer(
                self.model_name,
                cache_folder=str(self.model_cache_dir)
            )
            print(f"[SemanticSearch] Modèle chargé (dimension: {self.model.get_sentence_embedding_dimension()})")
        except Exception as e:
            print(f"[SemanticSearch] ERROR loading model: {e}")
            raise

        # Index FAISS et métadonnées
        self.index = None
        self.metadata = None

        # Cache queries (évite re-encoding)
        self.query_cache = {}
        self.cache_max_size = 1000

        # Chargement ou création index
        if self.index_path.exists() and self.metadata_path.exists():
            self.load_index()
        else:
            print("[SemanticSearch] Index non trouvé. Utilisez build_index() pour créer.")

    def build_index(self, kb_data: Dict, force_rebuild: bool = False):
        """
        Génère les embeddings et crée l'index FAISS

        Args:
            kb_data: Données KB format {"entries": [...]}
            force_rebuild: Forcer reconstruction même si index existe
        """
        if self.index is not None and not force_rebuild:
            print("[SemanticSearch] Index déjà chargé. Utilisez force_rebuild=True pour reconstruire.")
            return

        entries = kb_data.get('entries', [])
        if not entries:
            print("[SemanticSearch] WARN: Aucune entrée à indexer")
            return

        print(f"[SemanticSearch] Indexation de {len(entries)} entrées...")

        # Préparation textes à embedder
        texts = []
        for entry in entries:
            # Combinaison: titre + contenu + keywords
            text = f"{entry.get('title', '')} {entry.get('content', '')} {' '.join(entry.get('keywords', []))}"
            texts.append(text)

        # Génération embeddings par batch
        print("[SemanticSearch] Génération embeddings (peut prendre 1-2 min)...")
        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )

        # Création index FAISS (Inner Product pour cosine similarity)
        dimension = embeddings.shape[1]  # 384 pour MiniLM
        self.index = faiss.IndexFlatIP(dimension)

        # Normalisation pour cosine similarity
        faiss.normalize_L2(embeddings)

        # Ajout vecteurs à l'index
        self.index.add(embeddings.astype('float32'))

        # Sauvegarde métadonnées
        self.metadata = {
            'entries': entries,
            'dimension': dimension,
            'model_name': self.model_name,
            'created_at': pd.Timestamp.now().isoformat() if 'pd' in globals() else 'unknown',
            'total_entries': len(entries)
        }

        # Sauvegarde sur disque
        self.save_index()

        print(f"[SemanticSearch] Index créé: {len(entries)} vecteurs, dimension {dimension}")

    def save_index(self):
        """Sauvegarde index FAISS et métadonnées"""
        if self.index is None:
            print("[SemanticSearch] WARN: Aucun index à sauvegarder")
            return

        try:
            # Sauvegarde FAISS index
            faiss.write_index(self.index, str(self.index_path))

            # Sauvegarde métadonnées (pickle)
            with open(self.metadata_path, 'wb') as f:
                pickle.dump(self.metadata, f)

            print(f"[SemanticSearch] Index sauvegardé: {self.index_path}")
        except Exception as e:
            print(f"[SemanticSearch] ERROR saving index: {e}")

    def load_index(self):
        """Charge index FAISS et métadonnées depuis disque"""
        try:
            # Charge FAISS index
            self.index = faiss.read_index(str(self.index_path))

            # Charge métadonnées
            with open(self.metadata_path, 'rb') as f:
                self.metadata = pickle.load(f)

            print(f"[SemanticSearch] Index chargé: {self.metadata.get('total_entries', 0)} entrées")
        except Exception as e:
            print(f"[SemanticSearch] ERROR loading index: {e}")
            self.index = None
            self.metadata = None

    def search(self, query: str, top_k: int = 20, min_score: float = 0.1) -> List[Dict]:
        """
        Recherche sémantique

        Args:
            query: Query utilisateur
            top_k: Nombre de résultats max
            min_score: Score minimum (cosine similarity)

        Returns:
            Liste résultats avec scores
        """
        if self.index is None:
            print("[SemanticSearch] WARN: Index non chargé")
            return []

        # 1. Encode query (avec cache)
        query_embedding = self._get_query_embedding(query)

        # 2. Recherche FAISS
        scores, indices = self.index.search(query_embedding.reshape(1, -1), top_k)

        # 3. Format résultats
        results = []
        entries = self.metadata.get('entries', [])

        for idx, score in zip(indices[0], scores[0]):
            if idx < len(entries) and score >= min_score:
                entry = entries[idx].copy()
                entry['semantic_score'] = float(score)

                # Bonus keyword matching
                query_lower = query.lower()
                keywords = entry.get('keywords', [])
                keyword_matches = sum(1 for kw in keywords if kw.lower() in query_lower)
                entry['keyword_bonus'] = keyword_matches * 0.15

                # Score final
                entry['final_score'] = entry['semantic_score'] + entry['keyword_bonus']

                results.append(entry)

        # Tri par score final
        results.sort(key=lambda x: x['final_score'], reverse=True)

        return results

    def _get_query_embedding(self, query: str) -> np.ndarray:
        """
        Encode query en vecteur (avec cache)

        Args:
            query: Query utilisateur

        Returns:
            Vecteur numpy normalisé
        """
        # Cache key
        cache_key = hashlib.md5(query.encode('utf-8')).hexdigest()

        # Check cache
        if cache_key in self.query_cache:
            return self.query_cache[cache_key]

        # Encode
        embedding = self.model.encode([query], convert_to_numpy=True)[0]

        # Normalisation pour cosine similarity
        embedding = embedding / np.linalg.norm(embedding)

        # Cache (avec limite taille)
        if len(self.query_cache) >= self.cache_max_size:
            # Éviction simple: vider si plein
            self.query_cache.clear()

        self.query_cache[cache_key] = embedding

        return embedding

    def get_stats(self) -> Dict:
        """Statistiques index"""
        if self.index is None or self.metadata is None:
            return {
                'status': 'not_loaded',
                'total_entries': 0
            }

        return {
            'status': 'loaded',
            'total_entries': self.metadata.get('total_entries', 0),
            'dimension': self.metadata.get('dimension', 0),
            'model_name': self.metadata.get('model_name', 'unknown'),
            'index_file_size_mb': self.index_path.stat().st_size / (1024**2) if self.index_path.exists() else 0,
            'cache_size': len(self.query_cache)
        }


# Test rapide
if __name__ == "__main__":
    print("=== Test SemanticSearchEngine ===\n")

    # Chargement KB
    kb_path = Path("data/knowledge/core_kb.json")
    if not kb_path.exists():
        print(f"ERROR: KB non trouvé: {kb_path}")
        exit(1)

    with open(kb_path, 'r', encoding='utf-8') as f:
        kb_data = json.load(f)

    print(f"KB chargé: {len(kb_data.get('entries', []))} entrées\n")

    # Init engine
    engine = SemanticSearchEngine()

    # Création index si nécessaire
    if engine.index is None:
        print("Création index (première fois, ~1-2 min)...\n")
        engine.build_index(kb_data)

    # Stats
    stats = engine.get_stats()
    print(f"\n=== Stats ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    # Test recherche
    queries = [
        "température cpu élevée",
        "rtx 4090 câble alimentation",
        "ddr5 xmp activation"
    ]

    for query in queries:
        print(f"\n=== Query: '{query}' ===")
        results = engine.search(query, top_k=3)

        for i, res in enumerate(results, 1):
            print(f"\n{i}. Score: {res['final_score']:.3f} (semantic: {res['semantic_score']:.3f}, keyword: {res['keyword_bonus']:.2f})")
            print(f"   Titre: {res.get('title', 'N/A')[:100]}")
            print(f"   ID: {res.get('id', 'N/A')}")
