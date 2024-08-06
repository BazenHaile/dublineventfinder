# dublineventfinder/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Include URLs from the events app
    path('', include('events.urls')),

    # User authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='events/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # For other auth views
 
    # Redirect root URL to events app if needed
    # path('', RedirectView.as_view(pattern_name='event_list', permanent=False)),

    # Add any other project-wide URL patterns here
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
