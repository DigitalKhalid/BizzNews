# Generated by Django 4.0.4 on 2022-05-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014-test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='contact',
            field=models.CharField(default='-', max_length=50),
        ),
    ]