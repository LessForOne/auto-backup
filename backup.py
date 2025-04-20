import os
import requests
import subprocess
from datetime import datetime
import yaml

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

GITHUB_TOKEN = config["github_token"]
GITHUB_USER = config["github_user"]
BACKUP_DIR = config.get("backup_dir", "backups")

# Headers for GitHub API
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repos():
    url = "https://api.github.com/user/repos?per_page=100"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    repos = response.json()
    return [
        (repo["name"], f"git@github-personal:{repo['full_name']}.git")
        for repo in repos
    ]

def clone_repos(repos, date_folder):
    for name, clone_url in repos:
        repo_path = os.path.join(date_folder, name)
        if os.path.exists(repo_path):
            print(f"🟡 Repo {name} already exists, skipping.")
        else:
            print(f"🟢 Cloning {name}...")
            subprocess.run(["git", "clone", clone_url, repo_path], check=True)

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    date_folder = os.path.join(BACKUP_DIR, today)
    os.makedirs(date_folder, exist_ok=True)

    repos = get_repos()
    clone_repos(repos, date_folder)
    print(f"✅ Backup complete in {date_folder}")

if __name__ == "__main__":
    main()

