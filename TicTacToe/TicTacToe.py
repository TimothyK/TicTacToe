board = [str(x) for x in list(range(1,10))]

def print_board():
    print(board[6:9])
    print(board[3:6])
    print(board[0:3])

def available_inputs():
    return [x for x in board if x.isdigit()]

def is_game_over():
    return available_inputs() == []

def get_input(player):
    available = available_inputs()
    while True:
        result = input(f"Enter a selection for {player}: ")
        if result in available:
            return int(result)-1
        else:
            print("The available selections are: {}".format(' '.join(available)))

player = 'X'

while not is_game_over():
    print_board()
    cell = get_input(player)
    board[cell] = player
    player = 'O' if player=='X' else 'X'

