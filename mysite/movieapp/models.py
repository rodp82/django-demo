# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor, through='Cast')

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.movie, self.actor)