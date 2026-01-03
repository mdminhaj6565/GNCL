from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import (
    Moments , MomentImage,
    Signature, SignatureImage,
    Memories, MemoriesImage,
    Dining, DiningImage
)

class DiningPagination(PageNumberPagination):
    page_size = 5  # 5 dining image 
    page_size_query_param = 'page_size'
    max_page_size = 50

# Moments section
class MomentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentImage
        fields = '__all__'

class  MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'

# Signature section
class SignatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignatureImage
        fields = ["id", "signature_image"]


class SignatureSerializer(serializers.ModelSerializer):
    signature_images = SignatureImageSerializer(many=True, read_only=True)

    class Meta:
        model = Signature
        fields = ["id", "title", "sub_title", "signature_images"]


# Memories section
class MemoriesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoriesImage
        fields = ["id", "memories_image"]


class MemoriesSerializer(serializers.ModelSerializer):
    memory_images = MemoriesImageSerializer(many=True, read_only=True)

    class Meta:
        model = Memories
        fields = ["id", "memories_title", "memories_sub_title", "memory_images"]


# Dining section
class DiningImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningImage
        fields = ["id", "dining_image"]

class DiningSerializer(serializers.ModelSerializer):
    dining_images = DiningImageSerializer(many=True, read_only=True)

    class Meta:
        model = Dining
        fields = ['id', 'dining_title', 'dining_sub_title', 'dining_images'] 


