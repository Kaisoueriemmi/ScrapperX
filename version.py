"""
Version information for ScrapperX
"""

__version__ = "1.2.2"
__author__ = "Kais OUERIEMMI"
__email__ = "contact@kaisoueriemmi.com"
__status__ = "Production"
__date__ = "2026-01-05"

# Version history
VERSION_HISTORY = {
    "1.2.1": {
        "date": "2026-01-05",
        "type": "correctif",
        "fixes": [
            "Configuration automatique UTF-8 pour Windows",
            "Support complet des caractères accentués",
            "Support des emojis et symboles",
            "Affichage correct dans CMD/PowerShell/Windows Terminal"
        ],
        "files": [
            "twitter_scraper.py - Configuration UTF-8 ajoutée",
            "run.bat - chcp 65001 ajouté",
            "UTF8_FIX.md - Documentation du correctif"
        ]
    },
    "1.2.0": {
        "date": "2026-01-04",
        "features": [
            "Sécurité et anti-détection (User-Agent rotation, masquage WebDriver)",
            "Délais aléatoires pour comportement humain",
            "Logging complet avec fichier scraper.log",
            "Retry automatique avec gestion d'erreurs robuste",
            "Détection automatique de rate limit",
            "Mode headless configurable",
            "Statistiques de session détaillées"
        ],
        "improvements": [
            "Refactorisation complète de la classe TwitterScraper",
            "Fonction safe_find_element() avec retry",
            "Délais aléatoires entre toutes les actions",
            "Meilleure gestion des exceptions",
            "Affichage des statistiques finales"
        ]
    },
    "1.1.0": {
        "date": "2026-01-04",
        "features": [
            "Extraction de TOUS les commentaires disponibles",
            "Défilement automatique continu",
            "Déduplication des commentaires",
            "Progression en temps réel",
            "Nouvelle colonne 'Réponses' dans l'export Excel",
            "Interface en 3 étapes",
            "Mode interactif amélioré"
        ],
        "improvements": [
            "Séparation de scrape_post_data() et scrape_comments()",
            "Algorithme de scroll amélioré",
            "Meilleure gestion des erreurs",
            "Messages plus clairs et informatifs"
        ]
    },
    "1.0.0": {
        "date": "2026-01-04",
        "features": [
            "Scraper Twitter/X complet",
            "Export Excel professionnel",
            "Interface CLI simple",
            "Mode headless",
            "Support des URLs twitter.com et x.com"
        ]
    }
}

def get_version():
    """Retourne la version actuelle"""
    return __version__

def get_version_info():
    """Retourne les informations complètes de version"""
    return {
        "version": __version__,
        "author": __author__,
        "status": __status__,
        "date": __date__
    }

def print_version_info():
    """Affiche les informations de version"""
    print(f"ScrapperX v{__version__}")
    print(f"Auteur: {__author__}")
    print(f"Date: {__date__}")
    print(f"Statut: {__status__}")

if __name__ == "__main__":
    print_version_info()
