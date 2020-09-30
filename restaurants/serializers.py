from rest_framework import serializers
from .models import Restaurants, Comments, Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['password', ]

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'