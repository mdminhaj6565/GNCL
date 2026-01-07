from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    SwimmingPoolPlaceDes,
    SwimmingPoolPlaceImage,
    SwimmingPoolPlaceHighlight,
    SwimmingPoolPlaceOffer
)
from .serializers import (
    SwimmingPoolPlaceDesSerializer,
    SwimmingPoolPlaceImageSerializer,
    SwimmingPoolPlaceHighlightSerializer,
    SwimmingPoolPlaceOfferSerializer
)

# Create your views here.


class SwimmingPoolPlaceDesListAPIView(APIView):
    def get(self, request):
        data = SwimmingPoolPlaceDes.objects.all()
        serializer = SwimmingPoolPlaceDesSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place description fetched successfully",
            "data": serializer.data
        })


class SwimmingPoolPlaceImageListAPIView(APIView):
    def get(self, request, place_id):
        images = SwimmingPoolPlaceImage.objects.filter(place_id=place_id)
        serializer = SwimmingPoolPlaceImageSerializer(images, many=True)

        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place images fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class SwimmingPoolPlaceHighlightListAPIView(APIView):
    def get(self, request):
        data = SwimmingPoolPlaceHighlight.objects.all()
        serializer = SwimmingPoolPlaceHighlightSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place highlights fetched successfully",
            "data": serializer.data
        })


class SwimmingPoolPlaceOfferListAPIView(APIView):
    def get(self, request):
        data = SwimmingPoolPlaceOffer.objects.all()
        serializer = SwimmingPoolPlaceOfferSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place offers fetched successfully",
            "data": serializer.data
        })

