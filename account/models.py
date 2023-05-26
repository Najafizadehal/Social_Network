from django.db import models
from django.conf import settings

class country(models.Model):
    name = models.CharField(max_length=20)
    abbr = models.CharField(max_length=5)
    is_activate = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

class profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True,unique=True,null=True)
    country = models.ForeignKey(to=country,on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)