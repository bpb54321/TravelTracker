from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    predators = models.CharField(max_length=100)
    num_restaurants = models.IntegerField()
    img_url = models.CharField(max_length=300)

    def __str__(self):
        return self.name
