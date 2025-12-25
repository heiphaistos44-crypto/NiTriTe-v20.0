#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour analyser les applications sans winget_id"""

import json

with open('data/programs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

apps_without_winget = []
apps_with_download_only = []

for category, apps in data.items():
    for app_name, app_data in apps.items():
        is_portable = app_data.get('portable', False)
        has_winget_id = 'winget_id' in app_data
        has_download_url = 'download_url' in app_data
        install_method = app_data.get('install_method', 'winget')

        if not has_winget_id and not is_portable:
            apps_without_winget.append({
                'name': app_name,
                'category': category,
                'has_download_url': has_download_url,
                'install_method': install_method
            })

            if has_download_url and install_method == 'winget':
                apps_with_download_only.append(app_name)

print("ANALYSE DES APPLICATIONS")
print("=" * 60)
print(f"Total applications sans winget_id: {len(apps_without_winget)}")
print(f"Applications avec download_url mais method=winget: {len(apps_with_download_only)}")
print()

if apps_with_download_only:
    print("PROBLEME IDENTIFIE:")
    print("Les applications suivantes ont download_url mais essaient d'installer via WinGet:")
    print()
    for i, app_name in enumerate(apps_with_download_only[:20], 1):
        print(f"{i}. {app_name}")

    if len(apps_with_download_only) > 20:
        print(f"\n... et {len(apps_with_download_only) - 20} autres")
