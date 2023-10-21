"""
    Kali ini kita akan membuat perhitungan cash flow
    dimana akan dibungkus dalam sebuah list dengan
    isi setiap elemen dalam list berisikan 
    pengeluaran (bilangan negatif) dan pemasukan
    (bilangan positif) pada sebuah perusahaan 
    kita akan melakukan perhitungan untuk 
    data pengeluaran dan pemasukan dari
    sebuah perusahaan ini
    
    Pemasukan:
    2.500.000, 5.000.000, 5.000.000, 10.000.000
    7.500.000, 10.000.000, 25.000.000
    
    Pengeluaran:
    -1.000.000, -2500000, -5000000
    -1500000, -2500000
"""

list_cash_flow = [
    2500000, 5000000, -1000000, -2500000, 
    5000000, 10000000, -5000000, 7500000, 
    10000000, -1500000, 25000000, -2500000
]

total_pemasukan = 0
total_pengeluaran = 0

for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana

# Code dibawah digunakan untuk mengubah hasil
# dari pengeluaran yang tadinya negatif menjadi
# nilai positif

total_pengeluaran *= -1

# Code dibawah diguanakan utnuk menampilkan hasil
print("Total Pemasukan Rp.", total_pemasukan)
print("Total pengeluaran Rp.", total_pengeluaran)