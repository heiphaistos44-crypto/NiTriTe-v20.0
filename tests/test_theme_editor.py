#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Standalone - Éditeur de Thème Dynamique
Permet de tester l'éditeur de thème indépendamment de l'application
"""

import sys
import os

# Ajouter le dossier src au path pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import customtkinter as ctk
from v14_mvp.theme_editor_dynamic import ThemeEditorDynamic

def main():
    """Lancer le test de l'éditeur de thème"""
    print("=" * 60)
    print("Test de l'Éditeur de Thème Dynamique - NiTriTe V18.5")
    print("=" * 60)
    print()
    print("Chargement de l'interface...")

    # Configuration
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Créer la fenêtre principale (cachée)
    root = ctk.CTk()
    root.title("Test - Éditeur de Thème")
    root.withdraw()  # Cacher la fenêtre principale

    print("Interface chargée.")
    print()
    print("Ouverture de l'éditeur de thème...")
    print()
    print("Fonctionnalités disponibles:")
    print("  - Onglet Couleurs: 16 paramètres de couleur")
    print("  - Onglet Espacements: 5 niveaux d'espacement")
    print("  - Onglet Bordures: 3 rayons de bordure")
    print("  - Onglet Polices: 1 famille + 6 tailles")
    print("  - Onglet Presets: 6 thèmes pré-configurés")
    print("  - Prévisualisation temps réel")
    print("  - Sauvegarde/Chargement/Export de thèmes")
    print()
    print("Testez les différentes fonctionnalités:")
    print("  1. Changez des couleurs et observez la prévisualisation")
    print("  2. Appliquez un preset")
    print("  3. Sauvegardez votre thème personnalisé")
    print("  4. Chargez un thème existant")
    print("  5. Exportez un thème")
    print()

    # Ouvrir l'éditeur
    try:
        editor = ThemeEditorDynamic(root)
        editor.focus()

        print("Éditeur ouvert avec succès!")
        print()
        print("Fermez l'éditeur pour terminer le test.")
        print("=" * 60)

        # Démarrer la boucle principale
        root.mainloop()

        print()
        print("Test terminé avec succès!")

    except Exception as e:
        import traceback
        print()
        print("ERREUR lors de l'ouverture de l'éditeur:")
        print(f"  Type: {type(e).__name__}")
        print(f"  Message: {str(e)}")
        print()
        print("Traceback complet:")
        print(traceback.format_exc())
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
