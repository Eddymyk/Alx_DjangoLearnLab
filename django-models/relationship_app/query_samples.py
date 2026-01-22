from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# 2️⃣ List all books in a library
def books_in_library(library_name):
    return Book.objects.filter(libraries__name=library_name)

# 3️⃣ Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
