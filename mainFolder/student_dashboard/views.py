from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
def dashboard(request):
  if not request.user.is_authenticated:
    return redirect("authentication:index")
  
  data = {
    "username" : request.user.username
  }

  return render(request,'student_dashboard/dashboard.html', data)

def logout_user(request):
  logout(request) 
  return redirect('authentication:index')