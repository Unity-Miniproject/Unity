from django.urls import path
from . import views
from .views import PostListView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView, PostAnswerView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailedView.as_view(), name='detailed'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/answer/', PostAnswerView.as_view(), name='answer'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete')
]
