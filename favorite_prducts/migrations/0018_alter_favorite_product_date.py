# Generated by Django 5.0.7 on 2024-07-27 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0017_alter_favorite_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 13, 54, 57, 925160), verbose_name='تاریخ '),
        ),
    ]
