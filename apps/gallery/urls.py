from django.urls import path
from .views import (
    MomentImageListAPIView, MomentsListAPIView,
    SignatureAPIView, SignatureImageAPIView,
    MemoriesAPIView, MemoriesImagesAPIView,
   DiningAPIView,DiningImagesAPIView,
)

urlpatterns = [
    path('moments/', MomentsListAPIView.as_view(), name='moments-list'),
    path('moment-images/', MomentImageListAPIView.as_view(), name='moment-images-list'),


    path('signatures/', SignatureAPIView.as_view(), name='signature-list'),
    path('signature/', SignatureImageAPIView.as_view(), name='signature-detail'),


    path('memories/', MemoriesAPIView.as_view(), name='memories-list'),
    path('memorie/', MemoriesImagesAPIView.as_view(), name='memories-detail'),

    path('dining-images/', DiningAPIView.as_view(), name='dining-image-list'),
    path('dining-images/<int:pk>/', DiningImagesAPIView.as_view(), name='dining-image-detail'), 

]
