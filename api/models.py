from django.db import models


class Gallery(models.Model):
    # sections are 'My works', 'Painting', 'House' etc
    section = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='default_gallery.jpg',
                              upload_to='gallery_section_pics')

    def __str__(self):
        return self.section


class GalleryFolder(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='default_gallery.jpg',
                              upload_to=f'gallery_section_pics/{name}')

    def __str__(self):
        return f'{self.gallery.section} > {self.name}'


class GalleryFolderImage(models.Model):
    folder = models.ForeignKey(GalleryFolder,
                               default=None,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image = models.ImageField(default='default_gallery.jpg',
                              upload_to=f'gallery_section_pics/{name}')

    def __str__(self):
        return f'{self.folder.name} > {self.name}'
