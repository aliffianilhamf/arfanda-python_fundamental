# Print -> Menampilkan hasil ke layar
print("Hello, Saya sedang belajar Python")

# variabel adalah tempat untuk menyimpan sebuah data
nama_depan = "Aliffian Ilham"   # Variabel ini tipenya adalah string (Ditandai dengan diapit oleh petik dua)
umur = 22                       # variabel ini tipenya integer (tidak mengandung koma, pecahan, dan merupakan bilangan bulat)
tinggi_badan = 165.7            # variabel ini tipenya float ( biasa digunakan untuk bilangan desimal, (yang ada komanya))
apakah_merokok = False          # Variabel ini tipenya bool / boolean (yang isinya hanya True dan False)

print(nama_depan )

# f-string (Formatted string)
# print("Nama depan saya adalah : ", nama_depan , " umur saya : ", umur)
print(f"Nama depan saya adalah : {nama_depan}, umur saya : {umur}, Tinggi badan saya {tinggi_badan}, apakah saya merokok ? {apakah_merokok}")

print()
# input -> untuk menerima inputan dari user
barang = input("Masukkan nama barang : ")
# barang = "Gula"
# print(f"Barang yang anda inputkan adalah : {barang}")
harga = input("Masukkan harga barang : ")
harga_int = int(harga)
# print(f"Harga yang anda inputkan adalah : {type(harga_int)}")

jumlah = input("Masukkan jumlah barang : ")
jumlah_int = int(jumlah)
# print(f"jumlah yang anda inputkan adalah : {jumlah_int}")

total_harga = harga_int * jumlah_int
print(f"Total harga dari {jumlah_int} {barang} adalah : {total_harga}")

