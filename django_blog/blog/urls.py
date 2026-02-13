from django.urls import path
from . import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    login_view,
    logout_view,
    profile_view,
    home,
    PostByTagListView,
    search_posts
)
urlpatterns = [
    # Home page
    path('', home, name='home'),

    # Blog post CRUD
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('search/', views.search_posts, name='search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-new'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


    # Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

     # Tag filtering
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # Search
    path('search/', search_posts, name='search'),
]
