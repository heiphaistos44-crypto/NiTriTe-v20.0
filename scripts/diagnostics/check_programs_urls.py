#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour vérifier les URLs cassées dans programs.json"""

import json
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def check_url(url, timeout=10):
    """Vérifier si une URL est accessible"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)
        return response.status_code
    except requests.exceptions.Timeout:
        return 'TIMEOUT'
    except requests.exceptions.ConnectionError:
        return 'CONNECTION_ERROR'
    except requests.exceptions.TooManyRedirects:
        return 'TOO_MANY_REDIRECTS'
    except Exception as e:
        return f'ERROR: {str(e)[:50]}'

def check_programs_urls(category_filter=None):
    """Vérifier toutes les URLs dans programs.json"""
    print("=" * 100)
    print("VERIFICATION DES URLS DANS PROGRAMS.JSON")
    print("=" * 100)
    print()

    # Charger le JSON
    json_path = Path("data/programs.json")
    if not json_path.exists():
        print(f"[ERROR] Fichier non trouve: {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collecter toutes les URLs à vérifier
    urls_to_check = []
    for category, apps in data.items():
        # Filtrer par catégorie si spécifié
        if category_filter and category_filter.lower() not in category.lower():
            continue

        for app_name, app_info in apps.items():
            url = app_info.get('download_url') or app_info.get('url')
            if url:
                urls_to_check.append({
                    'category': category,
                    'app': app_name,
                    'url': url
                })

    print(f"[CHECK] {len(urls_to_check)} URLs a verifier...")
    if category_filter:
        print(f"   Filtre: categories contenant '{category_filter}'")
    print()

    # Vérifier les URLs en parallèle
    broken_urls = []
    working_urls = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        # Créer les futures
        future_to_url = {}
        for item in urls_to_check:
            future = executor.submit(check_url, item['url'])
            future_to_url[future] = item

        # Traiter les résultats
        for i, future in enumerate(as_completed(future_to_url), 1):
            item = future_to_url[future]
            status_code = future.result()

            # Afficher progression
            print(f"[{i}/{len(urls_to_check)}] ", end="", flush=True)

            if isinstance(status_code, int) and status_code < 400:
                print(f"[OK] {item['app'][:40]:<40} ({status_code})")
                working_urls.append(item)
            else:
                print(f"[FAIL] {item['app'][:40]:<40} ({status_code})")
                broken_urls.append({
                    'name': item['app'],
                    'category': item['category'],
                    'url': item['url'],
                    'status': status_code
                })

            # Petite pause pour éviter rate limiting
            time.sleep(0.1)

    # Afficher resume
    print()
    print("=" * 100)
    print("RESULTATS")
    print("=" * 100)
    print(f"[OK] URLs fonctionnelles: {len(working_urls)}")
    print(f"[FAIL] URLs cassees: {len(broken_urls)}")
    print()

    if broken_urls:
        print("=" * 100)
        print("URLS CASSEES DETAILLEES")
        print("=" * 100)
        print()

        # Sauvegarder dans un fichier JSON
        output_file = Path("broken_programs_urls.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(broken_urls, f, indent=2, ensure_ascii=False)

        print(f"[FILE] Liste sauvegardee dans: {output_file}")
        print()

        # Afficher les URLs cassées par catégorie
        categories = {}
        for item in broken_urls:
            cat = item['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item)

        for category, items in sorted(categories.items()):
            print(f"\n[{category}] ({len(items)} URL(s) cassee(s)):")
            for item in items:
                print(f"   - {item['name']}")
                print(f"     URL: {item['url'][:80]}...")
                print(f"     Statut: {item['status']}")

if __name__ == "__main__":
    import sys

    # Si un argument est fourni, l'utiliser comme filtre de catégorie
    category_filter = sys.argv[1] if len(sys.argv) > 1 else None

    check_programs_urls(category_filter)
