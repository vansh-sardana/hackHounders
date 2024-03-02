# admin.py


# Register the custom admin class for your custom user model
# falls/admin.py

from django.contrib import admin
from .models import CustomUser, EmergencyContact

admin.site.register(CustomUser)
admin.site.register(EmergencyContact)


