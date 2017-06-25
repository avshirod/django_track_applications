__author__ = 'chintanpanchamia, avshirod'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
