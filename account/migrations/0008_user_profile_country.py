# Generated by Django 3.0.5 on 2020-04-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200419_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='country',
            field=models.CharField(default='india', max_length=20),
        ),
    ]