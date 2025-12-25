#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour tester toutes les URLs du fichier portable_apps.json"""

import json
import requests
from pathlib import Path

# Charger le JSON
json_path = Path("data/portable_apps.json")
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=" * 80)
print("TEST DES URLS - PORTABLE APPS")
print("=" * 80)
print()

broken_urls = []
working_urls = []
redirect_urls = []
skip_count = 0

total_apps = sum(len(apps) for apps in data.values())
current = 0

for category, apps in data.items():
    print(f"\n{category}:")
    print("-" * 80)

    for app_name, app_info in apps.items():
        current += 1
        url = app_info.get('url', '')
        app_type = app_info.get('type', 'unknown')

        # Skip redirect types (pages de téléchargement manuelles)
        if app_type == 'redirect':
            print(f"  [{current}/{total_apps}] SKIP: {app_name} (page redirect)")
            redirect_urls.append({
                'name': app_name,
                'category': category,
                'url': url,
                'reason': 'Type redirect - page de téléchargement manuelle'
            })
            skip_count += 1
            continue

        # Tester l'URL
        try:
            print(f"  [{current}/{total_apps}] Test: {app_name}... ", end='', flush=True)

            # Timeout court pour accélérer
            response = requests.head(url, allow_redirects=True, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            })

            if response.status_code == 200:
                print("OK")
                working_urls.append(app_name)
            elif response.status_code == 404:
                print(f"404 NOT FOUND")
                broken_urls.append({
                    'name': app_name,
                    'category': category,
                    'url': url,
                    'status': 404
                })
            elif response.status_code == 403:
                # 403 peut juste signifier que HEAD n'est pas autorisé, essayer GET
                print(f"403 (retry GET)... ", end='', flush=True)
                response = requests.get(url, allow_redirects=True, timeout=10, stream=True, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                })
                if response.status_code == 200:
                    print("OK")
                    working_urls.append(app_name)
                else:
                    print(f"{response.status_code}")
                    broken_urls.append({
                        'name': app_name,
                        'category': category,
                        'url': url,
                        'status': response.status_code
                    })
            else:
                print(f"{response.status_code}")
                broken_urls.append({
                    'name': app_name,
                    'category': category,
                    'url': url,
                    'status': response.status_code
                })

        except requests.exceptions.Timeout:
            print("TIMEOUT")
            broken_urls.append({
                'name': app_name,
                'category': category,
                'url': url,
                'status': 'Timeout'
            })
        except requests.exceptions.ConnectionError:
            print("CONNECTION ERROR")
            broken_urls.append({
                'name': app_name,
                'category': category,
                'url': url,
                'status': 'Connection Error'
            })
        except Exception as e:
            print(f"ERROR: {str(e)[:50]}")
            broken_urls.append({
                'name': app_name,
                'category': category,
                'url': url,
                'status': f'Error: {type(e).__name__}'
            })

# Résumé
print("\n" + "=" * 80)
print("RESULTAT:")
print("=" * 80)
print(f"Total apps testees: {current}")
print(f"  - URLs OK: {len(working_urls)}")
print(f"  - URLs cassees: {len(broken_urls)}")
print(f"  - Pages redirect (skipped): {skip_count}")
print()

if broken_urls:
    print("URLS CASSEES:")
    print("-" * 80)
    for item in broken_urls:
        print(f"\n[{item['category']}] {item['name']}")
        print(f"  Status: {item['status']}")
        print(f"  URL: {item['url']}")

    # Sauvegarder dans un fichier
    with open('broken_urls.json', 'w', encoding='utf-8') as f:
        json.dump(broken_urls, f, indent=2, ensure_ascii=False)
    print(f"\nListe sauvegardee dans: broken_urls.json")
else:
    print("Aucune URL cassee trouvee!")
