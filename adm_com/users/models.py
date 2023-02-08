from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(_("Отчество"), max_length=150, blank=True)
    position = models.CharField(_("Должность"), max_length=300, blank=True)


class Role(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Роль в административной комиссии'
    )
    user = models.ManyToManyField(User, through='RoleUser')

    def __str__(self):
        return self.title


class RoleUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
