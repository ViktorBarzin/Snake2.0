from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from game.SnakeLogic.point_snake_snakeWorld import SnakeWorld
from game.SnakeLogic.temp_to_update import start_game, update_game
import json

# Create your views here.

# global variable which is used for ocmmunication between client and snake
# logic
user_id_arrow = {}
snk = ''

@login_required(login_url = 'login')
def index(request):
    global snk
    snk = start_game(22,
               len(list(get_user_id_arrow().keys())),
               list(get_user_id_arrow().keys()))
    # import ipdb; ipdb.set_trace()

    # Reset the user arrow dict so that everytime a game is created, the users
    # will be new with no initial moves
    # CAREFUL !!! PRONE TO BUGS !!! if something with arrows is not working,
    # delete the following line
    user_id_arrow ={}
    user = request.user
    # field = SnakeWorld(16, 4).get_world()
    return render(request, 'game.html')


def get_user_id_arrow():
    global user_id_arrow
    return user_id_arrow


def update_game_field_ajax(request):
    res = update_game(get_user_id_arrow(), snk )
    # import ipdb; ipdb.set_trace()# BREAKPOINT)

    return HttpResponse(json.dumps(res))


def get_arrows_ajax(request):
    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    # print('-'*20 + request.GET.params['key'])
    # print('-' * 20 + dict(request.GET).get('params[2][key]')[0])
    arrow = dict(request.GET).get('params[2][key]')[0]
    user_id = int(dict(request.GET).get('params[1][user_id]')[0])
    lobby_id = int(dict(request.GET).get('params[0][lobby_id]')[0])

    # Update dict
    update_parsed_directions({user_id : arrow})
    # print('-' * 20 + str(user_id_arrow))
    return HttpResponse()


def update_parsed_directions(user_id_arr):
    user_id_arrow[list(user_id_arr.keys())[0]] = list(user_id_arr.values())[0]
