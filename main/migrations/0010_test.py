# Generated by Django 4.0.4 on 2022-05-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
