import numpy as np

ROWS = 6
COLUMNS = 7

def create_board():
	return np.zeros((ROWS, COLUMNS), dtype=int)

def print_board(board):
	print("\n 1 2 3 4 5 6 7")
	for row in board:
		print('|' + '|'.join([' ' if x == 0 else ('X' if x == 1 else 'O') for x in row]) + '|')
	print("-----------------")

def is_valid_location(board, col):
	return board[0][col] == 0

def get_next_open_row(board, col):
	for r in range(ROWS-1, -1, -1):
		if board[r][col] == 0:
			return r
	return None

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def winning_move(board, piece):
	# Check horizontal
	for c in range(COLUMNS-3):
		for r in range(ROWS):
			if all(board[r][c+i] == piece for i in range(4)):
				return True
	# Check vertical
	for c in range(COLUMNS):
		for r in range(ROWS-3):
			if all(board[r+i][c] == piece for i in range(4)):
				return True
	# Check positively sloped diagonals
	for c in range(COLUMNS-3):
		for r in range(ROWS-3):
			if all(board[r+i][c+i] == piece for i in range(4)):
				return True
	# Check negatively sloped diagonals
	for c in range(COLUMNS-3):
		for r in range(3, ROWS):
			if all(board[r-i][c+i] == piece for i in range(4)):
				return True
	return False

def is_board_full(board):
	return all(board[0][c] != 0 for c in range(COLUMNS))

def main():
	board = create_board()
	game_over = False
	turn = 0
	print("Welcome to Connect 4!")
	print_board(board)
	while not game_over:
		player = 1 if turn % 2 == 0 else 2
		piece = player
		try:
			col = int(input(f"Player {player} (" + ("X" if player == 1 else "O") + "), choose column (1-7): ")) - 1
		except ValueError:
			print("Invalid input. Please enter a number between 1 and 7.")
			continue
		if col < 0 or col >= COLUMNS:
			print("Column out of range. Try again.")
			continue
		if not is_valid_location(board, col):
			print("Column full. Try another one.")
			continue
		row = get_next_open_row(board, col)
		drop_piece(board, row, col, piece)
		print_board(board)
		if winning_move(board, piece):
			print(f"Player {player} wins! Congratulations!")
			game_over = True
		elif is_board_full(board):
			print("It's a tie!")
			game_over = True
		turn += 1

if __name__ == "__main__":
	main()