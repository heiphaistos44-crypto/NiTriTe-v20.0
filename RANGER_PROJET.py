#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de rangement du projet NiTriTe V20.0
Nettoie la racine du projet en déplaçant les fichiers temporaires
"""

import os
import shutil
from pathlib import Path

# Fichiers/dossiers à GARDER à la racine
GARDER = {
    # Fichiers
    'LANCER_NITRITE_V20.bat',
    'README.md',
    '.gitignore',
    'requirements.txt',
    'NiTriTe_V20_Portable.spec',

    # Dossiers essentiels
    'dist',
    'build',
    'logiciel',
    'Script Windows',
    'Drivers',
    'src',
    'data',
    'config',
    'assets',

    # Git
    '.git',
    '.gitignore',
    '.claude',

    # Ce script lui-même
    'RANGER_PROJET.py'
}

# Dossiers de destination
DOSSIERS_ARCHIVE = {
    '_scripts_temp': ['.py'],  # Tous les scripts Python temporaires
    '_rapports': ['.md'],      # Tous les rapports markdown (sauf README.md)
    '_builds_anciens': ['.7z', '.zip'],  # Archives de builds
    '_json_temp': ['.json'],   # Fichiers JSON temporaires
    '_logs': ['.log', '.txt'], # Fichiers de log et txt
}

def creer_dossiers_archive():
    """Créer les dossiers d'archive s'ils n'existent pas"""
    for dossier in DOSSIERS_ARCHIVE.keys():
        Path(dossier).mkdir(exist_ok=True)
        print(f"[OK] Dossier cree: {dossier}/")

def est_a_garder(nom_fichier):
    """Vérifier si un fichier/dossier doit être gardé"""
    return nom_fichier in GARDER or nom_fichier.startswith('.')

def deplacer_fichier(fichier_path, dossier_dest):
    """Déplacer un fichier vers un dossier de destination"""
    try:
        dest_path = Path(dossier_dest) / fichier_path.name

        # Si le fichier existe déjà, ajouter un suffixe
        if dest_path.exists():
            base = dest_path.stem
            ext = dest_path.suffix
            i = 1
            while dest_path.exists():
                dest_path = Path(dossier_dest) / f"{base}_{i}{ext}"
                i += 1

        shutil.move(str(fichier_path), str(dest_path))
        return True
    except Exception as e:
        print(f"[X] Erreur deplacement {fichier_path.name}: {e}")
        return False

def ranger_projet():
    """Ranger le projet"""
    print("=" * 70)
    print("RANGEMENT DU PROJET NITRITE V20.0")
    print("=" * 70)
    print()

    # Créer les dossiers d'archive
    creer_dossiers_archive()
    print()

    racine = Path('.')
    fichiers_deplaces = {key: 0 for key in DOSSIERS_ARCHIVE.keys()}
    fichiers_gardes = []

    # Lister tous les fichiers à la racine
    for item in racine.iterdir():
        # Ignorer les dossiers sauf s'ils doivent être archivés
        if item.is_dir():
            # Déplacer les dossiers temporaires
            if item.name.startswith('test_') or item.name in ['test_download', 'test_portable', 'test_portable_release', 'test_reports', 'test_installation_env']:
                try:
                    dest = Path('_scripts_temp') / item.name
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.move(str(item), str(dest))
                    fichiers_deplaces['_scripts_temp'] += 1
                    print(f"[DIR] Dossier deplace: {item.name}/ -> _scripts_temp/")
                except Exception as e:
                    print(f"[X] Erreur dossier {item.name}: {e}")
            continue

        # Fichiers
        if est_a_garder(item.name):
            fichiers_gardes.append(item.name)
            continue

        # Déterminer où déplacer le fichier
        extension = item.suffix.lower()
        deplace = False

        for dossier, extensions in DOSSIERS_ARCHIVE.items():
            if extension in extensions:
                # Exception: garder README.md
                if item.name == 'README.md':
                    fichiers_gardes.append(item.name)
                    break

                if deplacer_fichier(item, dossier):
                    fichiers_deplaces[dossier] += 1
                    print(f"[FILE] {item.name} -> {dossier}/")
                    deplace = True
                    break

        if not deplace and item.exists():
            # Fichiers sans catégorie spécifique → _scripts_temp
            if deplacer_fichier(item, '_scripts_temp'):
                fichiers_deplaces['_scripts_temp'] += 1
                print(f"[FILE] {item.name} -> _scripts_temp/")

    # Rapport final
    print()
    print("=" * 70)
    print("RAPPORT DE RANGEMENT")
    print("=" * 70)
    print()

    print("[OK] FICHIERS/DOSSIERS GARDES A LA RACINE:")
    for nom in sorted(fichiers_gardes):
        print(f"   - {nom}")
    print()

    print("[ARCHIVE] FICHIERS DEPLACES:")
    total_deplaces = 0
    for dossier, count in fichiers_deplaces.items():
        if count > 0:
            print(f"   - {dossier}/: {count} fichier(s)")
            total_deplaces += count
    print()

    print(f"[STATS] TOTAL: {total_deplaces} fichier(s)/dossier(s) deplace(s)")
    print()
    print("[OK] RANGEMENT TERMINE!")
    print()
    print("Structure actuelle de la racine:")
    print("  |- LANCER_NITRITE_V20.bat")
    print("  |- README.md")
    print("  |- dist/")
    print("  |- logiciel/")
    print("  |- Script Windows/")
    print("  |- Drivers/")
    print("  |- src/")
    print("  |- data/")
    print("  \- ...")
    print()

if __name__ == "__main__":
    try:
        confirmation = input("ATTENTION - Voulez-vous vraiment ranger le projet? (o/N): ")
        if confirmation.lower() in ['o', 'y', 'oui', 'yes']:
            ranger_projet()
        else:
            print("[X] Rangement annule")
    except KeyboardInterrupt:
        print("\n[X] Rangement annule par l'utilisateur")
    except Exception as e:
        print(f"\n[X] Erreur: {e}")
        import traceback
        traceback.print_exc()
