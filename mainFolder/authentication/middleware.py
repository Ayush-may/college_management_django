from typing import Any
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse

class RedirectLoggedUserToDashboard:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    # index_path = reverse("authentication:index")
    login_path = reverse("authentication:login_user")
    create_path = reverse("authentication:create_user")

    if request.user.is_authenticated and request.path in [login_path,create_path]:
      return redirect("student_dashboard:dashboard")

    return self.get_response(request)