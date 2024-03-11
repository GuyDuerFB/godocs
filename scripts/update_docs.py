import os
import base64
import json
import requests
import re
from git import Repo
from bs4 import BeautifulSoup

# Configuration
SOURCE_REPO_URL = 'https://github.com/GuyDuerFB/godocs.git'
DOCS_DIR = 'docs'
TARGET_REPO = 'firebolt-analytics/gen_ai_repo'
TARGET_FILE_PATH = 'all_docs.txt'
TEMP_CLONE_DIR = '/tmp/source_repo_clone'
GITHUB_TOKEN = os.getenv('GENERAL_TOKEN')
COMMIT_MESSAGE = 'Update all_docs.txt with the latest documentation'

def clone_source_repo():
    """Clones the source repository."""
    if os.path.exists(TEMP_CLONE_DIR):
        os.system(f'rm -rf {TEMP_CLONE_DIR}')
    Repo.clone_from(SOURCE_REPO_URL, TEMP_CLONE_DIR, branch='gh-pages')  

def clean_content(content):
    """Remove HTML tags and URLs from content using BeautifulSoup."""
    # Use BeautifulSoup to remove HTML tags
    soup = BeautifulSoup(content, 'lxml')  # or 'html.parser'
    text = soup.get_text(separator=' ', strip=True)
    # Remove URLs
    text_no_urls = re.sub(r'http[s]?://\S+', '', text)
    # Remove Markdown headers
    text_no_md_headers = re.sub(r'#+\s?', '', text_no_urls)
    
    return text_no_md_headers

def aggregate_docs_content():
    """Aggregates and cleans the content of all Markdown files."""
    aggregated_content = ""
    docs_path = os.path.join(TEMP_CLONE_DIR, DOCS_DIR)
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    file_content = md_file.read()
                    cleaned_content = clean_content(file_content)
                    # Append cleaned content with minimal whitespace
                    aggregated_content += cleaned_content.strip() + "\n"  # One newline for separation
    return aggregated_content

def update_target_file(content):
    """Updates or creates the target file in the target repository with the given content."""
    url = f'https://api.github.com/repos/{TARGET_REPO}/contents/{TARGET_FILE_PATH}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    data = {
        'message': COMMIT_MESSAGE,
        'content': base64.b64encode(content.encode()).decode(),
        'branch': 'main',
    }
    # Try to get the file to retrieve its SHA (if it exists)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data['sha'] = response.json()['sha']
    
    # Make the request to create or update the file
    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code in [200, 201]:
        print("Successfully updated the documentation.")
    else:
        print(f"Failed to update the documentation. Status code: {response.status_code}, Response: {response.text}")

def main():
    clone_source_repo()
    new_content = aggregate_docs_content()
    update_target_file(new_content)

if __name__ == "__main__":
    main()
