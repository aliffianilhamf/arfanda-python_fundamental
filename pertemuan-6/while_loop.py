number = 1
while (number <= 5) : 
    print(f"Perulangan ke - {number}")
    number = number + 1 # increment (menaikkan value sebesar n)
    
    
#Iterasi 1 ==> number = 1, stop = 5, number_update = 2,
#Iterasi 2 ==> number = 2, stop = 5, number_update = 3,
#Iterasi 3 ==> number = 3, stop = 5, number_update = 4,
#Iterasi 4 ==> number = 4, stop = 5, number_update = 5,
#Iterasi 5 ==> number = 5, stop = 5, number_update = 6,
# Iterasi 6 ==> LOOP BERHENTI karena (6 <= 5 itu False)


print()

indeks = 0 #ini adalah nilai awal
while (indeks < 10):
    # cek aapakah bilangan termasuk bilangan genap
    if (indeks % 2 == 0):
        print(f"Perulangan ke-{indeks} - Bingo!! ini adalah bilangan Genap")
    else :
        print(f"Perulangan ke-{indeks} - Bilangan Ganjil")
        
    indeks = indeks + 1
    
    

""" 
- Buat program untuk menampilkan bilangan ganjil yang ada di rentan 1 - 20
- hanya print bilangan ganjilnya saja, "2 adalah bilangan ganjil"
- tidak usah print bilangan genapnya.
"1 adalah bilangan ganjil"
"3 adalah bilangan ganjil"
"5 adalah bilangan ganjil"
"""
print()
awal = 1
akhir = 20

while (awal <= akhir) :
    if (awal % 2 == 1) :
        print(f"{awal} adalah bilangan ganjil")
        
    # increment
    awal = awal + 1
    
# cetak nilai dari rentan 20 sampai 1
# perulangan ke-20
# perulangan ke-19
# perulangan ke-18
# perulangan ke-17
# ....
# perulangan ke-1
print()
awal = 20
akhir = 1

while (awal >= akhir):
    print(f"Perulangan ke-{awal}")
    
    # decrement
    awal = awal - 1


# bilangan = 1 
# while (bilangan <= 20):
#     if bilangan % 2 == 1 :
#         print(f"{bilangan} adalah bilangan ganjil")
        
#     bilangan = bilangan + 1  


print()


is_lanjut = True

while is_lanjut : 
    # print("Looping dari while")
    is_lanjut = int(input("Apakah mau lanjut (0 / 1)? : "))
    
    if is_lanjut == 1 : 
        print("Kamu memilih lanjut, perulangan akan berjalan lagi.")
        is_lanjut = True
    else : 
        print("Kamu memilih tidak lanjut, perulangan akan stop disini.")
        is_lanjut = False
        
        
"""

Latihan 2. 

- User akan menebak angka rahasia
- lakukan perulangan selama angka tebakan user itu tidak sama dengan angka rahasia
- tebakan user menggunakan fungsi input()
- jika tebakan user terlalu rendah, maka print "tebakan anda terlalu rendah"
- jika tebakan user terlalu tinggi, maka print "tebakan anda terlalu tinggi"
- kita hitung juga berapa kali user telah menebak
- Kalau tebakan benar, keluar dari loop dan print 
"Selamat tebakan anda benar, angka rahasianya adalah 7 dan sudah menebak sebanyak 4 kali"
"""

# langkah - langkah 
# - buat variable input untuk mendapatkan tebakan dari user
# - buat variabel pembantu untuk menghitung jumlah tebakan user yang kita isi nilai awalnya itu 1
# - buat kunci jawaban / angka rahasianya ke sebuah variabel misal angka_rahasia = 9
# - while (selama tebakan user itu tidak sama dengan angka rahasia) --> !=
#     - Copy step 1
#     - tambahkan jumlah tebakan user / increment
#     - cek apakah tebakan user terlalu rendah, kalau iya, print "tebakan anda terlalu rendah", 
#     - cek apakah tebakan user terlalu tinggi, kalau iya print "tebakan anda terlalu tinggi", 
# - kalau benar, kode akan keluar dari loop
# - di luar loop, print "Selamat tebakan anda benar, angka rahasianya adalah 7 dan sudah menebak sebanyak 4 kali"
print()
angka_rahasia = 7
jumlah_tebakan = 0
while True:
    tebakan = int(input("masukkan tebakan anda : "))
    jumlah_tebakan = jumlah_tebakan + 1
    
    if(tebakan < angka_rahasia):
        print(f"Tebakan terlalu rendah")
    elif(tebakan > angka_rahasia):
        print(f"Tebakan terlalu tinggi")
    else : 
        break
    
print(f"Tebakan anda benar, angka rahasianya adalah {angka_rahasia}, dan anda menebak sebanyak {jumlah_tebakan} kali")
