from django.contrib.auth.models import User
from django.db import models
from store.models import Benefit


class AbstractFullUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=16, blank=True)
    description = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='uploads', blank=True, verbose_name='Фотография')

    class Meta:
        abstract = True

    def __str__(self):
        return self.user.__str__()


class Volunteer(AbstractFullUser):
    points = models.IntegerField(default=0)
    benefits = models.ManyToManyField(Benefit, blank=True)


class Organization(AbstractFullUser):
    name = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=150, blank=True)


class Validator(AbstractFullUser):
    pass
