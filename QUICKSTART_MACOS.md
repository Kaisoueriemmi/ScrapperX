# 🚀 Guide de Démarrage Rapide - ScrapperX pour macOS

## 🍎 Installation sur macOS

### Prérequis

- macOS 10.14 (Mojave) ou supérieur
- Python 3.8 ou supérieur
- Google Chrome installé

---

## 📦 Installation en 3 Étapes

### 1️⃣ Vérifier Python

Ouvrez le Terminal (Applications → Utilitaires → Terminal) et vérifiez votre version de Python :

```bash
python3 --version
```

Si Python n'est pas installé, installez-le via Homebrew :

```bash
# Installer Homebrew (si pas déjà installé)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer Python
brew install python@3.11
```

### 2️⃣ Installer les Dépendances

Naviguez vers le dossier du projet :

```bash
cd ~/Downloads/ScrapperX  # Ajustez le chemin selon votre installation
```

Installez les dépendances :

```bash
pip3 install -r requirements.txt
```

### 3️⃣ Lancer le Scraper

```bash
python3 twitter_scraper.py
```

---

## 🎯 Utilisation Rapide

### Étape 1 : Entrez l'URL du Post

```
📎 Entrez l'URL du post Twitter/X: https://x.com/username/status/123456
```

### Étape 2 : Choisissez le Mode d'Extraction

```
💬 Nombre de commentaires à extraire:
   1. Tous les commentaires (recommandé)
   2. Nombre limité

Votre choix (1 ou 2): 1
```

### Étape 3 : Choisissez le Mode d'Affichage

```
👁️ Mode d'affichage:
   1. Mode visible (recommandé pour debug)
   2. Mode headless (invisible)

Votre choix (1 ou 2): 1
```

### Étape 4 : Attendez l'Extraction

Le scraper va :

- ✅ Ouvrir Chrome automatiquement
- ✅ Charger le post Twitter/X
- ✅ Défiler pour charger tous les commentaires
- ✅ Extraire toutes les données
- ✅ Créer un fichier Excel

### Étape 5 : Récupérez Votre Fichier

Le fichier Excel sera créé dans le même dossier :

```
twitter_scrape_20260104_222230.xlsx
```

---

## 🔧 Dépannage macOS

### ❌ Problème : "command not found: python"

**Solution :** Utilisez `python3` au lieu de `python`

```bash
python3 twitter_scraper.py
```

### ❌ Problème : "Permission denied"

**Solution :** Ajoutez les permissions d'exécution

```bash
chmod +x twitter_scraper.py
```

### ❌ Problème : ChromeDriver ne démarre pas

**Solution 1 :** Autorisez ChromeDriver dans les Préférences Système

1. Allez dans **Préférences Système** → **Sécurité et confidentialité**
2. Cliquez sur **Autoriser quand même** pour ChromeDriver

**Solution 2 :** Installez ChromeDriver manuellement

```bash
brew install chromedriver
```

### ❌ Problème : "SSL: CERTIFICATE_VERIFY_FAILED"

**Solution :** Installez les certificats Python

```bash
/Applications/Python\ 3.11/Install\ Certificates.command
```

### ❌ Problème : Chrome ne s'ouvre pas

**Solution :** Vérifiez que Chrome est installé

```bash
# Vérifier l'installation de Chrome
ls /Applications/Google\ Chrome.app

# Si Chrome n'est pas installé, téléchargez-le depuis
# https://www.google.com/chrome/
```

---

## 🍎 Commandes Spécifiques macOS

### Créer un Alias pour Lancement Rapide

Ajoutez ceci à votre `~/.zshrc` ou `~/.bash_profile` :

```bash
alias scrapperx='cd ~/Downloads/ScrapperX && python3 twitter_scraper.py'
```

Puis rechargez :

```bash
source ~/.zshrc  # ou source ~/.bash_profile
```

Maintenant vous pouvez lancer avec :

```bash
scrapperx
```

### Créer une Application macOS (Optionnel)

1. Ouvrez **Automator**
2. Créez une nouvelle **Application**
3. Ajoutez une action **Exécuter un script shell**
4. Collez ce code :

```bash
cd ~/Downloads/ScrapperX
/usr/local/bin/python3 twitter_scraper.py
```

5. Enregistrez comme "ScrapperX.app"
6. Double-cliquez pour lancer !

---

## 📊 Fichier Excel Généré

### Emplacement

Le fichier sera créé dans le dossier du projet :

```
~/Downloads/ScrapperX/twitter_scrape_YYYYMMDD_HHMMSS.xlsx
```

### Ouvrir avec Numbers ou Excel

