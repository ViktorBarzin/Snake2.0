from copy import deepcopy
from random import randint
from time import sleep
from subprocess import call

# from game.views import get_user_id_arrow


class Point:

    def __init__(self, coords, data_cont='.'):
        # content: b: body, h: head, f: food
        # empty point: .
        self.cord_x = coords[0]
        self.cord_y = coords[1]
        self.data_cont = data_cont

    def __add__(self, other, mod_compare=None):
        if mod_compare:
            self.cord_x = (self.cord_x +
                           other.cord_x) % mod_compare
            self.cord_y = (self.cord_y +
                           other.cord_y) % mod_compare
            return self
        self.cord_x = self.cord_x + other.cord_x
        self.cord_y = self.cord_y + other.cord_y
        return self

    def __sub__(self, other, mod_compare=None):
        if mod_compare:
            self.cord_x = (self.cord_x -
                           other.cord_x) % mod_compare
            self.cord_y = (self.cord_y -
                           other.cord_y) % mod_compare
            return self
        self.cord_x = self.cord_x - other.cord_x
        self.cord_y = self.cord_y - other.cord_y
        return self

    def __mod__(self, mod_value):
        self.cord_x = self.cord_x % mod_value
        self.cord_y = self.cord_y % mod_value
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
        return self.cord_x == -1 * (
            other.cord_x) and self.cord_y == -1 * (other.cord_y)

    def has_arg(self, arg):
        return self.cord_x == arg or self.cord_y == arg


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
        if not (direct.has_arg(1) or direct.has_arg(-1)):
                return self.curr_dir
        for key, value in self.directions.items():
            if value == direct:
                return {
                    'dir': key,
                    'point': value
                }

    def move(self, direct, field_size=None):
        if not direct:
            direct = self.curr_dir
        if self.directions[direct].oposite_points(self.curr_dir['point']):
            self.move(self.curr_dir['dir'], field_size)
        else:
            new_body = [deepcopy(self.head)]
            new_body[0].data_cont = self.body[0].data_cont
            new_body.extend(self.body[:-1])
            self.body = new_body
            if field_size:
                self.head = (self.head + self.directions[direct]) % field_size
            elif field_size is None:
                self.head = self.head + self.directions[direct]
            self.curr_dir = self.create_curr_dir()

    def check_for_border_walking(self, point, max_n):
        pass

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

    def died(self):
        self.is_alive = False


class SnakeWorld:

    def __init__(self, world_size=16, num_of_players=4, game_over=False):
        self.starting_pos = {
            0: Snake(
                Point(
                    (4, 4), '0'), [
                    Point((4, 3), '1'), Point((4, 2), '1')], snk_id=0),
            1: Snake(
                Point(
                    (6, 12), '2'), [
                    Point((5, 12), '3'), Point((4, 12), '3')], snk_id=1),
            2: Snake(
                Point(
                    (4, 10), '4'), [
                    Point((4, 11), '5'), Point((4, 12), '5')], snk_id=2),
            3: Snake(
                Point(
                    (10, 4), '6'), [
                    Point((11, 4), '7'), Point((12, 4), '7')], snk_id=3),
        }

        self.world_size = world_size
        self.snakes = self.starting_pos  # self.prepare_snakes(num_of_players)
        self.food = self.drop_food()
        self.num_of_players = num_of_players
        self.num_of_alive = num_of_players
        self.game_over = game_over

    def prepare_snakes(self, num, pl_ids):
        new_snakes = {}
        for i in range(num):
            # import ipdb; ipdb.set_trace()
            new_snakes[pl_ids[i]] = self.starting_pos[i]
        self.snakes = new_snakes

    # returns string representing every object, with it's data_content
    def get_world(self):
        res = ''
        for row in range(self.world_size):
            for col in range(self.world_size):
                if self.point_exists_in_snake(
                        Point((row, col))) and self.snake_alive(row, col):
                    # import ipdb; ipdb.set_trace()
                    curr_snake = self.point_belongs_snake(Point((row, col)))
                    res += curr_snake.get_point_content(Point((row, col)))
                elif self.food == Point((row, col)):
                    res += 'f'
                else:
                    res += '.'
            # res += '\n'
            res += '<br />'

        return res

    def snake_alive(self, row, col):
        return self.point_belongs_snake(Point((row, col))).is_alive

    def point_belongs_snake(self, point):
        for s_id, snake in self.snakes.items():
            if snake.point_in(point):
                return snake
        # import ipdb; ipdb.set_trace()
        return False


    def point_in_other_snakes(self, point, skip_snake=None):
        for s_id, snakfe in self.snakes.items():
            if s_id == skip_snake:
                continue
            if snake.point_in(point):
                return snake
        # import ipdb; ipdb.set_trace()
        return False

    def drop_food(self):
        new_x = randint(0, self.world_size)
        new_y = randint(0, self.world_size)
        while self.point_exists_in_snake(Point((new_x, new_y))):
            new_x = randint(0, self.world_size)
            new_y = randint(0, self.world_size)
        return Point((new_x, new_y))

    def point_exists_in_snake(self, point, skip_snake=None):
        # import ipdb; ipdb.set_trace()
        for snake_id, snake in self.snakes.items():
            if snake.point_in(point):
                return True
        return False

    def move_snakes(self, new_directions):
        for key, value in new_directions.items():
            if key in self.snakes:
                self.snakes[key].move(value, field_size=self.world_size)
        self.something_happened()

    def something_happened(self):
        self.check_for_colision()
        self.snake_ate()

    def in_other_snake(self, curr_head, curr_id):
        for s_id, snake in self.snakes.items():
            if s_id == curr_id:
                continue
            if snake.point_in(curr_head):
                return snake
        return False

    def check_for_colision(self):
        temp_dict = deepcopy(self.snakes)
        for s_id, snake in temp_dict.items():
            if self.in_other_snake(curr_head=snake.head, curr_id=s_id):
                # self.which_snake(snake.head).died()
                snake.died()
                self.snakes.pop(s_id, snake)
                self.kill_game()

    def kill_game(self):
        self.num_of_alive -= 1
        if self.num_of_alive < 2:
            self.game_over = True

    def which_snake(self, curr_head):
        for s_id, snake in self.snakes.items():
            if snake.head == curr_head:
                return snake

    def snake_ate(self):
        if self.point_exists_in_snake(self.food):
            for s_id, snake in self.snakes.items():
                if not snake.point_in(self.food):
                    snake.grow()
            self.food = self.drop_food()

    def handle_game(self, commands):
        while not self.game_over:
            yield self.get_world()
            self.move_snakes(commands)
            sleep(0.5)
        yield self.get_winner()

    def get_winner(self):
        for s_id, value in self.snakes.items():
            return s_id
        return None

    def get_directs(self):
        comms = get_comms()
        for id, command in user_comands:
            comms[id]= command
        return comms


def main():
    my_world = SnakeWorld(world_size=16, num_of_players=3)
    # import ipdb; ipdb.set_trace()
    for i in range(100):
        call(['clear'])
        print(my_world.get_world())
        my_world.move_snakes({

            0: 'right',
            1: 'down',
            2: 'left',
            3: 'left',})
        print(my_world.game_over)
        sleep(0.5)


if __name__ == '__main__':
    main()
