from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    PlaceDes,
    PlaceImage,
    PlaceHighlight,
    PlaceOffer
)
from .serializers import (
    PlaceDesSerializer,
    PlaceImageSerializer,
    PlaceHighlightSerializer,
    PlaceOfferSerializer
)


class PlaceDesListAPIView(APIView):
    def get(self, request):
        data = PlaceDes.objects.all()
        serializer = PlaceDesSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place description fetched successfully",
            "data": serializer.data
        })


class PlaceImageListAPIView(APIView):
    def get(self, request, place_id):
        images = PlaceImage.objects.filter(place_id=place_id)
        serializer = PlaceImageSerializer(images, many=True)

        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place images fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class PlaceHighlightListAPIView(APIView):
    def get(self, request):
        data = PlaceHighlight.objects.all()
        serializer = PlaceHighlightSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place highlights fetched successfully",
            "data": serializer.data
        })


class PlaceOfferListAPIView(APIView):
    def get(self, request):
        data = PlaceOffer.objects.all()
        serializer = PlaceOfferSerializer(data, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Place offers fetched successfully",
            "data": serializer.data
        })

