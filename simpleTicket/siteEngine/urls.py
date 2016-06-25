from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  # Index Page
  url(r'^$', views.index, name='index'),
  # User auth Page
  url(r'^login/$', views.login, name='login'),
  url(r'^login_auth/$', views.login_auth, name="login_auth"),
  url(r'^logout/$', views.logout, name='logout'),
  # Account Information
  url(r'^myaccount/$', views.myaccount, name='myaccount'),
  # Contact Page
  url(r'^contact/$', views.contact, name='contact'),
  # Services Page
  url(r'^services/$', views.services, name='services'),
  # Create Ticket
  url(r'^ticketcreate/$', views.create_ticket, name='create_ticket'),
  # View Active Tickets
  url(r'^ticketsactive/$', views.active_tickets, name='active_tickets'),
  # View Closed Tickets
  url(r'^ticketsclosed/$', views.closed_tickets, name='closed_tickets'),
  # Create Order
  url(r'^ordercreate/$', views.create_order, name='create_order'),
  # View Active Orders
  #url(r'^ordersactive/$', views.active_orders, name='active_orders'),
]