from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  # Change subalterns open orders status
  url(r'^employees/$', views.employees, name='employees'),
]