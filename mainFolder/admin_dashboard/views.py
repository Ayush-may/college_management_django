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
  q = request.GET.get('q','')
  d = request.GET.get('d','')

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
    if q or d:
      students = StudentModel.objects.select_related("department").filter(first_name__icontains=q, department__name__icontains=d).values(
        "id","first_name","last_name","enrollment","department__pk","department__code", "department__name"
      )
    else:
      students = StudentModel.objects.select_related("department").values(
        "id","first_name","last_name","enrollment","department__pk","department__code", "department__name"
      )
    
    departments = DepartmentModel.objects.all().values()
    return render(request,'admin_dashboard/student/students.html', {
      "students" : students,
      "departments" :departments,
      "q":q,
      "d" :d,
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
  return render(request,'admin_dashboard/staff/staff.html')

def add_staff(request):
  departments = DepartmentModel.objects.all()
  d = request.GET.get('d','')
  s = request.GET.get('s','')
  f = request.GET.get('f','')
  l = request.GET.get('l','')
  dob = request.GET.get('dob','')


  if request.method == "POST":
    s = request.POST.get('s','')
    d = request.POST.get('d','')
    f = request.POST.get('f','')
    l = request.POST.get('l','')
    dob = request.POST.get('dob','')

    if s is None or d is None or f is None or f is None or l is None or dob is None:
      messages.error(request,'Kindly enter all details')
      return redirect("admin_dashboard:staff")

    

  data = {
    "departments" : departments,
    'd':d,
    "s":s,
    "f":f,
    "l":l,
    "dob":dob,
  }
  return render(request,'admin_dashboard/staff/add_staff.html',data)

def departments(request):
  return HttpResponse('admin/departments')

def news(request):
  return HttpResponse('admin/news')