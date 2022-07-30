from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_add_news_tags copy'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_username',
            field=models.CharField(max_length=50, default='-'),
        ),
    ]