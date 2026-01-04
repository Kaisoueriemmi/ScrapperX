@echo off
REM Script de lancement rapide pour ScrapperX
REM Windows Batch File

echo ============================================================
echo    🐦 SCRAPPERX - TWITTER/X POST SCRAPER
echo ============================================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python n'est pas installé ou n'est pas dans le PATH
    echo.
    echo 📥 Téléchargez Python depuis: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python détecté
echo.

REM Vérifier si les dépendances sont installées
echo 🔍 Vérification des dépendances...
python -c "import selenium" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  Dépendances non installées
    echo 📦 Installation des dépendances...
    echo.
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Erreur lors de l'installation des dépendances
        pause
        exit /b 1
    )
    echo.
    echo ✅ Dépendances installées avec succès
)

echo ✅ Dépendances OK
echo.

REM Lancer le scraper
echo 🚀 Lancement de ScrapperX...
echo.
python twitter_scraper.py

echo.
echo ============================================================
echo    ✅ SCRAPING TERMINÉ
echo ============================================================
echo.
pause
