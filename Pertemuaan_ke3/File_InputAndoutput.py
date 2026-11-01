# Fungsi open(a, b) --> to open file
#  a --> name of file
#  b --> w: write
#        a: append
#        r: read
#        x: create
#        t: text mode
#        b: binary mode
# Example 1: dengan 'with' --> automatically close file
import json
# ============================================================
# BAGIAN 1: Menulis & Membaca Data Sederhana (contoh.json)
# ============================================================

# 1. Definisikan data dictionary terlebih dahulu
contoh = {
    "nama": "Budi",
    "nilai": 85
}

# 2. MENULIS dictionary ke file JSON(contoh.json akan otomatis terbuat file nya)
#  indent=2 agar rapi & mudah dibaca
with open("contoh.json", "w") as f: # f adalah variabel yang digunakan untuk mewakili file yang sedang dibuka
    json.dump(contoh, f, indent=2)  
print("-> data ditulis ke contoh.json")

# 3. MEMBACA kembali dari file JSON
with open("contoh.json", "r") as f:
    hasil = json.load(f)

print(f"-> data dibaca kembali : {hasil}")
print(f"   ambil satu key       : {hasil['nama']}\n")


# ============================================================
# BAGIAN 2: Contoh untuk DatabaseSiswa (List of Dictionaries)
# ============================================================

# 1. Siapkan data siswa (list berisi beberapa dictionary siswa)
database_siswa = [
    {"nis": "1001", "nama": "Andi", "kelas": "10A", "nilai": 88},
    {"nis": "1002", "nama": "Siti", "kelas": "10B", "nilai": 92},
    {"nis": "1003", "nama": "Budi", "kelas": "10A", "nilai": 85}
]

# 2. Simpan ke file JSON(database_siswa.json akan otomatis terbuat file nya))
with open("database_siswa.json", "w") as f:
    json.dump(database_siswa, f, indent=2)
print("-> Database siswa berhasil disimpan ke database_siswa.json")

# 3. Baca kembali data siswa dari file JSON
with open("database_siswa.json", "r") as f:
    data_terbaca = json.load(f)

print("-> Isi Database Siswa:")
for siswa in data_terbaca:
    print(f"   - {siswa['nis']} | {siswa['nama']} | Nilai: {siswa['nilai']}") 
