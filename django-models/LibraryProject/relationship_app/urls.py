# relationship_app/urls.py


from django.urls import path
from django.views.generic import RedirectView
from .views import (
    list_books,
    LibraryDetailView,
    UserLoginView,
    UserLogoutView,
    register
)

urlpatterns = [
    # Redirect root URL to /books/
    path("", RedirectView.as_view(url="/books/"), name="home"),

    # Book views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication views
    path("login/", UserLoginView.as_view(), name="login"),            # Login page
    path("logout/", UserLogoutView.as_view(), name="logout"),          # Logout (POST)
    path("register/", register, name="register"),                      # Registration
]
