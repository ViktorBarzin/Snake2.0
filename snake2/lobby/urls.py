from django.conf.urls import url, include
from lobby import views as lobby_views


urlpatterns = [
    url(r'^$', lobby_views.index, name='lobby')
]
