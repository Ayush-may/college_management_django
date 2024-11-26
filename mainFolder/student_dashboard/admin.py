from django.contrib import admin
from .models import StudentModel

# Register your models here.
# admin.site.register(StudentModel)

@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
  list_display = ['uid','first_name', 'last_name']