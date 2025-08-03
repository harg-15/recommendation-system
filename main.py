from src.load import load_data, clean_data
from src.display import display_user
from src.recommend import fymk, pymk

def main():
    # Load and clean data
    data = load_data("data/test.json")
    data = clean_data(data)

    # Display all users info
    print("--- User Data ---")
    display_user(data)

    print("\n--- Friend Suggestions (FYMK) ---")
    for user in data['users']:
        suggestions = fymk(data, user['id'])
        print(f"Friend suggestions for {user['name']} ({user['id']}): {suggestions}")

    print("\n--- Page Suggestions (PYMK) ---")
    for user in data['users']:
        suggestions = pymk(data, user['id'])
        print(f"Page suggestions for {user['name']} ({user['id']}): {suggestions}")

if __name__ == "__main__":
    main()
