#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Restore KB to last working state by removing broken mega batch additions"""

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find where mega batch additions start (they start after a specific marker)
# The mega batch added a comment: "# ===== CPU CATEGORIES ====="
mega_batch_start_marker = "        # ===== CPU CATEGORIES ====="

if mega_batch_start_marker in content:
    # Find the insertion point
    insert_point_marker = "        return kb"
    insert_idx = content.find(insert_point_marker)
    mega_start_idx = content.find(mega_batch_start_marker)

    if mega_start_idx < insert_idx and mega_start_idx > 0:
        # Remove everything between mega_start and insert_point
        clean_content = content[:mega_start_idx] + "\n" + content[insert_idx:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)

        print("Removed broken mega batch additions")
    else:
        print("Mega batch marker not found in expected location")
else:
    print("No mega batch additions found - file may already be clean")

# Test import
import sys
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")
if 'v14_mvp.ai_knowledge_unified' in sys.modules:
    del sys.modules['v14_mvp.ai_knowledge_unified']

try:
    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"\nSUCCESS! KB restored and working")
    print(f"Categories: {stats['categories']}/143")
    print(f"Tips: {stats['tips']}/5000 ({stats['tips']/5000*100:.1f}%)")
except Exception as e:
    print(f"\nERROR: {e}")
