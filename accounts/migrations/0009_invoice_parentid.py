# Generated by Django 3.1 on 2021-08-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210512_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='parentID',
            field=models.IntegerField(default=0),
        ),
    ]
