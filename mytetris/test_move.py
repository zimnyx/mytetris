
import unittest
from mytetris.moves import Move, KeyNotSupported, MoveMapper



class MoveMapperTest(unittest.TestCase):
    def setUp(self):
        config = {
            MoveMapper.KEY_NAME_MOVE_LEFT: 'a',
            MoveMapper.KEY_NAME_MOVE_RIGHT: 'd',
            MoveMapper.KEY_NAME_ROTATE_CCW: 'w',
            MoveMapper.KEY_NAME_ROTATE_CW: 's',
        }
        self.mapper = MoveMapper(config)

    def test_get_move_by_key_returns_expected_move(self):
        self.assertEqual(self.mapper.get_move_by_key('w'), Move.ROTATE_COUNTER_CLOCKWISE)

    def test_get_move_by_key_raises_exception_for_unsupported_key(self):
        with self.assertRaises(KeyNotSupported):
            self.mapper.get_move_by_key('W')
