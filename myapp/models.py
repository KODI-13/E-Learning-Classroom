from django.db import models

# Create your models here.
class Student(models.Model):
    uniqueid=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='student_images', default='default.jpg',null=True)

