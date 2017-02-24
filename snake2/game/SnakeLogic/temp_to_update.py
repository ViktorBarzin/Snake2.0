from game.SnakeLogic.point_snake_snakeWorld import SnakeWorld


def start_game(field_size, num_players,play_ids):
    snk = SnakeWorld(field_size, num_players)
    # import ipdb; ipdb.set_trace()# BREAKPOINT)

    snk.prepare_snakes(num_players, play_ids)
    return snk


def update_game(commands, snk):
    # import ipdb; ipdb.set_trace()# BREAKPOINT)

    snk.move_snakes(commands)
    return snk.get_world()
