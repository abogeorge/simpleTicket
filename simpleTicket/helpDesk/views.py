from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from siteEngine.models import Ticket, UserProfile, Order, TicketType, OrderType
from django.template import RequestContext
from siteEngine.validation_utils import *
from siteEngine.entities_utils import *

# Returns the user type for security purposes
def __get_user_role(request):
     # Retrieving user type
    user = request.user
    user_profile = user.userprofile
    user_role = get_user_type(user_profile)
    return user_role

# All Employees Page
@login_required
def employees(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving all Users Profile
    users_profile = get_employees()
    if len(users_profile) == 0:
        users_profile = False
    return render(request, "employees.html", {'employees':users_profile, 'user_role':user_role})

# All closed tickets page
@login_required
def closed_tickets(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving all Users Profile
    tickets = Ticket.objects.filter(status = 3)
    if len(tickets) == 0:
        tickets = False
    return render(request, "closed_tickets.html", {'tickets':tickets, 'user_role':user_role})

# All closed orders page
@login_required
def closed_orders(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving all Users Profile
    orders = Order.objects.filter(status = 3)
    if len(orders) == 0:
        orders = False
    return render(request, "closed_orders.html", {'orders':orders, 'user_role':user_role})
