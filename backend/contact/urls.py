from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='home'),        
    path('contact/', views.contact_view, name='contact'),  
]