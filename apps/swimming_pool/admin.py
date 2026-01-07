from django.contrib import admin
from .models import (
    SwimmingPoolPlaceDes,
    SwimmingPoolPlaceImage,
    SwimmingPoolPlaceHighlight,
    SwimmingPoolPlaceOffer
)

# Register your models here.

class SwimmingPoolPlaceImageInline(admin.TabularInline):
    model = SwimmingPoolPlaceImage
    extra = 1


class SwimmingPoolPlaceHighlightInline(admin.TabularInline):
    model = SwimmingPoolPlaceHighlight
    extra = 1


class SwimmingPoolPlaceOfferInline(admin.TabularInline):
    model = SwimmingPoolPlaceOffer
    extra = 1


@admin.register(SwimmingPoolPlaceDes)
class PlaceDesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        SwimmingPoolPlaceImageInline,
        SwimmingPoolPlaceHighlightInline,
        SwimmingPoolPlaceOfferInline,
    ]
