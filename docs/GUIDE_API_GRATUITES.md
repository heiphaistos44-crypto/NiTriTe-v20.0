# 🔑 GUIDE: Obtenir des Clés API GRATUITES pour NiTriTe

Ce guide explique comment obtenir des clés API **100% gratuites** pour utiliser les meilleurs modèles IA dans NiTriTe.

---

## 📋 SOMMAIRE

1. [**Gemini** (Google) - RECOMMANDÉ](#1-gemini-google---gratuit-50-requêtesjour)
2. [**OpenAI** (GPT-3.5/4) - Crédits gratuits](#2-openai-gpt-35-turbo---5-crédits-gratuits)
3. [**Mistral AI** - Gratuit](#3-mistral-ai---gratuit-tier)
4. [**DeepSeek** - Gratuit](#4-deepseek---100-gratuit)
5. [**Groq** - Ultra-rapide gratuit](#5-groq---ultra-rapide-gratuit)

---

## 1. GEMINI (Google) - Gratuit 50 requêtes/jour

**🏆 MEILLEUR CHOIX GRATUIT** - Puissant comme GPT-4, 100% gratuit!

### Étapes:

1. **Va sur**: https://aistudio.google.com/apikey
2. **Connecte-toi** avec ton compte Google (Gmail)
3. **Clique sur** "Create API Key"
4. **Copie la clé** (format: `AIzaSy...`)
5. **Colle dans NiTriTe** → Paramètres → APIs → Gemini

### Limites gratuites:
- ✅ **50 requêtes/jour** (largement suffisant)
- ✅ **Gemini 1.5 Pro** (aussi bon que GPT-4)
- ✅ **Gemini 1.5 Flash** (ultra-rapide)
- ✅ **Gemini 2.0 Flash** (experimental, très rapide)

**Aucune carte bancaire requise!** 🎉

---

## 2. OPENAI (GPT-3.5 Turbo) - $5 crédits gratuits

**Style Copilot** - Même technologie que ChatGPT

### Étapes:

1. **Va sur**: https://platform.openai.com/signup
2. **Crée un compte** (email + vérification téléphone)
3. **Va dans**: https://platform.openai.com/api-keys
4. **Clique sur** "Create new secret key"
5. **Copie la clé** (format: `sk-...`)
6. **Colle dans NiTriTe** → Paramètres → APIs → OpenAI

### Crédits gratuits:
- ✅ **$5 de crédits gratuits** lors de l'inscription
- ✅ **GPT-3.5-turbo** (~3-5 millions de mots avec $5)
- ✅ **GPT-4o-mini** (plus puissant, ~500k mots)

**⚠️ Carte bancaire requise** (mais non débitée si tu restes dans les $5 gratuits)

---

## 3. MISTRAL AI - Gratuit Tier

**Européen** - Excellent modèle style Copilot

### Étapes:

1. **Va sur**: https://console.mistral.ai/
2. **Crée un compte** (email)
3. **Va dans**: API Keys
4. **Clique sur** "Create new key"
5. **Copie la clé**
6. **Colle dans NiTriTe** → Paramètres → APIs → Mistral

### Limites gratuites:
- ✅ **Mistral-Small** gratuit
- ✅ **Bonne qualité** de réponses
- ✅ **Pas de carte bancaire**

---

## 4. DEEPSEEK - 100% Gratuit

**Chinois mais excellent** - Niveau GPT-4

### Étapes:

1. **Va sur**: https://platform.deepseek.com/
2. **Crée un compte**
3. **Va dans**: API Keys
4. **Génère une clé**
5. **Colle dans NiTriTe** → Paramètres → APIs → DeepSeek

### Limites gratuites:
- ✅ **Entièrement gratuit**
- ✅ **deepseek-chat** (très bon)
- ✅ **Pas de limite stricte**

---

## 5. GROQ - Ultra-rapide Gratuit

**Le plus RAPIDE** - Réponses instantanées

### Étapes:

1. **Va sur**: https://console.groq.com/
2. **Crée un compte** (GitHub ou email)
3. **Va dans**: API Keys
4. **Crée une clé**
5. **Colle dans NiTriTe** → Paramètres → APIs → Groq

### Limites gratuites:
- ✅ **Llama 3.3 70B** (excellent)
- ✅ **30 requêtes/minute** (très rapide!)
- ✅ **Gratuit sans limite mensuelle**

---

## 🎯 CONFIGURATION RECOMMANDÉE

Pour avoir le meilleur système avec fallback automatique:

### Configuration Ordre de priorité dans NiTriTe:

1. **Gemini** (priorité 1) - Le meilleur gratuit
2. **Groq** (priorité 2) - Le plus rapide
3. **DeepSeek** (priorité 3) - Backup illimité
4. **OpenAI** (priorité 4) - Si tu as crédits
5. **Mistral** (priorité 5) - Backup EU

Comme ça, si Gemini atteint sa limite quotidienne (50 req), NiTriTe bascule automatiquement sur Groq, puis DeepSeek!

---

## ❓ FAQ

### **Q: C'est vraiment gratuit?**
A: OUI! Gemini, Groq, DeepSeek = 100% gratuits. OpenAI = $5 offerts.

### **Q: Il faut une carte bancaire?**
A: NON pour Gemini, Groq, DeepSeek, Mistral. OUI pour OpenAI (mais non débitée dans les $5).

### **Q: Quelle est la meilleure?**
A: **Gemini 1.5 Pro** = meilleur rapport qualité/prix. Aussi bon que GPT-4, totalement gratuit!

### **Q: Les clés expirent?**
A: Non, elles restent valides jusqu'à ce que tu les révoque.

### **Q: C'est sécurisé?**
A: Oui, les clés sont stockées localement dans NiTriTe (fichier config crypté).

---

## 🚀 COMMENT CONFIGURER DANS NITRITE

1. Lance **NiTriTe_V18_Portable.exe**
2. Va dans **Paramètres** (⚙️)
3. Section **"APIs IA Avancées"**
4. Colle tes clés dans les champs
5. Clique **"Sauvegarder"**
6. Active le **mode en ligne** dans l'agent IA

C'est tout! 🎉

---

## 📊 COMPARAISON

| API | Gratuit | Qualité | Vitesse | Limite/jour |
|-----|---------|---------|---------|-------------|
| **Gemini 1.5 Pro** | ✅ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 50 req |
| **Groq (Llama 3.3)** | ✅ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 30/min |
| **DeepSeek** | ✅ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Illimité |
| **OpenAI GPT-3.5** | $5 gratuits | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $5 |
| **Mistral Small** | ✅ | ⭐⭐⭐ | ⭐⭐⭐ | Tier gratuit |

---

**Astuce Pro**: Configure **TOUTES** les APIs! Comme ça, si l'une ne fonctionne pas ou atteint sa limite, NiTriTe bascule automatiquement sur la suivante! 🚀
