# Generated by Django 5.0.3 on 2024-03-28 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]
