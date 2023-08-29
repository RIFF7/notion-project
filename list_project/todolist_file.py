# Membuat To Do List dengan penyimpanan file ".txt"
# Serta membuat tampilan view tertata rapih

import os, time, sys

TodoList = []

try:
    file = open("TodoList.txt", "r")
    TodoList = eval(file.read())
    file.close()
except:
    pass

def add():
    time.sleep(1)
    os.system("cls") # -> jika kamu menggunakan MacOS atau Linux, maka silakan untuk ubah menjadi "clear"
    name = input("Nama: ").title()
    date = input("Tenggat Waktu: ")
    cases = input("Daftar Kerjaan: ")
    priority = input("Prioritas: ").capitalize()
    row = [name, date, cases, priority]
    TodoList.append(row)
    print()
    print("List Added!")
    
def view():
    time.sleep(1)
    os.system("cls")
    option = input("1. Tampilkan Semua Prioritas\n2. Pilih Berdasarkan Prioritas\n> ")
    h1 = "Nama"
    h2 = "Tenggat Waktu"
    h3 = "Daftar Kerjaan"
    h4 = "Prioritas"
    if option == "1":
        print(f"{h1:^30}{h2:^30}{h3:^30}{h4:^30}")
        for row in TodoList:
            print(f"{row[0]:^30}{row[1]:^30}{row[2]:^30}{row[3]:^30}")
        print()
    else:
        priority = input("Silakan Masukkan Prioritas: ").title()
        print()
        for row in TodoList:
            if priority in row:
                print(f"{h1:^30}{h2:^30}{h3:^30}{h4:^30}")
                print(f"{row[0]:^30}{row[1]:^30}{row[2]:^30}{row[3]:^30}")
                print()
        print()
    time.sleep(3)

def edit():
    time.sleep(1)
    os.system("cls")
    character = input("Masukkan nama list yang dicari: ").title()
    found = False
    for row in TodoList:
        if character in row:
            found = True
    
    if not found:
        print("Nama tidak ada pada list, silakan menginat-ingat kembali!")
        time.sleep(2)
        return
    
    for row in TodoList:
        if character in row:
            TodoList.remove(row)
    
    name = input("Nama: ").title()
    date = input("Tenggat Waktu: ")
    cases = input("Daftar Kerjaan: ")
    priority = input("Prioritas: ").capitalize()
    row = [name, date, cases, priority]
    TodoList.append(row)
    print("Done Edited!")
    
def remove():
    time.sleep(1)
    os.system("cls")
    character = input("Name List yang akan kamu hapus: ")
    found = False
    for row in TodoList:
        if character in row:
            found = True
    
    if not found:
        print("Nama tidak ada pada list, silakan menginat-ingat kembali!")
        time.sleep(2)
        return
    
    for row in TodoList:
        if character in row:
            TodoList.remove(row)
            print("Done Remove!")

while True:
    print()
    print("Simple To Do List With Console!")
    print()
    menu = input("1. Add\n2. View\n3. Edit\n4. Remove\n5. Exit\n> ")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    elif menu == "4":
        remove()
    else:
        sys.exit()
    time.sleep(1)
    os.system("cls")
    
    file = open("TodoList.txt", "w")
    file.write(str(TodoList))
    file.close()