from rest_framework import serializers
from .models import Gallery


class GallerySerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('id', 'image', 'section', 'description', 'image_url')
        # fields = '__all__'

    def get_image_url(self, gallery):
        request = self.context.get('request')
        image_url = gallery.image.url
        return request.build_absolute_uri(image_url)
