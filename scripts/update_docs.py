import os
import base64
import json
import requests
import re  # Import the regular expressions module
from git import Repo

# Configuration
SOURCE_REPO_URL = 'https://github.com/GuyDuerFB/godocs.git'
DOCS_DIR = 'docs'
TARGET_REPO = 'firebolt-analytics/gen_ai_repo'
TARGET_FILE_PATH = 'all_docs.txt'
TEMP_CLONE_DIR = '/tmp/source_repo_clone'
GITHUB_TOKEN = os.getenv('GENERAL_TOKEN')
COMMIT_MESSAGE = 'Update all_docs.txt with the latest documentation'

def clone_source_repo():
    if os.path.exists(TEMP_CLONE_DIR):
        os.system(f'rm -rf {TEMP_CLONE_DIR}')
    Repo.clone_from(SOURCE_REPO_URL, TEMP_CLONE_DIR)

def clean_content(content):
    """Remove URLs, HTML tags, and special characters from content."""
    # Remove URLs
    content_no_urls = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', content)
    # Remove HTML tags
    content_no_html = re.sub(r'<[^>]+>', '', content_no_urls)
    # Remove special characters, except for basic punctuation and underscores
    content_clean = re.sub(r'[^a-zA-Z0-9\s,._!?-]', '', content_no_html)
    return content_clean

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
                    aggregated_content += cleaned_content + "\n\n"
    return aggregated_content

def update_target_file(content):
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
        data['sha'] = sha
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
