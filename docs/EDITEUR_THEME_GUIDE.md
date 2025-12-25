# Guide Complet - Éditeur de Thème Dynamique

## Table des Matières

1. [Vue d'Ensemble](#vue-densemble)
2. [Accès à l'Éditeur](#accès-à-léditeur)
3. [Interface de l'Éditeur](#interface-de-léditeur)
4. [Onglet Couleurs](#onglet-couleurs)
5. [Onglet Espacements](#onglet-espacements)
6. [Onglet Bordures](#onglet-bordures)
7. [Onglet Polices](#onglet-polices)
8. [Onglet Presets](#onglet-presets)
9. [Prévisualisation Temps Réel](#prévisualisation-temps-réel)
10. [Gestion des Thèmes](#gestion-des-thèmes)
11. [Application du Thème](#application-du-thème)
12. [Conseils de Design](#conseils-de-design)
13. [Thèmes Accessibles](#thèmes-accessibles)
14. [Dépannage](#dépannage)
15. [Format JSON](#format-json)
16. [FAQ](#faq)
17. [Exemples de Thèmes](#exemples-de-thèmes)

---

## Vue d'Ensemble

L'**Éditeur de Thème Dynamique** de Nitrite V18.5 est un outil complet qui vous permet de personnaliser entièrement l'apparence de l'application en temps réel.

### Fonctionnalités Principales

- **Personnalisation complète** : 16 couleurs, 5 espacements, 3 rayons de bordure, 7 paramètres de police
- **Prévisualisation instantanée** : Visualisez vos changements en temps réel (< 50ms)
- **Gestion de thèmes** : Sauvegardez, chargez et exportez vos thèmes personnalisés
- **6 presets pré-configurés** : Thèmes professionnels prêts à l'emploi
- **Interface intuitive** : Organisation en onglets avec des contrôles faciles à utiliser

### Spécifications Techniques

- **Fenêtre** : 1200x800 pixels
- **Technologie** : CustomTkinter
- **Format de sauvegarde** : JSON
- **Compatibilité** : Nitrite V18.5 et versions ultérieures

---

## Accès à l'Éditeur

### Méthode 1 : Via les Paramètres (Recommandé)

1. Lancez Nitrite V18.5
2. Cliquez sur l'icône **Paramètres** dans la barre latérale
3. Naviguez vers la section **Apparence**
4. Cliquez sur le bouton **"Ouvrir l'Éditeur"**

### Méthode 2 : Test Standalone

Pour tester l'éditeur indépendamment de l'application :

```bash
cd "C:\Users\Utilisateur\Downloads\Nitrite-V18.5"
python test_theme_editor.py
```

### Raccourci Clavier (Futur)

Un raccourci clavier sera disponible dans une version future pour accéder rapidement à l'éditeur.

---

## Interface de l'Éditeur

### Disposition Générale

L'éditeur est divisé en trois zones principales :

```
┌─────────────────────────────────────────────────┐
│ Header (Titre + Boutons d'Action)              │
├──────────────────┬──────────────────────────────┤
│                  │                              │
│  Panel Gauche    │   Panel Droit                │
│  (Onglets)       │   (Prévisualisation)         │
│                  │                              │
│  - Couleurs      │   - Widgets exemples         │
│  - Espacements   │   - Mise à jour temps réel   │
│  - Bordures      │                              │
│  - Polices       │                              │
│  - Presets       │                              │
│                  │                              │
└──────────────────┴──────────────────────────────┘
```

### Header - Boutons d'Action

| Bouton | Action | Description |
|--------|--------|-------------|
| **Nouveau** | Reset | Réinitialise tous les paramètres aux valeurs par défaut |
| **Charger** | Load | Charge un thème sauvegardé depuis `data/themes/` |
| **Sauvegarder** | Save | Sauvegarde le thème actuel dans `data/themes/` |
| **Exporter** | Export | Exporte le thème vers n'importe quel emplacement |
| **Appliquer** | Apply | Applique le thème à l'application (redémarrage requis) |

---

## Onglet Couleurs

### Vue d'Ensemble

L'onglet **Couleurs** permet de personnaliser **16 paramètres de couleur** répartis en 5 catégories :

### 1. Couleurs de Fond (5 paramètres)

| Paramètre | Utilisation | Défaut |
|-----------|-------------|--------|
| **Fond Principal** (`bg_primary`) | Arrière-plan principal de l'application | `#0a0a0a` |
| **Fond Secondaire** (`bg_secondary`) | Zones de contenu secondaire | `#151515` |
| **Fond Tertiaire** (`bg_tertiary`) | Zones tertiaires, sous-sections | `#202020` |
| **Fond Élevé** (`bg_elevated`) | Cartes, éléments surélevés | `#252525` |
| **Fond Survol** (`bg_hover`) | État de survol des éléments | `#2a2a2a` |

### 2. Couleurs d'Accent (3 paramètres)

| Paramètre | Utilisation | Défaut |
|-----------|-------------|--------|
| **Accent Principal** (`accent_primary`) | Boutons, liens, éléments interactifs | `#ff6b35` |
| **Accent Survol** (`accent_hover`) | État de survol des éléments d'accent | `#ff8555` |
| **Accent Pressé** (`accent_pressed`) | État pressé des boutons | `#ff5020` |

### 3. Couleurs de Texte (3 paramètres)

| Paramètre | Utilisation | Défaut |
|-----------|-------------|--------|
| **Texte Principal** (`text_primary`) | Titres, texte important | `#ffffff` |
| **Texte Secondaire** (`text_secondary`) | Descriptions, labels | `#b0b0b0` |
| **Texte Tertiaire** (`text_tertiary`) | Texte peu important, désactivé | `#808080` |

### 4. Couleurs Sémantiques (4 paramètres)

| Paramètre | Utilisation | Défaut |
|-----------|-------------|--------|
| **Succès** (`success`) | Messages de succès, confirmations | `#4caf50` |
| **Avertissement** (`warning`) | Alertes, avertissements | `#ff9800` |
| **Erreur** (`error`) | Messages d'erreur, actions destructives | `#f44336` |
| **Information** (`info`) | Messages informatifs | `#2196f3` |

### 5. Couleurs de Bordure (2 paramètres)

| Paramètre | Utilisation | Défaut |
|-----------|-------------|--------|
| **Bordure Par Défaut** (`border_default`) | Bordures standard | `#2a2a2a` |
| **Bordure Focus** (`border_focus`) | Bordures des éléments en focus | `#ff6b35` |

### Utilisation du Sélecteur de Couleur

1. **Aperçu** : Un bouton coloré affiche la couleur actuelle
2. **Code Hex** : Le code hexadécimal est affiché à côté
3. **Modification** :
   - Cliquez sur le bouton aperçu OU
   - Cliquez sur le bouton "Choisir"
4. **Sélecteur** : Utilisez le sélecteur de couleur pour choisir une nouvelle teinte
5. **Validation** : La prévisualisation se met à jour instantanément

### Conseils pour les Couleurs

- **Contraste** : Assurez-vous d'un bon contraste entre le texte et le fond (ratio 4.5:1 minimum)
- **Cohérence** : Utilisez des teintes de la même famille pour les fonds
- **Hiérarchie** : Les couleurs de texte doivent refléter l'importance (primaire > secondaire > tertiaire)
- **Accessibilité** : Testez avec des outils de simulation de daltonisme

---

## Onglet Espacements

### Vue d'Ensemble

L'onglet **Espacements** contrôle les **marges et paddings** à travers l'application avec 5 niveaux.

### Paramètres d'Espacement

| Niveau | Plage | Défaut | Utilisation |
|--------|-------|--------|-------------|
| **XS** (Extra Small) | 2-8px | 4px | Espaces très réduits, séparateurs fins |
| **SM** (Small) | 4-16px | 8px | Petits espacements, marges internes |
| **MD** (Medium) | 8-32px | 16px | Espacements standards, entre sections |
| **LG** (Large) | 16-48px | 24px | Grands espacements, entre blocs importants |
| **XL** (Extra Large) | 24-64px | 32px | Espacements très larges, marges extérieures |

### Utilisation des Sliders

1. **Déplacer le curseur** pour ajuster la valeur
2. **Valeur en temps réel** affichée à droite du slider
3. **Prévisualisation** mise à jour instantanément

### Impact des Espacements

- **XS** : Utilisé pour les séparateurs, les icônes
- **SM** : Padding des boutons, marges entre éléments proches
- **MD** : Espacement standard entre widgets, sections
- **LG** : Marges importantes entre groupes de contenu
- **XL** : Marges extérieures de l'application, grands blocs

### Recommandations

- **Cohérence** : Utilisez toujours les mêmes niveaux pour les mêmes types d'éléments
- **Progression** : Chaque niveau devrait être environ 1.5-2x le niveau précédent
- **Respiration** : Ne sous-estimez pas l'importance de l'espace blanc

---

## Onglet Bordures

### Vue d'Ensemble

L'onglet **Bordures** contrôle les **rayons de courbure** des éléments arrondis avec 3 niveaux.

### Paramètres de Rayon

| Niveau | Plage | Défaut | Utilisation |
|--------|-------|--------|-------------|
| **SM** (Small) | 0-16px | 8px | Boutons, petits éléments |
| **MD** (Medium) | 4-32px | 16px | Cartes, sections moyennes |
| **LG** (Large) | 8-48px | 24px | Grands conteneurs, modales |

### Styles Possibles

#### Style Carré (Rayons à 0)
```
SM = 0px, MD = 0px, LG = 0px
→ Design moderne, géométrique, professionnel
```

#### Style Doux (Rayons modérés)
```
SM = 8px, MD = 16px, LG = 24px (défaut)
→ Équilibre moderne/amical, recommandé
```

#### Style Très Arrondi (Rayons élevés)
```
SM = 16px, MD = 32px, LG = 48px
→ Design ludique, moderne, doux
```

### Impact Visuel

- **Rayons petits (0-8px)** : Aspect professionnel, sérieux
- **Rayons moyens (8-16px)** : Équilibré, moderne
- **Rayons grands (16-48px)** : Doux, accessible, amical

---

## Onglet Polices

### Vue d'Ensemble

L'onglet **Polices** permet de personnaliser la **famille de police** et **6 tailles** différentes.

### 1. Famille de Police

Sélectionnez parmi 6 polices système :

| Police | Style | Recommandé pour |
|--------|-------|-----------------|
| **Segoe UI** (défaut) | Moderne, lisible | Usage général |
| **Arial** | Classique, universelle | Compatibilité maximale |
| **Helvetica** | Élégante, professionnelle | Design soigné |
| **Calibri** | Moderne, Microsoft | Documents Office |
| **Consolas** | Monospace | Code, terminal |
| **Courier New** | Monospace classique | Texte technique |

### 2. Tailles de Police

| Niveau | Plage | Défaut | Utilisation |
|--------|-------|--------|-------------|
| **XS** | 8-14px | 10px | Notes de bas de page, métadonnées |
| **SM** | 9-16px | 11px | Labels, texte secondaire |
| **MD** | 11-18px | 13px | Texte standard, corps de texte |
| **LG** | 14-22px | 16px | Sous-titres, emphase |
| **XL** | 18-28px | 20px | Titres de section |
| **2XL** | 20-36px | 24px | Titres principaux, headers |

### Hiérarchie Typographique

```
2XL (24px) → Titre de page
XL (20px)  → Titre de section
LG (16px)  → Sous-titre
MD (13px)  → Texte standard
SM (11px)  → Labels, descriptions
XS (10px)  → Métadonnées, notes
```

### Conseils Typographiques

- **Lisibilité** : Minimum 11px pour le texte principal
- **Contraste de taille** : Ratio de 1.5-2x entre niveaux adjacents
- **Cohérence** : Utilisez toujours les mêmes tailles pour les mêmes types de contenu
- **Longueur de ligne** : 50-75 caractères maximum pour une lecture optimale

---

## Onglet Presets

### Vue d'Ensemble

L'onglet **Presets** offre **6 thèmes pré-configurés** professionnels, prêts à l'emploi.

### Presets Disponibles

#### 1. Orange NiTriTe (Défaut)
```
Accent: #ff6b35 (Orange vif)
Style: Énergique, moderne, signature de la marque
Usage: Défaut, polyvalent
```

#### 2. Bleu Pro
```
Accent: #2196f3 (Bleu professionnel)
Style: Professionnel, corporate, fiable
Usage: Environnements professionnels, bureautique
```

#### 3. Vert Tech
```
Accent: #4caf50 (Vert technologique)
Style: Écologique, innovant, tech
Usage: Développement, projets tech
```

#### 4. Violet Creative
```
Accent: #9c27b0 (Violet créatif)
Style: Créatif, artistique, original
Usage: Design, créativité, multimédia
```

#### 5. Rouge Energy
```
Accent: #f44336 (Rouge énergique)
Style: Dynamique, urgent, puissant
Usage: Actions importantes, urgence
```

#### 6. Cyan Fresh
```
Accent: #00bcd4 (Cyan frais)
Style: Frais, moderne, digital
Usage: Applications modernes, interfaces légères
```

### Application d'un Preset

1. **Cliquez** sur le bouton "Appliquer" du preset désiré
2. **Visualisez** instantanément le changement dans la prévisualisation
3. **Les couleurs d'accent** sont mises à jour (primary, hover, pressed, border_focus)
4. **Personnalisez** ensuite si désiré
5. **Sauvegardez** votre configuration

### Personnalisation après Preset

Les presets ne modifient que les couleurs d'accent. Vous pouvez ensuite :
- Ajuster les couleurs de fond
- Modifier les espacements
- Changer les bordures
- Personnaliser les polices

---

## Prévisualisation Temps Réel

### Vue d'Ensemble

La **prévisualisation temps réel** vous permet de visualiser instantanément vos modifications sur des widgets d'exemple.

### Widgets Prévisualisés

#### 1. Titre
- Police personnalisée (2XL)
- Couleur texte primaire
- Exemple : "Exemple de Titre"

#### 2. Carte
- Fond élevé (`bg_elevated`)
- Rayon de bordure MD
- Titre (police LG) + sous-titre (police MD)
- Texte primaire et secondaire

#### 3. Boutons
- **Bouton Principal** : Couleur accent, rayon SM
- **Bouton Secondaire** : Fond élevé, rayon SM

#### 4. Boutons Sémantiques
- **Succès** : Vert
- **Attention** : Orange/Jaune
- **Erreur** : Rouge
- **Info** : Bleu

#### 5. Champ de Saisie
- Fond secondaire
- Bordure par défaut
- Rayon SM
- Placeholder

#### 6. Contrôles
- **Switch** : Accent primary
- **Slider** : Accent primary/hover
- **Progress Bar** : Accent primary

### Performance

- **Mise à jour** : < 50ms après chaque modification
- **Fluidité** : Aucun ralentissement, même avec modifications rapides
- **Précision** : Rendu identique à l'application réelle

---

## Gestion des Thèmes

### Sauvegarde d'un Thème

1. **Personnalisez** votre thème avec l'éditeur
2. **Cliquez** sur le bouton "Sauvegarder"
3. **Entrez** un nom pour votre thème (ex: "Mon Thème Bleu")
4. **Le thème** est sauvegardé dans `data/themes/mon_theme_bleu.json`
5. **Confirmation** : Un message vous indique le succès de la sauvegarde

### Chargement d'un Thème

1. **Cliquez** sur le bouton "Charger"
2. **Sélectionnez** un fichier JSON dans `data/themes/`
3. **Le thème** est chargé instantanément
4. **Tous les paramètres** sont restaurés (couleurs, espacements, bordures, polices)
5. **Prévisualisation** mise à jour automatiquement

### Export d'un Thème

1. **Cliquez** sur le bouton "Exporter"
2. **Choisissez** un emplacement (n'importe où sur votre système)
3. **Nommez** le fichier (ex: `mon_theme.json`)
4. **Le thème** est exporté au format JSON
5. **Partageable** : Vous pouvez partager le fichier avec d'autres utilisateurs

### Nouveau Thème

1. **Cliquez** sur le bouton "Nouveau"
2. **Confirmation** demandée (réinitialisation)
3. **Tous les paramètres** reviennent aux valeurs par défaut
4. **Recommencez** votre personnalisation depuis zéro

### Organisation des Thèmes

```
data/themes/
├── mon_theme_bleu.json
├── theme_travail.json
├── theme_soir.json
├── theme_presentation.json
└── ...
```

**Recommandations :**
- Nommez clairement vos thèmes (usage, couleur dominante)
- Créez des thèmes pour différents contextes (travail, loisir, présentation)
- Exportez régulièrement vos thèmes favoris comme backup

---

## Application du Thème

### Processus d'Application

1. **Personnalisez** votre thème dans l'éditeur
2. **Cliquez** sur le bouton "Appliquer"
3. **Confirmation** demandée avec message :
   ```
   Voulez-vous appliquer ce thème à l'application?

   Note: L'application devra être redémarrée pour que
   tous les changements prennent effet.
   ```
4. **Acceptez** la confirmation
5. **Le thème** est sauvegardé dans `~/.nitrite_config.json`
6. **Redémarrez** Nitrite pour voir tous les changements

### Configuration Utilisateur

Le thème est stocké dans :
```
~/.nitrite_config.json
```

Contenu :
```json
{
  "custom_theme": {
    "name": "Mon Thème",
    "colors": { ... },
    "spacing": { ... },
    "radius": { ... },
    "fonts": { ... }
  },
  "theme": "Orange NiTriTe",
  "appearance_mode": "dark"
}
```

### Restauration du Thème Par Défaut

Pour revenir au thème par défaut :

**Méthode 1 - Via l'éditeur :**
1. Ouvrez l'éditeur
2. Cliquez sur "Nouveau"
3. Cliquez sur "Appliquer"
4. Redémarrez

**Méthode 2 - Via les paramètres :**
1. Paramètres → Actions
2. "Réinitialiser Configuration"
3. Confirmation
4. Redémarrez

**Méthode 3 - Manuel :**
1. Supprimez le fichier `~/.nitrite_config.json`
2. Redémarrez Nitrite

---

## Conseils de Design

### Principes Généraux

#### 1. Contraste et Lisibilité
- **Texte/Fond** : Ratio de contraste minimum 4.5:1 (WCAG AA)
- **Éléments interactifs** : Bien distinguables du fond
- **Focus** : États de focus clairement visibles

#### 2. Cohérence
- **Couleurs** : Palette limitée (3-5 couleurs principales max)
- **Espacements** : Utiliser les mêmes valeurs pour les mêmes types d'éléments
- **Typographie** : Maximum 2-3 polices différentes

#### 3. Hiérarchie Visuelle
- **Tailles** : Les éléments importants sont plus grands
- **Couleurs** : L'accent attire l'attention
- **Espacement** : Grouper les éléments liés

### Palettes de Couleurs Recommandées

#### Palette Sombre Professionnelle
```
Fonds:    #0a0a0a → #151515 → #202020
Accent:   #2196f3 (Bleu)
Texte:    #ffffff → #b0b0b0 → #808080
```

#### Palette Sombre Chaleureuse
```
Fonds:    #1a1612 → #2d2419 → #3f3220
Accent:   #ff6b35 (Orange)
Texte:    #f5f5f5 → #c9c9c9 → #9d9d9d
```

#### Palette Sombre Fraîche
```
Fonds:    #0d1117 → #161b22 → #21262d
Accent:   #00bcd4 (Cyan)
Texte:    #c9d1d9 → #8b949e → #484f58
```

### Erreurs à Éviter

❌ **Trop de couleurs** : Limitez-vous à une palette cohérente
❌ **Contraste insuffisant** : Testez toujours la lisibilité
❌ **Espacements incohérents** : Utilisez le système de spacing
❌ **Polices trop petites** : Minimum 11px pour le texte
❌ **Bordures trop arrondies** : Peut donner un aspect non professionnel

### Outils Recommandés

- **Contrast Checker** : WebAIM Contrast Checker
- **Palette Generator** : Coolors.co, Adobe Color
- **Accessibilité** : axe DevTools, WAVE

---

## Thèmes Accessibles

### Principes d'Accessibilité

#### 1. Contraste WCAG

**Norme AA (minimum) :**
- Texte normal : 4.5:1
- Texte large : 3:1

**Norme AAA (recommandé) :**
- Texte normal : 7:1
- Texte large : 4.5:1

#### 2. Daltonisme

Testez votre thème avec des simulateurs de daltonisme :
- **Protanopie** (rouge)
- **Deutéranopie** (vert)
- **Tritanopie** (bleu)

#### 3. Mode Sombre Adapté

- **Évitez** le blanc pur (#ffffff) sur fond noir pur (#000000)
- **Préférez** gris clair (#f0f0f0) sur gris très foncé (#0a0a0a)
- **Réduisez** l'intensité des couleurs vives

### Thème Haute Accessibilité

```json
{
  "name": "Haute Accessibilité",
  "colors": {
    "bg_primary": "#0a0a0a",
    "bg_secondary": "#1a1a1a",
    "accent_primary": "#ffd700",
    "text_primary": "#f0f0f0",
    "text_secondary": "#d0d0d0"
  },
  "spacing": {
    "xs": 6, "sm": 12, "md": 20, "lg": 32, "xl": 48
  },
  "fonts": {
    "size_md": 15,
    "size_lg": 18
  }
}
```

**Caractéristiques :**
- Contraste élevé (> 10:1)
- Espacements généreux
- Polices plus grandes
- Couleur d'accent très visible

---

## Dépannage

### Problème : L'éditeur ne s'ouvre pas

**Solutions :**
1. Vérifiez que vous êtes dans les Paramètres → Apparence
2. Vérifiez que le fichier `theme_editor_dynamic.py` existe
3. Testez avec `python test_theme_editor.py`
4. Vérifiez les logs dans `data/logs/`

### Problème : Les modifications ne sont pas visibles

**Solutions :**
1. Vérifiez la prévisualisation (doit se mettre à jour instantanément)
2. Cliquez sur "Appliquer" pour appliquer à l'application
3. Redémarrez l'application après avoir appliqué
4. Vérifiez le fichier `~/.nitrite_config.json`

### Problème : Impossible de sauvegarder un thème

**Solutions :**
1. Vérifiez que le dossier `data/themes/` existe
2. Vérifiez les permissions d'écriture
3. Utilisez "Exporter" vers un autre emplacement
4. Vérifiez l'espace disque disponible

### Problème : Thème chargé incorrect

**Solutions :**
1. Vérifiez que le fichier JSON est valide
2. Rechargez le thème depuis l'éditeur
3. Utilisez "Nouveau" pour réinitialiser
4. Supprimez `~/.nitrite_config.json` et redémarrez

### Problème : Performance lente

**Solutions :**
1. Fermez les autres applications gourmandes
2. Vérifiez les ressources système (RAM, CPU)
3. Redémarrez l'éditeur
4. Redémarrez l'application complète

---

## Format JSON

### Structure Complète

```json
{
  "name": "Nom du Thème",
  "created_at": "2025-12-18T20:00:00",
  "colors": {
    "bg_primary": "#0a0a0a",
    "bg_secondary": "#151515",
    "bg_tertiary": "#202020",
    "bg_elevated": "#252525",
    "bg_hover": "#2a2a2a",
    "accent_primary": "#ff6b35",
    "accent_hover": "#ff8555",
    "accent_pressed": "#ff5020",
    "text_primary": "#ffffff",
    "text_secondary": "#b0b0b0",
    "text_tertiary": "#808080",
    "success": "#4caf50",
    "warning": "#ff9800",
    "error": "#f44336",
    "info": "#2196f3",
    "border_default": "#2a2a2a",
    "border_focus": "#ff6b35"
  },
  "spacing": {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32
  },
  "radius": {
    "sm": 8,
    "md": 16,
    "lg": 24
  },
  "fonts": {
    "family": "Segoe UI",
    "size_xs": 10,
    "size_sm": 11,
    "size_md": 13,
    "size_lg": 16,
    "size_xl": 20,
    "size_2xl": 24
  }
}
```

### Édition Manuelle

Vous pouvez éditer manuellement les fichiers JSON :

1. **Ouvrez** le fichier avec un éditeur de texte
2. **Modifiez** les valeurs désirées
3. **Sauvegardez** (respectez la syntaxe JSON)
4. **Chargez** dans l'éditeur ou redémarrez l'application

**Attention :** Respectez les contraintes :
- Couleurs : format hexadécimal `#rrggbb`
- Espacements : entiers (px)
- Rayons : entiers (px)
- Tailles de police : entiers (px)
- Famille de police : chaîne de caractères

---

## FAQ

### Q1 : Combien de thèmes puis-je créer ?
**R :** Illimité ! Vous pouvez créer autant de thèmes que vous le souhaitez. Ils sont stockés dans `data/themes/`.

### Q2 : Puis-je partager mes thèmes ?
**R :** Oui ! Exportez votre thème en JSON et partagez le fichier. Les autres utilisateurs peuvent le charger via "Charger".

### Q3 : Les thèmes affectent-ils les performances ?
**R :** Non. Les thèmes n'ont aucun impact sur les performances de l'application.

### Q4 : Puis-je avoir des thèmes différents pour le jour/nuit ?
**R :** Pas automatiquement pour l'instant, mais vous pouvez créer deux thèmes et les charger manuellement.

### Q5 : Comment revenir au thème par défaut ?
**R :** Utilisez le bouton "Nouveau" dans l'éditeur, puis "Appliquer", ou réinitialisez la configuration dans les Paramètres.

### Q6 : Les presets peuvent-ils être modifiés ?
**R :** Les presets eux-mêmes ne peuvent pas être modifiés, mais vous pouvez appliquer un preset puis le personnaliser et le sauvegarder sous un nouveau nom.

### Q7 : Quelle est la différence entre "Sauvegarder" et "Exporter" ?
**R :**
- **Sauvegarder** : Enregistre dans `data/themes/` (facile à charger)
- **Exporter** : Enregistre n'importe où (partage, backup)

### Q8 : Puis-je utiliser mes propres polices ?
**R :** Actuellement, seules les 6 polices système proposées sont disponibles. Le support de polices personnalisées est prévu pour une version future.

### Q9 : La prévisualisation est-elle exacte ?
**R :** Oui, à 100%. Le rendu de la prévisualisation est identique à celui de l'application réelle.

### Q10 : Que faire si je perds mon thème ?
**R :** Exportez régulièrement vos thèmes favoris comme backup. Vous pouvez aussi vérifier `data/themes/` pour les thèmes sauvegardés.

---

## Exemples de Thèmes

### 1. Thème Minimaliste Noir et Blanc

```json
{
  "name": "Minimaliste B&W",
  "colors": {
    "bg_primary": "#000000",
    "bg_secondary": "#0a0a0a",
    "bg_elevated": "#151515",
    "accent_primary": "#ffffff",
    "accent_hover": "#f0f0f0",
    "text_primary": "#ffffff",
    "text_secondary": "#b0b0b0"
  },
  "radius": {
    "sm": 0,
    "md": 0,
    "lg": 0
  }
}
```

### 2. Thème Bleu Nuit

```json
{
  "name": "Bleu Nuit",
  "colors": {
    "bg_primary": "#0d1117",
    "bg_secondary": "#161b22",
    "bg_tertiary": "#21262d",
    "accent_primary": "#58a6ff",
    "accent_hover": "#79c0ff",
    "text_primary": "#c9d1d9"
  },
  "spacing": {
    "md": 18,
    "lg": 28
  }
}
```

### 3. Thème Chaleureux Automne

```json
{
  "name": "Automne Chaleureux",
  "colors": {
    "bg_primary": "#1a1612",
    "bg_secondary": "#2d2419",
    "accent_primary": "#ff6b35",
    "accent_hover": "#ff8555",
    "success": "#d4af37",
    "text_primary": "#f5e6d3"
  },
  "radius": {
    "sm": 12,
    "md": 20,
    "lg": 32
  }
}
```

---

## Conclusion

L'**Éditeur de Thème Dynamique** vous offre un contrôle total sur l'apparence de Nitrite V18.5. Expérimentez, créez, partagez vos thèmes et personnalisez votre expérience !

**Ressources Supplémentaires :**
- Documentation technique : `EDITEUR_THEME_README.md`
- Rapport complet : `RAPPORT_FINAL_COMPLET.md`
- Test standalone : `test_theme_editor.py`

**Support :**
- GitHub Issues : [lien vers repo]
- Documentation : `docs/`

---

**Version du guide :** 1.0
**Date de création :** 2025-12-18
**Compatibilité :** Nitrite V18.5+
