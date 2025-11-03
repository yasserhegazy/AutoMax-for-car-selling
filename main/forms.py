from django import forms 
from .models import Listing

class ListingForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:  # Corrected from 'Mete' to 'Meta'
        model = Listing
        fields = ['brand', 'model', 'vin', 'mileage', 'color', 'discription', 'engine', 'transmission', 'image']
