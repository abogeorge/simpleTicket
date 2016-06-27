from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from siteEngine.models import Ticket, UserProfile, Order, TicketType, OrderType
from django.template import RequestContext
from siteEngine.validation_utils import *
from siteEngine.entities_utils import *

# All Employees Page
@login_required
def employees(request):
    # Retrieving user type
    user = request.user
    user_profile = user.userprofile
    user_role = get_user_type(user_profile)
    # Retrieving all Users Profile
    users_profile = get_employees()
    if len(users_profile) == 0:
        users_profile = False
    return render(request, "employees.html", {'employees':users_profile, 'user_role':user_role})