# src/app.py

from repository import TaskRepository
from service import TaskService

def menu():
    print("\n1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")

def executar():
    service = TaskService(TaskRepository())

    while True:
        menu()
        choice = input("Escolha: ")

        try:
            if choice == "1":
                desc = input("Descrição: ")
                service.add_task(desc)
                print("Tarefa adicionada.")
            
            elif choice == "2":
                desc = input("Tarefa: ")
                service.remove_task(desc)
                print("Tarefa removida.")
            
            elif choice == "3":
                tasks = service.list_tasks()
                print("\nSuas tarefas:")
                for t in tasks:
                    print(f"- {t}")
            
            elif choice == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)
