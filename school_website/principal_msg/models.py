from django.db import models

from django.db import models

class PrincipalMessage(models.Model):
    image = models.ImageField(upload_to='media/principal_images/')
    message = models.TextField()

    def __str__(self):
        return "Principal's Message"

