from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views


urlpatterns = [
    #path("", views.blog_index, name="blog"),
    # path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path('', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', views.search, name='search'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("<category>/", views.blog_category, name="blog_category"),
]