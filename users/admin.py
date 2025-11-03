from django.contrib import admin
from .models import Profile, Location
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass
# Register the Profile model with the admin site
# This code registers the Profile model with the Django admin site.
# It allows the Profile model to be managed through the admin interface.
admin.site.register(Profile, ProfileAdmin)


# Register the Location model with the admin site
# This code registers the Location model with the Django admin site.
# It allows the Location model to be managed through the admin interface.
admin.site.register(Location, LocationAdmin)