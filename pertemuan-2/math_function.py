a = 10
b = 3.64
c = -6


# round (Pembulatan otomatis)
result = round(b) # output : 3
print(f"Hasil round dari {b} adalah {result}")

# abs (selalu positif)
result = abs(c) # output : 6
print(f"Hasil absolute dari {c} adalah {result}")

# pow / pangkat
result = pow(a, 2)
print(f"Hasil dari {a} pangkat 2 adalah {result}")

# max
result = max(1, 54, 6, 77, 23, 43)
print(f"Nilai maksimalnya adalah {result}")

# min
result = min(1, 54, 6, 77, 23, 43)
print(f"Nilai minimalnya adalah {result}")

print()

import math


print(math.pi)
print(math.sqrt(9))

print()

# siapakan variabel untuk menampung jari jari (namanya bebas)
jari_jari = input("Masukkan jari jari lingkaran : ")
jari_jari = float(jari_jari)
# Sipakan variabel untuk menampung luas lingkaran (namanya bebas)
# kemudain variabel luas, di isi dengan rumus = phi * pow(jari jari, 2)
luas = math.pi * pow(jari_jari, 2)

# Sipakan variabel untuk menampung keliling lingkaran (namanya bebas)
# kemudain variabel keliling, di isi dengan rumus = 2 *phi * jari jari
keliling = 2 * math.pi * jari_jari
# print
# Lingkaran dengan jari jari : {berapa}, memiliki luas : {berapa}, dan keliling : {berapa}
print(f"Lingkaran dengan jari jari : {jari_jari}, memiliki luas : {luas}, dan keliling : {keliling}")



