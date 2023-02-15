from django.db import models


class Benefit(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    cost = models.IntegerField(default=0)
