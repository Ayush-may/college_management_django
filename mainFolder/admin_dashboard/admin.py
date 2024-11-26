from django.contrib import admin
from .models import AdminModel

# Register your models here.
@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
  list_display = ['pk','username',]