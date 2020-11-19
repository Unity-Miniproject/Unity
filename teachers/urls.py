from django.urls import path
from . import views
urlpatterns = [
    path('', views.teachers, name='teacher'),
    path('profile', views.teacherProfile, name='teacherprofile')
]