import os
import requests

# GitHub Personal Access Token (stored securely as environment variable)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = os.getenv("GITHUB_USER")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Basic GitHub API wrapper for repository management
def list_repositories():
    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=HEADERS)
    repos = response.json()
    return [repo['name'] for repo in repos]

def create_issue(repo_name, title, body):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/issues"
    issue_data = {"title": title, "body": body}
    response = requests.post(url, headers=HEADERS, json=issue_data)
    return response.json()

# Main workflow automation example
if __name__ == "__main__":
    print("Listing Repositories:")
    repositories = list_repositories()
    for repo in repositories:
        print(repo)

    # Example: create an automated notification issue
    print("\nCreating automated issue in active repository...")
    if repositories:
        auto_repo = repositories[0]
        create_issue(auto_repo, "Automated Task Notification", "Workflow triggered successfully from Termux agent.")
