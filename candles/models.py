from django.db import models

# Create your models here.

class Fragrant(models.Model):
    scent = models.CharField(max_length=300)
    seasonal_collection = models.CharField(max_length=300)
    color = models.CharField(max_length=200)
    gift_quantity = models.IntegerField()
    wick_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    


