from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'price_per_hour', 'available', 'image']

    image = forms.ImageField(required=False)