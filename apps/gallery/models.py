from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Memoris section model
class Moments(TimeStamp):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    

class MomentImage(TimeStamp):
     moments = models.ForeignKey(Moments,on_delete=models.CASCADE,related_name='moments_images')
     moments_image = models.ImageField(upload_to='Gallery/moments/')
     
     def __str__(self):
         return f"Image of {self.moments.title}"
     

# Signature Section
class Signature(TimeStamp):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SignatureImage(TimeStamp):
    signature = models.ForeignKey(
        Signature,
        on_delete=models.CASCADE,
        related_name='signature_images'
    )
    signature_image = models.ImageField(upload_to='Gallery/signature/')

    def __str__(self):
        return f"Image of {self.signature.title}"


# Memories Section
class Memories(TimeStamp):
    memories_title = models.CharField(max_length=255)
    memories_sub_title = models.CharField(max_length=255)

    def __str__(self):
        return self.memories_title


class MemoriesImage(TimeStamp):
    memories = models.ForeignKey(
        Memories,
        on_delete=models.CASCADE,
        related_name='memory_images'
    )
    memories_image = models.ImageField(
        upload_to='Gallery/memories/',
        blank=True, null=True
    )

    def __str__(self):
        return self.memories_image.name if self.memories_image else ""


# Dining Section (WITH PAGINATION)
class Dining(TimeStamp):
    dining_title = models.CharField(max_length=255)
    dining_sub_title = models.CharField(max_length=255)

    def __str__(self):
        return self.dining_title


class DiningImage(TimeStamp):
    dining = models.ForeignKey(
        Dining,
        on_delete=models.CASCADE,
        related_name='dining_images'
    )
    dining_image = models.ImageField(
        upload_to='Gallery/dining/',
        blank=True, null=True
    )

    def __str__(self):
        return f"Image of {self.dining.dining_title}"
