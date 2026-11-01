dig = int(input("Masukkan 5 digit : "))
print(f"Input valid : {dig < 100000 and dig > 9999}")
satuan = dig % 10 
puluhan = dig // 10 % 10 
ratusan = dig // 100 % 10 
tribuan = dig // 1000 % 10 
puluhribuan = dig // 10000 % 10
pal = str(satuan)+ str(puluhan) + str(ratusan) + str(tribuan) + str(puluhribuan)
genap = (1 and satuan % 2 == 0 or 0) + (1 and puluhan % 2 == 0 or 0) + (1 and ratusan % 2 == 0 or 0) + (1 and tribuan % 2 == 0 or 0) + (1 and puluhribuan % 2 == 0 or 0) 
print(f"Jumlah Digit: {satuan + puluhan + ratusan + tribuan + puluhribuan}")
print(f"Banyak Digit Genap : {genap}")
print(f"Bilangan Terbalik : {pal}")
print(f"Palindrom : {dig==int(pal)}")
print(f"Bilangan Harshad : {dig % (satuan + puluhan + ratusan + tribuan + puluhribuan) == 0}")
