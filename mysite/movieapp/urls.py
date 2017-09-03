from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='movie_list', permanent=False), name='index'),
    url(r'^movies$', views.MovieList.as_view(), name='movie_list'),
    url(r'^movies/create$', views.MovieCreate.as_view(), name='movie_create'),
    url(r'^movies/(?P<pk>\d+)$', views.MovieDetail.as_view(), name='movie_detail'),
    url(r'^movies/(?P<pk>\d+)/update', views.MovieUpdate.as_view(), name='movie_update'),

    url(r'^actors$', views.ActorList.as_view(), name='actor_list'),
    url(r'^actors/create$', views.ActorCreate.as_view(), name='actor_create'),
    url(r'^actors/(?P<pk>\d+)$', views.ActorDetail.as_view(), name='actor_detail'),
    url(r'^actors/(?P<pk>\d+)/update', views.ActorUpdate.as_view(), name='actor_update'),
]