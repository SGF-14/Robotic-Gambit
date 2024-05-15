# ChessBoard.py
import chess
import chess.svg
import cairosvg
import io
from firebase_admin import db

board = chess.Board()

def get_board():
    global board
    return board

def reset_board():
    global board
    board.reset()

def get_board_png(board: chess.Board, size=900):
    print(board)
    svg_content = chess.svg.board(board=board,orientation=chess.BLACK, size=size)
    css_styles = """<style>
    .square.light { fill: #ebedd1; } 
    .square.dark  { fill: #739453; } 
    .white.piece { fill: #f8f8f9; stroke: #000; } 
    .black.piece { fill: #5c5856; stroke: #fff; } 
    </style>"""
    
    insert_position = svg_content.find('>') + 1
    svg_with_css = svg_content[:insert_position] + css_styles + svg_content[insert_position:]

    png_bytes = cairosvg.svg2png(bytestring=svg_content.encode('utf-8'))
    return png_bytes
    # svg2png(bytestring=svg_with_css.encode('utf-8'), write_to='styled_chess_board.png')

def update_fen_in_database():
    fen = board.fen()
    ref = db.reference('chess_matches/currentGame')  
    ref.update({'fen': fen})
    print("Updated FEN in database:", fen)
