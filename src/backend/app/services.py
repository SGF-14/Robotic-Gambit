import cv2
import numpy as np
import json
import chess
import chess.pgn
import chess.svg
from cairosvg import svg2png
from .vision_utils import setup_camera, release_resources, find_square, draw_outlines, show_board

import firebase_admin
from firebase_admin import credentials, db, exceptions

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:

    cred = credentials.Certificate('app/robotic-gambit-firebase-adminsdk-qoeq8-0e937ad0f9.json')

    firebase_admin.initialize_app(cred, {

        'databaseURL': 'https://robotic-gambit-default-rtdb.europe-west1.firebasedatabase.app/'

    })

# Reference to chess matches in Firebase
chess_matches_ref = db.reference('chess_matches')

def can_start_new_match():
    try:
        active_match = chess_matches_ref.order_by_child('status').equal_to('active').get()
        return not bool(active_match)  # True if no active match exists
    except exceptions.FirebaseError as e:
        print(f"Failed to check active matches: {e}")
        return False  # Assume a match is active if there's a problem checking

def start_chess_match(username):
    if can_start_new_match():
        try:
            new_match = chess_matches_ref.push({
                'username': username,
                'status': 'active'
            })
            print(f"New chess match started for {username}, Match ID: {new_match.key}")
            # Add logic to control the robotic arm here
            setup_camera()
            process_chess_match()  # Handles the chess match logic and OpenCV operations
        except exceptions.FirebaseError as e:
            print(f"Failed to start new match: {e}")
    else:
        print("A match is currently active. Please wait until the current match is completed.")

def complete_chess_match(match_id):
    try:
        match_ref = chess_matches_ref.child(match_id)
        match_ref.update({'status': 'completed'})
        release_resources()
        print(f"Chess match {match_id} completed.")
    except exceptions.FirebaseError as e:
        print(f"Failed to complete the match {match_id}: {e}")

def process_chess_match():
    global cap
    # cap = setup_camera()
    try:
        # cap = cv2.VideoCapture(1)  
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        initial = []
        final = []
        bounding_boxes = []
        centers = []
        highlights = set()

        board = chess.Board()
        show_board(board)
        cv2.waitKey(2)

        while not board.is_game_over():
            ret, frame = cap.read()
            draw_outlines(sq_points, frame)
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('r'):
                if len(initial) == 0:
                    initial = frame
                    print("Your turn")# CAPTURE THE CORRENT STATUS OF THE BOARD
                elif len(final) == 0:
                    print('Enemy  turn !')# CAPTURE THE FINAL  STATUS OF THE BOARD
                    final = frame

                    gray1 = cv2.cvtColor(initial, cv2.COLOR_BGR2GRAY)
                    gray2 = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
                    diff = cv2.absdiff(gray1, gray2)
                    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)




                    diff = cv2.dilate(diff, None, iterations=4)
                    kernel_size = 3
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
                    diff = cv2.erode(diff, kernel, iterations=6)

                    contours, _ = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    sorted_contours_and_areas = sorted(zip(contours, [cv2.contourArea(c) for c in contours]), key=lambda x: x[1], reverse=True)
                    try:
                        contours = [sorted_contours_and_areas[0][0], sorted_contours_and_areas[1][0]]
                        cv2.drawContours(frame, contours, 1, (255, 0, 0), 4)

                        bounding_boxes = [cv2.boundingRect(c) for c in contours]

                        centers = [(x + w // 2, y + h // 2) for (x, y, w, h) in bounding_boxes]
                        highlights = set()
                        for p in centers:
                            highlights.add(find_square(*p))
                        initial = []
                        final = []
                    except:
                        highlights = set()
                        highlights.add('rand')
                        highlights.add('placeholder')
                        initial = []
                        final = []

                    if len(highlights) == 2:
                        try:
                            sq1, sq2 = highlights.pop(), highlights.pop()
                            if board.color_at(chess.parse_square(sq1)) == board.turn:
                                start, end = sq1, sq2
                            else:
                                start, end = sq2, sq1
                            uci = start + end
                            board.push_uci(uci)
                        except:
                            uci = input("Couldn't record proper move. Override: ")
                            board.push_uci(uci)
                        show_board(board)
                        highlights = set()
                        centers = []

            if cv2.waitKey(2) & 0xFF == ord('q'):
                break

            cv2.imshow('Frame', frame)

            show_board(board)
    finally:
        if cap:
            cap.release()
            print("Camera released")
        # cap.release()