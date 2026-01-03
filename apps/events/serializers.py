from rest_framework import serializers
from .models import (
     HeroSection, HeroImage, 
     Events, EventsImage, 
)


# Hero Section Serializers
class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ['id', 'image']


class HeroSectionSerializer(serializers.ModelSerializer):
    images = HeroImageSerializer(many=True, read_only=True)

    class Meta:
        model = HeroSection
        fields = ['id', 'title', 'description', 'background_image', 'images']
        

#events sections
class EventsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsImage
        fields = ['id', 'images']


class EventsSerializer(serializers.ModelSerializer):
    images = EventsImageSerializer(source='eventsimage_set', many=True, read_only=True)

    class Meta:
        model = Events
        fields = ['id', 'title', 'sub_title', 'date', 'images']
