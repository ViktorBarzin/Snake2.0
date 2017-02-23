from django.shortcuts import render, reverse, redirect
<<<<<<< HEAD
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, JsonResponse
=======
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponseBadRequest
>>>>>>> da5f639aa261d478619a0bf8a1465f7804213281
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
# from django.utils import simplejson
from django.core import serializers
import json


from lobby.models import Lobby
# Create your views here.


@login_required(login_url='login')
def index(request, lobby_id):
    # The page includes a form to invite friends
    # if request.method == 'POST':
    #     invite_friends_link = create_invite_link()

    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    user = request.user
    lobby = Lobby.objects.filter(id=lobby_id).first()
    if lobby is None:
        raise Http404('No such lobby')
    if isinstance(user, User):
        join_lobby(user, lobby)
    users = lobby.users.all()
    return render(request, 'lobby.html', locals())


@login_required(login_url='login')
def create_lobby(request):
    user = request.user
    try:
        # lobby = Lobby.objects.create(is_full=False, owner=user.profile, users = [user.profile])
        lobby = Lobby.objects.create(is_full=False, owner=user.profile)
        # import ipdb; ipdb.set_trace()# BREAKPOINT)
        # Check if user is already in lobby
        join_lobby(user, lobby)

        lobby.save()
        # user.save()
    except IntegrityError:
       # return HttpResponseForbidden('You are not allowed to create more than 1 lobby!')
        lobby = Lobby.objects.filter(owner_id=user.id).first()
        # import ipdb; ipdb.set_trace()# BREAKPOINT)
        return render(request, 'error_pages/delete_lobby.html', locals())
    else:
        # import ipdb; ipdb.set_trace()# BREAKPOINT)
        # join_lobby(user, lobby)
        pass

        return redirect('/lobby/{}'.format(lobby.id))


# This is actually when user leaves lobby, not neccesasri delete lobby
@login_required(login_url='login')
def leave_lobby_view(request, lobby_id):
    # import ipdb; ipdb.set_trace()
    user = request.user
    lobby = Lobby.objects.filter(id=lobby_id).first()
    leave_lobby(user, lobby)
    # if lobby is not None:
    #     lobby.delete()

    # else:
    #     raise ValueError('There is no lobby with id "{}"'.format(lobby.id))
    return HttpResponseRedirect(reverse('baseapp:index'))


# This view is for the "invite friends" link/button
@login_required(login_url='login')
def invite_friends(request, lobby_id):
    pass


def join_lobby(user, lobby):
    # import ipdb; ipdb.set_trace()

    if user not in lobby.users.all(): # and user != lobby.owner:
        lobby.users.add(user.profile)
        return 0
    # User is in lobby and no need to join again

def leave_lobby(user, lobby):
    if user.profile in lobby.users.all():
        if user.profile not in lobby.users.all():
            raise ValueError('Cannot remove this user form the lobby because he has not joined it!')
        else:
            # import ipdb; ipdb.set_trace()

            lobby.users.remove(user.profile)

        if len(lobby.users.all()) == 0:
            lobby.delete()


def get_users_in_lobby_ajax(request):
    lobby_id = request.GET.get('lobby_id')
    if not lobby_id:
        return HttpResponseBadRequest
    lobby_id = int(lobby_id)
    lobby = Lobby.objects.filter(id = lobby_id).first()

    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    # have to append username manually because it is in the django User model
    # and lobby.users are my custom user model
    users = lobby.users.all()
    # for user in users:
    #     user.set_field({'profile_username': user.username})
    usernames = [{"user":x.username}  for x in lobby.users.all()]
    # [{user:"username"}, {user:"username"}]
    # data = serializers.serialize('json', usernames)
    data = json.dumps(usernames)
    # data = []
    # if len(usernames) == 1:
    #     data.append(usernames)
    # else:
    #     for username in usernames:
    #         data.append(username)
    # data = json.dumps(usernames)
    # return HttpResponse(simplejson.dumps({'foo':'bar'}), mimetype='application/json')
    return HttpResponse(data)
