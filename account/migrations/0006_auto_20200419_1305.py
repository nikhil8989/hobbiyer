# Generated by Django 3.0.5 on 2020-04-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200419_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='city',
            field=models.CharField(choices=[('select city', 'select city'), ('a', 'a'), ('b', 'b')], default='select state', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='state',
            field=models.CharField(choices=[('select State', 'select state'), ('a', 'a'), ('b', 'b')], default='select state', max_length=20),
        ),
    ]
