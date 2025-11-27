# src/service/user_service.py

from src.repository.user_repo import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.users = repo.load()

    def add_user(self, name: str):
        name = name.strip()
        if not name:
            raise ValueError("Nome vazio.")
        if name in self.users:
            raise ValueError("Usuário já existe.")
        self.users.append(name)
        self.repo.save(self.users)

    def list_users(self):
        return self.users.copy()
