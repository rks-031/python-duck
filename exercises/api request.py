import requests
import json
response = requests.get("https://api.github.com/users/rks-031/repos")

if response.status_code == 200:
    data = response.json()
    for repo in data:
        print(f"Project Name: {repo['name']} \n Project URL: {repo['html_url']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)