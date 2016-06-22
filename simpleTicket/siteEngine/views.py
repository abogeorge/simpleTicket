from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Ticket, UserProfile, Order
from django.core.mail import send_mail

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
        return render(request, "index.html")
    else:
        return render(request, "login.html", {'change_succeded':False})

# Logout view
def logout(request):
    auth.logout(request)
    return render(request, "login.html", {'change_succeded':True})

# Account Page
@login_required
def myaccount(request):
    # User Auth object
    user = request.user
    tickets = []
    orders = []
    # Retrieving User
    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None
    # Retrieving Tickets
    tickets = Ticket.objects.filter(user_type = user_profile)
    if len(tickets) == 0:
        tickets = False
    # Retrieving orders
    orders = Order.objects.filter(user_type = user_profile)
    if len(orders) == 0:
        orders = False;
    return render(request, "myaccount.html", {'user':user, 'user_profile':user_profile, 'tickets':tickets, 'orders':orders})

# Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        phone = request.POST.get("phone", "-")
        company_name = request.POST.get("company_name", "-")
        message = request.POST.get("message")
        send_message = "Message received from: " + name + "\n" \
                       + "Phone Number: " + phone + "\n" +  "Company: " + company_name + "\n" \
                       + "Message:\n" + message
        send_result = send_mail(
            subject,
            send_message,
            email,
            ['abordioaie.george@yahoo.com'],
            fail_silently=False,
        )
        if send_result == 1:
            return render(request, "contact.html", {'sent':True})
        else:
            return render(request, "contact.html", {'sent':False})
    else:
        return render(request, "contact.html")