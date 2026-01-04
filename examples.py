"""
Exemple d'utilisation du Twitter Scraper
"""

from twitter_scraper import TwitterScraper


def exemple_simple():
    """Exemple simple d'utilisation"""
    print("=== Exemple Simple ===\n")
    
    # URL du post à scraper
    post_url = "https://twitter.com/elonmusk/status/1234567890"
    
    # Initialiser le scraper
    scraper = TwitterScraper()
    
    try:
        # Scraper les données
        post_data, comments = scraper.scrape_post_data(post_url)
        
        # Exporter vers Excel
        if post_data:
            filename = scraper.export_to_excel(post_data, comments)
            print(f"\n✅ Données exportées vers: {filename}")
    
    finally:
        # Toujours fermer le scraper
        scraper.close()


def exemple_personnalise():
    """Exemple avec nom de fichier personnalisé"""
    print("\n=== Exemple avec fichier personnalisé ===\n")
    
    post_url = "https://twitter.com/example/status/123456"
    
    scraper = TwitterScraper()
    
    try:
        post_data, comments = scraper.scrape_post_data(post_url)
        
        if post_data:
            # Nom de fichier personnalisé
            custom_filename = "mon_analyse_twitter.xlsx"
            scraper.export_to_excel(post_data, comments, custom_filename)
            print(f"\n✅ Données exportées vers: {custom_filename}")
    
    finally:
        scraper.close()


def exemple_analyse_multiple():
    """Exemple pour analyser plusieurs posts"""
    print("\n=== Exemple d'analyse multiple ===\n")
    
    posts = [
        "https://twitter.com/user1/status/111",
        "https://twitter.com/user2/status/222",
        "https://twitter.com/user3/status/333"
    ]
    
    scraper = TwitterScraper()
    
    try:
        for idx, post_url in enumerate(posts, 1):
            print(f"\n--- Post {idx}/{len(posts)} ---")
            post_data, comments = scraper.scrape_post_data(post_url)
            
            if post_data:
                filename = f"post_{idx}_analysis.xlsx"
                scraper.export_to_excel(post_data, comments, filename)
                print(f"✅ Exporté: {filename}")
    
    finally:
        scraper.close()


if __name__ == "__main__":
    print("🐦 EXEMPLES D'UTILISATION DU TWITTER SCRAPER\n")
    print("Décommentez l'exemple que vous souhaitez exécuter:\n")
    
    # Décommentez l'exemple que vous voulez tester
    # exemple_simple()
    # exemple_personnalise()
    # exemple_analyse_multiple()
    
    print("\n💡 Conseil: Modifiez les URLs avec de vrais posts Twitter/X")
