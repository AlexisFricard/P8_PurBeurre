""" MODELS FILE """

from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_url = models.TextField()
    product_img = models.TextField()
    category = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=5)
    code = models.TextField(default=0)

    class Meta:
        db_table = "product"


class Nutriment(models.Model):

    code = models.TextField(max_length=200)
    energy_100g = models.DecimalField(max_digits=7, decimal_places=2)
    energy_unit = models.CharField(max_length=5)
    proteins_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fat_100g = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates_100g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fiber_100g = models.DecimalField(max_digits=6, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = "nutriment"


class Save(models.Model):

    save_id = models.AutoField(primary_key=True)
    user = models.TextField(default=0)
    substitute = models.TextField(default=0)
    product_substitued = models.TextField(default=0)

    class Meta:
        db_table = "save"
