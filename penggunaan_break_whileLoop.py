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
    73000, -67000, 350000, 
    250000, -125000, 100000, -23000
    ]

i = 0
banyak_tagihan = len(bayar_tagihan)
total_bayar = 0

while i < banyak_tagihan:
    # Jika terdapat nilai bayar_tagihan ke-i bernilai minus (dibawah nol),
    # perulangan akan dihentikan
    if bayar_tagihan[i] < 0:
        total_bayar = -1
        print("Terdapat Nilai Minus dalam list bayar_tagihan, perhitungan dihentikan!!!")
        break
    
    total_bayar += bayar_tagihan[i]
    i += 1
    
print("Total tagihan yang harus dibayar Rp.", total_bayar)