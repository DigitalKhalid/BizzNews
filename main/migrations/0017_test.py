from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='icon',
            field=models.ImageField(upload_to='pics'),
        ),

        migrations.AddField(
            model_name='main',
            name='logo',
            field=models.ImageField(upload_to='pics'),
        ),
    ]