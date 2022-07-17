from django.db import models

class Subcatagory(models.Model):
    subcatagory = models.CharField(max_length=50)
    catagoryid = models.IntegerField(null=False)

    def __str__(self):
        return self.subcatagory