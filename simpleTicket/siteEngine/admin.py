from django.contrib import admin
from .models import UserProfile
from .models import Role

class RoleAdmin(Role):
    fields = ['role_description']
    list_display = ('role_description', 'role')

admin.site.register(UserProfile)
admin.site.register(Role)