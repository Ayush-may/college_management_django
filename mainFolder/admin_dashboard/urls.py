from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('students/',views.students,name='students'),
    path('departments/',views.departments,name='departments'),
    path('news/',views.news,name='news'),

    # students
    path('students/',views.students,name='students'),
    path('students/<int:id>',views.student_details,name='student_details'),
    path('students/delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('students/update_student/<int:id>',views.update_student,name='update_student'),
    
    # staffs
    path('staffs/',views.staffs,name='staffs'),
    path('staffs/add_staff',views.add_staff,name='add_staff'),
]