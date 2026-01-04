# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer à **ScrapperX** ! Nous accueillons toutes les contributions, qu'il s'agisse de corrections de bugs, de nouvelles fonctionnalités ou d'améliorations de la documentation.

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Signaler un Bug](#signaler-un-bug)
- [Proposer une Fonctionnalité](#proposer-une-fonctionnalité)
- [Soumettre une Pull Request](#soumettre-une-pull-request)
- [Standards de Code](#standards-de-code)
- [Structure du Projet](#structure-du-projet)

## 📜 Code de Conduite

En participant à ce projet, vous acceptez de respecter notre code de conduite :

- Soyez respectueux et inclusif
- Acceptez les critiques constructives
- Concentrez-vous sur ce qui est le mieux pour la communauté
- Faites preuve d'empathie envers les autres membres

## 🚀 Comment Contribuer

### 1. Fork le Repository

```bash
# Cliquez sur le bouton "Fork" en haut de la page GitHub
# Puis clonez votre fork
git clone https://github.com/VOTRE_USERNAME/ScrapperX.git
cd ScrapperX
```

### 2. Créer une Branche

```bash
# Créez une branche pour votre fonctionnalité ou correction
git checkout -b feature/ma-nouvelle-fonctionnalite
# ou
git checkout -b fix/correction-bug
```

### 3. Faire vos Modifications

- Écrivez du code propre et commenté
- Suivez les standards de code Python (PEP 8)
- Testez vos modifications

### 4. Commit vos Changements

```bash
git add .
git commit -m "feat: ajouter une nouvelle fonctionnalité"
# ou
git commit -m "fix: corriger le bug XYZ"
```

**Format des messages de commit:**

- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage, points-virgules manquants, etc.
- `refactor:` Refactorisation du code
- `test:` Ajout de tests
- `chore:` Maintenance

### 5. Push vers GitHub

```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

### 6. Créer une Pull Request

- Allez sur votre fork sur GitHub
- Cliquez sur "New Pull Request"
- Décrivez vos changements en détail
- Attendez la review

## 🐛 Signaler un Bug

Si vous trouvez un bug, veuillez créer une issue avec :

**Template de Bug Report:**

```markdown
### Description du Bug

[Description claire et concise du bug]

### Étapes pour Reproduire

1. Aller à '...'
2. Cliquer sur '...'
3. Faire défiler jusqu'à '...'
4. Voir l'erreur

### Comportement Attendu

[Ce qui devrait se passer]

### Comportement Actuel

[Ce qui se passe réellement]

### Captures d'Écran

[Si applicable, ajoutez des captures d'écran]

### Environnement

- OS: [ex. Windows 11]
- Python: [ex. 3.11.0]
- Version Chrome: [ex. 120.0.0]
- Version ScrapperX: [ex. 1.0.0]

### Informations Supplémentaires

[Tout autre contexte pertinent]
```

## 💡 Proposer une Fonctionnalité

Pour proposer une nouvelle fonctionnalité :

**Template de Feature Request:**

```markdown
### Description de la Fonctionnalité

[Description claire de la fonctionnalité]

### Problème Résolu

[Quel problème cette fonctionnalité résout-elle?]

### Solution Proposée

[Comment pensez-vous que cela devrait fonctionner?]

### Alternatives Considérées

[Avez-vous pensé à d'autres solutions?]

### Exemples d'Utilisation

[Montrez comment cette fonctionnalité serait utilisée]
```

## 🔍 Soumettre une Pull Request

### Checklist avant de soumettre

- [ ] Le code suit les standards PEP 8
- [ ] Les commentaires sont clairs et en français
- [ ] La documentation est mise à jour si nécessaire
- [ ] Les tests passent (si applicable)
- [ ] Le commit message suit le format conventionnel
- [ ] La PR a une description claire

### Process de Review

1. Un mainteneur reviewera votre PR
2. Des changements peuvent être demandés
3. Une fois approuvée, votre PR sera mergée
4. Vous serez ajouté aux contributeurs ! 🎉

## 📝 Standards de Code

### Style Python

```python
# ✅ BON
def scrape_comments(self, max_comments=50):
    """
    Scrape les commentaires du post

    Args:
        max_comments (int): Nombre maximum de commentaires

    Returns:
        list: Liste des commentaires
    """
    comments = []
    # Code...
    return comments

# ❌ MAUVAIS
def scrapeComments(self,maxComments=50):
    comments=[]
    return comments
```

### Conventions de Nommage

- **Variables**: `snake_case`
- **Fonctions**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_CASE`

### Documentation

- Utilisez des docstrings pour toutes les fonctions
- Commentez le code complexe
- Mettez à jour le README si nécessaire

## 📁 Structure du Projet

```
ScrapperX/
├── .git/                   # Git repository
├── .gitignore             # Fichiers à ignorer
├── CHANGELOG.md           # Historique des versions
├── CONTRIBUTING.md        # Ce fichier
├── DEMO.md                # Démonstrations
├── LICENSE                # Licence MIT
├── QUICKSTART.md          # Guide de démarrage rapide
├── README.md              # Documentation principale
├── config.py              # Configuration
├── examples.py            # Exemples d'utilisation
├── requirements.txt       # Dépendances Python
└── twitter_scraper.py     # Script principal
```

## 🎯 Domaines de Contribution

Nous recherchons des contributions dans les domaines suivants :

### 🔧 Code

- Nouvelles fonctionnalités
- Corrections de bugs
- Optimisations de performance
- Support de nouvelles plateformes

### 📚 Documentation

- Amélioration du README
- Tutoriels et guides
- Traductions
- Exemples d'utilisation

### 🧪 Tests

- Tests unitaires
- Tests d'intégration
- Tests de performance

### 🎨 Design

- Interface graphique (GUI)
- Visualisations de données
- Logos et assets

## 🏆 Contributeurs

Merci à tous nos contributeurs ! 🎉

<!-- ALL-CONTRIBUTORS-LIST:START -->

- **Kais Oueriemmi** - _Créateur & Mainteneur_ - [@Kaisoueriemmi](https://github.com/Kaisoueriemmi)
<!-- ALL-CONTRIBUTORS-LIST:END -->

## 📞 Questions ?

Si vous avez des questions :

- 💬 Ouvrez une [Discussion](https://github.com/Kaisoueriemmi/ScrapperX/discussions)
- 🐛 Créez une [Issue](https://github.com/Kaisoueriemmi/ScrapperX/issues)
- 📧 Contactez-nous via GitHub

## 📄 Licence

En contribuant à ScrapperX, vous acceptez que vos contributions soient sous licence MIT.

---

**Merci de contribuer à ScrapperX ! 🚀**
