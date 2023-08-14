from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from admin_interface1.models import CourseDetails,Technology
from django.contrib.auth import authenticate, login
from datetime import datetime

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
    user_id = 1
    context = {}
    data = {
        "act":"home",
        "user_name":"Riju Ghosh",
        "today_date":datetime.now(),
        "metting_details":[
            {"metting_for":"For Django class", "time":"12.05 PM"},
            {"metting_for":"For Angular class", "time":"15.05 PM"},
            {"metting_for":"For Fun class", "time":"10.05 AM"}
        ]
    }
    context.update(data)
    return render(request, 'stu_dash/students_dashboard.html', context)

def student_p_courses(request):
    context = {}
    all_course = CourseDetails.objects.all().values()
    context.update({"all_course":all_course, "act":"p_courses"})
    return render(request, 'stu_dash/students_p_course.html',context)

def student_courses(request):
    context = {}
    context.update({"act":"course","l":[1,2,3,4,5,6,7]})
    return render(request, 'stu_dash/students_courses.html',context)

def student_view_courses(request):
    context = {}
    context.update({"act":"course"})
    return render(request, 'stu_dash/students_view_courses.html',context)

def student_today_class(request):
    context = {}
    context.update({"act":"course"})
    return render(request, 'stu_dash/students_today_class.html',context)


def student_trophy(request):
    context ={}
    context.update({"act":"trophy"})
    return render(request, 'stu_dash/students_trophy.html',context)