from django.db import models
from departments.models import DepartmentModel

# Create your models here.
class StaffModel(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=200, unique=True)
  phone_number = models.CharField(max_length=200, unique=True)
  salary = models.DecimalField(decimal_places=2, default=0, max_digits=10)
  year = models.CharField(choices=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
  ), max_length=10)
  department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, unique=True)
  joined_at = models.TimeField(auto_now=True)