from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(_("Отчество"), max_length=150, blank=True)
    position = models.CharField(_("Должность"), max_length=300, blank=True)
