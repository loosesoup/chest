import pygame
import sys
import csv


SIZE = 3
def create_board():
	return [['0','0','0'] for _ in range(SIZE)]

def print_board(board):
	for row in board[::-1]:
		print(row)

def valid_selection(board,Z):
	r,c = int(Z[0]) , int(Z[2])
	print('c',c,type(c))
	return board[r][c] == '0'

def mark_spot(board,x,y,mark):
	print(mark + f' you choose r = {x} c = {y}')
	board[x][y] = mark


def win(board):
	# check 3 rows
	for row in board:
		if len(set(row)) == 1 and row[0] != '0':
			print('row')
			return True


	# check 3 cols
	r = c = 0
	while c < SIZE:
		col = [board[r][c] for r in range(SIZE)]
		if len(set(col)) == 1 and col[0] != '0':
			print('col')
			return True
		c +=1
	# check front diagnoanl
	dx = [board[c][c] for c in range(SIZE)]
	if len(set(dx)) == 1 and dx[0] != '0':
		print(dx)
		print('diagnonal')
		return True

	# check back diagnoanl
	idx = [(2,0),(1,1),(0,2)]
	
	dx = [board[r][c] for r,c in idx]
	if len(set(dx)) == 1 and dx[0] != '0':
		print(dx)
		print('diagnonal')
		return True

board = create_board()
print_board(board)
turn = 0

while turn < SIZE**2:

	#player1 --> x
	if turn % 2 == 0:
		X = input(' X ... choose row and col of selection seperated by a space ex. -> 0 1 --> : ')
		if valid_selection(board,X):
			r,c = int(X[0]),int(X[2])
			mark_spot(board,r,c,'X')
			print_board(board)

			if win(board):
				gg = 'X'
				print("player 'X' wins ")
				break



	#player2 --> o
	else:
		O = input(' O ... choose row and col of selection seperated by a space ex. -> 0 1 --> : ')
		if valid_selection(board,O):
			r,c = int(O[0]),int(O[2])
			mark_spot(board,r,c,'O')
			print_board(board)

			if win(board):
				gg = 'O'
				print('player "O" wins')
				break
	# print board then check if game is over
	

	turn +=1
# game is a tie
if turn == SIZE**2:
	print('game ends in a draw')

