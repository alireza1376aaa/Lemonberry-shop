# Generated by Django 5.0.7 on 2024-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='address_url',
            field=models.TextField(default='salam', verbose_name='لینک ادرس در گوگل'),
            preserve_default=False,
        ),
    ]
