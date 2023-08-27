import os, time, sys

def penjumlahan():
    number1 = int(input("Masukkan Angka Pertama: "))
    number2 = int(input("Masukkan Angka Kedua: "))
    result = number1 + number2
    print()
    print(f"Hasil penjumlahan dari {number1} dan {number2} adalah", result)
    time.sleep(3)

def pengurangan():
    number1 = int(input("Masukkan Angka Pertama: "))
    number2 = int(input("Masukkan Angka Kedua: "))
    result = number1 - number2
    print()
    print(f"Hasil pengurangan dari {number1} dan {number2} adalah", result)
    time.sleep(3)

def perkalian():
    number1 = int(input("Masukkan Angka Pertama: "))
    number2 = int(input("Masukkan Angka Kedua: "))
    result = number1 * number2
    print()
    print(f"Hasil dari perkalian {number1} dan {number2} adalah", result)
    time.sleep(3)

def pembagian():
    number1 = int(input("Masukkan Angka Pertama: "))
    number2 = int(input("Masukkan Angka Kedua: "))
    result = number1 / number2
    print()
    print(f"Hasil dari perkalian {number1} dan {number2} adalah", result)
    time.sleep(3)

while True:
    time.sleep(1)
    os.system("cls")

    print("Simple Calculator\n")

    print("""
    +-----------------------------------------------------------------------------+
    | Rule untuk menggunakan sistem perhitungan dibawah adalah, kamu akan diminta |
    | untuk menginput pilihan perhitungan yang tersedia atara 'Penjumlahan,       |
    | Pengurangan, Perkalian, Pembagian'. Tolong pastikan kamu memasukkan angka   |
    | pada program guna menghindari ERROR! yang terjadi.                          |
    +-----------------------------------------------------------------------------+
    """)
    
    calculate = input("1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (*)\n4. Pembagian (/)\n5. Exit\n> ")
    if calculate == "1":
        penjumlahan()
    elif calculate == "2":
        pengurangan()
    elif calculate == "3":
        perkalian()
    elif calculate == "4":
        pembagian()
    else:
        sys.exit()