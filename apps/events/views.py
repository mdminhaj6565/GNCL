from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework import status
import datetime
from .models import (
    HeroSection, Events, 
)

from .serializers import (
    HeroImageSerializer,HeroSectionSerializer,
    EventsSerializer,
)
# Create your views here.


# Hero Section API
class HeroSectionListAPIView(APIView):
    def get(self, request):
        heroes = HeroSection.objects.all()
        serializer = HeroSectionSerializer(heroes, many=True)

        return Response({
            'status': 'success',
            'message': 'Hero sections fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    

class EventsListView(APIView):
    def get(self, request):
        filter_type = request.query_params.get('type')
        today = datetime.date.today()

        if filter_type == 'past':
            obj = Events.objects.filter(date__lt=today)

        elif filter_type == 'future':
            obj = Events.objects.filter(date__gt=today)

        elif filter_type == 'all':
            obj = Events.objects.all()

        else:
            obj = Events.objects.filter(date=today)

        serializer = EventsSerializer(obj, many=True)
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Events fetched successfully.",
            "data": serializer.data
        })

 # Only past events
class EventsImagesView(APIView):
    def get(self, request):
        today = datetime.date.today()

        past_events = Events.objects.filter(date__lt=today)

        serializer = EventsSerializer(past_events, many=True)

        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Past event images fetched successfully.",
            "data": serializer.data
        })
