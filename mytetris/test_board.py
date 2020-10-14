
import unittest
from mytetris.shape import Shape
from mytetris.board import Board, FieldAlreadyAccupied, BoardBoundaryCrossed



class BoardTest(unittest.TestCase):

    def test_init_empty_board(self):
        board = Board(3,2)
        expected = [
            [False, False, False],
            [False, False, False],
        ]
        self.assertEqual(board.init_empty(), expected)

    def test_with_shape_returns_expected_board_if_placed_inside_board(self):
        board = Board(6,7)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        expected = [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, True,  False, True,  False, False],
            [False, True,  True,  True,  False, False],
            [False, False, False, True,  False, False],
            [False, False, False, False, False, False],
        ]
        self.assertEqual(board.with_shape(shape, 1,5).fields, expected)

    def test_with_shape_returns_expected_board_if_crossing_top_border(self):
        board = Board(6,7)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        expected = [
            [False, True,  True,  True,  False, False],
            [False, False, False, True,  False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
        ]
        self.assertEqual(board.with_shape(shape, 1,1).fields, expected)

    def test_with_shape_throws_exception_on_collision(self):
        board = Board(6,7)
        fields = [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, True,  False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
        ]
        board.set_fields(fields)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        with self.assertRaises(FieldAlreadyAccupied):
            board.with_shape(shape, 1,5)

    def test_with_shape_throws_exception_on_left_border_cross(self):
        board = Board(6,7)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        with self.assertRaises(BoardBoundaryCrossed):
            board.with_shape(shape, -1,5)

    def test_with_shape_throws_exception_on_right_border_cross(self):
        board = Board(6,7)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        with self.assertRaises(BoardBoundaryCrossed):
            board.with_shape(shape, 4,5)

    def test_with_shape_throws_exception_on_bottom_border_cross(self):
        board = Board(6,7)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        with self.assertRaises(BoardBoundaryCrossed):
            board.with_shape(shape, 1,7)

    def test_ah(self):
        board = Board(8,8)
        fields = [
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False],
            [False, False, False, True, True, False, False, False],
            [False, False, False, True, True, False, False, False],
            [False, False, False, True, True, False, False, False],
            [False, False, False, True, True, False, False, False],
        ]
        board.set_fields(fields)
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        board.with_shape(shape, 2,4)
