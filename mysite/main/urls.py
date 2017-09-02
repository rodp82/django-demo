from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^page1$', views.page1, name='page1'),
    # url(r'^page2$', views.page2, name='page2'),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^page1$', views.PageOne.as_view(), name='page1'),
    url(r'^page2$', views.PageTwo.as_view(), name='page2')
]