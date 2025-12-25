#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Réorganisation - Nitrite V18.5
Réorganise le projet pour avoir le strict minimum à la racine
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

class ProjectReorganizer:
    """Classe pour réorganiser le projet Nitrite"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.moves = []  # Liste des déplacements effectués
        self.errors = []  # Liste des erreurs rencontrées
        self.created_dirs = []  # Liste des dossiers créés

    def create_directory_structure(self):
        """Créer la structure de dossiers nécessaire"""
        print("\n" + "=" * 60)
        print("CRÉATION DE LA STRUCTURE DE DOSSIERS")
        print("=" * 60)

        directories = [
            "scripts/diagnostics",
            "scripts/fixes",
            "scripts/tests",
            "build_tools",
            "data/config_runtime",
            "archive/launchers",
            "assets"
        ]

        for dir_path in directories:
            full_path = self.project_root / dir_path
            if not full_path.exists():
                try:
                    full_path.mkdir(parents=True, exist_ok=True)
                    self.created_dirs.append(str(dir_path))
                    print(f"  [CRÉÉ] {dir_path}")
                except Exception as e:
                    self.errors.append(f"Impossible de créer {dir_path}: {e}")
                    print(f"  [ERREUR] {dir_path}: {e}")
            else:
                print(f"  [EXISTE] {dir_path}")

    def move_file(self, source: str, destination: str, description: str = "") -> bool:
        """Déplacer un fichier avec gestion d'erreurs"""
        src_path = self.project_root / source
        dst_path = self.project_root / destination

        if not src_path.exists():
            return False

        try:
            # Créer le dossier de destination si nécessaire
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            # Déplacer le fichier
            shutil.move(str(src_path), str(dst_path))

            self.moves.append({
                "source": source,
                "destination": destination,
                "description": description
            })

            desc_text = f" - {description}" if description else ""
            print(f"  [DÉPLACÉ] {source} → {destination}{desc_text}")
            return True

        except Exception as e:
            self.errors.append(f"Impossible de déplacer {source}: {e}")
            print(f"  [ERREUR] {source}: {e}")
            return False

    def reorganize_diagnostic_scripts(self):
        """Déplacer les scripts de diagnostic"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES SCRIPTS DE DIAGNOSTIC")
        print("=" * 60)

        scripts = [
            ("check_apps.py", "scripts/diagnostics/check_apps.py", "Vérification des applications"),
            ("check_programs_urls.py", "scripts/diagnostics/check_programs_urls.py", "Vérification des URLs de programmes"),
            ("outils_diagnostic_tools.py", "scripts/diagnostics/outils_diagnostic_tools.py", "Outils de diagnostic"),
        ]

        moved = 0
        for src, dst, desc in scripts:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(scripts)} fichiers")

    def reorganize_fix_scripts(self):
        """Déplacer les scripts de correction"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES SCRIPTS DE CORRECTION")
        print("=" * 60)

        scripts = [
            ("fix_broken_urls.py", "scripts/fixes/fix_broken_urls.py", "Correction des URLs cassées"),
            ("fix_programs_urls.py", "scripts/fixes/fix_programs_urls.py", "Correction des URLs de programmes"),
            ("comprehensive_fix_nitrite.py", "scripts/fixes/comprehensive_fix_nitrite.py", "Correction complète"),
        ]

        moved = 0
        for src, dst, desc in scripts:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(scripts)} fichiers")

    def reorganize_test_scripts(self):
        """Déplacer les scripts de test"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES SCRIPTS DE TEST")
        print("=" * 60)

        scripts = [
            ("test_install_method.py", "scripts/tests/test_install_method.py", "Test d'installation"),
            ("test_portable_urls.py", "scripts/tests/test_portable_urls.py", "Test des URLs portables"),
        ]

        moved = 0
        for src, dst, desc in scripts:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(scripts)} fichiers")

    def reorganize_build_scripts(self):
        """Déplacer les scripts de build"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES SCRIPTS DE BUILD")
        print("=" * 60)

        scripts = [
            ("build_portable_fixed.py", "build_tools/build_portable_fixed.py", "Build portable"),
        ]

        moved = 0
        for src, dst, desc in scripts:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(scripts)} fichiers")

    def reorganize_config_files(self):
        """Déplacer les fichiers de configuration runtime"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES FICHIERS DE CONFIGURATION")
        print("=" * 60)

        files = [
            ("broken_urls.json", "data/config_runtime/broken_urls.json", "URLs cassées"),
            ("broken_programs_urls.json", "data/config_runtime/broken_programs_urls.json", "URLs programmes cassées"),
            ("config_manager.py", "scripts/config_manager.py", "Gestionnaire de config"),
            ("tool_downloader.py", "scripts/tool_downloader.py", "Téléchargeur d'outils"),
        ]

        moved = 0
        for src, dst, desc in files:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(files)} fichiers")

    def reorganize_assets(self):
        """Déplacer les fichiers assets (icônes)"""
        print("\n" + "=" * 60)
        print("DÉPLACEMENT DES ASSETS")
        print("=" * 60)

        assets = [
            ("Nitrite Icon.ico", "assets/Nitrite_Icon.ico", "Icône principale"),
        ]

        moved = 0
        for src, dst, desc in assets:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Déplacé: {moved}/{len(assets)} fichiers")

    def archive_legacy_files(self):
        """Archiver les fichiers legacy"""
        print("\n" + "=" * 60)
        print("ARCHIVAGE DES FICHIERS LEGACY")
        print("=" * 60)

        legacy = [
            ("Lancer_nitrite_v17.bat", "archive/launchers/Lancer_nitrite_v17.bat", "Lanceur v17"),
        ]

        moved = 0
        for src, dst, desc in legacy:
            if self.move_file(src, dst, desc):
                moved += 1

        print(f"\n  Archivé: {moved}/{len(legacy)} fichiers")

    def count_root_files(self) -> Tuple[int, List[str]]:
        """Compter les fichiers à la racine"""
        root_files = []
        for item in self.project_root.iterdir():
            if item.is_file():
                root_files.append(item.name)

        return len(root_files), root_files

    def generate_report(self):
        """Générer un rapport de réorganisation"""
        print("\n" + "=" * 60)
        print("GÉNÉRATION DU RAPPORT")
        print("=" * 60)

        report = {
            "date": datetime.now().isoformat(),
            "project_root": str(self.project_root),
            "statistics": {
                "directories_created": len(self.created_dirs),
                "files_moved": len(self.moves),
                "errors": len(self.errors)
            },
            "created_directories": self.created_dirs,
            "moved_files": self.moves,
            "errors": self.errors
        }

        # Sauvegarder le rapport JSON
        report_path = self.project_root / "RAPPORT_REORGANISATION.json"
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"\n  [CRÉÉ] RAPPORT_REORGANISATION.json")
        except Exception as e:
            print(f"\n  [ERREUR] Impossible de créer le rapport: {e}")

        # Générer un rapport Markdown
        md_report = self.generate_markdown_report(report)
        report_md_path = self.project_root / "RAPPORT_REORGANISATION.md"
        try:
            with open(report_md_path, 'w', encoding='utf-8') as f:
                f.write(md_report)
            print(f"  [CRÉÉ] RAPPORT_REORGANISATION.md")
        except Exception as e:
            print(f"  [ERREUR] Impossible de créer le rapport MD: {e}")

        return report

    def generate_markdown_report(self, report: Dict) -> str:
        """Générer un rapport au format Markdown"""
        before_count, _ = self.count_root_files()

        md = f"""# Rapport de Réorganisation - Nitrite V18.5

