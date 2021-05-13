from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=12)
    price = models.FloatField()
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
