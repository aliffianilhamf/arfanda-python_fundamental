# Memanipulasi Huruf
print("Memanipulasi String")

text = "Belajar Python Fundamental sAngat meNyenangkan"
print(f"Original    : {text}")
text_upper = text.upper() # String method tidak akan mereplace value lamanya.
print(f"Uppercase   : {text_upper}")
# print(f"Original    : {text}")
print(f"Lowercase   : {text.lower()}")
print(f"Capitalize  : {text.capitalize()}")
print(f"Title       : {text.title()}")
print(f"Swapcase    : {text.swapcase()}")

# membersihkan Spasi 
print()
print("Membersihkan Spasi")
text_kotor = "  Ini data Kotor  "
print(f"Original        : '{text_kotor}'")
print(f"Method Strip    : '{text_kotor.strip()}'")
print(f"Method Lstrip   : '{text_kotor.lstrip()}'")
print(f"Method Rstrip   : '{text_kotor.rstrip()}'")


# Splitting
print()
print("Memisahkan data")
text = "Belajar Python Fundamental sAngat meNyenangkan"
text_split = text.split(" ")
# text_split.append(1)
# text_split.append(200)
# text_split.append(True)
print(f"Originalnya     : {text}")
print(f"Hasil Split     : {text_split}")

kode_barang = "XII-098-AAA"
print(f"Originalnya     : {kode_barang}")
print(f"Hasil Split     : {kode_barang.split('-')}")

# Tipe konten
print()
print("Mengecek Tipe Konten pada String")
kursus = "Python3"
# isalnum -> apakah string terdiri dari alpa numerik / karakter + angka
print(f"Apakah terdiri dari karakter & angka ? : {kursus.isalnum()}")
# isalpa -> apakah string terdiri dari alpa / huruf
print(f"Apakah terdiri dari karakter ? : {kursus.isalpha()}")
# isdigit -> apakah string terdiri dari angka
print(f"Apakah terdiri dari angka ? : {kursus.isdigit()}")


# Replace
print()
print("Mengubah value pada string")
kode_barang = "XII-098-AAA"
print(f"Originalnya     : {kode_barang}")
print(f"Hasil Replace   : {kode_barang.replace('-', '*')}")

nama = "Hendi Prabowo"
print(f"Originalnya     : {nama}")
print(f"Hasil Replace   : {nama.replace('Hendi', 'Sardi')}")


# Join / menggabungkan string 
print()
print("Menggabungkan string")
list_string = ['Hari', 'Ini', 'Cerah']
hasil = "==".join(list_string)
print(f"Original    : {list_string}")
print(f"Hasil       : {hasil} ")


# Menggunakan banyak string method dalam 1 line
print()
print("Menggunakan banyak string method dalam 1 line")
text = "Belajar Python Fundamental sAngat meNyenangkan"
# 1. menjadikan lower case
# 2. replace Fundamental menjadi Advanced
# 3. Split berdasarkan spasi
text_result = text.lower().replace('Fundamental', 'Advanced').split(" ")
print(f"Original    : {text}")
print(f"Result      : {text_result}")

""" 
Latihan Soal 1. 
Bersihkan spasi diawal /akhir dan ubah menjadi huruf kecil semua 
- input : " JaKaRtA  "
- target : "jakarta"

Latihan Soal 2. 
Hapus "Rp" (termasuk spasi setelah Rp) dan hapus tanda titik "."
- input : "Rp 15.000.000"
- Target : "15000000"

Latihan Soal 3.
Pecah String berdasarkan karakter strip (-)
- input : "IPHONE13-RED-256GB 
- Target : ['IPHONE13', 'RED', '256GB']

Latihan Soal 4. 
gabungkan list menggunakan separator tanda hubung (-)
- input : ['belajar', 'python', 'untuk', 'pemula']
- target : "belajar-python-untuk-pemula"

Latihan Soal 5. 
Pisahkan string berdasarkan |, bersihkan spasi diawal dan akhir setiap item, ubah jadi huruf kecil, ubah spase di tengah menjadi udnerscore (_), hapus tanda kurung
- input : " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
- target : ['nama_customer_', '_total_belanja_idr_', '_alamat_pengiriman']
"""
# 1
text = " JaKaRtA  "
print(f"'{text.strip().lower()}'")

# 2
text = "Rp 15.000.000"
print(f"'{text.replace('Rp ', '').replace('.', '')}'")

# 3
text = "IPHONE13-RED-256GB"
print(f"'{text.split('-')}'")

# 4
text_list = ['belajar', 'python', 'untuk', 'pemula']
print(f"'{'-'.join(text_list)}'")

# 5
text = " Nama Customer | Total Belanja (IDR) | Alamat Pengiriman  "
print(f"'{text.strip().lower().replace(' ', '_').replace('(', '').replace(')', '').split('|')}'")