from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class CustomPictureImageFieldWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer=renderer)
        img_html = ''
        
        if value:  # Check if value exists (could be a string path or FieldFile)
            try:
                # Handle both string paths and FieldFile objects
                if hasattr(value, 'url'):
                    img_url = value.url  # FieldFile object
                else:
                    # Ensure MEDIA_URL is properly appended to the string path
                    img_url = f"{settings.MEDIA_URL}{value}"
                
                img_html = f'<img src="{img_url}" width="200" style="display:block;margin-bottom:10px;" />'
            except Exception:
                # Fallback to raw value if URL construction fails
                img_html = f'<p>Current: {value}</p>'
                
        return mark_safe(f'{img_html}{input_html}')