#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive fix for ALL Windows path backslashes"""

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
for line in lines:
    # Fix Windows registry paths - need quadruple backslash in source
    line = line.replace('HKLM\\\\SOFTWARE', 'HKLM\\\\\\\\SOFTWARE')
    line = line.replace('HKLM\\\\SYSTEM', 'HKLM\\\\\\\\SYSTEM')
    line = line.replace('HKLM\\SOFTWARE', 'HKLM\\\\\\\\SOFTWARE')
    line = line.replace('HKLM\\SYSTEM', 'HKLM\\\\\\\\SYSTEM')

    # Fix Windows paths
    line = line.replace('C:\\\\ProgramData\\NVIDIA', 'C:\\\\\\\\ProgramData\\\\\\\\NVIDIA')
    line = line.replace('C:\\ProgramData\\NVIDIA', 'C:\\\\\\\\ProgramData\\\\\\\\NVIDIA')
    line = line.replace('\\Setup\\MoSetup', '\\\\\\\\Setup\\\\\\\\MoSetup')
    line = line.replace('\\NV_Cache', '\\\\\\\\NV_Cache')
    line = line.replace('\\Policies\\Microsoft', '\\\\\\\\Policies\\\\\\\\Microsoft')
    line = line.replace('\\Windows\\DataCollection', '\\\\\\\\Windows\\\\\\\\DataCollection')

    fixed_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("All backslashes fixed!")

# Test import
import sys
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")
if 'v14_mvp.ai_knowledge_unified' in sys.modules:
    del sys.modules['v14_mvp.ai_knowledge_unified']

try:
    from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
    kb = UnifiedKnowledgeBase()
    stats = kb.get_stats()
    print(f"\nSUCCESS! Import successful!")
    print(f"Categories: {stats['categories']}/143")
    print(f"Tips: {stats['tips']}/5000 ({stats['tips']/5000*100:.1f}%)")
except SyntaxError as e:
    print(f"\nERROR: Still have syntax error: {e}")
    print("Line:", e.lineno)
