# Generated by Django 3.0.5 on 2020-04-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='country',
            field=models.CharField(max_length=20),
        ),
    ]
