# Generated by Django 5.0.7 on 2024-07-30 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0033_alter_favorite_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 30, 20, 17, 58, 850659), verbose_name='تاریخ '),
        ),
    ]