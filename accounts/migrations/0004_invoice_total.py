# Generated by Django 3.1 on 2021-05-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_invoice_parentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(default=0.0),
        ),
    ]