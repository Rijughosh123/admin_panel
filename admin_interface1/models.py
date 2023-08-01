from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=1000)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id

class CourseDetails(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=100000)
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
    base_technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    