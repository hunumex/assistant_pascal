Assistant Pascal
================

Description du projet
---------------------

Assistant Pascal est une application développée pour aider les utilisateurs à accomplir diverses tâches rapidement et efficacement. L'assistant est conçu pour résoudre divers problèmes, notamment en fournissant des réponses aux questions, en organisant des événements et en effectuant des recherches. Le but principal de l'application est de faciliter la vie des utilisateurs en leur fournissant un outil intuitif et intelligent.

Installation
------------

Pour installer l'application Assistant Pascal et ses dépendances, vous devez disposer de Python et Pipenv sur votre système. Voici comment procéder :

1.  Clonez le dépôt GitHub :

bashCopy code

`git clone https://github.com/user/assistant-pascal.git
cd assistant-pascal`

1.  Installez les dépendances et créez un environnement virtuel avec Pipenv :

bashCopy code

`pipenv install`

1.  Activez l'environnement virtuel :

bashCopy code

`pipenv shell`

Si cela pose problème installer les bibliothèques individuellement avec pip install

1. pyttsx3
2. speechrecognition
3. pyaudio
4. pygame
5. python-dotenv
6. gtts
7. openai 

Utilisation
-----------

Pour utiliser l'application Assistant Pascal, exécutez la commande suivante :

bashCopy code

`python main.py`

Vous pouvez également utiliser les options de la ligne de commande pour personnaliser l'expérience utilisateur. Par exemple :

bashCopy code

`python main.py --lang fr --mode text`

Configuration
-------------

Avant d'utiliser l'application, vous devez configurer certaines variables d'environnement dans un fichier `.env`. Voici les variables d'environnement requises :

makefileCopy code

`API_KEY=your_api_key
SECRET_KEY=your_secret_key`

Remplacez `your_api_key` et `your_secret_key` par les clés appropriées.

Contribution
------------

Les contributions au projet Assistant Pascal sont les bienvenues. Pour contribuer, veuillez suivre ces étapes :

1.  Forkez le dépôt GitHub.
2.  Créez une nouvelle branche avec un nom descriptif.
3.  Faites vos modifications et soumettez-les avec des messages de commit clairs.
4.  Créez une demande de fusion en décrivant les modifications apportées et les raisons pour lesquelles elles devraient être intégrées.

Licence
-------

Assistant Pascal est distribué sous la licence MIT. Pour plus d'informations, consultez le fichier `LICENSE` dans le dépôt GitHub.

Badges
------

[![Coverage Status](https://coveralls.io/repos/github/user/assistant-pascal/badge.svg?branch=master)](https://coveralls.io/github/user/assistant-pascal?branch=master) [![Code Quality](https://img.shields.io/lgtm/grade/python/g/user/assistant-pascal.svg)](https://lgtm.com/projects/g/user/assistant-pascal/context:python) ![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)
