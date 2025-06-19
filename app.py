from flask import Flask, request, jsonify
import logging
import sys

# Configure Flask app
app = Flask(__name__)

# Set up logging to stdout for Azure capture
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(logging.INFO)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

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
