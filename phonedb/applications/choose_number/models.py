from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    number = models.IntegerField(primary_key=True)
    reserved = models.BooleanField(default=False)
