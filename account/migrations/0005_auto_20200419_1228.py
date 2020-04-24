# Generated by Django 3.0.5 on 2020-04-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='city',
            field=models.CharField(choices=[('select city', '')], default='select state', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='state',
            field=models.CharField(choices=[('select State', '')], default='select state', max_length=20),
        ),
    ]
