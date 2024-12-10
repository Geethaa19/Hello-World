import os
from git import Repo

# GitHub Wiki repository details
pat = input("enter: ")
GITHUB_WIKI_URL = "https://"+pat+"@github.com/abcde/Hello-World.wiki.git"  # Replace with your details
REPO_DIR = "Hello-World.wiki"  # Directory where the repository will be cloned
CSV_FILE_NAME = "data.csv"  # Name of the CSV file to add

def ensure_repo_cloned(repo_url, repo_dir):
    """
    Clone the repository if it doesn't exist, or pull updates if it does.
    """
    if not os.path.exists(repo_dir):
        print(f"Cloning repository from {repo_url}...")
        Repo.clone_from(repo_url, repo_dir)
    else:
        print(f"Repository already exists. Pulling latest changes...")
        repo = Repo(repo_dir)
        origin = repo.remote(name="origin")
        origin.pull()

def create_csv_file(file_name):
    """
    Create a simple CSV file.
    """
    print(f"Creating CSV file: {file_name}")
    with open(file_name, "w") as f:
        f.write("Name,Age,Location\nJohn,25,USA\nAlice,30,Canada\n")

def add_commit_push(repo_dir, file_name):
    """
    Add the CSV file to the repo, commit, and push changes.
    """
    print(f"Adding {file_name} to the repository...")
    repo = Repo(repo_dir)
    # Copy CSV file to the repository directory
    os.system(f"cp {file_name} {repo_dir}")
    repo.git.add(A=True)
    repo.index.commit("Add CSV file to Wiki")
    print("Pushing changes to remote...")
    origin = repo.remote(name="origin")
    origin.push()

def main():
    # Ensure the repository is cloned or updated
    ensure_repo_cloned(GITHUB_WIKI_URL, REPO_DIR)
    # Create the CSV file
    create_csv_file(CSV_FILE_NAME)
    # Add, commit, and push the CSV file to the Wiki repository
    add_commit_push(REPO_DIR, CSV_FILE_NAME)
    print("CSV file successfully published to the Wiki!")

if __name__ == "__main__":
    main()
