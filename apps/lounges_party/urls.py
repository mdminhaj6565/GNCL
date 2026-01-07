from django.urls import path
from .views import (
    loungesPlaceDesListAPIView,
    loungesPlaceImageListAPIView,
    loungesPlaceHighlightListAPIView,
    loungesPlaceOfferListAPIView
)

urlpatterns = [
    path("lounges/places/", loungesPlaceDesListAPIView.as_view()),

    # All images of a place
    path("lounges/places/<int:place_id>/images/", loungesPlaceImageListAPIView.as_view()),

    path("lounges/highlights/", loungesPlaceHighlightListAPIView.as_view()),
    path("lounges/offers/", loungesPlaceOfferListAPIView.as_view()),
]
