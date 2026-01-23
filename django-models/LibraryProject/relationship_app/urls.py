# relationship_app/urls.py

from django.urls import path
from django.views.generic import RedirectView
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", RedirectView.as_view(url="/books/"), name="home"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Use Django built-in LoginView and LogoutView directly
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    
    # Register view
    path("register/", register, name="register"),
]
