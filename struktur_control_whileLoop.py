"""
    Pada kesempatan kali ini, saya akan menuliskan
    beberapa contoh penggunaan struktur control dari while looping
    guna memperdalam pemahaman tentang penggunaan while looping
    
    Disini sebagai permisalan, saya memiliki list tagihan
    dan saya ingin melakukan perhitungannya untuk membayar
    tagihan yang ada menggunakan fungsi while loop
    
    - Tagihan 1 = Rp 73.000
    - Tagihan 2 = Rp 67.000
    - Tagihan 3 = Rp 350.000
    - Tagihan 4 = Rp 250.000
    - Tagihan 5 = Rp 125.000
    - Tagihan 6 = Rp 100.000
    - Tagihan 7 = Rp 23.000
"""

# Langkah pertama, kita akan memasukkan tagihan
# pada list untuk melakukan perhitungan, dimulai
# tanpa menggunakan while looping sampai dengan
# menggunakan while looping

bayar_tagihan = [
    73000, 67000, 350000, 
    250000, 125000, 100000, 23000
    ]

# Tanpa menggunakan while loop
total_tagihan = bayar_tagihan[0] + bayar_tagihan[1] + bayar_tagihan[2] + bayar_tagihan[3] + bayar_tagihan[4] + bayar_tagihan[5] + bayar_tagihan[6]

print("Tagihan yang harus dibayarkan adalah Rp.", total_tagihan)

# Menggunakan while loop
# Langkah pertama adalah membuat variable
# yang akan mengakses index dari tagihan yang ada
# pada list bayar_tagihan
i = 0
banyak_tagihan = len(bayar_tagihan) # Menentukan panjang dari list bayar_tagihan
total_bayar = 0 # Atur value total bayar dengan 0 untuk melakukan perhitungan
while i < banyak_tagihan: # Selama value i kurang dari banyak_tagihan
    # Lakukan perhitungan bayar_tagihan[i] dengan penjumlahan untuk menghasilkan total_bayar
    total_bayar += bayar_tagihan[i] 
    i += 1 # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya, sekaligus menghentikan perulanagan.

# Cetak hasil akhir dari total_bayar
print("Total tagihan yang harus dibayar Rp.", total_bayar)