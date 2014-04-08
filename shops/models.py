from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to="shops", blank=True)
    timetable = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    categories = models.CharField(max_length=255)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name
