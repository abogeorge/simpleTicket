from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')