class Board:
    def __init__(self):
        self.board = [str(x) for x in list(range(1,10))]

    def row(self, x):
        return self.board[(x-1)*3:x*3]
    def col(self, x):
        return self.board[x-1:9:3]
    def forward_cross_line(self):
        return [self.board[0]] + [self.board[4]] + [self.board[8]]
    def back_cross_line(self):
        return [self.board[2]] + [self.board[4]] + [self.board[6]]

    def print_board(self):
        print(self.row(3))
        print(self.row(2))
        print(self.row(1))

    def available_inputs(self):
        return [x for x in self.board if x.isdigit()]

    def change_cell(self, cell, player_mark):
        '''
        cell should be a value returned from available_inputs
        '''
        pos = int(cell)-1
        self.board[pos] = player_mark

    def winner(self):
        def lines():
            return[self.row(1), self.row(2), self.row(3), self.col(1), self.col(2), self.col(3), self.forward_cross_line(), self.back_cross_line()]

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
