# match.py
from flask import make_response, jsonify
import cv2
import numpy as np
import json
import chess
import chess.pgn
import chess.svg
from cairosvg import svg2png

from .FrameManagement import get_initial_frame, capture_frame, release_resources

# impport Computer Vision utils
from .ComputerVision import setup_camera, find_square, draw_outlines, show_board, get_square_points, detect_move, capture_initial_frame
# import AI
from .MachineLearning import make_ai_move

# import Firebase 
import firebase_admin
from firebase_admin import db, exceptions

# import ChessBoard
from .ChessBoard import get_board, reset_board, get_board_png

from .database_config import initialize_firebase_app



if not firebase_admin._apps:
    initialize_firebase_app()
            
board = get_board

def get_database_reference():
    
    return db.reference('some_reference')


def some_database_interaction():
    ref = get_database_reference()
    


chess_matches_ref = db.reference('chess_matches')

def initialize_matches():
    active_matches = chess_matches_ref.order_by_child('status').equal_to('active').get()
    for match_id, match in active_matches.items():
        if match and 'status' in match and match['status'] == 'active':
            print(f"Setting match {match_id} to completed.")
            chess_matches_ref.child(match_id).update({'status': 'completed'})

def can_start_new_match():
    try:
        active_match = chess_matches_ref.order_by_child('status').equal_to('active').get()
        return not bool(active_match)  
    except exceptions.FirebaseError as e:
        print(f"Failed to check active matches: {e}")
        return False  

def start_chess_match(username):
    if can_start_new_match():
        try:
            new_match = chess_matches_ref.push({
                'username': username,
                'status': 'active'
            })
            print(f"New chess match started for {username}, Match ID: {new_match.key}")
            
            board = chess.Board()
            reset_board()
            make_ai_move()
            if setup_camera() is None:
                print("Camera setup failed. Camera features will not be available.")

            # TEMP COMMENT THIS v
            # setup_camera()
            # process_chess_match()
            return "Match Started"
        except exceptions.FirebaseError as e:
            print(f"Failed to start new match: {e}")
            return f"Failed to start new match: {e}"
    else:
        print("A match is currently active. Please wait until the current match is completed.")
        return "A match is currently active. Please wait."


def end_turn():
    global board
    try:
        initial_frame = get_initial_frame()  
        if initial_frame is None:
            print("Initial frame is not set, cannot proceed with ending turn.")
            return None, "Initial frame is not set."

        final_frame = capture_frame()
        if final_frame is None:
            print("Final Frame is None")
            return None, "Final frame capture failed"

        print("Initial Frame Captured:", initial_frame)
        print("Final Frame Captured:", final_frame)
        
        user_move = detect_move(initial_frame, final_frame)
        print("Detected Move:", user_move)

        if user_move and board.is_legal(chess.Move.from_uci(user_move)):
            board.push_uci(user_move)
            check_game_status()
            if not game_over:
                make_ai_move()
            return "Turn processed successfully", None
        else:
            return None, 'Invalid or illegal move'
    except Exception as e:
        print(f"Error in end_turn: {str(e)}")
        return None, f'Error processing move: {str(e)}'



def complete_chess_match(match_id):
    try:
        initialize_matches()
        match_ref = chess_matches_ref.child(match_id)
        match_ref.update({'status': 'completed'})
        release_resources()
        print(f"Chess match {match_id} completed.")
        return "Match completed"
    except exceptions.FirebaseError as e:
        print(f"Failed to complete the match {match_id}: {e}")
        return f"Failed to complete the match: {e}"

def check_game_status():
    if board.is_checkmate():
        print("Checkmate detected.")
    elif board.is_stalemate():
        print("Stalemate detected.")