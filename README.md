# Application Python pour Jenkins

## Description

Projet simple pour apprendre Jenkins et découvrir les tests unitaires.

## Prérequis

1. Docker

2. Git

3. python >= 3.9 & < 4.

4. venv avec python

5. Jenkins

## Démarrage

```shell
# venv : est un programme en Python
# pour créer une copie du répertoire "python" dans notre projet
# .venv : répertoire de destination de notre copie, c est lui qui contiendra
# les dependances installees avec "pip install"
python -m venv .venv

# activation de l'environnement virtuel de PowerShell
.\.venv\Scripts\Activate.ps1
# activation de l'environnement virtuel en cmd
.\.venv\Scripts\activate.bat
# activation de l'environnement virtuel en shell/bash/bsh
sheel ./.venv/Scripts/activate

# installation des dependances du projet depuis le fichier requirements.txt
pip install -r .\requirements.txt
```

## Notes

[Moteur de recherche](https://google.fr)