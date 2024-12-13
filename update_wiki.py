import csv
import requests

import pandas as pd
hi = 2
# Create the DataFrame
runners_df = pd.DataFrame({
    "No. of jobs running during the duration": hi,
    "Average Execution Time": hi,
    "Average Queue Time": hi,
    "Number of Failed Jobs": hi
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

# Example usage
markdown_file_path = "runners.md"
csv_to_markdown(csv_file_path, markdown_file_path)

