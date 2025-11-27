# src/app.py

from src.repository.user_repo import UserRepository
from src.repository.book_repo import BookRepository
from src.repository.reservation_repo import ReservationRepository
from src.service.user_service import UserService
from src.service.book_service import BookService
from src.service.reservation_service import ReservationService

def menu():
    print("""
== Gerenciador de Reservas - Biblioteca ==
1 - Cadastrar usuário
2 - Cadastrar livro
3 - Reservar livro
4 - Cancelar reserva
5 - Listar reservas
6 - Listar usuários
7 - Listar livros
8 - Sair
""")

def executar():
    user_repo = UserRepository()
    book_repo = BookRepository()
    res_repo = ReservationRepository()

    user_service = UserService(user_repo)
    book_service = BookService(book_repo)
    res_service = ReservationService(res_repo)

    while True:
        menu()
        c = input("Escolha: ").strip()
        try:
            if c == "1":
                name = input("Nome do usuário: ")
                user_service.add_user(name)
                print("Usuário cadastrado com sucesso.")
            elif c == "2":
                title = input("Título do livro: ")
                book_service.add_book(title)
                print("Livro cadastrado com sucesso.")
            elif c == "3":
                user = input("Usuário: ")
                book = input("Livro: ")
                date = input("Data (YYYY-MM-DD): ")
                res_service.reserve(user, book, date, user_service.users, book_service.books)
                print("Reserva efetuada.")
            elif c == "4":
                user = input("Usuário: ")
                book = input("Livro: ")
                res_service.cancel(user, book)
                print("Reserva cancelada.")
            elif c == "5":
                print("\nReservas:")
                for r in res_service.list_reservations():
                    print(f"- Usuário: {r[0]} | Livro: {r[1]} | Data: {r[2]}")
            elif c == "6":
                print("\nUsuários:")
                for u in user_service.list_users():
                    print(f"- {u}")
            elif c == "7":
                print("\nLivros:")
                for b in book_service.list_books():
                    print(f"- {b}")
            elif c == "8":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    executar()
