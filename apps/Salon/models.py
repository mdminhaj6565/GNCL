from django.db import models
from django.forms import CharField

# Create your models here.

class SalonPlaceDes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class SalonPlaceImage(models.Model):
    place = models.ForeignKey(
        SalonPlaceDes,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="places/images/")

    def __str__(self):
        return f"Image of {self.place.title}"


class SalonPlaceHighlight(models.Model):
    place = models.ForeignKey(
        SalonPlaceDes,
        related_name="highlights",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100,blank=True,null=True)
    icon = models.ImageField(
        upload_to="places/highlights/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class SalonPlaceOffer(models.Model):
    place = models.ForeignKey(
        SalonPlaceDes,
        related_name="offers",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to="salon_places/offers/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    