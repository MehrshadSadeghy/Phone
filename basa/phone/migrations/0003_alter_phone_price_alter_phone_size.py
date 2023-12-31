# Generated by Django 4.2.4 on 2023-08-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_alter_phone_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(verbose_name='Phone price'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='size',
            field=models.FloatField(max_length=5, verbose_name='Phone size'),
        ),
    ]
