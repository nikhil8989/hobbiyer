# Generated by Django 3.0.5 on 2020-04-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200418_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], default='select gwnder', max_length=10),
        ),
    ]
