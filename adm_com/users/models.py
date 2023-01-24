from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
    position = models.CharField(_("position"), max_length=300, blank=True)
