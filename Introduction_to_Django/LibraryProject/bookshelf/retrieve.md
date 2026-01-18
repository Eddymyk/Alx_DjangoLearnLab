
---

## 2️⃣ `retrieve.md`

```md
## Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year
