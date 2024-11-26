from django.urls import path
from . import views

app_name = 'student_dashboard'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('logout/',views.logout_user,name='logout'),
]