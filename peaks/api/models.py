from django.db import models


class MountainPeak(models.Model):
    name = models.CharField(max_length=250)
    altitude = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()