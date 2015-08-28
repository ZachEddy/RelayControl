from django.db import models

# Create your models here.

class Pin(models.Model):
	number = models.IntegerField(default = 0)
	output = models.BooleanField(default = True)
	active = models.BooleanField(default = False)	
