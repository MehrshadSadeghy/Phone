# Generated by Django 4.2.4 on 2023-08-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_alter_phone_price_alter_phone_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='manufacturing_country',
            field=models.CharField(default=1, max_length=20, verbose_name='Manufacturing country'),
            preserve_default=False,
        ),
    ]
