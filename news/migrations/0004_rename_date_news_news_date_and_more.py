# Generated by Django 4.0.4 on 2022-07-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_news_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='date',
            new_name='news_date',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='image',
            new_name='news_image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='image_path',
        ),
        migrations.AddField(
            model_name='news',
            name='news_catagoryid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='news_views',
            field=models.IntegerField(default=0),
        ),
    ]