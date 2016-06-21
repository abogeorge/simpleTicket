from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Home Page
@login_required
def index(request):
    return render(request, "index.html")

# Login view
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("login.html", c)

# Login authview
def login_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        #print("\n\n\n\n" + request.user.username + "\n\n\n\n")
        return render(request, "index.html")
    else:
        # c = {}
        # c.update(csrf(request))
        return render(request, "login.html", {'change_succeded':False})

# Logout view
def logout(request):
    auth.logout(request)
    # c = {}
    # c.update(csrf(request))
    return render(request, "login.html", {'change_succeded':True})