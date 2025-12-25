#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG System (Retrieval-Augmented Generation)
Système de recherche web en temps réel pour augmenter les réponses de l'agent IA
Utilise DuckDuckGo Search API (gratuit, pas de clé requise)
"""

import requests
import json
from typing import List, Dict, Optional
from urllib.parse import quote_plus
import time

class RAGSystem:
    """
    Système RAG pour enrichir les réponses avec des informations web actuelles
    """

    def __init__(self):
        self.search_engines = {
            "duckduckgo": {
                "name": "DuckDuckGo",
                "url": "https://api.duckduckgo.com/",
                "enabled": True,
                "free": True
            },
            "duckduckgo_html": {
                "name": "DuckDuckGo HTML",
                "url": "https://html.duckduckgo.com/html/",
                "enabled": True,
                "free": True
            }
        }

        self.max_results = 5
        self.timeout = 10

    def search_web(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Recherche web avec fallback sur plusieurs moteurs

        Args:
            query: Requête de recherche
            max_results: Nombre maximum de résultats

        Returns:
            Liste de résultats avec {title, url, snippet}
        """
        # Essayer DuckDuckGo instant answer API d'abord
        results = self._search_duckduckgo_instant(query)

        if not results or len(results) < max_results:
            # Fallback: parser HTML DuckDuckGo (plus fiable)
            html_results = self._search_duckduckgo_html(query, max_results)
            if html_results:
                results.extend(html_results)

        # Limiter au nombre demandé
        return results[:max_results]

    def _search_duckduckgo_instant(self, query: str) -> List[Dict[str, str]]:
        """
        Recherche avec DuckDuckGo Instant Answer API (gratuit, officiel)
        """
        try:
            params = {
                "q": query,
                "format": "json",
                "no_html": "1",
                "skip_disambig": "1"
            }

            response = requests.get(
                self.search_engines["duckduckgo"]["url"],
                params=params,
                timeout=self.timeout,
                headers={"User-Agent": "NiTriTe-AI-Agent/1.0"}
            )

            if response.status_code != 200:
                return []

            data = response.json()
            results = []

            # Abstract (réponse directe)
            if data.get("AbstractText"):
                results.append({
                    "title": data.get("Heading", "DuckDuckGo Answer"),
                    "url": data.get("AbstractURL", ""),
                    "snippet": data.get("AbstractText", "")
                })

            # Related Topics
            for topic in data.get("RelatedTopics", [])[:3]:
                if isinstance(topic, dict) and "Text" in topic:
                    results.append({
                        "title": topic.get("Text", "")[:100],
                        "url": topic.get("FirstURL", ""),
                        "snippet": topic.get("Text", "")
                    })

            return results

        except Exception as e:
            print(f"DuckDuckGo Instant API error: {e}")
            return []

    def _search_duckduckgo_html(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Recherche en parsant le HTML de DuckDuckGo (fallback)
        Note: Simple parsing, peut casser si DuckDuckGo change leur HTML
        """
        try:
            # Construire URL de recherche
            search_url = f"https://lite.duckduckgo.com/lite/?q={quote_plus(query)}"

            response = requests.get(
                search_url,
                timeout=self.timeout,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
            )

            if response.status_code != 200:
                return []

            # Parser HTML simple (chercher les liens et snippets)
            html = response.text
            results = []

            # Méthode simple: chercher les patterns de résultats
            # Format DuckDuckGo Lite: <a rel="nofollow" href="URL">Title</a>
            import re

            # Trouver tous les liens avec snippets
            link_pattern = r'<a rel="nofollow" href="([^"]+)">([^<]+)</a>'
            snippet_pattern = r'<td class="result-snippet">([^<]+)</td>'

            links = re.findall(link_pattern, html)
            snippets = re.findall(snippet_pattern, html)

            for i, (url, title) in enumerate(links[:max_results]):
                snippet = snippets[i] if i < len(snippets) else ""

                # Filtrer les résultats internes DuckDuckGo
                if "duckduckgo.com" not in url:
                    results.append({
                        "title": title.strip(),
                        "url": url.strip(),
                        "snippet": snippet.strip()
                    })

            return results[:max_results]

        except Exception as e:
            print(f"DuckDuckGo HTML parsing error: {e}")
            return []

    def should_use_rag(self, user_query: str, local_response: str) -> bool:
        """
        Déterminer si on doit utiliser RAG (recherche web)

        Critères:
        - Réponse locale trop courte ou générique
        - Question contient des mots-clés temporels (2024, 2025, latest, nouveau)
        - Question sur des specs hardware récentes
        - Réponse locale contient "je ne sais pas" ou équivalent
        """
        query_lower = user_query.lower()
        response_lower = local_response.lower()

        # Mots-clés indiquant besoin de recherche web
        temporal_keywords = ["2024", "2025", "latest", "nouveau", "récent", "actuel", "dernier"]
        uncertainty_keywords = ["ne sais pas", "pas sûr", "peut-être", "probablement"]

        # Check si question temporelle
        if any(keyword in query_lower for keyword in temporal_keywords):
            return True

        # Check si réponse incertaine
        if any(keyword in response_lower for keyword in uncertainty_keywords):
            return True

        # Check si réponse trop courte (probable manque d'info)
        if len(local_response) < 100:
            return True

        return False

    def augment_response(self, user_query: str, local_response: str, api_manager=None) -> str:
        """
        Augmenter la réponse locale avec des informations web

        Args:
            user_query: Question de l'utilisateur
            local_response: Réponse générée localement
            api_manager: APIManager pour reformuler les résultats (optionnel)

        Returns:
            Réponse augmentée avec sources web
        """
        # Faire recherche web
        search_results = self.search_web(user_query, max_results=5)

        if not search_results:
            return local_response  # Pas de résultats, retourner réponse locale

        # Construire contexte web
        web_context = "\n\n📚 **Informations complémentaires du web:**\n\n"

        for i, result in enumerate(search_results, 1):
            web_context += f"{i}. **{result['title']}**\n"
            if result['snippet']:
                web_context += f"   {result['snippet'][:200]}...\n"
            if result['url']:
                web_context += f"   🔗 Source: {result['url']}\n"
            web_context += "\n"

        # Si APIManager disponible, reformuler avec contexte web
        if api_manager:
            try:
                synthesis_prompt = f"""En tant qu'expert, synthétise une réponse complète en combinant:

RÉPONSE LOCALE:
{local_response}

INFORMATIONS WEB RÉCENTES:
{web_context}

QUESTION: {user_query}

Fournis une réponse unifiée et détaillée qui combine le meilleur des deux sources.
Cite les sources web pertinentes."""

                augmented, api_used = api_manager.query(
                    user_message=synthesis_prompt,
                    temperature=0.7,
                    max_tokens=1500
                )

                if augmented:
                    return augmented

            except Exception as e:
                print(f"Erreur synthesis RAG: {e}")

        # Fallback: concatener simplement
        return local_response + "\n\n" + web_context

    def get_stats(self) -> Dict:
        """Statistiques du système RAG"""
        return {
            "search_engines": len(self.search_engines),
            "enabled_engines": sum(1 for e in self.search_engines.values() if e["enabled"]),
            "free_engines": sum(1 for e in self.search_engines.values() if e["free"])
        }


# Test rapide
if __name__ == "__main__":
    rag = RAGSystem()

    print("🔍 Test RAG System\n")

    # Test recherche
    query = "RTX 4070 vs RTX 4070 Ti SUPER performance"
    print(f"Query: {query}\n")

    results = rag.search_web(query, max_results=3)

    if results:
        print(f"✅ Trouvé {len(results)} résultats:\n")
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']}")
            print(f"   URL: {r['url']}")
            print(f"   Snippet: {r['snippet'][:100]}...")
            print()
    else:
        print("❌ Aucun résultat trouvé")
