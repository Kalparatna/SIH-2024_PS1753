from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),                   # Admin site
    path('admin_portal/', include(('admin_portal.urls', 'admin_portal'), namespace='admin_portal')),
    path('', include('admin_portal.urls')),           # Include admin_portal URLs
    path('routes/', RedirectView.as_view(url='routes/')),   # Redirect to the routes path if necessary
]
