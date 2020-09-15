from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_in, name='login'),
    path('accounts/login/', views.GoogleLogin, name='googlelogin'),
    path('logout', views.log_out, name='logout'),
    path('profile', views.profile, name='profile')
]
