from django.urls import path
from .views import ContactView, health_check 

urlpatterns = [
    path('ping/', health_check, name='ping'),
    path('health/', health_check, name='health_check'),
    path('contact/', ContactView.as_view(), name='api-contact'),
]