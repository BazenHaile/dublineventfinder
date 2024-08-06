# This file defines custom permissions for our application

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Event

def create_event_permissions():
    # Get the content type for the Event model
    event_content_type = ContentType.objects.get_for_model(Event)
    
    # Create a new permission
    Permission.objects.get_or_create(
        # The codename is how we'll refer to this permission in our code
        codename='can_manage_all_events',
        # This is a human-readable name for the permission
        name='Can manage all events',
        # This links the permission to the Event model
        content_type=event_content_type,
    )

# This function needs to be called somewhere in your application setup
# (like in the app's ready() method) to actually create the permission