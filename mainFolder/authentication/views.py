from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, sessions
from django.contrib.auth import authenticate , login , logout, hashers
from django.contrib.auth.models import User
# from .models import AdminModel
from admin_dashboard.models import AdminModel

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    return redirect('student_dashboard:dashboard')
  
  return render(request,'authentication/index.html')

def login_admin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    user = AdminModel.objects.filter(username = username,password=password).values()

    if user is None:
      messages.error(request, "admin is not available")
      return redirect('authentication:index')

    request.session['admin_username'] = username
    messages.success(request, "Logged in!")
    
    return redirect("admin_dashboard:dashboard")
  return render(request, 'authentication/login_admin.html')

def login_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    user = authenticate(username = username, password=password)

    if user is None:
      messages.error(request, "user is not available")
      return redirect('authentication:index')

    messages.success(request, "Logged in!")
    login(request, user)
    
    return redirect("authentication:login_user")
  return render(request, 'authentication/login_user.html')

def create_user(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')

    if username is None or password != confirm_password:
      messages.error(request, "Password is not matching")
      return redirect('authentication:create_user')

    user = User.objects.create_user(username)
    user.set_password(password)
    user.save()

    messages.success(request, "user is created !")
    return redirect("authentication:login_user")
  
  return render(request, 'authentication/create_user.html')

def create_admin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')

    if username is None or password != confirm_password:
      messages.error(request, "Password is not matching")
      return redirect('authentication:create_user')

    hash_password = hashers.make_password(password=password)

    admin = AdminModel.objects.create(
      username = username , 
      password = hash_password
      )
    admin.save()

    messages.success(request, "admin is created !")
    return redirect("authentication:index")
  
  return render(request, 'authentication/create_admin.html')