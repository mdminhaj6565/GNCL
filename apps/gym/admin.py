from django.contrib import admin
from .models import (
    PlaceDes,
    PlaceImage,
    PlaceHighlight,
    PlaceOffer
)


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


class PlaceHighlightInline(admin.TabularInline):
    model = PlaceHighlight
    extra = 1


class PlaceOfferInline(admin.TabularInline):
    model = PlaceOffer
    extra = 1


@admin.register(PlaceDes)
class PlaceDesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        PlaceImageInline,
        PlaceHighlightInline,
        PlaceOfferInline,
    ]
