from django.conf.urls import url
from baseapp import views as baseapp_views

urlpatterns = [
    url(r'^$', baseapp_views.index, name='index'),
]
