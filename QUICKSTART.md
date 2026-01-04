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

3. **Attendez l'extraction**
   Le scraper va automatiquement:

   - ✅ Extraire les statistiques (retweets, likes, vues)
   - ✅ Collecter les commentaires
   - ✅ Créer un fichier Excel

4. **Récupérez votre fichier Excel**
   Le fichier sera créé dans le même dossier avec un nom comme:
   ```
   twitter_scrape_20260104_213845.xlsx
   ```

## 📊 Contenu du Fichier Excel

### Feuille 1: Statistiques du Post

| Métrique | Valeur       |
| -------- | ------------ |
| URL      | Lien du post |
| Retweets | Nombre de RT |
| Likes    | Nombre de ❤️ |
| Réponses | Nombre de 💬 |
| Vues     | Nombre de 👁️ |

### Feuille 2: Commentaires

| #   | Utilisateur | Handle     | Texte       | Date       | Likes | RT  |
| --- | ----------- | ---------- | ----------- | ---------- | ----- | --- |
| 1   | John Doe    | @johndoe   | Super post! | 2026-01-04 | 12    | 3   |
| 2   | Jane Smith  | @janesmith | Merci!      | 2026-01-04 | 5     | 0   |

## 🎯 Exemples d'URLs Valides

```
https://twitter.com/elonmusk/status/1234567890
https://x.com/username/status/9876543210
https://twitter.com/user/status/1111111111
```

## ⚙️ Options Avancées

### Modifier le nombre de commentaires

Ouvrez `twitter_scraper.py` et modifiez:

```python
comments = self.scrape_comments(max_comments=100)  # Par défaut: 50
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
