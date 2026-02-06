from django.contrib import admin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters in the admin sidebar
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')
