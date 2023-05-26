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

class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB,'web')
        (DEVICE_ANDROID, 'android')
        (DEVICE_IOS, 'ios')
        (DEVICE_PC, 'pc')
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Device', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID', null=True)
    last_login = models.DateTimeField('Last login date', null=True)
    device_type = models.PositiveIntegerField(choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField('device os',max_length=20,blank=True)
    device_model = models.CharField('device model',max_length=20,blank=True)
    app_version = models.CharField('App version', max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)