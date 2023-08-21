from django.shortcuts import render

from rest_framework import viewsets
from .models import Artists, Albums, Tracks
from .serializers import (ArtistSerializer,
                          AlbumSerializer,
                          TrackSerializer)

class ArtistViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows artists to be viewed or edited'''
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows albums to be viewed or edited'''
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer

class TrackViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows songs to be viewed or edited'''
    queryset = Tracks.objects.all()
    serializer_class = TrackSerializer

