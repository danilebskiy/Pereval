from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class Pereval_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_images
        fields = ['date', 'title']


class Pereval_addedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'


class PerevalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'
        read_only_fields = ['users', ]
