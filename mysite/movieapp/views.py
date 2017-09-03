# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from .models import Movie


# Create your views here.
class MovieList(ListView):
    model = Movie
    context_object_name = 'movie_list'  # changes the name of default object_list name used in templates
