@echo off
chcp 65001 >nul
cls
echo ========================================
echo    REBUILD COMPLET - SANS CACHE
echo ========================================
echo.

echo [1/4] Nettoyage cache Python...
powershell -Command "Get-ChildItem -Path . -Include __pycache__ -Recurse -Force | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue"
del /s /q *.pyc >nul 2>&1
echo ✓ Cache Python supprimé

echo.
echo [2/4] Nettoyage build/dist...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo ✓ Build/dist supprimés

echo.
echo [3/4] Test import modules Python...
py -3.12 -c "import sys; sys.path.insert(0, 'src'); from v14_mvp.ai_response_generator import DynamicResponseGenerator; print('✓ ai_response_generator OK')"
if %ERRORLEVEL% NEQ 0 (
    echo ✗ ERREUR: Problème import ai_response_generator
    pause
    exit /b 1
)

echo.
echo [4/4] Build PyInstaller...
py -3.12 build_tools\build_portable_fixed.py

echo.
if exist "dist\NiTriTe_V18_Portable.exe" (
    echo ========================================
    echo    BUILD RÉUSSI! ✓
    echo ========================================
    echo.
    echo Exécutable: dist\NiTriTe_V18_Portable.exe
    echo.
    echo Test maintenant avec "mon pc surchauffe"
    echo Les réponses doivent être 100%% FRANÇAISES!
) else (
    echo ========================================
    echo    ERREUR BUILD ✗
    echo ========================================
)

echo.
pause
