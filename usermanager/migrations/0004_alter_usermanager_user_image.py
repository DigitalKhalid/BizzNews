# Generated by Django 4.0.4 on 2022-07-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0003_alter_usermanager_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermanager',
            name='user_image',
            field=models.ImageField(default='media/pics/avatar.jpg', upload_to='pics'),
        ),
    ]
