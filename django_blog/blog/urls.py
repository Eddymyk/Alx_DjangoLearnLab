from django.urls import path
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
    add_comment,
    edit_comment,
    delete_comment
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

    path('post/<int:post_id>/comments/new/', add_comment, name='comment-add'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='comment-edit'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='comment-delete'),


    # Authentication
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
