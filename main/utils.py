# 
def user_listing_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.seller.id}/listings/{filename}'