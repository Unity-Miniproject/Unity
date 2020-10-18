from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_in, name='login'),
    path('accounts/login/', views.GoogleLogin, name='googlelogin'),
    path('logout', views.log_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/<slug:slug>', views.viewProfile, name='profile'),
    path('profile/<slug:slug>/editprofile', views.editProfile, name='editprofile'),
    path("profile/<slug:slug>/", views.subjects, name="subjects"),
    path("profile/<slug:slug>/classes", views.classes, name="classes"),
    path("profile/<slug:slug>/assignments", views.assignments, name="assignments"),
]
