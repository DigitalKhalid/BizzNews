from time import timezone
from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    readstatus = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' | ' + str(self.pk)
