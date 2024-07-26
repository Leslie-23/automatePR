import requests

# Replace 'your_token' with your GitHub personal access token
headers = {
    'Authorization': 'token your_token'
}

# Search for open pull requests in a specific repository
repo = "owner/repository-name"
url = f"https://api.github.com/repos/{repo}/pulls"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    pull_requests = response.json()
    for pr in pull_requests:
        print(f"PR #{pr['number']}: {pr['title']} - {pr['html_url']}")
else:
    print("Failed to fetch pull requests")
