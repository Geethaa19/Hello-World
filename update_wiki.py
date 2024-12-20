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
csv_file_path1 = "runners1.csv"
csv_file_path2 = "runners2.csv"
csv_file_path3 = "runners3.csv"
csv_file_path4 = "runners4.csv"
runners_df.to_csv(csv_file_path1, index=False)
runners_df.to_csv(csv_file_path2, index=False)
runners_df.to_csv(csv_file_path3, index=False)
runners_df.to_csv(csv_file_path4, index=False)
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
markdown_file_path1 = "runners1.md"
markdown_file_path2 = "runners2.md"
markdown_file_path3 = "runners3.md"
markdown_file_path4 = "runners4.md"
csv_to_markdown(csv_file_path1, markdown_file_path1)
csv_to_markdown(csv_file_path2, markdown_file_path2)
csv_to_markdown(csv_file_path3, markdown_file_path3)
csv_to_markdown(csv_file_path4, markdown_file_path4)

# wiki_repo_url = "https://github.com/Geethaa19/Hello-World.wiki.git"  # Replace with your Wiki repo URL
# publish_to_github_wiki(wiki_repo_url, markdown_file_path1)
# publish_to_github_wiki(wiki_repo_url, markdown_file_path2)
# publish_to_github_wiki(wiki_repo_url, markdown_file_path3)
# publish_to_github_wiki(wiki_repo_url, markdown_file_path4)

