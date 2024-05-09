from django.contrib import admin

from teacher.models import Course, Teachers, Video

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Course)
admin.site.register(Video)

