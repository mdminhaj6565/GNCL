from django.urls import path
from .views import (
    SwimmingPoolPlaceDesListAPIView,
    SwimmingPoolPlaceImageListAPIView,
    SwimmingPoolPlaceHighlightListAPIView,
    SwimmingPoolPlaceOfferListAPIView
)

urlpatterns = [
    path("SwimmingPool/places/", SwimmingPoolPlaceDesListAPIView.as_view()),

    # All images of a place
    path("SwimmingPool/places/<int:place_id>/images/", SwimmingPoolPlaceImageListAPIView.as_view()),

    path("SwimmingPool/highlights/", SwimmingPoolPlaceHighlightListAPIView.as_view()),
    path("SwimmingPool/offers/", SwimmingPoolPlaceOfferListAPIView.as_view()),
]