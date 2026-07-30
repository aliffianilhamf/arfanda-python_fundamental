# Dictonary adalah tipe data yang menyimpan data dalam bentuk pasangan key dan value. Key harus unik, sedangkan value bisa sama. Dictionary menggunakan tanda kurung kurawal {}.


# membuat dictionary
my_dict = {"nama": "Aldo", "umur": 20, "status": True} # dictionary yang isinya campuran
my_dict2 = {"buah": "apel", "warna": "merah", "harga": 5000} # dictionary yang key-nya string
my_dict3 = {1: "satu", 2: "dua", 3: "tiga"} # dictionary yang key-nya integer

print(my_dict)
print(my_dict2)
print(my_dict3)

# mengakses dictionary
print("\nMengakses dictionary")
# mengakses value dengan key
print(my_dict["nama"]) # output : Aldo
print(my_dict2["warna"]) # output : merah
print(my_dict3[2]) # output : dua
print(my_dict.get("umur")) # output : 20

# mengubah dictionary
print("\nMengubah dictionary")
my_dict["umur"] = 21 # mengubah value dari key "umur"
print(my_dict) # output : {'nama': 'Aldo', 'umur': 21, 'status': True}

my_dict2.update({"harga": 6000}) # mengubah value dari key "harga"
print(my_dict2) # output : {'buah': 'apel', 'warna': 'merah', 'harga': 6000}

# menambahkan item pada dictionary
print("\nMenambahkan item pada dictionary")
my_dict["alamat"] = "Jakarta" # menambahkan key "alamat" dengan value "Jakarta"
print(my_dict) # output : {'nama': 'Aldo', 'umur': 21, 'status': True, 'alamat': 'Jakarta'}

my_dict2.update({"stok": 10}) # menambahkan key "stok" dengan value 10
print(my_dict2) # output : {'buah': 'apel', 'warna': 'merah', 'harga': 6000, 'stok': 10}


# menghapus item pada dictionary
print("\nMenghapus item pada dictionary")
del my_dict["status"] # menghapus key "status" beserta value-nya
print(my_dict) # output : {'nama': 'Aldo', 'umur': 21, 'alamat': 'Jakarta'}

my_dict.clear() # menghapus semua item pada dictionary
print(my_dict) # output : {}