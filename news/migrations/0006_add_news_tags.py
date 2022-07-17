from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_news_news_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_tags',
            field=models.TextField(default='-'),
        ),
    ]