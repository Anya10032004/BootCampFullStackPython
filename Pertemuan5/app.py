from flask import Flask, jsonify, request
import json
from datetime import datetime


app = Flask(__name__)



#Pembuatan Class Note 


# class Notes():
#     def __init__(self, id_note, deskripsi, status):
#         id_note = id_note
#         deskripsi = deskripsi
#         status = status
#         create_at = datetime.now()
#         delete_at = None
#         update_at = None
    

#     #Buat method untuk menyimpan ke dalam database 
#     def save_data(data):
#         with open("catatan.json", "w") as f:
#             json.dump(data, f)
    
#     def info(self):
#         return {
#             "id_note": self.id_note,
#             "deskripsi": self.deskripsi,
#             "status": self.status,
#             "create_at": self.create_at,
#             "delete_at": self.delete_at,
#             "update_at": self.update_at,
#         }


#read 
@app.route("/", methods = ["GET"])
def beranda ():    
    return "Hallo Ini Merupakan System API REST"


#Pembuatan CRUD untuk API REST
# Create 


# Read ALl 
@app.route("/get_note", methods = ["GET"])
def getRoute():
    with open("catatan.json", "r") as f:
        data = json.load(f)
    
    return jsonify({
        "status":200,
        "message": "Data Berhasil Di Ambil",
        "data": data
    }) 

# Get By ID 
@app.route("/get_note_by_id/<int:id_note>", methods = ["GET"])
def getNoteByID(id_note):
    ##membuka Json Database
    with open("catatan.json", "r") as f:
        data = json.load(f)
        #Mencari data berdasarkan ID yang di input 

    #Kita harus membalikan 404 apabila data tidak di temukan dan kalau kosong kita harus balikan nilai 400 
    if id_note == 0:
        return jsonify({

            "status":400,
            "message": "Id Tidak Boleh 0",
        }), 400
    else:
        # Kita akan melakukan sebuah perulangan untuk mencari data berdasarkan ID yang di input 
        for data in data:
            if data["id_note"] == id_note:
                return jsonify({
                    "status":200,
                    "message": "Data Berhasil Di Ambil",
                    "data": data
                })
        # Apabila data tidak di temukan maka akan di kembalikan nilai 404
        return jsonify({
            "status":404,
            "message": "Data Tidak Di Temukan",
        }), 404

@app.route("/create_note", methods=["POST"])
def createNote():
    ## Membuka Json Database dengan penanganan jika file kosong
    try:
        with open("catatan.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        data_lama = []

    ## Menerima Data 
    data = request.get_json()
    id_note = data["id_note"]
    deskripsi = data["deskripsi"]
    status = data["status"]
    
    data_baru = {"id_note": id_note, "deskripsi": deskripsi, "status": status}   
    
    # Append Data 


    data_lama.append(data_baru)

    # Simpan kembali ke dalam Database (uncomment bagian ini)
    with open("catatan.json", "w") as f:
        json.dump(data_lama, f, indent=4)

    return jsonify({
        "status": 201,
        "message": "Data Berhasil Di Tambahkan",
        "data": data_baru
    }), 201


# Update 

@app.route("/update_note/<int:id_note>", methods=["PUT"])
def updateNote(id_note):
    # Validasi ID
    if id_note == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400

    ## Membuka Json Database
    try:
        with open("catatan.json", "r") as f:
            daftar_catatan = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        daftar_catatan = []

    ## Menerima Data JSON dari request
    req_data = request.get_json() or {}

    # Melakukan perulangan untuk mencari data berdasarkan ID yang diinput
    for catatan in daftar_catatan:
        if catatan["id_note"] == id_note:
            # Merubah data (bisa fleksibel sesuai input atau default "DONE")
            if "deskripsi" in req_data:
                catatan["deskripsi"] = req_data["deskripsi"]
            if "status" in req_data:
                catatan["status"] = req_data["status"]
            else:
                catatan["status"] = "DONE"

            ## Simpan seluruh daftar catatan kembali ke database
            with open("catatan.json", "w") as f:
                json.dump(daftar_catatan, f, indent=4)

            return jsonify({
                "status": 200,
                "message": "Data Berhasil Diperbarui",
                "data": catatan
            }), 200

    # Apabila data tidak ditemukan
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404




@app.route("/delete_note/<int:id_note>", methods=["DELETE"])
def deleteNote(id_note):
    # Validasi ID
    if id_note == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400

    ## Membuka Json Database
    try:
        with open("catatan.json", "r") as f:
            daftar_catatan = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        daftar_catatan = []

    # Melakukan perulangan untuk mencari data berdasarkan ID yang diinput
    for catatan in daftar_catatan:
        if catatan["id_note"] == id_note:
            # Hapus catatan dari list
            daftar_catatan.remove(catatan)

            ## Simpan seluruh daftar catatan kembali ke database
            with open("catatan.json", "w") as f:
                json.dump(daftar_catatan, f, indent=4)

            return jsonify({
                "status": 200,
                "message": "Data Berhasil Dihapus",
                "data": catatan
            }), 200

    # Apabila data tidak ditemukan
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404



        

if __name__ == "__main__":
    app.run(debug=True)