from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, register
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/books/"), name="home"),  # Redirect root to /books/
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", register, name="register"),
]
