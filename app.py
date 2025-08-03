from flask import Flask, render_template
from src.load import load_data, clean_data
from src.recommend import fymk, pymk

app = Flask(__name__)

# Load and clean data once at startup
data = load_data("data/test.json")
data = clean_data(data)

# Prepare user info for template
users = []
for user in data['users']:
    users.append({
        "id": user["id"],
        "name": user["name"],
        "friends": [u["name"] for u in data['users'] if u["id"] in user.get("friends", [])],
        "pages": [p["name"] for p in data['pages'] if p["id"] in user.get("liked_pages", [])]
    })

# Prepare recommendations for all users
recommendations = {}
for user in data['users']:
    uid = user['id']
    recommendations[uid] = {
        "friends": fymk(data, uid),
        "pages": pymk(data, uid)
    }

@app.route("/")
def index():
    return render_template("index.html", users=users, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
