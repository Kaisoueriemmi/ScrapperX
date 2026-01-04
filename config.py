# Configuration du Scraper Twitter/X

# Paramètres de scraping
MAX_COMMENTS = 50  # Nombre maximum de commentaires à extraire
SCROLL_ATTEMPTS = 5  # Nombre de scrolls pour charger plus de commentaires
SCROLL_DELAY = 2  # Délai entre chaque scroll (secondes)
PAGE_LOAD_DELAY = 5  # Délai d'attente pour le chargement de la page (secondes)

# Paramètres du navigateur
HEADLESS_MODE = True  # True = mode sans interface, False = voir le navigateur
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Paramètres d'export Excel
EXCEL_HEADER_COLOR = "1DA1F2"  # Couleur Twitter/X pour les en-têtes
EXCEL_HEADER_TEXT_COLOR = "FFFFFF"  # Blanc pour le texte des en-têtes

# Colonnes Excel - Statistiques
STATS_COLUMNS = ['Métrique', 'Valeur']

# Colonnes Excel - Commentaires
COMMENTS_COLUMNS = ['#', 'Nom d\'utilisateur', 'Handle', 'Texte', 'Date', 'Likes', 'Retweets']

# Largeurs des colonnes Excel
COLUMN_WIDTHS = {
    'stats': {
        'A': 20,  # Métrique
        'B': 50   # Valeur
    },
    'comments': {
        'A': 5,   # #
        'B': 20,  # Nom d'utilisateur
        'C': 20,  # Handle
        'D': 60,  # Texte
        'E': 20,  # Date
        'F': 10,  # Likes
        'G': 10   # Retweets
    }
}

# Messages
MESSAGES = {
    'fr': {
        'driver_init_success': '✅ Driver Chrome initialisé avec succès',
        'driver_init_error': '❌ Erreur lors de l\'initialisation du driver',
        'scraping_post': '🔍 Scraping du post',
        'stats_extracted': '📊 Statistiques extraites',
        'extracting_comments': '💬 Extraction des commentaires',
        'comments_extracted': '✅ {count} commentaires extraits',
        'export_excel': '📝 Export vers Excel',
        'export_success': '✅ Fichier Excel créé avec succès',
        'export_error': '❌ Erreur lors de l\'export Excel',
        'driver_closed': '🔒 Driver fermé',
        'scraping_complete': '✅ SCRAPING TERMINÉ AVEC SUCCÈS!',
        'scraping_failed': '❌ Échec du scraping'
    }
}
