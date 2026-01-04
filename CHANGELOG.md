# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

## [1.0.0] - 2026-01-04

### ✨ Ajouté

- **Scraper Twitter/X complet** avec Selenium
  - Extraction des statistiques de post (retweets, likes, réponses, vues)
  - Scraping des commentaires avec détails complets
  - Support des posts publics
- **Export Excel professionnel**
  - Feuille "Statistiques Post" avec métriques du post
  - Feuille "Commentaires" avec tous les détails
  - Mise en forme avec couleurs Twitter/X
  - Colonnes auto-dimensionnées
- **Interface utilisateur**
  - CLI simple et intuitive
  - Messages en français
  - Indicateurs de progression
  - Gestion d'erreurs robuste
- **Documentation complète**
  - README.md détaillé
  - QUICKSTART.md pour démarrage rapide
  - Fichier examples.py avec cas d'usage
  - Configuration centralisée (config.py)
- **Fonctionnalités avancées**
  - Mode headless (sans interface graphique)
  - Scroll automatique pour charger plus de commentaires
  - Noms de fichiers avec timestamp
  - Support des URLs twitter.com et x.com

### 🔧 Configuration

- Chrome WebDriver avec gestion automatique
- User-Agent personnalisé pour éviter la détection
- Délais configurables pour le chargement
- Nombre de commentaires paramétrable

### 📦 Dépendances

- selenium >= 4.0.0
- webdriver-manager
- openpyxl
- pandas
- beautifulsoup4
- requests

### 📄 Licence

- Licence MIT

### 👤 Auteur

- Kais Oueriemmi (@Kaisoueriemmi)

---

## Format du Changelog

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

### Types de changements

- **Ajouté** pour les nouvelles fonctionnalités
- **Modifié** pour les changements aux fonctionnalités existantes
- **Déprécié** pour les fonctionnalités bientôt supprimées
- **Supprimé** pour les fonctionnalités supprimées
- **Corrigé** pour les corrections de bugs
- **Sécurité** en cas de vulnérabilités
