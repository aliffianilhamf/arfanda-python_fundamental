# Pass
for i in range(5):
    if i % 2 == 1 : 
        # print()
        # pass
        print("Ini adalah bilangan Ganjil")
        
    print(f"Perulangan ke {i + 1}")
    

print()
# Continue 
for i in range(1, 5):
    if i % 2 == 1 : 
        # pass
        continue
    
    print(f"Perulangan ke {i }")
    
# iterasi 1 -> i = 1, i % 2 == 1 (true), continue
# iterasi 2 -> i = 2, i % 2 == 1 (false), print
# iterasi 3 -> i = 3, i % 2 == 1 (true), continue
# iterasi 4 -> i = 4, i % 2 == 1 (false), print

print()
# break
for i in range(1, 100):
    if i == 5 :
        break
    
    print(f"Perulangan ke {i }")


