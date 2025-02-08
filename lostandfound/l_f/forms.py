from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['name', 'email', 'phone', 'title', 'description', 'image']
