# Generated by Django 2.1.5 on 2019-01-24 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190124_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 15, 31, 37, 718081, tzinfo=utc), verbose_name='date published'),
        ),
    ]