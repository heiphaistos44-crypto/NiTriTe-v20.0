@echo off
echo ========================================
echo RELANCEMENT PROPRE DE NITRITE V20.0
echo ========================================
echo.

echo [1/4] Arret de tous les processus Python...
taskkill /F /IM python.exe /T >nul 2>&1
taskkill /F /IM pythonw.exe /T >nul 2>&1
timeout /t 2 >nul

echo [2/4] Suppression du cache Python...
for /d /r "src" %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul
del /s /q "src\*.pyc" >nul 2>&1

echo [3/4] Nettoyage termine
echo.

echo [4/4] Lancement de NiTriTe V20.0...
echo.
start pythonw -m src.v14_mvp.main_app

timeout /t 2 >nul
echo.
echo ========================================
echo APPLICATION LANCEE AVEC SUCCES!
echo ========================================
echo.
pause
