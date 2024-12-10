import os
import csv
import shutil
from git import Repo

# Configuration
GITLAB_WIKI_URL = input("Enter your GitLab Wiki URL (with token embedded): ").strip()
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
    try:
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data[0])  # Write header
            writer.writerows(data[1:])  # Write rows
        print(f"CSV file '{file_name}' created.")
    except Exception as e:
        print(f"Error creating CSV file: {e}")
        raise

# Clone GitLab Wiki repository
def clone_wiki_repo(url, clone_dir):
    try:
        if os.path.exists(clone_dir):
            print(f"Cleaning up existing directory '{clone_dir}'...")
            shutil.rmtree(clone_dir)
        print(f"Cloning Wiki repository from {url}...")
        Repo.clone_from(url, clone_dir)
    except Exception as e:
        print(f"Error cloning repository: {e}")
        raise

# Update Wiki page and commit changes
def update_wiki(csv_file, wiki_page, repo_dir):
    try:
        # Copy CSV file to repository directory
        shutil.copy(csv_file, repo_dir)
        
        # Update or create the Wiki page
        wiki_path = os.path.join(repo_dir, wiki_page)
        if not os.path.exists(wiki_path):
            with open(wiki_path, "w") as page:
                page.write("# Example Page\n")
        
        with open(wiki_path, "a") as page:
            page.write(f"\n[Download CSV]({CSV_FILE_NAME})\n")
        
        # Commit and push changes
        repo = Repo(repo_dir)
        repo.git.add(all=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")
        origin.push()
        print("CSV file and Wiki page updates pushed to GitLab.")
    except Exception as e:
        print(f"Error updating Wiki: {e}")
        raise

# Main function
def main():
    try:
        # Step 1: Generate the CSV file
        generate_csv(CSV_FILE_NAME)

        # Step 2: Clone the GitLab Wiki repository
        clone_wiki_repo(GITLAB_WIKI_URL, CLONE_DIR)

        # Step 3: Update the Wiki page and push changes
        update_wiki(CSV_FILE_NAME, WIKI_PAGE_NAME, CLONE_DIR)
    except Exception as e:
        print(f"Process failed: {e}")
    finally:
        # Step 4: Cleanup
        if os.path.exists(CLONE_DIR):
            shutil.rmtree(CLONE_DIR)
        print("Process completed.")

if __name__ == "__main__":
    main()
