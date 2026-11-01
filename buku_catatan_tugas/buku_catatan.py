import json

class Catatan():
    def __init__(self, judull, isii):
        self.judul = judull
        self.isi = isii
    
    def tambah(self, file_name = "catatan.json"):
        print("Menambahkan catatan")
        try: # if the file not empty
            with open(file_name, "r") as filee:
                file = json.load(filee)

        except json.JSONDecodeError: # if the file is empty
            file = []

        file.append({"judul": self.judul, "isi": self.isi})
        with open(file_name, "w") as filee:
            json.dump(file, filee, indent = 2)

    
    
while True:
    print("Masukkan Pilihan : ")
    print("1. Tambah Catatan")
    print("2. Lihat Semua Catatan")
    print("3. Keluar")
    pilihan = input("Masukkan Pilihan : ")
    if pilihan == "1":
        judul = input("Masukkan Judul: ")
        isi = input("Masukkan Isi : ")
        catatan = Catatan(judul, isi)
        catatan.tambah("catatan.json")
    elif pilihan == '2':
        try: 
            with open("catatan.json", "r") as filee:
                file = json.load(filee)
            for a in file:
                print("Judul : ", a["judul"])
                print("Isi : ", a["isi"])
                print("-"*10)
        except json.JSONDecodeError: 
            print("json file is empty")
            continue
    elif pilihan == '3':
        print("Keluar")
        break
    else:
        print("Pilihan tidak ada")

    
