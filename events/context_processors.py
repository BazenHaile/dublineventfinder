# events/context_processors.py

from .models import Message

def unread_messages(request):
    """
    Context processor to add the count of unread messages to every RequestContext.
    """
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(receiver=request.user, read=False).count()
        return {'unread_messages_count': unread_count}
    return {'unread_messages_count': 0}