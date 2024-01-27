from django import forms
from .models import houses


class houseform(forms.ModelForm):
    class Meta:
        model = houses
        fields = ['title', 'price','state', 'location', 'area', 'rooms', 'bathrooms']
