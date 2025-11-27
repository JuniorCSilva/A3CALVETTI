# src/domain/book.py

class Book:
    def __init__(self, title: str):
        if not title or not title.strip():
            raise ValueError("Título de livro inválido.")
        self.title = title.strip()

    def __repr__(self):
        return f"Book(title='{self.title}')"
