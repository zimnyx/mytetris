
import unittest
import random
from mytetris.game import Tetris, DEFAULT_MOVE_STRATEGY
from mytetris.moves import MoveMapper
from mytetris.shape import Shape
from mytetris.board import Board
#from mytetris.board import Board, BoardBoundaryCrossed



class GameTest(unittest.TestCase):
    def setUp(self):
        mapper = MoveMapper({
            MoveMapper.KEY_NAME_MOVE_LEFT: 'a',
            MoveMapper.KEY_NAME_MOVE_RIGHT: 'd',
            MoveMapper.KEY_NAME_ROTATE_CCW: 'w',
            MoveMapper.KEY_NAME_ROTATE_CW: 's',
        })
        shapes = (
            '****',
            '* \n* \n**',
            ' *\n *\n**',
            ' *\n**\n* ',
            '**\n**',
        )
        board = Board(6,7)
        self.game = Tetris(mapper, board, [Shape.parse_from_string(data, '*') for data in shapes], DEFAULT_MOVE_STRATEGY)

    def test_get_random_start_x_returns_value_in_expected_range(self):
        # generated random values will be consisent every time we run this test
        random.seed(1)
        shape = Shape.parse_from_string('* *\n***\n  *', '*')
        x = self.game.get_random_start_x(shape)
        for i in range(30):
            self.assertGreaterEqual(x, 0, 'Start x cannot be negative')
            self.assertLessEqual(x, 3, 'Start x too large - shape exceeds board\'s right border')


