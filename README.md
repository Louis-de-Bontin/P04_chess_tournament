# Utilisation du programme

### Lancer le programme :
- Créer le dossier de destination
- Se localiser dans le dossier de destination
- Cloner le code via le lien suivant : https://github.com/likhardcore/P04_chess_tournament.git
- Créer un environnement virtuel avec la commande `python -m venv env`
- Activer l'environnement virtuel avec la commande `env/scripts/activate` sous windows ou `env/bin/activate` sous macOS. 
- Installer les packages avec la commande `pip install -r requirements.txt`
- Lancer le programme avec la commande `python __main__.py`

### Utiliser le programme :
##### 1) Créer un tournois
- Le programme vous demandes différentes informations à propos du tournois.
- Note : il sera impossible de faire un tournois si il n’y a pas au moins 4 joueurs.
- Vous pouvez ensuite les valider et continuer, ou les invalider pour les entrer à nouveau en cas d’erreur.
- Avant de commencer le premier round, le programme demande si vous voulez conserver le nombre de rounds total à la valeur par défaut (4).
- Vous avez ensuite le choix de poursuivre ou de retourner au menu principal.
- Les matchs sont créés si vous choisissez de poursuivre. Vous devez maintenant rentrer les résultats des matchs.
- Une fois fait, le tournois est sauvegardé, et vous avez le choix de continuer, ou de retourner au menu principal.
- Si vous continuez, les étapes précédentes se répètent jusqu’à la fin du tournois.
- Une fois le tournois fini vous êtes redirigé vers le menu principal.

##### 2) Gérer les joueurs
Vous pouvez soit :
- Créer des joueurs (entre 1 et 20 à la fois) en entrant les infos demandées. En cas d’erreur, vous pourrez recommencer à la fin.
- Modifier le rang d’un joueur
- Afficher la liste de joueurs enregistrés

##### 3) Charger un tournois en cours
- La liste des tournois pas terminés s’affichent
- Vous pouvez reprendre le tournois de votre choix

##### 4) Afficher un tournois terminé
- La liste des tournois terminés s’affichent
- Vous pouvez voir dans le détail les résultats d’un des tournois qui s’affichent

##### 5) Quitter
Permet de quitter le programme

### Générer le rapport flake8 :
- Installer flake8 avec la commande `pip intall flake8-html`
- S'il n'existe pas, créer un fichier *setup.cfg*
- Ecrire le texte suivant dedans :
```
[flake8]
exclude = .git, env, __pycache__, .gitignore
max-line-length = 119
```
- Taper la commande `flake8 --format=html --htmldir=flake-report`
- Le rapport est apparu dans un dossier nommé *flake-report*