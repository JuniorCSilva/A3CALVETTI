# tests/test_reservation_service.py

import pytest
from src.service.reservation_service import ReservationService

class FakeRepo:
    def __init__(self):
        self.storage = []

    def load(self):
        return self.storage

    def save(self, reservations):
        self.storage = reservations

def test_reserve_success():
    repo = FakeRepo()
    service = ReservationService(repo)
    service.reserve("Ana", "Livro A", "2025-11-01", ["Ana"], ["Livro A"])
    assert repo.storage == [("Ana", "Livro A", "2025-11-01")]

def test_reserve_book_taken():
    repo = FakeRepo()
    service = ReservationService(repo)
    service.reserve("Ana", "Livro A", "2025-11-02", ["Ana"], ["Livro A"])
    with pytest.raises(ValueError):
        service.reserve("Joao", "Livro A", "2025-11-03", ["Ana","Joao"], ["Livro A"])

def test_cancel_success():
    repo = FakeRepo()
    service = ReservationService(repo)
    service.reserve("Ana", "Livro A", "2025-11-02", ["Ana"], ["Livro A"])
    service.cancel("Ana", "Livro A")
    assert repo.storage == []

def test_cancel_not_found():
    repo = FakeRepo()
    service = ReservationService(repo)
    with pytest.raises(ValueError):
        service.cancel("Ana", "Livro X")
