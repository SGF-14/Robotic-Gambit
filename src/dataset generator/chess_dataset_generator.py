import chess
import chess.engine
import chess.svg

import random
import numpy 

from IPython.display import display, SVG

# ########## Methods ##########
def random_board(max_depth=24):
    board = chess.Board()
    depth = random.randrange(0, max_depth)

    for _ in range(depth):
        all_moves = list(board.legal_moves)
        random_move = random.choice(all_moves)
        board.push(random_move)
        if board.is_game_over():
            break

    return board

def get_score(board, depth):
    with chess.engine.SimpleEngine.popen_uci('stockfish-windows-x86-64-avx2.exe') as engine:
        result = engine.analyse(board, chess.engine.Limit(depth=depth))
        score = result['score'].white()  # Get the score from White's perspective
        
        # Check if the score indicates a checkmate
        if score.is_mate():
            # If it's a checkmate score, handle accordingly
            # You might want to assign a large positive or negative value
            return 100000 if score.mate() > 0 else -100000
        else:
            # If it's a regular centipawn score
            # Use score.cp to get the centipawn value
            return score.cp

squares_index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

# example: h3 -> 17
def square_to_index(square):
    letter = chess.square_name(square)
    return 8 - int(letter[1]), squares_index[letter[0]]

def split_dims(board):
    # this is the 3d matrix
    board3d = numpy.zeros((14, 8, 8), dtype=numpy.int8)

    # here we add the pieces' view on the matrix
    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            idx = numpy.unravel_index(square, (8, 8))
            board3d[piece - 1][7 - idx[0]][idx[1]] = 1
        for square in board.pieces(piece, chess.BLACK):
            idx = numpy.unravel_index(square, (8, 8))
            board3d[piece + 5][7 - idx[0]][idx[1]] = 1
    # add attacks and valid moves too
    # so the network knows what is being attacked
    aux = board.turn
    board.turn = chess.WHITE
    for move in board.legal_moves:
        i, j = square_to_index(move.to_square)
        board3d[13][i][j] = 1

    # Restore the board turn
    board.turn = aux

    return board3d

def generate_dataset(size=50, max_depth=24, score_depth=10):
    positions = []
    scores = []
    
    for _ in range(size):
        
        print(_)
        board = random_board(max_depth=max_depth)
        board_3d = split_dims(board)
        board_score = get_score(board, depth=score_depth)  # Use the renamed function
        
        positions.append(board_3d)
        scores.append(board_score)

    positions = numpy.array(positions, dtype=numpy.int8)
    scores = numpy.array(scores, dtype=numpy.float32)

    # Normalize scores
    scores = scores / abs(scores).max() / 2 + 0.5

    numpy.savez('dataset.npz', positions=positions, scores=scores)

generate_dataset()

# data = numpy.load('dataset.npz')
# print(data.files)


# positions = data['positions']
# scores = data['scores']


# # Print the shapes of the arrays
# print("Positions shape:", positions.shape)
# print("Scores shape:", scores.shape)

# # Sample the first entry in the dataset
# print("First position (flattened):", positions[0].flatten())
# print("First score:", scores[0])
