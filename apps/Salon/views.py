from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    SalonPlaceDes,
    SalonPlaceImage,
    SalonPlaceHighlight,
    SalonPlaceOffer
)
from .serializers import (
    SalonPlaceDesSerializer,
    SalonPlaceImageSerializer,
    SalonPlaceHighlightSerializer,
    SalonPlaceOfferSerializer
)

# Create your views here.


class SalonPlaceDesListAPIView(APIView):
    def get(self, request):
        data = SalonPlaceDes.objects.all()
        serializer = SalonPlaceDesSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place description fetched successfully",
            "data": serializer.data
        })


class SalonPlaceImageListAPIView(APIView):
    def get(self, request, place_id):
        images = SalonPlaceImage.objects.filter(place_id=place_id)
        serializer = SalonPlaceImageSerializer(images, many=True)

        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place images fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class SalonPlaceHighlightListAPIView(APIView):
    def get(self, request):
        data = SalonPlaceHighlight.objects.all()
        serializer = SalonPlaceHighlightSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place highlights fetched successfully",
            "data": serializer.data
        })


class SalonPlaceOfferListAPIView(APIView):
    def get(self, request):
        data = SalonPlaceOffer.objects.all()
        serializer = SalonPlaceOfferSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place offers fetched successfully",
            "data": serializer.data
        })

