from django.urls import path
from .views import PrincipalMessageView

urlpatterns = [
    path('', PrincipalMessageView.as_view(), name='principal_message'),
]
