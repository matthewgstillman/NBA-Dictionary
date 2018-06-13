from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^teams$', views.get_teams),
    url(r'^team_and_city$', views.team_and_city),
    url(r'^team_city_color$', views.team_and_city_color),
    url(r'^team_city_color_hex$', views.team_city_color_hex),
    url(r'^website$', views.website),
    url(r'^team_city_conf$', views.team_city_conf),
    url(r'^players$', views.players),
]