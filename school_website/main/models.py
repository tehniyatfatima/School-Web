from django.db import models

from django.db import models

class NavbarIcon(models.Model):
    icon = models.ImageField(upload_to='icons/', default='icons/defaulticon.jpg')

    def __str__(self):
        return f"Navbar Icon {self.id}"


class SliderImage(models.Model):
    image1 = models.ImageField(upload_to='slider/', default='slider/default.jpg')
    image2 = models.ImageField(upload_to='slider/', default='slider/default.jpg')
    image3 = models.ImageField(upload_to='slider/', default='slider/default.jpg')
    caption = models.CharField(max_length=200, blank=True, null=True)

