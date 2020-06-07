from colorama import init
from colorama import Fore, Back, Style

class Board:
    def __init__(self):
        self.__board = [str(x) for x in list(range(1,10))]
        init()

    def __row(self, x):
        return self.__board[(x-1)*3:x*3]
    def __col(self, x):
        return self.__board[x-1:9:3]
    def __forward_cross_line(self):
        return [self.__board[0]] + [self.__board[4]] + [self.__board[8]]
    def __back_cross_line(self):
        return [self.__board[2]] + [self.__board[4]] + [self.__board[6]]
    def __lines(self):
        return[self.__row(1), self.__row(2), self.__row(3), self.__col(1), self.__col(2), self.__col(3), self.__forward_cross_line(), self.__back_cross_line()]
    
    def print_board(self):
        def add_color(x):
            #program must be run from a command line to see the colors. 
            if x == 'X':
                return Style.BRIGHT + Fore.YELLOW + x + Fore.RESET + Style.RESET_ALL
            elif x == 'O':
                return Style.BRIGHT + Fore.GREEN + x + Fore.RESET + Style.RESET_ALL
            else:
                return x

        def print_row(row):
            print(' '.join(add_color(x) for x in row))

        print_row(self.__row(3))
        print_row(self.__row(2))
        print_row(self.__row(1))
        print(Fore.RESET)
                                     
    def available_inputs(self):
        return [x for x in self.__board if x.isdigit()]

    def change_cell(self, cell, player_mark):
        '''
        cell should be a value returned from available_inputs
        '''
        pos = int(cell)-1
        self.__board[pos] = player_mark

    def winner(self):
        def line_winner(line):
            token = set(line)        
            if len(token)==1:
               return token.pop()
            else:
               return False

        for line in self.__lines():        
            if line_winner(line):
                return line_winner(line)
        
        return False

    def is_game_over(self):
        return self.available_inputs() == [] or self.winner() != False

    def print_game_result(self):
        print()
        winner = self.winner()
        if winner == False:
            print("The game is a draw")
        else:
            print("The winner is player {}".format(winner))
        self.print_board()
