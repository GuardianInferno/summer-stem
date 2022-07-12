from django.db import models
from datetime import datetime
# Create your models here.
class userInfo(models.Model):
    username = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=100,decimal_places=2)
    join_date = models.DateTimeField()
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ['username',]

    def __str__(self):
        return self.username


class objectInfo(models.Model):
    object = models.ForeignKey(userInfo,related_name='objects', on_delete=models.CASCADE)
    object_name = models.CharField(max_length=100)
    object_amount = models.IntegerField()
    object_price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.object_name


