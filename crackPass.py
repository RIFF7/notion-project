from random import *

import os

u_pwd = input("Enter a Password: ")
pwd = ['a', 'b', 'c', 'd', 'e', 
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'S', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5',
        '6', '7', '8', '9']

pw = ""
while(pw != u_pwd):
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pass = pwd[randint(0,5)]
        pw = str(guess_pass) + str(pw)
        print(pw)
        print("Cracking Password...Please wait 😉")
        os.system("cls")
print("Your Password Is:", pw)

# from random import shuffle
# import os

# passWord = input("Masukkan Kata Sandi: ")
# lst_pwd = ["a", "b", "c", "d", "e", 
#            "f", "g", "h", "i", "j",
#            "k", "l", "m", "n", "o",
#            "p", "q", "r", "s", "t",
#            "u", "v", "w", "x", "y", "z",
#            "A", "B", "C", "D", "E", 
#            "F", "G", "H", "I", "J",
#            "K", "L", "M", "N", "O",
#            "P", "Q", "S", "S", "T",
#            "U", "V", "W", "X", "Y", "Z",
#            "0", "1", "2", "3", "4", "5",
#            "6", "7", "8", "9"]

# pwd = ""
# while pwd != passWord:
#     guess_list = lst_pwd.copy()
#     shuffle(guess_list)
#     pwd = "".join(guess_list)
#     print(pwd)
#     print("Menggabungkan Kata Sandi...Tunggu sebentar 😉")
#     os.system("cls")
#     if pwd == passWord:
#         break
# print("Kata Sandi Anda:", pwd)
