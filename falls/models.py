# falls/models.py
from django.db import models
from django.contrib.auth.models import User

class FallDetection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    heartbeat=models.IntegerField(default=0)

    def __str__(self):
        return f"Fall at {self.date_time} - {self.location} (Heartbeat: {self.heartbeat})"




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the user profile
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    # address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
from django.db import models

class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
