from django.urls import path
from .views import (
    SalonPlaceDesListAPIView,
    SalonPlaceImageListAPIView,
    SalonPlaceHighlightListAPIView,
    SalonPlaceOfferListAPIView
)

urlpatterns = [
    path("places_salon/", SalonPlaceDesListAPIView.as_view()),

    # All images of a place
    path("places_salon/<int:place_id>/images/", SalonPlaceImageListAPIView.as_view()),

    path("highlights_salon/", SalonPlaceHighlightListAPIView.as_view()),
    path("offers_salon/", SalonPlaceOfferListAPIView.as_view()),
]