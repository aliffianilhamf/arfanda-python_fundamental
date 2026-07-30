# Tupple adalah tipe data yang mirip dengan list, namun bersifat immutable (tidak bisa diubah)
# Tupple menggunakan tanda kurung () sedangkan list menggunakan tanda kurung siku []
# Tupple juga bisa menampung banyak item dan banyak tipe data, serta memiliki indeks
# Tupple bisa digunakan untuk menyimpan data yang tidak boleh diubah, misalnya koordinat, data konstan, dsb.


# membuat tupple
my_tupple = ("Aldo", 20, True, 12.8) # tupple yang isinya campuran
numbers = (1, 2, 3, 4) # tupple of integers
hari = ("Senin", "Selasa", "Rabu") # tupple yang terdiri dari string


print(my_tupple)
print(numbers)
print(hari)

# mengakses tupple
print("\nMengakses tupple")
# indeks
print(my_tupple[0]) # output : Aldo
print(numbers[2]) # output : 3
print(hari[-1]) # output : Rabu

# slicing
print(hari[0:2]) # output : ('Senin', 'Selasa')

# unpacking tupple
print("\nUnpacking tupple")
# unpacking tupple adalah proses mengambil nilai dari tupple dan menyimpannya ke variabel
# jumlah variabel harus sama dengan jumlah item pada tupple
nama, umur, *status = my_tupple
# print(f"Nama : {nama}, Umur : {umur}, Status : {status}, Tinggi : {tinggi}")
print(f"Nama : {nama}, Umur : {umur}, Status : {status}")

# mendapatkan panjang tupple
print("\nPanjang tupple")
print(f"Panjang tupple my_tupple : {len(my_tupple)}")
print(f"Panjang tupple numbers : {len(numbers)}")

# looping tupple
print("\nLooping tupple")
for item in my_tupple:
    print(f"Item : {item}")