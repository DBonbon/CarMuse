from django.db import models
import PIL
from PIL import Image, ExifTags
from django.urls import reverse



class AboutPage(models.Model):
    '''Model representing a the cover page'''
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True, null=True, help_text='Enter a brief description on Cariage Foundation')
    image = models.ImageField(upload_to='media/about/', null=True, blank=True)
    link = models.URLField(max_length=200)
    contact_title = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

