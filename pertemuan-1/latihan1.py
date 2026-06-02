# 1. Buat variable untuk menampung panjang persegi panjang (namanya bebas tapi direkomendasikan bernama "panjang") & variable tersebut bisa menerima inputan user
panjang = input("Masukkan panjang persegi panjang : ")
# 2. Buat variable untuk menampung lebar persegi panjang (namanya bebas tapi direkomendasikan bernama "lebar") & variable tersebut bisa menerima inputan user
lebar = input("Masukkan lebar persegi panjang : ")
    # konversi ke int, sebelum mengalikan
panjang = int(panjang)
lebar = int(lebar)
# 3. tampung hasil perkalian ke dalam variable bernama "luas" yang di dapatkan dari panjang x lebar
luas = panjang * lebar
# 4. Print hasilnya
print(luas)