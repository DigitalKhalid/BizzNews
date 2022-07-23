from datetime import datetime
from django.db import models

class Usermanager(models.Model):
    class Userstatus(models.TextChoices):
        Active = 'Active'
        Inactive = 'Inactive'

    username = models.CharField(max_length=50)
    user_firstname = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_contact = models.CharField(max_length=50)
    user_biography = models.TextField()
    user_address = models.TextField()
    user_doj = models.DateTimeField(default=datetime.now)
    user_image = models.ImageField(upload_to='pics', default='avatar.jpg')
    user_status = models.CharField(max_length=8, choices=Userstatus.choices, default=Userstatus.Active)
    user_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.username
