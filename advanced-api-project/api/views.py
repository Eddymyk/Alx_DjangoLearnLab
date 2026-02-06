from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# -------------------------------
# Author API (read-only)
# -------------------------------
class AuthorListAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


# -------------------------------
# Book API (CRUD with permissions)
# -------------------------------
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable search and ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly()]


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [IsAuthenticatedOrReadOnly()]


# -----------------
# Wrapper classes
# -----------------
class ListView(BookListCreateAPIView):
    pass

class DetailView(BookRetrieveUpdateDestroyAPIView):
    pass

class CreateView(BookListCreateAPIView):
    pass

class UpdateView(BookRetrieveUpdateDestroyAPIView):
    pass

class DeleteView(BookRetrieveUpdateDestroyAPIView):
    pass
