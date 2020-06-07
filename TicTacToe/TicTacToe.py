board = [str(x) for x in list(range(1,10))]

def row(x):
    return board[(x-1)*3:x*3]
def col(x):
    return board[x-1:9:3]
def forward_cross_line():
    return [board[0]] + [board[4]] + [board[8]]
def back_cross_line():
    return [board[2]] + [board[4]] + [board[6]]

def print_board():
    print(row(3))
    print(row(2))
    print(row(1))

def available_inputs():
    return [x for x in board if x.isdigit()]

def get_input(player):
    available = available_inputs()
    while True:
        result = input(f"Enter a selection for {player}: ")
        if result in available:
            return int(result)-1
        else:
            print("The available selections are: {}".format(' '.join(available)))



def winner():
    def lines():
        return[row(1), row(2), row(3), col(1), col(2), col(3), forward_cross_line(), back_cross_line()]

    def line_winner(line):
        token = set(line)        
        if len(token)==1:
           return token.pop()
        else:
           return False

    for line in lines():        
        if line_winner(line):
            return line_winner(line)
        
    return False

def is_game_over():
    return available_inputs() == [] or winner() != False

def print_game_result():
    print()
    winner = winner()
    if winner == False:
        print("The game is a draw")
    else:
        print("The winner is player {}".format(winner))
    print_board()

#GAME MAIN
player = 'X'

while not is_game_over():
    print_board()
    cell = get_input(player)
    board[cell] = player
    player = 'O' if player=='X' else 'X'

print_game_result()

