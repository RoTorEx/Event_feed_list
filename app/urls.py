from django.urls import path

from .views import AchievementListView, PostDetailView, PostListView, UserDetailView


urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('post/<int:pk>/', PostListView.as_view()),
    path('post/<int:pk>/<str:title>/', PostDetailView.as_view()),
    path('achievement/<int:pk>/', AchievementListView.as_view()),
]
