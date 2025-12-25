"""
Gestionnaire de fournisseurs d'outils de diagnostic avec vérification des liens

Cette classe gère la collection d'outils de diagnostic, valide les URLs,
et permet de mettre à jour les liens portables.
"""

import re
from urllib.parse import urlparse
from datetime import datetime


class DiagnosticToolProvider:
    """Fournisseur d'outil de diagnostic avec validation"""
    
    def __init__(self, name, portable_url, version="1.0", is_portable=True):
        """
        Initialise un fournisseur d'outil
        
        Args:
            name: Nom de l'outil
            portable_url: URL du fichier portable
            version: Numéro de version
            is_portable: Indicateur d'exécutable portable
        """
        self.name = name
        self.portable_url = portable_url
        self.version = version
        self.is_portable = is_portable
        self.last_validated = datetime.now()
        
        # Validation automatique à la création
        self.validate_url()
    
    def validate_url(self):
        """
        Valide l'URL du fichier portable
        
        Returns:
            dict: Statut de validation avec des détails
        """
        validation_result = {
            "valid": False,
            "message": "",
            "url": self.portable_url,
            "timestamp": datetime.now()
        }
        
        # Vérification de base du format URL
        if not self._is_valid_url_format():
            validation_result["message"] = "Format d'URL invalide"
            return validation_result
        
        # Vérification pour les URLs portables (doivent contenir 'portable' ou 'download')
        if self.is_portable:
            if not self._contains_portable_keywords():
                validation_result["message"] = "URL portable invalide (manque 'portable' ou 'download')"
                return validation_result
        
        # Vérification des extensions de fichier
        file_extension = self._get_file_extension()
        if file_extension and not self._is_valid_file_extension(file_extension):
            validation_result["message"] = f"Extension de fichier invalide: {file_extension}"
            return validation_result
        
        # Si toutes les vérifications passent
        validation_result["valid"] = True
        validation_result["message"] = "URL valide"
        
        return validation_result
    
    def _is_valid_url_format(self):
        """Vérifie le format général de l'URL"""
        url_pattern = r'https?://[^/\s]+/[^/\s]+?\.(?:exe|zip|rar|7z|portable)'
        return re.match(url_pattern, self.portable_url) is not None
    
    def _contains_portable_keywords(self):
        """Vérifie la présence de mots-clés pour les fichiers portables"""
        portable_patterns = [
            r'portable',
            r'download',
            r'version-\d+',
            r'version\s+\d+'
        ]
        
        for pattern in portable_patterns:
            if re.search(pattern, self.portable_url, re.IGNORE_CASE):
                return True
        return False
    
    def _get_file_extension(self):
        """Extrait l'extension de fichier depuis l'URL"""
        from urllib.parse import urlparse
        
        parsed = urlparse(self.portable_url)
        path = parsed.path if parsed.path else ""
        
        # Extraire l'extension depuis le chemin
        match = re.search(r'\.(?:exe|zip|rar|7z|portable)$', path)
        return match.group(0) if match else None
    
    def _is_valid_file_extension(self, extension):
        """Vérifie si l'extension est valide pour un fichier portable"""
        valid_extensions = ['\.exe$', '\.zip$', '\.rar$', '\.7z$', '\.portable$']
        
        for ext_pattern in valid_extensions:
            if re.match(ext_pattern, extension):
                return True
        return False
    
    def update_portable_url(self, new_url):
        """
        Met à jour l'URL du fichier portable avec validation
        
        Args:
            new_url: Nouvelle URL à valider
            
        Returns:
            bool: Statut de réussite
        """
        # Valider la nouvelle URL avant de l'enregistrer
        validator = self.validate_url()
        
        if validator["valid"]:
            self.portable_url = new_url
            self.last_validated = datetime.now()
            return True
        
        return False


