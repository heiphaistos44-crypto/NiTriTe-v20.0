#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart Cache Manager - Cache intelligent 3 niveaux pour AI Agent
L1: RAM (LRU, ultra-rapide)
L2: SQLite (persistant, moyen terme)
L3: Embeddings (similarité sémantique)
"""

import sqlite3
import hashlib
import json
import time
from typing import Optional, Dict, List, Tuple
from pathlib import Path
from collections import OrderedDict
from datetime import datetime, timedelta
from v14_mvp.logger_system import logger


class LRUCache:
    """Cache LRU simple en mémoire (L1)"""

    def __init__(self, capacity: int = 100):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[str]:
        """Récupère une valeur du cache"""
        if key in self.cache:
            # Déplacer en fin (= récemment utilisé)
            self.cache.move_to_end(key)
            self.hits += 1
            return self.cache[key]

        self.misses += 1
        return None

    def put(self, key: str, value: str):
        """Ajoute une valeur au cache"""
        if key in self.cache:
            # Déjà présent, déplacer en fin
            self.cache.move_to_end(key)
        else:
            # Nouveau, ajouter
            self.cache[key] = value

            # Éviction si capacité dépassée
            if len(self.cache) > self.capacity:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
                logger.debug("Cache_L1", f"Éviction: {oldest_key[:50]}...")

    def clear(self):
        """Vide le cache"""
        self.cache.clear()
        self.hits = 0
        self.misses = 0

    def get_stats(self) -> Dict:
        """Statistiques du cache"""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0

        return {
            "size": len(self.cache),
            "capacity": self.capacity,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.1f}%"
        }


class SQLiteCache:
    """Cache persistant SQLite (L2)"""

    def __init__(self, db_path: str = "data/cache/ai_responses.db", max_entries: int = 10000, expiration_days: int = 30):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.max_entries = max_entries
        self.expiration_days = expiration_days

        self._init_database()
        self._cleanup_expired()

    def _init_database(self):
        """Initialise la base de données"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    query TEXT NOT NULL,
                    response TEXT NOT NULL,
                    model TEXT,
                    timestamp INTEGER NOT NULL,
                    hit_count INTEGER DEFAULT 1,
                    metadata TEXT
                )
            """)

            # Index pour recherche rapide
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_timestamp
                ON cache(timestamp DESC)
            """)

            conn.commit()

        logger.info("Cache_L2", f"DB initialisée: {self.db_path}")

    def get(self, key: str) -> Optional[Dict]:
        """Récupère une entrée du cache"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT query, response, model, timestamp, hit_count, metadata
                FROM cache
                WHERE key = ?
            """, (key,))

            row = cursor.fetchone()

            if row:
                # Incrémenter hit_count
                conn.execute("""
                    UPDATE cache
                    SET hit_count = hit_count + 1
                    WHERE key = ?
                """, (key,))
                conn.commit()

                return {
                    "query": row[0],
                    "response": row[1],
                    "model": row[2],
                    "timestamp": row[3],
                    "hit_count": row[4] + 1,
                    "metadata": json.loads(row[5]) if row[5] else {}
                }

            return None

    def put(self, key: str, query: str, response: str, model: str = None, metadata: Dict = None):
        """Ajoute une entrée au cache"""
        timestamp = int(time.time())
        metadata_json = json.dumps(metadata) if metadata else None

        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO cache
                (key, query, response, model, timestamp, hit_count, metadata)
                VALUES (?, ?, ?, ?, ?, 1, ?)
            """, (key, query, response, model, timestamp, metadata_json))

            conn.commit()

        # Vérifier si besoin d'éviction
        self._evict_if_needed()

    def _evict_if_needed(self):
        """Éviction LRU si trop d'entrées"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT COUNT(*) FROM cache")
            count = cursor.fetchone()[0]

            if count > self.max_entries:
                # Supprimer les entrées les moins utilisées et les plus anciennes
                to_delete = count - self.max_entries

                conn.execute("""
                    DELETE FROM cache
                    WHERE key IN (
                        SELECT key FROM cache
                        ORDER BY hit_count ASC, timestamp ASC
                        LIMIT ?
                    )
                """, (to_delete,))

                conn.commit()
                logger.info("Cache_L2", f"Éviction: {to_delete} entrées supprimées")

    def _cleanup_expired(self):
        """Supprime les entrées expirées"""
        expiration_timestamp = int((datetime.now() - timedelta(days=self.expiration_days)).timestamp())

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                DELETE FROM cache
                WHERE timestamp < ?
            """, (expiration_timestamp,))

            deleted = cursor.rowcount
            conn.commit()

            if deleted > 0:
                logger.info("Cache_L2", f"Nettoyage: {deleted} entrées expirées supprimées")

    def get_stats(self) -> Dict:
        """Statistiques du cache"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT
                    COUNT(*) as total,
                    SUM(hit_count) as total_hits,
                    AVG(hit_count) as avg_hits_per_entry
                FROM cache
            """)

            row = cursor.fetchone()

            return {
                "entries": row[0],
                "max_entries": self.max_entries,
                "total_hits": row[1] or 0,
                "avg_hits_per_entry": f"{row[2] or 0:.1f}",
                "db_size_mb": f"{self.db_path.stat().st_size / 1024 / 1024:.2f}" if self.db_path.exists() else "0"
            }

    def search_by_query(self, query_fragment: str, limit: int = 10) -> List[Dict]:
        """Recherche dans le cache par fragment de query"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT key, query, response, model, timestamp, hit_count
                FROM cache
                WHERE query LIKE ?
                ORDER BY hit_count DESC, timestamp DESC
                LIMIT ?
            """, (f"%{query_fragment}%", limit))

            results = []
            for row in cursor.fetchall():
                results.append({
                    "key": row[0],
                    "query": row[1],
                    "response": row[2][:200] + "...",  # Tronquer réponse
                    "model": row[3],
                    "timestamp": row[4],
                    "hit_count": row[5]
                })

            return results


class SmartCacheManager:
    """Gestionnaire de cache intelligent multi-niveaux"""

    def __init__(self, l1_capacity: int = 100, l2_max_entries: int = 10000):
        # L1: Cache RAM (ultra-rapide)
        self.l1_cache = LRUCache(capacity=l1_capacity)

        # L2: Cache SQLite (persistant)
        self.l2_cache = SQLiteCache(max_entries=l2_max_entries)

        # Statistiques globales
        self.total_requests = 0
        self.l1_hits = 0
        self.l2_hits = 0
        self.misses = 0

        logger.info("SmartCache", "Gestionnaire multi-niveaux initialisé")

    def _generate_key(self, query: str, model: str = None) -> str:
        """Génère une clé unique pour une query"""
        content = f"{query}|{model or 'default'}"
        return hashlib.sha256(content.encode()).hexdigest()

    def get(self, query: str, model: str = None) -> Optional[str]:
        """
        Récupère une réponse du cache (L1 → L2)

        Args:
            query: Query utilisateur
            model: Modèle utilisé (optionnel)

        Returns:
            str: Réponse cachée ou None
        """
        self.total_requests += 1
        key = self._generate_key(query, model)

        # Recherche L1 (RAM)
        response = self.l1_cache.get(key)
        if response:
            self.l1_hits += 1
            logger.debug("SmartCache", f"[L1 HIT] {query[:50]}...")
            return response

        # Recherche L2 (SQLite)
        cache_entry = self.l2_cache.get(key)
        if cache_entry:
            response = cache_entry['response']
            self.l2_hits += 1
            logger.debug("SmartCache", f"[L2 HIT] {query[:50]}...")

            # Promouvoir en L1 pour accès futurs
            self.l1_cache.put(key, response)
            return response

        # Miss complet
        self.misses += 1
        logger.debug("SmartCache", f"[MISS] {query[:50]}...")
        return None

    def put(self, query: str, response: str, model: str = None, metadata: Dict = None):
        """
        Met en cache une réponse (L1 + L2)

        Args:
            query: Query utilisateur
            response: Réponse à cacher
            model: Modèle utilisé
            metadata: Métadonnées additionnelles
        """
        key = self._generate_key(query, model)

        # Stocker dans L1 (RAM)
        self.l1_cache.put(key, response)

        # Stocker dans L2 (SQLite)
        self.l2_cache.put(key, query, response, model, metadata)

        logger.debug("SmartCache", f"[STORED] {query[:50]}...")

    def clear_all(self):
        """Vide tous les caches"""
        self.l1_cache.clear()
        # Note: L2 n'a pas de clear complet pour sécurité

        logger.warning("SmartCache", "L1 cache vidé")

    def get_stats(self) -> Dict:
        """Statistiques complètes du cache"""
        hit_rate = ((self.l1_hits + self.l2_hits) / self.total_requests * 100) if self.total_requests > 0 else 0

        return {
            "global": {
                "total_requests": self.total_requests,
                "l1_hits": self.l1_hits,
                "l2_hits": self.l2_hits,
                "misses": self.misses,
                "hit_rate": f"{hit_rate:.1f}%"
            },
            "l1": self.l1_cache.get_stats(),
            "l2": self.l2_cache.get_stats()
        }

    def print_stats(self):
        """Affiche les statistiques de façon formatée"""
        stats = self.get_stats()

        print("\n" + "="*60)
        print("SMART CACHE - STATISTIQUES")
        print("="*60)

        print("\n📊 GLOBAL:")
        print(f"  Total requêtes:  {stats['global']['total_requests']}")
        print(f"  L1 hits:         {stats['global']['l1_hits']}")
        print(f"  L2 hits:         {stats['global']['l2_hits']}")
        print(f"  Misses:          {stats['global']['misses']}")
        print(f"  Hit rate:        {stats['global']['hit_rate']}")

        print("\n💾 L1 (RAM):")
        print(f"  Taille:          {stats['l1']['size']}/{stats['l1']['capacity']}")
        print(f"  Hit rate L1:     {stats['l1']['hit_rate']}")

        print("\n💿 L2 (SQLite):")
        print(f"  Entrées:         {stats['l2']['entries']}/{stats['l2']['max_entries']}")
        print(f"  Total hits:      {stats['l2']['total_hits']}")
        print(f"  Hits moyens:     {stats['l2']['avg_hits_per_entry']}")
        print(f"  Taille DB:       {stats['l2']['db_size_mb']} MB")

        print("="*60 + "\n")


# Singleton pour accès global
_cache_manager_instance = None

def get_cache_manager() -> SmartCacheManager:
    """Retourne l'instance singleton du SmartCacheManager"""
    global _cache_manager_instance
    if _cache_manager_instance is None:
        _cache_manager_instance = SmartCacheManager()
    return _cache_manager_instance


