import csv
import requests

# Replace with your repository, token, and base URL
GITHUB_USERNAME = "Geethaa19"
REPOSITORY_NAME = "Hello-World"
TOKEN = input("Enter token")
BASE_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPOSITORY_NAME}/wiki"

def update_wiki_page(title, content):
    url = f"{BASE_URL}/{title.replace(' ', '-')}"  # URL for the wiki page
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "message": f"Updated {title} page",
        "content": content,
    }
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        print(f"Successfully updated page: {title}")
    else:
        print(f"Failed to update page: {title}. Response: {response.text}")

def main():
    csv_file = "example.csv"  # Your CSV file path

    with open(csv_file, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["Title"]
            content = row["Content"]
            update_wiki_page(title, content)

if __name__ == "__main__":
    main()
