# Generated by Django 4.0.4 on 2022-07-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='news_count',
            field=models.IntegerField(default=0),
        ),
    ]
