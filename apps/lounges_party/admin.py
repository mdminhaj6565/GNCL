from django.contrib import admin
from .models import (
    loungesPlaceDes,
    loungesPlaceImage,
    loungesPlaceHighlight,
    loungesPlaceOffer
)

# Register your models here.

class loungesPlaceImageInline(admin.TabularInline):
    model = loungesPlaceImage
    extra = 1


class loungesPlaceHighlightInline(admin.TabularInline):
    model = loungesPlaceHighlight
    extra = 1


class loungesPlaceOfferInline(admin.TabularInline):
    model = loungesPlaceOffer
    extra = 1


@admin.register(loungesPlaceDes)
class loungesPlaceDesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [
        loungesPlaceImageInline,
        loungesPlaceHighlightInline,
        loungesPlaceOfferInline,
    ]
