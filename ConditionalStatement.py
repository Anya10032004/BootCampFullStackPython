# Percabangan if/elif/else
nilai = int(input("Masukan nilai:"))

if nilai == 100: # Seleksi kondisi pertama
    print("Nilai sempurna")
elif nilai >= 80:
    print("Nilai anda A")
elif nilai >= 75:
    print("Nilai anda B")
elif nilai >= 60:
    print("Nilai anda C")
else:
    print("Anda belum lolos")

# Jika menggunakan operator logika
nilaiTugas = int(input("Masukkan nilai Tugas: "))
nilaiAbsensi = int(input("Masukkan nilai Absensi: "))

if nilaiTugas >= 65 and nilaiAbsensi >= 65:
    print("Anda lolos")
else:
    print("Anda tidak lolos")

