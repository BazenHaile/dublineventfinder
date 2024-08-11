from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_permissions(sender, **kwargs):
    from .permissions import create_event_permissions
    create_event_permissions()

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        post_migrate.connect(create_permissions, sender=self)