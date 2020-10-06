from rest_framework import serializers
from .models import Gallery


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
