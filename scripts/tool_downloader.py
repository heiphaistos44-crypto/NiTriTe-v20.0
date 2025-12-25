"""Module pour télécharger et gérer les outils de diagnostic"""


import os
import requests
import zipfile
import io
import hashlib


class ToolDownloader:
    """Gère le téléchargement et la vérification des outils"""
    
    def __init__(self, tools_manager):
        """Initialise le downloader avec le gestionaire d'outils"""
        self.tools_manager = tools_manager
    
    def download_tool(self, tool_name, save_path="."):
        """
        Télécharge un outil
        
        Args:
            tool_name: Nom de l'outil
            save_path: Chemin pour sauvegarder le fichier
        """
        url = self.tools_manager.get_tool_download_url(tool_name)
        
        if not url:
            raise ValueError(f"L'outil {tool_name} n'existe pas dans le gestionaire")
        
        print(f"Téléchargement de {tool_name} depuis {url}...")
        
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Sauvegarder le fichier
            file_path = os.path.join(save_path, f"{tool_name}.zip")
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            
            # Vérifier l'intégrité
            integrity_result = self.verify_tool_integrity(tool_name, file_path)
            
            if integrity_result['valid']:
                print(f"{tool_name} téléchargé et vérifié avec succès!")
                return file_path
            else:
                print(f"Échec de la vérification pour {tool_name}")
                
        except Exception as e:
            print(f"Erreur lors du téléchargement de {tool_name}: {str(e)}")
    
    def extract_tool(self, zip_file_path, extract_to="."):
        """
        Décompresse un fichier outil
        
        Args:
            zip_file_path: Chemin du fichier ZIP
            extract_to: Répertoire de décompression
        """
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                print(f"Décompressé {zip_file_path} dans {extract_to}")
        except Exception as e:
            print(f"Erreur lors de la décompression: {str(e)}")
    
    def verify_tool_integrity(self, tool_name, file_path):
        """
        Vérifie l'intégrité du fichier outil
        
        Args:
            tool_name: Nom de l'outil
            file_path: Chemin du fichier à vérifier
            
        Returns:
            Dictionnaire avec le statut de vérification
        """
        # Exemple de vérification par hachage (à adapter)
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        
        # Comparaison avec un hachage attendu (exemple statique)
        expected_hash = "sha256_example_hash_value"
        
        return {
            'valid': file_hash == expected_hash,
            'actual_hash': file_hash,
            'expected_hash': expected_hash
        }


# File: main_application.py