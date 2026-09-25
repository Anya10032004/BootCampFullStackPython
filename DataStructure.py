# Data Structure:
# - List
# - Dictionary
# - Tuple
# - Set

# List:
# Ex:
list_nilai_ujian = [80, 90, 75, 85, 95]
list_nama_mahasiswa = ["Anya", "Budi", "Citra", "Dewi", "Eko"]
print("List Nilai Ujian: ", list_nilai_ujian)
print("List Nama Mahasiswa: ", list_nama_mahasiswa)

# Using loops
for a in list_nama_mahasiswa:
    print(f"Nama Mahasiswa: {a}")
    
# Edit data
list_nama_mahasiswa[0] = "Anisa"
print("Nama mahasiswa ke 1 adalah: ", list_nama_mahasiswa[0])

# Add data
list_nama_mahasiswa.append("Fira")
print("Data setelah ditambahkan: ", list_nama_mahasiswa)

# Remove data
list_nama_mahasiswa.remove("Budi")
print("Data setelah dihapus: ", list_nama_mahasiswa)

print(" ")
print(" ")
print("==================================")
print(" ")
print(" ")

#Dictionary:
# Ex:
data_mahasiswa = {
    "nama": "Andi", 
    "NPM": "123456", 
    "umur": 19,
    "Jurusan": "Teknik Informatika",
    "Universitas": "Universitas Mercu Buana",
    "status_menikah": False
    }
# Terdiri dari 2 hal, yaitu value and key(untuk mengakses si value)
# key: "nama", "NPM", "Jurusan", "umur", "Universitas", "status_menikah"
# value: "Andi", "123456", "Teknik Informatika", 19, "Universitas Mercu Buana", False

# Dictionary is an important for Json format file
# JSON stands for JavaScript Object Notation. It's just a simple,
# text-based way to structure data so both humans and computers can read it easily.

# Let's access one of the value
print(data_mahasiswa["nama"]) # to get the name, Andi
print(data_mahasiswa["NPM"])  # ti get his NPM number, 123456


# We can add a dictionary as a value inside a dictionary
hobybagja = [{
    "id_hobi": 1,
    "nama_hobi": "Bermain Gitar",
    "keterangan": "Bisa main gitar"
},
{
    "id_hobi": 2,
    "nama_hobi": "Renang",
    "keterangan": "Bisa berenang"
}
]
Profilbagja = {
    "nama": "Bagja",
    "NPM": "123456",
    "umur": 19,
    "Jurusan": "Teknik Informatika",
    "Universitas": "Universitas Mercu Buana",
    "status_menikah": False,
    "hobybagja": hobybagja
}

print(Profilbagja)

# Edit the dictionary
Profilbagja["nama"] = "Anya"
print(Profilbagja["nama"])

# menambah item di dalam dictionary
Profilbagja["agama"] = "Kristen Protestan"
print(Profilbagja["agama"])

# menghapus item di dalam dictionary
del Profilbagja["agama"]

# mengakses dictionary nested
print(Profilbagja["hobybagja"][0]["nama_hobi"])
print(Profilbagja["hobybagja"][1]["nama_hobi"])

# Memperbagus format
import pprint
pprint.pprint(Profilbagja)
