# Entity User: 
# With the data: id_user, username, email, password, role, 
# create_user OK
# get_id OK
# get_all OK
# update_data OK
# delete_data OK
# created_at
# updated_at
# deleted_at

# NOTEE:
# Untuk mengetest flow API kamu lebih baik pakai postman daripada pakai browsers, 
# terutama jika butuh input dari user

# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

# Check aja
@app.route('/', methods = ["GET"])
def main():
    return "API WORK YEYYYYYYY"

# Create
@app.route("/create_user", methods=["POST"])
def create_user():

    # Open the database user(user.json)
    try:
        with open("user.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        data_lama = []

    ## Get the data sent by the user
    data = request.get_json() 
    id_user = data["id_user"]
    username = data["username"]
    email = data["email"]
    password = data["password"]
    role = data["role"]
    created_at = datetime.now().isoformat() # .isformst() untuk mengkonversikan nya menjadi string
    updated_at = datetime.now().isoformat() # .isformst() untuk mengkonversikan nya menjadi string
    
    # Check if the user id is already exists
    for a in data_lama:
        if a['id_user'] == id_user:
            return jsonify({
                "status": 400,
                "message": f"Id {id_user} sudah ada",
            }), 400
    
    # Check if the user id is equal to zero
    if id_user == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    
    data_baru = {
        "id_user": id_user, 
        "username": username, 
        "email": email, 
        "password": password, 
        "role": role, 
        "created_at": created_at, 
        "updated_at": updated_at
        }   
    
            
    # Append Data 
    data_lama.append(data_baru)

    # Save back to the database 
    with open("user.json", "w") as f:
        json.dump(data_lama, f, indent=4)

    # Send response
    return jsonify({
        "status": 200,
        "message": "Data Berhasil Di Tambahkan",
        "data": data_baru
    }), 200

# Read 
# Get by ID
@app.route("/read_user/<int:user_id>", methods=["GET"])
def read_user(user_id):
    # Open the database user(user.json)
    try:
        with open("user.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong"
        }), 404

    # if the id equals to zero
    if user_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400
    
    # if the user id is found
    for d in data_lama:
        if d['id_user'] == user_id:
            return jsonify({
                "status": 200,
                "message": "Data Berhasil Di Baca",
                "data": d
            }), 200

    # if the user is not found
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404

# Read all of them
# Get user's list
@app.route("/read_user_list", methods=["GET"])
def read_user_list():
    # Open the database user(user.json)
    try:
        with open("user.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404
    # for d in data_lama:
    #     print(f"{d['id_user']} | {d['username']} | {d['email']} | {d['password']} | {d['role']}")
    
    
    return jsonify({
        "data": data_lama,
        "status": 200,
        "message": "Data Berhasil Di Tampilkan",
    }), 200

@app.route("/update_user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Read the Database
    try:
        with open("user.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404

    if user_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400 


    # the data input from user
    new_input = request.get_json() or {}

    for c in data_lama:
        if c['id_user'] == user_id:
            if "username" in new_input:
                c["username"] = new_input["username"]
            if "email" in new_input:
                c["email"] = new_input["email"]
            if "password" in new_input:
                c["password"] = new_input["password"]
            if "role" in new_input:
                c["role"] = new_input["role"]
            c["updated_at"] = datetime.now().isoformat()
                
            # Save back to the database
            with open("user.json", "w") as f:
                json.dump(data_lama, f, indent=4)
            
            return jsonify({
                "status": 200,
                "message": "Data Berhasil Di Update",
                }), 200
        
    # if the user is not found
    return jsonify({
        "status": 404,
        "message": "Data Tidak Di Temukan",
    }), 404

@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id): 
    # Validate the id
    if user_id == 0:
        return jsonify({
            "status": 400,
            "message": "Id Tidak Boleh 0",
        }), 400 
    
    # Read the Database
    try:
        with open("user.json", "r") as f:
            data_lama = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return jsonify({
            "status": 404,
            "message": "Database Kosong",
        }), 404

    # Iterate the user data
    for c in data_lama:
        if c['id_user'] == user_id:
            # Remove the data
            data_lama.remove(c)
            
            # Save back to the database
            with open("user.json", "w") as f:
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
    



    
    