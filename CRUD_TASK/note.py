# Entity : Note 
# data : id_note, id_user, title, content, 
#  created_at, updated_at, deleted_at

from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# Check aja
@app.route('/', methods = ["GET"])
def main():
    return "This for the note API"

# Create
@app.route("/create_note", methods=["POST"])
def create_note():

    # Open the database note(note.json)
    try:
        with open("note.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        data_lama = []

    ## Get the data sent by the user
    data = request.get_json() 
    id_note = data["id_note"]
    id_user = data["id_user"]
    title = data["title"]
    content = data["content"]

    # Check if the note id is already exists
    for a in data_lama:
        if a['id_note'] == id_note:
            return jsonify({
                "status": 400,
                "message": f"Id {id_note} sudah ada",
            }), 400
    
    # Check if the user id is equal to zero
    if id_note == 0 or id_user == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    
    data_baru = {
        "id_note": id_note, 
        "id_user": id_user, 
        "title": title, 
        "content": content, 
        "created_at": datetime.now().isoformat(), 
        "updated_at": datetime.now().isoformat()}   
    
            
    # Append Data 
    data_lama.append(data_baru)

    # Save back to the database 
    with open("note.json", "w") as f:
        json.dump(data_lama, f, indent=4)

    # Send response
    return jsonify({
        "status": 200,
        "message": "Data Berhasil Di Tambahkan",
        "data": data_baru
    }), 200

# Read 
# Get by ID
@app.route("/read_note/<int:note_id>", methods=["GET"])
def read_note(note_id):
    # Open the database note(note.json)
    try:
        with open("note.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong"
        }), 404

    # if the id equals to zero
    if note_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    
    # if the note id is found
    for d in data_lama:
        if d["id_note"] == note_id:
            return jsonify({
                "status": 200,
                "message": "Data Berhasil Di Baca",
                "data": d
            }), 200

    # if the note is not found
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404

# Read all of them
# Get user's list
@app.route("/read_note_list", methods=["GET"])
def read_note_list():
    # Open the database note(note.json)
    try:
        with open("note.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404
    
    
    return jsonify({
        "data": data_lama,
        "status": 200,
        "message": "Data Berhasil Di Tampilkan",
    }), 200

@app.route("/update_note/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    # Read the Database
    try:
        with open("note.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404

    if note_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400 


    # the data input from user
    new_input = request.get_json() or {}

    for c in data_lama:
        if c['id_note'] == note_id:
            if "title" in new_input:
                c["title"] = new_input["title"]
            if "content" in new_input:
                c["content"] = new_input["content"]
            c["updated_at"] = datetime.now().isoformat()
                
            # Save back to the database
            with open("note.json", "w") as f:
                json.dump(data_lama, f, indent=4)
                
            return jsonify({
                "status": 200,
                "message": "Data Berhasil Di Update",
                "data": c
                }), 200
        
    # if the user is not found
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404

@app.route("/delete_note/<int:note_id>", methods=["DELETE"])
def delete_note(note_id): 
    # Validate the id
    if note_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400 
    
    # Read the Database
    try:
        with open("note.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404

    # Iterate the user data
    for c in data_lama:
        if c['id_note'] == note_id:
            # Remove the data
            data_lama.remove(c)
            
            # Save back to the database
            with open("note.json", "w") as f:
                json.dump(data_lama, f, indent=4)
            
            return jsonify({
                "status": 200,
                "message": "Data Berhasil Di Hapus",
                "data": c
                }), 200
    
    # if the user is not found
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
    



    
    