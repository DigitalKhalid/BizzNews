# Generated by Django 4.0.4 on 2022-07-23 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanager',
            name='user_doj',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