**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Résumé

- **Dossiers créés:** {report['statistics']['directories_created']}
- **Fichiers déplacés:** {report['statistics']['files_moved']}
- **Erreurs:** {report['statistics']['errors']}

## Objectif

Réorganiser le projet pour avoir le strict minimum à la racine (5 fichiers essentiels).

## Dossiers Créés

"""
        for dir_name in report['created_directories']:
            md += f"- `{dir_name}`\n"

        md += "\n## Fichiers Déplacés\n\n"
        md += "| Source | Destination | Description |\n"
        md += "|--------|-------------|-------------|\n"

        for move in report['moved_files']:
            md += f"| `{move['source']}` | `{move['destination']}` | {move['description']} |\n"

        if report['errors']:
            md += "\n## Erreurs\n\n"
            for error in report['errors']:
                md += f"- {error}\n"

        md += f"""

## Structure Finale

```
Nitrite-V18.5/
├── LANCER_NITRITE_V18.bat
├── START.bat
├── requirements.txt
├── README.md
├── Nitrite_V18_Portable.spec
├── src/
│   └── v14_mvp/
│       ├── main_app.py
│       ├── theme_editor_dynamic.py (NOUVEAU)
│       └── ...
├── data/
│   ├── programs.json
│   ├── portable_apps.json
│   ├── themes/ (NOUVEAU)
│   └── config_runtime/ (NOUVEAU)
├── assets/
│   └── Nitrite_Icon.ico
├── scripts/
│   ├── diagnostics/
│   ├── fixes/
│   └── tests/
├── build_tools/
├── docs/
├── archive/
└── ...
```

