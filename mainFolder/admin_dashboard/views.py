from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from student_dashboard.models import StudentModel
from departments.models import DepartmentModel
from django.contrib import messages

# Create your views here.
def dashboard(request):
  return render(request, 'admin_dashboard/dashboard.html',{
    "total_students" : StudentModel.objects.all().count(),
    "total_departments" : DepartmentModel.objects.all().count(),
  })

def logout(request):
  pass

def students(request):
  if request.GET.get("add_student"):
    student = StudentModel( 
      first_name = request.GET.get("first_name"),
      last_name = request.GET.get("last_name"),
      enrollment = request.GET.get("enrollment"),
      department = DepartmentModel.objects.get(id=request.GET.get("department")),
      )
    student.save()
    messages.success(request, "Student is created!")
    return redirect("admin_dashboard:students")

  else:
    students = StudentModel.objects.select_related("department").values(
      "id","first_name","last_name","enrollment","department__pk","department__code", "department__name"
      )
    departments = DepartmentModel.objects.all().values()
    return render(request,'admin_dashboard/student/students.html', {
      "students" : students,
      "departments" :departments
      })

def delete_student(request,id):
  student = StudentModel.objects.get(id=id)
  if request.method == "POST":
    student.delete()
    messages.success(request, "Student is deleted!")
    return redirect("admin_dashboard:students")

  return render(request,'admin_dashboard/confim_student_delete.html')

def update_student(request, id):
  student = StudentModel.objects.get(id=id)
  departments = DepartmentModel.objects.all().values()

  if request.method == "POST":
    student.first_name = request.POST.get('first_name')
    student.last_name = request.POST.get('last_name')
    student.enrollment = request.POST.get('enrollment')
    student.save()
    messages.success(request, 'Student is updated')
    return redirect("admin_dashboard:students")
  return render(request,"admin_dashboard/update_student.html", {"student" : student, "departments":departments})

def student_details(request,id):
  student = StudentModel.objects.all().values()
  return render(request, 'admin_dashboard/student/student_details.html')

def staffs(request):
  return HttpResponse('admin/staffs')

def departments(request):
  return HttpResponse('admin/departments')

def news(request):
  return HttpResponse('admin/news')