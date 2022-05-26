
import numpy as np

class GameState:
    # chess board defined of 8x8
    # b = black and w = white
    # bR = black Rook
    # bN = black Knight
    # bB = black Bishop
    # bQ = black queen
    # bK = black king
    # bp = black Pawn

    def __init__(self):
        self.board = np.array([["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                               ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                               ["--", "--", "--", "--", "--", "--", "--", "--"],
                               ["--", "--", "--", "--", "--", "--", "--", "--"],
                               ["--", "--", "--", "--", "--", "--", "--", "--"],
                               ["--", "--", "--", "--", "--", "--", "--", "--"],
                               ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                               ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
                               ])
        self.whiteToMove = True
        self.moveLog = []
        
    
