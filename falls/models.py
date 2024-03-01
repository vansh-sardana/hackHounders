# falls/models.py
from django.db import models

class FallDetection(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    heartbeat=models.IntegerField()

    def __str__(self):
        return f"Fall at {self.date_time} - {self.location} (Heartbeat: {self.heartbeat})"

