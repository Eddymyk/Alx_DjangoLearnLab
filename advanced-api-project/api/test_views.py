from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author2)

        # URLs
        self.list_url = reverse('book-list')  # /api/books/
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])  # /api/books/<id>/

    # ----------------------
    # TEST LISTING BOOKS
    # ----------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    # ----------------------
    # TEST CREATING BOOK
    # ----------------------
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Permission denied

    # ----------------------
    # TEST RETRIEVE BOOK
    # ----------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ----------------------
    # TEST UPDATE BOOK
    # ----------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {"title": "Updated Book"}
        response = self.client.patch(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Updated Book"}
        response = self.client.patch(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------
    # TEST DELETE BOOK
    # ----------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------
    # TEST FILTERING, SEARCH, ORDERING
    # ----------------------
    def test_filter_by_author(self):
        response = self.client.get(self.list_url, {'author__name': 'Author One'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_search_by_title(self):
        response = self.client.get(self.list_url, {'search': 'Book Two'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_order_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.data[0]['publication_year'], 2021)
