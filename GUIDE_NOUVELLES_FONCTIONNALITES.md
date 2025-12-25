# Guide Rapide - Nouvelles Fonctionnalités V18.5

## 🚀 Démarrage Rapide

### Mode Portable
**Aucune installation requise - Zéro trace sur le PC**

1. Copiez `NiTriTe_V18_Portable.exe` sur votre clé USB
2. Double-cliquez pour lancer
3. Tous les fichiers sont créés à côté de l'exe
4. Fermez et relancez → vos paramètres sont conservés

**Dossiers créés automatiquement:**
- `config/` - Vos paramètres et thèmes
- `logs/` - Historique des actions
- `temp/` - Fichiers temporaires (nettoyés à la fermeture)

---

## 🔧 Installer des Pilotes Spécifiques

### Page: Updates → Pilotes Génériques Windows

**Avant V18.5:**
- Un seul bouton "Installer Tous les Pilotes"
- Installation massive de tout

**Nouveau dans V18.5:**
4 boutons séparés pour installer uniquement ce dont vous avez besoin:

1. **🔌 Installer Pilotes USB**
   - Clé USB non reconnue?
   - Ports USB qui ne fonctionnent pas?
   - → Cliquez ici

2. **💿 Installer Pilotes Chipset**
   - Carte mère pas optimisée?
   - Problèmes de performance système?
   - → Cliquez ici

3. **📡 Installer Pilotes Bluetooth**
   - Bluetooth introuvable?
   - Appareils Bluetooth ne se connectent pas?
   - → Cliquez ici

4. **🖨️ Installer Pilotes Imprimantes**
   - Imprimante non détectée?
   - Impression impossible?
   - → Cliquez ici

**Comment ça marche:**
1. Cliquez sur le bouton correspondant
2. Confirmez l'action (droits admin requis)
3. Un terminal vert s'ouvre → scan des périphériques
4. Windows Update s'ouvre automatiquement
5. Cliquez sur "Rechercher des mises à jour"
6. Les pilotes sont détectés et proposés
7. Installez les pilotes trouvés

**Avantage:**
- Installation ciblée (rapide)
- Pas de surcharge de pilotes inutiles
- Terminal affiche la progression en temps réel

---

## 📦 Ajouter Vos Propres Outils

### Page: Diagnostic → Outils de Diagnostic

**Nouveau dans V18.5:**
Vous pouvez ajouter vos propres applications portables à NiTriTe!

### Méthode 1: Ajout Manuel (avec interface graphique)

1. **Cliquez sur "➕ Ajouter Application"** (en haut à droite)

2. **Fenêtre qui s'ouvre:**
   - Cliquez "📁 Parcourir" → sélectionnez votre .exe
   - Le nom se remplit automatiquement (modifiable)
   - Choisissez une icône emoji (14 au choix)
   - Cliquez "Enregistrer"

3. **Résultat:**
   - Votre app apparaît dans la liste des outils
   - Bouton cliquable pour la lancer
   - Bouton ❌ pour la supprimer

**Exemple d'utilisation:**
```
Vous avez "Speccy.exe" sur votre PC?
→ Ajoutez-le avec l'emoji 🔬
→ Lancez-le directement depuis NiTriTe
```

### Méthode 2: Auto-Scan (sans configuration)

**Encore plus simple:**

1. **Créez le dossier** (si pas déjà fait):
   ```
   NiTriTe_V18_Portable.exe
   └── logiciel/
       └── Custom/    ← Placez vos .exe ici
   ```

2. **Copiez vos .exe dans `logiciel/Custom/`**
   Exemple:
   ```
   logiciel/Custom/
   ├── Speccy.exe
   ├── TreeSize.exe
   └── MonOutil.exe
   ```

3. **Redémarrez NiTriTe**
   → Tous les .exe sont automatiquement détectés
   → Boutons créés avec icône 📦

**Avantage:**
- Zéro configuration
- Ajoutez/retirez des .exe à volonté
- Détection automatique au démarrage

### Supprimer une App

**App ajoutée manuellement:**
- Cliquez sur le bouton ❌
- Confirmez la suppression
- L'app disparaît

**App auto-scannée:**
- Cliquez sur ❌ → message d'info
- Pour la supprimer définitivement:
  → Supprimez le .exe du dossier `logiciel/Custom/`

