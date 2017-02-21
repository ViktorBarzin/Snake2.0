from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from authentication.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from lobby.models import Profile
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.


def register_view(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            # TODO: hash password!
            # form.save()
            user = Profile.objects.create_user(username=form.data.get('username',''),
                email=form.data.get('email', ''),
                password=form.data.get('password', '')
            )
            user.save()
            # return HttpResponse('ok')

            return HttpResponseRedirect(reverse('login'))

        # If form is not valid post errors
    status_message = 'Something went wrong while registering you!'
    form = RegistrationForm()
    return render(request, 'registration/registration_form.html', locals())


def login(request):
    if request.method == 'POST':
        # user = User.objects.filter(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)

            # Check if redirection is needed
            redirect_url = request.GET.get('next')
            if redirect_url:
                return HttpResponseRedirect(redirect_url)

            return HttpResponseRedirect(reverse('baseapp:index'))
        return HttpResponse('nema takav')
    form = LoginForm()
    return render(request, 'registration/login.html', locals())

