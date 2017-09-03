# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')


class ActorList(ListView):
    model = Actor
    context_object_name = 'actor_list'


class ActorDetail(DetailView):
    model = Actor
    context_object_name = 'actor'


class ActorCreate(CreateView):
    model = Actor
    fields = ['name']

    def get_context_data(self, **kwargs):
        """ Overrides the parent to get the context data and adds page_title to it """
        context = super(ActorCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Add Actor'
        return context


class ActorUpdate(UpdateView):
    model = Actor
    fields = ['name']

    def get_context_data(self, **kwargs):
        """ Overrides the parent to get the context data and adds page_title to it """
        context = super(ActorUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Actor'
        return context


class ActorDelete(DeleteView):
    model = Actor
    success_url = reverse_lazy('movie_list')