#!/bin/bash

# ScrapperX Launcher pour macOS
# Version 1.2.0

echo "============================================================"
echo "   🐦 SCRAPPERX - TWITTER/X POST SCRAPER"
echo "============================================================"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "📦 Installez Python avec: brew install python@3.11"
    exit 1
fi

echo "✅ Python détecté: $(python3 --version)"

# Vérifier les dépendances
echo ""
echo "🔍 Vérification des dépendances..."

if ! python3 -c "import selenium" &> /dev/null; then
    echo "⚠️  Dépendances manquantes"
    echo "📦 Installation des dépendances..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✅ Dépendances installées"
    else
        echo "❌ Erreur lors de l'installation"
        exit 1
    fi
else
    echo "✅ Dépendances OK"
fi

# Lancer le scraper
echo ""
echo "🚀 Lancement de ScrapperX..."
echo ""

python3 twitter_scraper.py

# Fin
echo ""
echo "============================================================"
echo "   ✅ SCRAPING TERMINÉ"
echo "============================================================"
echo ""
echo "Appuyez sur Entrée pour quitter..."
read
