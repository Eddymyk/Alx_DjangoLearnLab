from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('books/create', BookListCreateAPIView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-delete'),
]

