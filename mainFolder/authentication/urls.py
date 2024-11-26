from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('',views.index,name='index'),
    path('auth/login_admin', views.login_admin,name='login_admin'),
    path('auth/login_user', views.login_user,name='login_user'),
    path('auth/create_user', views.create_user,name='create_user'),
    path('auth/create_admin', views.create_admin,name='create_admin'),
]