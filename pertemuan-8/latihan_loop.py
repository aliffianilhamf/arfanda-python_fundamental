""" 
Latihan Soal 1. 
- kalimat = "Dokumen ini berisi latihan-latihan sederhana menggunakan Python"
- print hanya huruf konsonan saja (selain aiueo) dan juga print berapa jumlah hurufnya

Latihan Soal 2. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- cari nilai maksimum dari list diatas, tanpa menggunakan fungsi max() dari python
if number > max:
    max = number

Latihan Soal 3. 
- numbers = [30, 23, 33, 45, 54, 6, 55]
- Hitung total nilai dari yang ada di list

"""

# Segitiga siku siku kiri 
for i in range(1, 6):
    print("*" * i)

print()
# Segitiga siku siku kebalil 
for i in range(5, 0, -1):
    print("*" * i)
    
    
print()
# Segitiga siku siku kanan 
spasi = 0
jumlah_bintang = 5
# for i in range(1,6):
for i in range(1, jumlah_bintang + 1):
    spasi = jumlah_bintang - i
    # print(f"{spasi}{i}")
    print(f"{' ' * spasi}{'*' * i}")
    
print()
# Piramida
spasi = 0
bintang = 0
jumlah_baris = 5
# for i in range(1,6):
for i in range(1, jumlah_baris + 1):
    spasi = jumlah_baris - i
    bintang = (2 * i) - 1
    
    print(f"{' ' * spasi}{'*' * bintang}")