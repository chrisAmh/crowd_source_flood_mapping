from django import forms
from .models import FloodImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = FloodImage
        fields = ['image', 'title', 'description', 'taken_at', 'latitude', 'longitude']
