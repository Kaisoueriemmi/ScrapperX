# Twitter/X Post Scraper

Un outil Python pour scraper les réactions, retweets et commentaires d'un post X (Twitter) et exporter les données dans un fichier Excel.

## 🚀 Fonctionnalités

- ✅ Extraction des statistiques du post (retweets, likes, réponses, vues)
- ✅ Scraping des commentaires avec détails (auteur, texte, date, likes, retweets)
- ✅ Export automatique vers Excel avec mise en forme
- ✅ Interface en ligne de commande simple
- ✅ Support du mode headless (sans interface graphique)

## 📋 Prérequis

- Python 3.8 ou supérieur
- Google Chrome installé sur votre système

## 🔧 Installation

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

Les dépendances incluent:

- `selenium` - Pour l'automatisation du navigateur
- `webdriver-manager` - Gestion automatique du ChromeDriver
- `openpyxl` - Création de fichiers Excel
- `pandas` - Manipulation de données

## 💻 Utilisation

### Méthode 1: Exécution simple

```bash
python twitter_scraper.py
```

Ensuite, entrez l'URL du post Twitter/X quand demandé:

```
📎 Entrez l'URL du post Twitter/X: https://twitter.com/username/status/1234567890
```

### Méthode 2: Utilisation programmatique

```python
from twitter_scraper import TwitterScraper

# Initialiser le scraper
scraper = TwitterScraper()

# Scraper un post
post_url = "https://twitter.com/username/status/1234567890"
post_data, comments = scraper.scrape_post_data(post_url)

# Exporter vers Excel
scraper.export_to_excel(post_data, comments, "mon_export.xlsx")

# Fermer le scraper
scraper.close()
```

## 📊 Format du fichier Excel

Le fichier Excel généré contient deux feuilles:

### Feuille 1: "Statistiques Post"

- URL du post
- ID du post
- Date de scraping
- Nombre de retweets
- Nombre de likes
- Nombre de réponses
- Nombre de vues

### Feuille 2: "Commentaires"

- Numéro du commentaire
- Nom d'utilisateur
- Handle (@username)
- Texte du commentaire
- Date de publication
- Nombre de likes
- Nombre de retweets

## ⚙️ Configuration

### Mode headless

Par défaut, le scraper fonctionne en mode headless (sans interface graphique). Pour voir le navigateur en action, modifiez la ligne dans `twitter_scraper.py`:

```python
# Commentez cette ligne pour désactiver le mode headless
# chrome_options.add_argument('--headless')
```

### Nombre de commentaires

Par défaut, le scraper extrait jusqu'à 50 commentaires. Pour modifier ce nombre:

```python
comments = self.scrape_comments(max_comments=100)  # Extraire 100 commentaires
```

## ⚠️ Limitations et Notes

1. **Authentification**: Ce scraper fonctionne sur les posts publics. Pour les posts privés, une authentification serait nécessaire.

2. **Rate Limiting**: Twitter/X peut limiter le nombre de requêtes. Utilisez avec modération.

3. **Structure de la page**: Twitter/X change régulièrement la structure de ses pages. Le scraper peut nécessiter des mises à jour.

4. **Données dynamiques**: Certaines données peuvent ne pas être disponibles selon le type de post.

## 🛠️ Dépannage

### Erreur "ChromeDriver not found"

```bash
pip install --upgrade webdriver-manager
```

### Erreur "No such element"

La structure de la page Twitter a peut-être changé. Vérifiez les sélecteurs XPath dans le code.

### Timeout errors

Augmentez les délais d'attente dans le code:

```python
time.sleep(5)  # Augmentez cette valeur
```

## 📝 Exemple de sortie

```
============================================================
🐦 TWITTER/X POST SCRAPER
============================================================

📎 Entrez l'URL du post Twitter/X: https://twitter.com/example/status/123

✅ Driver Chrome initialisé avec succès

🔍 Scraping du post: https://twitter.com/example/status/123
📊 Statistiques extraites:
   - Retweets: 1.2K
   - Likes: 5.3K
   - Réponses: 234
   - Vues: 45.6K

💬 Extraction des commentaires...
✅ 50 commentaires extraits

📝 Export vers Excel: twitter_scrape_20260104_213845.xlsx
✅ Fichier Excel créé avec succès

============================================================
✅ SCRAPING TERMINÉ AVEC SUCCÈS!
📁 Fichier: twitter_scrape_20260104_213845.xlsx
📊 Statistiques: 1.2K RT, 5.3K Likes
💬 Commentaires: 50
============================================================
```

## 📄 Licence

Ce projet est fourni à des fins éducatives. Respectez les conditions d'utilisation de Twitter/X.

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## ⚖️ Avertissement

Ce scraper est fourni à des fins éducatives uniquement. L'utilisation de scrapers peut violer les conditions d'utilisation de Twitter/X. Utilisez-le de manière responsable et à vos propres risques.
