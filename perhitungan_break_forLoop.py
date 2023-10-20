"""
    Sama seperti penggunaan perulangan while 
    pada perulangan for kita juga
    dapat menggunakan statement break dan juga 
    continue, kali ini saya akan menggunakan data
    dibawah ini untuk menggunakan fungsi break dan
    continue dengan data dibawah ini:
    
    - Tagihan 1 = Rp 73.000
    - Tagihan 2 = Rp 67.000
    - Tagihan 3 = Rp - 350.000
    - Tagihan 4 = Rp 250.000
    - Tagihan 5 = Rp - 125.000
    - Tagihan 6 = Rp 100.000
    - Tagihan 7 = Rp - 23.000
"""

bayar_tagihan = [
    73000, 67000, -350000, 
    250000, -125000, 100000, -23000
    ]

print()
print("Penggunaan Perulangan dengan statement 'break'")
total_tagihan_break = 0

for tagihan in bayar_tagihan:
    if tagihan < 0:
        print("Perhitungan dihentikan karena terdapat angka minus!")
        break
    total_tagihan_break += tagihan

print()
print("Total tagihan %d," % total_tagihan_break)
print()