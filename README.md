# 🐦 ScrapperX - Twitter/X Post Scraper

![Version](https://img.shields.io/badge/version-1.2.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

Un scraper Twitter/X professionnel pour extraire **tous les commentaires** d'un post avec leurs statistiques complètes.

---

## ✨ Fonctionnalités

### 🎯 Extraction Complète

- ✅ **Extraction illimitée** de tous les commentaires disponibles
- ✅ **Statistiques du post** : Retweets, Likes, Réponses, Vues
- ✅ **Données par commentaire** : Username, Handle, Texte, Date, Likes, Retweets, Réponses
- ✅ **Déduplication automatique** des commentaires
- ✅ **Progression en temps réel**

### 🛡️ Sécurité & Anti-Détection

- ✅ **Rotation de User-Agent** (4 User-Agents différents)
- ✅ **Masquage WebDriver** (navigator.webdriver = undefined)
- ✅ **Délais aléatoires** pour simuler un comportement humain
- ✅ **Détection automatique de rate limit**

### 🔧 Robustesse

- ✅ **Retry automatique** (3 tentatives par défaut)
- ✅ **Logging complet** (fichier scraper.log)
- ✅ **Gestion avancée des erreurs**
- ✅ **Statistiques de session**

### 📊 Export

- ✅ **Export Excel professionnel** avec 2 feuilles
- ✅ **Formatage automatique** (couleurs, largeurs de colonnes)
- ✅ **Horodatage** de chaque export

---

## 📋 Prérequis

- **Python 3.8+**
- **Google Chrome** installé

---

## 🚀 Installation

### Windows

```bash
# 1. Cloner ou télécharger le projet
git clone https://github.com/Kaisoueriemmi/ScrapperX.git
cd ScrapperX

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer le scraper
python twitter_scraper.py
# ou
run.bat
```

### macOS / Linux

```bash
# 1. Cloner ou télécharger le projet
git clone https://github.com/Kaisoueriemmi/ScrapperX.git
cd ScrapperX

# 2. Installer les dépendances
pip3 install -r requirements.txt

# 3. Lancer le scraper
python3 twitter_scraper.py
# ou
chmod +x run_macos.sh && ./run_macos.sh
```

---

## 💻 Utilisation

### Mode Interactif (Recommandé)

```bash
python twitter_scraper.py
```

Le scraper vous guidera à travers 3 étapes :

#### Étape 1 : URL du Post

```
📎 Entrez l'URL du post Twitter/X: https://x.com/username/status/123456
```

#### Étape 2 : Nombre de Commentaires

```
💬 Nombre de commentaires à extraire:
   1. Tous les commentaires (recommandé)
   2. Nombre limité

Votre choix (1 ou 2): 1
```

#### Étape 3 : Mode d'Affichage

```
👁️ Mode d'affichage:
   1. Mode visible (recommandé pour debug)
   2. Mode headless (invisible)

Votre choix (1 ou 2): 1
```

### Mode Programmatique

```python
from twitter_scraper import TwitterScraper

# Initialiser le scraper
scraper = TwitterScraper(headless=False, max_retries=3)

# Étape 1: Extraire les données du post
post_url = "https://x.com/username/status/123456"
post_data = scraper.scrape_post_data(post_url)

# Étape 2: Extraire les commentaires
comments = scraper.scrape_comments()  # Tous les commentaires
# ou
comments = scraper.scrape_comments(max_comments=100)  # Limité à 100

# Étape 3: Exporter vers Excel
scraper.export_to_excel(post_data, comments)

# Fermer le driver
scraper.close()
```

---

## 📊 Format de Sortie Excel

Le fichier Excel généré contient 2 feuilles :

### Feuille 1 : "Statistiques Post"

| Métrique              | Valeur              |
| --------------------- | ------------------- |
| URL                   | https://x.com/...   |
| Post ID               | 123456789           |
| Date de scraping      | 2026-01-05 10:30:00 |
| Retweets              | 3 k                 |
| Likes                 | 17 k                |
| Réponses              | 733                 |
| Vues                  | 45 k                |
| Commentaires extraits | 733                 |
| Scrolls effectués     | 15                  |

### Feuille 2 : "Commentaires"

| #   | Nom d'utilisateur | Handle     | Texte                 | Date          | Likes | Retweets | Réponses |
| --- | ----------------- | ---------- | --------------------- | ------------- | ----- | -------- | -------- |
| 1   | John Doe          | @johndoe   | Super post !          | 2026-01-04... | 5     | 0        | 2        |
| 2   | Jane Smith        | @janesmith | Merci pour le partage | 2026-01-04... | 12    | 1        | 0        |

---

## 🔧 Configuration

### Paramètres du Scraper

```python
TwitterScraper(
    headless=False,      # Mode sans interface graphique
    max_retries=3        # Nombre de tentatives en cas d'erreur
)
```

### Extraction de Commentaires

```python
scraper.scrape_comments(
    max_comments=None    # None = tous, ou un nombre spécifique
)
```

---

## 📝 Logs

Tous les événements sont enregistrés dans `scraper.log` :

```
2026-01-05 10:30:00 - INFO - Initialisation du scraper...
2026-01-05 10:30:02 - INFO - User-Agent sélectionné: Mozilla/5.0...
2026-01-05 10:30:03 - INFO - Driver initialisé en mode visible
2026-01-05 10:30:05 - INFO - Début du scraping du post: https://x.com/...
2026-01-05 10:30:10 - INFO - Statistiques extraites: RT=3k, Likes=17k
2026-01-05 10:30:15 - INFO - Début de l'extraction des commentaires
2026-01-05 10:35:20 - INFO - Extraction terminée: 733 commentaires
2026-01-05 10:35:25 - INFO - Export réussi: twitter_scrape_20260105_103525.xlsx
```

---

## 🐛 Dépannage

### Windows

#### Problème : Caractères mal affichés (é → ├®)

**Solution :** Le scraper configure automatiquement UTF-8. Si le problème persiste :

```bash
chcp 65001
python twitter_scraper.py
```

#### Problème : ChromeDriver non trouvé

**Solution :** Le scraper télécharge automatiquement ChromeDriver. Vérifiez votre connexion internet.

### macOS

#### Problème : "python: command not found"

**Solution :** Utilisez `python3`

```bash
python3 twitter_scraper.py
```

#### Problème : ChromeDriver bloqué par Gatekeeper

**Solution :**

```bash
# Méthode 1 : Via Préférences Système
# Préférences Système → Sécurité → Autoriser quand même

# Méthode 2 : Via Terminal
xattr -d com.apple.quarantine /path/to/chromedriver
```

#### Problème : Chrome ne s'ouvre pas

**Solution :**

```bash
# Vérifier l'installation
ls /Applications/Google\ Chrome.app

# Installer si nécessaire
brew install --cask google-chrome
```

### Linux

#### Problème : Dépendances manquantes

**Solution :**

```bash
sudo apt-get update
sudo apt-get install python3-pip chromium-browser
pip3 install -r requirements.txt
```

---

## 🎯 Exemples d'Utilisation

### Exemple 1 : Post Viral (1000+ commentaires)

```python
from twitter_scraper import TwitterScraper

scraper = TwitterScraper()
post_url = "https://x.com/elonmusk/status/..."

# Extraire les données
post_data = scraper.scrape_post_data(post_url)
comments = scraper.scrape_comments()  # Tous les commentaires

print(f"✅ {len(comments)} commentaires extraits !")

# Exporter
scraper.export_to_excel(post_data, comments)
scraper.close()
```

### Exemple 2 : Extraction Rapide (100 commentaires)

```python
from twitter_scraper import TwitterScraper

scraper = TwitterScraper(headless=True)  # Mode invisible
post_url = "https://x.com/username/status/..."

post_data = scraper.scrape_post_data(post_url)
comments = scraper.scrape_comments(max_comments=100)  # Limité à 100

scraper.export_to_excel(post_data, comments)
scraper.close()
```

### Exemple 3 : Analyse de Plusieurs Posts

```python
from twitter_scraper import TwitterScraper

posts = [
    "https://x.com/user1/status/111",
    "https://x.com/user2/status/222",
    "https://x.com/user3/status/333"
]

scraper = TwitterScraper()

for post_url in posts:
    post_data = scraper.scrape_post_data(post_url)
    comments = scraper.scrape_comments(max_comments=50)
    scraper.export_to_excel(post_data, comments)
    print(f"✅ {post_url} terminé")

scraper.close()
```

---

## 📚 Structure du Projet

```
ScrapperX/
├── twitter_scraper.py      # Script principal
├── requirements.txt        # Dépendances Python
├── version.py             # Informations de version
├── config.py              # Configuration
├── examples.py            # Exemples d'utilisation
├── test_scraper.py        # Tests
├── run.bat               # Lanceur Windows
├── run_macos.sh          # Lanceur macOS/Linux
├── test_macos.sh         # Tests macOS
├── README.md             # Ce fichier
├── CHANGELOG.md          # Historique des versions
├── CONTRIBUTING.md       # Guide de contribution
└── LICENSE               # Licence MIT
```

---

## 🔒 Sécurité & Confidentialité

### Données Collectées

- ✅ Aucune donnée personnelle stockée
- ✅ Logs locaux uniquement
- ✅ Pas de connexion à des serveurs tiers
- ✅ Fonctionne uniquement sur posts publics

### Bonnes Pratiques

- ✅ Respecter les délais entre requêtes
- ✅ Ne pas scraper trop fréquemment
- ✅ Utiliser uniquement sur posts publics
- ✅ Respecter les ToS de Twitter/X

---

## 🌐 Compatibilité

### Systèmes d'Exploitation

- ✅ **Windows 10/11** : Fonctionne parfaitement
- ✅ **macOS 10.14+** : Compatible (Intel & Apple Silicon)
- ✅ **Linux** : Compatible (Ubuntu, Debian, Fedora, etc.)

### Navigateurs

- ✅ **Google Chrome** : Recommandé
- ⚠️ **Chromium** : Compatible mais non testé

### Python

- ✅ **Python 3.8+** : Recommandé
- ✅ **Python 3.7** : Compatible avec limitations
- ❌ **Python 2.x** : Non supporté

---

## 📈 Performance

### Temps d'Exécution Estimé

| Nombre de Commentaires | Temps Estimé   |
| ---------------------- | -------------- |
| 50 commentaires        | ~1-2 minutes   |
| 100 commentaires       | ~2-4 minutes   |
| 500 commentaires       | ~5-10 minutes  |
| 1000+ commentaires     | ~10-20 minutes |

### Consommation Ressources

- **CPU** : 10-30% (pendant le scraping)
- **RAM** : ~200-400 MB
- **Disque** : ~50 MB (avec dépendances)
- **Réseau** : Variable (selon le post)

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

### Comment Contribuer

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

## 📜 Changelog

Consultez [CHANGELOG.md](CHANGELOG.md) pour l'historique complet des versions.

### Dernières Versions

#### v1.2.1 (2026-01-05)

- 🔧 Correctif UTF-8 pour Windows
- ✅ Support complet des caractères accentués et emojis

#### v1.2.0 (2026-01-04)

- 🛡️ Sécurité et anti-détection
- 🔄 Retry automatique
- 📊 Logging complet

#### v1.1.0 (2026-01-04)

- 🚀 Extraction illimitée de commentaires
- 📈 Progression en temps réel

---

## 📄 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

---

## 👤 Auteur

**Kais OUERIEMMI**

- GitHub: [@Kaisoueriemmi](https://github.com/Kaisoueriemmi)
- Email: contact@kaisoueriemmi.com

---

## 🙏 Remerciements

- [Selenium](https://www.selenium.dev/) - Automatisation du navigateur
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) - Gestion automatique de ChromeDriver
- [openpyxl](https://openpyxl.readthedocs.io/) - Export Excel
- [pandas](https://pandas.pydata.org/) - Manipulation de données

---

## ⭐ Support

Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile sur GitHub !

[![GitHub stars](https://img.shields.io/github/stars/Kaisoueriemmi/ScrapperX.svg?style=social&label=Star)](https://github.com/Kaisoueriemmi/ScrapperX)

---

## 📞 Support & Contact

- 📖 **Documentation** : Ce README
- 📝 **Changelog** : [CHANGELOG.md](CHANGELOG.md)
- 🐛 **Issues** : [GitHub Issues](https://github.com/Kaisoueriemmi/ScrapperX/issues)
- 💬 **Discussions** : [GitHub Discussions](https://github.com/Kaisoueriemmi/ScrapperX/discussions)

---

**Version** : 1.2.1  
**Date** : 2026-01-05  
**Statut** : ✅ Production Ready

**Bon scraping ! 🐦✨**
