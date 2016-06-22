from django.db import models
from django.contrib.auth.models import User

# Role Class
class Role(models.Model):
    # 0 - admin; 1 - user; 2 - helpdesk;
    role = models.IntegerField(default=1)
    role_description = models.CharField(max_length=100)
    def __unicode__(self):
        return self.role_description

# User Class
class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE)
    supervisor_user = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    def __unicode__(self):
       return self.user_auth.first_name + " " + self.user_auth.last_name

# Ticket Type Class
class TicketType(models.Model):
    # 0 - hardware problem; 1 - software; 2 - telecom; 3 - other problem
    ticket_type = models.IntegerField(default=0)
    ticket_description = models.CharField(max_length=100)

# Ticket Class
class Ticket(models.Model):
    ticket_type = models.ForeignKey('TicketType', on_delete=models.CASCADE)
    user_type = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    # 0 - low priority; 1 - medium; 2 - high
    priority = models.IntegerField(default=0)
    # 0 - sent; 1 - approved; 2 - processing; 3 - solved; 4 - reopened
    status = models.IntegerField(default=0)
    def __unicode__(self):
       return self.title

# Order Type Class
class OrderType(models.Model):
    # 0 - inventory item; 1 - project necessity; 2 - raw material; 3 - other
    order_type = models.IntegerField(default=1)
    order_description = models.CharField(max_length=100)

# Order Class
class Order(models.Model):
    order_type = models.ForeignKey('OrderType', on_delete=models.CASCADE)
    user_type = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    comments = models.CharField(max_length=250)
    value_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.IntegerField(default=1)
    delivery_office = models.CharField(max_length=50)
    # 0 - sent; 1 - approved; 2 - processing; 3 - solved; 4 - reopened
    status = models.IntegerField(default=0)