from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 手机号
    phone = models.CharField(max_length=11, unique=True)
    # 说明
    desc = models.CharField(max_length=255, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'user'


# class UserProfile(models.Model):
#     phone = models.CharField(max_length=11, unique=True)
#     User = models.OneToOneField()