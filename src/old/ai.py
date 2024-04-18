import chess

# oop object-oriented programming concept.

class ai:
    def __init__(self):
        
        self.piece_square_table = [
            [-50, -40, -30, -30, -30, -30, -40, -50],
            [-40, -20,   0,   0,   0,   0, -20, -40],
            [-30,   0,  10,  15,  15,  10,   0, -30],
            [-30,   5,  15,  20,  20,  15,   5, -30],
            [-30,   0,  15,  20,  20,  15,   0, -30],
            [-30,   5,  10,  15,  15,  10,   5, -30],
            [-40, -20,   0,   5,   5,   0, -20, -40],
            [-50, -40, -30, -30, -30, -30, -40, -50],
        ]
    

    def eval(self, board):
        score_white = 0
        score_black = 0
        for i in range(8): #ABCDEFGH
            for j in range(8): #12345678
                square_ij = chess.square(i, j)
                piece_ij = board.piece_at(square_ij)
                if piece_ij:
                    value = {'P': 100, 'N': 310, 'B': 320, 'R': 500, 'Q': 900}.get(piece_ij.symbol().upper(), 0)
                    score = value + self.piece_square_table[i][j]
                    if piece_ij.color == chess.WHITE:
                        score_white += score
                    else:
                        score_black += score
        return score_white - score_black


    def alpha_beta(self, board, depth, alpha, beta, maximize):
        if board.is_checkmate():
            return -100000 if board.turn == chess.WHITE else 100000
        if depth == 0:
            return self.eval(board)
        
        if maximize:
            max_eval = -999999
            for move in board.legal_moves:
                board.push(move)
                eval = self.alpha_beta(board, depth-1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = 999999
            for move in board.legal_moves:
                board.push(move)
                eval = self.alpha_beta(board, depth-1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    break
            return min_eval


    def get_next_move(self, depth, board, maximize):
        best_move = None
        best_value = -999999 if maximize else 999999
        for move in board.legal_moves:
            board.push(move)
            value = self.alpha_beta(board, depth - 1, -10000, 10000, not maximize)
            board.pop()
            if (maximize and value > best_value) or (not maximize and value < best_value):
                best_value = value
                best_move = move
        return best_move