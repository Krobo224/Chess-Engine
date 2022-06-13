
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
        self.whiteToMove = True # true means there is chance of white to play. False means there is black's chance
        self.moveLog = [] # maintains history of the moves made
    
    # the below method to make move
    # Note: This will not work for castling, en-passant, pawn capturing techniques    
    def makeMove(self, move):
        self.board[move.startRow][move.startColumn] = '--'
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move) # updating the history of moves
        self.whiteToMove = not self.whiteToMove # swapping the players (for alternate chances)
        
    #undo functionality
    def undoFunc(self):
        if len(self.moveLog) != 0:
            temp_obj = self.moveLog.pop() # returns the last element as well as deleted it.
            self.board[temp_obj.startRow][temp_obj.startColumn] = temp_obj.pieceMoved
            self.board[temp_obj.endRow][temp_obj.endColumn] = temp_obj.pieceCaptured
            self.whiteToMove = not self.whiteToMove
class moveClass:
    # below 4 variables are used for rank-file notation
    rankstoRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6": 2, "7": 1, "8":0}
    rowstoRanks = {v : k for k, v in rankstoRows.items()}
    
    filestoColumns = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    columnstoFiles = {v : k for k, v in filestoColumns.items()}
    
    #Constructor
    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startColumn = startSquare[1]
        
        self.endRow = endSquare[0]
        self.endColumn = endSquare[1]
        
        self.pieceMoved = board[self.startRow][self.startColumn] # Piece on the current board state at the where the user clicked first
        self.pieceCaptured = board[self.endRow][self.endColumn] # Piece on the current board states at the place where user wants to move the selected piece
        
        # To get real chess notations (i.e every square in real chess is denoted as a4: file-rank)
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startColumn) + self.getRankFile(self.endRow, self.endColumn)
        
    def getRankFile(self, r, c):
        return self.columnstoFiles[c] + self.rowstoRanks[r]