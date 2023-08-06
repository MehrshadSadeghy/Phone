# Generated by Django 4.2.4 on 2023-08-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('nationality', models.CharField(max_length=30, verbose_name='Nationality')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_model', models.CharField(max_length=20, verbose_name='Phone name')),
                ('phone_color', models.CharField(max_length=15)),
                ('price', models.IntegerField(max_length=20, verbose_name='Phone price')),
                ('size', models.FloatField(max_length=5, verbose_name='Phone size')),
                ('is_available', models.BooleanField(default=True)),
                ('phone_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.brand', verbose_name='Phone brand')),
            ],
        ),
    ]