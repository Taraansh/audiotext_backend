from .models import Audio, Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'