---

## 📋 Terminal des Logs Amélioré

### Page: Logs

**Nouveau dans V18.5:**
Terminal redimensionnable pour plus de confort

**Comment l'utiliser:**

1. **Bouton ▼ Agrandir Terminal**
   - Cliquez pour agrandir le terminal
   - Hauteur passe de 300px → 600px
   - Meilleure visibilité des logs

2. **Bouton ▲ Réduire Terminal**
   - Cliquez pour réduire
   - Libère de l'espace pour les logs principaux

**Fix du scroll:**
- Scroll dans le terminal → ne fait plus défiler toute la page
- Expérience plus fluide

---

## 💡 Astuces et Conseils

### Portabilité Maximale
```
✅ À FAIRE:
- Lancez l'exe depuis une clé USB
- Copiez tout le dossier (exe + config + logiciel)
- Utilisez sur n'importe quel PC Windows

❌ À NE PAS FAIRE:
- Ne déplacez pas juste l'exe seul
- Gardez les dossiers logiciel/ et Script Windows/
```

### Organisation des Custom Apps
```
Recommandations:
- Utilisez des noms courts et clairs
- Choisissez des emojis cohérents:
  📊 → Monitoring/Stats
  🔧 → Outils de réparation
  🛠️ → Utilitaires système
  🔍 → Diagnostic
  📦 → Apps portables génériques
```

### Pilotes
```
Ordre recommandé d'installation:
1. Chipset (base système)
2. USB (périphériques)
3. Bluetooth (sans fil)
4. Imprimantes (si nécessaire)
```

---

## 🔍 Où Trouver Quoi?

### Structure Complète
```
NiTriTe_V18_Portable.exe
│
├── config/                    # ⚙️ Paramètres
│   ├── nitrite_config.json   # Configuration app
│   └── nitrite_theme.json    # Thème sombre/clair
│
├── logs/                      # 📋 Historique
│   ├── nitrite_v18_*.log     # Logs de session
│   └── errors.log            # Erreurs uniquement
│
├── temp/                      # 🗑️ Temporaire
│   ├── downloads/            # Téléchargements
│   ├── scripts/              # Scripts .bat/.ps1
│   └── benchmark/            # Tests performance
│
├── logiciel/                  # 🔧 Outils
│   ├── Custom/               # 📦 VOS APPS ICI
│   ├── HWMonitor/
│   ├── CrystalDiskInfo/
│   └── [+25 outils]
│
├── Script Windows/            # 📜 Scripts système
│
└── data/                      # 💾 Données
    ├── programs.json         # Liste programmes
    └── custom_diagnostic_tools.json  # Apps perso
```

---

## ❓ FAQ

**Q: Puis-je ajouter plusieurs .exe dans Custom/?**
R: Oui, illimité! Tous seront auto-détectés.

**Q: Les apps custom sont-elles sauvegardées?**
R: Oui, dans `data/custom_diagnostic_tools.json` (apps manuelles) et rescannées au démarrage (apps auto).

**Q: Comment changer l'icône d'une app auto-scannée?**
R: Supprimez-la avec ❌, puis rajoutez-la manuellement avec "➕ Ajouter Application".

**Q: Les pilotes individuels remplacent-ils "Installer Tous"?**
R: Non, les deux options existent. Utilisez "Tous" pour une installation complète, ou les boutons individuels pour cibler.

**Q: L'app laisse-t-elle des traces sur le PC?**
R: Non! Tout est portable. Les anciens configs dans `C:\Users\[User]\` sont automatiquement migrés.

**Q: Puis-je utiliser mes apps custom sur un autre PC?**
R: Oui, si les .exe sont portables. Copiez tout le dossier `logiciel/Custom/`.

---

## 📞 Support

**En cas de problème:**
1. Consultez `logs/errors.log`
2. Vérifiez que les dossiers `logiciel/` et `Script Windows/` sont présents
3. Relancez l'app avec droits admin si nécessaire

**Fichiers importants à conserver:**
- `config/` → Vos paramètres
- `logiciel/Custom/` → Vos apps personnalisées
- `data/custom_diagnostic_tools.json` → Config apps manuelles

---

**Version**: V18.5 Portable
**Build**: 2025-12-24
**Taille**: ~745 MB
**Compatibilité**: Windows 10/11
