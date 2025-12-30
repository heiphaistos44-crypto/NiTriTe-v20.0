"""
Script de compression des dossiers volumineux pour la release
Compresse Drivers, Script Windows, et logiciel en archives ZIP
"""

import sys
from pathlib import Path

# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent / "src"))

from v14_mvp.archive_manager import ArchiveManager
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Compresse tous les dossiers volumineux"""
    print("=" * 60)
    print("COMPRESSION DES DOSSIERS VOLUMINEUX POUR LA RELEASE")
    print("=" * 60)
    print()

    manager = ArchiveManager()

    # Liste des dossiers à compresser
    folders_to_compress = [
        ("Drivers", "Drivers.zip"),
        ("Script Windows", "Script_Windows.zip"),
    ]

    # Ajouter logiciel s'il existe
    logiciel_path = manager.base_dir / "logiciel"
    if logiciel_path.exists():
        folders_to_compress.append(("logiciel", "logiciel.zip"))

    success_count = 0
    total_count = len(folders_to_compress)

    for folder_name, archive_name in folders_to_compress:
        print(f"\n{'='*60}")
        print(f"[+] Compression de: {folder_name}")
        print(f"{'='*60}")

        source_path = manager.base_dir / folder_name

        if not source_path.exists():
            print(f"[!] Dossier introuvable: {folder_name} - Ignore")
            total_count -= 1
            continue

        # Calculer la taille avant compression
        try:
            original_size = sum(f.stat().st_size for f in source_path.rglob('*') if f.is_file())
            print(f"[i] Taille originale: {original_size / 1024 / 1024:.2f} MB")
        except Exception as e:
            logger.warning(f"Impossible de calculer la taille: {e}")
            original_size = 0

        # Compresser
        success = manager.compress_directory(folder_name, archive_name)

        if success:
            success_count += 1
            archive_path = manager.archives_dir / archive_name
            compressed_size = archive_path.stat().st_size

            if original_size > 0:
                ratio = (1 - compressed_size / original_size) * 100
                savings = (original_size - compressed_size) / 1024 / 1024

                print(f"[OK] Compression reussie!")
                print(f"[i] Taille compressee: {compressed_size / 1024 / 1024:.2f} MB")
                print(f"[i] Economie: {savings:.2f} MB ({ratio:.1f}%)")
            else:
                print(f"[OK] Compression reussie!")
                print(f"[i] Taille compressee: {compressed_size / 1024 / 1024:.2f} MB")
        else:
            print(f"[X] Echec de la compression")

    # Résumé
    print(f"\n{'='*60}")
    print("RESUME")
    print(f"{'='*60}")
    print(f"[OK] Succes: {success_count}/{total_count}")

    if success_count == total_count:
        print("\n[OK] Toutes les compressions ont reussi!")
        print(f"\n[i] Archives creees dans: {manager.archives_dir}")
        print("\n[!] IMPORTANT:")
        print("1. Incluez le dossier 'archives_compressed' dans votre release")
        print("2. Les dossiers originaux peuvent etre supprimes de la release")
        print("3. L'application extraira automatiquement les archives au premier lancement")
        return 0
    else:
        print(f"\n[!] Certaines compressions ont echoue ({total_count - success_count} echecs)")
        return 1


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Interruption par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erreur inattendue: {e}", exc_info=True)
        sys.exit(1)
