from django.db import models

class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_catagoryid = models.IntegerField()
    # news_catagoryid = models.ForeignKey(Subcatagory, on_delete=models.CASCADE, related_name='news_catagoryid')
    news_summary = models.TextField()
    news_detail = models.TextField()
    news_date = models.DateField()
    news_image = models.ImageField(upload_to='pics')
    news_writer = models.CharField(max_length=50)
    news_views = models.IntegerField(default=0)
    news_tags = models.TextField(default='-')
    news_username = models.CharField(max_length=50)
    
    def __str__(self):
        return self.news_title