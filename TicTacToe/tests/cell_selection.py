import unittest
from board import Board

class Test_cell_selection(unittest.TestCase):
    def test_emptyBoard_allAvailable(self):
        #Arrange
        board = Board()
        
        #Act
        inputs = board.available_inputs()
        
        #Assert
        self.assertEqual(len(inputs), 9)
        self.assertEqual(inputs, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

    def test_chooseOne_oneNotAvailable(self):
        #Arrange
        board = Board()
        board.change_cell('1', 'X')

        #Act
        inputs = board.available_inputs()
        
        #Assert
        self.assertEqual(len(inputs), 8)
        self.assertEqual(inputs, ['2', '3', '4', '5', '6', '7', '8', '9'])



if __name__ == '__main__':
    unittest.main()
