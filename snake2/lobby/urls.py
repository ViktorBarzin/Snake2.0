from django.conf.urls import url, include
from lobby import views as lobby_views


urlpatterns = [
    url(r'^(?P<lobby_id>[0-9]+)$', lobby_views.index, name='lobby'),
    url(r'new/', lobby_views.create_lobby, name='new'),
    url(r'delete/(?P<lobby_id>[0-9]+)$', lobby_views.delete_lobby),
    url(r'users/', lobby_views.get_lobby_users, name='users'),
]