```bash
# Ouvrir avec Numbers (macOS)
open twitter_scrape_*.xlsx

# Ou avec Excel si installé
open -a "Microsoft Excel" twitter_scrape_*.xlsx
```

### Contenu

**Feuille 1 : Statistiques Post**

- URL, Retweets, Likes, Réponses, Vues
- Nombre de commentaires extraits
- Nombre de scrolls effectués

**Feuille 2 : Commentaires**

- Username, Handle, Texte, Date
- Likes, Retweets, Réponses

---

## 🔒 Sécurité et Confidentialité sur macOS

### Permissions Requises

Le scraper peut demander les permissions suivantes :

- ✅ **Accès à Chrome** : Pour automatiser le navigateur
- ✅ **Accès réseau** : Pour charger les pages Twitter/X
- ✅ **Accès au dossier** : Pour créer le fichier Excel

### Fichiers Créés

- `scraper.log` : Logs détaillés (local uniquement)
- `twitter_scrape_*.xlsx` : Fichier Excel avec les données
- Aucune donnée n'est envoyée à des serveurs tiers

---

## 🎨 Mode Sombre macOS

Le scraper respecte le mode sombre de macOS. Les logs dans le Terminal s'adapteront automatiquement.

---

## ⚡ Raccourcis Clavier macOS

Pendant l'exécution :

- **Cmd + C** : Arrêter le scraper
- **Cmd + Q** : Quitter le Terminal
- **Cmd + W** : Fermer la fenêtre Chrome

---

## 📱 Compatibilité

### Versions macOS Testées

- ✅ macOS Sonoma (14.x)
- ✅ macOS Ventura (13.x)
- ✅ macOS Monterey (12.x)
- ✅ macOS Big Sur (11.x)
- ✅ macOS Catalina (10.15)

### Architectures

- ✅ **Apple Silicon (M1/M2/M3)** : Fonctionne nativement
- ✅ **Intel** : Fonctionne parfaitement

---

## 🔄 Mise à Jour

Pour mettre à jour le scraper :

```bash
cd ~/Downloads/ScrapperX
git pull  # Si installé via Git

# Ou téléchargez la dernière version et remplacez les fichiers
```

Puis réinstallez les dépendances :

```bash
pip3 install -r requirements.txt --upgrade
```

---

## 📝 Logs et Débogage

### Consulter les Logs

```bash
# Voir les logs en temps réel
tail -f scraper.log

# Voir les dernières lignes
tail -n 50 scraper.log

# Ouvrir avec TextEdit
open -a TextEdit scraper.log
```

### Activer le Mode Verbose

Pour plus de détails, modifiez `twitter_scraper.py` :

```python
# Ligne 40 environ
logging.basicConfig(
    level=logging.DEBUG,  # Changez INFO en DEBUG
    ...
)
```

---

## 🎯 Exemples d'URLs Valides

```
https://x.com/elonmusk/status/1234567890
https://twitter.com/username/status/9876543210
https://x.com/user/status/1111111111
```

---

## 💡 Astuces macOS

### 1. Utiliser Spotlight

Ajoutez le dossier ScrapperX aux favoris du Finder, puis :

- **Cmd + Space** → Tapez "ScrapperX" → Entrée

### 2. Créer un Service Quick Action

1. Ouvrez **Automator**
2. Créez un **Service rapide**
3. Ajoutez **Exécuter un script shell**
4. Configurez pour recevoir du texte (URL)
5. Enregistrez comme "Scraper Twitter"

Maintenant, clic droit sur une URL → Services → Scraper Twitter !

### 3. Utiliser avec Alfred (si installé)

Créez un workflow Alfred pour lancer le scraper avec une URL.

---

## 🆘 Support

### Problèmes Courants

| Problème            | Solution                      |
| ------------------- | ----------------------------- |
| Python non trouvé   | Utilisez `python3`            |
| Permission refusée  | `chmod +x twitter_scraper.py` |
| ChromeDriver bloqué | Autorisez dans Sécurité       |
| SSL Error           | Installez les certificats     |

### Ressources

- 📖 **README.md** : Documentation complète
- 🔒 **SECURITY_v1.2.0.md** : Guide de sécurité
- 📝 **CHANGELOG.md** : Historique des versions
- 📊 **scraper.log** : Logs détaillés

---

## 🎉 C'est Parti !

Vous êtes prêt à scraper Twitter/X sur macOS ! 🚀

```bash
python3 twitter_scraper.py
```

---

**Version** : 1.2.0  
**Plateforme** : macOS 10.14+  
**Auteur** : Kais OUERIEMMI  
**Licence** : MIT

**Bon scraping ! 🐦✨**
