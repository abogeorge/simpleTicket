from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  # View all employees
  url(r'^employees/$', views.employees, name='employees'),
  # View all closed tickets
  url(r'^closed_tickets/$', views.closed_tickets, name='closed_tickets'),
  # View all closed orders
  url(r'^closed_orders/$', views.closed_orders, name='closed_orders'),
  # View all active tickets
  url(r'^active_tickets/$', views.active_tickets, name='active_tickets'),
  # Change active ticket status view
  url(r'^active_tickets_cs/$', views.active_tickets_cs, name='active_tickets_cs'),
  # View all active orders
  url(r'^active_orders/$', views.active_orders, name='active_orders'),
  # Change active order status view
  url(r'^active_orders_cs/$', views.active_orders_cs, name='active_orders_cs'),
]