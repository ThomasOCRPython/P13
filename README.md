## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

- A partir de Heroku : `https://dashboard.heroku.com/apps/oc-lettings-thomas` on selectionne "open app", qui ouvre l'application à l'adresse suivant : `https://oc-lettings-thomas.herokuapp.com/`.
### Prérequis

- Compte [DockerHub](https://hub.docker.com/)
- Compte [CircleCI](https://circleci.com/signup/)
- Compte [Heroku](https://signup.heroku.com/)
- Installer [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Compte [Sentry](https://sentry.io/signup/)

### Installation 

 1. Créer le repository Github
 2. Créer un projet Heroku
 3. Lier le repository Github avec le compte [CircleCI](https://app.circleci.com/projects)
 4. Créer un projet Sentry et récupérer la clé [SDK](https://sentry.io/openranga/django/getting-started/python-django/)
 5. Récupérer un token d'authentification Heroku. [Documentation](https://devcenter.heroku.com/articles/authentication)
 6. Informer les [clés d'environnement](#cles-denvironnement) dans les settings du projet CircleCI et Heroku
 7. Commit le fichier sur la branche `master`
 8. 
 


 ### Clés d'environnement

| Clé  | Valeur          | Destination |
| :--------------: |:---------------:|:---------:|
| DOCKER_PASSWORD  |   Mot de passe Dockerhub  | CircleCI/project/settings |
| DOCKER_USENAME  |   Identifiant Dockerhub  | CircleCI/project/settings |
| HEROKU_TOKEN  | Tocken  Heroku  | CircleCI/project/settings |
| DEBUG  | FAlSE  | CircleCI/project/settings |
| SECRET_KEY  | `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s` | Heroku/project/settings |
| SENTRY_SDK  | Adresse Sentry  | Heroku/project/settings |