# falls/urls.py
# falls/urls.py
from django.urls import path
from . import views
from .views import home

from .views import emergency_contacts, add_emergency_contact,update_emergency_contact,delete_emergency_contact
app_name = 'falls'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('emergency-contacts/', emergency_contacts, name='emergency_contacts'),
    path('add-emergency-contact/', add_emergency_contact, name='add_emergency_contact'),
    path('update-emergency-contact/<int:pk>/', update_emergency_contact, name='update_emergency_contact'),
    path('delete-emergency-contact/<int:pk>/', delete_emergency_contact, name='delete_emergency_contact'),
]

