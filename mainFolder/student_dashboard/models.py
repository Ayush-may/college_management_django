import uuid
from django.db import models
from departments.models import DepartmentModel

# Create your models here.

class StudentModel(models.Model):
  uid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100, blank=True)
  enrollment = models.CharField(max_length=12, null=True)
  DOB = models.DateField(blank=True,null=True)
  department = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # DOB, admission date, 