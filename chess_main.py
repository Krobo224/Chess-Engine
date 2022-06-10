import pygame as p
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION  #this is division which adjust it to a whole number to left on a number line (eg if value obtained after div is 3.5 it will return/assign 3)
MAX_FPS = 15 #frame rate (Images to be drawn per second)
IMAGES = {}  #dictionary to store the image where key: piece_name; value = image_path

'''
Initializing a global dictionary of images
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        
        #Now images can be accessed by just saying IMAGES['wp']
        
def main():
    p.init() #initializes pygame library
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white")) #background color
    gs = chess_engine.GameState() #object created of class GameState
    loadImages()
    running = True
    squareSelected = () # a tuple containing a value for the last mouse position
    playerClicks = [] # list of two tuples containing the two mouse click positions e.g. [(6,4), (4,4)]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        elif e.type == p.MOUSEBUTTONDOWN:
            location = p.mouse.get_pos() # will get (x,y) position of mouse
            col = location[0] // SQ_SIZE
            row = location[1] // SQ_SIZE
            if squareSelected == (row, col): # this is when the player selects the same square again
                squareSelected = () # deselcts the square
                playerClicks = [] # click player clicks
            else:
                squareSelected = (row, col)
                playerClicks.append(squareSelected) #appends for both 1st and 2nd click
            
            if len(playerClicks) == 2: # after 2nd click
                
                
            
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
  

      
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
    
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
if __name__ == '__main__':
    main()