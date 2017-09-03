# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from .models import Movie, Actor


# Create your views here.
class MovieList(ListView):
    model = Movie
    context_object_name = 'movie_list'  # changes the name of default object_list name used in templates


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'


class ActorList(ListView):
    model = Actor
    context_object_name = 'actor_list'


class ActorDetail(DetailView):
    model = Actor
    context_object_name = 'actor'
