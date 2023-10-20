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
print("""
      --------------------------------------------------
      | Penggunaan Perulangan dengan statement 'break' |
      --------------------------------------------------
      """)
print()

total_tagihan_break = 0
total_tagihan_continue = 0

for tagihan in bayar_tagihan:
    if tagihan < 0:
        print("Perhitungan dihentikan karena terdapat angka minus!")
        break
    total_tagihan_break += tagihan

print()
print("Total tagihan %d," % total_tagihan_break)
print()

print("==============================================================")
print()

print("""
      -----------------------------------------------------
      | Penggunaan Perulangan dengan statement 'continue' |
      -----------------------------------------------------
      """)
print()

for tagihan in bayar_tagihan:
    if tagihan< 0:
        print("Terdapat angka minus dalam perhitungan tagihan, untuk tagihan %d dilewati" % tagihan)
        continue
    total_tagihan_continue += tagihan

print()
print("Total tagihan setelah iterasi %d" % total_tagihan_continue)
print()

print("==============================================================")
print()

"""
    Dalam perulangan for juga kita dapat menggunakan
    nested loops, yaitu perulangan bersarang.
    
    Dalam nested loops kita dapat mengkombinasikan
    (menambahkan) struktur perulangan lain didalamnya
    sebagai contoh dengan data dibawah ini:
    
    Nama Buah: Apel, Duku, Jeruk
    Nama Daerah: Malang, Palembang, Medan
    
    Dibuat hingga menjadi data table 
    seperti dibawah ini:
    
    -----------------------------------
    |   Nama Buah   |   Nama Daerah   |
    -----------------------------------
    |    Data1      |     Data1       |
    -----------------------------------
    |    Data2      |     Data2       |
    -----------------------------------
    |    DataN      |     DataN       |
    -----------------------------------
"""

print("""
      --------------------------------
      | Penggunaan Neste Loops 'for' |
      --------------------------------
      """)
print()

list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']

h1 = "Nama Buah"
h2 = "Nama Daerah"

print("-----------------------------------------")
print(f"| {h1:^17} | {h2:^17} |")
print("-----------------------------------------")
print()

for row in list_buah:
    for item in list_daerah:
        print(f"| {row:^17} | {item:^17} |")
        print("-----------------------------------------")
    print()
print()