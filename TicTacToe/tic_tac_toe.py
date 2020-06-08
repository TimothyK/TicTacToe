'''
Tic Tac Toe game
'''
from board import Board

def get_input(board, player):
    '''
    Gets the user's selection for where to place their token on the board
    '''
    available = board.available_inputs()
    while True:
        result = input(f"Enter a selection for {player}: ")
        if result in available:
            return result
        print("The available selections are: {}".format(' '.join(available)))

#GAME MAIN
def run():
    '''
    Single run of the Tic Tac Toe game
    '''
    board = Board()
    player = 'X'

    while not board.is_game_over():
        board.print_board()
        cell = get_input(board, player)
        board.change_cell(cell, player)
        player = 'O' if player == 'X' else 'X'

    board.print_game_result()

if __name__ == "__main__":
    run()
