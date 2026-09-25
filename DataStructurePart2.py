# Tuple --> Mirip List, tetapi data-data nya tidak bisa berubah
KordinatKecPasarKemis = (-6.1252747854012895, 106.63944652843147)
print("Kordinat kecamatan Pasar Kemis adalah: ", KordinatKecPasarKemis)
print("Latitdue: ", KordinatKecPasarKemis[0])
print("Longitdue: ", KordinatKecPasarKemis[1])

# Jika kita ubah datanya maka akan error
# KordinatKecPasarKemis[0] = 10
# print(KordinatKecPasarKemis[0]) # akan Error karena tupple bersifat immutable(tidak dapat diubah data nya)

# Set --> Mirip List, tapi tidak bisa ada data yang sama dan data di dalam set tidak memiliki posisi yang tetap
# Ex: 
Set_Hobi = {"Berenang", "Renang", "Berenang", "Bermain Gitar", "Renang", "Berenang"}
print(Set_Hobi, len(Set_Hobi)) # Output nya hanya ada 3 karena set tidak bisa ada data yang sama

# Added a value to the set
Set_Hobi.add("Bersepeda")
print(Set_Hobi)

# remove a value from the set
Set_Hobi.pop() #  the pop will remore any one value
print(Set_Hobi)