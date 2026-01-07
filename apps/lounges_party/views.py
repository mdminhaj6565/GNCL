from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    loungesPlaceDes,
    loungesPlaceImage,
    loungesPlaceHighlight,
    loungesPlaceOffer
)
from .serializers import (
    loungesPlaceDesSerializer,
    loungesPlaceImageSerializer,
    loungesPlaceHighlightSerializer,
    loungesPlaceOfferSerializer
)

# Create your views here.

class loungesPlaceDesListAPIView(APIView):
    def get(self, request):
        data = loungesPlaceDes.objects.all()
        serializer = loungesPlaceDesSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place description fetched successfully",
            "data": serializer.data
        })


class loungesPlaceImageListAPIView(APIView):
    def get(self, request, place_id):
        images = loungesPlaceImage.objects.filter(place_id=place_id)
        serializer = loungesPlaceImageSerializer(images, many=True)

        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place images fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class loungesPlaceHighlightListAPIView(APIView):
    def get(self, request):
        data = loungesPlaceHighlight.objects.all()
        serializer = loungesPlaceHighlightSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place highlights fetched successfully",
            "data": serializer.data
        })


class loungesPlaceOfferListAPIView(APIView):
    def get(self, request):
        data = loungesPlaceOffer.objects.all()
        serializer = loungesPlaceOfferSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place offers fetched successfully",
            "data": serializer.data
        })

