# Set adalah struktur data di python, yang bisa menampung banyak item, dan banyak tipe data.
# Set bersifat mutable (bisa diubah ubah), namun tidak memiliki indeks, dan tidak bisa menampung item yang sama (unique item)
# Set menggunakan tanda kurung kurawal

# membuat set
my_set = {1, 2, 3, 4, 5} # set of integers
my_set2 = {"Aldo", 20, True, 12.8} # set yang isinya campuran
my_set3 = {"Aldo", "Budi", "Caca", "Deni", "Aldo"} # set yang isinya string, namun ada item yang sama (Aldo), maka akan dihapus

print(my_set)
print(my_set2)
print(my_set3) # output : {'Aldo', 'Budi', 'Caca', 'Deni'} -> item yang sama (Aldo) dihapus

# mengakses set
print("\nMengakses set")
# looping set
for item in my_set3:
    print(f"Item : {item}")
    

# menambahkan item pada set
print("\nMenambahkan item pada set")
my_set.add(6) # menambahkan item 6 pada set my_set
print(f"Set setelah ditambahkan item 6 : {my_set}")

