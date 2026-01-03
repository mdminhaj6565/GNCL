from django.db import models

from apps.about.models import __str__
# Timestamp abstract model

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Hero Section
class HeroSection(TimeStamp, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to="hero_bg/")

    def __str__(self):
        return self.title


class HeroImage(TimeStamp, models.Model):
    hero = models.ForeignKey(HeroSection, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hero_images/")

    def __str__(self):
        return f"Image {self.id} of Hero '{self.hero.title}'"
   

# Events model
class Events(TimeStamp, models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.title


class EventsImage(TimeStamp, models.Model):
    event = models.ForeignKey(Events, null=True, blank=True, on_delete=models.SET_NULL)
    images = models.ImageField(upload_to='Events/events-image')

    def __str__(self):
        if self.event:
            return f"Image of {self.event.title}"
        return "Image (No event assigned)"

