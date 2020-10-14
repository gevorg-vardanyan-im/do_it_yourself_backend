from rest_framework import serializers
from .models import Gallery, GalleryFolder, GalleryFolderImage


class GallerySerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = '__all__'
        # fields = ('id', 'image', 'section', 'description', 'image_url')

    def get_image_url(self, gallery):
        request = self.context.get('request')
        image_url = gallery.image.url
        return request.build_absolute_uri(image_url)


class GalleryFolderSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryFolder
        fields = '__all__'
        # fields =\
        #     ('id', 'name', 'description', 'gallery', 'image', 'image_url')

    def get_image_url(self, gallery_folder):
        request = self.context.get('request')
        image_url = gallery_folder.image.url
        return request.build_absolute_uri(image_url)


class GalleryFolderImageSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryFolderImage
        fields = '__all__'
        # fields = ('id', 'name', 'description', 'folder', 'image', 'image_url')

    def get_image_url(self, gallery_folder_image):
        request = self.context.get('request')
        image_url = gallery_folder_image.image.url
        return request.build_absolute_uri(image_url)
