tt = int(input("tanggal : "))
bulan = int(input("bulan : "))
tahun = int(input("tahun : "))
bul = ("January" and bulan == 1 or "February" and bulan == 2 or "March" and bulan == 3 or "April" and bulan == 4 or "May" and bulan == 5 or "June" and bulan == 6 or "July" and bulan == 7 or "August" and bulan == 8 or "September" and bulan == 9 or "October" and bulan == 10 or "November" and bulan == 11 or "December" and bulan == 12)
jum_hari = bulan == 2 and (tahun % 4 ==0 and tahun % 100 !=0 or tahun % 400 ==0) and 29 or bulan == 2 and 28 or (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11) and 30 or 31
print(f"Tahun kabisat : {tahun % 4 ==0 and tahun % 100 !=0 or tahun % 400 ==0}")
print(f"Jumlah hari : {jum_hari}")
print(f"Tanggal valid {tt>0 and tt<=jum_hari}")

# age = 20

# status = age >= 18 and "Adult" or "Minor"
# print(status)

# print(f"Jumlah hari : {jum_hari}")
