from django.shortcuts import render, redirect
from subjects.models import WtLab, AcA, ML, SaN, CC, MlLab, WT, project
from students.models import StudentDetails

# Create your views here.


def teachers(request):
    return redirect('teacherprofile')


def teacherProfile(request):

    context = {
        'topic': ML.objects.all()
    }
    return render(request, 'teachers/profile/index.html', context)


def studentsList(request):
    context = {
        'students': StudentDetails.objects.all()
    }
    return render(request, 'teachers/studentsdetails/index.html', context)


def createClass(request, slug):
    context = {

    }
    return render(request, 'teachers/createclass/index.html')
