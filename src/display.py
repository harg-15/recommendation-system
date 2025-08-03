def display_user(data):
    user_id_to_name = {user['id']: user['name'] for user in data['users']}
    page_id_to_name = {page['id']: page['name'] for page in data['pages']}

    for user in data['users']:
        friend_names = [user_id_to_name[fid] for fid in user.get('friends', []) if fid in user_id_to_name]
        page_names = [page_id_to_name[pid] for pid in user.get('liked_pages', []) if pid in page_id_to_name]
        friends_str = ", ".join(friend_names) if friend_names else "no one"
        pages_str = ", ".join(page_names) if page_names else "no pages"
        print(f"{user['id']}: {user['name']} is friends with {friends_str} and likes the pages {pages_str}")
