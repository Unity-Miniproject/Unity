from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.db import DatabaseError
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import StudentDetails
from subjects.models import newClasses
from dynamic_models.models import ModelSchema
from subjects.models import Branch, Section, Semester

# Create your views here.

def log_in(request):
    if login_required():
        return redirect('profile')
    else:
        return redirect('googlelogin')


def log_out(request):
    logout(request)
    return redirect('/')


def GoogleLogin(request):
    return render(request, 'logins/login.html')


@login_required(redirect_field_name='googlelogin')
def profile(request):
    current_user = request.user
    if current_user.is_staff:
        return redirect('teacherprofile')
    else :
        try:
            details = StudentDetails.objects.get(user_id=request.user.id)
            if login_required():
                context = {
                    'classes': newClasses.objects.filter(classBranch=details.branch, classSemester=details.semester, classSection=details.section)
                }
                return render(request, 'students/dashboard.html', context)
        except StudentDetails.DoesNotExist:
            return render(request, 'students/dashboard.html')

@login_required(redirect_field_name='login')
def viewProfile(request, slug):
    current_user = request.user
    
    try:
        context = {
            'details': StudentDetails.objects.get(user_id=current_user.id),
        }
        return render(request, 'students/profile.html', context)
    except StudentDetails.DoesNotExist:
        return redirect('editprofile', slug)


@login_required(redirect_field_name='login')
def editProfile(request, slug):
    try : 
        if request.POST:
            studentName = request.POST['studentname']
            studentUsn = request.POST['studentusn']
            studentBranch = request.POST['studentbranch']
            studentSemester = request.POST['studentsemester']
            studentSection = request.POST['studentsection']
            print(studentBranch)
            StudentDetails.objects.create(
                user = request.user,
                usn=studentUsn,
                email=request.user.email,
                name=studentName, 
                section=studentSection, 
                branch=studentBranch, 
                semester=studentSemester)
            return render(request, 'students/dashboard.html')
    except DatabaseError:
        return render(request, 'errorpage/index.html')
    context = {
        'branch': Branch.objects.all(),
        'semester': Semester.objects.all(),
        'section': Section.objects.all(),
    }
    return render(request, 'students/editprofile.html', context)


@login_required(redirect_field_name='login')
def subjects(request, slug):
    model = ModelSchema.objects.get(name=slug).as_model()
    context = {
        'classDetails': model.objects.all().order_by('completed_date').reverse()
    }
    
    return render(request, 'subjects/index.html', context)


@login_required(redirect_field_name='login')
def classes(request, slug):
    return render(request, 'subjects/index.html')


@login_required(redirect_field_name='login')
def assignments(request, slug):
    return render(request, 'assignments/index.html')


@login_required(redirect_field_name='login')
def notes(request, slug):
    return render(request, 'notes/index.html')


def updateprofile(request, slug):
    if request.POST:
        try:
            t = StudentDetails.objects.get(user_id=request.user.id)
            studentName = request.POST['studentname']
            studentUsn = request.POST['studentusn']
            studentBranch = request.POST['studentbranch']
            studentSemester = request.POST['studentsemester']
            studentSection = request.POST['studentsection']
            t.usn=studentUsn,
            t.email=request.user.email,
            t.name=studentName, 
            t.section=studentSection, 
            t.branch=studentBranch, 
            t.semester=studentSemester
            t.save()
        except DatabaseError:
            return render(request, 'errorpage/index.html')
    context = {
        'details': StudentDetails.objects.get(user_id=request.user.id),
        'branch' : Branch.objects.all(),
        'semester' : Semester.objects.all(),
        'section' : Section.objects.all(),
    }
    return render(request, 'students/updateprofile.html', context)

