from django.db import models
from users.models import Organization, Volunteer


class Tag(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Task(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    users = models.ManyToManyField(Volunteer, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    award = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='uploads', blank=True, verbose_name='Превью')
    beginning = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
