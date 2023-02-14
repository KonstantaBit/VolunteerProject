from django.contrib.auth.models import User
from django.db import models


class AbstractFullUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=16, blank=True)
    description = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True, verbose_name='Фотография')

    class Meta:
        abstract = True

    def __str__(self):
        return self.user


class Volunteer(AbstractFullUser):
    pass


class Organization(AbstractFullUser):
    name = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=150, blank=True)


class Validator(AbstractFullUser):
    pass
