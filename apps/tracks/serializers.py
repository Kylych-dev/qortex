
from rest_framework import serializers
from .models import (Artists,
                     Albums,
                     Tracks)

class ArtistSerializer(serializers.ModelSerializer):
    '''Serializer for the Artist model'''
    class Meta:
        model = Artists
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    '''Serializer for the Album model'''
    class Meta:
        model = Albums
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    '''Serializer for the Track model'''
    class Meta:
        model = Tracks
        fields = '__all__'