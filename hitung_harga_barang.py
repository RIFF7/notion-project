"""
    Membuat perhitungan sederhana untuk pembelian bawang pada list dibawah ini:
    
    -------------------------------------------------------------
    |   Nama Barang     |       Harga       |       Diskon      |
    -------------------------------------------------------------
    |   Sepatu Nike     |     2300000       |       175000      |
    |   Baju Uniklo     |     127000        |       23500       |
    |   Celanan Jeans   |     175000        |       15000       |
    |   Jacket Bomber   |     235000        |         0         |
    |   Kaca Mata Hitam |     112000        |       17000       |
    -------------------------------------------------------------
    
    Dari data belanja yang kita punya diatas, kita akan membuat program
    sederhana dimana untuk menghitung total belanja yang sudah dihitung juga
    dengan total pajak sebanyak 10%, sehingga kita mendapat total bersih
    dari banyaknya uang yang kita belanjakan untuk 5 item diatas 😂
"""

# Hal pertama yang dilakukan adalah membuat dictionary yang akan
# menampung data belanjaan kita

sepatu = {
    "nama": "Sepatu Nike",
    "harga": 2300000,
    "diskon": 175000
    }

baju = {
    "nama": "Baju Uniklo",
    "harga": 127000,
    "diskon": 23500
}

celana = {
    "nama": "Celanan Jeans",
    "harga": 175000,
    "diskon": 15000
}

jaket = {
    "nama": "Jacket Bomber",
    "harga": 235000,
    "diskon": 0
}

aksesoris = {
    "nama": "Kaca Mata Hitam",
    "harga": 112000,
    "diskon": 17000
}

# Setelah membuat dictionary untuk menjabarkan barang, 
# harga dan diskon dari 5 item yang ada
# selanjutnya kita akan melakukan perhitungan
# untuk harga masing - masing item setelah dikurangi
# diskon yang sudah dibuat

harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
harga_jaket = jaket["harga"] - jaket["diskon"]
harga_aksesoris = aksesoris["harga"] - aksesoris["diskon"]

# Code dibawah adalah code penjabawannya
# namu kita juga bisa memperpendek code dibawah 
# dengan code pada contoh selanjutnya

# -- Sebelum Penyederhanaan Code
# Setelah mendapatkan harga masing - masing item setelah
# dikurangi diskon, selanjutnya kita akan menjumlahkan total hargannya

# total_harga = harga_sepatu + harga_baju + harga_celana + harga_jaket + harga_aksesoris

# # Setelah mendapatkan total harga, selanjutnya kita akan melakukan perhitungan
# # dari total pajak sebanyak 10% dari total harga

# total_pajak = total_harga * 0.1

# # Setelah mendapatkan total pajak
# # selanjutnya kita akan menampilkan harga total keseluruhan
# # yang perlu kita bayarkan 

# print("Harga yang perlu kita bayarkan adalah", total_harga + total_pajak)

# -- Setelah penyederhanaan Code

"""
    Penjelasan untuk 1.1
    
    Saat kita mengalikan suatu nilai dengan 1.1,
    kita sebenarnya menambahkan 10% dari nilai 
    tersebut dan menghasilkan total 110% dari 
    nilai awal, atau dengan kata lain, 
    meningkatkannya sebesar 10%. 
    Jadi, 1.1 adalah faktor pengali yang menghasilkan 
    peningkatan sebesar 10%.
    
    Faktor 1.1 digunakan untuk meningkatkan 
    total harga sebesar 10% untuk pajak
"""
total_harga = (harga_sepatu + harga_baju + harga_celana + harga_jaket + harga_aksesoris) * 1.1

print("Harga yang harus dibayarkan adalah", round(total_harga))