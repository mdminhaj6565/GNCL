from django.db import models

# Create your models here.

class PlaceDes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        PlaceDes,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="places/images/")

    def __str__(self):
        return f"Image of {self.place.title}"


class PlaceHighlight(models.Model):
    place = models.ForeignKey(
        PlaceDes,
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


class PlaceOffer(models.Model):
    place = models.ForeignKey(
        PlaceDes,
        related_name="offers",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to="places/offers/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    