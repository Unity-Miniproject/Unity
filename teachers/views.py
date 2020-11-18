from django.shortcuts import render, redirect

# Create your views here.
def teacherProfile(request):
    return render(request, 'teachers/profile/index.html')