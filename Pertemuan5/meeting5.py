import requests_oauthlib
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Pembuatan class Notes untuk mempermudah dalam proses CRUD
# class Notes(id_note, desc, status):
#     def __init__(self, id_note, desc, status):
#         self.id_note = id_note
#         self.desc = desc
#         self.status = status
    
#     def save_data(data):
#         with open("catatan,json", "w") as f:
#             json.dump(data, f)
        
    
#     def to_dict(self):
#         return {
#             "id_note": self.id_note,
#             "desc": self.desc,
#             "status": self.status}

@app.route("/", methods = ["GET"])
def main():
    return "Try yukk:"

# Pembuatan CRUD untuk REST API
# Read
@app.route('/get_note', methods = ["GET"])
def get_notes():
    with open("catatan.json", "r") as f:
        data = json.load(f)
    
    return jsonify({"notes" : data})

# Get By ID
@app.route('/get_note/<id_notes>', methods = ["GET"])
def get_note_by_id(id_notes):

    # Getting the json database
    with open("catatan.json", "r") as ff:
        data = json.load(ff)
        # mencari data bedasarkan ID yang di input

    # Kita harus membalikan 404 apabila ID yang diminta tidak ditemukan
    if id_notes == 0:
        return jsonify({
            "pesan" : "data tidak ditemukan",
            "status": 404})
    else:
        for data in data:
            if data["id_notes"] == int(id_notes):
                return jsonify(data)
    
    return jsonify({"pesan" : "data tidak ditemukan",
                    "status" : 404})
    
# Create
@app.route("/create_note", methods = ["POST"])
def create_note():
    with open("catatan.json", "r") as gg:
        data = json.load(gg)
    # Menerima data
    # {
    #     "id_note": 1,
    #     "deskription" : "Hari ini belajar API REST",
    #     "status" : "selesai"
    # }

    # menerima data 
    data_input = request.get_json()
    id_note = data_input["id_note"]
    desc = data_input["deskription"]
    status = data_input["status"]


    if id_note == 0:
        return jsonify({
            "pesan" : "data tidak ada",
            "status": 404})

    if status == "":
        return jsonify({
            "pesan" : "data tidak ada",
            "status": 400})
    
    data_baru = {
        "id_note": id_note,
        "desc": desc,
        "status": status
    }
    data.append(data_baru)
    
    with open("catatan.json", "w") as gg:
        json.dump(data, gg, indent=4)
        


    return jsonify({
        "pesan": "data berhasil ditambahkan",
        "data": data_input
    })
    
# Update
@app.route("/update_note/<int:id_note>", methods=["PUT"])
def updateNote(id_note):
    #membuka Json Database
    try:
        with open("catatan.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    #mencari data berdasarkan ID yang di input

    data_input = request.get_json()
    id_note = data_input["id_note"]
    desc = data_input["deskription"]
    status = data_input["status"]

    #Kita harus membalikan 404 apabila data tidak di temukan
    #dan kalau kosong kita harus balikan nilai 400
    if id_note == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    else:
        # Kita akan melakukan sebuah perulangan untuk mencari data berdasarkan ID yang di input
        for data in data:
            if data["id_note"] == id_note:

                #Untuk merubah data
                data["deskripsi"] = desc or data["deskripsi"]
                data["status"] = status or data["status"]

                return jsonify({
                    "status": 200,
                    "message": "Data Berhasil Di Ambil",
                    "data": data
                })
# Delete
@app.route("/delete_note/<int:id_note>", methods=["DELETE"])
def deleteNote(id_note):
    #membuka Json Database
    try:
        with open("catatan.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    #mencari data berdasarkan ID yang di input

    data_input = request.get_json()
    id_note = data_input["id_note"]
    desc = data_input["deskription"]
    status = data_input["status"]

    if id_note == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    else:
        # Kita akan melakukan sebuah perulangan untuk mencari data berdasarkan ID yang di input
        for data in data:
            if data["id_note"] == id_note:
                data.remove(data)
                return jsonify({
                    "status": 200,
                    "message": "Data Berhasil Di Hapus",
                    "data": data
                })
    
    
if __name__ == "_main_":
    app.run(debug = True)