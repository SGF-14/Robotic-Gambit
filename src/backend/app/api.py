from flask import Blueprint, request, jsonify
from .services import start_chess_match

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/start_match', methods=['POST'])
def start_match():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    try:
        start_chess_match(username)
        return jsonify({'message': f'Match started for {username}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
