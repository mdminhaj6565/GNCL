from rest_framework import serializers
from .models import (
    PlaceDes,
    PlaceImage,
    PlaceHighlight,
    PlaceOffer
)


class PlaceDesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceDes
        fields = ["id", "title", "description"]


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ["id", "place", "image"]


class PlaceHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceHighlight
        fields = ["id", "title", "sub_title", "icon"]


class PlaceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOffer
        fields = ["id", "name", "icon"]
