'''board - Tic Tac Toe board'''
from colorama import init
from colorama import Fore, Style

class Board:
    '''
    Tic Tac Toe Board
    '''
    def __init__(self):
        self.__board = [str(x) for x in list(range(1, 10))]
        init()

    def __row(self, row_num):
        return self.__board[(row_num-1)*3:row_num*3]
    def __rows(self):
        return [self.__row(x) for x in range(1, 4)]

    def __lines(self):
        def col(col_num):
            return self.__board[col_num-1:9:3]
        def cols():
            return [col(x) for x in range(1, 4)]
        def forward_cross_line():
            return [self.__board[0]] + [self.__board[4]] + [self.__board[8]]
        def back_cross_line():
            return [self.__board[2]] + [self.__board[4]] + [self.__board[6]]
        def cross():
            return [forward_cross_line(), back_cross_line()]

        return self.__rows() + cols() + cross()

    def print_board(self):
        ''' Prints the Tic Tac Toe board, with available selections '''
        def add_color(marker):
            #program must be run from a command line to see the colors.
            if marker == 'X':
                return Style.BRIGHT + Fore.YELLOW + marker + Fore.RESET + Style.RESET_ALL
            if marker == 'O':
                return Style.BRIGHT + Fore.GREEN + marker + Fore.RESET + Style.RESET_ALL
            return marker

        def print_row(row):
            print(' '.join(add_color(x) for x in row))

        for row in self.__rows()[::-1]:
            print_row(row)
        print(Fore.RESET)

    def available_inputs(self):
        ''' Lists available selections for the player to put their mark '''
        return [x for x in self.__board if x.isdigit()]

    def change_cell(self, cell, player_mark):
        '''
        Changes a cell to the player's mark

        Args:
            cell (str): should be a value returned from available_inputs
            player_mark (str): 'X' or 'O'
        '''
        pos = int(cell)-1
        self.__board[pos] = player_mark

    def winner(self):
        '''
        Returns the winner of the game 'X' or 'O'.
        Returns False if there is no winner.
        '''
        def line_winner(line):
            token = set(line)
            if len(token) == 1:
                return token.pop()
            return False

        for line in self.__lines():
            if line_winner(line):
                return line_winner(line)

        return False

    def is_game_over(self):
        ''' Reports (bool) if game has a winner or is a draw '''
        return self.available_inputs() == [] or self.winner()

    def print_game_result(self):
        ''' Prints the final result of the game, including game board '''
        print()
        winner = self.winner()
        if not winner:
            print("The game is a draw")
        else:
            print("The winner is player {}".format(winner))
        self.print_board()
