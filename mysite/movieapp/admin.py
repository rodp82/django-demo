# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Movie, Cast, Actor


# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Cast)