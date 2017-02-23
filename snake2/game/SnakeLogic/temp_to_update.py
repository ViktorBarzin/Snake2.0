from game.SnakeLogic.point_snake_snakeWorld import SnakeWorld


def start_game(field_size, num_players, play_ids):
    snk = SnakeWorld(num_players, field_size, play_ids)
    snk.prepare_snakes(num_players, play_ids)
    return snk


def update_game(commands, snk):
    return snk.handle_game()
