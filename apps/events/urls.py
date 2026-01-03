from django.urls import path
from .views import HeroSectionListAPIView, EventsListView,EventsImagesView

urlpatterns = [
    # Hero Section API
    path('heroes/', HeroSectionListAPIView.as_view(), name='hero-list'),
    path('events/', EventsListView.as_view(), name='events-list'),
    path('past-events/', EventsImagesView.as_view(), name='past-events-list'),
]
