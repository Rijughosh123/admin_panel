from django.db import models
from django.contrib.auth.models import User
from admin_interface1.models import CourseDetails

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    profile_picture = models.FileField(upload_to="user_profile_pic/", null=True, blank=True)
    about = models.CharField(max_length=1000)

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Course = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)
    update = models.FloatField()