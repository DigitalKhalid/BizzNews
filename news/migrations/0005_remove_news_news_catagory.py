# Generated by Django 4.0.4 on 2022-07-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_date_news_news_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_catagory',
        ),
    ]
