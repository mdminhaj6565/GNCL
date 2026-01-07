from django.contrib import admin
from .models import (
    SalonPlaceDes,
    SalonPlaceImage,
    SalonPlaceHighlight,
    SalonPlaceOffer
)
# Register your models here.

class SalonPlaceImageInline(admin.TabularInline):
    model = SalonPlaceImage
    extra = 1


class SalonPlaceHighlightInline(admin.TabularInline):
    model = SalonPlaceHighlight
    extra = 1


class SalonPlaceOfferInline(admin.TabularInline):
    model = SalonPlaceOffer
    extra = 1


@admin.register(SalonPlaceDes)
class SalonPlaceDesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        SalonPlaceImageInline,
        SalonPlaceHighlightInline,
       SalonPlaceOfferInline,
    ]
