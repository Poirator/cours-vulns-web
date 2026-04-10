import requests
import os

# Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # À définir dans tes variables d'environnement
REPO_OWNER = 'ton-org-ou-utilisateur'    # Remplace par ton organisation ou utilisateur
REPO_NAME = 'ton-depot'                   # Remplace par le nom de ton dépôt

def get_codeql_alerts():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/code-scanning/alerts"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des alertes CodeQL: {response.status_code}")
        return []

def get_dependabot_alerts():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/dependabot/alerts"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des alertes Dependabot: {response.status_code}")
        return []

def main():
    print("Récupération des alertes CodeQL...")
    codeql_alerts = get_codeql_alerts()
    print(f"Nombre d'alertes CodeQL: {len(codeql_alerts)}")
    for alert in codeql_alerts:
        print(f"- {alert['rule']['id']}: {alert['rule']['description']} (fichier: {alert['most_recent_instance']['location']['path']})")

    print("\nRécupération des alertes Dependabot...")
    dependabot_alerts = get_dependabot_alerts()
    print(f"Nombre d'alertes Dependabot: {len(dependabot_alerts)}")
    for alert in dependabot_alerts:
        print(f"- {alert['dependency']['package']['name']}@{alert['dependency']['version']}: {alert['security_vulnerability']['advisory']['summary']}")

if __name__ == "__main__":
    main()
