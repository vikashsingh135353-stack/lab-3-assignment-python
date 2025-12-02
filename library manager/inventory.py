## Author: Vikash rawat
import json
from pathlib import Path
from .book import Book
import logging

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, path="catalog.json"):
        self.path = Path(path)
        self.books = []
        self.load()

    def add_book(self, book: Book):
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("ISBN already exists.")
        self.books.append(book)
        self.save()

    def search_by_title(self, q):
        q = q.lower()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return list(self.books)

    def save(self):
        data = [b.to_dict() for b in self.books]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self):
        try:
            if not self.path.exists():
                self.books = []
                return
            raw = self.path.read_text(encoding="utf-8")
            data = json.loads(raw)
            self.books = [Book(**x) for x in data]
        except Exception:
            self.books = []