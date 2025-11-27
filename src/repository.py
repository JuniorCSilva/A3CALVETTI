# src/repository.py

from typing import List

class TaskRepository:
    def __init__(self, filepath: str = "tasks.txt"):
        self.filepath = filepath

    def load(self) -> List[str]:
        try:
            with open(self.filepath, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def save(self, tasks: List[str]):
        with open(self.filepath, "w") as f:
            f.writelines(task + "\n" for task in tasks)
