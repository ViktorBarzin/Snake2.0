from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from lobby.models import Lobby
# Create your views here.


@login_required(login_url='login')
def index(request):
    # import ipdb; ipdb.set_trace()# BREAKPOINT)
    lobbies = Lobby.objects.all()

    return render(request, 'index.html', locals())
