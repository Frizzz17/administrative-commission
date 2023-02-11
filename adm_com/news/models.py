from django.db import models
from users.models import User


class News(models.Model):
    '''Создаёт статью.'''
    header = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

