# src/service/reservation_service.py

from src.repository.reservation_repo import ReservationRepository

class ReservationService:
    def __init__(self, repo: ReservationRepository):
        self.repo = repo
        self.reservations = repo.load()  # list of tuples (user, book, date)

    def reserve(self, user: str, book: str, date: str, users_list, books_list):
        # validations
        if user not in users_list:
            raise ValueError("Usuário não existe.")
        if book not in books_list:
            raise ValueError("Livro não existe.")
        for u, b, _ in self.reservations:
            if b == book:
                raise ValueError("Livro já reservado.")
        self.reservations.append((user, book, date))
        self.repo.save(self.reservations)

    def cancel(self, user: str, book: str):
        before = len(self.reservations)
        self.reservations = [r for r in self.reservations if not (r[0] == user and r[1] == book)]
        if len(self.reservations) == before:
            raise ValueError("Reserva não encontrada.")
        self.repo.save(self.reservations)

    def list_reservations(self):
        return self.reservations.copy()
