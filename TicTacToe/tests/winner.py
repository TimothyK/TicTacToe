import unittest
from board import Board

class Test_winner(unittest.TestCase):
    def test_emptyBoard_noWinner(self):
        #Arrange
        board = Board()

        #Act
        winner = board.winner()

        #Assert
        self.assertFalse(winner)

    def test_topRow_winner(self):
        #Arrange
        board = Board()
        board.change_cell('7', 'X')
        board.change_cell('8', 'X')
        board.change_cell('9', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_middleRow_winner(self):
        #Arrange
        board = Board()
        board.change_cell('4', 'X')
        board.change_cell('5', 'X')
        board.change_cell('6', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_bottomRow_winner(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'X')
        board.change_cell('2', 'X')
        board.change_cell('3', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_leftColumn_winner(self):
        #Arrange
        board = Board()
        board.change_cell('7', 'X')
        board.change_cell('4', 'X')
        board.change_cell('1', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_middleColumn_winner(self):
        #Arrange
        board = Board()
        board.change_cell('8', 'X')
        board.change_cell('5', 'X')
        board.change_cell('2', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_rightColumn_winner(self):
        #Arrange
        board = Board()
        board.change_cell('9', 'X')
        board.change_cell('6', 'X')
        board.change_cell('3', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_backCross_winner(self):
        #Arrange
        board = Board()
        board.change_cell('7', 'X')
        board.change_cell('5', 'X')
        board.change_cell('3', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')

    def test_forwardCross_winner(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'X')
        board.change_cell('5', 'X')
        board.change_cell('9', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'X')
    
    def test_differentToken_winner(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'O')
        board.change_cell('5', 'O')
        board.change_cell('9', 'O')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, 'O')

    def test_blocked_noWinner(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'X')
        board.change_cell('5', 'O')
        board.change_cell('9', 'X')

        #Act
        winner = board.winner()

        #Assert
        self.assertEqual(winner, False)

    def test_winner_gameOver(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'O')
        board.change_cell('5', 'O')
        board.change_cell('9', 'O')

        #Act
        game_over = board.is_game_over()

        #Assert
        self.assertTrue(game_over)
    
    def test_draw_gameOver(self):
        #Arrange
        board = Board()
        board.change_cell('7', 'X')
        board.change_cell('8', 'O')
        board.change_cell('9', 'X')

        board.change_cell('4', 'O')
        board.change_cell('5', 'O')
        board.change_cell('6', 'X')

        board.change_cell('1', 'O')
        board.change_cell('2', 'X')
        board.change_cell('3', 'O')

        #Act
        game_over = board.is_game_over()

        #Assert
        self.assertTrue(game_over)

    def test_emptyBoard_notGameOver(self):
        #Arrange
        board = Board()

        #Act
        game_over = board.is_game_over()

        #Assert
        self.assertFalse(game_over)


if __name__ == '__main__':
    unittest.main()
