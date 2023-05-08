from django.db import models


# Create your models here.

class User(models.Model):
    user = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    permissions_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    permissions = models.SmallIntegerField(verbose_name='权限', choices=permissions_choices)


class UserOrder(models.Model):
    user = models.OneToOneField(verbose_name='用户', to='User', on_delete=models.CASCADE)
    token = models.CharField(verbose_name='认证', max_length=64)
