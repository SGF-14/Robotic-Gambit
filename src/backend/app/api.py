# api.py
from flask import Blueprint, request, jsonify
from .match import start_chess_match

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/start_match', methods=['POST'])
def start_match():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    try:
        result = start_chess_match(username)  # Ensure this function returns some status
        if result == "Match Started":
            return jsonify({'message': 'Match started successfully'}), 200
        else:
            return jsonify({'error': 'A match is currently active. Please wait.'}), 403  # or another appropriate status code
    except Exception as e:
        return jsonify({'error': str(e)}), 500