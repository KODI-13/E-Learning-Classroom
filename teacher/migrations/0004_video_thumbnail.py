# Generated by Django 5.0.3 on 2024-03-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_remove_course_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='video_thumbnails'),
        ),
    ]
