"""
    List adalah struktur data di python, yang bisa menampung banyak item, dan banyak tipe data.
    sifatnya immutable (bisa diubah ubah), dan memilik indeks
    """
    
# membuat list
hari = ['Senin', 'Selasa', 'Rabu'] # list yang terdiri dari string
numbers = [1, 2, 3, 4] # list of integers
my_list = ["Aldo", 20, True, 12.8] # list yang isinya campuran 

print(hari)
print(numbers)
print(my_list)

print("\nMengakses list")
# indeks 
print(hari[0]) # outputnya : Senin
print(numbers[2]) # output : 3 
print(my_list[-1]) # output : 12.8
print(my_list[-2]) # output : True

# slicing 
# [start:stop:step]
print(hari[0:2]) # [senin, selasa]
print(my_list[:3]) # ["Aldo", 20, True]
print(my_list[1:3]) # [20, True]
print(my_list[1:]) # ["20, True, 12.8]

""" 
Latihan List
my_list_3 = ["Ratna", 0, 100, 32, False, [99,88], True]

1. Tampilkan item ke 3
2. Dapatkan nilai false dengan negatif indexing 
3. Dapatkan nilai [99,88]
4. Dapatkan nilai [100, 32, False, [99, 88]]
5. Dapatkan Nilai ["Ratna", 100, False, True]
"""

print("\nMengubah value pada list")
my_list2 =["Apel", "Nanas", "Mangga", "Semangka"]
print(my_list2)

# Nanas menjadi Anggur
my_list2[1] = "Anggur"
print(f"List Setelah di ubah : {my_list2}")
my_list2[-1] = "Melon"
print(f"List Setelah di ubah : {my_list2}")

my_list2[1:4] = ["Jambu", "Timun", "Pepaya"]
print(f"List Setelah di ubah : {my_list2}")

print("\nMenambah Item pada List")
# 1. append -> menambahkan item di paling belakang 
numbers = [10, 20, 30, 40 ,50]

print(f"Original list numbers : {numbers}")

numbers.append(60)
print(f"Setelah di append(60) -> {numbers}")
numbers.append(70)
print(f"Setelah di append(70) -> {numbers}")
numbers.append(80)
print(f"Setelah di append(80) -> {numbers}")

# 2. insert 
my_list3 = my_list2.copy() 
print(f"\nOriginal my_list3 : {my_list3}")

my_list3.insert(2, "Semangka")
print(f"Setelah di insert(2, Semangka) -> {my_list3}")
my_list3.insert(4, "Nanas")
print(f"Setelah di insert(4, Nanas) -> {my_list3}")

# 3. extend
print(f"\nOriginal list numbers : {numbers}")
print(f"Original list my_list3 : {my_list3}")

numbers.extend(my_list3)
print(f"Setelah di extend, list numbers : {numbers}")
print(my_list3)

""" 
months = ["Januari", "Mei", "Agustus", "Oktober"]
- Lengkapi list months dengan menambahkan bulan yang kosong menggunakan bahasa inggris (cth, February, March, June, dst)
- Ubah "Januari", "Mei", "Agustus", "Oktober" ke bahasa inggris juga

"""

print("\nMenghapus item pada list")
# pop -> akan menghapus item terakhir kalau indeksnya tidak secara eksplisit di sebutkan
# pop itu akan mengembalikan item yang di hapus
my_list4 = [12, 66, 88, 32]
print(f"Original list my_list4 : {my_list4}")
hasil_pop = my_list4.pop()
print(f"my_list4 setelah di pop() : {my_list4}, yang di pop adalah : {hasil_pop}")
hasil_pop = my_list4.pop(0)
print(f"my_list4 setelah di pop(0) : {my_list4}, yang di pop adalah : {hasil_pop}")

