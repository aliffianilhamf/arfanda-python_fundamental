kondisi_1 = True 
kondisi_2 = True 

result = kondisi_1 and kondisi_2 
print(f"Konndisi 1 {kondisi_2} and kondisi 2 {kondisi_2} maka hasilnya : {result}")

bilangan = -11 

if ((bilangan % 2 == 0) and (bilangan > 0)):
    print(f"Bilangan {bilangan} Merupakan bilangan genap positif")
elif ((bilangan % 2 == 1) and (bilangan > 0)): # pengecekan bilangan ganjil dan positif
    print(f"Bilangan {bilangan} Merupakan bilangan ganjil positif")
elif ((bilangan % 2 == 0) and (bilangan < 0)) : # pengecekan bilangan genap dan negatif
    print(f"Bilangan {bilangan} Merupakan bilangan genap negaitf")
elif ((bilangan % 2 == 1) and (bilangan < 0)) : # pengecekan bilangan ganjil dan negatif
    print(f"Bilangan {bilangan} Merupakan bilangan ganjil negatif")
else : 
    print("Bilangan anda adalah Nol")
    
print("Akhir dari Program")


print()
print("LOGIKA OR")
# Mengecek siswa apakah mendapatkan penghargaan atau tidak
# Syaratnya
nilai_siswa = 80
kehadiran_siswa = 100
 
apakah_nilai_tinggi = nilai_siswa >= 90 # True
apakah_kehadiran_sempurna = kehadiran_siswa == 100 # False

# Siswa akan mendapatkan penghargaan, jika nilainya tinggi atau kehadirannya sempurna 
print("Pengujian operator OR (salah satu benar, sudah menghsilkan True)")
if ((apakah_nilai_tinggi) or (apakah_kehadiran_sempurna)) : 
    print("Siswa Mendapat Penghargaan (Nilanya sangat tinggi ATAU kehadirannya sempurna)")
else : 
    print("Siswa tidak mendapatkan penghargaan")
    

print()
print("LOGIKA NOT")

is_bermasalah = True 

if not is_bermasalah : 
    print("Selamat kamu bebas dari hukuman")
else : 
    print("Kamu bermasalah, kena hukuman")
# if  is_bermasalah : 
#     print("Kamu bermasalah, kena hukuman")
# else : 
#     print("Selamat kamu bebas dari hukuman")
    