# Generated by Django 2.2.1 on 2020-05-19 22:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('creche', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidays',
            name='holiday',
        ),
        migrations.AddField(
            model_name='holidays',
            name='datefrom',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holidays',
            name='dateto',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
