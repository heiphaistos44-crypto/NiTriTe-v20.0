"""
Module de nettoyage NiTrite
Supprime toutes les traces de l'application et ses dépendances
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


class NiTriteCleanup:
    """Gère le nettoyage complet de NiTrite et ses dépendances"""
    
    def __init__(self):
        self.app_dir = Path(__file__).parent.parent
        self.python_exe = sys.executable
        self.python_dir = Path(self.python_exe).parent
        
    def get_cleanup_items(self) -> List[Tuple[str, str, int]]:
        """
        Retourne la liste des éléments à supprimer
        
        Returns:
            Liste de tuples (nom, chemin, taille_mb)
        """
        items = []
        
        # 1. Dossier de l'application
        app_size = self._get_folder_size(self.app_dir)
        items.append((
            " NiTrite (application complète)",
            str(self.app_dir),
            app_size
        ))
        
        # 2. Python (si installé dans un dossier local)
        if self._is_local_python():
            python_size = self._get_folder_size(self.python_dir)
            items.append((
                " Python (interpréteur)",
                str(self.python_dir),
                python_size
            ))
        
        # 3. Fichiers temporaires
        temp_dirs = [
            Path(os.environ.get('TEMP', '')) / 'nitrite',
            Path(os.environ.get('LOCALAPPDATA', '')) / 'NiTrite',
        ]
        
        for temp_dir in temp_dirs:
            if temp_dir.exists():
                temp_size = self._get_folder_size(temp_dir)
                items.append((
                    f" Fichiers temporaires ({temp_dir.name})",
                    str(temp_dir),
                    temp_size
                ))
        
        return items
    
    def _get_folder_size(self, folder: Path) -> int:
        """Calcule la taille d'un dossier en Mo"""
        try:
            if not folder.exists():
                return 0
            
            total_size = 0
            for item in folder.rglob('*'):
                if item.is_file():
                    try:
                        total_size += item.stat().st_size
                    except (OSError, PermissionError):
                        pass
            
            return int(total_size / (1024 * 1024))  # Convertir en Mo
        except Exception as e:
            logger.warning(f"Erreur calcul taille {folder}: {e}")
            return 0
    
    def _is_local_python(self) -> bool:
        """Vérifie si Python est installé localement (pas système)"""
        python_path = str(self.python_dir).lower()
        
        # Python système typique
        system_paths = [
            'program files',
            'windows',
            'python311',  # Installation Windows Store
            'python312',
            'python313',
            'python314',
        ]
        
        # Si Python est dans un de ces dossiers, c'est une installation système
        for sys_path in system_paths:
            if sys_path in python_path:
                return False
        
        # Sinon, c'est probablement une installation locale
        return True
    
    def create_cleanup_script(self) -> Path:
        """
        Crée un script de nettoyage qui s'exécute après la fermeture de l'application
        
        Returns:
            Chemin du script créé
        """
        script_path = self.app_dir / "cleanup_nitrite.bat"
        
        script_content = f"""@echo off
echo.
echo ================================================
echo      NETTOYAGE NITRITE EN COURS...
echo ================================================
echo.

REM Attendre que l'application se ferme complètement
timeout /t 2 /nobreak > nul

echo  Suppression de l'application NiTrite...
rd /s /q "{self.app_dir}" 2>nul

"""
        
        # Ajouter Python seulement si c'est une installation locale
        if self._is_local_python():
            script_content += f"""
echo  Suppression de Python...
rd /s /q "{self.python_dir}" 2>nul
"""
        
        script_content += """
echo.
echo  Nettoyage terminé !
echo.
echo Appuyez sur une touche pour fermer...
pause > nul

REM Auto-supprimer ce script
del "%~f0"
"""
        
        try:
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            logger.info(f" Script de nettoyage créé: {script_path}")
            return script_path
            
        except Exception as e:
            logger.error(f" Erreur création script: {e}")
            return None
    
    def execute_cleanup(self, items_to_delete: List[str]) -> bool:
        """
        Exécute le nettoyage des éléments sélectionnés
        
        Args:
            items_to_delete: Liste des chemins à supprimer
            
        Returns:
            True si le script a été créé et lancé
        """
        try:
            # Créer le script de nettoyage
            script_path = self.create_cleanup_script()
            
            if not script_path or not script_path.exists():
                logger.error(" Impossible de créer le script de nettoyage")
                return False
            
            # Lancer le script en arrière-plan
            logger.info(f" Lancement du script de nettoyage: {script_path}")
            
            subprocess.Popen(
                ['cmd', '/c', str(script_path)],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                cwd=str(self.app_dir.parent)
            )
            
            logger.info(" Script de nettoyage lancé")
            return True
            
        except Exception as e:
            logger.error(f" Erreur exécution nettoyage: {e}")
            return False
    
    def get_total_size(self) -> int:
        """Retourne la taille totale de tous les éléments en Mo"""
        items = self.get_cleanup_items()
        return sum(size for _, _, size in items)
    
    def cleanup_logs_only(self):
        """Nettoie uniquement les fichiers de log"""
        try:
            logs_dir = self.app_dir / "logs"
            if logs_dir.exists():
                for log_file in logs_dir.glob("*.log"):
                    try:
                        log_file.unlink()
                        logger.info(f" Log supprimé: {log_file.name}")
                    except (OSError, PermissionError):
                        pass
        except Exception as e:
            logger.warning(f" Erreur nettoyage logs: {e}")


if __name__ == "__main__":
    # Test du module
    logging.basicConfig(level=logging.INFO)
    
    cleanup = NiTriteCleanup()
    
    print("\n ÉLÉMENTS DÉTECTÉS POUR NETTOYAGE:\n")
    
    items = cleanup.get_cleanup_items()
    total_size = 0
    
    for name, path, size in items:
        print(f"{name}")
        print(f"   Chemin: {path}")
        print(f"   Taille: {size} Mo")
        print()
        total_size += size
    
    print(f" Taille totale: {total_size} Mo")
    print(f" Python local: {'Oui' if cleanup._is_local_python() else 'Non (système)'}")
