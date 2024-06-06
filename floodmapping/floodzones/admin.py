from django.contrib import admin

from .models import FloodImage, Comment

@admin.register(FloodImage)
class FloodImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude', 'uploaded_at', 'taken_at')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('flood_image', 'user', 'comment', 'created_at')
    search_fields = ('comment',)