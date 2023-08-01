from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

def student_home(request):
    return render(request, 'home.html')

def student_login(request):
    return render(request, 'authenticate.html')

def student_dashboard(request):
    return render(request, 'authenticate.html')

# def add_user(request):
#     add = [
#         {"username":"riju123", "email":"riju@gmail.com", "password":"12345", "first_name":"Riju", "last_name":"Ghosh"},
#         {"username":"dipu123", "email":"dipu@gmail.com", "password":"12345", "first_name":"Dipu", "last_name":"Mondal"},
#         {"username":"anirban123", "email":"anirban@gmail.com", "password":"12345", "first_name":"Anirban", "last_name":"Roy"}
#         ]
#     for i in add:
#         user = User.objects.create(username=i['username'], email=i['email'], first_name=i['first_name'], last_name=i['last_name'])
#         user.set_password(i['password'])
#         Profile.objects.create(user_id=user.id, student=True)
#         user.save()
#     return HttpResponse("successfull")

def student_home(request):
    return render(request, 'stu_dash/students_dashboard.html')

def student_courses(request):
    return render(request, 'stu_dash/students_course.html',{"l":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})