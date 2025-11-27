# src/domain/reservation.py

class Reservation:
    def __init__(self, user: str, book: str, date: str):
        if not user or not book or not date:
            raise ValueError("Dados da reserva incompletos.")
        self.user = user
        self.book = book
        self.date = date

    def to_tuple(self):
        return (self.user, self.book, self.date)

    def __repr__(self):
        return f"Reservation(user='{self.user}', book='{self.book}', date='{self.date}')"
