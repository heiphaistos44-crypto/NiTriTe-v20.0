#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test final du Batch 4
"""

import sys
import os

# Ajouter le chemin pour l'import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'v14_mvp'))

from ai_knowledge_unified import UnifiedKnowledgeBase

def test_batch_4():
    """Test et affiche les statistiques finales"""

    kb = UnifiedKnowledgeBase()

    # Statistiques
    total_categories = len(kb.kb)
    total_tips = sum(len(cat["tips"]) for cat in kb.kb.values())

    print("="*70)
    print("KNOWLEDGE BASE STATISTICS - AFTER BATCH 4")
    print("="*70)
    print(f"Total Categories: {total_categories}")
    print(f"Total Tips: {total_tips}")
    print(f"\nProgress towards goal:")
    print(f"  Categories: {total_categories}/143 ({total_categories/143*100:.1f}%)")
    print(f"  Tips: {total_tips}/5000 ({total_tips/5000*100:.1f}%)")

    # Vérifier les nouvelles catégories Batch 4
    batch_4_categories = [
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

    print("\n" + "-"*70)
    print("BATCH 4 CATEGORIES VERIFICATION (15 nouvelles catégories)")
    print("-"*70)

    all_present = True
    batch_4_tips_total = 0

    for cat in batch_4_categories:
        if cat in kb.kb:
            tips_count = len(kb.kb[cat]["tips"])
            priority = kb.kb[cat]["metadata"]["priority"]
            batch_4_tips_total += tips_count
            print(f"[OK] {cat}: {tips_count} tips (priority {priority})")
        else:
            print(f"[FAIL] {cat}: MISSING!")
            all_present = False

    print("\n" + "-"*70)
    if all_present:
        print(f"[SUCCESS] All 15 Batch 4 categories successfully added!")
        print(f"[SUCCESS] Batch 4 added {batch_4_tips_total} new tips")
    else:
        print("[FAIL] Some categories are missing!")

    print("="*70)

if __name__ == "__main__":
    test_batch_4()
