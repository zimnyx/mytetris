
import enum


class Move(enum.Enum):
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    ROTATE_COUNTER_CLOCKWISE = 3
    ROTATE_CLOCKWISE = 4



class KeyNotSupported(Exception):
    pass



class MoveMapper:
    KEY_NAME_MOVE_LEFT = 'KEY_MOVE_LEFT'
    KEY_NAME_MOVE_RIGHT = 'KEY_MOVE_RIGHT'
    KEY_NAME_ROTATE_CCW = 'KEY_ROTATE_CCW'
    KEY_NAME_ROTATE_CW = 'KEY_ROTATE_CW'

    def __init__(self, config: dict):
        self.mapping = {
            config[self.KEY_NAME_MOVE_LEFT]: Move.MOVE_LEFT,
            config[self.KEY_NAME_MOVE_RIGHT ]: Move.MOVE_RIGHT,
            config[self.KEY_NAME_ROTATE_CCW]: Move.ROTATE_COUNTER_CLOCKWISE,
            config[self.KEY_NAME_ROTATE_CW]: Move.ROTATE_CLOCKWISE,
        }

    def get_move_by_key(self, key: str):
        try:
            return self.mapping[key]
        except KeyError:
            raise KeyNotSupported(key)

    def __str__(self) -> str:
        return ' | '.join(f'{move.name}: {key}' for key, move in self.mapping.items())



