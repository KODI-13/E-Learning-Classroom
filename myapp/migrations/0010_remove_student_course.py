# Generated by Django 5.0.3 on 2024-03-28 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
    ]
