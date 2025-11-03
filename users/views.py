from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserForm, ProfileForm, LocationForm
from main.models import Listing, LikedListing

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You now logging as {username}!, Welcome')
                # User is authenticated, log them in
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'views/login.html', {'login_form': login_form})

# logout view
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
# Register view
class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        print(register_form.__class__)
        if register_form.is_valid():
            user = register_form.save()
            # Automatically log in the user after registration
            user.refresh_from_db()
            login(request, user)
            # Optionally, you can add a success message
            messages.success(request, f'Account created for {user.username}! And you are logged in now.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
        return render(request, 'views/register.html', {'register_form': register_form})
    
# profile view
# if we use class based view, we need to use this line instead of the line @login_required
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        
        return render(request, 'views/profile.html', {'user_form': user_form,
                                                      'profile_form': profile_form,
                                                      'location_form': location_form,
                                                      'user_listings': user_listings,
                                                      'user_liked_listings': user_liked_listings,
                                                      })
        
    def post(self, request):
        user_listings = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)

        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            # Redirect to the profile page after a successful save
            return redirect('profile') # <-- ADD THIS LINE
        else:
            # If forms are invalid, re-render the page with the forms containing the errors
            messages.error(request, 'Error Updating Profile. Please check the errors below.')

        # This part will now only be reached if the forms are invalid
        return render(request, 'views/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'location_form': location_form,
            'user_listings': user_listings,
            'user_liked_listings': user_liked_listings,
        })
