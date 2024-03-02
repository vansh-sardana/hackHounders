# falls/models.py
from django.db import models# falls/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    # Your custom fields go here
    custom_field1 = models.CharField(max_length=255)
    custom_field2 = models.IntegerField()

    # Override related names to avoid clashes
    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True)

    def __str__(self):
        return self.username  # Adjust as per your requireme
class FallDetection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    heartbeat = models.IntegerField(default=0)

    def __str__(self):
        return f"Fall at {self.timestamp} - {self.location} (Heartbeat: {self.heartbeat})"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add any additional fields you need for the user profile
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    # address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
