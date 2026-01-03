from django.contrib import admin
from .models import (
    Moments , MomentImage,
    Signature, SignatureImage,
    Memories, MemoriesImage,
    Dining, DiningImage
)


# Admin for Moments
@admin.register(Moments)
class MomentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'created_at', 'updated_at')
    search_fields = ('title', 'sub_title')

# Admin for MomentImage
@admin.register(MomentImage)
class MomentImageAdmin(admin.ModelAdmin):
    list_display = ('moments', 'moments_image', 'created_at')
    search_fields = ('moments__title',)
    list_filter = ('moments',)



# Signature Section Admin
class SignatureImageInline(admin.TabularInline):
    model = SignatureImage
    fields = ['signature_image', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'created_at', 'updated_at']
    inlines = [SignatureImageInline]


# Memories Section Admin
class MemoriesImageInline(admin.TabularInline):
    model = MemoriesImage
    fields = ['memories_image', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Memories)
class MemoriesAdmin(admin.ModelAdmin):
    list_display = ['memories_title', 'memories_sub_title', 'created_at', 'updated_at']
    inlines = [MemoriesImageInline]


# Dining Section Admin
class DiningImageInline(admin.TabularInline):
    model = DiningImage
    fields = ['dining_image', 'created_at']
    readonly_fields = ['created_at']


@admin.register(Dining)
class DiningAdmin(admin.ModelAdmin):
    list_display = ['dining_title', 'dining_sub_title', 'created_at', 'updated_at']
    inlines = [DiningImageInline]
