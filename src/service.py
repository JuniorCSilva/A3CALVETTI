# src/service.py

from typing import List
from repository import TaskRepository

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo
        self.tasks: List[str] = repo.load()

    def add_task(self, description: str):
        if not description.strip():
            raise ValueError("Task description cannot be empty.")
        self.tasks.append(description)
        self.repo.save(self.tasks)

    def remove_task(self, description: str):
        if description not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks.remove(description)
        self.repo.save(self.tasks)

    def list_tasks(self) -> List[str]:
        return self.tasks.copy()
