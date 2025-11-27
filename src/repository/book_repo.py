# src/repository/book_repo.py

class BookRepository:
    def __init__(self, filepath="books.txt"):
        self.filepath = filepath

    def load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            return []

    def save(self, books):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.writelines(b + "\n" for b in books)
