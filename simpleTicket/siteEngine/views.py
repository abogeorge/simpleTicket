from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Ticket, UserProfile, Order, TicketType
from django.core.mail import send_mail
from django.template import RequestContext

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

# 404 Handler
def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

# Services Page
@login_required
def services(request):
    return render(request, "services.html")

# Create a Ticket Page
@login_required
def create_ticket(request):
    if request.method == "POST":
        # Validation Flag
        valid = True
        # Collecting Form Data
        title = request.POST.get("title")
        valid = __validateMinCharLength(title)
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        type = request.POST.get("type")
        # Retrieving Ticket Type
        try:
            ticket_type = TicketType.objects.get(pk=int(type))
        except TicketType.DoesNotExist:
            valid = False
        # Retrieving User Profile
        user = request.user
        try:
            user_profile = user.userprofile
        except UserProfile.DoesNotExist:
            valid = False
        if valid is True:
            ticket = Ticket.objects.create(
                title = title,
                description = description,
                comments = "-",
                priority = int(priority),
                status = 0,
                ticket_type = ticket_type,
                user_type = user_profile
            )
            return render(request, "ticketcreate.html", {'sent':True})
        else:
            fail_message = "Invalid data provided, please try again! The title of the ticket must be at least 5 characters long."
            return render(request, "ticketcreate.html", {'sent':False, 'fail_message':fail_message})
    else:
        return render(request, "ticketcreate.html")

# Checks if the
def __validateMinCharLength(field):
    if len(field) >= 5:
        return True
    else:
        return False
