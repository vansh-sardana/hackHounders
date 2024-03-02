"""
URL configuration for fall_detection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from falls import views
from django.contrib.auth.views import LoginView


from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from falls.views import emergency_contacts, add_emergency_contact, update_emergency_contact, delete_emergency_contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    path('falls/', include('falls.urls')),
    
     path('emergency-contacts/', emergency_contacts, name='emergency_contacts'),
    path('add-emergency-contact/', add_emergency_contact, name='add_emergency_contact'),
    path('update-emergency-contact/<int:pk>/', update_emergency_contact, name='update_emergency_contact'),
    path('delete-emergency-contact/<int:pk>/', delete_emergency_contact, name='delete_emergency_contact'),
    path('nearby-hospitals/', views.nearby_hospitals, name='nearby_hospitals'),
    path('<path:undefined_path>/', views.handle_undefined_path, name='handle_undefined_path'),
    
]


