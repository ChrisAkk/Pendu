# 🪓 Jeu du Pendu

Groupe (MITD02) : Chris Abou Karam, Yassine Krifa et Anis Chader

Projet réalisé dans le cadre de la première année de Licence (L1). L'objectif est de concevoir un jeu du pendu complet avec une interface graphique web, une gestion de session, des effets sonores et un système anti-triche.

-> Le README a été entièrement rédigé par l'intelligence artificielle Claude pour gagner du temps (bien sûr, il a été corrigé ensuite).

---

## 🎮 Fonctionnalités

- **9 thèmes disponibles** : Animaux, Pays, Films/Séries, Personnages, Nourriture, Musique, Sport, Sciences, Histoire
- **3 niveaux de difficulté** par longueur de mot : 4–6 lettres, 7–10 lettres, 11 lettres et plus
- **Nombre d'essais personnalisable** : de 3 à 12
- **Option indice** : un indice textuel peut être affiché pour aider le joueur
- **Longueur de mot aléatoire** : possibilité de laisser le jeu choisir la difficulté
- **Clavier virtuel + support du clavier physique**
- **Effets sonores** : musique d'ambiance, sons de bonne/mauvaise réponse, victoire et défaite
- **Journal des parties** : historique des 50 derniers résultats (victoires et défaites)
- **Système anti-triche** : détection de manipulation des requêtes HTTP via un ticket de session
- **Page d'aide** intégrée avec les règles du jeu

---

## 🚀 Lancer le projet

### Prérequis

- Python 3.x
- Flask

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-utilisateur/pendu.git
cd pendu

# Installer les dépendances
pip install flask

# Lancer l'application
python app.py
```

L'application sera accessible à l'adresse : [http://localhost:5002](http://localhost:5002)

---

## 📁 Structure du projet

```
Pendu/
├── app.py                  # Point d'entrée : initialise le serveur Flask
├── routes.py               # Gestion des routes et de la logique de jeu
├── dictionnaire.py         # Base de données des mots (9 thèmes × 3 longueurs)
├── dictionnaireIA.py       # Dictionnaire étendu généré par IA
├── templates/
│   ├── index.html          # Page d'accueil, menu et configuration
│   ├── game.html           # Page de jeu
│   └── triche.html         # Page affichée en cas de tentative de triche
├── static/
│   ├── css/
│   │   ├── index.css       # Styles de la page d'accueil
│   │   └── game.css        # Styles de la page de jeu
│   ├── js/
│   │   └── index.js        # Interactions : thèmes, toggles, clavier, effets
│   ├── img/
│   │   ├── pendu/          # Images des étapes du pendu (0.png à 11.png + win/lost)
│   │   └── ...             # Images de fond et décors
│   └── sons/
│       ├── ambiance.mp3    # Musique du menu
│       ├── game.mp3        # Musique en partie
│       ├── correct.mp3     # Son bonne lettre
│       ├── wrong.mp3       # Son mauvaise lettre
│       ├── win.mp3         # Son victoire
│       └── loose.mp3       # Son défaite / triche
└── LICENSE
```

---

## 🔁 Fonctionnement technique

### Routes Flask (`routes.py`)

|      Route     | Méthode |                        Description                            |
|----------------|---------|---------------------------------------------------------------|
| `/`            | GET     | Page d'accueil avec l'historique des parties                  |
| `/game`        | POST    | Initialise une nouvelle partie selon la configuration choisie |
| `/take_chance` | POST    | Traite la lettre proposée par le joueur                       |

### Session Flask

Toutes les données de la partie en cours sont stockées côté serveur dans la session Flask :
- le mot à deviner, son état masqué, le thème, la difficulté
- le compteur d'erreurs, le nombre d'essais, l'index d'image du pendu
- les lettres déjà jouées, l'indice, l'historique des parties

### Système anti-triche

À chaque partie, un ticket aléatoire est généré et stocké en session. Il est envoyé dans chaque requête de lettre et vérifié côté serveur. Si le ticket ne correspond pas (requête rejouée ou modifiée), le joueur est redirigé vers la page `triche.html`.

---

## 📖 Règles du jeu

1. Un mot est tiré aléatoirement selon le thème et la longueur choisis.
2. Le mot est affiché sous forme de tirets (`_`).
3. Le joueur propose des lettres une par une via le clavier virtuel ou son clavier physique.
4. **Bonne lettre** : elle s'affiche à sa ou ses positions dans le mot.
5. **Mauvaise lettre** : une partie du pendu apparaît et un essai est décompté.
6. **Victoire** : toutes les lettres sont trouvées avant d'épuiser les essais.
7. **Défaite** : le nombre d'essais est atteint avant de compléter le mot.

---

## 🛠️ Technologies utilisées

- **Back-end** : Python, Flask
- **Front-end** : HTML5, CSS3, JavaScript (Vanilla)
- **Templating** : Jinja2
- **Icônes** : [Remix Icon](https://remixicon.com/)
- **Sons** : libre de droit sur le site freesound (https://freesound.org/)
- **Images** : Tous creer par Chris Abou Karam

---

