from django.db import models

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    images = models.ManyToManyField('EventImage')

class EventImage(models.Model):
    image = models.ImageField(upload_to='media/event_images/')

