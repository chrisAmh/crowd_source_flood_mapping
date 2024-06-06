from django.shortcuts import render, redirect
from .models import FloodImage, Comment
from .forms import ImageUploadForm

def display_map(request):
    images = FloodImage.objects.all()
    return render(request, 'floodzones/map.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('map')
    else:
        form = ImageUploadForm()
    return render(request, 'floodzones/upload.html', {'form': form})

def image_detail(request, image_id):
    image = FloodImage.objects.get(id=image_id)
    comments = image.comments.all()
    return render(request, 'floodzones/image_detail.html', {'image': image, 'comments': comments})
