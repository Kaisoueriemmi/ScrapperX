# 🐦 ScrapperX - Twitter/X Post Scraper

![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Un outil Python puissant pour scraper les réactions, retweets et commentaires d'un post X (Twitter) et exporter les données dans un fichier Excel professionnel.

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

### Windows

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

3. **Lancer le scraper**

```bash
python twitter_scraper.py
# ou
run.bat
```

### macOS / Linux

1. **Cloner ou télécharger le projet**

2. **Installer les dépendances**

```bash
pip3 install -r requirements.txt
```

3. **Lancer le scraper**

```bash
python3 twitter_scraper.py
# ou
chmod +x run_macos.sh && ./run_macos.sh
```

📖 **Guide complet macOS** : Consultez [`QUICKSTART_MACOS.md`](QUICKSTART_MACOS.md) pour un guide détaillé spécifique à macOS.

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

# Étape 1: Extraire les données du post
post_data = scraper.scrape_post_data(post_url)

# Étape 2: Extraire les commentaires (tous par défaut)
comments = scraper.scrape_comments()

# Ou avec une limite
# comments = scraper.scrape_comments(max_comments=50)

# Étape 3: Exporter vers Excel
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
- **Nombre de commentaires extraits** (nouveau)

### Feuille 2: "Commentaires"

- Numéro du commentaire
- Nom d'utilisateur
- Handle (@username)
- Texte du commentaire
- Date de publication
- Nombre de likes
- Nombre de retweets
- **Nombre de réponses** (nouveau)

## ⚙️ Configuration

### Mode headless

Par défaut, le scraper fonctionne en mode headless (sans interface graphique). Pour voir le navigateur en action, modifiez la ligne dans `twitter_scraper.py`:

```python
# Commentez cette ligne pour désactiver le mode headless
# chrome_options.add_argument('--headless')
```

### Nombre de commentaires

**🆕 Nouvelle fonctionnalité**: Le scraper peut maintenant extraire **TOUS** les commentaires disponibles!

Lors de l'exécution, vous aurez le choix:

1. **Tous les commentaires** (recommandé) - Le scraper défilera automatiquement jusqu'à charger tous les commentaires disponibles
2. **Nombre limité** - Spécifiez un nombre maximum de commentaires à extraire

Pour l'utilisation programmatique:

```python
# Extraire TOUS les commentaires (par défaut)
comments = scraper.scrape_comments()

# Ou limiter à un nombre spécifique
comments = scraper.scrape_comments(max_comments=100)
```

Le scraper affiche la progression en temps réel:

- Nombre de scrolls effectués
- Nombre de tweets chargés
- Nombre de commentaires extraits

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

💬 Nombre de commentaires à extraire:
   1. Tous les commentaires (recommandé)
   2. Nombre limité

Votre choix (1 ou 2): 1
✅ Extraction de TOUS les commentaires disponibles

✅ Driver Chrome initialisé avec succès

============================================================
📊 ÉTAPE 1: Extraction des données du post
============================================================

🔍 Accès au post: https://twitter.com/example/status/123
✅ Statistiques du post extraites:
   • Retweets: 1.2K
   • Likes: 5.3K
   • Réponses: 234
   • Vues: 45.6K

============================================================
📊 ÉTAPE 2: Extraction des commentaires
============================================================

💬 Extraction des commentaires...
⏳ Défilement pour charger tous les commentaires disponibles...
   📊 Scroll #1 - 25 tweets chargés
   📊 Scroll #2 - 52 tweets chargés
   📊 Scroll #3 - 89 tweets chargés
   📊 Scroll #4 - 134 tweets chargés
   📊 Scroll #5 - 187 tweets chargés
   📊 Scroll #6 - 234 tweets chargés
   📊 Tentative 1/3 - 234 tweets chargés
   📊 Tentative 2/3 - 234 tweets chargés
   📊 Tentative 3/3 - 234 tweets chargés

✅ Défilement terminé après 6 scrolls
📝 Extraction des données des commentaires...
   Total de tweets trouvés: 234
   ⏳ 10 commentaires extraits...
   ⏳ 20 commentaires extraits...
   ⏳ 30 commentaires extraits...
   ...
   ⏳ 230 commentaires extraits...

✅ 233 commentaires uniques extraits avec succès!

============================================================
📊 ÉTAPE 3: Export vers Excel
============================================================

📝 Export vers Excel: twitter_scrape_20260104_215236.xlsx
✅ Fichier Excel créé avec succès

============================================================
✅ SCRAPING TERMINÉ AVEC SUCCÈS!
============================================================
📁 Fichier: twitter_scrape_20260104_215236.xlsx
📊 Statistiques du post:
   • Retweets: 1.2K
   • Likes: 5.3K
   • Vues: 45.6K
💬 Commentaires extraits: 233
============================================================

🔒 Fermeture du navigateur...
```

## 📄 Licence

Ce projet est fourni à des fins éducatives. Respectez les conditions d'utilisation de Twitter/X.

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## ⚖️ Avertissement

Ce scraper est fourni à des fins éducatives uniquement. L'utilisation de scrapers peut violer les conditions d'utilisation de Twitter/X. Utilisez-le de manière responsable et à vos propres risques.
