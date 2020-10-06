from django.db import models


# Create your models here.

class Gallery(models.Model):
    # sections are 'My works', 'Painting', 'House' etc
    section = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='default_gallery.jpg',
                              upload_to='gallery_section_pics')

    def __str__(self):
        return self.section
