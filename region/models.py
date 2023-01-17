from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
