from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    Lost = "Lost"
    Found = "Found"
    STATUS_CHOICES = [
        (Lost, "Lost"),
        (Found, "Found")
    ]

    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=255)
    description = models.TextField()
    dateReported = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to= 'item_photos/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=Lost)
    contactInfo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.itemName} ({self.get_status_display()})"