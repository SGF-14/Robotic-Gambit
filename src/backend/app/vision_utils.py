import cv2
import numpy as np
import json
from cairosvg import svg2png
import chess

# Load square points data
with open('app/sqdict.json', 'r') as fp:
    sq_points = json.load(fp)

def setup_camera():
    global cap
    if 'cap' in globals():
        if cap.isOpened():
            cap.release()  # Make sure to release any previously opened resources
    cap = cv2.VideoCapture(1)
    return cap

def release_resources():
    global cap
    if cap and cap.isOpened():
        cap.release()
        print("Camera resources released successfully.")

def find_square(x: float, y: float):
    for square in sq_points:
        points = np.array(sq_points[square], np.int32)
        if cv2.pointPolygonTest(points, (x, y), False) > 0:
            return square
    return None

def draw_outlines(sq_points: dict, frame, show_text=False):
    for square in sq_points:
        points = np.array(sq_points[square], np.int32)
        cv2.polylines(frame, [points], True, (0, 255, 0), thickness=2)
        if show_text:
            x, y, _, _ = cv2.boundingRect(points)
            cv2.putText(frame, square, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def show_board(board: chess.Board, size=900):
    svgwrap = chess.svg.board(board, size=size)
    svg2png(svgwrap, write_to='output.png')
    cv2.imshow('Game', cv2.imread('output.png'))
