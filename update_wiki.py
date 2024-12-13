import csv
import requests
import os
import subprocess

import pandas as pd
hi = 4
# Create the DataFrame
runners_df = pd.DataFrame({
    "No. of jobs running during the duration": [hi],
    "Average Execution Time": [hi],
    "Average Queue Time": [hi],
    "Number of Failed Jobs": [hi]
})

# Save to CSV
csv_file_path = "runners.csv"
runners_df.to_csv(csv_file_path, index=False)

# Convert to Markdown
def csv_to_markdown(input_csv, output_md):
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Convert DataFrame to Markdown format
    markdown = df.to_markdown(index=False)

    # Save to .md file
    with open(output_md, 'w') as md_file:
        md_file.write(markdown)

    print(f"Markdown table has been saved to {output_md}")

def publish_to_github_wiki(wiki_repo_url, md_file_path, commit_message="Update Wiki"):
    # Clone the wiki repository
    clone_dir = "temp_wiki_repo"
    if not os.path.exists(clone_dir):
        print("Cloning the Wiki repository...")
        subprocess.run(["git", "clone", wiki_repo_url, clone_dir], check=True)
    else:
        print("Wiki repository already exists. Pulling the latest changes...")
        subprocess.run(["git", "-C", clone_dir, "pull"], check=True)

    # Copy the .md file into the wiki directory
    print("Copying the .md file to the Wiki repository...")
    destination_path = os.path.join(clone_dir, os.path.basename(md_file_path))
    subprocess.run(["cp", md_file_path, destination_path], check=True)

    # Commit and push the changes
    print("Committing and pushing the changes...")
    subprocess.run(["git", "-C", clone_dir, "add", "."], check=True)
    subprocess.run(["git", "-C", clone_dir, "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "-C", clone_dir, "push"], check=True)

    # Cleanup (optional)
    print("Cleaning up temporary files...")
    subprocess.run(["rm", "-rf", clone_dir], check=True)

    print("Wiki updated successfully!")


# Example usage
markdown_file_path = "runners.md"
csv_to_markdown(csv_file_path, markdown_file_path)

wiki_repo_url = "https://github.com/Geethaa19/Hello-World.wiki.git"  # Replace with your Wiki repo URL
md_file_path = "runners.md"  # Path to your .md file
publish_to_github_wiki(wiki_repo_url, md_file_path)

