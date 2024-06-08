


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('events/', include('events.urls')),
    path('school-life/', include('school_life.urls')),
    path('principal-message/', include('principal_msg.urls')),
    path('contact/', include('contact.urls')),
]

