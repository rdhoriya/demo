from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, CommentsViewSet, RestaurantsViewSet, NearByRestaurantsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'near-by-restaurants', NearByRestaurantsViewSet, basename='Restaurants')

urlpatterns = [
    path('', include(router.urls)),
]