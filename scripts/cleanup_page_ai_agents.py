#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour nettoyer page_ai_agents.py
Supprime le code mort entre fin de process_message() et autodiagnostic_system()
"""

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\page_ai_agents.py"

# Lire le fichier
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Supprimer les lignes 2460-2671 (indices 2459-2670 en Python 0-indexed)
# La vraie autodiagnostic_system est à la ligne 2672
start_delete = 2459  # Ligne 2460 (0-indexed)
end_delete = 2670     # Ligne 2671 (0-indexed, inclusive)

print(f"Fichier original: {len(lines)} lignes")
print(f"Suppression lignes {start_delete+1} à {end_delete+1}...")

# Créer nouvelle liste sans les lignes à supprimer
new_lines = lines[:start_delete] + lines[end_delete+1:]

print(f"Fichier nettoyé: {len(new_lines)} lignes")
print(f"Lignes supprimées: {len(lines) - len(new_lines)}")

# Écrire le fichier nettoyé
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ Nettoyage terminé!")
print(f"✅ Fichier sauvegardé: {file_path}")
