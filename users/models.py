from django.contrib.auth.models import User
from django.db import models


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.user


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True)
    address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user


class Validator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return self.user