if __name__ == "__main__":
    # Tests
    print("=== Smart Cache Manager - Tests ===\n")

    cache = get_cache_manager()

    # Test 1: Store & Retrieve
    print("Test 1: Store & Retrieve")
    query1 = "Comment optimiser Windows pour le gaming?"
    response1 = "Voici 3 étapes: 1) Désactiver services inutiles, 2) Mode performances, 3) Optimiser GPU"

    cache.put(query1, response1, model="llama3:8b")
    print(f"✓ Stored: {query1[:50]}...")

    # Récupération L1
    result = cache.get(query1)
    assert result == response1, "L1 cache failed"
    print(f"✓ Retrieved from L1: {result[:50]}...")

    # Test 2: L2 retrieval (vider L1 d'abord)
    print("\nTest 2: L2 Retrieval")
    cache.l1_cache.clear()
    result = cache.get(query1)
    assert result == response1, "L2 cache failed"
    print(f"✓ Retrieved from L2: {result[:50]}...")

    # Test 3: Cache miss
    print("\nTest 3: Cache Miss")
    result = cache.get("Query jamais vue avant")
    assert result is None, "Should be cache miss"
    print("✓ Cache miss détecté correctement")

    # Test 4: Multiple queries
    print("\nTest 4: Multiple Queries")
    for i in range(10):
        cache.put(f"Query {i}", f"Response {i}", model="test")

    print(f"✓ Stored 10 queries")

    # Stats finales
    cache.print_stats()

    # Test 5: Search
    print("\nTest 5: Search by Query Fragment")
    results = cache.l2_cache.search_by_query("optimiser")
    print(f"✓ Found {len(results)} results for 'optimiser'")
    for r in results:
        print(f"  - {r['query'][:60]}... (hits: {r['hit_count']})")

    print("\n✓ Tous les tests réussis!")
