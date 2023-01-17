from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
