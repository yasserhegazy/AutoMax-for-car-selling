from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Listing, LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django.core.paginator import Paginator

def main_view(request):
    return render(request, 'views/main.html', {"name": "User"})

@login_required
def home_view(request):
    page = request.GET.get('page')
    sort = request.GET.get('sort', '-created_at')
    
    valid_sorts = {
        'price_asc': 'price',
        'price_desc': '-price',
        'newest': '-created_at',
        'oldest': 'created_at',
        'mileage': 'mileage',
    }
    order_by = valid_sorts.get(sort, '-created_at')
    
    listing_filter = ListingFilter(request.GET, queryset=Listing.objects.all().order_by(order_by))
    filtered_listings = listing_filter.qs

    # Apply pagination after filtering
    paginator = Paginator(filtered_listings, 6)
    page_obj = paginator.get_page(page)

    # Get liked listings by current user
    user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).values_list('listing', flat=True)

    context = {
        'listing_filter': listing_filter,
        'page_obj': page_obj,
        'liked_listings_ids': list(user_liked_listings),
        'current_sort': sort,
    }
    return render(request, 'views/home.html', context)


@login_required
def list_view(request):
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, request.FILES)
        location_form = LocationForm(request.POST)
        if listing_form.is_valid() and location_form.is_valid():
            listing = listing_form.save(commit=False)
            listing_location = location_form.save()
            listing.seller = request.user.profile
            listing.location = listing_location
            listing.save()
            messages.info(request, f'{listing.model} Listing Posted Successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form': location_form})
@login_required
def listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'views/listing.html', {'listing': listing})

@login_required
def edit_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        listing_form = ListingForm(request.POST, request.FILES, instance=listing)
        location_form = LocationForm(request.POST, instance=listing.location)
        if listing_form.is_valid() and location_form.is_valid():
            listing_form.save()
            location_form.save()
            messages.success(request, f'Listing updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while trying to edit the listing.')
    else:
        listing_form = ListingForm(instance=listing)
        location_form = LocationForm(instance=listing.location)
    return render(request, 'views/edit.html', {
        'listing_form': listing_form,
        'location_form': location_form,
    })
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
        email_subject = f'{request.user.username} is interested in {listing.model}'
        email_message = f'Hi {listing.seller.user.username}, {request.user.username} is interested in your {listing.model} listing on AutoMax.'
        send_mail(email_subject, email_message, 'noreply@automax.com', [listing.seller.user.email], fail_silently=True)
        return JsonResponse({"success": True})
    except Exception:
        return JsonResponse({"success": False, "info": "Failed to send email."}, status=500)

@login_required
def delete_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    if listing.seller.user != request.user:
        messages.error(request, 'You can only delete your own listings.')
        return redirect('home')
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Listing deleted successfully.')
        return redirect('home')
    return redirect('listing', id=id)
        