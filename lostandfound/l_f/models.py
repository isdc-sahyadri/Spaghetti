from django.db import models
from django.contrib.auth.models import User  

class LostItem(models.Model):
    STATUS_CHOICES = [
        ("lost", "Lost"),
        ("found", "Found"),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="lost_items"
    )  
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="lost_items/", blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="lost"
    )  # Status field for Lost/Found
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
