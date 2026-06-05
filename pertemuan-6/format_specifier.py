nilai_pi = 3.14159265

# 1. Mengatur presisi
print("Mengatur Presisi")
print(f"Nilai PI asli : {nilai_pi}, setelah di format (2 angka dibelakang koma) : {nilai_pi:.2f}") 
print(f"Nilai PI asli : {nilai_pi}, setelah di format (2 angka dibelakang koma) : {nilai_pi:.5f}") 

# Mengatur Ribuan Rp. 1,250,000.00
print()
print("Menambahkan koma sebagai pemisah ribuan")
harga_barang = 1250000
print(f"Harga barang : Rp. {harga_barang:,.2f}")

# Persentase
print()
print("Menampilkan persen")
persentase_diskon = 0.5
print(f"Diskon : {persentase_diskon:.0%}")

# Mengatur perataan dan lebar kolom
print()
print("Mengatur perataan dan lebar kolom")
nama = "Aksal"
print(f"Nama siswa (rata kiri) : '{nama:<10}'") 
print(f"Nama siswa (rata kanan) : '{nama:>10}'") 
print(f"Nama siswa (rata tengah) : '{nama:^10}'") 
