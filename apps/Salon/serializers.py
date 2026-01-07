from rest_framework import serializers
from .models import (
    SalonPlaceDes,
    SalonPlaceImage,
    SalonPlaceHighlight,
    SalonPlaceOffer
)


class SalonPlaceDesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonPlaceDes
        fields = ["id", "title", "description"]


class SalonPlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonPlaceImage
        fields = ["id", "place", "image"]


class SalonPlaceHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonPlaceHighlight
        fields = ["id", "title","sub_title", "icon"]


class SalonPlaceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalonPlaceOffer
        fields = ["id", "name", "icon"]
