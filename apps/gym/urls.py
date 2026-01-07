from django.urls import path
from .views import (
    PlaceDesListAPIView,
    PlaceImageListAPIView,
    PlaceHighlightListAPIView,
    PlaceOfferListAPIView
)

urlpatterns = [
    path("places/", PlaceDesListAPIView.as_view()),

    # All images of a place
    path("places/<int:place_id>/images/", PlaceImageListAPIView.as_view()),

    path("highlights/", PlaceHighlightListAPIView.as_view()),
    path("offers/", PlaceOfferListAPIView.as_view()),
]
