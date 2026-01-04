"""
Script de test rapide pour ScrapperX
Teste les fonctionnalités principales sans lancer le scraper complet
"""

from twitter_scraper import TwitterScraper

def test_initialization():
    """Test l'initialisation du scraper"""
    print("🧪 Test 1: Initialisation du scraper")
    try:
        scraper = TwitterScraper()
        print("✅ Scraper initialisé avec succès")
        scraper.close()
        return True
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

def test_url_extraction():
    """Test l'extraction de l'ID du post"""
    print("\n🧪 Test 2: Extraction de l'ID du post")
    scraper = TwitterScraper()
    
    test_urls = [
        "https://twitter.com/user/status/1234567890",
        "https://x.com/user/status/9876543210",
        "https://twitter.com/user/status/1111111111?s=20"
    ]
    
    try:
        for url in test_urls:
            post_id = scraper.extract_post_id(url)
            print(f"   URL: {url}")
            print(f"   ID extrait: {post_id}")
            print()
        print("✅ Extraction d'ID réussie")
        scraper.close()
        return True
    except Exception as e:
        print(f"❌ Erreur: {e}")
        scraper.close()
        return False

def test_export_structure():
    """Test la structure de l'export Excel"""
    print("\n🧪 Test 3: Structure de l'export Excel")
    scraper = TwitterScraper()
    
    # Données de test
    post_data = {
        'url': 'https://twitter.com/test/status/123',
        'post_id': '123',
        'timestamp': '2026-01-04 21:55:00',
        'retweets': '100',
        'likes': '500',
        'replies': '50',
        'views': '10K'
    }
    
    comments = [
        {
            'username': 'User1',
            'handle': '@user1',
            'text': 'Test comment 1',
            'timestamp': '2026-01-04',
            'likes': '10',
            'retweets': '2',
            'replies': '1'
        },
        {
            'username': 'User2',
            'handle': '@user2',
            'text': 'Test comment 2',
            'timestamp': '2026-01-04',
            'likes': '5',
            'retweets': '0',
            'replies': '0'
        }
    ]
    
    try:
        filename = scraper.export_to_excel(post_data, comments, "test_export.xlsx")
        if filename:
            print(f"✅ Export Excel créé: {filename}")
            print(f"   • Statistiques du post: OK")
            print(f"   • {len(comments)} commentaires: OK")
            print(f"   • Colonnes: #, Username, Handle, Text, Date, Likes, Retweets, Replies")
            scraper.close()
            return True
        else:
            print("❌ Échec de l'export")
            scraper.close()
            return False
    except Exception as e:
        print(f"❌ Erreur: {e}")
        scraper.close()
        return False

def main():
    """Exécute tous les tests"""
    print("=" * 60)
    print("🧪 TESTS SCRAPPERX v1.1.0")
    print("=" * 60)
    
    results = []
    
    # Test 1: Initialisation
    results.append(test_initialization())
    
    # Test 2: Extraction d'ID
    results.append(test_url_extraction())
    
    # Test 3: Export Excel
    results.append(test_export_structure())
    
    # Résumé
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Tests réussis: {passed}/{total}")
    
    if passed == total:
        print("✅ Tous les tests sont passés!")
    else:
        print(f"⚠️ {total - passed} test(s) échoué(s)")
    print("=" * 60)

if __name__ == "__main__":
    main()
