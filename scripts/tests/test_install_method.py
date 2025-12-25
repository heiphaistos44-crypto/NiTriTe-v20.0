#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de test pour vérifier la détection automatique de la méthode d'installation"""

import json

def detect_install_method(app_data):
    """
    Déterminer la méthode d'installation intelligemment
    (Copie de la logique dans pages_optimized.py)
    """
    has_winget_id = 'winget_id' in app_data or 'id' in app_data
    has_download_url = 'download_url' in app_data

    if 'install_method' in app_data:
        # Méthode explicite définie
        method = app_data['install_method']
        reason = "Methode explicite definie"
    elif has_winget_id:
        # A un winget_id => utiliser WinGet
        method = 'winget'
        reason = "WinGet ID disponible"
    elif has_download_url:
        # A un download_url mais pas de winget_id => téléchargement direct
        method = 'download'
        reason = "Download URL sans WinGet ID"
    else:
        # Aucune info => essayer WinGet par défaut
        method = 'winget'
        reason = "Par defaut (aucune info)"

    return method, reason

# Charger les données
with open('data/programs.json', 'r', encoding='utf-8') as f:
    programs_data = json.load(f)

print("=" * 80)
print("TEST DE DETECTION AUTOMATIQUE DE LA METHODE D'INSTALLATION")
print("=" * 80)
print()

# Statistiques
stats = {
    'winget': 0,
    'download': 0,
    'chocolatey': 0,
    'other': 0
}

# Tester quelques applications
test_apps = []
categories_to_check = ['Navigateurs', 'Outils OrdiPlus', 'Office']

for category in categories_to_check:
    if category in programs_data:
        for app_name, app_data in list(programs_data[category].items())[:5]:
            method, reason = detect_install_method(app_data)
            test_apps.append({
                'name': app_name,
                'category': category,
                'method': method,
                'reason': reason,
                'has_winget_id': 'winget_id' in app_data,
                'has_download_url': 'download_url' in app_data,
                'is_portable': app_data.get('portable', False)
            })

# Afficher les résultats
print("EXEMPLES D'APPLICATIONS:")
print("-" * 80)
for app in test_apps:
    print(f"\nApp: {app['name']}")
    print(f"  Categorie: {app['category']}")
    print(f"  WinGet ID: {'OUI' if app['has_winget_id'] else 'NON'}")
    print(f"  Download URL: {'OUI' if app['has_download_url'] else 'NON'}")
    print(f"  Portable: {'OUI' if app['is_portable'] else 'NON'}")
    print(f"  --> METHODE: {app['method'].upper()}")
    print(f"  --> Raison: {app['reason']}")

# Statistiques globales
print("\n" + "=" * 80)
print("STATISTIQUES GLOBALES:")
print("-" * 80)

for category, apps in programs_data.items():
    for app_name, app_data in apps.items():
        method, _ = detect_install_method(app_data)
        if method in stats:
            stats[method] += 1
        else:
            stats['other'] += 1

total = sum(stats.values())
print(f"\nTotal applications: {total}")
print(f"  - WinGet:        {stats['winget']:4d} ({stats['winget']*100//total}%)")
print(f"  - Download:      {stats['download']:4d} ({stats['download']*100//total}%)")
print(f"  - Chocolatey:    {stats['chocolatey']:4d} ({stats['chocolatey']*100//total}%)")
print(f"  - Autre:         {stats['other']:4d} ({stats['other']*100//total}%)")

print("\n" + "=" * 80)
print("AVANT LE CORRECTIF:")
print("  - Toutes les apps sans winget_id essayaient d'utiliser WinGet")
print("  - Resultat: erreur 'ne peut pas s'installer sur ce PC'")
print("\nAPRES LE CORRECTIF:")
print(f"  - {stats['download']} apps utilisent maintenant le telechargement direct")
print("  - Ces apps seront telechargees et installees correctement")
print("=" * 80)
