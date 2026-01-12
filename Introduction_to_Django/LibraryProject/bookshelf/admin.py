from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search box for title and author
    search_fields = ('title', 'author')
    
    # Add filters for publication_year
    list_filter = ('publication_year',)

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
