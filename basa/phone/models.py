from django.db import models


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    nationality = models.CharField(max_length=30, verbose_name="Nationality")

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_model = models.CharField(max_length=20, verbose_name="Phone name")
    phone_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Phone brand")
    manufacturing_country = models.CharField(max_length=20, verbose_name="Manufacturing country")
    phone_color = models.CharField(max_length=15)
    price = models.IntegerField(verbose_name="Phone price")
    size = models.FloatField(max_length=5, verbose_name="Phone size")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.phone_model
