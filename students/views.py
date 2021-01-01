from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.db import DatabaseError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import StudentDetails


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
        if login_required():
            return render(request, 'students/dashboard.html')


@login_required(redirect_field_name='login')
def viewProfile(request, slug):
    current_user = request.user
    try:
        context = {
            'details': StudentDetails.objects.get(user_id=current_user.id)
        }
        return render(request, 'students/profile.html', context)
    except StudentDetails.DoesNotExist:
        return redirect('editprofile', slug)


@login_required(redirect_field_name='login')
def editProfile(request, slug):
    current_user = request.user
    context = {
        'details': StudentDetails.objects.get(user_id=current_user.id)
    }
    return render(request, 'students/editprofile.html', context)


@login_required(redirect_field_name='login')
def subjects(request, slug):
    return render(request, 'subjects/index.html')


@login_required(redirect_field_name='login')
def classes(request, slug):
    return render(request, 'subjects/index.html')


@login_required(redirect_field_name='login')
def assignments(request, slug):
    return render(request, 'assignments/index.html')


@login_required(redirect_field_name='login')
def notes(request, slug):
    return render(request, 'notes/index.html')
