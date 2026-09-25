ulangi = int(input("Masukkan jumlah perulangan: "))
print("Jumlah Looping yaitu adalah: ")

for i in range(ulangi):
    print(i + 1)

should_continue = True
while should_continue:
    n = int(input("Masukkan Angka: "))
    if n <= 0 or n % 2:
        print(n, "Is not a even number or it's a  negative number")
        should_continue = False
    else:
        print(n)
    
        
        