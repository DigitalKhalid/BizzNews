# Generated by Django 4.0.4 on 2022-05-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='about',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.TextField(verbose_name=50),
        ),
    ]
