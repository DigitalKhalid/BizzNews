from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_main_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='address',
            field=models.CharField(max_length=250, default='-'),
        ),
    ]