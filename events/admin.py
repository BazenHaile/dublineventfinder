# This file customizes the Django admin interface for our application

from django.contrib import admin
from .models import Event, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register the Event model with the admin site
# This allows us to manage Event objects through the admin interface
admin.site.register(Event)

# This class customizes how our CustomUser model appears in the admin interface
class CustomUserAdmin(BaseUserAdmin):
    # Add our custom fields to the default user fields in the admin
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture', 'bio', 'contact_phone', 'saved_events')}),
    )
    
    # Also add our custom fields to the "add user" form in the admin
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_picture', 'bio', 'contact_phone', 'saved_events')}),
    )

# Register our CustomUser model with the admin site, using our custom admin class
admin.site.register(CustomUser, CustomUserAdmin)