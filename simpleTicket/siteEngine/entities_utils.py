from .models import Ticket, UserProfile, Order, TicketType, OrderType

# Retrieving user profile for the specified user
def get_profile_for_user(user):
    try:
        user_profile = user.userprofile
        return user_profile
    except UserProfile.DoesNotExist:
        return None

# Retrieving tickets for the specificied user profile
def get_tickets_for_user_profile(user_profile):
    tickets = Ticket.objects.filter(user_type = user_profile)
    if len(tickets) == 0:
        tickets = False
    return tickets

# Retrieving orders for the specified user profile
def get_orders_for_user_profile(user_profile):
    orders = Order.objects.filter(user_type = user_profile)
    if len(orders) == 0:
        orders = False;
    return orders

# Retrieving the total number of subalterns for a specific user profile
def get_subalterns_number(user_profile):
    subalterns = UserProfile.objects.filter(supervisor_user = user_profile)
    return len(subalterns)

# Retrieving a list of all subalterns for a specific user profile
def get_subalterns(user_profile):
    subalterns = UserProfile.objects.filter(supervisor_user = user_profile)
    return  subalterns

# Returns the type of the user:
# 0 - admin; 1 - user; 2 - helpdesk;
def get_user_type(user_profile):
    user_role = user_profile.role
    return user_role.role

# Returns all exmployees from the database
def get_employees():
    users = UserProfile.objects.all()
    return users

# Returns the id of the ticket with the specified title
def get_ticket_id_from_title(name):
    tickets = Ticket.objects.all()
    print ("\n\n\n")
    print ("Tickets: " + str(tickets))
    print ("Title: " + name)
    for ticket in tickets:
        print ("Ticket " + str(ticket.id) + ": " +ticket.title)
        if ticket.title == name:
            return ticket.id
    return False