# Generated by Django 2.2.1 on 2020-05-19 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creche', '0003_holidays_holiday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidays',
            name='holiday',
        ),
    ]
