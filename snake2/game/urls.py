from django.conf.urls import url
from game import views as game_views

urlpatterns = [
        url('^$', game_views.index, name='game'),
        url(r'get_arrows_ajax', game_views.get_arrows_ajax, name='get_arrows'),
        url(r'update_game_ajax', game_views.update_game_field_ajax, name='update_game')
]
