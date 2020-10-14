
from __future__ import annotations
import copy
from mytetris.shape import Shape



class FieldAlreadyAccupied(Exception):
    pass

class BoardBoundaryCrossed(Exception):
    pass

class Board:

    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.set_fields(self.init_empty())

    def init_empty(self):
        fields = []
        for y in range(self.height):
            fields.append([])
            for x in range(self.width):
                fields[y].append(False)
        return fields

    def set_fields(self, fields):
        self.fields = fields

    def with_shape(self, shape: Shape, shape_x: int, shape_y: int) -> Shape:
        '''
        Return new board with shape placed.
        If you take rectangle that encloses shape, it's left bottom will be put at (x,y).
        We accept if shape crosses top border. Other boarder crossing will result in BoardBoundaryCrossed exception
        '''
        if shape_x < 0:
            raise BoardBoundaryCrossed()

        fields = copy.deepcopy(self.fields)
        for y_in_shape, y_on_board in enumerate(range(shape_y - shape.height +  1, shape_y+1)):
            if y_on_board < 0:
                continue
            for x_in_shape, x_on_board in enumerate(range(shape_x, shape_x+shape.width)):
                try:
                    fields[y_on_board][x_on_board]
                except IndexError:
                    raise BoardBoundaryCrossed()
                # skip this field if shape doesn't fill it
                if shape.fields[y_in_shape][x_in_shape] is False:
                    continue

                if fields[y_on_board][x_on_board] is True:
                    raise FieldAlreadyAccupied(f'{x_on_board=},{y_on_board=}')

                fields[y_on_board][x_on_board] = shape.fields[y_in_shape][x_in_shape]
        board = Board(self.width, self.height)
        board.set_fields(fields)
        return board

