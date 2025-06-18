from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='logins.log', level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'secure123':
        app.logger.info(f"Successful login attempt by {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f"Failed login attempt by {username}")
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run()
