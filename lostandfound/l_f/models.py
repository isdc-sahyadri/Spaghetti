from django.db import models

class LostItem(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='lost_items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
