#!/usr/bin/env python3
# sample code chess ai

import chess

class ChessAI:
    def __init__(self, depth):
        self.depth = depth

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in board.legal_moves:
                board.push(move)
                evaluation, _ = self.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.legal_moves:
                board.push(move)
                evaluation, _ = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval, best_move

    def get_best_move(self, board):
        _, best_move = self.minimax(board, self.depth, float('-inf'), float('inf'), True)
        return best_move

    def evaluate_board(self, board):
        # Simple evaluation: material count
        score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                piece_type = piece.piece_type
                piece_color = piece.color
                value = {
                    chess.PAWN: 1,
                    chess.KNIGHT: 3,
                    chess.BISHOP: 3,
                    chess.ROOK: 5,
                    chess.QUEEN: 9,
                    chess.KING: 0  # King's value is handled separately
                }[piece_type]
                if piece_color == chess.WHITE:
                    score += value
                else:
                    score -= value
        return score
    
# import required module
import chess

# create board object
board=chess.Board()

chess_ai = ChessAI(1)
best_move = chess_ai.get_best_move(board)
print(best_move)

# display chess board
print(board)