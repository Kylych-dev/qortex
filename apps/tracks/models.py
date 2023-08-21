from django.db import models

class Artists(models.Model):
    '''Model representing an artist'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Albums(models.Model):
    '''Model representing an album'''
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

class Tracks(models.Model):
    '''Model representing a tracks'''
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    track_number = models.IntegerField()


    class Meta:
        unique_together = ('album', 'track_number')

    def __str__(self):
        return self.title



