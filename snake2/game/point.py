class Point:

    def __init__(self, cord_x, cord_y, data_cont=None):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.data_cont = data_cont

    def __add__(self, other):
        return {'cord_x': self.cord_x + other.cord_x,
                'cord_y': self.cord_y + other.cord_y}

    def __sub__(self, other):
        pass

    def get_content(self):
        return self.data_cont


class Snake:

    def __init__(self, start_pos, body):
        self.head = Point(start_pos)
        self.body = body
        self.size = len(body) + 1

        self.directions = {
                'up' = Point(-1, 0),
                'down' = Point(1), 0),
                'right = Point(0, 1),
                'left = Point(0, -1)
        }

        self.curr_dir = self.head - self.body[0]

    def move(self, direct):
        self.body = list(self.head).extend(self.body[:-1])
        self.head = Point(self.head + self.directions[direct]
