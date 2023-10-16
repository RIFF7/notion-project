"""
    Pada kesempatan kali ini, saya akan menuliskan code
    penggunaan continue pada fungsi while looping
    dengan menggunakan permisalah "Tagihan" dimulai dari
    angka positif dan negatif, fungsi dari continue adalah
    jika nilai yang diinisialisasi bernilai negatif, maka
    perintah perhitungan akan diabaikan dan lanjut
    pada nilai berikutnya
    
    - Tagihan 1 = Rp 73.000
    - Tagihan 2 = Rp 67.000
    - Tagihan 3 = Rp 350.000
    - Tagihan 4 = Rp 250.000
    - Tagihan 5 = Rp - 125.000
    - Tagihan 6 = Rp - 100.000
    - Tagihan 7 = Rp - 23.000
"""

# Seperti biasa data yang sudah kita punya akan dijadikan
# sebagai list terlebih dahulu

bayar_tagihan = [
    73000, 67000, 350000, 
    250000, -125000, -100000, -23000
    ]

i = 0
banyak_tagihan = len(bayar_tagihan)
total_bayar = 0

while i < banyak_tagihan:
    # jika terdapat tagihan ke-i yang bernilai 
    # minus (di bawah nol),
    # abaikan tagihan ke-i dan lanjutkan ke 
    # tagihan berikutnya
    if bayar_tagihan[i] < 0:
        # nilai variabel i akan diinkrementasi 
        # (bertambah 1) menggunakan i += 1. 
        # Ini berfungsi untuk memproses 
        # elemen selanjutnya di iterasi berikutnya.
        i += 1
        
        # Ini adalah pernyataan continue yang 
        # akan memulai iterasi berikutnya dari 
        # loop saat ini. Artinya, jika elemen 
        # ke-i kurang dari 0, maka loop akan 
        # melanjutkan ke elemen berikutnya 
        # tanpa menjalankan kode di bawahnya.
        continue
    
    # Sehingga nilai yang bersifat positif saja
    # yang akan dilakukan penjumlahan
    # unutk menentukan value dari
    # total_bayar
    total_bayar += bayar_tagihan[i]
    
    # tambahkan nilai i dengan 1 untuk memproses tagihan selanjutnya, sekaligus menghentikan perulanagan.
    i += 1

# Tampilkan hasil akhir
print("Total tagihan yang harus dibayar Rp.", total_bayar)