from django.db import models

# Create your models here.


class employeeinfo(models.Model):
    emp_id      = models.IntegerField()
    emp_name    = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=200)
    emp_email   = models.EmailField(max_length=200)
    emp_phone   = models.CharField(max_length=20)