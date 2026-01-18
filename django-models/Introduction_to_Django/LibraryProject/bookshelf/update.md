
---

## 3️⃣ `update.md`

```md
## Update Book

```python
from bookshelf.models import Book

# Update the title of the existing book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
