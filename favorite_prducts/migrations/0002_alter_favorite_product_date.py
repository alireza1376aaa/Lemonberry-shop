# Generated by Django 5.0.7 on 2024-07-24 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 24, 12, 13, 23, 694946), verbose_name='تاریخ '),
        ),
    ]
