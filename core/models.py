from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    serving_size = models.CharField(max_length=100)
    # ----------------------------------------
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)


    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=6, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    sodium = models.DecimalField(max_digits=6, decimal_places=2)
    magnesium = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    # ----------------------------------------
