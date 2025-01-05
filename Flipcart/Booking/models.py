from django.db import models
from unicodedata import decimal


# Create your models here.
class emp(models.Model):
    employee_id=models.IntegerField(primary_key=True)
    employee_name=models.TextField(max_length=15)
    salary=models.FloatField(max_length=10)
    dno=models.IntegerField()

