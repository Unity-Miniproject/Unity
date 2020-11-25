from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_in, name='login'),
    path('accounts/login/', views.GoogleLogin, name='googlelogin'),
    path('logout', views.log_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/<slug:slug>', views.viewProfile, name='profile'),
    path('<slug:slug>/editprofile', views.editProfile, name='editprofile'),
    path('subject/<slug:slug>/', views.subjects, name='subjects'),
    path('<slug:slug>/classes', views.classes, name='classes'),
    path('<slug:slug>/assignments', views.assignments, name='assignments'),
    path('<slug:slug>/notes', views.notes, name='notes'),
]
