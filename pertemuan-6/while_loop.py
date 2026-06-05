# number = 1
# while number <= 5 : 
#     print(f"Perulangan ke - {number}")
#     number = number + 1
    
is_lanjut = True

while is_lanjut : 
    is_lanjut = int(input("Apakah mau lanjut (0 / 1)? : "))
    
    if is_lanjut == 1 : 
        print("Kamu memilih lanjut, perulangan akan berjalan lagi.")
        is_lanjut = True
    else : 
        print("Kamu memilih tidak lanjut, perulangan akan stop disini.")
        is_lanjut = False