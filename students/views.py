from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def log_in(request):
    if login_required():
        return redirect('profile')
    else:
        return redirect('googlelogin')



def log_out(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect('/')


def GoogleLogin(request):
    return render(request, 'logins/login.html')


@login_required(redirect_field_name='googlelogin')
def profile(request):
    if login_required():
        return render(request, 'students/dashboard.html')
