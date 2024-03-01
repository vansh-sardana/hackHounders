# falls/urls.py
# falls/urls.py
from django.urls import path
from . import views

app_name = 'falls'

urlpatterns = [
    path('', views.home, name='home'),
]
