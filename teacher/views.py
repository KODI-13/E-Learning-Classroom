from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from teacher.models import Course, Teachers, Video



# Create your views here.
def register(request):
    if request.method == 'POST':
        cn = request.POST.get('name')
        im = request.FILES.get('img','default.jpg')
        qu = request.POST.get('qualify')
        ex = request.POST.get('expert')
        un = request.POST.get('username')
        ps = request.POST.get('password')
        data = Teachers(name=cn,image=im,qualification=qu,experience=ex,uniqueid=un,password=ps)
        data.save()
        return redirect('/tlogin/')

    return render(request,'teacher/register.html')

def tlogin(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')  # Assuming username is passed via GET request
        user=Teachers.objects.all()
        for i in user:
                if i.uniqueid == input_username:
                    if i.is_approved == True:
                        return redirect('/teacher_profile/{}/'.format(i.id)) # Redirect to the dashboard page upon successful login
                    else:
                        return HttpResponse("<script>alert('Teacher is not approved yet by admin, please contact admin');</script>")
                else:
                    continue
    return render(request,'teacher/tlogin.html')

def teacher_profile(request,id):
    teacher= Teachers.objects.get(id=id)
    data = Teachers.objects.get(id=id)
    courses = teacher.courses.all()
    request.session['teacher_id'] = id
    num=0
    for i in courses:
        num = num + 1
    return render(request,'teacher/teacher_profile.html', {'teacher': teacher, 'courses': courses,'data':data, 'num':num})

def add(request, id):
    data = Teachers.objects.get(id=id)
    context = {'data': data}
    if request.method == 'POST':
        title = request.POST['title']
        thumbnail = request.FILES['thumbnail']
        # video = request.FILES['video']
        teacher_id = id
        
        course = Course.objects.create(
            title=title,
            thumbnail=thumbnail,
            # video=video,
            teacher_id=teacher_id
        )
        # Optionally, you can perform additional actions after saving the course.
        # For example, you can redirect the user to a success page.
        return redirect('/add/{}/'.format(id))  # Replace 'success_page' with the name of your success page URL pattern
        
    return render(request, 'teacher/add.html', context)

def playlist(request,id):
    teacher_id = request.session.get('teacher_id')
    course = Course.objects.get(id=id)
    request.session['course_id'] = id
    if request.method == 'POST':
        # Assuming you have a form to add videos to the playlist
        caption = request.POST['caption']
        video_file = request.FILES['video']
        thumbnail_file = request.FILES.get('thumbnail')

        # Create a new Video object associated with the course
        video = Video.objects.create(course=course, caption=caption, video_file=video_file, thumbnail=thumbnail_file)

        # Optionally, you can perform additional actions after saving the video.
        # For example, you can redirect the user to a success page or reload the playlist page.

    # Retrieve all videos associated with the course
    videos = course.videos.all()
    data = get_object_or_404(Teachers, id=teacher_id) if teacher_id else None
    context = {
        'course': course,
        'videos': videos,
        'data': data,
    }
    return render(request, 'teacher/playlist.html',context)


def cedit(request,id):
    teacher_id = request.session.get('teacher_id')  # Retrieve student ID from session
    data = get_object_or_404(Teachers, id=teacher_id) if teacher_id else None
    course = Course.objects.get(id=id)
    context={
        'course':course,
        'data':data
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        thumbnail = request.FILES.get('thumbnail')
        teacher_id=teacher_id 
        course.title = title
        course.thumbnail = thumbnail
        course.save()
        return redirect("/teacher_profile/{}/".format(teacher_id))
    return render(request, 'teacher/cedit.html',context)

def delete(request,id):
    teacher_id = request.session.get('teacher_id')  # Retrieve student ID from session
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/teacher_profile/{}/".format(teacher_id))

def playedit(request,id):
    teacher_id = request.session.get('teacher_id')
    data = get_object_or_404(Teachers, id=teacher_id) if teacher_id else None
    course_id = request.session.get('course_id') 
    video = Video.objects.get(id=id)
    context = {
        'video':video,
        'data':data
    }
    if request.method == 'POST':
        # Assuming you have a form to add videos to the playlist
        caption = request.POST.get('caption')
        video_file = request.FILES.get('video')
        thumbnail_file = request.FILES.get('thumbnail')
        video.caption = caption
        video.video_file = video_file
        video.thumbnail = thumbnail_file
        video.save()
        return redirect("/playlist/{}/".format(course_id))
    return render(request,'teacher/playedit.html', context)

def playdelete(request,id):
    course_id = request.session.get('course_id')  # Retrieve student ID from session
    video = Video.objects.get(id=id)
    video.delete()
    return redirect("/playlist/{}/".format(course_id))

def t_update(request,id):
    teacher_id = request.session.get('teacher_id')  # Retrieve student ID from session
    teacher = Teachers.objects.get(id=id)
    context ={
        'teacher_id':teacher_id,
        'teacher':teacher
    }
    if request.method == 'POST':
        cn = request.POST.get('name')
        im = request.FILES.get('img','default.jpg')
        qu = request.POST.get('qualify')
        ex = request.POST.get('expert')
        teacher.name = cn
        teacher.image = im
        teacher.qualification = qu
        teacher.experience = ex
        teacher.save()
        return redirect("/teacher_profile/{}/".format(teacher_id))
    return render(request,'teacher/t_update.html', context)