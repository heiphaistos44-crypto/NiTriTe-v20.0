"""
Gestionnaire d'archives pour NiTriTe V20
Gère l'extraction automatique des dossiers compressés (Drivers, Script Windows, etc.)
"""

import os
import sys
import zipfile
import shutil
import logging
from pathlib import Path
from typing import Optional, List
import threading
import requests
from tqdm import tqdm

logger = logging.getLogger(__name__)


class ArchiveManager:
    """Gestionnaire d'extraction et d'accès aux archives"""

    def __init__(self, base_dir: Optional[str] = None, github_release_url: Optional[str] = None):
        """
        Initialise le gestionnaire d'archives

        Args:
            base_dir: Répertoire de base (par défaut: répertoire de l'application)
            github_release_url: URL de base pour télécharger les archives depuis GitHub
        """
        if base_dir is None:
            # Déterminer le répertoire de base selon le mode d'exécution
            if getattr(sys, 'frozen', False):
                # Mode PyInstaller - utiliser le dossier de l'exécutable
                exe_dir = Path(sys.executable).parent
                base_dir = exe_dir
            else:
                # Mode développement - remonter de src/v14_mvp vers la racine
                base_dir = Path(__file__).parent.parent.parent
        else:
            base_dir = Path(base_dir)

        self.base_dir = base_dir
        self.archives_dir = base_dir / "archives_compressed"
        self.archives_source_dir = self.archives_dir
        self.extraction_status = {}
        self.extraction_lock = threading.Lock()

        # URL GitHub pour télécharger les archives
        # Format: https://github.com/user/repo/releases/download/vX.X.X/
        self.github_release_url = github_release_url or "https://github.com/heiphaistos44-crypto/NiTriTe-v20.0/releases/latest/download/"

        # Archives à gérer (nom_archive -> dossier_cible)
        self.managed_archives = {
            "Drivers.zip": "Drivers",
            "Script_Windows.zip": "Script Windows",
            "logiciel.zip": "logiciel"
        }

    def download_archive(self, archive_name: str, show_progress: bool = True) -> bool:
        """
        Télécharge une archive depuis GitHub Releases

        Args:
            archive_name: Nom de l'archive à télécharger
            show_progress: Afficher la progression du téléchargement

        Returns:
            True si le téléchargement a réussi
        """
        try:
            # Créer le dossier archives_compressed s'il n'existe pas
            self.archives_dir.mkdir(parents=True, exist_ok=True)

            # URL de téléchargement
            url = f"{self.github_release_url}{archive_name}"
            archive_path = self.archives_dir / archive_name

            if show_progress:
                print(f"[..] Telechargement de {archive_name} depuis GitHub...")

            # Télécharger avec barre de progression
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))

            # Télécharger par chunks avec barre de progression
            if show_progress and total_size > 0:
                with open(archive_path, 'wb') as f:
                    with tqdm(total=total_size, unit='B', unit_scale=True, desc=archive_name) as pbar:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                pbar.update(len(chunk))
            else:
                with open(archive_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

            if show_progress:
                print(f"[OK] {archive_name} telecharge avec succes")

            logger.info(f"Archive {archive_name} téléchargée depuis {url}")
            return True

        except requests.RequestException as e:
            logger.error(f"Erreur lors du téléchargement de {archive_name}: {e}")
            if show_progress:
                print(f"[X] Echec du telechargement de {archive_name}: {e}")
            return False
        except Exception as e:
            logger.error(f"Erreur inattendue lors du téléchargement de {archive_name}: {e}")
            if show_progress:
                print(f"[X] Erreur: {e}")
            return False

    def check_and_extract_all(self, show_progress: bool = True) -> bool:
        """
        Vérifie et extrait toutes les archives nécessaires
        Télécharge les archives depuis GitHub si elles ne sont pas présentes localement

        Args:
            show_progress: Afficher la progression

        Returns:
            True si toutes les extractions ont réussi
        """
        all_success = True

        for archive_name, target_dir in self.managed_archives.items():
            archive_path = self.archives_source_dir / archive_name
            target_path = self.base_dir / target_dir

            # Vérifier si le dossier cible est déjà extrait
            if self._is_dir_populated(target_path):
                logger.debug(f"{target_dir} déjà extrait")
                continue

            # Si l'archive n'existe pas localement, essayer de la télécharger
            if not archive_path.exists():
                logger.info(f"Archive {archive_name} introuvable, téléchargement depuis GitHub...")
                if show_progress:
                    print(f"[..] Archive {archive_name} non trouvee, telechargement...")

                download_success = self.download_archive(archive_name, show_progress=show_progress)
                if not download_success:
                    logger.error(f"Impossible de télécharger {archive_name}")
                    if show_progress:
                        print(f"[!] Impossible de telecharger {archive_name}, passage...")
                    all_success = False
                    continue

            # Extraire l'archive
            logger.info(f"Extraction de {archive_name}...")
            if show_progress:
                print(f"[..] Extraction de {archive_name}...")

            success = self.extract_archive(archive_name)
            if success:
                if show_progress:
                    print(f"[OK] {archive_name} extrait avec succes")
            else:
                logger.error(f"Échec de l'extraction de {archive_name}")
                if show_progress:
                    print(f"[X] Echec de l'extraction de {archive_name}")
                all_success = False

        return all_success

    def extract_archive(self, archive_name: str) -> bool:
        """
        Extrait une archive spécifique

        Args:
            archive_name: Nom de l'archive à extraire

        Returns:
            True si l'extraction a réussi
        """
        with self.extraction_lock:
            if archive_name not in self.managed_archives:
                logger.error(f"Archive inconnue: {archive_name}")
                return False

            archive_path = self.archives_source_dir / archive_name
            target_dir = self.managed_archives[archive_name]
            target_path = self.base_dir / target_dir

            if not archive_path.exists():
                logger.warning(f"Archive introuvable: {archive_path}")
                return False

            try:
                # Créer le dossier cible s'il n'existe pas
                target_path.parent.mkdir(parents=True, exist_ok=True)

                # Extraire l'archive
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    zip_ref.extractall(self.base_dir)

                self.extraction_status[archive_name] = True
                logger.info(f"Archive {archive_name} extraite vers {target_path}")
                return True

            except Exception as e:
                logger.error(f"Erreur lors de l'extraction de {archive_name}: {e}")
                self.extraction_status[archive_name] = False
                return False

    def _is_dir_populated(self, dir_path: Path) -> bool:
        """
        Vérifie si un dossier existe et contient des fichiers

        Args:
            dir_path: Chemin du dossier à vérifier

        Returns:
            True si le dossier existe et contient au moins un fichier
        """
        if not dir_path.exists():
            return False

        # Vérifier s'il y a au moins un fichier (pas seulement des dossiers vides)
        try:
            for root, dirs, files in os.walk(dir_path):
                if files:
                    return True
            return False
        except Exception as e:
            logger.error(f"Erreur lors de la vérification de {dir_path}: {e}")
            return False

    def get_extraction_status(self) -> dict:
        """
        Retourne le statut d'extraction de toutes les archives

        Returns:
            Dictionnaire {archive_name: status}
        """
        status = {}
        for archive_name, target_dir in self.managed_archives.items():
            target_path = self.base_dir / target_dir
            status[archive_name] = self._is_dir_populated(target_path)
        return status

    def compress_directory(self, dir_name: str, archive_name: Optional[str] = None) -> bool:
        """
        Compresse un dossier en archive ZIP

        Args:
            dir_name: Nom du dossier à compresser
            archive_name: Nom de l'archive (par défaut: {dir_name}.zip)

        Returns:
            True si la compression a réussi
        """
        if archive_name is None:
            archive_name = f"{dir_name.replace(' ', '_')}.zip"

        source_path = self.base_dir / dir_name

        if not source_path.exists():
            logger.error(f"Dossier introuvable: {source_path}")
            return False

        # Créer le dossier archives_compressed s'il n'existe pas
        self.archives_dir.mkdir(parents=True, exist_ok=True)
        archive_path = self.archives_dir / archive_name

        try:
            logger.info(f"Compression de {source_path} vers {archive_path}...")

            with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(self.base_dir)

                        # Écrire le fichier dans l'archive
                        try:
                            zipf.write(file_path, arcname)
                        except ValueError as e:
                            # Gérer les fichiers avec timestamps invalides (avant 1980)
                            if "ZIP does not support timestamps before 1980" in str(e):
                                logger.warning(f"Fichier avec timestamp invalide, correction: {file_path}")
                                # Lire le contenu et l'écrire avec un timestamp valide
                                with open(file_path, 'rb') as f:
                                    data = f.read()
                                # Utiliser writestr avec un ZipInfo pour contrôler le timestamp
                                zinfo = zipfile.ZipInfo(filename=str(arcname))
                                zinfo.date_time = (1980, 1, 1, 0, 0, 0)  # Timestamp minimal valide
                                zinfo.compress_type = zipfile.ZIP_DEFLATED
                                zipf.writestr(zinfo, data, compress_type=zipfile.ZIP_DEFLATED)
                            else:
                                raise

            logger.info(f"Archive créée: {archive_path}")

            # Afficher la taille économisée
            original_size = sum(f.stat().st_size for f in source_path.rglob('*') if f.is_file())
            compressed_size = archive_path.stat().st_size
            ratio = (1 - compressed_size / original_size) * 100

            logger.info(f"Taille originale: {original_size / 1024 / 1024:.2f} MB")
            logger.info(f"Taille compressée: {compressed_size / 1024 / 1024:.2f} MB")
            logger.info(f"Compression: {ratio:.1f}%")

            return True

        except Exception as e:
            logger.error(f"Erreur lors de la compression de {dir_name}: {e}")
            return False


def initialize_archives(show_progress: bool = True) -> bool:
    """
    Fonction d'initialisation à appeler au démarrage de l'application

    Args:
        show_progress: Afficher la progression

    Returns:
        True si l'initialisation a réussi
    """
    manager = ArchiveManager()
    return manager.check_and_extract_all(show_progress=show_progress)


if __name__ == "__main__":
    # Configuration du logging pour les tests
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Test d'extraction
    print("=== Test du gestionnaire d'archives ===")
    result = initialize_archives(show_progress=True)
    print(f"\nRésultat: {'✅ Succès' if result else '❌ Échec'}")
