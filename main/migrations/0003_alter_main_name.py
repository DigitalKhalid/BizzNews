# Generated by Django 4.0.4 on 2022-05-29 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about_alter_main_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.TextField(),
        ),
    ]