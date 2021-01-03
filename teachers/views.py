from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import render, redirect
from students.models import StudentDetails
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from subjects.models import newClasses

@login_required
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def teacherlogin(self):
        if login_required():
            return redirect('teacherprofile')
        else:
            return redirect('googlelogin')


@login_required
def teachers(request):
    return redirect('teacherprofile')


@login_required
def teacherProfile(request):

    context = {
        'classes' : newClasses.objects.filter(author=request.user)
    }
    return render(request, 'teachers/profile/index.html', context)


@login_required
def studentsList(request):
    context = {
        'students': StudentDetails.objects.all()
    }
    return render(request, 'teachers/studentsdetails/index.html', context)


@login_required
def createClass(request, slug):
    context = {

    }
    return render(request, 'teachers/createclass/index.html')



def viewClass(request, slug):
    context = {
    }
    return render(request,'teachers/classdetails/index.html')