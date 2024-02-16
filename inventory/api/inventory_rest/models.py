from django.db import models


class Pellets(models.Model):
    item_number = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    unit_price = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()
