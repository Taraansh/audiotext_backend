from models import Audio
from rest_framework import serializers

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Audio
        fields = '__all__'