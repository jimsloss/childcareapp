# Generated by Django 3.1 on 2021-08-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.parent'),
        ),
    ]