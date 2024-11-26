from django.db import models
from student_dashboard.models import StudentModel

class FeesTransactionModel(models.Model):
  student = models.ForeignKey(StudentModel,on_delete=models.CASCADE,blank=False,null=False)
  amount = models.DecimalField(decimal_places=2)
  paid_at = models.DateTimeField(auto_now_add=True)
  year = models.TextChoices