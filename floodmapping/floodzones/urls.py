from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_map, name='map'),
    path('upload/', views.upload_image, name='upload_image'),
    path('image/<int:image_id>/', views.image_detail, name='image_detail'),
]
