from rest_framework import serializers
from .models import (
    loungesPlaceDes,
    loungesPlaceImage,
    loungesPlaceHighlight,
    loungesPlaceOffer
)


class loungesPlaceDesSerializer(serializers.ModelSerializer):
    class Meta:
        model = loungesPlaceDes
        fields = ["id", "title", "description"]


class loungesPlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = loungesPlaceImage
        fields = ["id", "place", "image"]


class loungesPlaceHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = loungesPlaceHighlight
        fields = ["id", "title", "sub_title", "icon"]


class loungesPlaceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = loungesPlaceOffer
        fields = ["id", "name", "icon"]