## Résultat

Projet réorganisé avec succès! La racine ne contient maintenant que les fichiers essentiels.
"""

        return md

    def run(self):
        """Exécuter la réorganisation complète"""
        print("\n" + "=" * 70)
        print(" " * 15 + "RÉORGANISATION DU PROJET NITRITE V18.5")
        print("=" * 70)

        print(f"\nRépertoire du projet: {self.project_root}")

        # Compter les fichiers avant
        before_count, before_files = self.count_root_files()
        print(f"Fichiers à la racine AVANT: {before_count}")

        # Étapes de réorganisation
        self.create_directory_structure()
        self.reorganize_diagnostic_scripts()
        self.reorganize_fix_scripts()
        self.reorganize_test_scripts()
        self.reorganize_build_scripts()
        self.reorganize_config_files()
        self.reorganize_assets()
        self.archive_legacy_files()

        # Compter les fichiers après
        after_count, after_files = self.count_root_files()
        print(f"\n" + "=" * 60)
        print("RÉSULTAT FINAL")
        print("=" * 60)
        print(f"Fichiers à la racine APRÈS: {after_count}")
        print(f"Réduction: {before_count - after_count} fichiers ({((before_count - after_count) / before_count * 100):.1f}%)")

        # Générer le rapport
        report = self.generate_report()

        print("\n" + "=" * 60)
        print("RÉORGANISATION TERMINÉE")
        print("=" * 60)
        print(f"\nDossiers créés: {len(self.created_dirs)}")
        print(f"Fichiers déplacés: {len(self.moves)}")
        print(f"Erreurs: {len(self.errors)}")

        if self.errors:
            print("\nErreurs rencontrées:")
            for error in self.errors:
                print(f"  - {error}")

        print("\nRapports générés:")
        print("  - RAPPORT_REORGANISATION.json")
        print("  - RAPPORT_REORGANISATION.md")

        return len(self.errors) == 0


def main():
    """Fonction principale"""
    import sys

    # Obtenir le chemin du projet
    project_root = os.path.dirname(os.path.abspath(__file__))

    print("\n" + "=" * 70)
    print(" " * 20 + "RÉORGANISATION NITRITE V18.5")
    print("=" * 70)
    print("\nCe script va réorganiser le projet pour avoir un minimum de fichiers")
    print("à la racine (5 fichiers essentiels).")
    print("\nLes fichiers seront déplacés vers des dossiers organisés:")
    print("  - scripts/diagnostics/")
    print("  - scripts/fixes/")
    print("  - scripts/tests/")
    print("  - build_tools/")
    print("  - data/config_runtime/")
    print("  - assets/")
    print("  - archive/")

    response = input("\nVoulez-vous continuer? (o/n): ").strip().lower()
    if response != 'o':
        print("\nRéorganisation annulée.")
        return 0

    # Créer le réorganisateur
    reorganizer = ProjectReorganizer(project_root)

    # Exécuter la réorganisation
    success = reorganizer.run()

    if success:
        print("\n✓ Réorganisation terminée avec succès!")
        return 0
    else:
        print("\n✗ Réorganisation terminée avec des erreurs.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
