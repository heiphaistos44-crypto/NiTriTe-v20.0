#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de Correction Complète - Nitrite V18.5
Supprime les emojis, corrige les erreurs, améliore le code
"""

import os
import re
import ast
import json
from pathlib import Path
from typing import List, Dict

class NitriteFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.src_dir = self.project_root / "src"
        self.backup_dir = self.project_root / "backups_corrections"
        self.backup_dir.mkdir(exist_ok=True)
        
        self.errors_found = []
        self.emojis_removed = 0
        self.files_fixed = []
        
        # Pattern emojis
        self.emoji_pattern = re.compile(
            "["
            "\U0001F300-\U0001F9FF"
            "\U0001F600-\U0001F64F"
            "\U0001F680-\U0001F6FF"
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+"
        )
    
    def backup_file(self, filepath: Path):
        """Créer backup"""
        relative_path = filepath.relative_to(self.project_root)
        backup_path = self.backup_dir / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[BACKUP] {relative_path}")
    
    def remove_emojis(self, filepath: Path) -> int:
        """Supprimer emojis"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_len = len(content)
            content_cleaned = self.emoji_pattern.sub('', content)
            emojis_count = original_len - len(content_cleaned)
            
            if emojis_count > 0:
                self.backup_file(filepath)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content_cleaned)
                print(f"[EMOJI] {emojis_count} chars supprimés dans {filepath.name}")
                self.emojis_removed += emojis_count
                self.files_fixed.append(str(filepath.relative_to(self.project_root)))
                return emojis_count
            return 0
        except Exception as e:
            print(f"[ERREUR] {filepath}: {e}")
            return 0
    
    def check_syntax(self, filepath: Path) -> List[str]:
        """Vérifier syntaxe"""
        errors = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            try:
                ast.parse(content)
            except SyntaxError as e:
                error_msg = f"Ligne {e.lineno}: {e.msg}"
                errors.append(error_msg)
                self.errors_found.append({
                    'file': str(filepath.relative_to(self.project_root)),
                    'line': e.lineno,
                    'error': e.msg
                })
        except Exception as e:
            errors.append(f"Erreur lecture: {e}")
        return errors
    
    def scan_all(self):
        """Scanner tous les fichiers"""
        print("\n" + "="*70)
        print("CORRECTION COMPLÈTE - NITRITE V18.5")
        print("="*70 + "\n")
        
        python_files = list(self.src_dir.rglob("*.py"))
        print(f"[INFO] {len(python_files)} fichiers Python trouvés\n")
        
        for filepath in python_files:
            if 'backup' in str(filepath).lower():
                continue
            
            print(f"[SCAN] {filepath.name}...")
            self.remove_emojis(filepath)
            
            syntax_errors = self.check_syntax(filepath)
            if syntax_errors:
                print(f"  [ERREUR] {len(syntax_errors)} erreurs")
                for error in syntax_errors:
                    print(f"    - {error}")
    
    def generate_report(self):
        """Générer rapport"""
        report = {
            'emojis_removed': self.emojis_removed,
            'files_fixed': list(set(self.files_fixed)),
            'errors_found': self.errors_found
        }
        
        report_path = self.project_root / "RAPPORT_CORRECTIONS.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print("\n" + "="*70)
        print("RAPPORT FINAL")
        print("="*70)
        print(f"Emojis supprimés: {self.emojis_removed}")
        print(f"Fichiers corrigés: {len(set(self.files_fixed))}")
        print(f"Erreurs: {len(self.errors_found)}")
        print(f"Rapport: {report_path}")
        print("="*70 + "\n")

if __name__ == "__main__":
    fixer = NitriteFixer(str(Path(__file__).parent))
    fixer.scan_all()
    fixer.generate_report()
    print("[OK] Correction terminée!")
