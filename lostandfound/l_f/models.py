from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="lost_items/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.name}"
