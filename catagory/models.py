from django.db import models

class Catagory(models.Model):
    catagory = models.CharField(max_length=50)
    news_count = models.IntegerField(default=0)

    def __str__(self):
        return self.catagory