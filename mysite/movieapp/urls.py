from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MovieList.as_view(), name='movie_list'),
    url(r'^(?P<pk>\d+)$', views.MovieDetail.as_view(), name='movie_detail'),
]