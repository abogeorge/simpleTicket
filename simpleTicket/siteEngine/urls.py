from django.conf.urls import patterns, url
from . import views

urlpatterns = [
  # Index Page
  url(r'^$', views.index, name='index'),
  # User auth Page
  url(r'^login/$', views.login, name='login'),
  url(r'^login_auth/$', views.login_auth, name="login_auth"),
  url(r'^logout/$', views.logout, name='logout'),
  # Account Information View
  url(r'^myaccount/$', views.myaccount, name='myaccount'),
  # Contact View
  url(r'^contact/$', views.contact, name='contact'),
]