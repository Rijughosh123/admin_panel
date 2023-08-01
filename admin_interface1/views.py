from django.shortcuts import render
from .models import CourseDetails,Technology
from django.contrib.auth.models import User
def home(req):
    total_courses = CourseDetails.objects.all().count()
    total_students = User.objects.all().count()
    print(total_courses,total_students)
    active_page = 'dashboard'
    return render(req, "dashboard.html", {'active_page': active_page,'total_courses':total_courses, 'total_students':total_students})

def my_store(request):
    active_page = 'my_store'
    return render(request, "my_store.html",{'active_page': active_page})

def course(request):
    if request.method == 'POST':
        try:
            selected_value = request.POST['techno']
            if selected_value is not None:
                obj = CourseDetails.objects.filter(base_technology_id=int(selected_value)).values()
                tech = Technology.objects.all()
                selected = Technology.objects.filter(id=int(selected_value)).values('name')[0]
                active_page = 'course'
                return render(request, "course.html",{'active_page': active_page, 'course_details':obj, 'tech':tech, 'selected':selected['name']})
        except:
            name = request.POST['course_titel']
            description = request.POST['course_description']
            price = request.POST['course_price']
            duration = request.POST['course_duration']
            base_tech = int(request.POST['base_tech'])
            CourseDetails.objects.create(name=name, description=description, price=price, duration=duration, base_technology_id=base_tech)
    obj = CourseDetails.objects.all()
    tech = Technology.objects.all()
    active_page = 'course'
    return render(request, "course.html",{'active_page': active_page, 'course_details':obj, 'tech':tech})

# def course_details(request):
#     if request.method == 'POST':
#         name = request.POST['course_titel']
#         description = request.POST['course_description']
#         price = request.POST['course_price']
#         duration = request.POST['course_duration']
#         base_tech = int(request.POST['base_tech'])
#         CourseDetails.objects.create(name=name, description=description, price=price, duration=duration, base_technology_id=base_tech) 
#     obj = CourseDetails.objects.all()
#     tech = Technology.objects.all()
#     active_page = 'course'
#     return render(request, "course.html",{'active_page': active_page, 'course_details':obj, 'tech':tech})

def chat(req):
    active_page = 'chat'
    return render(req, "chat.html",{'active_page': active_page})

def team(req):
    active_page = 'team'
    return render(req, "team.html",{'active_page': active_page})

def calendar(req):
    active_page = 'calendar'
    return render(req, "calendar.html",{'active_page': active_page})

def invitation_link(req):
    return render(req, "invitation_link.html")

def start_exam(req):
    return render(req, "start_exam.html")