# Generated by Django 5.0.7 on 2024-07-29 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0028_alter_favorite_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 29, 12, 12, 48, 972521), verbose_name='تاریخ '),
        ),
    ]
