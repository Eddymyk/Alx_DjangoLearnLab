from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author():
    """
    Query all books written by J.K Rowling.
    """
    books = Book.objects.filter(author__name="J.K Rowling")
    return books


def list_all_books_in_library():
    """
    List all books in Central Library.
    """
    library = Library.objects.get(name="Central Library")
    return library.books.all()


def retrieve_librarian_for_library():
    """
    Retrieve the librarian for Central Library.
    """
    library = Library.objects.get(name="Central Library")
    return library.librarian


# Example execution (for testing purposes)
if __name__ == "__main__":
    print("Books by J.K Rowling:")
    for book in query_books_by_author():
        print(book.title)

    print("\nBooks in Central Library:")
    for book in list_all_books_in_library():
        print(book.title)

    print("\nLibrarian of Central Library:")
    librarian = retrieve_librarian_for_library()
    print(librarian.name)
