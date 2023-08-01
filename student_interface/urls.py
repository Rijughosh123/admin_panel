from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.student_home), 
    path('login/', views.student_login), 
    path('stu_dash/', views.student_dashboard), 
    path('stu_home/', views.student_home), 
    path('stu_course/', views.student_courses),
]