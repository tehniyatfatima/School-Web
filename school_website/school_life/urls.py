from django.urls import path
from .views import SchoolLifeView

urlpatterns = [
    path('', SchoolLifeView.as_view(), name='school_life'),
]
