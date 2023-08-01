from django.urls import path, include
from .import views 
urlpatterns = [
    path('home/', views.home),
    path('my_store/', views.my_store),
    path('course/', views.course),
    path('chat/', views.chat),
    path('team/', views.team),
    path('calendar/', views.calendar),
    path('invitation_link/', views.invitation_link),
    path('start_exam/', views.start_exam)
]