# relationship_app/urls.py
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # import all views

urlpatterns = [
    path("", RedirectView.as_view(url="/books/"), name="home"),
    path("books/", views.list_books, name="list_books"),  # use views.list_books
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),  # use views.register
]
