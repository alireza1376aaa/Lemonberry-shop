# Generated by Django 5.0.7 on 2024-07-27 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_men_product_discription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_men',
            name='tag_products',
        ),
    ]