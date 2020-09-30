from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer, RestaurantsSerializer, CommentsSerializer
from .models import Comments, Restaurants, Users


def home(request):
    return render(request, 'base.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, edited or deleted.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed, created, edited or deleted.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class RestaurantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed, created, edited or deleted.
    """
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


class NearByRestaurantsViewSet(viewsets.ModelViewSet):
    """
    List all near by restaurants by nearest landmark
    """
    serializer_class = RestaurantsSerializer

    def get_queryset(self):
        return Restaurants.objects.filter(landmark=self.request.user.landmark)
