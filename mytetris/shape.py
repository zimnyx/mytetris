

class UnconsistentRowLength(ValueError):
    pass



class Shape:

    DEFAULT_FIELD_OCUPIED_MARKER = '*'

    def __init__(self, fields):
        self.validate_shape(fields)
        self.fields = fields
        self.height = len(fields)
        self.width = len(fields[0])

    def validate_shape(self, fields):
        expected_width = len(fields[0])
        for row in fields:
            if len(row) != expected_width:
                raise ValueError(f'This shape has unconsistent line lenght: {fields}')

    @staticmethod
    def parse_from_string(data: str, field_occupied_marker):
        fields = []
        for y, line in enumerate(data.splitlines()):
            fields.append([])
            for x, is_filled in enumerate(line):
                fields[y].append(is_filled == field_occupied_marker)
        try:
            return Shape(fields)
        except UnconsistentRowLength:
            raise ValueError(f'This shape has unconsistent line lenght: {data}')

    def rotate_ccw(self):
        fields = []
        for x in range(self.width):
            fields.append([])
            for y in range(self.height):
                fields[x].append(self.fields[y][self.width - (x+1)])
        return Shape(fields)

    def rotate_cw(self):
        fields = []
        for new_y in range(self.width):
            fields.append([])
            for new_x in range(self.height):
                fields[new_y].append(self.fields[self.height - (new_x+1)][new_y])
        return Shape(fields)

    def __eq__(self, other):
        return self.fields == other.fields


