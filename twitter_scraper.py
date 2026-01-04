"""
Twitter/X Post Scraper
Scrape les réactions, retweets et commentaires d'un post X/Twitter
et exporte les données dans un fichier Excel
"""

import os
import re
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment


class TwitterScraper:
    def __init__(self):
        """Initialise le scraper avec Selenium"""
        self.driver = None
        self.setup_driver()
    
    def setup_driver(self):
        """Configure le driver Chrome avec les options nécessaires"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Mode sans interface graphique
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            print("✅ Driver Chrome initialisé avec succès")
        except Exception as e:
            print(f"❌ Erreur lors de l'initialisation du driver: {e}")
            raise
    
    def extract_post_id(self, url):
        """Extrait l'ID du post depuis l'URL"""
        pattern = r'/status/(\d+)'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        return None
    
    def scrape_post_data(self, post_url):
        """Scrape les données du post (réactions, retweets, commentaires)"""
        print(f"\n🔍 Scraping du post: {post_url}")
        
        try:
            self.driver.get(post_url)
            time.sleep(5)  # Attendre le chargement de la page
            
            # Données du post principal
            post_data = {
                'url': post_url,
                'post_id': self.extract_post_id(post_url),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Extraire les statistiques du post
            try:
                # Retweets
                retweet_elements = self.driver.find_elements(By.XPATH, "//button[@data-testid='retweet']//span")
                post_data['retweets'] = retweet_elements[0].text if retweet_elements else '0'
                
                # Likes
                like_elements = self.driver.find_elements(By.XPATH, "//button[@data-testid='like']//span")
                post_data['likes'] = like_elements[0].text if like_elements else '0'
                
                # Réponses (commentaires)
                reply_elements = self.driver.find_elements(By.XPATH, "//button[@data-testid='reply']//span")
                post_data['replies'] = reply_elements[0].text if reply_elements else '0'
                
                # Vues
                view_elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/analytics')]//span")
                post_data['views'] = view_elements[0].text if view_elements else '0'
                
                print(f"📊 Statistiques extraites:")
                print(f"   - Retweets: {post_data['retweets']}")
                print(f"   - Likes: {post_data['likes']}")
                print(f"   - Réponses: {post_data['replies']}")
                print(f"   - Vues: {post_data['views']}")
                
            except Exception as e:
                print(f"⚠️ Erreur lors de l'extraction des statistiques: {e}")
            
            # Scraper les commentaires
            comments = self.scrape_comments()
            
            return post_data, comments
            
        except Exception as e:
            print(f"❌ Erreur lors du scraping: {e}")
            return None, []
    
    def scrape_comments(self, max_comments=50):
        """Scrape les commentaires du post"""
        print(f"\n💬 Extraction des commentaires...")
        comments = []
        
        try:
            # Scroll pour charger plus de commentaires
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_attempts = 0
            max_scrolls = 5
            
            while scroll_attempts < max_scrolls:
                # Scroll vers le bas
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                # Calculer la nouvelle hauteur
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                    
                last_height = new_height
                scroll_attempts += 1
            
            # Extraire les commentaires
            tweet_elements = self.driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
            
            for idx, tweet in enumerate(tweet_elements[1:max_comments+1]):  # Skip le premier (post original)
                try:
                    comment_data = {}
                    
                    # Nom d'utilisateur
                    try:
                        username_elem = tweet.find_element(By.XPATH, ".//div[@data-testid='User-Name']")
                        comment_data['username'] = username_elem.text.split('\n')[0]
                    except:
                        comment_data['username'] = 'N/A'
                    
                    # Handle (@username)
                    try:
                        handle_elem = tweet.find_element(By.XPATH, ".//div[@data-testid='User-Name']//span[contains(text(), '@')]")
                        comment_data['handle'] = handle_elem.text
                    except:
                        comment_data['handle'] = 'N/A'
                    
                    # Texte du commentaire
                    try:
                        text_elem = tweet.find_element(By.XPATH, ".//div[@data-testid='tweetText']")
                        comment_data['text'] = text_elem.text
                    except:
                        comment_data['text'] = 'N/A'
                    
                    # Timestamp
                    try:
                        time_elem = tweet.find_element(By.XPATH, ".//time")
                        comment_data['timestamp'] = time_elem.get_attribute('datetime')
                    except:
                        comment_data['timestamp'] = 'N/A'
                    
                    # Likes du commentaire
                    try:
                        like_elem = tweet.find_element(By.XPATH, ".//button[@data-testid='like']//span")
                        comment_data['likes'] = like_elem.text if like_elem.text else '0'
                    except:
                        comment_data['likes'] = '0'
                    
                    # Retweets du commentaire
                    try:
                        retweet_elem = tweet.find_element(By.XPATH, ".//button[@data-testid='retweet']//span")
                        comment_data['retweets'] = retweet_elem.text if retweet_elem.text else '0'
                    except:
                        comment_data['retweets'] = '0'
                    
                    comments.append(comment_data)
                    
                except Exception as e:
                    print(f"⚠️ Erreur lors de l'extraction du commentaire {idx}: {e}")
                    continue
            
            print(f"✅ {len(comments)} commentaires extraits")
            return comments
            
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction des commentaires: {e}")
            return comments
    
    def export_to_excel(self, post_data, comments, filename=None):
        """Exporte les données vers un fichier Excel"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"twitter_scrape_{timestamp}.xlsx"
        
        print(f"\n📝 Export vers Excel: {filename}")
        
        try:
            # Créer un workbook
            wb = Workbook()
            
            # Feuille 1: Statistiques du post
            ws_stats = wb.active
            ws_stats.title = "Statistiques Post"
            
            # En-têtes avec style
            headers_stats = ['Métrique', 'Valeur']
            ws_stats.append(headers_stats)
            
            # Style des en-têtes
            for cell in ws_stats[1]:
                cell.font = Font(bold=True, color="FFFFFF")
                cell.fill = PatternFill(start_color="1DA1F2", end_color="1DA1F2", fill_type="solid")
                cell.alignment = Alignment(horizontal="center")
            
            # Données du post
            ws_stats.append(['URL', post_data.get('url', 'N/A')])
            ws_stats.append(['Post ID', post_data.get('post_id', 'N/A')])
            ws_stats.append(['Date de scraping', post_data.get('timestamp', 'N/A')])
            ws_stats.append(['Retweets', post_data.get('retweets', '0')])
            ws_stats.append(['Likes', post_data.get('likes', '0')])
            ws_stats.append(['Réponses', post_data.get('replies', '0')])
            ws_stats.append(['Vues', post_data.get('views', '0')])
            
            # Ajuster la largeur des colonnes
            ws_stats.column_dimensions['A'].width = 20
            ws_stats.column_dimensions['B'].width = 50
            
            # Feuille 2: Commentaires
            if comments:
                ws_comments = wb.create_sheet(title="Commentaires")
                
                # En-têtes
                headers_comments = ['#', 'Nom d\'utilisateur', 'Handle', 'Texte', 'Date', 'Likes', 'Retweets']
                ws_comments.append(headers_comments)
                
                # Style des en-têtes
                for cell in ws_comments[1]:
                    cell.font = Font(bold=True, color="FFFFFF")
                    cell.fill = PatternFill(start_color="1DA1F2", end_color="1DA1F2", fill_type="solid")
                    cell.alignment = Alignment(horizontal="center")
                
                # Données des commentaires
                for idx, comment in enumerate(comments, 1):
                    ws_comments.append([
                        idx,
                        comment.get('username', 'N/A'),
                        comment.get('handle', 'N/A'),
                        comment.get('text', 'N/A'),
                        comment.get('timestamp', 'N/A'),
                        comment.get('likes', '0'),
                        comment.get('retweets', '0')
                    ])
                
                # Ajuster la largeur des colonnes
                ws_comments.column_dimensions['A'].width = 5
                ws_comments.column_dimensions['B'].width = 20
                ws_comments.column_dimensions['C'].width = 20
                ws_comments.column_dimensions['D'].width = 60
                ws_comments.column_dimensions['E'].width = 20
                ws_comments.column_dimensions['F'].width = 10
                ws_comments.column_dimensions['G'].width = 10
            
            # Sauvegarder le fichier
            wb.save(filename)
            print(f"✅ Fichier Excel créé avec succès: {filename}")
            
            return filename
            
        except Exception as e:
            print(f"❌ Erreur lors de l'export Excel: {e}")
            return None
    
    def close(self):
        """Ferme le driver"""
        if self.driver:
            self.driver.quit()
            print("\n🔒 Driver fermé")


def main():
    """Fonction principale"""
    print("=" * 60)
    print("🐦 TWITTER/X POST SCRAPER")
    print("=" * 60)
    
    # Demander l'URL du post
    post_url = input("\n📎 Entrez l'URL du post Twitter/X: ").strip()
    
    if not post_url:
        print("❌ URL invalide!")
        return
    
    # Initialiser le scraper
    scraper = TwitterScraper()
    
    try:
        # Scraper les données
        post_data, comments = scraper.scrape_post_data(post_url)
        
        if post_data:
            # Exporter vers Excel
            filename = scraper.export_to_excel(post_data, comments)
            
            if filename:
                print(f"\n{'=' * 60}")
                print(f"✅ SCRAPING TERMINÉ AVEC SUCCÈS!")
                print(f"📁 Fichier: {filename}")
                print(f"📊 Statistiques: {post_data.get('retweets', '0')} RT, {post_data.get('likes', '0')} Likes")
                print(f"💬 Commentaires: {len(comments)}")
                print(f"{'=' * 60}")
        else:
            print("\n❌ Échec du scraping")
    
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
    
    finally:
        # Fermer le driver
        scraper.close()


if __name__ == "__main__":
    main()
