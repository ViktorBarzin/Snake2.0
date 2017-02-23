from django.conf.urls import url
from game import views as game_views

urlpatterns = [
        url('^$', game_views.index, name='game'),
        url(r'get_arrows_ajax', game_views.get_arrows_ajax)
]
