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

# All active tickets page
@login_required
def active_tickets(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving all Users Profile
    tickets = Ticket.objects.exclude(status = 0).exclude(status = 3)
    if len(tickets) == 0:
        tickets = False
    # If the view is accessed as a POST request:
    if request.method == "POST":
        # Loop to identify the selected ticket
        for ticket in tickets:
            if str(ticket.id) in request.POST:
                # Add ticket to session request
                request.session['selected_ticket_hd'] = ticket.id
                # Load change status page if the ticket is identified
                # Change the status of the ticket as Processing
                ticket.status = 2
                ticket.save()
                return render(request, "active_tickets_cs.html", {'ticket':ticket, 'user_role':user_role})
        if len(tickets) == 0:
            tickets = False
        # Load the opened tickets page
        return render(request, "active_tickets.html", {'tickets':tickets, 'user_role':user_role})
    else:
        return render(request, "active_tickets.html", {'tickets':tickets, 'user_role':user_role})

# Change active ticket status
@login_required
def active_tickets_cs(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving ticket
    ticket_id = request.session.get('selected_ticket_hd')
    ticket = Ticket.objects.get(pk=ticket_id)
    status = request.POST.get("status")
    comments = request.POST.get("comments")
    ticket.status = status
    ticket.comments = comments
    ticket.save()
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, "active_tickets_cs.html", {'ticket':ticket, 'change_succeded':True, 'user_role':user_role})

# All active orders page
@login_required
def active_orders(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving all Users Profile
    orders = Order.objects.exclude(status = 0).exclude(status = 3)
    if len(orders) == 0:
        orders = False
    # If the view is accessed as a POST request:
    if request.method == "POST":
        # Loop to identify the selected ticket
        for order in orders:
            if str(order.id) in request.POST:
                # Add ticket to session request
                request.session['selected_order_hd'] = order.id
                # Load change status page if the order is identified
                # Change the status of the order as Processing
                order.status = 2
                order.save()
                return render(request, "active_orders_cs.html", {'order':order, 'user_role':user_role})
        if len(orders) == 0:
            orders = False
        # Load the opened tickets page
        return render(request, "active_orders.html", {'orders':orders, 'user_role':user_role})
    else:
        return render(request, "active_orders.html", {'orders':orders, 'user_role':user_role})

# Change active order status
@login_required
def active_orders_cs(request):
    # Retrieving user type
    user_role = __get_user_role(request)
    # Retrieving ticket
    order_id = request.session.get('selected_order_hd')
    order = Order.objects.get(pk=order_id)
    status = request.POST.get("status")
    comments = request.POST.get("comments")
    order.status = status
    order.comments = comments
    order.save()
    order = Order.objects.get(pk=order_id)
    return render(request, "active_orders_cs.html", {'order':order, 'change_succeded':True, 'user_role':user_role})