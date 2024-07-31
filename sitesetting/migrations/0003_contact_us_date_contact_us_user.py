# Generated by Django 5.0.7 on 2024-07-27 05:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0002_sitesetting_address_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ارسال نظر'),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
