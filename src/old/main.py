import cv2
import numpy as np
import json
import chess
import chess.pgn
import chess.svg
from cairosvg import svg2png
# Flask API VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading




# connect firebase vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
import firebase_admin
from firebase_admin import credentials,initialize_app,db 

cred = credentials.Certificate("robotic-gambit-firebase-adminsdk-qoeq8-b21de07f35.json")

app = initialize_app(cred,{
    'databaseURL' : 'https://robotic-gambit-default-rtdb.europe-west1.firebasedatabase.app/'
})


ref = db.reference("/records/")
with open("./data.json","r") as f:
    data=json.load(f)

ref.set(data)
print("new db updated")

# firebase_admin.initialize_app(cred)
# end of Firebase connection ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# sqdict file 
with open('sqdict.json', 'r') as fp:
    sq_points = json.load(fp)


def find_square(x: float, y: float):
    for square in sq_points:
        points = np.array(sq_points[square], np.int32)
        if cv2.pointPolygonTest(points, (x, y), False) > 0:
            return square
    return None

def draw_outlines(sq_points: dict, frame, show_text=False) -> None:
    for square in sq_points:
        points = sq_points[square]
        points = np.array(points, dtype=np.int32)
        cv2.polylines(frame, [points], True, (0, 255, 0), thickness=2)
        if show_text:
            x, y, _, _ = cv2.boundingRect(points)
            cv2.putText(frame, square, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

def show_board(board: chess.Board, size=900) -> None:
    svgwrap = chess.svg.board(board, size=size)
    svg2png(svgwrap, write_to='output.png')
    cv2.imshow('Game', cv2.imread('output.png'))

# START MATCH
def start_chess_match(username):


    print("Test")
    print(f"Starting match for user: {username}")

    cap = cv2.VideoCapture(1)  
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
    cap.release()



app = Flask(__name__)
CORS(app)

@app.route('/start_match', methods=['POST'])
def start_match():
    print("flask test")
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'No username provided'}), 400
    try:
        threading.Thread(target=start_chess_match, args=(username,)).start()
        return jsonify({'message': f'Match started for {username}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# start_chess_match("username")
# Close all windows
# cv2.destroyAllWindows()
