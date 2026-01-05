#!/bin/bash

# Script de test de compatibilité macOS pour ScrapperX
# Version 1.2.1

echo "============================================================"
echo "   🍎 SCRAPPERX - TEST DE COMPATIBILITÉ MACOS"
echo "============================================================"
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compteurs
TESTS_PASSED=0
TESTS_FAILED=0

# Fonction de test
test_check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $1${NC}"
        ((TESTS_PASSED++))
        return 0
    else
        echo -e "${RED}❌ $1${NC}"
        ((TESTS_FAILED++))
        return 1
    fi
}

echo "🔍 Test 1: Vérification de la plateforme"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${GREEN}✅ macOS détecté${NC}"
    ((TESTS_PASSED++))
    sw_vers
else
    echo -e "${RED}❌ Ce script est conçu pour macOS${NC}"
    ((TESTS_FAILED++))
    exit 1
fi

echo ""
echo "🔍 Test 2: Vérification de Python"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ Python installé: $PYTHON_VERSION${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${RED}❌ Python 3 n'est pas installé${NC}"
    echo -e "${YELLOW}💡 Installez avec: brew install python@3.11${NC}"
    ((TESTS_FAILED++))
fi

echo ""
echo "🔍 Test 3: Vérification de l'encodage UTF-8"
ENCODING=$(python3 -c "import sys; print(sys.stdout.encoding)" 2>/dev/null)
if [ "$ENCODING" = "utf-8" ] || [ "$ENCODING" = "UTF-8" ]; then
    echo -e "${GREEN}✅ Encodage UTF-8 détecté${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${YELLOW}⚠️  Encodage: $ENCODING (UTF-8 recommandé)${NC}"
fi

echo ""
echo "🔍 Test 4: Test d'affichage des caractères"
python3 -c "print('Test: ✅ é è à ù 🐦 ✨')" 2>/dev/null
test_check "Affichage des caractères spéciaux"

echo ""
echo "🔍 Test 5: Vérification de Google Chrome"
if [ -d "/Applications/Google Chrome.app" ]; then
    CHROME_VERSION=$(/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version 2>/dev/null)
    echo -e "${GREEN}✅ Chrome installé: $CHROME_VERSION${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${RED}❌ Google Chrome n'est pas installé${NC}"
    echo -e "${YELLOW}💡 Installez avec: brew install --cask google-chrome${NC}"
    ((TESTS_FAILED++))
fi

echo ""
echo "🔍 Test 6: Vérification des dépendances Python"

# Selenium
python3 -c "import selenium" 2>/dev/null
test_check "selenium"

# openpyxl
python3 -c "import openpyxl" 2>/dev/null
test_check "openpyxl"

# pandas
python3 -c "import pandas" 2>/dev/null
test_check "pandas"

# webdriver-manager
python3 -c "import webdriver_manager" 2>/dev/null
test_check "webdriver-manager"

echo ""
echo "🔍 Test 7: Vérification des fichiers du projet"

FILES=("twitter_scraper.py" "requirements.txt" "run_macos.sh" "README.md")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✅ $file${NC}"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}❌ $file manquant${NC}"
        ((TESTS_FAILED++))
    fi
done

echo ""
echo "🔍 Test 8: Vérification des permissions"
if [ -x "run_macos.sh" ]; then
    echo -e "${GREEN}✅ run_macos.sh est exécutable${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${YELLOW}⚠️  run_macos.sh n'est pas exécutable${NC}"
    echo -e "${YELLOW}💡 Exécutez: chmod +x run_macos.sh${NC}"
fi

echo ""
echo "🔍 Test 9: Test d'import du scraper"
python3 -c "from twitter_scraper import TwitterScraper; print('Import réussi')" 2>/dev/null
test_check "Import de TwitterScraper"

echo ""
echo "🔍 Test 10: Vérification de l'architecture"
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    echo -e "${GREEN}✅ Apple Silicon (M1/M2/M3) détecté${NC}"
    echo -e "${GREEN}   Performance native optimale${NC}"
    ((TESTS_PASSED++))
elif [ "$ARCH" = "x86_64" ]; then
    echo -e "${GREEN}✅ Intel x86_64 détecté${NC}"
    echo -e "${GREEN}   Pleinement compatible${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${YELLOW}⚠️  Architecture: $ARCH${NC}"
fi

echo ""
echo "============================================================"
echo "   📊 RÉSULTATS DES TESTS"
echo "============================================================"
echo ""
echo -e "${GREEN}✅ Tests réussis: $TESTS_PASSED${NC}"
echo -e "${RED}❌ Tests échoués: $TESTS_FAILED${NC}"
echo ""

TOTAL_TESTS=$((TESTS_PASSED + TESTS_FAILED))
PERCENTAGE=$((TESTS_PASSED * 100 / TOTAL_TESTS))

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 TOUS LES TESTS SONT PASSÉS ! (100%)${NC}"
    echo -e "${GREEN}✅ ScrapperX est prêt à être utilisé sur macOS${NC}"
    echo ""
    echo "🚀 Lancez le scraper avec:"
    echo "   python3 twitter_scraper.py"
    echo "   ou"
    echo "   ./run_macos.sh"
    EXIT_CODE=0
elif [ $PERCENTAGE -ge 80 ]; then
    echo -e "${YELLOW}⚠️  TESTS PARTIELLEMENT RÉUSSIS ($PERCENTAGE%)${NC}"
    echo -e "${YELLOW}Certaines fonctionnalités peuvent ne pas fonctionner${NC}"
    echo ""
    echo "💡 Installez les dépendances manquantes:"
    echo "   pip3 install -r requirements.txt"
    EXIT_CODE=1
else
    echo -e "${RED}❌ TESTS ÉCHOUÉS ($PERCENTAGE%)${NC}"
    echo -e "${RED}Veuillez installer les dépendances manquantes${NC}"
    echo ""
    echo "📖 Consultez QUICKSTART_MACOS.md pour l'installation"
    EXIT_CODE=2
fi

echo ""
echo "============================================================"
echo "   📝 INFORMATIONS SYSTÈME"
echo "============================================================"
echo ""
echo "macOS Version: $(sw_vers -productVersion)"
echo "Architecture: $ARCH"
echo "Python: $(python3 --version 2>/dev/null || echo 'Non installé')"
echo "Encodage: $ENCODING"
echo ""

exit $EXIT_CODE
