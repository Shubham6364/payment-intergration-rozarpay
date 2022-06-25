from django.db import models

# Create your models here.


class Cofee(models.Model):
	name = models.CharField(max_length=255)
	amount = models.CharField(max_length=100)
	payment_id = models.CharField(max_length=100)
	paid = models.BooleanField(default=False)