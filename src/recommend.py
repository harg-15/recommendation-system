def fymk(data, user_id):
    user_id_to_name = {user['id']: user['name'] for user in data['users']}
    user_friend = {user['id']: set(user.get('friends', [])) for user in data['users']}

    if user_id not in user_friend:
        return []

    direct_friends = user_friend[user_id]
    suggestions = {}

    for friend in direct_friends:
        for mutual in user_friend.get(friend, []):
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    sorted_suggestion = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [user_id_to_name[suggested_id] for suggested_id, _ in sorted_suggestion if suggested_id in user_id_to_name]

def pymk(data, user_id):
    page_id_to_name = {page['id']: page['name'] for page in data['pages']}
    user_page = {user['id']: set(user.get('liked_pages', [])) for user in data['users']}

    if user_id not in user_page:
        return []

    direct_pages = user_page[user_id]
    suggestions = {}

    for other_user, pages in user_page.items():
        if other_user != user_id:
            common_pages = direct_pages.intersection(pages)
            for page in pages:
                if page not in direct_pages:
                    suggestions[page] = suggestions.get(page, 0) + len(common_pages)

    sorted_suggestion = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    return [page_id_to_name[page_id] for page_id, _ in sorted_suggestion if page_id in page_id_to_name]

def print_all_users_info(data):
    user_id_to_name = {user['id']: user['name'] for user in data['users']}
    page_id_to_name = {page['id']: page['name'] for page in data['pages']}

    for user in data['users']:
        friend_names = [user_id_to_name[fid] for fid in user.get('friends', []) if fid in user_id_to_name]
        page_names = [page_id_to_name[pid] for pid in user.get('liked_pages', []) if pid in page_id_to_name]
        friends_str = ", ".join(friend_names) if friend_names else "no one"
        pages_str = ", ".join(page_names) if page_names else "no pages"
        print(f"{user['id']}: {user['name']} is friends with {friends_str} and likes the pages {pages_str}")

def print_recommendations_for_all(data):
    for user in data['users']:
        user_id = user['id']
        user_name = user['name']

        friend_suggestions = fymk(data, user_id)
        page_suggestions = pymk(data, user_id)

        print(f"Friend suggestions for {user_name} (ID: {user_id}): {friend_suggestions if friend_suggestions else 'No suggestions'}")
        print(f"Page suggestions for {user_name} (ID: {user_id}): {page_suggestions if page_suggestions else 'No suggestions'}")
        print("-" * 60)
