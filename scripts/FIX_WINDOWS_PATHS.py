#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix Windows path escaping in ai_knowledge_unified.py"""

file_path = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Windows registry paths
content = content.replace('HKLM\\SOFTWARE', 'HKLM\\\\SOFTWARE')
content = content.replace('HKLM\\SYSTEM', 'HKLM\\\\SYSTEM')
content = content.replace('C:\\ProgramData', 'C:\\\\ProgramData')
content = content.replace('C:\\Windows', 'C:\\\\Windows')

# Fix any remaining single backslashes in registry/Windows paths (be careful)
import re
# Fix pattern: \S (invalid escape) to \\S
content = re.sub(r'([^\\])\\([SPWC])', r'\1\\\\\2', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Windows path escaping fixed!")

# Test import
import sys
sys.path.insert(0, r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src")
if 'v14_mvp.ai_knowledge_unified' in sys.modules:
    del sys.modules['v14_mvp.ai_knowledge_unified']

from v14_mvp.ai_knowledge_unified import UnifiedKnowledgeBase
kb = UnifiedKnowledgeBase()
stats = kb.get_stats()

print(f"Import successful! Categories: {stats['categories']}, Tips: {stats['tips']}")
