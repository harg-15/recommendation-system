import json
import os

def load_data(filename):
    # Resolve path relative to the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def clean_data(data):
    # Remove users with empty names
    data['users'] = [user for user in data['users'] if user.get('name', '').strip()]

    # Remove duplicate friends and filter out duplicates by user ID
    unique_users = {}
    for user in data['users']:
        user['friends'] = list(set(user.get('friends', [])))
        user['liked_pages'] = list(set(user.get('liked_pages', [])))  # Deduplicate liked_pages too
        unique_users[user['id']] = user
    data['users'] = list(unique_users.values())

    # Remove inactive users (no friends and no liked pages)
    data['users'] = [
        user for user in data['users']
        if user.get('friends') or user.get('liked_pages')
    ]

    # Remove duplicate pages by ID
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())

    return data
