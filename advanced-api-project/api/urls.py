from django.urls import path
from .views import (
    AuthorListAPIView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),

    # Book CRUD endpoints
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

  
    path('books/list/', ListView.as_view(), name='book-list-view'),
    path('books/detail/<int:pk>/', DetailView.as_view(), name='book-detail-view'),
    path('books/create/', CreateView.as_view(), name='book-create-view'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update-view'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete-view'),
]
