# urls.py
from django.urls import path
from django.views.generic import RedirectView
from . import views  # import your views module

urlpatterns = [
    path("", RedirectView.as_view(url="/books/"), name="home"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Use your custom login/logout views
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),

    # Register
    path("register/", views.register, name="register"),
]
