from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .models import Moments,MomentImage, Signature, Memories, Dining, DiningImage
from .serializers import (
    SignatureSerializer, MemoriesSerializer,
    DiningSerializer, DiningImageSerializer,
    MomentImageSerializer, MomentsSerializer,
)



# Moments API
class MomentsListAPIView(APIView):
    def get(self, request):
        moments = Moments.objects.all()
        serializer = MomentsSerializer(moments, many=True)
        return Response({
            'status': 'success',
            'message': 'Moments list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })

# Moment Images List API
class MomentImageListAPIView(APIView):
    def get(self, request):
        images = MomentImage.objects.all()
        serializer = MomentImageSerializer(images, many=True)
        return Response({
            'status': 'success',
            'message': 'Moment images list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


# Signature& image API
class SignatureAPIView(APIView):
    def get(self, request):
        items = Signature.objects.all()
        serializer = SignatureSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Signature list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class SignatureImageAPIView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Signature, pk=pk)
        serializer = SignatureSerializer(item)
        return Response({
            'status': 'success',
            'message': 'Signature details fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


# Memories  & image API
class MemoriesAPIView(APIView):
    def get(self, request):
        items = Memories.objects.all()
        serializer = MemoriesSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Memories list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class MemoriesImagesAPIView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Memories, pk=pk)
        serializer = MemoriesSerializer(item)
        return Response({
            'status': 'success',
            'message': 'Memory details fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


# Dining Images Pagination
class DiningImagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class DiningImageListAPIView(ListAPIView):
    serializer_class = DiningImageSerializer
    pagination_class = DiningImagePagination

    def get_queryset(self):
        dining_id = self.request.query_params.get('dining_id')
        if dining_id:
            return DiningImage.objects.filter(dining_id=dining_id).order_by('-created_at')
        return DiningImage.objects.all().order_by('-created_at')


class DiningImageDetailAPIView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(DiningImage, pk=pk)
        serializer = DiningImageSerializer(item)
        return Response({
            'status': 'success',
            'message': 'Dining image details fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


# Dining title and sub title & image API (Dining model only - no pagination needed here)
class DiningAPIView(APIView):
    def get(self, request):
        items = Dining.objects.all()
        serializer = DiningSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Dining list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class DiningImagesAPIView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Dining, pk=pk)
        serializer = DiningSerializer(item) 
        return Response({
            'status': 'success',
            'message': 'Dining details fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })
