# src/repository/user_repo.py

class UserRepository:
    def __init__(self, filepath="users.txt"):
        self.filepath = filepath

    def load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines() if line.strip()]
        except FileNotFoundError:
            return []

    def save(self, users):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.writelines(u + "\n" for u in users)
