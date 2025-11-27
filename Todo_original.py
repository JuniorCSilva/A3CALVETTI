# todo_original.py

tasks = []

def load():
    try:
        f = open("tasks.txt", "r")
        for l in f:
            tasks.append(l.strip())
        f.close()
    except:
        print("File error")

def save():
    f = open("tasks.txt", "w")
    for t in tasks:
        f.write(t + "\n")
    f.close()

def add():
    t = input("Task: ")
    tasks.append(t)
    save()

def remove():
    n = input("Task to remove: ")
    if n in tasks:
        tasks.remove(n)
        save()
    else:
        print("Not found")

def show():
    print("Tasks:")
    for x in tasks:
        print(x)

def main():
    load()
    while True:
        print("1 add")
        print("2 remove")
        print("3 show")
        print("4 exit")
        c = input("choice:")
        if c == "1":
            add()
        elif c == "2":
            remove()
        elif c == "3":
            show()
        elif c == "4":
            break
        else:
            print("invalid")

main()
