# for loop, sama dengan while loop, sama sama digunakan untuk melakukan perulangan
# Range 
for angka in range(10): # range(stop)
    print(f"Perulangan ke-{angka}")
    
print()
for indeks in range(2,10): # range(start, stop)
    print(f"Perulangan ke-{indeks}")
    
print()
for i in range(10, 0, -1): # range(start, stop, step)
    print(f"Perulangan ke-{i}")


print()
# list 
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis']

for item in hari:
    print(item)
    
for indeks, item in enumerate(hari):
    print(f"{item} itu ada di urutan ke {indeks}")
    

print()
# string 
judul = "Pelangi di Matamu"
count = 0
for karakter in judul :
    if karakter in 'aiueo' :
        print(karakter)
        count = count + 1
       
print(f"count huruf konsonan : {count}")