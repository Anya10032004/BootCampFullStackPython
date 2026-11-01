# This is a comment --> We need to # to make a comment

# Variabel
a = 10
b = a > 10 and "lebih besar" or "lebih kecil"
print(b)

# INGATT:
# Operator Logika AND adalah && (di Java, C, dll)
# Operator Logika AND adalah and (di Python)
# Operator Logika OR adalah || (di Java, C, dll)
# Operator Logika OR adalah or (di Python)

# Loops:
# For loops: Perulangan yang sudah ditentukan jumlahnya
# While loops: Perulangan yang belum ditentukan jumlahnya

# Example:
for a in range(10):
    print(f"This the {a+1}th loop")

kondisiAwal = True
while kondisiAwal:
    print("Looping")
    kondisiAwal = False

# Data Structure:
# List: Kumpulan data yang bisa diubah-ubah --> () 
# Tuple: Kumpulan data yang tidak bisa diubah-ubah(hapus, edit, dll)--> []
# Set: Kumpulan data yang data-datanya tidak memiliki posisi tetap --> {}
# Dictionary: Kumpulan data yang memiliki key dan value --> {key:value}

# Example(of List)
listSiswa = ["Anya", "Budi", "Citra", 122, 187.5]
print(listSiswa[0])
print(listSiswa[3])
print(listSiswa[4])

# untuk mengukur banyak item di list --> len()
print(len(listSiswa))

#To add a new item to a list --> .append(data)
listSiswa.append("Sefanya")
print(listSiswa[5])

#To remove a item from a list --> .remove(data)
listSiswa.remove("Anya")
print(listSiswa[0])

#To check if the data is in the list --> in
print("Budi" in listSiswa)

print(" ")
print(" ")

# Example(of Tuple)
tupleSiswa = ("Anya", "Budi", "Citra", 122, 187.5)
print(tupleSiswa[0])
print(tupleSiswa[3])
print(tupleSiswa[4])

# untuk mengukur banyak item di tuple --> len()
print(len(tupleSiswa))


#To check if the data is in the tuple --> in
print("Budi" in tupleSiswa)


print(" ")
print(" ")

# Set
SetSiswa = {"Anya", "Budi", "Citra", 122, 187.5}

# untuk mengukur banyak item di set --> len()
print(len(SetSiswa))

#To add a new item to a set --> .add(data)
SetSiswa.add("Sefanya")

#To check if the data is in the set --> in
print("Budi" in SetSiswa)

print(" ")
print(" ")

# Function --> To put a block of code together
def functionName():
    print("Hello")

def luasSegitiga(alas, tinggi):
    return 0.5*alas*tinggi

print(luasSegitiga(10, 20))
# alas and tinggi --> parameter
# teh "return" is to return the value(get the value outside the function)
# Without "return" --> 
# With "return" --> can use it in other function or variable 
