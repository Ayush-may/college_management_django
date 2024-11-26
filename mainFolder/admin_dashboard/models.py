from django.db import models

# Create your models here.
class AdminModel(models.Model):
  username = models.CharField(name='username',max_length=10, primary_key=True)
  password = models.CharField(name='password', max_length=128)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  last_login = models.DateTimeField(blank=True, null=True)