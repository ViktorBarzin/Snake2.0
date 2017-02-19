from django.conf.urls import url, include
# from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from authentication.views import register_view, login

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'register/$', register_view, name='register'),
    url(r'logout/$', auth_logout, name='logout'),
]
