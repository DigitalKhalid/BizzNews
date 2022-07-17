# Generated by Django 4.0.4 on 2022-05-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50)),
                ('news_summary', models.TextField()),
                ('news_detail', models.TextField()),
                ('date', models.DateField()),
                ('image_path', models.TextField()),
                ('news_writer', models.CharField(max_length=50)),
            ],
        ),
    ]