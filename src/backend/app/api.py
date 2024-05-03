# api.py
from flask import Blueprint, request, jsonify, send_file, make_response
from .ChessBoard import get_board, get_board_png
from .match import start_chess_match, end_turn, complete_chess_match
from .FrameManagement import capture_initial_frame

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/start_match', methods=['POST'])
def start_match():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    try:
        result = start_chess_match(username)  
        if result == "Match Started":
            return jsonify({'message': 'Match started successfully'}), 200
        else:
            return jsonify({'error': 'A match is currently active. Please wait.'}), 403  
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/end_turn', methods=['POST'])
def end_turn_endpoint():
    _, error = end_turn()
    if error is None:
        return jsonify({'message': 'Turn processed successfully'}), 200
    else:
        return jsonify({'error': error}), 400

@api_blueprint.route('/initial_frame', methods=['POST'])
def initial_frame_endpint():
    try:
        capture_initial_frame()  
        response = {
            'status': 'success',
            'message': 'Initial frame set successfully'
        }
        return jsonify(response), 200

    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(error_response), 500


@api_blueprint.route('/complete_chess_match', methods=['POST'])
def complete_chess_match_endpoint():
    data = request.get_json()
    match_id = data.get('match_id')
    try:
        result = complete_chess_match(match_id)
        if result == "Match completed":
            return jsonify({'status': 'Match completed successfully'}), 200
        else:
            return jsonify({'status': 'Failed to complete the match', 'error': result}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_blueprint.route('/get_board_image', methods=['GET'])
def get_board_image():
    try:
        return send_file('../styled_chess_board.png', mimetype='image/png') 
    except Exception as e:
        return str(e), 500