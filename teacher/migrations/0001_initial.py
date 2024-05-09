# Generated by Django 5.0.3 on 2024-03-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('uniqueid', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('qualification', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(default='default.jpg', null=True, upload_to='teacher_images')),
            ],
        ),
    ]