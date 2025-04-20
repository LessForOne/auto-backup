# GitHub Auto Backup

Un script Python pour sauvegarder automatiquement tous vos dépôts GitHub en local via SSH.

## Fonctionnalités

- Clone automatiquement tous vos dépôts GitHub
- Utilise SSH pour une connexion sécurisée
- Organise les sauvegardes par date
- Configuration simple via fichier YAML

## Prérequis

- Python 3.x
- Git installé
- Un token d'accès GitHub

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/ton_utilisateur/auto-backup.git
cd auto-backup
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez vos identifiants GitHub :
   - Renommez `config.example.yaml` en `config.yaml`
   - Modifiez le fichier avec vos informations :
```yaml
github_token: "ghp_xxxxxxxx"  # Votre token GitHub
github_user: "votre_username"  # Votre nom d'utilisateur GitHub
backup_dir: "backups"         # Dossier de sauvegarde
```

## Utilisation

Exécutez simplement :
```bash
python backup.py
```

Les dépôts seront clonés dans un dossier `backups/YYYY-MM-DD` (par exemple : `backups/2025-04-20`).

## Structure du projet

```
.
├── backup.py           # Script principal
├── config.yaml         # Configuration (à créer)
├── config.example.yaml # Exemple de configuration
└── backups/           # Dossier des sauvegardes
```

## Sécurité

- Ne partagez jamais votre token GitHub
- Gardez votre fichier `config.yaml` sécurisé
- Utilisez des permissions appropriées pour vos fichiers de configuration
