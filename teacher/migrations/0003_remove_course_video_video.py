# Generated by Django 5.0.3 on 2024-03-26 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('video_file', models.FileField(upload_to='course_videos')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='teacher.course')),
            ],
        ),
    ]
