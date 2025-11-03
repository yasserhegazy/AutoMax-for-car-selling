from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Listing, LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django.core.paginator import Paginator  # Fixed typo
from django.core.serializers import serialize
# Create your views here.
# responsible for rendering the pages of the application
# This file contains the views for the main application
# It handles the logic for displaying the home page and other views
def main_view(request):
    # return HttpResponse("<h1>Welcome to the AutoMax application!</h1>")
    # by using render function we can render the template
    return render(request, 'views/main.html', {"name" : "User"})  # Render the home template

@login_required
def home_view(request):
    page = request.GET.get('page')
    
    # Apply filtering first
    listing_filter = ListingFilter(request.GET, queryset=Listing.objects.all())
    filtered_listings = listing_filter.qs

    # Apply pagination after filtering
    paginator = Paginator(filtered_listings, 3)
    page_obj = paginator.get_page(page)

    # Get liked listings by current user
    user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing', flat=True)

    context = {
        'listing_filter': listing_filter,
        'page_obj': page_obj,
        'liked_listings_ids': list(user_liked_listings),
    }
    return render(request, 'views/home.html', context)


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST, )
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('home')

        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form, })
@login_required
def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html/', {'listing': listing,})        
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing')
        return redirect('home')

@login_required
def edit_view(request, id):
    try: 
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception()
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save()
                location_form.save()
                messages.success(request, f'Listing {id} updatied successfully!')
                return redirect('home')
            else:
                messages.error(request, f'An error occured while trying to edit the listing {id}!')
                return redirect('edit', id=id)
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        context = {
            'listing_form': listing_form,
            'location_form': location_form,
        }
        return render(request, 'views/edit.html', {'context': context,})
    except Exception as e:
        messages.error(request, f'An error occured while trying to edit the listing {id}!')
        return redirect('home')
@login_required
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    liked_listing, created = LikedListing.objects.get_or_create(profile=request.user.profile, listing=listing)
    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    return JsonResponse({
        'is_liked_by_user': created,
    })
  
@login_required
def inquire_listing_using_email(request, id):
    listing = get_object_or_404(Listing, id=id)
    try:
        emailSubject = f'{request.user.username} is intersted in {listing.model}'
        emailMessage = f'Hi, {listing.seller.user.username}, {request.user.username} is intersted in your {listing.model} listing on AutoMax'
        send_mail(emailSubject, emailMessage, 'noreply@automax.com', [listing.seller.user.email], fail_silently=True)
        return JsonResponse({
            "success": True,
        })
    except Exception as e:
        return JsonResponse({
            "success": False,
            "info": e,
        })
        