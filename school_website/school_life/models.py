from django.db import models

from django.db import models

class SchoolLifeImage(models.Model):
    image = models.ImageField(upload_to='media/school_life_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

