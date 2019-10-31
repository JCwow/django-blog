from django.db import models

# Create your models here.
class Restaurant(models.Model):
    title = models.CharField(max_length=120) # max_lenght=required
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, null=True)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField()