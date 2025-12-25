#!/usr/bin/env python3
"""
NiTriTe V18.5 Knowledge Base Direct File Editor
This script directly modifies the ai_knowledge_unified.py file to add tips
"""

import re
import os

# Target file
TARGET_FILE = r"C:\Users\Utilisateur\Downloads\Nitrite-V18.5\src\v14_mvp\ai_knowledge_unified.py"

def find_category_tips_end(content, category_name):
    """Find the position where we should insert new tips for a category"""
    # Pattern to match the category and find its tips array end
    pattern = rf'kb\["{category_name}"\]\s*=\s*\{{'
    match = re.search(pattern, content)

    if not match:
        return None

    start_pos = match.end()
    # Find the "tips": [ section
    tips_pattern = r'"tips"\s*:\s*\['
    tips_match = re.search(tips_pattern, content[start_pos:])

    if not tips_match:
        return None

    tips_start = start_pos + tips_match.end()

    # Find the closing ] of the tips array
    # We need to count brackets to find the matching close
    bracket_count = 1
    i = tips_start
    in_string = False
    escape_next = False

    while i < len(content) and bracket_count > 0:
        char = content[i]

        if escape_next:
            escape_next = False
            i += 1
            continue

        if char == '\\':
            escape_next = True
        elif char == '"' and not escape_next:
            in_string = not in_string
        elif not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return i  # Return position just before the closing ]

        i += 1

    return None

def format_tip_as_python(tip_dict):
    """Convert a Python dictionary to a formatted Python code string"""
    # Properly escape quotes in content
    content = tip_dict['content'].replace('\\', '\\\\').replace('"', '\\"')

    keywords_str = ', '.join(f'"{k}"' for k in tip_dict['keywords'])
    tags_str = ', '.join(f'"{t}"' for t in tip_dict['tags'])
    tools_str = ', '.join(f'"{t}"' for t in tip_dict['related_tools'])

    tip_str = f'''                {{"content": "{content}", "keywords": [{keywords_str}], "difficulty": "{tip_dict['difficulty']}", "tags": [{tags_str}], "related_tools": [{tools_str}]}}'''

    return tip_str

def add_tips_to_category(content, category_name, new_tips):
    """Add new tips to a category in the content"""
    insert_pos = find_category_tips_end(content, category_name)

    if insert_pos is None:
        print(f"ERROR: Could not find category {category_name}")
        return content

    # Check if there are existing tips (look backwards for last tip)
    # If the last non-whitespace character before ] is a }, we need a comma
    prefix = content[:insert_pos].rstrip()
    needs_comma = prefix.endswith('}')

    # Format new tips
    tips_str = ""
    for i, tip in enumerate(new_tips):
        if i == 0 and needs_comma:
            tips_str += ",\n"
        elif i > 0:
            tips_str += ",\n"
        tips_str += format_tip_as_python(tip)

    # Insert the new tips
    new_content = content[:insert_pos] + tips_str + "\n" + content[insert_pos:]

    return new_content

def main():
    print("=" * 80)
    print("NITRITE V18.5 - DIRECT FILE EDITOR FOR KNOWLEDGE BASE")
    print("=" * 80)

    # Backup original file
    backup_file = TARGET_FILE + ".backup_phase2"
    if not os.path.exists(backup_file):
        print(f"\nCreating backup: {backup_file}")
        with open(TARGET_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Backup created successfully!")
    else:
        print(f"\nBackup already exists: {backup_file}")
        with open(TARGET_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

    # Define tips to add for gpu_intel_arc (sample - just 5 for testing)
    gpu_intel_arc_tips = [
        {
            "content": "Intel Arc A770 ReBAR (Resizable BAR) is mandatory for optimal performance. Enable in BIOS under PCI Subsystem Settings > Above 4G Decoding (Enabled) + Re-Size BAR Support (Enabled). Without ReBAR, expect 20-40% performance loss in gaming workloads. Verify activation: GPU-Z shows 'Resizable BAR: Enabled'. Requires UEFI mode, CSM disabled, Windows 10 20H1+ or Windows 11.",
            "keywords": ["ReBAR", "Resizable BAR", "Intel Arc", "performance"],
            "difficulty": "intermediate",
            "tags": ["gpu", "bios", "optimization"],
            "related_tools": ["GPU-Z", "BIOS"]
        },
        {
            "content": "Arc GPU driver updates are critical - monthly releases fix major performance issues. Use Intel Driver & Support Assistant for auto-updates or manual DDU (Display Driver Uninstaller) clean install quarterly. Example: Driver 31.0.101.4502 (Q4 2023) improved A750 performance 15-30% in DX11 titles vs launch drivers. Always benchmark before/after with 3DMark Time Spy to validate improvements.",
            "keywords": ["Intel Arc drivers", "DDU", "driver updates"],
            "difficulty": "beginner",
            "tags": ["drivers", "maintenance"],
            "related_tools": ["DDU", "Intel DSA", "3DMark"]
        }
    ]

    print(f"\nAdding {len(gpu_intel_arc_tips)} tips to gpu_intel_arc...")
    content = add_tips_to_category(content, "gpu_intel_arc", gpu_intel_arc_tips)

    # Write back to file
    print(f"\nWriting updated content to {TARGET_FILE}...")
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "=" * 80)
    print("FILE UPDATE COMPLETE!")
    print("=" * 80)
    print("\nVerify the changes by importing the module...")

if __name__ == "__main__":
    main()
