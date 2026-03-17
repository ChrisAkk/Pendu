# Pendu

🪓 Jeu du Pendu - Projet L1
Ce projet a été réalisé dans le cadre de ma première année de Licence (L1). L'objectif est de créer un jeu du pendu fonctionnant avec une interface graphique web.

🚀 Comment lancer le projet ?
Le point d'entrée de l'application est le fichier app.py. C'est lui qui initialise le serveur et permet d'accéder au site.

📁 Organisation des fichiers
Le projet est découpé en plusieurs fichiers pour bien séparer la logique de l'affichage :

app.py : Le script principal qui lance le serveur.

routes.py : Assure la communication entre Python et le HTML. Il récupère les choix de l'utilisateur (formulaires) et renvoie les données nécessaires au jeu.

dictionnaire.py : Contient la base de données des mots. Ils sont organisés par thèmes (9 au total) et triés selon 3 longueurs de caractères différentes pour ajuster la difficulté.

Dossier /static : Regroupe les ressources visuelles et techniques (images, CSS, JavaScript, vidéos).

Dossier /templates : Contient les pages de structure du site (index.html pour l'accueil et game.html pour la partie en cours).
