from django.contrib.auth.models import User
from .models import Profile, Location
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Signal to create the Profile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to create the Location when a Profile is created
@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        location = Location.objects.create()  # ✅ No profile field
        instance.location = location
        instance.save()
        
# Signal to delete the Location when the Profile is deleted
@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, **kwargs):
    if instance.location:
        instance.location.delete()
