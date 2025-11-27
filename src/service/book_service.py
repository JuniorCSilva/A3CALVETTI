# src/service/book_service.py

from src.repository.book_repo import BookRepository

class BookService:
    def __init__(self, repo: BookRepository):
        self.repo = repo
        self.books = repo.load()

    def add_book(self, title: str):
        title = title.strip()
        if not title:
            raise ValueError("Título vazio.")
        if title in self.books:
            raise ValueError("Livro já existe.")
        self.books.append(title)
        self.repo.save(self.books)

    def list_books(self):
        return self.books.copy()
