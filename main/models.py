from __future__ import unicode_literals
from asyncio.windows_events import NULL
from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    facebook = models.CharField(max_length=100, default='-')
    twiter = models.CharField(max_length=100, default='-')
    youtube = models.CharField(max_length=100, default='-')
    title = models.CharField(max_length=50, default='-')
    email = models.EmailField(default='-')
    contact = models.CharField(max_length=50, default='-')
    address = models.CharField(max_length=250, default='-')
    icon = models.ImageField(upload_to='pics')
    logo = models.ImageField(upload_to='pics')

    

    def __str__(self):
        return self.title + ' | ' + str(self.pk)