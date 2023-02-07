from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.cache import cache


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('damagedealers', 'ДД'),
        ('merchants', 'Торговцы'),
        ('guildmasters', 'Гильдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('potionmasters', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='tanks')
    file = models.FileField(upload_to='uploads/', blank=True)

    def get_absolute_url(self):
        return "/articles/%i" % self.id


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
