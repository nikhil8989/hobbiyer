# Generated by Django 3.0.5 on 2020-04-19 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200418_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='country',
        ),
    ]