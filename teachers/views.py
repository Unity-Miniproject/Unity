from django.shortcuts import render, redirect
from subjects.models import WtLab, AcA, ML, SaN, CC, MlLab, WT, project


# Create your views here.

def teachers(request):
    return redirect('teacherprofile')


def teacherProfile(request):

    context = {
        'topic': ML.objects.all()
    }
    return render(request, 'teachers/profile/index.html', context)
