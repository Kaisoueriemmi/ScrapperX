# 🚀 Guide de Démarrage Rapide - ScrapperX

## Installation en 3 étapes

### 1️⃣ Cloner le repository

```bash
git clone https://github.com/Kaisoueriemmi/ScrapperX.git
cd ScrapperX
```

### 2️⃣ Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Lancer le scraper

```bash
python twitter_scraper.py
```

## 📝 Utilisation Simple

1. **Lancez le programme**

   ```bash
   python twitter_scraper.py
   ```

2. **Entrez l'URL du post Twitter/X**

   ```
   📎 Entrez l'URL du post Twitter/X: https://twitter.com/username/status/1234567890
   ```

3. **Choisissez le mode d'extraction** 🆕

   ```
   💬 Nombre de commentaires à extraire:
      1. Tous les commentaires (recommandé)
      2. Nombre limité

   Votre choix (1 ou 2): 1
   ```

4. **Attendez l'extraction**
   Le scraper va automatiquement:

   - ✅ Extraire les statistiques (retweets, likes, vues)
   - ✅ Défiler pour charger TOUS les commentaires
   - ✅ Afficher la progression en temps réel
   - ✅ Créer un fichier Excel

5. **Récupérez votre fichier Excel**
   Le fichier sera créé dans le même dossier avec un nom comme:
   ```
   twitter_scrape_20260104_215236.xlsx
   ```

## 📊 Contenu du Fichier Excel

### Feuille 1: Statistiques du Post

| Métrique                  | Valeur       |
| ------------------------- | ------------ |
| URL                       | Lien du post |
| Retweets                  | Nombre de RT |
| Likes                     | Nombre de ❤️ |
| Réponses                  | Nombre de 💬 |
| Vues                      | Nombre de 👁️ |
| **Commentaires extraits** | **Nombre**   |

### Feuille 2: Commentaires

| #   | Utilisateur | Handle     | Texte       | Date       | Likes | RT  | **Réponses** |
| --- | ----------- | ---------- | ----------- | ---------- | ----- | --- | ------------ |
| 1   | John Doe    | @johndoe   | Super post! | 2026-01-04 | 12    | 3   | **2**        |
| 2   | Jane Smith  | @janesmith | Merci!      | 2026-01-04 | 5     | 0   | **0**        |

## 🎯 Exemples d'URLs Valides

```
https://twitter.com/elonmusk/status/1234567890
https://x.com/username/status/9876543210
https://twitter.com/user/status/1111111111
```

## ⚙️ Options Avancées

### 🆕 Extraction de TOUS les commentaires (Nouveau!)

**Mode par défaut** : Le scraper extrait maintenant TOUS les commentaires disponibles!

- Défilement automatique jusqu'à la fin
- Affichage de la progression en temps réel
- Détection intelligente de la fin du contenu
- Déduplication automatique

### Limiter le nombre de commentaires

Pour l'utilisation programmatique:

```python
from twitter_scraper import TwitterScraper

scraper = TwitterScraper()
post_data = scraper.scrape_post_data(post_url)

# Extraire tous les commentaires (par défaut)
comments = scraper.scrape_comments()

# OU limiter à un nombre spécifique
comments = scraper.scrape_comments(max_comments=50)

scraper.export_to_excel(post_data, comments)
scraper.close()
```

### Voir le navigateur en action

Commentez la ligne headless dans `twitter_scraper.py`:

```python
# chrome_options.add_argument('--headless')
```

## 🆘 Problèmes Courants

### ❌ "ChromeDriver not found"

**Solution:**

```bash
python -m pip install --upgrade webdriver-manager
```

### ❌ "No such element"

**Solution:** La structure de Twitter a changé. Attendez une mise à jour du scraper.

### ❌ Timeout errors

**Solution:** Augmentez les délais dans le code:

```python
time.sleep(10)  # Au lieu de 5
```

## 📞 Support

- 🐛 **Bugs:** Ouvrez une issue sur GitHub
- 💡 **Suggestions:** Pull requests bienvenues
- 📧 **Contact:** Via GitHub

## ⚠️ Important

- ✅ Utilisez sur des posts **publics** uniquement
- ✅ Respectez les limites de Twitter/X
- ✅ Usage **éducatif** et **responsable**

---

**Bon scraping! 🐦✨**
