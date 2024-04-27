# FrameManagement.py
import cv2
import numpy as np
import json

squares = [
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
    'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
    'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'
]


sq_points = {}

cap = None
initial_frame = None

def setup_camera():
    global cap
    cap = cv2.VideoCapture(1)  
    if not cap.isOpened():
        print("Failed to open camera")
        raise Exception("Camera could not be initialized")

def capture_frame():
    """Captures a single frame from the initialized camera."""
    global cap
    if cap is None:
        setup_camera()  
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        return None
    return frame

def release_resources():
    """Releases the camera resources."""
    global cap
    if cap:
        cap.release()
        print("Camera resources released")
        cap = None

def get_initial_frame():
    global initial_frame
    if initial_frame is None:
        raise ValueError("Initial frame is not set.")
    return initial_frame

def capture_initial_frame():
    global initial_frame
    initial_frame = capture_frame()
    if initial_frame is None:
        print("Failed to capture initial frame")

def get_final_frame():
    """Function to capture and return the final frame."""
    return capture_frame()

def Squareupdate():
    global squares, sq_points
    Choise = None
    Choise = input("Do you want to update square corners (recommended if the camera moved)? (y/n) ")
    if Choise == "y":
        
        camera_number = int(input("Enter the camera device input number: "))
        print(" ⌞ ⌝ | Press the 4 corners for each square in the camera\n⚠︎ | left click in the camera to set the corner, Right click in the camera to undo \n⚠︎ | press Q in the camera to quit ")
        
        
        cap = cv2.VideoCapture(camera_number)
        
        
        sq_points.clear()
        
        cv2.namedWindow('Chessboard')
        cv2.setMouseCallback('Chessboard', mouse_callback)
        
        while True:
            ret, frame = cap.read()
            
            for square, points in sq_points.items():
                for point in points:
                    cv2.circle(frame, tuple(point), 1, (0, 255, 0), -1)
            cv2.imshow('Chessboard', frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or len(squares) == 0:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        
        with open('new_sqdict.json', 'w') as f:
            json.dump(sq_points, f, indent=2)
        print("Square coordinates updated!\n    | Loading Robotic Gambit...")
    else:
        print(" | Loading Robotic Gambit...")

def mouse_callback(event, x, y, flags, param):
    global squares, sq_points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(squares) > 0:
            square = squares[0]
            if square not in sq_points:
                sq_points[square] = []
            sq_points[square].append([x, y])
            print(f"Clicked on square {square} at coordinates ({x}, {y})")
            if len(sq_points[square]) == 4:
                squares.pop(0)
                print(f"Captured all coordinates for square {square}")
    elif event == cv2.EVENT_RBUTTONDOWN:
        if len(squares) > 0:
            square = squares[0]
            if square in sq_points and len(sq_points[square]) > 0:
                removed_point = sq_points[square].pop()
                print(f"Removed last coordinate ({removed_point[0]}, {removed_point[1]}) from square {square}")
                if len(sq_points[square]) == 0:
                    del sq_points[square]
                    print(f"Removed all coordinates from square {square}")
