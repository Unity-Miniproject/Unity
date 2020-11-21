from django.urls import path
from . import views
urlpatterns = [
    path('', views.videos, name='videos'),
    path('play/<slug:slug>', views.PlayVideo, name="playvideo")
]
