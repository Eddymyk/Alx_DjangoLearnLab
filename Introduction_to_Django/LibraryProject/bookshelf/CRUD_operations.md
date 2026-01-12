# Import the Book model
from bookshelf.models import Book

# --------------------
# CREATE
# --------------------
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book  

# --------------------
# RETRIEVE
# --------------------
Book.objects.all()  # Expected >

# --------------------
# UPDATE
# --------------------
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  

# --------------------
# DELETE
# --------------------
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()  
