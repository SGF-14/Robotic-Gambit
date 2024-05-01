# ComputerVision.py
import cv2
import numpy as np
import json
from cairosvg import svg2png
import chess


from .FrameManagement import capture_frame, get_initial_frame, get_final_frame




# from .MachineLearning import make_ai_move
# Load square points data
with open('app/sqdict.json', 'r') as fp:
    sq_points = json.load(fp)

cap = None

initial_frame = None

def setup_camera():
    global cap  
    cap = cv2.VideoCapture(1)  
    if not cap.isOpened():
        cap.open(1)  
        if not cap.isOpened():
            print("Cannot open camera")
            return None
    return cap


def capture_frame():
    global cap
    if cap is None or not cap.isOpened():
        print("Camera not initialized or closed.")
        return None
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        return None
    return frame



def release_resources():
    global cap
    if cap and cap.isOpened():
        cap.release()
        print("Camera resources released successfully.")


def draw_outlines(sq_points: dict, frame, show_text=False):
    for square in sq_points:
        points = np.array(sq_points[square], np.int32)
        cv2.polylines(frame, [points], True, (0, 255, 0), thickness=2)
        if show_text:
            x, y, _, _ = cv2.boundingRect(points)
            cv2.putText(frame, square, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def show_board(board: chess.Board, size=900):
    print(board)
    svg_content = chess.svg.board(board=board, size=size)
    css_styles = """<style>
    .square.light { fill: #ebedd1; } /* Light squares */
    .square.dark  { fill: #739453; } /* Dark squares */
    .white.piece { fill: #f8f8f9; stroke: #000; } /* White pieces */
    .black.piece { fill: #5c5856; stroke: #fff; } /* Black pieces */
    </style>"""
    
    insert_position = svg_content.find('>') + 1
    svg_with_css = svg_content[:insert_position] + css_styles + svg_content[insert_position:]
    
    svg2png(bytestring=svg_with_css.encode('utf-8'), write_to='styled_chess_board.png')
    
    frame = cv2.imread('styled_chess_board.png')
    
    cv2.imshow('Game', frame)


def detect_move(initial, final):
    print("Detecting move...")

    # Load square points data
    with open('app/sqdict.json', 'r') as fp:
        sq_points = json.load(fp)

    # Convert images to grayscale
    print("Converting to grayscale...")
    gray_initial = cv2.cvtColor(initial, cv2.COLOR_BGR2GRAY)
    gray_final = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)

    # Compute the difference and apply threshold
    print("Computing difference and applying threshold...")
    diff = cv2.absdiff(gray_initial, gray_final)
    # _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

    # Noise reduction through morphological operations
    print("Applying morphological operations...")
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    thresh = cv2.erode(thresh, kernel, iterations=2)

    # Contour detection
    print("Detecting contours...")
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Detected {len(contours)} contours")

    # Contour analysis
    if len(contours) < 2:
        print("Not enough contours to determine a move.")
        return None

    # Further processing if contours are sufficient
    print("Analyzing contours...")
    moves = []
    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[:2]:
        M = cv2.moments(contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            square = find_square(cx, cy, sq_points)
            if square:
                moves.append(square)

    if len(moves) == 2:
        print(f"Detected move from {moves[0]} to {moves[1]}")
        return moves[0] + moves[1]
    else:
        print("Could not determine both squares.")
        return None





def find_square(x: float, y: float, sq_points):
    for square in sq_points:
        points = np.array(sq_points[square], np.int32)
        if cv2.pointPolygonTest(points, (x, y), False) > 0:
            return square
    return None



def get_contour_center(contour):
    x, y, w, h = cv2.boundingRect(contour)
    return (x + w // 2, y + h // 2)

def order_squares(squares):
    if board.color_at(chess.parse_square(squares[0])) == board.turn:
        return squares[0] + squares[1]
    else:
        return squares[1] + squares[0]

def get_square_points():
    return sq_points

def capture_initial_frame():
    
    global initial_frame
    print("Attempting to capture initial frame")
    initial_frame = capture_frame()
    if initial_frame is None:
        print("Failed to capture initial frame")
    else:
        print("Initial frame captured successfully")


def get_initial_frame():
    global initial_frame
    if initial_frame is None:
        raise Exception("Initial frame is not set.")
    return initial_frame
