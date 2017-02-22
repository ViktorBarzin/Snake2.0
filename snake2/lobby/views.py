from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User

from lobby.models import Lobby
# Create your views here.


@login_required(login_url='login')
def index(request, lobby_id):
    # The page includes a form to invite friends
    # if request.method == 'POST':
    #     invite_friends_link = create_invite_link()

    import ipdb; ipdb.set_trace()# BREAKPOINT)
    user = request.user
    lobby = Lobby.objects.filter(id=lobby_id).first()
    if lobby is None:
        raise Http404('No such lobby')
    if isinstance(user, User):
        join_lobby(user, lobby)
        return render(request, 'lobby.html', locals())


@login_required(login_url='login')
def create_lobby(request):
    user = request.user
    try:
        import ipdb; ipdb.set_trace()# BREAKPOINT)
        lobby = Lobby.objects.create(is_full=False, owner=user.profile)
        lobby.save()
        # Check if user is already in lobby
        join_lobby(user, lobby)

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


@login_required(login_url='login')
def delete_lobby(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).first()
    if lobby is not None:
        import ipdb; ipdb.set_trace()
        if request.user.profile not in lobby.users.all():
            raise ValueError('Cannot remove this user form the lobby because he has not joined it!')
        else:
            leave_lobby(request.user, lobby)
        if len(lobby.users.all()) == 0:
            lobby.delete()

    else:
        raise ValueError('There is no lobby with id "{}"'.format(lobby.id))
    return HttpResponseRedirect(reverse('baseapp:index'))


# This view is for the "invite friends" link/button
@login_required(login_url='login')
def invite_friends(request, lobby_id):
    pass


# @login_required(login_url='login')
def join_lobby(user, lobby):
    import ipdb; ipdb.set_trace()

    if user not in lobby.users.all(): # and user != lobby.owner:
        lobby.users.add(user.profile)
        return 0
    # User is in lobby and no need to join again

def leave_lobby(user, lobby):
    if user.profile in lobby.users.all():
        import ipdb; ipdb.set_trace()

        lobby.users.remove(user.profile)
