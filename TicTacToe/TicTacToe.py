board = [str(x) for x in list(range(1,10))]

def print_board():
    print(board[6:9])
    print(board[3:6])
    print(board[0:3])

print_board()

player = 'X'

cell = input(f"Enter a selection for {player}: ")

print("You choose {}".format(cell))

board[int(cell)-1] = player
print_board()

