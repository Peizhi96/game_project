from random import randint

grid = []
for i in range(10):
	grid.append([0] * 10)

def grid1(grid):
	for row in grid:
		print(" ".join(row))

def randomrow(grid):
	return randint(0, len(grid) - 1)

def randomcol(grid):
	return randint(0, len(grid[0]) - 1)

shiprow = randomrow(grid)
shipcol = randomcol(grid)

print("Game begins!")
grid1(gird)

for turn in range(5):
	print("Turn", turn + 1)
	guess_row = int(input("Guess Row (0-9): "))
	guess_col = int(input("Guess Col (0-9):"))

	if guess_col == shipcol and guess_row == shiprow:
		print("Congrats! You sank my ship!")
		break
	else:
		if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
			print("Invalid!")
		elif (grid[guess_row][guess_col] == 'X'):
			print('This one has already been guessed.')
		else:
			print('You missed my ship!')
			grid[guess_row][guess_col] = 'X'
		if (turn == 4):
			print('Game Over')
		grid1(grid)
















