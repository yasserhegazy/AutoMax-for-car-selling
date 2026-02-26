from django import forms 
from .models import Location, Profile
from localflavor.us.forms import USZipCodeField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .widgets import CustomPictureImageFieldWidget


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a username',
            'class': 'form-control',
        }),
        help_text='',
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a password',
            'class': 'form-control',
        }),
        help_text='',
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
            'class': 'form-control',
        }),
        help_text='',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name',}
    
class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.CharField(widget=forms.Textarea)  # Changed to CharField with Textarea
    
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')
        
class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)
    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'} 
        