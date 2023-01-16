from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    model = models.CharField(max_length=40)

    def __str__(self):
        return self.name
