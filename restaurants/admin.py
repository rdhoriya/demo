from django.contrib import admin
from .models import Comments, Restaurants

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'restaurant', 'user', 'added_time')

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'landmark', 'city')
