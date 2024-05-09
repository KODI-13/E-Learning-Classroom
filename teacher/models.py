from django.db import models

from myapp.models import Student

# Create your models here.
class Teachers(models.Model):
    name=models.CharField(max_length=200,null=True)
    uniqueid=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    qualification=models.CharField(max_length=200,null=True)
    experience=models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='teacher_images', default='default.jpg',null=True)
    is_approved = models.BooleanField(default=False)

class Course(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='course_thumbnails', null=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField(Student, related_name='courses')

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    caption = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='course_videos')
    thumbnail = models.ImageField(upload_to='video_thumbnails', null=True)




# video = models.FileField(upload_to='course_videos', null=True)
