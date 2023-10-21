"""
    Case:
    
    Disuatu pagi aku menyambut ponselku yang ada
    diatas meja ternyata terdapat pesan masuk
    dengan pegirim adalah pamanku yang ada di jakarta
    beliau menjelaskan bahwa tempo hari beliau harus
    mengeluarkan dana sebesar Rp. 1.500.000 per mobil
    dalam sehari. Tetapi beliau dengan total pengeluaran
    per bulan, karena adanay aturan ganjil - genap yang
    membuat pengoperasian mobil yang berbeda.
    
    Disini aku berandai-andai membuat beberapa 
    variabel seperti jumlah_hari dengan isi hari dalam
    jangka waktu 1 bulan lalu variabel list_plat_nomor
    berisi seluruh plat nomor mobil milik paman.
    
    Jika seperti ini paman hanya perlu mengganti variabel
    jumlah_hari atau melakukan modifikasi variabel
    list_plat_nomor untuk melacaak total pengeluaran paman
    selama 1 bulan 😁
"""

# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]

# Pengecekan kendaraan dengan nomor ganjil atau genap
# Lakukan deklarasi kendaraan_genap dan kendaraan_ganjil
kendaraan_genap = 0
kendaraan_ganjil = 0

for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1
    else:
        kendaraan_ganjil += 1

# Total pengeluaran untuk kendaraan dengan nomor plat ganjil
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0

while i <= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)
    i += 1

print("Total pengeluaran Rp.", total_pengeluaran)