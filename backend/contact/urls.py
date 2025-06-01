from django.urls import path
from .views import ContactView
from django.contrib import admin
from .views import health_check 

urlpatterns = [
    path('contact/', ContactView.as_view(), name='api-contact'),
    path('ping/', health_check), 
    path('admin/', admin.site.urls),
]