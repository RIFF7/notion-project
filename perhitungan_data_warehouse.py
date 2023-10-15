"""
    Membuat perhitungan pembayaran sederhana untuk jasa 
    pembuatan data warehouse, dengan data dibawah ini:
    
    --------------------------------------------------------------------------------------------------------
    |       Nama Jasa       |       Harga per-Hari       |       Total Hari      |        Sub Total        |
    --------------------------------------------------------------------------------------------------------
    |   Data Warehousing    |         1000000           |           15           |         15000000        |
    |   Data Cleanning      |         1500000           |           10           |         15000000        |
    |   Data Integration    |         2000000           |           15           |         30000000        |
    |   Data Transformation |         2500000           |           10           |         25000000        |
    -------------------------------------------------------------------------------------------------------|
    |   Total               |                                                    |         85000000        |
    -------------------------------------------------------------------------------------------------------|
    
    Dari data yang telah kita miliki diatas saat ini tujuannya adalah,
    menghitung tagihan pembayaran dimana isi dari table diatas
    akan kita masukkan pada dictionary yang nantinya akan dilakukan
    sebuah perhitungan untuk mengetahui besaran tagihan yang harus dibayarkan
"""
# Pertama kita akan membuat nama
# penerima dari data tagihan diatas

tagihan_tertuju = "Mr. Sebas"

# Setelah membuat nama tujuan tagihan akan dikirim
# Selanjutnya adalah memasukkan data table pada dictionary

warehousing = {
    "nama_jasa": "Data Warehousing",
    "harga_harian": 1000000,
    "total_hari": 15,
    "sub_total": 15000000
}

cleanning = {
    "nama_jasa": "Data Cleanning",
    "harga_harian": 1500000,
    "total_hari": 10,
    "sub_total": 15000000
}

integration = {
    "nama_jasa": "Data Integration",
    "harga_harian": 2000000,
    "total_hari": 15,
    "sub_total": 30000000
}

transformation = {
    "nama_jasa": "Data Transformation",
    "harga_harian": 2500000,
    "total_hari": 10,
    "sub_total": 25000000
}

# Setelah mengubah data dalam table menjadi beberapa
# dictionary, selanjutnya adalah proses perhitungan
# untuk mengetahui harga per-hari dari total hari untuk 
# setiap jasa yang dilakukan

jasa_warehousing = warehousing["harga_harian"] * warehousing["total_hari"]
jasa_cleanning = cleanning["harga_harian"] * cleanning["total_hari"]
jasa_integration = integration["harga_harian"] * integration["total_hari"]
jasa_transformation = transformation["harga_harian"] * transformation["total_hari"]

total_harga = (jasa_warehousing + jasa_cleanning + jasa_integration + jasa_transformation)

# Pengembangan tahap ke-1
# -----------------------
# print("Tagihan yang perlu", tagihan_tertuju, "bayarkan adalah sebesar", total_harga)

# ====================================================================================

# Pengembangan tahap ke-2 menggunakan if - elif dan else
# --------------------------------------------------------

# Jika kita membuat seolah ini adalah sebuah surel/email
# yang mana memiliki jam disetiap pengirimannya
# maka kita perlu melakukan set jam terlebih dahulu

print("""
      =======================================================
      | Batas Pengiriman E-mail adalah pukul 21 (21:00) WIB |
      =======================================================
      """)

jam = int(input("Masukkan Jam Saat ini tanpa diikuti oleh menit: ")) # Example -> input: 17
print()
print("Tagihan Kepada:")
print(tagihan_tertuju)

if jam >= 19 and jam < 21:
    print("Selamat Malam, anda memiliki tagihan pembangunan yang perlu dibayar sebesar:")
elif jam >= 15 and jam <= 18:
    print("Selamat Sore, anda memiliki tagihan pembangunan yang perlu dibayar sebesar:")
elif jam >= 11 and jam <= 14:
    print("Selamat Siang, anda memiliki tagihan pembangunan yang perlu dibayar sebesar:")
else:
    print("Selamat Pagi, anda memiliki tagihan pembangunan yang perlu dibayar sebesar:")

print(total_harga)
print()