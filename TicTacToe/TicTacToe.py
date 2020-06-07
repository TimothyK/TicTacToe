board = [str(x) for x in list(range(1,10))]

def print_board():
    print(board[6:9])
    print(board[3:6])
    print(board[0:3])

print_board()

player = 'X'

def available_inputs():
    return [x for x in board if x.isdigit()]

def is_game_over():
    return available_inputs() == []

def get_input():
    available = available_inputs()
    while True:
        result = input(f"Enter a selection for {player}: ")
        if result in available:
            return int(result)-1
        else:
            print("The available selections are: {}".format(' '.join(available)))
       
cell = get_input()

print("You choose {}".format(cell))

board[cell] = player
print_board()

