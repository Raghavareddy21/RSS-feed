from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^blogaggr', views.feed, name = 'feed'),
    url(r'^search', views.search, name = 'search'),

]
