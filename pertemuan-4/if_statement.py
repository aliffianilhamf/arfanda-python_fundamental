umur = 16

#  if statement
# if (umur >= 17) :
#     print("Anda sudah bisa membuat KTP")

# if else statement
# if (umur >= 17) :
#     print("Anda sudah bisa membuat KTP")
# else : 
#     print("Anda belum bisa membuat KTP, Syarat membuat ktp minimal 17 Tahun!")

# if elif else statement
# if (umur >= 18) :
#     print("Anda sudah memasuki usia dewasa")
# elif (umur >= 12) :
#     print("Anda sudah memasuki usia remaja")
# elif (umur >= 3) :
#     print("Anda sudah memasuki usia anak-anak")
# else : 
#     print("Anda belum bisa membuat KTP, Syarat membuat ktp minimal 17 Tahun!")


# harga = float(input("Masukkan harga barang : "))

# if (harga > 1000):
#     diskon = 0.1 * harga
#     print(f"Anda mendapatkan diskon sebesar {diskon}")
# else :
#     print("Anda tidak mendapatkan diskon")
    
# print("Program selesai")

# Latihan
# 20% untuk jumlah di atas 10.000,
# 10% untuk jumlah lebih dari 5.000,
#  5% jika jumlahnya lebih dari 1.000.
#  Tidak ada diskon jika jumlahnya kurang dari 1.000.

# Nested if statement
# kartu_keluarga = True #tipe data boolean
# if (umur >= 18):
#     print("Anda diizinkan masuk")
    
#     if (kartu_keluarga == True) :
#         print("anda mendapat diskon 20%, karena anda memiliki kartu keluarga")
#     else : 
#         print("anda diizinkan masuk, tetapi tidak mendapatkan diskon")
        
# else :
#     print("Anda tidak diizinkan masuk, karena umur anda belum cukup") 

# sistem tilang
# buat input user untuk bertanya apakah punya sim dan stnk, jawaban user bisa berupa "ya" atau "tidak"
# sim  = input("Apakah anda memiliki SIM? (ya/tidak) : ")

# if(sim.lower() == "ya") :
#     stnk = input("Apakah anda memiliki STNK? : ")
    
#     if(stnk == "ya") :
#         print("Anda tidak kena tilang")
#     else : 
#         print("Anda kena tilang 50%")
# elif (sim == "tidak") : 
#     print("Anda kena tilang 100%")
# else :    
#     print("Anda tidak mema
# sukkan jawaban yang benar, silahkan masukkan jawaban dengan benar (ya/tidak)")

# jika punya sim dan punya stnk, maka tidak kena tilang
# jika tidak punya stnk, maka kena tilang 50%
# jika tidak punya sim dan stnk maka kena tilang 100%

print("")
# program untuk mengecek apakah suatu angka itu ganjil atau genap
nomor = -45

if (nomor % 2 == 1):
    # cek apakah bilangan ganjil positif atau negatif 
    if (nomor > 0):
        print(f"{nomor} merupakan bilangan ganjil positif")
    elif (nomor < 0):
        print(f"{nomor} merupakan bilangan ganjil negatif")
    else : 
        print(f"{nomor} yang anda masukkan adalah 0")
        
else : 
    if (nomor > 0):
        print(f"{nomor} merupakan bilangan genap positif")
    elif (nomor < 0):
        print(f"{nomor} merupakan bilangan genap negatif")
    else : 
        print(f"{nomor} yang anda masukkan adalah 0")
        
        
# Latihan Soal 
""" 
Membuat Kalkulator Sederhana
- Memiliki 3 input : 
    - input angka pertama -> angka_1 = int(input("Masukkan angka 1: "))
    - input operator (x, /, +, -) -> operator = 
    - input angka kedua -> angka_2 =
    
    if(operator == "/"):
    angka_1 = float(angka_1)
    angka_2 = float(angka_2)
    
- buat pengkondisian berdasarkan operatornya
    - contoh : jika operator == +, maka angka 1 + angka 2 = angka 3
    - begitu juga untuk perkalian, pembagian, dan pengurangan 
- namun ada yang unik dari pembagian, karena kita perlu mengecek terlebih dahulu
  angka ke 2 tidak boleh 0. jika angka ke 2 itu nol, maka print (Angka yang anda masukkan tidak boleh Nol)
  jika angka kedua tidak nol, maka lakukan operasi pembagian
- contoh ilustrasi program : 

masukkan angka pertama : 13
masukkan operator (x, /, -, +) : + 
masukkan angka kedua : 12

13 + 12 = 25


masukkan angka pertama : 2
masukkan operator (x, /, -, +) : x 
masukkan angka kedua : 3

2 x 3 = 6
"""

angka_1 = int(input("Masukkan angka pertama : "))
operator = input("Masukkan operator (/, x, +, -) : ")
angka_2 = int(input("Masukkan angka kedua : "))



if (operator == "+"):
    hasil_penjumlahan = angka_1 + angka_2
    print(f"{angka_1} {operator} {angka_2} = {hasil_penjumlahan}")
elif (operator == '-'):
    print(f"{angka_1} {operator} {angka_2} = {angka_1 - angka_2}")
elif (operator == 'x') : 
    print(f"{angka_1} {operator} {angka_2} = {angka_1 * angka_2}")
elif (operator == '/'): 
    if (angka_2 != 0):
        print(f"{angka_1} {operator} {angka_2} = {angka_1 / angka_2}")
    else : 
        print("Angka kedua tidak boleh nol!")
else : 
    print("Operator yang bisa dimasukkan hanya (/, x, +, -)!")
    

""" 
Program Konversi Suhu

- buat variabel untuk menampung inpitan suhu celcius 
- print pilihan konversinya
    1. celcius ke fahrenheit
    2. celcius ke reamur
    3. celcius ke kelvin
- buat variabel untuk menampung inputan pilihan user, apakah 1, 2, atau 3

- pengcekan pilihan dari user : 
    jika user memilih 1 : 
        - rumus konversi celcius ke fahrenheit = (celcius x 9/5) + 32
        - 90 celcius = 40 fahrenheit
    jika user memilih 2 : 
        - rumus konversi celcius ke reamur = (4/5) * celcius
        - 90 celcius = 40 reamur
    jika user memilih 3 : 
        - rumus konversi celcius ke reamur = celcius + 273.15
        - 90 celcius = 310 kelvin
    jika user memilih selain 1,2,3
        - tampilkan (Maaf pilihan yang tersedia hanya 1, 2, dan 3. )
"""
    
    