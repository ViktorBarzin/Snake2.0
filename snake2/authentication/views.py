from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from authentication.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
from django.contrib.auth import login as auth_login


def register_view(request):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()

        form = RegistrationForm(request.POST)
        if form.is_valid():
            # TODO: hash password!
            form.save()
            # return HttpResponse('ok')
            user = authenticate(username=form.data.get('username', ''), password=form.data.get('password', ''))

            return HttpResponseRedirect(reverse('login'))

        # If form is not valid post errors
    status_message = 'Something went wrong while registering you!'
    form = RegistrationForm()
    return render(request, 'registration/registration_form.html', locals())


def login(request):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        user = User.objects.filter(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
        # user = authenticate(user=request.POST.get('username', ''), password=request.POST.get('password', ''))
        if user:
            return HttpResponse('logna se')
        return HttpResponse('nema takav')
    form = LoginForm()
    return render(request, 'registration/login.html', locals())

