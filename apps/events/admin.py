from django.contrib import admin
from .models import (
    HeroSection, HeroImage,
    Events, EventsImage
)
# Register your models here.


# Hero Section Admin
class HeroImageInline(admin.TabularInline):
    model = HeroImage


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [HeroImageInline]


# Completed Event Admin

class EventsImageInline(admin.TabularInline):
    model = EventsImage
    extra = 1


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'date')
    inlines = [EventsImageInline]


@admin.register(EventsImage)
class EventsImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'images')

