# Membuat Tampilan list
# Name | Date | List | Priority

import os, time, sys

TodoList = []

def add():
    time.sleep(1)
    os.system("cls") # -> jika kamu menggunakan MacOS atau Linux, maka silakan untuk ubah menjadi "clear"
    name = input("Nama: ").capitalize()
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
    if option == "1":
        for row in TodoList:
            for item in row:
                print(item, end=" | ")
            print()
        print()
    else:
        priority = input("Silakan Masukkan Prioritas: ")
        print()
        for row in TodoList:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print()
        print()
    time.sleep(3)

def edit():
    time.sleep(1)
    os.system("cls")
    character = input("Masukkan nama list yang dicari: ")
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
    
    name = input("Nama: ").capitalize()
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