class DiagnosticToolsManager:
    """Gestionnaire centralisé des outils de diagnostic"""
    
    def __init__(self):
        self.tools = []
        self.changelog = []
        self.last_modified = datetime.now()
        
        # Charger les outils persistants
        self.load_persistent_tools()
    
    def add_tool(self, provider):
        """
        Ajoute un nouveau fournisseur d'outil
        
        Args:
            provider: Instance DiagnosticToolProvider
        """
        if self._is_valid_provider(provider):
            self.tools.append(provider)
            self.last_modified = datetime.now()
            self._save_persistent_tools()
    
    def update_tool_url(self, tool_name, new_url):
        """
        Met à jour l'URL d'un outil spécifique
        
        Args:
            tool_name: Nom de l'outil à mettre à jour
            new_url: Nouvelle URL
            
        Returns:
            dict: Résultat avec statut et détails
        """
        # Trouver l'outil par nom
        tool = self._find_tool_by_name(tool_name)
        
        if not tool:
            return {
                "success": False,
                "error": "Outil non trouvé",
                "tool_name": tool_name
            }
        
        # Créer un nouveau fournisseur avec l'URL mise à jour
        updated_provider = DiagnosticToolProvider(
            name=tool.name,
            portable_url=new_url,
            version=tool.version,
            is_portable=tool.is_portable
        )
        
        # Remplacer l'ancien par le nouveau
        index = self.tools.index(tool)
        self.tools[index] = updated_provider
        
        # Enregistrer les changements
        self.last_modified = datetime.now()
        self._save_persistent_tools()
        
        # Créer un historique des modifications
        self.changelog.append({
            "tool": tool.name,
            "old_url": tool.portable_url,
            "new_url": new_url,
            "timestamp": datetime.now()
        })
        
        return {
            "success": True,
            "updated_tool": updated_provider,
            "tool_name": tool_name,
            "timestamp": datetime.now()
        }
    
    def validate_all_tools(self):
        """Valide tous les fournisseurs d'outils"""
        results = []
        
        for tool in self.tools:
            validation = tool.validate_url()
            results.append(validation)
        
        return results
    
    def get_invalid_tools(self):
        """Récupère tous les outils avec des URLs invalides"""
        return [tool for tool in self.tools if not tool.validate_url()["valid"]]
    
    def _is_valid_provider(self, provider):
        """Vérifie si le fournisseur est valide"""
        if not isinstance(provider, DiagnosticToolProvider):
            raise ValueError("Le fournisseur doit être une instance de DiagnosticToolProvider")
        
        # Vérifier que l'URL est valide
        validation = provider.validate_url()
        return validation["valid"]
    
    def _find_tool_by_name(self, name):
        """Trouve un outil par nom (recherche partielle)"""
        for tool in self.tools:
            if tool.name.lower() in name.lower():
                return tool
        return None
    
    def load_persistent_tools(self):
        """Charge les outils persistants depuis le stockage"""
        # Implémentation d'exemple - dans un vrai projet, utiliser un fichier de sauvegarde
        self.persistent_tools = []
        
        # Exemple de données prédéfinies
        initial_data = [
            DiagnosticToolProvider(
                "Crystal Disk Mark",
                "https://download.crystaldiskmark.com/portable/Portable-CrystalDiskMark-1.0.4.2.exe",
                "1.0.4.2",
                True
            ),
            DiagnosticToolProvider(
                "HWMonitor",
                "https://www.cpuid.com/files/download/HWMonitorPortable_2.35.exe",
                "2.35",
                True
            ),
            DiagnosticToolProvider(
                "HWinfo",
                "https://www.cpuid.com/files/download/HWiNFO64_Portable_v8.10.rar",
                "8.10",
                True
            )
        ]
        
        self.persistent_tools = initial_data
    
    def _save_persistent_tools(self):
        """Sauvegarde les outils persistants (implémentation d'exemple)"""
        # Dans un vrai projet, sauvegarder dans un fichier JSON ou base de données
        print(f"Généré le {self.last_modified} - Outils: {len(self.persistent_tools)}")


class LinkValidator:
    """Validateur spécialisé pour les liens portables"""
    
    def validate_portable_link(self, link):
        """
        Valide un lien portable avec des critères spécifiques
        
        Args:
            link: Lien à valider
            
        Returns:
            dict: Résultat de validation détaillé
        """
        result = {
            "link": link,
            "valid": False,
            "issues": [],
            "confidence_score": 0
        }
        
        # Vérification 1: Format général
        if not self._is_valid_portable_format(link):
            result["issues"].append("Format d'URL invalide pour un fichier portable")
        
        # Vérification 2: Contenu des segments d'url
        if not self._contains_valid_segments(link):
            result["issues"].append("Segments URL non optimaux pour un lien portable")
        
        # Vérification 3: Mots-clés de version
        if not self._contains_version_keywords(link):
            result["issues"].append("Aucun indicateur de version trouvé dans l'URL")
        
        # Calcul du score de confiance
        result["confidence_score"] = len(result["issues"]) / 3
        
        # Décision finale
        result["valid"] = len(result["issues"]) == 0 or result["confidence_score"] > 0.6
        
        return result
    
    def _is_valid_portable_format(self, link):
        """Vérifie le format spécifique des liens portables"""
        # Pattern pour les fichiers exécutables portable
        exe_pattern = r'portable(?:-\d+\.\d+[\.-]\d+)?\.(exe|zip|rar|7z)$'
        
        # Vérifier si l'URL contient 'portable' dans le chemin
        if not re.search(r'/portable/?', link):
            return False
        
        # Vérifier l'extension de fichier
        if not re.search(exe_pattern, link):
            return False
        
        return True
    
    def _contains_valid_segments(self, link):
        """Vérifie les segments d'url pour un lien portable valide"""
        # Parser l'URL
        from urllib.parse import urlparse
        parsed = urlparse(link)
        
        # Vérifier le nom de domaine (doit être professionnel)
        domain = parsed.netloc
        if not self._is_professional_domain(domain):
            return False
        
        # Vérifier le chemin (doit contenir 'download' ou 'files')
        path = parsed.path
        if not re.search(r'(download|files|telechargement)', path, re.IGNORE_CASE):
            return False
        
        return True
    
    def _contains_version_keywords(self, link):
        """Vérifie la présence de numéros de version"""
        # Chercher des patterns de version
        version_patterns = [
            r'v?\d+\.\d+(?:\.\d+)?',  # v1.2.3 ou 1.2.3
            r'version-\d+\.\d+',     # version-1.2
            r'release-\d+',          # release-5
            r'(\d{4})'               # Année (pour les versions anciennes)
        ]
        
        for pattern in version_patterns:
            if re.search(pattern, link):
                return True
        
        return False
    
    def _is_professional_domain(self, domain):
        """Vérifie si le domaine semble professionnel"""
        # Liste de domains commerciaux courants
        commercial_domains = ['com', 'net', 'org', 'io', 'dev']
        
        # Vérifier s'il contient un domaine commercial
        if any(d in domain for d in commercial_domains):
            return True
        
        # Vérifier les noms de domaine (doivent être courts et pertinents)
        from urllib.parse import urlparse
        
        parsed = urlparse(f"https://{domain}")
        hostname = parsed.hostname or domain
        
        if hostname and len(hostname.split('.')) > 2:
            return False
        
        return True