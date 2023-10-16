"""
    Pada kesempatan kali ini, saya akan menuliskan code
    penggunaan break pada fungsi while looping
    dengan menggunakan permisalah "Tagihan" dimulai dari
    angka positif dan negatif, fungsi dari break adalah
    jika nilai yang diinisialisasi bernilai negatif, maka
    perintah perhitungan akan dihentikan
    
    - Tagihan 1 = Rp 73.000
    - Tagihan 2 = Rp - 67.000
    - Tagihan 3 = Rp 350.000
    - Tagihan 4 = Rp 250.000
    - Tagihan 5 = Rp - 125.000
    - Tagihan 6 = Rp 100.000
    - Tagihan 7 = Rp - 23.000
"""

# Seperti biasa data yang sudah kita punya akan dijadikan
# sebagai list terlebih dahulu

bayar_tagihan = [
    73000, 67000, 350000, 
    250000, -125000, 100000, -23000
    ]

i = 0 # Setting nilai awal i adalah 0
banyak_tagihan = len(bayar_tagihan) # Tetapkan panjang list dengan fungsi len()
total_bayar = 0 # Setting nilai awal tagihan adalah 0

# Ketika value i kurang dari panjang bayar_tagihan
# Lakukan perintah selanjutnya
while i < banyak_tagihan: 
    # Jika terdapat nilai bayar_tagihan ke-i bernilai minus (dibawah nol),
    # perulangan akan dihentikan
    if bayar_tagihan[i] < 0:
        # Setting nilai total_bayar dengan -1, untuk menampilkan 
        # perhitungan terdapat nilai minus sehingga pada perintah
        # print() terakhir tidak menampilkan total jumlah bayar
        # melainkan menampilkan nilai -1
        total_bayar = -1
        print("Terdapat Nilai Minus dalam list bayar_tagihan, perhitungan dihentikan!!!")
        break
    # Jika nilai tidak ada yang bersifat minus
    # maka perintah penjumlahan sebanyak 
    # bayar_tagihan ke-i akan dijalankan
    total_bayar += bayar_tagihan[i]
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya, sekaligus menghentikan perulanagan.
# Jika tidak ada nilai minus maka total_bayar hasil
# dari penjumlahan akan ditampilkan
# Sebaliknya jika terdapat nilai minus maka nilai
# total_tagihan akan menampilkan -1, sesuai dengan
# setting pada perintah if sebelumnya    
print("Total tagihan yang harus dibayar Rp.", total_bayar)