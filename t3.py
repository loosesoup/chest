import pygame
import sys
import numpy as np


pygame.init()
SIZE = 3
pixels = 75
width = SIZE * pixels
height = (SIZE+1) * pixels
font = pygame.font.SysFont('monospace',pixels-10)

colors = {
	'blue' : (0,0,200),
	'white' : (230,230,230),
	'black' : (0,0,0),
	'red' : (200,25,25),
	'yellow' : (200,200,25),
	'green' : (50,200,25)
}



def create_board():
	board = [['0','0','0'] for _ in range(SIZE)]
	return board


def print_board(board):
	for row in board[::-1]:
		print(row)

def valid_selection(board,Z):
	r,c = int(Z[0]) , int(Z[1])
	print(f'row {r} col {c}')
	return board[r][c] == '0'

def mark_spot(board,x,y,mark):
	print(mark + f' you choose r = {x} c = {y}')
	board[x][y] = mark


def win(board):
	# check 3 rows
	for row in board:
		if len(set(row)) == 1 and row[0] != '0':
			#print('row')
			return True


	# check 3 cols
	r = c = 0
	while c < SIZE:
		col = [board[r][c] for r in range(SIZE)]
		if len(set(col)) == 1 and col[0] != '0':
			#print('col')
			return True
		c +=1
	# check front diagnoanl
	dx = [board[c][c] for c in range(SIZE)]
	if len(set(dx)) == 1 and dx[0] != '0':
		#print(dx)
		#print('diagnonal')
		return True

	# check back diagnoanl
	idx = [(2,0),(1,1),(0,2)]
	
	dx = [board[r][c] for r,c in idx]
	if len(set(dx)) == 1 and dx[0] != '0':
		#print(dx)
		#print('diagnonal')
		return True

def draw_board(board):

	# draw blank board skeleton
	for r in range(SIZE):
		# Rect(left, top, width, height) -> Rect
		pygame.draw.rect(screen,colors['white'],(r*pixels,0,pixels,height)) # white cols
	
	# horizontal lines
	for r in range(1,SIZE+1):
		pygame.draw.line(screen,colors['black'], start_pos = (0,r*pixels+pixels), end_pos = (SIZE*pixels,r*pixels+pixels))

	# vertical lines
	for r in range(SIZE):
		pygame.draw.line(screen,colors['black'], start_pos = (r*pixels+pixels,pixels), end_pos = (r*pixels+pixels,SIZE*pixels+pixels))

	# mark each players move on board
	for r in range(SIZE):
		for c in range(SIZE):
			if board[r][c] == 'X' or board[r][c] == 'O':
				mark = font.render(board[r][c],1,colors['black'])
				left = c*pixels + 17
				top = height-(r*pixels+pixels)+10
				screen.blit(mark,(left,top))
	pygame.display.update()






size = (width,height)

board = create_board()
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


print_board(board)
turn = 0

while turn < SIZE**2:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:  
			#player1 --> x
			if turn % 2 == 0:
				y , x  = event.pos[0]//pixels , abs(event.pos[1]//pixels-3)
				# X = input(' X ... choose row and col of selection seperated by a space ex. -> 0 1 --> : ')
				X = (x,y)
				if valid_selection(board,X):
					r,c = x,y
					mark_spot(board,r,c,'X')
					draw_board(board)
					print_board(board)

			#player2 --> o
			else:
				y , x = event.pos[0]//pixels , abs(event.pos[1]//pixels-3)
				O = (x,y)
				# O = input(' O ... choose row and col of selection seperated by a space ex. -> 0 1 --> : ')
				if valid_selection(board,O):
					r,c = x,y
					mark_spot(board,r,c,'O')
					print_board(board)
					draw_board(board)
			# print board then check if game is over
			if win(board):
				gg = 'X' if turn % 2 == 0 else 'O'
				print(f"Congrats player {gg}")
				turn = SIZE**2
				print('why am i here')

			turn +=1
	pygame.display.update()

while True:
	# game is a tie
	if turn < SIZE**2:
		congrats = "Congrats Player " + gg + " !!!"
		label = font.render(congrats,1,colors.green)
		screen.blit(label,(40,10))
		print() 
	else:
		

	for events in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
