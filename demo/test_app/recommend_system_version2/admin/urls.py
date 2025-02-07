from django.urls import path
from . import views
from templates import *

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('student_info/', views.student_info, name='student_info'),
    path('admin/', views.admin_view, name='admin'),
    path('admin_login/', views.admin_login, name='admin_login')
]
