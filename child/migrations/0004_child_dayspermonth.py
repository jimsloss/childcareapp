# Generated by Django 3.1 on 2021-09-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0003_child_daysperweek'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='dayspermonth',
            field=models.IntegerField(default=0),
        ),
    ]
