# 1. KONVERSI DARI STRING KE INTEGER

angka = "10"
# angka = "alip" # akan error
print("Sebelum typecasting")
print(f"{angka} + 5")
print(type(angka)) # harusnya string

angka = int(angka) # process konversi dari string ke int

print("Sesudah typecasting")
print(type(angka))
print(angka + 5)

# 2. KONVERSI DARI STRING KE BOOLEAN
print("\n")
# nama_depan = "alip"
nama_depan = ""
print("Sebelum di konversi ke boolean")
print(nama_depan)

nama_depan = bool(nama_depan) #proses konversi

print("Sesudah dikonversi ke boolean")
print(nama_depan)

# 3. KONVERSI DARI BOOLEAN KE STRING
is_active = False 
print("\n")
print("Sebelum Konversi ke string")
print(f'isi dari is_active adalah : {is_active}, yang memiliki tipe data : {type(is_active)}')

is_active = str(is_active) # "False"

print("Sesudah Konversi ke string")
print(f'isi dari is_active adalah : {is_active}, yang memiliki tipe data : {type(is_active)}')


# 4. KONVERSI DARI INT/FLOAT KE STRING
number = 10 
print("\n")
print("Sebelum Konversi ke string")
print(f'isi dari number adalah : {number}, yang memiliki tipe data ; {type(number)}')

number = str(number) # "10"

print("Sesudah Konversi ke string")
print(f'''isi dari number adalah : {number},
      
      yang memiliki tipe data ; {type(number)}''')