# remove -> menghapus item yang di pilih (bukan indeks)
my_list5 = ["Jono", "Doni", "Adi", "Sofyan"]
print(f"\nOriginal list my_list5 : {my_list5}")
hasil_pop = my_list5.remove("Doni")
print(f"my_list5 setelah di remove(Doni) : {my_list5}, yang di remove adalah : {hasil_pop}")


print("\nLooping pada list")
persons = ["Jono", "Doni", "Adi", "Sofyan"]

# 1. looping dengan for 
indeks = 0
for person in persons : 
    print(f"Nama : {person}, indeks : {indeks}")
    indeks = indeks + 1

# print()    
# number_ganjil = [1, 3, 5, 7, 9]
# for n in number_ganjil:
#     print(f"Number : {n}")
#     if n == 5 : 
#         print("Bingo!")

length_persons = len(persons) # hasilnya = 4
for i in range(length_persons)  : 
    if i >3 : 
        break
    print(f"Nama : {persons[i]}, indeks : {i}")
    
    
months = ["Januari", "Mei", "Agustus", "Oktober"]
# 1. tampilkan item dan indeksnya menggunakan for biasa, dan for range

print()
cars = ["Toyota", "Honda", "Mitsubishi", "Suzuki"]

for car in cars: 
    print(f"Nama Mobil : {car}")
    

print()

nilai = [70, 80, 90, 100, 60, 70, 80, 90, 100, 60, 70, 80, 90, 100, 60]

nilai_lulus = [] # nilai lulus, kalau nilanya lebih dari 70, maka masuk ke list ini

for n in nilai :
    if n > 70:
        nilai_lulus.append(n)
   
# iterasi 1 : nilai_lulus = []
# iterasi 2 : nilai_lulus = [80]
# iterasi 3 : nilai_lulus = [80, 90]
# .......
# iterasi 15 : nilai_lulus = [80, 90, 100, 80, 90, 100, 80, 90, 100]  
print(f"Nilai Lulus : {nilai_lulus}")


print()
kontak_kotor = ["Aldo", "Doni", "Adi", "Sofyan", "Doni", "Adi", "Sofyan"]
kontak_bersih = [] # kontak yang bersih, tidak ada duplikat

for nama in kontak_kotor : 
    if nama not in kontak_bersih:
        kontak_bersih.append(nama)

# iterasi 1 : kontak_bersih = ["Aldo"]
# iterasi 2 : kontak_bersih = ["Aldo", "Doni"]
# iterasi 3 : kontak_bersih = ["Aldo", "Doni", "Adi"]
# iterasi 4 : kontak_bersih = ["Aldo", "Doni", "Adi", "Sofyan"]
# iterasi 5 : kontak_bersih = ["Aldo", "Doni", "Adi", "Sofyan"]
# iterasi 6 : kontak_bersih = ["Aldo", "Doni", "Adi", "Sofyan"]
# iterasi 7 : kontak_bersih = ["Aldo", "Doni", "Adi", "Sofyan"]
print(f"Kontak bersih : {kontak_bersih}")


numbers = [10, 20, 30, 40 ,50]
# cari total perkalian dari semua item di list numbers
w = 1
for number in numbers : 
    w = w * number 
    
    

# algoritma perkalian list 
# 0. 1 * 10 = w
# 1. w * 20 = x
# 2. x * 30 = y 
# 3. y * 40 = z
# 4. z * 50 = a

# 0. x = 1 * 10 = 10
# 1. x = x * 20  = 200
# 2. x = x * 30  = 6000
# 3. x = x * 40 
# 4. x = x * 50 
print()
numbers = [10, 20, 30, 40 ,50]
x = 1
for number in numbers:
    x = x * number
    
    
# iterasi pertama : x awal = 1, number = 10, 1 * 10 = 10,x akhir = 10
# iterasi kedua : x awal = 10, number = 20, 10 * 20 = 200, x akhir = 200
# iterasi ketiga : x awal = 200, number = 30, 200 * 30, x akhir = 6000
# dst
print(f"Hasilnya x : {x}")

