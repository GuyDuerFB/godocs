import os
import base64
import json
import requests
import re
from git import Repo
from bs4 import BeautifulSoup

# Configuration
SOURCE_REPO_URL = 'https://github.com/GuyDuerFB/godocs.git'  # Adjust with your source repository's URL
DOCS_DIR = 'docs'  # The directory within the source repo containing Markdown files
TARGET_REPO = 'firebolt-analytics/gen_ai_repo'  # Your target repository
TARGET_FILE_PATH = 'all_docs.txt'  # Target file path in the target repository, here assumed to be at the root
TEMP_CLONE_DIR = '/tmp/source_repo_clone'  # Temporary directory for cloning the source repository
GITHUB_TOKEN = os.getenv('GENERAL_TOKEN')  # Assumes the GENERAL_TOKEN environment variable is set with your GitHub PAT
COMMIT_MESSAGE = 'Update all_docs.txt with the latest documentation'

def clone_source_repo():
    """Clones the source repository."""
    if os.path.exists(TEMP_CLONE_DIR):
        os.system(f'rm -rf {TEMP_CLONE_DIR}')
    Repo.clone_from(SOURCE_REPO_URL, TEMP_CLONE_DIR, branch='gh-pages')  # Adjust the branch if needed

def clean_content(content):
    """Removes HTML tags, URLs, and Markdown headers from content."""
    soup = BeautifulSoup(content, 'lxml')  # Use 'html.parser' as an alternative
    text = soup.get_text(separator=' ', strip=True)  # Extract clean text from HTML
    text_no_urls = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
    text_no_md_headers = re.sub(r'\n#+\s?', '\n', text_no_urls)  # Remove Markdown headers
    return text_no_md_headers

def aggregate_docs_content():
    """Aggregates cleaned content of all Markdown files within the specified docs directory."""
    aggregated_content = ""
    docs_path = os.path.join(TEMP_CLONE_DIR, DOCS_DIR)
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    file_content = md_file.read()
                    cleaned_content = clean_content(file_content)
                    aggregated_content += cleaned_content.strip() + "\n"  # Ensure minimal whitespace with a single newline
    return aggregated_content

def update_target_file(content):
    """Creates or updates the target file in the target repository with the aggregated content."""
    url = f'https://api.github.com/repos/{TARGET_REPO}/contents/{TARGET_FILE_PATH}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    get_response = requests.get(url, headers=headers)
    sha = get_response.json().get('sha') if get_response.status_code == 200 else None
    data = {
        'message': COMMIT_MESSAGE,
        'content': base64.b64encode(content.encode()).decode(),
        'branch': 'main',
    }
    if sha:
        data['sha'] = sha  # Include SHA for updates

    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code in [200, 201]:
        print("Successfully updated the documentation.")
    else:
        print(f"Failed to update the documentation. Status code: {response.status_code}, Response: {response.text}")

def main():
    """Main function to execute the defined steps for updating the target file."""
    clone_source_repo()
    new_content = aggregate_docs_content()
    update_target_file(new_content)

if __name__ == "__main__":
    main()
