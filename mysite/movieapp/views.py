# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView

from .models import Movie, Actor


# Create your views here.
class MovieList(ListView):
    model = Movie
    context_object_name = 'movie_list'  # changes the name of default object_list name used in templates


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'year']

    def get_context_data(self, **kwargs):
        """ Overrides the parent to get the context data and adds page_title to it """
        context = super(MovieCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Add Movie'
        return context


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'year']

    def get_context_data(self, **kwargs):
        """ Overrides the parent to get the context data and adds page_title to it """
        context = super(MovieUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Movie'
        return context


class ActorList(ListView):
    model = Actor
    context_object_name = 'actor_list'


class ActorDetail(DetailView):
    model = Actor
    context_object_name = 'actor'
