# Fungsi adalah blok kode yang dapat digunakan kembali yang membantu dalam mengorganisir kode serta membuatnya lebih modular dan memudahkan pemeliharaan.
# Untuk membuat sebuah fungsi, kita menggunakan kata kunci def, diikuti nama fungsinya.
# fungsi itu ada dua tipe : 1. tipe void (tidak mengembalikan nilai) dan 2. tipe return (mengembalikan nilai).

print("Fungsi tipe void") 
def sapa(): 
    print("Halo, selamat datang di kelas Python!")
    print("ini dari fungsi sapa")
    
print("ini dari luar fungsi sapa")
    
# setelah membuat fungsi, kita dapat memanggilnya dengan menuliskan nama fungsinya diikuti tanda kurung.
sapa() # output : Halo, selamat datang di kelas Python!

def jumlah():
    a = 20
    b = 50
    print(f"hasil penjumlahan dari {a} + {b} = {a+b}")
    
    
jumlah() # output : hasil penjumlahan dari 20 + 50 = 70


print("\nFungsi tipe return")
def sapa_return():
    return "Halo, selamat datang di kelas Python!"


# kita dapat menyimpan nilai yang dikembalikan oleh fungsi ke dalam sebuah variabel.
pesan = sapa_return()
print(pesan) # output : Halo, selamat datang di kelas Python!

def jumlah_return():
    a = 20
    b = 50
    c = a + b
    return c


hasil_jumlah = jumlah_return()
# hasil_jumlah = 70
print(f"hasil penjumlahan dari 20 + 50 = {hasil_jumlah}") # output : hasil penjumlahan dari 20 + 50 = 70
print(f"hasil penjumlahan dari 20 + 50 = {jumlah_return()}") # output : hasil penjumlahan dari 20 + 50 = 70


# Latihan soal 
# 1. Buat fungsi yang tipenya void untuk menampilkan pesan "ini dari fungsi yang saya buat"
# 2. Buat fungsi yang tipenya return untuk mengembalikan nilai Luas persegi panjang dengan panjang 10 dan lebar 5 (p x l)


# Parameter : adalah sebuah variabel yang digunakan untuk menyimpan sebuah nilai yang dikirimkan ke dalam fungsi.
# sehingga ini menjadikan fungsi lebih fleksibel, karena kita dapat mengirimkan nilai yang berbeda - beda ke dalam fungsinya
# parameter di tulis di dalam tanda kurung setelah nama fungsi. Parameter dapat memiliki nilai default, sehingga jika tidak ada nilai yang dikirimkan, maka parameter akan menggunakan nilai defaultnya.

print("\nFungsi tipe void dengan parameter")
def sapa_saya(nama):
    print(f"Halo {nama}, selamat datang di kelas Python!")
    
    
# memanggil fungsi denganmengirimkan data ke parameter 

sapa_saya("Budi") # output : Halo Budi, selamat datang di kelas Python!
sapa_saya("Aldo") # output : Halo Aldo, selamat datang di kelas Python!
sapa_saya("Rina") # output : Halo Rina, selamat datang di kelas Python!

print("\nFungsi tipe return dengan parameter")
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# memanggil fungsi dengan mengirimkan data ke parameter
hasil_luas = luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang dengan panjang 10 dan lebar 5 adalah {hasil_luas}") 

hasil_luas2 = luas_persegi_panjang(7, 3)
print(f"Luas persegi panjang dengan panjang 7 dan lebar 3 adalah {hasil_luas2}")



# latihan soal
# 1. Buat fungsi yang tipenya void dengan parameter "nama" dan "alamat", untuk menampilkan pesan "Halo nama, selamat datang di alamat"

# 2. Buat fungsi yang tipenya return dengan parameter "bilangan", untuk mengembalikan nilai kuadrat dari bilangan tersebut (bilangan * bilangan atau bilangan ** 2)

# default parameter : 
print("\nFungsi dengan default parameter")
def greet(nama, alamat="Semarang"):
    print(f"Halo {nama}, selamat datang di {alamat}!")
    
    
    
greet("Budi") # output : Halo Budi, selamat datang di Semarang!
greet("Aldo", "Jakarta") # output : Halo Aldo, selamat datang di Jakarta!
greet("Rina", "Bandung") # output : Halo Rina, selamat datang di Bandung!

# keyword argument :
print("\nFungsi dengan keyword argument")
def greet_keyword(nama, alamat):
    print(f"Halo {nama}, selamat datang di {alamat}!")
    
# memanggil fungsi dengan keyword argument
greet_keyword(alamat="Jakarta", nama="Aldo") # output : Halo Aldo, selamat datang di Jakarta!
greet_keyword(nama="Rina", alamat="Bandung") # output : Halo Rina, selamat datang di Bandung!

# latihan soal 
# 1. Buat fungsi dengan default parameter "nama" dan "alamat", untuk menampilkan pesan "Halo nama, selamat datang di alamat". Jika tidak ada nilai yang dikirimkan, maka nama akan menggunakan nilai default "Anonim" dan alamat akan menggunakan nilai default "Semarang".

# 2. buat fungsi dengan keyword argument "nama", "hobi", dan "umur", untuk menampilkan pesan "Halo nama, umur tahun, hobi hobi". Panggil fungsi tersebut dengan mengirimkan nilai ke parameter dengan menggunakan keyword argument.