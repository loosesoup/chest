import numpy as np
import pygame
import sys
import csv

BLUE = (0,0,200)
WHITE = (230,230,230)
BLACK = (0,0,0)
RED = (200,25,25)
YELLOW = (200,200,25)
GREEN = (50,200,25)
PURPLE = (150,10,150)


ROWS = 6
COLS = 7

def create_board():
    #board = [[0] * COLS for _ in range(ROWS)]
    board = np.zeros((ROWS,COLS))
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
    row = r
    col = c
    # diagonal

    # slope = 1
    while inBounds(board,row,col) and board[row][col] == piece:
            row+=1
            col+=1
            cnt+=1
            if cnt == 4: return True

    #reset vars to reiterate 
    row = r
    col = c
    cnt = 0
    # slope = -1
    while inBounds(board,row,col) and board[row][col] == piece:
            row+=1
            col-=1
            cnt+=1
            if cnt == 4: return True
            
    return False
    


def win(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                
                horizontal = dfsh(board,i,j,board[i][j],0)
                vertical = dfsv(board,i,j,board[i][j],0)
                diagonal = dfsd(board,i,j,board[i][j],0)
                
                if horizontal == True or vertical == True or diagonal == True:
                    return True
                
    
                
    return False
                
    # dfs vertical            
    # dfs horizontal
    # dfs diafonal

def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen,BLUE,(c*SS,r*SS+SS,SS,SS))
            pygame.draw.circle(screen,BLACK,(c*SS+SS//2,r*SS+SS+SS//2),RADIUS)


    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                pygame.draw.circle(screen,RED,(c*SS+SS//2,height-(r*SS+SS//2)),RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen,YELLOW,(c*SS+SS//2,height-(r*SS+SS//2)),RADIUS)
    
    pygame.display.update()

p1_moves = []
p2_moves = []
def move_list(p1_moves,p2_moves):
    rows = ['p1_moves', 'p2_moves']
    cols = [p1_moves,p2_moves]
    filename = 'move_list.csv'

    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(rows)
        csvwriter.writerows(cols)

        # filename.close()

    with open('move_list.csv','r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

board = create_board()
print_board(board)
game_over = False

turn = 0

pygame.init()

SS = 75 # pixels

width = COLS * SS
height = (ROWS+1) * SS

size = (width,height)
RADIUS = int(SS//2 - 5)


screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

pygame.font.init()
myfont = pygame.font.SysFont('monospace',38)
c4font = pygame.font.SysFont('ariel',24)

font = pygame.font.SysFont('monospace',1)
C4 = c4font.render('Connect4',1,PURPLE)
C41 = c4font.render('Player 1 ...',1,RED)
C42 = c4font.render('Player 2 ...',1,YELLOW)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SS))
            posx = event.pos[0]
            if turn % 2 == 0:
                pygame.draw.circle(screen,RED,(posx,SS//2),RADIUS-10)
                #screen.blit(C41,(600,10))
            else:
                pygame.draw.circle(screen,YELLOW,(posx,SS//2),RADIUS-10)
                #screen.blit(C42,(600,10))
            screen.blit(C4,(20,10))
        
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
    
            # player 1 turn
            if turn % 2 == 0:
                posx = event.pos[0]
                col = posx//SS
                p1_moves.append(col)
                
                if valid_selection(board,col):
                    row = next_open_row(board,col)
                    drop_piece(board,row,col,1)

            else:
                posx = event.pos[0]
                col = posx//SS
                p2_moves.append(col)

                if valid_selection(board,col):
                    row = next_open_row(board,col)
                    drop_piece(board,row,col,2)
            print_board(board)
            draw_board(board)

            game_over = win(board)

            if game_over:

                move_list(p1_moves,p2_moves) # gives shows of each players moves saved as move_list.csv in same directory

                # congrats = "Congrats Player" +str(((turn-1)%2) + 1)+ " !!!"
                # label = myfont.render(congrats,1,GREEN)
                # screen.blit(label,(40,10))
            turn += 1
pygame.draw.rect(screen,BLACK,(0,0,width,SS))

while True:
    #screen.blit(label,(20,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    congrats = "Congrats Player" +str(((turn-1)%2) + 1)+ " !!!"
    label = myfont.render(congrats,1,GREEN)
    screen.blit(label,(40,10))

    pygame.display.update()
