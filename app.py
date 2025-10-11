from flask import Flask, request, jsonify
from auth import signup_user, login_user

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    # Expecting JSON like: { "email": "user@example.com", "password": "pass123", "full_name": "Yogesh" }
    result = signup_user(
        data['email'],
        data['password'],
        data.get('full_name', "")
    )
    return jsonify(result), (201 if result["success"] else 400)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Expecting JSON like: { "email": "user@example.com", "password": "pass123" }
    result = login_user(
        data['email'],
        data['password']
    )
    return jsonify(result), (200 if result["success"] else 401)


if __name__ == "__main__":
    app.run(debug=True)
