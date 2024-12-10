import os
import csv
from git import Repo

# Configuration
pat = input()
GITLAB_WIKI_URL = "https://Geethaa19:"+pat+"@github.com/Hello-World.wiki.git"

CSV_FILE_NAME = "data.csv"  # Name of the CSV file to be generated
WIKI_PAGE_NAME = "Home.md"  # Name of the Wiki page to update
CLONE_DIR = "gitlab_wiki_repo"  # Temporary directory to clone the Wiki repository
COMMIT_MESSAGE = "Automatically publish CSV file to Wiki"

# Generate CSV file
def generate_csv(file_name):
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "San Francisco"],
        ["Charlie", 35, "Chicago"],
    ]
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data[0])  # Write header
        writer.writerows(data[1:])  # Write rows
    print(f"CSV file '{file_name}' created.")

# Clone GitLab Wiki repository
def clone_wiki_repo(url, clone_dir):
    if os.path.exists(clone_dir):
        print(f"Directory '{clone_dir}' already exists. Cleaning up...")
        os.system(f"rm -rf {clone_dir}")
    print(f"Cloning Wiki repository from {url}...")
    Repo.clone_from(url, clone_dir)

# Update Wiki page and commit changes
def update_wiki(csv_file, wiki_page, repo_dir):
    os.chdir(repo_dir)
    # Add CSV file to Wiki repo
    os.system(f"cp ../{csv_file} .")
    # Update or create the Wiki page
    if not os.path.exists(wiki_page):
        with open(wiki_page, "w") as page:
            page.write("# Example Page\n")
    with open(wiki_page, "a") as page:
        page.write(f"\n[Download CSV]({csv_file})\n")
    # Commit and push changes
    repo = Repo(repo_dir)
    repo.git.add(all=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name="origin")
    origin.push()
    print("CSV file and Wiki page updates pushed to GitLab.")

# Main function
def main():
    # Step 1: Generate the CSV file
    generate_csv(CSV_FILE_NAME)

    # Step 2: Clone the GitLab Wiki repository
    clone_wiki_repo(GITLAB_WIKI_URL, CLONE_DIR)

    # Step 3: Update the Wiki page and push changes
    update_wiki(CSV_FILE_NAME, WIKI_PAGE_NAME, CLONE_DIR)

    # Step 4: Cleanup
    os.system(f"rm -rf {CLONE_DIR}")
    print("Process completed successfully.")

if __name__ == "__main__":
    main()
