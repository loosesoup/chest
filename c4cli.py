import numpy as np

ROWS = 7
COLS = 6

def create_board():
    #board = [[0] * COLS for _ in range(ROWS)]
    board = np.zeros((COLS,ROWS))
    return board

def valid_selection(board,col):
     return board[5][col] == 0 # valid selection

def next_open_row(board,col):
    # gets the row the piece falls on
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def print_board(board):
    print(np.flip(board,0))

def inBounds(board,r,c):
    n,m = len(board), len(board[0])
    return 0 <= r < n and 0 <= c < m

def dfsv(board,r,c,piece,cnt):

    while inBounds(board,r,c) and board[r][c] == piece:
            r+=1
            cnt+=1
            if cnt == 4: return True
            # vertital
    return False
    
    
def dfsh(board,r,c,piece,cnt):
    
    while inBounds(board,r,c) and board[r][c] == piece:
            c+=1
            cnt+=1
            if cnt == 4: return True
    return False
     # horizontal
    

def dfsd(board,r,c,piece,cnt):
    
    while inBounds(board,r,c) and board[r][c] == piece:
            r+=1
            c+=1
            cnt+=1
            if cnt == 4: return True
            # diagonal
    return False

def win(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 or board[i][j] == 2:
                
                horizontal = dfsh(board,i,j+1,board[i][j],1)
                vertical = dfsv(board,i+1,j,board[i][j],1)
                diagonal = dfsd(board,i+1,j+1,board[i][j],1)
                
                if horizontal == True or vertical == True or diagonal == True:
                    return True
            
                
    return False
                
    # dfs vertical            
    # dfs horizontal
    # dfs diafonal


board = create_board()
print_board(board)
game_over = False

turn = 0

while not game_over:
    # player 1 turn
    if turn % 2 == 0:
        col = int(input('Player 1! Please make your selection (0-6).'))
        if valid_selection(board,col):
            row = next_open_row(board,col)
            drop_piece(board,row,col,1)

    else:
        col = int(input('Player 2! Please make your selection (0-6).'))
        if valid_selection(board,col):
            row = next_open_row(board,col)
            drop_piece(board,row,col,2)
    print_board(board)
    game_over = win(board)
    
    turn +=1
print("Congrats Player" +str(((turn-1)%2) + 1)+ " !!!")
