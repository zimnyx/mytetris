

import sys
from mytetris.game import Tetris, DEFAULT_MOVE_STRATEGY, GameOver, ConfigurationError
from mytetris.moves import MoveMapper
from mytetris.shape import Shape
from mytetris.board import Board
import local_config



def run_game():
    shapes = [Shape.parse_from_string(data, Shape.DEFAULT_FIELD_OCUPIED_MARKER) for data in local_config.SHAPES]
    move_mapper = MoveMapper(local_config.KEY_MAPPING)
    board = Board(local_config.BOARD_WIDTH, local_config.BOARD_HEIGHT)
    Tetris(move_mapper, board, shapes, DEFAULT_MOVE_STRATEGY).run()



try:
    run_game()
except GameOver:
    sys.exit(0)
except ConfigurationError as e:
    print(e)
    sys.exit(1)



