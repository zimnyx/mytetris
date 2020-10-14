

#from mytetris.moves import Move, KeyNotSupported, MoveMapper

import typing
import random
import os
from os import system, name
from mytetris.moves import MoveMapper, KeyNotSupported, Move
from mytetris.shape import Shape
from mytetris.board import Board, FieldAlreadyAccupied, BoardBoundaryCrossed




class GameOver(Exception):
    pass

class ConfigurationError(ValueError):
    pass



class MoveLeft:
    def execute(self, shape: Shape, shape_x: int, shape_y: int) -> (Shape, int, int):
        shape_x -= 1
        shape_y += 1
        return shape, shape_x, shape_y

class MoveRight:
    def execute(self, shape: Shape, shape_x: int, shape_y: int) -> (Shape, int, int):
        shape_x += 1
        shape_y += 1
        return shape, shape_x, shape_y

class RotateCounterClockwise:
    def execute(self, shape: Shape, shape_x: int, shape_y: int) -> (Shape, int, int):
        shape_y += 1
        return shape.rotate_ccw(), shape_x, shape_y

class RotateClockwise:
    def execute(self, shape: Shape, shape_x: int, shape_y: int) -> (Shape, int, int):
        shape_y += 1
        return shape.rotate_cw(), shape_x, shape_y


DEFAULT_MOVE_STRATEGY = {
    Move.MOVE_LEFT: MoveLeft(),
    Move.MOVE_RIGHT: MoveRight(),
    Move.ROTATE_COUNTER_CLOCKWISE: RotateCounterClockwise(),
    Move.ROTATE_CLOCKWISE: RotateClockwise(),
}



class Tetris:
    BOARD_DRAW_CHAR = '#'
    def __init__(self, move_mapper: MoveMapper, board: Board, shapes: typing.List[Shape], move_strategy: dict):
        random.seed(4)
        self.move_mapper = move_mapper
        self.board = board
        self.shapes = shapes
        self.move_strategy = move_strategy
        self.shape_side_max_len = max([max(shape.width, shape.height) for shape in self.shapes])

    def validate_config(self):
        if self.shape_side_max_len > min(self.board.width, self.board.height):
            raise ConfigurationError('Every defined shape should fit into board dimentions')

    def get_random_start_x(self, shape: Shape):
        return random.randint(0, self.board.width - shape.width + 1)

    def get_user_move(self):
        key = input('--> ')
        return self.move_mapper.get_move_by_key(key)

    def run(self):
        while True:
            shape = random.choice(self.shapes)
            shape_x = self.get_random_start_x(shape)
            # shape appears above board
            shape_y = -1
            self.process_shape(shape, shape_x, shape_y)

    def process_shape(self, shape: Shape, shape_x: int, shape_y: int) -> None:
        while True:
            if not self.any_move_allowed(shape, shape_x, shape_y):
                if shape_y == -1:
                    self.print_board_with_shape(shape, shape_x, shape_y)
                    print('Game Over!')
                    raise GameOver()
                else:
                    self.board = self.board.with_shape(shape, shape_x, shape_y)
                    return
            try:
                self.print_board_with_shape(shape, shape_x, shape_y)
                move = self.get_user_move()
                if not self.move_allowed(move, shape, shape_x, shape_y):
                    continue
                shape, shape_x, shape_y = self.execute_move(move, shape, shape_x, shape_y)
            except KeyNotSupported:
                continue

    def any_move_allowed(self, shape: Shape, shape_x: int, shape_y: int) -> bool:
        for move in Move:
            if self.move_allowed(move, shape, shape_x, shape_y):
                return True
        return False

    def move_allowed(self, move: Move, shape: Shape, shape_x: int, shape_y: int):
        try:
            self.board.with_shape(*self.execute_move(move, shape, shape_x, shape_y))
            return True
        except (BoardBoundaryCrossed, FieldAlreadyAccupied):
            return False

    def execute_move(self, move: Move, shape: Shape, shape_x: int, shape_y: int) -> (Shape, int, int):
        return self.move_strategy[move].execute(shape, shape_x, shape_y)

    def print_board_with_shape(self, shape: Shape, shape_x: int, shape_y: int) -> str:
        self.clear_screen()
        output = ''
        # print above board
        for board_y in range(-self.shape_side_max_len, 0):
            if board_y == shape_y - shape.height + 1:
                break
            print()

        for shape_y_tmp, board_y in enumerate(range(shape_y - shape.height + 1, 0)):
            if board_y == 0:
                break
            output += ' ' * (shape_x + 1) + ''.join([Shape.DEFAULT_FIELD_OCUPIED_MARKER if field is True else ' ' for field in shape.fields[shape_y_tmp]]) + os.linesep

        # print board
        for row in self.board.with_shape(shape, shape_x, shape_y).fields:
            output += self.BOARD_DRAW_CHAR + ''.join([Shape.DEFAULT_FIELD_OCUPIED_MARKER if field is True else ' ' for field in row]) + self.BOARD_DRAW_CHAR + os.linesep
        output += self.BOARD_DRAW_CHAR * (self.board.width + 2)
        output += os.linesep
        output += str(self.move_mapper)
        print(output)

    def clear_screen(self):
        # for windows
        if name == 'nt':
            system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')
