from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from lobby.models import Lobby
# Create your views here.


@login_required(login_url='login')
def index(request, lobby_id):
    # The page includes a form to invite friends
    # if request.method == 'POST':
    #     invite_friends_link = create_invite_link()

    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    lobby = Lobby.objects.filter(id=lobby_id).first()
    if lobby is None:
        raise Http404('No such lobby')
    return render(request, 'lobby.html', locals())


@login_required(login_url='login')
def create_lobby(request):
    user = request.user
    try:
        lobby = Lobby.objects.create(is_full=False, owner=user)
        # lobby.users.append(user)
        lobby.save()
        # user.save()
    except IntegrityError:
       # return HttpResponseForbidden('You are not allowed to create more than 1 lobby!')
        lobby = Lobby.objects.filter(owner_id=user.id).first()
        import ipdb; ipdb.set_trace()# BREAKPOINT)

        return render(request, 'error_pages/delete_lobby.html', locals())
    return redirect(f'/lobby/{lobby.id}')


@login_required(login_url='login')
def delete_lobby(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).first()
    if lobby is not None:
        lobby.delete()
    else:
        raise ValueError(f'There is no lobby with id "{lobby_id}"')
    return HttpResponseRedirect(reverse('baseapp:index'))


# This view is for the "invite friends" link/button
@login_required(login_url='login')
def invite_friends(request, lobby_id):
    pass
