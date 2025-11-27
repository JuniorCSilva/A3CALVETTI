# original/library_original.py
# Código legado intencionalmente ruim — mistura de I/O, lógica e persistência

users = []
books = []
reservations = []

def load():
    try:
        f = open("db.txt","r")
        for l in f:
            parts = l.strip().split(";")
            if parts[0] == "user":
                users.append(parts[1])
            elif parts[0] == "book":
                books.append(parts[1])
            elif parts[0] == "reservation":
                reservations.append((parts[1], parts[2], parts[3]))
        f.close()
    except:
        print("Erro ao carregar")

def save():
    f = open("db.txt","w")
    for u in users:
        f.write("user;" + u + "\n")
    for b in books:
        f.write("book;" + b + "\n")
    for r in reservations:
        f.write("reservation;" + r[0] + ";" + r[1] + ";" + r[2] + "\n")
    f.close()

def add_user():
    u = input("Nome usuario: ")
    users.append(u)
    save()

def add_book():
    b = input("Nome livro: ")
    books.append(b)
    save()

def reserve():
    u = input("Usuario: ")
    b = input("Livro: ")
    d = input("Data (YYYY-MM-DD): ")
    if u not in users:
        print("User not exists")
        return
    if b not in books:
        print("Book not exists")
        return
    for r in reservations:
        if r[1] == b:
            print("Book already reserved")
            return
    reservations.append((u,b,d))
    save()

def cancel():
    u = input("Usuario: ")
    b = input("Livro: ")
    for r in reservations:
        if r[0] == u and r[1] == b:
            reservations.remove(r)
            save()
            return
    print("Reservation not found")

def show():
    for r in reservations:
        print(r)

def main():
    load()
    while True:
        print("1 add user")
        print("2 add book")
        print("3 reserve")
        print("4 cancel")
        print("5 show")
        print("6 exit")
        c = input("choice:")
        if c == "1":
            add_user()
        elif c == "2":
            add_book()
        elif c == "3":
            reserve()
        elif c == "4":
            cancel()
        elif c == "5":
            show()
        elif c == "6":
            break
        else:
            print("Erro")

if __name__ == "__main__":
    main()
