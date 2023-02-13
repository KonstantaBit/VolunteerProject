from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from users.models import Organization, Volunteer


class Photo(models.Model):
    photo = models.ImageField(upload_to='uploads', verbose_name='Фотография')

    @property
    def get_img(self):
        return get_thumbnail(self.photo, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.photo:
            return mark_safe(f'<img src="{self.get_img.url}">')
        return 'Нет изображения'

    image_tmb.short_description = 'Превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


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
    limiter = models.IntegerField(default=1)
    photo = models.ImageField(upload_to='uploads', blank=True, verbose_name='Превью')
    album = models.ManyToManyField(Photo, related_name='album', blank=True, verbose_name='Альбом')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
