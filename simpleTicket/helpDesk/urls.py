from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  # View all employees
  url(r'^employees/$', views.employees, name='employees'),
  # View all closed tickets
  url(r'^closed_tickets/$', views.closed_tickets, name='closed_tickets'),
  # View all closed orders
  url(r'^closed_orders/$', views.closed_orders, name='closed_orders'),
]