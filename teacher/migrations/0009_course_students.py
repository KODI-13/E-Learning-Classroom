# Generated by Django 5.0.3 on 2024-03-28 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_student_course'),
        ('teacher', '0008_remove_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='myapp.student'),
        ),
    ]
