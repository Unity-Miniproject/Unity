from django.urls import path
from . import views
urlpatterns = [
    path('', views.teachers, name='teacher'),
    path('profile', views.teacherProfile, name='teacherprofile'),
    path('students', views.studentsList, name='studentslist'),
    path('create/<slug:slug>', views.createClass, name='createclass'),
    path('class/<slug:slug>', views.viewClass, name='viewclass'),
    path('class/<slug:slug>/notes', views.classNotes, name='classnotes'),
]
