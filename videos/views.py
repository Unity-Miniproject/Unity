from django.shortcuts import render
from .models import videoLink
from django.http import Http404

# Create your views here.


def videos(request):
    context = {
        'videos': videoLink.objects.all()
    }
    return render(request, 'videos/index/index.html', context)


def PlayVideo(request, slug):
    try:
        display = videoLink.objects.get(link=slug)
    except videoLink.DoesNotExist:
        raise Http404("Video Does Not Exist.")
    context = {
        'display': display,
        'videos': videoLink.objects.all()
    }
    return render(request, 'videos/playvideo/play.html', context)
