from django.db import models
from users.models import Profile, Location
import uuid
from .consts import CAR_BRANDS, TRANSMISSIONS_OPTIONS
from .utils import user_listing_path
# Create your models here.
class Listing(models.Model):
    # create our unique id for each listing, insted of using id field
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    # Define the fields for the Listing model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKey to the User model (assuming you are using Django's built-in User model)
    # This creates a many-to-one relationship with the User model
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, choices=CAR_BRANDS)
    model = models.CharField(max_length=64)
    vin = models.CharField(max_length=17, unique=True)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24, default='white')
    discription = models.TextField(blank=True, null=True)
    engine = models.CharField(max_length=64)
    transmission = models.CharField(max_length=24, choices=TRANSMISSIONS_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=user_listing_path, blank=True, null=True)

    def __str__(self):
        return f'{self.seller.user.username}\'s listing - {self.model}'
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.listing.model} listing liked by {self.profile.user.username}'
    