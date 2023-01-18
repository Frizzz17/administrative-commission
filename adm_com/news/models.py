from django.db import models


class News(models.Model):
    '''Создаёт статью.'''
    header = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
