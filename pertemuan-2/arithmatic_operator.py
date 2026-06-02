# Arithmatic operator di python, itu sama seperti operator matematika biasa yang kita gunakan
#  ada penjumlahan (+), pengurangan (-), perkalian (*), permbagian (/), modulo / sisa hasil bagi (%)

angka_1 = 200
angka_2 = 100


# Penjumlahan
hasil_jumlah = angka_1 + angka_2
print(f"penjumlahan antara angka_1 + angka_2 adalah : angka_1 + angka_2")
print(f"Penjumlahan antara {angka_1} + {angka_2} adalah : {hasil_jumlah}")

# Pengurangan
hasil_kurang = angka_1 - angka_2
print(f"Pengurangan antara {angka_1} - {angka_2} adalah : {hasil_kurang}")

# perkalian
hasil_kali = 200 * 5
print(f"Perkalian antara 200 * 5 adalah : {hasil_kali}")

# pembagian
hasil_bagi = 203 / 5
print(f"Pembagian antara 203 / 5 adalah : {hasil_bagi}")

# modulo (sisa hasil bagi)
hasil_modulo = 203 % 5
print(f"Modulo dari 203 % 5 adalah : {hasil_modulo}")


# compound asignment (Operator penugasan langsung)
angka_3 = 500
angka_4 = 100

# biasa
# angka_4 = angka_3 + angka_4

# compound operator
angka_4 += angka_3
print(f"[penjumlahan] Hasilnya adalah {angka_4}")

# compound operator untuk pengurangan
# biasa
# angka_4 = angka_4 - angka_3

angka_4 -= angka_3
print(f"[pengurangan] Hasilnya adalah {angka_4}")

# compound operator untuk perkalian
target output : 500
# biasa 

# compound operator untuk pembagian
target output : 10

# compound operator untuk modulo
target output : 1