# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
# def home(request):
#     tplVars = {'message': 'Welcome'}
#     return render(request, 'main/home.html', tplVars)
#
# def page1(request):
#     return render(request, 'main/page1.html')
#
# def page2(request):
#     return render(request, 'main/page2.html')

class Home(View):
    def get(self, request):
        tplVars = {'message': 'Welcome'}
        return render(request, 'main/home.html', tplVars)


class PageOne(View):
    def get(self, request):
        return render(request, 'main/page1.html')


class PageTwo(View):
    def get(self, request):
        return render(request, 'main/page2.html')
