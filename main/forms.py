from django import forms 
from .models import Listing

class ListingForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:  # Corrected from 'Mete' to 'Meta'
        model = Listing
        fields = ['brand', 'model', 'year', 'price', 'vin', 'mileage', 'color', 'description', 'engine', 'transmission', 'image']
