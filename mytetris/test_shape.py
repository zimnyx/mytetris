
import unittest
from mytetris.shape import Shape



class ShapeTest(unittest.TestCase):
    def test_parse_from_string_returns_exected_shape_for_single_line(self):
        data = '* *'
        shape = Shape.parse_from_string(data, '*')
        expected = [
                [True, False, True],
        ]
        self.assertEqual(shape.fields, expected)

    def test_parse_from_string_returns_exected_shape_for_multiline(self):
        data = '* *\n***\n  *'
        shape = Shape.parse_from_string(data, '*')
        expected = [
                [True, False, True],
                [True, True, True],
                [False, False, True],
        ]
        self.assertEqual(shape.fields, expected)

    def test_rorate_ccw_returns_expected_shape(self):
        data = '***\n*  '
        shape = Shape.parse_from_string(data, '*')
        expected = [
                [True, False],
                [True, False],
                [True, True],
        ]
        self.assertEqual(shape.rotate_ccw().fields, expected)

    def test_rorate_ccw_4x_returns_identical_shape(self):
        data = '***\n*  '
        ori_shape = Shape.parse_from_string(data, '*')
        shape = ori_shape
        for i in range(4):
            shape = shape.rotate_ccw()
        self.assertEqual(shape.fields, ori_shape.fields)

    def test_rorate_cw_returns_expected_shape(self):
        data = '***\n*  '
        shape = Shape.parse_from_string(data, '*')
        expected = [
                [True, True],
                [False, True],
                [False, True],
        ]
        self.assertEqual(shape.rotate_cw().fields, expected)

    def test_rorate_cw_4x_returns_identical_shape(self):
        data = '***\n*  '
        ori_shape = Shape.parse_from_string(data, '*')
        shape = ori_shape
        for i in range(4):
            shape = shape.rotate_cw()
        self.assertEqual(shape.fields, ori_shape.fields)

    def test_double_rotate_should_result_in_same_result_as_opposite_rotation(self):
        data = '***\n*  '
        shape = Shape.parse_from_string(data, '*')
        self.assertEqual(shape.rotate_ccw().rotate_ccw(), shape.rotate_cw().rotate_cw())

