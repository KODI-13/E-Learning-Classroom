from django.shortcuts import get_object_or_404, redirect, render

from myapp.models import Student
from teacher.models import Course, Teachers

# from myapp.models import Student

# Create your views here.
def login(request):
    if request.method == 'POST':
        input_username = request.POST.get('username')  # Assuming username is passed via GET request
        user=Student.objects.all()
        for i in user:
                if i.uniqueid == input_username:
                    return redirect('/home/{}/'.format(i.id),{'id':i.id}) # Redirect to the dashboard page upon successful login
                else:
                    continue
    return render(request,'myapp/login.html')

def new(request):
    # request.session['student_id'] = id
    if request.method == 'POST':
        cn = request.POST.get('name')
        image = request.FILES.get('image')
        ct = request.POST.get('city')
        un = request.POST.get('username')
        ps = request.POST.get('password')
        data = Student(name=cn,image=image,city=ct,uniqueid=un,password=ps)
        data.save()
        return redirect('/login/')
    return render(request,'myapp/new.html')

def home(request,id=None):
    if id is None:
        s_data,id = None,None
        context={
            's_data':s_data,
            'id':id
        }
        return render(request, "myapp/home.html",context)

    s_data=Student.objects.get(id=id)
    request.session['student_id'] = id
    data1 = Course.objects.filter(students=s_data)
    context={
            's_data':s_data,
            'data1':data1
        }
    return render(request, "myapp/home.html",context)

def course(request,id=None):
    if id is None:
        s_data = None
        id = None
        request.session['student_id'] = id
        data1=Course.objects.all()
        context={
            's_data':s_data,
            'id':id,
            'data1':data1
        }
        return render(request, "myapp/course.html", context)
    
    s_data = get_object_or_404(Student, id=id)
    request.session['student_id'] = id
    data1=Course.objects.all() 
    context={
        's_data':s_data,
        'data1':data1
    }
    return render(request,'myapp/course.html',context)


def teachers(request,id=None):
    if id is None:
        s_data = None
        id = None
        request.session['student_id'] = id
        data1 = Teachers.objects.all()
        context={
            's_data':s_data,
            'data1':data1,
            'id':id
        }
        return render(request, "myapp/teachers.html", context)
    s_data = get_object_or_404(Student, id=id)
    # Store the id parameter in the session
    request.session['student_id'] = id
    # Retrieve all teachers
    data1 = Teachers.objects.all()
    context={
        's_data':s_data,
        'data1':data1
    }
    return render(request,'myapp/teachers.html', context)

def t_profile(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    student_id = request.session.get('student_id')  # Retrieve student ID from session
    s_data = get_object_or_404(Student, id=student_id) if student_id else None  # Retrieve student based on ID or None if not found
    courses = teacher.courses.all()
    num=0
    for i in courses:
        num = num + 1
    return render(request, 'myapp/t_profile.html', {'teacher': teacher, 'courses': courses, 's_data': s_data,'num':num})


def t_playlist(request,id):
    course = Course.objects.get(id=id)
    videos = course.videos.all()
    data = course.teacher 
    student_id = request.session.get('student_id')  # Retrieve student ID from session
    s_data = get_object_or_404(Student, id=student_id) if student_id else None  # Retrieve student based on ID or None if not found
    context = {
        'course': course,
        'videos': videos,
        'data': data,
        's_data': s_data
    }
    return render(request, 'myapp/t_playlist.html', context)

def contact(request,id=None):
    if id is None:
        s_data = None
        context={
            's_data':s_data
        }
        return render(request, "myapp/contact.html",context)
    s_data=Student.objects.get(id=id)
    context={
        's_data':s_data
    }
    return render(request,'myapp/contact.html',context)

def about(request,id=None):
    if id is None:
        s_data = None
        context={
            's_data':s_data
        }
        return render(request, "myapp/about.html",context)
    s_data=Student.objects.get(id=id)
    context={
        's_data':s_data
    }
    return render(request,'myapp/about.html',context)


def purchase(request,id):
    student_id = request.session.get('student_id')
    if student_id == None:
        return redirect("/new/")
    course = Course.objects.get(id=id)
    videos = course.videos.all()
    data = course.teacher 
    student_id = request.session.get('student_id')  # Retrieve student ID from session
    s_data = get_object_or_404(Student, id=student_id) if student_id else None  # Retrieve student based on ID or None if not found
    course.students.add(s_data)
    course.save()
    context = {
        'course': course,
        'videos': videos,
        'data': data,
        's_data': s_data
    }
    return render(request, 'myapp/purchase.html', context)

def update(request,id):
    s_data=Student.objects.get(id=id)
    student_id = request.session.get('student_id')  
    context={
        's_data':s_data
    }
    if request.method == 'POST':
        cn = request.POST.get('name')
        im = request.FILES.get('image')
        ct = request.POST.get('city')
        s_data.name = cn
        s_data.image = im
        s_data.city = ct 
        s_data.save()
        return redirect("/home/{}/".format(student_id))
    return render(request,'myapp/update.html', context)


# def t_profile(request,id):
#     teacher= Teachers.objects.get(id=id)
#     data = Student.objects.get(id=id)
#     courses = teacher.courses.all()
#     return render(request,'myapp/t_profile.html', {'teacher': teacher, 'courses': courses, 'data':data})


# if request.method == 'POST':
#         course = Course.objects.get(id=id)
#         s_data = get_object_or_404(Student, id=student_id) if student_id else None  # Retrieve student based on ID or None if not found