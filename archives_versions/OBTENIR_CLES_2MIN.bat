@echo off
chcp 65001 >nul
cls
color 0A

echo ═══════════════════════════════════════════════════════════════════
echo    🔑 ASSISTANT RAPIDE - OBTENIR TES CLÉS API GRATUITES
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Ce script va t'ouvrir les pages pour obtenir tes clés GRATUITES!
echo.
echo ⏱️  Temps total: 2-5 minutes pour TOUT configurer
echo 💰 Coût: 0€ (100%% gratuit)
echo 💳 Carte bancaire: NON requise
echo.
pause

cls
echo ═══════════════════════════════════════════════════════════════════
echo    📋 ÉTAPE 1/3 - GEMINI (Google) - LE MEILLEUR GRATUIT
echo ═══════════════════════════════════════════════════════════════════
echo.
echo ✨ Gemini 1.5 Pro = Aussi puissant que GPT-4, GRATUIT!
echo ✅ 50 requêtes/jour (largement suffisant)
echo ✅ Pas de carte bancaire
echo.
echo Je vais ouvrir la page pour générer ta clé Gemini...
echo.
echo 📝 INSTRUCTIONS:
echo    1. Connecte-toi avec ton compte Google (Gmail)
echo    2. Clique sur "Create API Key"
echo    3. COPIE la clé (format: AIzaSy...)
echo    4. Reviens ici et COLLE la clé
echo.
pause

start https://aistudio.google.com/apikey

echo.
echo ⏳ Attends que la page s'ouvre...
timeout 3 >nul
echo.
echo ══════════════════════════════════════════════════════════════
set /p GEMINI_KEY="📋 COLLE ta clé Gemini ici: "
echo ══════════════════════════════════════════════════════════════
echo.

if "%GEMINI_KEY%"=="" (
    echo ❌ Pas de clé entrée, on passe...
    set GEMINI_KEY=VIDE
) else (
    echo ✅ Clé Gemini enregistrée!
)

timeout 2 >nul

cls
echo ═══════════════════════════════════════════════════════════════════
echo    📋 ÉTAPE 2/3 - GROQ - ULTRA-RAPIDE GRATUIT
echo ═══════════════════════════════════════════════════════════════════
echo.
echo ⚡ Groq = Réponses INSTANTANÉES, 100%% gratuit!
echo ✅ Llama 3.3 70B (excellent)
echo ✅ 30 requêtes/minute (très rapide)
echo.
echo Je vais ouvrir la page pour générer ta clé Groq...
echo.
echo 📝 INSTRUCTIONS:
echo    1. Crée un compte (GitHub ou email)
echo    2. Va dans "API Keys"
echo    3. Clique "Create API Key"
echo    4. COPIE la clé (format: gsk_...)
echo.
pause

start https://console.groq.com/

echo.
echo ⏳ Attends que la page s'ouvre...
timeout 3 >nul
echo.
echo ══════════════════════════════════════════════════════════════
set /p GROQ_KEY="📋 COLLE ta clé Groq ici: "
echo ══════════════════════════════════════════════════════════════
echo.

if "%GROQ_KEY%"=="" (
    echo ❌ Pas de clé entrée, on passe...
    set GROQ_KEY=VIDE
) else (
    echo ✅ Clé Groq enregistrée!
)

timeout 2 >nul

cls
echo ═══════════════════════════════════════════════════════════════════
echo    📋 ÉTAPE 3/3 - DEEPSEEK - GRATUIT ILLIMITÉ
echo ═══════════════════════════════════════════════════════════════════
echo.
echo 🚀 DeepSeek = Niveau GPT-4, GRATUIT ILLIMITÉ!
echo ✅ Pas de limite quotidienne
echo ✅ Très bon modèle
echo.
echo Je vais ouvrir la page pour générer ta clé DeepSeek...
echo.
echo 📝 INSTRUCTIONS:
echo    1. Crée un compte
echo    2. Va dans "API Keys"
echo    3. Génère une clé
echo    4. COPIE la clé (format: sk-...)
echo.
pause

start https://platform.deepseek.com/

echo.
echo ⏳ Attends que la page s'ouvre...
timeout 3 >nul
echo.
echo ══════════════════════════════════════════════════════════════
set /p DEEPSEEK_KEY="📋 COLLE ta clé DeepSeek ici: "
echo ══════════════════════════════════════════════════════════════
echo.

if "%DEEPSEEK_KEY%"=="" (
    echo ❌ Pas de clé entrée, on passe...
    set DEEPSEEK_KEY=VIDE
) else (
    echo ✅ Clé DeepSeek enregistrée!
)

timeout 2 >nul

cls
echo ═══════════════════════════════════════════════════════════════════
echo    💾 SAUVEGARDE DES CLÉS
echo ═══════════════════════════════════════════════════════════════════
echo.

REM Créer le fichier de config JSON
(
echo {
echo   "gemini": {
echo     "api_key": "%GEMINI_KEY%",
echo     "enabled": true
echo   },
echo   "groq": {
echo     "api_key": "%GROQ_KEY%",
echo     "enabled": true
echo   },
echo   "deepseek": {
echo     "api_key": "%DEEPSEEK_KEY%",
echo     "enabled": true
echo   },
echo   "openai": {
echo     "api_key": "",
echo     "enabled": false
echo   },
echo   "mistral": {
echo     "api_key": "",
echo     "enabled": false
echo   }
echo }
) > config\api_keys.json

echo ✅ Clés sauvegardées dans: config\api_keys.json
echo.

echo ═══════════════════════════════════════════════════════════════════
echo    ✨ RÉCAPITULATIF
echo ═══════════════════════════════════════════════════════════════════
echo.

if not "%GEMINI_KEY%"=="VIDE" (
    echo ✅ Gemini:   CONFIGURÉ
) else (
    echo ❌ Gemini:   PAS CONFIGURÉ
)

if not "%GROQ_KEY%"=="VIDE" (
    echo ✅ Groq:     CONFIGURÉ
) else (
    echo ❌ Groq:     PAS CONFIGURÉ
)

if not "%DEEPSEEK_KEY%"=="VIDE" (
    echo ✅ DeepSeek: CONFIGURÉ
) else (
    echo ❌ DeepSeek: PAS CONFIGURÉ
)

echo.
echo ═══════════════════════════════════════════════════════════════════
echo    🚀 PROCHAINE ÉTAPE
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Lance NiTriTe et active le mode en ligne dans l'Agent IA!
echo.
echo Tes clés sont déjà configurées, c'est prêt! 🎉
echo.
pause
