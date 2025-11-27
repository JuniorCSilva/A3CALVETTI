# src/domain/user.py

class User:
    def __init__(self, name: str):
        if not name or not name.strip():
            raise ValueError("Nome de usuário inválido.")
        self.name = name.strip()

    def __repr__(self):
        return f"User(name='{self.name}')"
