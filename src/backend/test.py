import cv2
import chess
from app.ComputerVision import capture_frame, detect_move
from app.MachineLearning import make_ai_move
from app.ChessBoard import get_board, reset_board

def play_chess_game():
    reset_board()
    board = get_board()

    while not board.is_game_over():
        print("Current board state:")
        print(board)

        # AI makes a move
        make_ai_move()
        initial_frame = capture_frame()
        print("AI made a move.")
        print(board)

        # Player's turn
        input("Press Enter when you have made your move...")
        final_frame = capture_frame()
        user_move = detect_move(initial_frame, final_frame)

        if user_move and board.is_legal(chess.Move.from_uci(user_move)):
            board.push_uci(user_move)
            print("Player made a move.")
        else:
            print("Invalid or illegal move. Please try again.")

    print("Game over!")
    print(board.result())

if __name__ == "__main__":
    play_chess_game()