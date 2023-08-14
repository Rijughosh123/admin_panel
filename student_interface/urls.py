from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.student_home), 
    path('login/', views.student_login), 

    path('stu_home/', views.student_dash), 
    path('stu_course/', views.student_courses),
    path('student_view_courses/', views.student_view_courses), 
    path('student_today_class/', views.student_today_class),
    path('stu_p_course/', views.student_p_courses), 
    path('student_trophy/', views.student_trophy), 
]