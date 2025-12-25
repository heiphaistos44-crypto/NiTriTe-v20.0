#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean duplicates from Batch 4 enrichment
Removes duplicate category definitions
"""

import re

def clean_duplicates():
    """Supprimer les doublons des catégories Batch 4"""

    file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Catégories Batch 4 à nettoyer
    batch_4_cats = [
        "networking_wifi_optimization",
        "networking_vpn_protocols",
        "virtualization_vmware_workstation",
        "virtualization_virtualbox",
        "wsl2_linux_windows",
        "development_git_workflow",
        "development_vscode_setup",
        "multimedia_video_encoding",
        "multimedia_obs_streaming",
        "file_management_tools",
        "compression_formats",
        "remote_desktop_gaming",
        "dual_boot_management",
        "system_cloning_migration",
        "windows_sandbox_security"
    ]

    for cat in batch_4_cats:
        pattern = rf'kb\["{cat}"\]\s*='
        matches = list(re.finditer(pattern, content))

        if len(matches) > 1:
            print(f"Found {len(matches)} occurrences of {cat}, keeping first, removing {len(matches)-1}")

            # Garder uniquement la première occurrence
            # Trouver les positions de début de chaque occurrence
            # On va supprimer de la 2ème occurrence jusqu'à la fin de la structure

            # Pour chaque occurrence après la première
            for i in range(len(matches) - 1, 0, -1):
                start_pos = matches[i].start()

                # Trouver la ligne "kb[" de début
                line_start = content.rfind('\n', 0, start_pos) + 1

                # Trouver la fermeture "        }" de cette catégorie
                # On cherche la prochaine ligne qui commence par "        }" après kb["xxx"]
                search_start = start_pos
                bracket_count = 0
                in_tips = False
                closing_pos = -1

                # Trouver le début du dict (premier {)
                dict_start = content.find('{', start_pos)

                # Parser jusqu'à trouver la fermeture correspondante
                pos = dict_start
                depth = 0
                while pos < len(content):
                    if content[pos] == '{':
                        depth += 1
                    elif content[pos] == '}':
                        depth -= 1
                        if depth == 0:
                            closing_pos = pos
                            break
                    pos += 1

                if closing_pos != -1:
                    # Trouver la fin de la ligne après }
                    line_end = content.find('\n', closing_pos)
                    if line_end == -1:
                        line_end = len(content)
                    else:
                        line_end += 1

                    # Supprimer tout le bloc
                    content = content[:line_start] + content[line_end:]
                    print(f"  Removed occurrence {i+1} from position {line_start} to {line_end}")

    # Écrire le fichier nettoyé
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n[OK] Duplicates cleaned successfully!")
    return True

if __name__ == "__main__":
    print("="*70)
    print("CLEANING BATCH 4 DUPLICATES")
    print("="*70)
    clean_duplicates()
