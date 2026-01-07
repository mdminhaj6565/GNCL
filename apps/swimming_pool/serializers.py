from rest_framework import serializers
from .models import (
    SwimmingPoolPlaceDes,
    SwimmingPoolPlaceImage,
    SwimmingPoolPlaceHighlight,
    SwimmingPoolPlaceOffer
)

class SwimmingPoolPlaceDesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingPoolPlaceDes
        fields = ["id", "title", "description"]


class SwimmingPoolPlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingPoolPlaceImage
        fields = ["id", "place", "image"]


class SwimmingPoolPlaceHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingPoolPlaceHighlight
        fields = ["id", "title", "sub_title", "icon"]


class SwimmingPoolPlaceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingPoolPlaceOffer
        fields = ["id", "name", "icon"]
