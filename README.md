
# GitHub Auto Backup

Ce projet permet de **backuper tous tes repositories GitHub** dans un répertoire local, en utilisant **SSH** pour cloner les dépôts.

## Prérequis

- **Python 3.x**
- **Git** installé
- Un **token GitHub** pour l'authentification

## Installation

1. **Clone ce repository** sur ta machine :

   ```bash
   git clone https://github.com/ton_utilisateur/auto-backup.git
   cd auto-backup
Installe les dépendances Python :

Si tu n'as pas déjà installé les dépendances, exécute la commande suivante :

bash
Copier le code
pip install -r requirements.txt
Configure tes credentials GitHub :

Renomme le fichier config.example.yaml en config.yaml.

Ouvre config.yaml et remplis avec tes informations :

github_token: Ton token GitHub (génère-le depuis GitHub).

github_user: Ton nom d'utilisateur GitHub.

Exemple de configuration :

yaml
Copier le code
github_token: "ghp_xxxxxxxx"  # Ton token GitHub
github_user: "ton_github_username"
backup_dir: "backups"
Utilisation
Une fois que ta configuration est prête, il te suffit de lancer le script Python pour cloner tous tes dépôts :

bash
Copier le code
python backup.py
Les dépôts seront clonés dans un dossier backups avec la date du jour. Par exemple, les dépôts clonés aujourd'hui seront dans un dossier backups/2025-04-20.

Structure des fichiers
backup.py: Le script Python qui gère le clonage des repos.

config.yaml: Le fichier de configuration contenant ton token et ton nom d'utilisateur GitHub.

backups/: Le répertoire où tes dépôts seront sauvegardés.

config.example.yaml: Exemple de configuration à adapter.
