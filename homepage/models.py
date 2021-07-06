from django.db import models
import PIL
from PIL import Image, ExifTags
from django.urls import reverse



class Cover(models.Model):
    '''Model representing a the cover page'''
    header = models.CharField(max_length=200)
    pitch = models.TextField(max_length=1000, blank=True, help_text='Enter a brief pitch for the homepage...only if needed')
    image = models.ImageField(upload_to='media/homepage/', null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.header



# todo create models so sections can be created, updated b. add Gender, online
#  b. Write 4-5 paragraphs to sell

# todo bootstraps: a. Menu headers login, b. reducing font size. c. colors make a palette and apply. d. make unique size of photos, to resize by the spot size

# todo images: a. how to serve images dynamically, to understand. b. Create crop feature. c. add color correction feature.

# Todo: Upload photos

# todo Django anywhere, updated version.