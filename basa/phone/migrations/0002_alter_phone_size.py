# Generated by Django 4.2.4 on 2023-08-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='size',
            field=models.FloatField(verbose_name='Phone size'),
        ),
    ]