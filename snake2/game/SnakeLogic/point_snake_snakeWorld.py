from copy import deepcopy
from random import randint
from time import sleep


class Point:

    def __init__(self, coords, data_cont=None):
        # content: b: body, h: head, f: food
        # empty point: .
        self.cord_x = coords[0]
        self.cord_y = coords[1]
        self.data_cont = data_cont

    def __add__(self, other):
        self.cord_x = self.cord_x + other.cord_x
        self.cord_y = self.cord_y + other.cord_y
        return self

    def __sub__(self, other):
        # import ipdb; ipdb.set_trace()
        self.cord_x = self.cord_x - other.cord_x
        self.cord_y = self.cord_y - other.cord_y
        return self

    def __str__(self):
        return '({}, {})'.format(self.cord_x, self.cord_y)

    def __repr__(self):
        return '({}, {})'.format(self.cord_x, self.cord_y)

    def __eq__(self, other):
        return self.cord_x == other.cord_x and self.cord_y == other.cord_y

    def __hash__(self):
        return hash(self.cord_x)


    def get_content(self):
        return self.data_cont

    def oposite_points(self, other):
        # import ipdb; ipdb.set_trace()
        return self.cord_x == -1*(other.cord_x) and self.cord_y == -1*(other.cord_y)


class Snake:

    def __init__(self, start_pos, body, snk_id=None, is_alive=True):
        # import ipdb; ipdb.set_trace()
        self.head = start_pos
        self.body = body
        self.size = len(body) + 1
        self.snk_id = id
        self.is_alive = is_alive

        self.directions = {
                'up': Point((-1, 0)),
                'down': Point((1, 0)),
                'right': Point((0, 1)),
                'left': Point((0, -1))
        }

        self.curr_dir = self.create_curr_dir()

    def create_curr_dir(self):
        direct = deepcopy(self.head) - self.body[0]
        for key, value in self.directions.items():
            if value == direct:
                return {
                    'dir': key,
                    'point': value
                }

    def move(self, direct):
        if self.directions[direct].oposite_points(self.curr_dir['point']):
            self.move(self.curr_dir['dir'])
        else:
            new_body = [deepcopy(self.head)]
            new_body[0].data_cont = self.body[0].data_cont
            new_body.extend(self.body[:-1])
            self.body = new_body
            self.head = self.head + self.directions[direct]
            self.curr_dir = self.create_curr_dir()

    def point_in(self, point):
        for pt in self.body:
            if point == pt:
                return True
        return point == self.head

   # snake will grow after next move
    def grow(self):
        self.body.extend([Point((0, 0))])
        self.size += 1

    def get_point_content(self, point):
        for pt in self.body:
            if point == pt:
                return pt.get_content()
        return self.head.get_content()


class SnakeWorld:


    def __init__(self, world_size=16, num_of_players=4):
        self.starting_pos = {
                0: Snake(Point((4, 4), '0'), [Point((4, 3), '1'), Point((4, 2), '1')], snk_id=0),
                1: Snake(Point((6, 12), '2'), [Point((5, 12), '3'), Point((4, 12), '3')], snk_id=1),
                2: Snake(Point((12, 10), '4'), [Point((12, 11), '5'), Point((12, 12), '5')], snk_id=2),
                3: Snake(Point((10, 4), '6'), [Point((11, 4), '7'), Point((12, 4), '7')], snk_id=3)
        }

        self.snakes = self.prepare_snakes(num_of_players)
        self.world_size = world_size
        self.food = self.drop_food()
        self.num_of_players = num_of_players


    def prepare_snakes(self, num):
        snakes = {}
        for i in range(num):
            # import ipdb; ipdb.set_trace()
            snakes[i] = self.starting_pos[i]
        return snakes

    # returns string representing every object, with it's data_content
    def get_world(self):
        res = ''
        for row in range(self.world_size):
            for col in range(self.world_size):
                if self.point_exists(Point((row, col))):
                    curr_snake = self.point_to_snake(Point((row, col)))
                    res += curr_snake.get_point_content(Point((row, col)))
                else:
                    res += '.'
            res += '\n'
        return res

    def point_to_snake(self, point, curr_snake=None):
        if curr_snake:
            for s_id, snake in self.snakes.items():
                if s_id == curr_snake:
                    continue
                if snake.point_in(point):
                    return True
            # import ipdb; ipdb.set_trace()
            return False
        else:
            for s_id, snake in self.snakes.items():
                if snake.point_in(point):
                    return snake
            # import ipdb; ipdb.set_trace()
            return False

    def drop_food(self):
        new_x = randint(0, self.world_size)
        new_y = randint(0, self.world_size)
        while self.point_exists(Point((new_x, new_y))):
            new_x = randint(0, self.world_size)
            new_y = randint(0, self.world_size)
        return Point((new_x, new_y))

    def point_exists(self, point):
        # import ipdb; ipdb.set_trace()
        for snake_id, snake in self.snakes.items():
            if snake.point_in(point):
                return True
        return False

    def move_snakes(self, new_directions):
        for key, value in new_directions.items():
            self.snakes[key].move(value)
        self.something_happened()

    def something_happened(self):
        self.check_for_colision()
        self.snake_ate()

    def check_for_colision(self):
        for key, value in self.snake.items():


    def snake_ate(self):
        pass


def main():
    snk1 = Snake(Point((1, 1), 'h'), [Point((1, 2), 'b'), Point((1, 3), 'b')])
    snk2 = Snake(Point((3, 1), 'h'), [Point((3, 2), 'b'), Point((3, 3), 'b')])
    my_world = SnakeWorld(16, 2)
    # import ipdb; ipdb.set_trace()
    for i in range(3):
        print(my_world.get_world())
        my_world.move_snakes({
            0: 'up',
            1: 'down'
            })
        sleep(1)


if __name__ == '__main__':
    main()