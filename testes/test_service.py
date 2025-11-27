# tests/test_service.py

import pytest
from src.service import TaskService
from src.repository import TaskRepository

class FakeRepo(TaskRepository):
    def __init__(self):
        self.saved_data = []
    def load(self):
        return []
    def save(self, tasks):
        self.saved_data = tasks

def test_add_task():
    repo = FakeRepo()
    service = TaskService(repo)
    service.add_task("Estudar")
    assert "Estudar" in repo.saved_data

def test_add_empty_task():
    repo = FakeRepo()
    service = TaskService(repo)
    with pytest.raises(ValueError):
        service.add_task("")

def test_remove_task():
    repo = FakeRepo()
    service = TaskService(repo)
    service.add_task("A")
    service.remove_task("A")
    assert repo.saved_data == []

def test_remove_nonexistent():
    repo = FakeRepo()
    service = TaskService(repo)
    with pytest.raises(ValueError):
        service.remove_task("Z")
