# Generated by Django 3.1.5 on 2021-06-21 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210607_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='listning',
            name='auction_end',
            field=models.BooleanField(default=False),
        ),
    ]
