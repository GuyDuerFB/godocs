import os
import base64
import json
import requests
from git import Repo

# Configuration
SOURCE_REPO_URL = 'https://github.com/GuyDuerFB/godocs.git'  # URL of the source repository
DOCS_DIR = 'docs'  # Path to the docs directory in the source repository
TARGET_REPO = 'firebolt-analytics/gen_ai_repo'  # Target repository
TARGET_FILE_PATH = 'all_docs.txt'  # Path to all_docs.txt in the target repository, placed at the root
TEMP_CLONE_DIR = '/tmp/source_repo_clone'
GITHUB_TOKEN = os.getenv('GENERAL_TOKEN')  # Using the GENERAL_TOKEN environment variable for authentication
COMMIT_MESSAGE = 'Update all_docs.txt with the latest documentation'

def clone_source_repo():
    """Clones the source repository."""
    if os.path.exists(TEMP_CLONE_DIR):
        os.system(f'rm -rf {TEMP_CLONE_DIR}')
    Repo.clone_from(SOURCE_REPO_URL, TEMP_CLONE_DIR)

def aggregate_docs_content():
    """Aggregates the content of all Markdown files from the docs directory and its subdirectories."""
    aggregated_content = ""
    docs_path = os.path.join(TEMP_CLONE_DIR, DOCS_DIR)
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    aggregated_content += md_file.read() + "\n\n"
    return aggregated_content

def update_target_file(content):
    """Updates the target file in the target repository with the given content."""
    url = f'https://api.github.com/repos/{TARGET_REPO}/contents/{TARGET_FILE_PATH}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    
    # Try to get the file to retrieve its SHA (if it exists)
    response = requests.get(url, headers=headers)
    sha = response.json().get('sha') if response.status_code == 200 else None

    data = {
        'message': COMMIT_MESSAGE,
        'content': base64.b64encode(content.encode()).decode(),
        'branch': 'main',  # Adjust the branch if necessary
    }
    if sha:
        data['sha'] = sha  # Include the SHA in the request to update the file

    # Create or update the file
    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code in [200, 201]:
        print("Successfully updated the documentation.")
    else:
        print(f"Failed to update the documentation. Status code: {response.status_code}, Response: {response.text}")

def main():
    """Main function to clone the source repo, aggregate docs content, and update the target file."""
    clone_source_repo()
    new_content = aggregate_docs_content()
    update_target_file(new_content)

if __name__ == "__main__":
    main()
