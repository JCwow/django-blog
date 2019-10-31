from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200, default='') # max_lenght=required
    location = models.CharField(max_length=200, default='')
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, null=True)
    pub_date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ('-pub_date',)
    def __str__(self):
        return self.name
    