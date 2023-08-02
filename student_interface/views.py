from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from admin_interface1.models import CourseDetails,Technology
from django.contrib.auth import authenticate, login

def student_home(request):
    return render(request, 'home.html')

def student_login(request):
    print("hello")
    if request.method == 'POST':
        print("hello2")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        print(username,password)
        if user is not None:
            login(request, user)
            return redirect(student_dash) 
    return render(request, 'authenticate.html')

#-------------------- after Authentication ---------------------
def student_dash(request):
    return render(request, 'stu_dash/students_dashboard.html')

def student_p_courses(request):
    context = {}
    all_course = CourseDetails.objects.all().values()
    context.update({"all_course":all_course, "act":"p_courses"})
    return render(request, 'stu_dash/students_p_course.html',context)

def student_courses(request):
    context = {}
    context.update({"act":"course"})
    return render(request, 'stu_dash/students_courses.html',context)

def student_trophy(request):
    context ={}
    context.update({"act":"trophy"})
    return render(request, 'stu_dash/students_trophy.html',context)