"""
    Pada kesempatan kali ini, saya akan menuliskan code
    penggunaan for loop dengan menggunakan 
    permisalan "Tagihan" dimulai dari
    angka positif dan negatif, untuk menghitung
    total tagihan dibawah ini:
    
    - Tagihan 1 = Rp 73.000
    - Tagihan 2 = Rp 67.000
    - Tagihan 3 = Rp 350.000
    - Tagihan 4 = Rp 250.000
    - Tagihan 5 = Rp - 125.000
    - Tagihan 6 = Rp - 100.000
    - Tagihan 7 = Rp - 23.000
"""

bayar_tagihan = [
    73000, -67000, 350000, 
    -250000, 125000, -100000, 23000
    ]

total_bayar = 0

for tagihan in bayar_tagihan:
    total_bayar += tagihan
    print(f"Hasil Iterasi dalam list {tagihan} =", total_bayar)

print("Tagihan yang perlu dibayarkan adalah Rp.", total_bayar)